#!/usr/bin/env python3
"""Validate the raw Cangjie Stage-1 *structure*, without falsely declaring semantic V1 verification.

Usage:
  python3 validate_tiexue_stage1.py RESEARCH/CANGJIE/TIEXUECANMING
  python3 validate_tiexue_stage1.py <directory> --source-jsonl <local-private-chapter_records.jsonl>

EPUB-derived full text must NEVER be committed to the public repository.
"""
import argparse
import collections
import json
import pathlib
import re
import sys

try:
    import yaml
except ImportError as exc:
    raise SystemExit("Install PyYAML for this audit: pip install PyYAML") from exc

FILES = {
    "frameworks": "f",
    "principles": "p",
    "cases": "c",
    "counter-examples": "ce",
    "glossary": "g",
}
TASK_RE = re.compile(r"^TX-T(0[1-9]|1[0-8])$")
SRC_RE = re.compile(r"^Text/[A-Za-z0-9_.-]+\.html$")


def issue(issues, code, item, detail=""):
    issues.append({"code": code, "id": item, "detail": detail})


def required_string(rec, field, issues):
    if not isinstance(rec.get(field), str) or not rec[field].strip():
        issue(issues, "invalid_string", rec.get("id"), field)


def required_list(rec, field, issues, pattern=None):
    values = rec.get(field)
    if not isinstance(values, list) or not values or not all(isinstance(v, str) and v.strip() for v in values):
        issue(issues, "invalid_list", rec.get("id"), field)
    elif pattern is not None and not all(pattern.fullmatch(v) for v in values):
        issue(issues, "invalid_list_item", rec.get("id"), field + ": " + repr(values))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source_root", type=pathlib.Path)
    ap.add_argument("--source-jsonl", type=pathlib.Path, default=None,
                    help="Optional private EPUB extraction; enables literal quote validation")
    args = ap.parse_args()
    records = None
    if args.source_jsonl:
        records = {}
        for ln in args.source_jsonl.open(encoding="utf-8"):
            r = json.loads(ln)
            records[r["source_href"]] = r["text"]

    issues = []
    seen = set()
    counts = {}
    tasks = collections.Counter()
    source_refs = set()
    for name, prefix in FILES.items():
        path = args.source_root / "candidates" / f"{name}.md"
        try:
            raw = path.read_text(encoding="utf-8")
            start = re.search(r"(?m)^- id: ", raw)
            if not start:
                raise ValueError("No YAML candidate section")
            entries = yaml.safe_load(raw[start.start():])
            if not isinstance(entries, list):
                raise ValueError("YAML candidates are not a list")
        except Exception as exc:
            issue(issues, "parse_failed", name, str(exc))
            continue
        counts[name] = len(entries)
        for rec in entries:
            if not isinstance(rec, dict):
                issue(issues, "invalid_record", name)
                continue
            ident = rec.get("id")
            if not isinstance(ident, str) or not re.fullmatch(prefix + r"[0-9]+", ident):
                issue(issues, "invalid_id", str(ident), name)
            if ident in seen:
                issue(issues, "duplicate_id", str(ident))
            seen.add(ident)
            required_string(rec, "source_chapter", issues)
            required_string(rec, "source_quote", issues)
            required_list(rec, "tags", issues)
            required_list(rec, "task_ids", issues, TASK_RE)
            if isinstance(rec.get("task_ids"), list):
                tasks.update(v for v in rec["task_ids"] if isinstance(v, str) and TASK_RE.fullmatch(v))
            if isinstance(rec.get("source_quote"), str) and len(rec["source_quote"]) > 30:
                issue(issues, "quote_too_long_for_public_repo", ident)
            source_ref = rec.get("source_locator")
            if not isinstance(source_ref, str) or not SRC_RE.fullmatch(source_ref):
                issue(issues, "invalid_source_locator", ident, str(source_ref))
            else:
                source_refs.add(source_ref)
                if records is not None:
                    if source_ref not in records:
                        issue(issues, "source_not_found", ident, source_ref)
                    elif rec.get("source_quote") not in records[source_ref]:
                        issue(issues, "quote_not_in_source", ident, source_ref)
            if name == "frameworks":
                for field in ["title", "summary", "inputs", "outputs", "steps", "missing_conditions"]:
                    required_string(rec, field, issues)
            elif name == "principles":
                for field in ["title", "summary"]:
                    required_string(rec, field, issues)
            elif name == "cases":
                for field in ["title", "summary", "example_kind", "outcome"]:
                    required_string(rec, field, issues)
                required_list(rec, "bound_to", issues)
            elif name == "counter-examples":
                for field in ["title", "failure_mode", "mechanism"]:
                    required_string(rec, field, issues)
                required_list(rec, "warning_signs", issues)
                required_list(rec, "bound_to", issues)
            elif name == "glossary":
                for field in ["term", "author_definition", "key_distinction", "why_it_matters"]:
                    required_string(rec, field, issues)
    report = {
        "result": "PASS_SCHEMA" if not issues else "FAIL_SCHEMA",
        "semantic_coverage": "NOT_TESTED_BY_THIS_SCRIPT",
        "literal_quote_check": "PERFORMED" if records is not None else "NOT_PERFORMED_SOURCE_UNAVAILABLE",
        "counts": counts,
        "total": sum(counts.values()),
        "distinct_sources": len(source_refs),
        "valid_task_ids": sorted(tasks),
        "issues": issues,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not issues else 1


if __name__ == "__main__":
    sys.exit(main())