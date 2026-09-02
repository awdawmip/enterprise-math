# 研究调度协议 V2

状态：`ACTIVE / CURRENT ONLY`

任务定义只来自不可变的 V2 发布记录。`research_control_dispatch.py` 先处理陈旧会话下的既有 owner 恢复，再把全新任务选择交给 `tools/research_dispatch.py`，把并行 cohort lane 选择交给 `tools/research_lane_dispatch.py`。

Issue #240 的运行态变更必须来自经服务器认证、未编辑且属于授权操作者的 GitHub 评论封装。`tools/research_runtime_reducer.py` 只是纯 reducer，不持有任务表，也没有数学权威。

选择顺序由 `research_runtime_policy_v2.json` 定义。owner lease 与会话存活相互独立；陈旧会话在核验 durable frontier 后接管原 claim，不创建第二个 claim。
