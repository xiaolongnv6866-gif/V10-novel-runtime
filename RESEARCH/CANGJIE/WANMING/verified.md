# 《晚明》Stage 1.5 — Triple Verification

> validation_version: task-first-v2。这里的 verified 只表示知识层 V1/V2/V3 通过；**不等于独立 Skill，不等于进入 V10 Runtime**。

- id: wm-v01
  title: 行动资格逐级兑现
  type: narrative-capability
  merged_raw_candidates: [f01,p01,c01,c02]
  task_ids: [WM-T01]
  source_evidence:
    - "第一卷第18章《白——领》"
    - "第一卷第51章《天启驾崩》"
    - "第二卷第13章《组织结构》"
  V1_source_sufficiency:
    passed: true
    reason: |
      跨卷可见：人物先获得工作/信用，再有资本、官面身份、人员与组织；“一万多两凭什么争霸”直接把目标与当前资格分开。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：一名低身份主角刚获得一次性财富，却想立刻指挥数百人。演练要求列出当前已有资格、缺失桥梁、下一阶段可合法取得的两项资源，并禁止一步跳到最终权力。输出可明确核验是否闭合。
  V3_task_utility:
    passed: true
    expected_benefit: |
      能直接阻止“有钱=有兵=有权”的跳级，稳定前期成长因果。
  decision: verified

- id: wm-v02
  title: 反馈—筛选—规则修改的组织学习闭环
  type: narrative-capability
  merged_raw_candidates: [f02,p03,c04]
  task_ids: [WM-T02]
  source_evidence:
    - "第二卷第38章《总结会》"
  V1_source_sufficiency:
    passed: true
    reason: |
      原文完整展示基层提出、上级筛选、会议争论、主官裁决以及会后修改，机制链条在单章内闭合。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：一次护送任务结束后出现迟到、物资损耗和角色冲突。演练可按“基层事实→合并重复→讨论代价→规则修改→下次检查点”输出复盘单；完成标准明确。
  V3_task_utility:
    passed: true
    expected_benefit: |
      把失败/成功经验转为组织记忆，避免复盘只成为对白或作者总结。
  decision: verified

- id: wm-v03
  title: 规模触发的组织重构
  type: narrative-capability
  merged_raw_candidates: [f03,p02,c07,ce01]
  task_ids: [WM-T03]
  source_evidence:
    - "第五卷第3章《钱庄总部》"
    - "第五卷第36—37章"
    - "第五卷第153章《民事官》"
  V1_source_sufficiency:
    passed: true
    reason: |
      文本明确说“组织结构也到了调整的时候”，之后再次因地域扩大出现反应速度瓶颈，证明不是一次性设定。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：一个组织从1个据点50人扩到6个据点800人。演练先找旧结构瓶颈，再决定是否增加层级/部门，并要求每个新增单元对应一个已出现的具体负荷。
  V3_task_utility:
    passed: true
    expected_benefit: |
      防止为了显得庞大而堆部门，也防止数万人仍靠开局三个人直接管理。
  decision: verified

- id: wm-v04
  title: 信息分流与决策优先级
  type: narrative-capability
  merged_raw_candidates: [f04,p04]
  task_ids: [WM-T02,WM-T03]
  source_evidence:
    - "第五卷第16章《文登军报》"
  V1_source_sufficiency:
    passed: true
    reason: |
      单章完整给出文件分类、按紧急/重要排序、附处理意见再上报的运行方式。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：同日到达12条商业、民事、人员和风险消息。演练输出“立即裁决/委派/例行记录/补信息”四类，并为需要领导裁决者附一行建议。
  V3_task_utility:
    passed: true
    expected_benefit: |
      减少主角成为全知信息中心，并提供多线世界状态进入场景的自然接口。
  decision: verified

- id: wm-v05
  title: 职责—资源—问责的权力契约
  type: narrative-capability
  merged_raw_candidates: [f05,p05]
  task_ids: [WM-T03]
  source_evidence:
    - "第五卷第36章《军——政》"
    - "第五卷第37章《新气象》"
  V1_source_sufficiency:
    passed: true
    reason: |
      部门职责、任命权、预算/资源、考绩与替换都在原文中出现，可重建“权力不是官名”的完整机制。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：设计一个地方建设主管。演练必须给出其可调用资源、必须交付结果、不可越界事项、向谁协调、失败后的问责；缺一项即不完成。
  V3_task_utility:
    passed: true
    expected_benefit: |
      能把权力写成可执行关系，而不是“升官后大家自然听话”。
  decision: verified

- id: wm-v06
  title: 方向上收、专业执行下放
  type: narrative-capability
  merged_raw_candidates: [f06,p06,c08]
  task_ids: [WM-T02,WM-T05]
  source_evidence:
    - "第五卷第145章《真正的利益》"
    - "第五卷第37章《新气象》"
  V1_source_sufficiency:
    passed: true
    reason: |
      原文明确揭示大战后建设并非陈新逐项安排，而由各司和参谋按既有职责推进。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：成熟组织要在主角离场三天时完成一次迁建。演练只允许主角给目标、期限、红线；细化方案必须由相关岗位产生，并注明审批点。
  V3_task_utility:
    passed: true
    expected_benefit: |
      直接削弱“主角发现—主角方案—众人执行”的单中心因果。
  decision: verified

- id: wm-v07
  title: 中央瓶颈后的地方分权与试点
  type: narrative-capability
  merged_raw_candidates: [f07,p08,c09]
  task_ids: [WM-T03,WM-T11]
  source_evidence:
    - "第五卷第153章《民事官》"
  V1_source_sufficiency:
    passed: true
    reason: |
      同章同时给出旧结构迟缓、新地方层级、权限需求与“最好试点”的条件，来源充分。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：三个远端据点的普通事务等待总部批复过久。演练需划出可下放事项、保留中央事项、试点范围、回收指标和扯皮接口。
  V3_task_utility:
    passed: true
    expected_benefit: |
      为扩张期的权力下放提供可检验路径，而不是一道命令突然完成地方治理。
  decision: verified

- id: wm-v08
  title: 适应性对手与世界反馈
  type: narrative-capability
  merged_raw_candidates: [f08,p13,c11]
  task_ids: [WM-T05]
  source_evidence:
    - "第三卷第29章《战——后》"
    - "第五卷第209章《阴——险》"
  V1_source_sufficiency:
    passed: true
    reason: |
      对手在意外结果后明确重新评估威胁；后续章节继续表现对登州方法的针对性反应。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：主角首次用新组织方式赢得局部竞争。演练从对手掌握的信息出发，写出至少两项下一步调整和一项可能误判，禁止复制旧行为。
  V3_task_utility:
    passed: true
    expected_benefit: |
      维持世界独立性，使主角成功真正改变后续博弈。
  decision: verified

- id: wm-v09
  title: 成功同时生成收益与新约束
  type: narrative-capability
  merged_raw_candidates: [f09]
  task_ids: [WM-T06]
  source_evidence:
    - "第五卷第145章《真正的利益》"
    - "第六卷第42章《委员会》"
  V1_source_sufficiency:
    passed: true
    reason: |
      文本把胜利转成声望、信用、土地和政治资本，同时写朝廷戒心、盟友重新估价和内部利益上升。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：角色完成一次高声望事件。演练必须同时列出“立即收益、被谁重新估价、新责任、暴露面、下一层约束”，不能只发奖励。
  V3_task_utility:
    passed: true
    expected_benefit: |
      为长篇连续升级提供内生冲突，不需要每次靠新反派凭空登场。
  decision: verified

- id: wm-v10
  title: 微观生活仪表盘与社会成本穿透
  type: narrative-capability
  merged_raw_candidates: [f10,p11,p12,c05,c06,ce06]
  task_ids: [WM-T07]
  source_evidence:
    - "第二卷第25—26章"
    - "第五卷第68章《畿——南》"
  V1_source_sufficiency:
    passed: true
    reason: |
      住房、工资、节庆、孩子上学与伤亡后退学都直接出现，正反两面证据完整。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：一个改革让粮食供应和治安改善，但增加征役。演练不能写“民心提升”，而要选3个家庭/生活指标表现收益，再选1个指标表现成本。
  V3_task_utility:
    passed: true
    expected_benefit: |
      解决宏观制度只剩旁白和数字的问题，让社会变化可感。
  decision: verified

- id: wm-v11
  title: 宏观任务线与日常生活线交替
  type: narrative-capability
  merged_raw_candidates: [f11]
  task_ids: [WM-T08]
  source_evidence:
    - "第二卷第25—27章"
    - "第三卷第20章《百——态》"
    - "第六卷第2—6章"
  V1_source_sufficiency:
    passed: true
    reason: |
      跨卷反复出现大战/建设前后的过年、街坊、家庭和私人生活段，并承担人物目标与代价信息；非单一偶然场景。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：连续6章均为政治/组织推进。演练要求找出一个已经被宏观变化影响的私人关系或生活需求，插入一场会改变后续判断的生活场景；纯“休息章”不算完成。
  V3_task_utility:
    passed: true
    expected_benefit: |
      降低长篇任务链疲劳，同时给宏观选择提供私人重量。
  decision: verified

- id: wm-v12
  title: 多位置有限信息拼接重大事件
  type: narrative-capability
  merged_raw_candidates: [f12]
  task_ids: [WM-T09]
  source_evidence:
    - "第三卷第17—21章"
    - "第三卷己巳战争段"
  V1_source_sufficiency:
    passed: true
    reason: |
      同一危机连续切换边关、京师、敌军、难民、情报人员和主角，每方只掌握局部信息，结构证据充足。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：一场城市危机同时涉及地方官、商人、普通家庭和对手。演练建立“每个视角知道/不知道什么、能做什么、何时相撞”的场景表；任何单视角知道全部信息即失败。
  V3_task_utility:
    passed: true
    expected_benefit: |
      适合战争和政治大事件，提升悬念并防作者知识直接侵入人物意识。
  decision: verified

- id: wm-v13
  title: 高潮后的后果持续结算
  type: narrative-capability
  merged_raw_candidates: [f13,p14]
  task_ids: [WM-T10]
  source_evidence:
    - "第三卷第29—31章"
    - "第四卷第107章《战后登州》"
    - "第五卷第57章《静夜伤逝》"
  V1_source_sufficiency:
    passed: true
    reason: |
      多个重大事件后均继续写伤员、资源、声望、敌方反应、家庭与政治处置，重复性足够。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：一场行动取得胜利。演练至少结算人员、资源、关系/政治、普通生活四类中的三类，并指出其中哪一项会成为下一场景输入。
  V3_task_utility:
    passed: true
    expected_benefit: |
      让高潮成为下一段因果的起点，而不是“赢了以后清零”。
  decision: verified

- id: wm-v14
  title: 制度移植的试点—缺口—争论—修订循环
  type: narrative-capability
  merged_raw_candidates: [f14,p09,p10,p15,c10,ce03,ce04,ce08,ce10]
  task_ids: [WM-T11]
  source_evidence:
    - "第五卷第153章《民事官》"
    - "第六卷第31—33章"
    - "第四卷第68章"
  V1_source_sufficiency:
    passed: true
    reason: |
      司法试点给出知识缺口、配套缺口、现场混乱与价值争论；其他制度/技术线也出现试点和改进，来源多点支持。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：穿越者想引入一个只记得大概的现代制度。演练必须列“已知/未知/必要配套/最小试点/失败信号/继续或暂停标准”；禁止把未知部分用常识补齐。
  V3_task_utility:
    passed: true
    expected_benefit: |
      直接限制现代知识外挂，并把失败转成剧情与认知收益。
  decision: verified

- id: wm-v15
  title: 重复场景只展开差值
  type: narrative-capability
  merged_raw_candidates: [f15]
  task_ids: [WM-T12]
  source_evidence:
    - "第二卷第26章《大——年》"
    - "第五卷第37章《新气象》"
    - "第六卷第3—6章"
  V1_source_sufficiency:
    passed: true
    reason: |
      全书反复使用过年、会议、训练、回家等同类场景，后期重点转为规模、身份和关系差值；“当年的小渔村，今日的登州强镇”形成明确自我对照。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：作品已完整写过一次年度会议，现在又到第二年。演练先列读者已知基线，再只展开新增角色、规则变化、权力变化和情绪差值；重复旧机制即失败。
  V3_task_utility:
    passed: true
    expected_benefit: |
      为超长篇控制重复，同时让时间累积可见。
  decision: verified

- id: wm-v16
  title: 终局的公共记忆再编码
  type: narrative-capability
  merged_raw_candidates: [f16,c12]
  task_ids: [WM-T15]
  source_evidence:
    - "第六卷第82—84章"
  V1_source_sufficiency:
    passed: true
    reason: |
      结尾先做当事人价值结算，再跳到茶馆评书，明确出现夸张、错置和商业化“灌水”。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：长篇已完成主要历史结局。演练生成“当事人事实层 / 后世公共叙述层 / 两者差异产生的主题回声”三栏，且后世版本必须有自身传播动机。
  V3_task_utility:
    passed: true
    expected_benefit: |
      可用于终局二次回收主题，尤其适合历史题材，但适用范围相对窄。
  decision: verified

- id: wm-v17
  title: 长期关系的多轴状态演化
  type: narrative-capability
  merged_raw_candidates: [f17,c13]
  task_ids: [WM-T13]
  source_evidence:
    - "第一卷第51章《天启驾崩》"
    - "第六卷第33章《九——年》"
    - "第六卷第83章《英——雄（下）》"
  V1_source_sufficiency:
    passed: true
    reason: |
      陈新/刘民有从朋友到军政搭档，长期争论目标与制度，最终仍以“不会骗我”定义可信度；信任与同意明确分离。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：两名合作十年的角色要在重大政策上争执。演练分别记录信任、利益、职位依赖、私人感情、价值分歧五轴，并要求争执只改变其中部分轴。
  V3_task_utility:
    passed: true
    expected_benefit: |
      防止长篇关系退化为单一“忠诚度”，支持旧关系在新身份下持续生长。
  decision: verified

- id: wm-v18
  title: 冲突史料的作者侧裁决与 Canon 固化
  type: narrative-capability
  merged_raw_candidates: [f18]
  task_ids: [WM-T14]
  source_evidence:
    - "作品相关《崔呈秀的去职过程》"
    - "第二卷第6—8章"
  V1_source_sufficiency:
    passed: true
    reason: |
      资料页明确比较《长编》《国榷》等记载差异并写“本书采信”哪一时间线，随后正文按选定版本推进。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：两份史料对同一官员去职日期和先后因果冲突。演练输出“来源差异、选择依据、不确定项、本文采用 Canon、正文不得再混用的版本”；若证据不足则保留未知。
  V3_task_utility:
    passed: true
    expected_benefit: |
      为历史小说事实一致性提供可审计流程，避免模型记忆或多个版本混写。
  decision: verified

- id: wm-v19
  title: 资源升值后的基层权力再拆分
  type: narrative-capability
  merged_raw_candidates: [p07,ce02]
  task_ids: [WM-T03,WM-T06]
  source_evidence:
    - "第五卷第153章《民事官》"
  V1_source_sufficiency:
    passed: true
    reason: |
      原文直接指出物资分配权产生寻租，并具体提出取消若干分配权限，机制在单章内完整。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：早期聚落由负责人统一分配店铺、贷款和原料，后来这些资源价值大涨。演练必须识别哪些权力兼具裁决与获利空间，并提出拆分/监督方案。
  V3_task_utility:
    passed: true
    expected_benefit: |
      能让“制度成功后腐化风险”从抽象警告变成可见结构问题。
  decision: verified

- id: wm-v20
  title: 用权力与资源结构碰撞生成冲突
  type: narrative-capability
  merged_raw_candidates: [p17,ce07]
  task_ids: [WM-T05,WM-T06,WM-T13]
  source_evidence:
    - "第五卷第37章《新气象》"
  V1_source_sufficiency:
    passed: true
    reason: |
      文本直接说明新体系的权力/资源与现有社会结构冲突，并在同章展示任命前的站队行为。
  V2_executability:
    passed: true
    check_mode: walkthrough
    walkthrough: |
      新输入：一个新机构获得税收、任命和土地审批权。演练必须列出至少三个原有群体失去什么、会采取何种合理阻力，而不是直接创造“坏人反对改革”。
  V3_task_utility:
    passed: true
    expected_benefit: |
      稳定生成制度型冲突，同时保持配角利益合理。
  decision: verified
