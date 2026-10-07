# V10 Novel Runtime v0.1

这是 V10 明末历史战争长篇小说的最小可恢复运行库。

目标不是保存聊天记忆，而是让一个完全失忆的新对话只读取本仓库后，恢复到当前项目 95% 左右的创作判断与项目状态。

## 唯一入口

新会话必须首先读取：`V10_SKILL.md`

## 当前最小结构

- `V10_SKILL.md`：启动协议与权威顺序
- `RUNTIME/CORE.md`：必须默认生效的创作内核
- `CURRENT/PROJECT_STATE.md`：当前项目状态缓存
- `CANON/MASTER_SETTING.md`：已经确认的正式设定
- `INDEX/INDEX.md`：当前索引入口
- `TESTS/BLIND_TESTS.md`：失忆恢复盲测题

## 设计原则

1. 聊天记录不是事实源。
2. Canon 是小说事实的最高存储层。
3. Runtime 是已验证的创作能力，不等于原始研究资料。
4. Current 是工作缓存，可以重建，不得覆盖 Canon。
5. 新能力不得因为“听起来正确”直接进入 Runtime；必须经过测试。
6. Cangjie 用于蒸馏书，NUWA 用于蒸馏作者心智；两者产物先验证，再晋级 Runtime。
