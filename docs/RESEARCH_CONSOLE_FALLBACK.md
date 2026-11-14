# 研究中控台不可用时的科研资料接续（项目入口附录）

本文件补充 `docs/PORTABLE_RESEARCH_PROTOCOL.md`；面向**已有独立 GitHub 访问权限**的研究者与客户端。它提供资料回退和独立成果保全路线，不变更当前正式 Task/CLAIM/Result/Review 权威。

## 取得科研材料

- 已有准确、当前适用的完整正文，直接复用。中控台返回摘要、缺失、明显过旧或服务不可用时，只从 GitHub 补取**需要**的文件及相关证据；不默认每轮全仓扫描。
- 普通 TASK 研究以 `p000_reality_foundation.json`、`definitions/EM_FOUNDATION_STARTUP.json`、`definitions/00_CURRENT_NATIVE_FOUNDATION.md`、准确任务书和实际数学依赖为来源。当前行为规则与冻结的科学输入分别固定。
- **FREE Phase A** 以 `definitions/EM_FREE_A_FOUNDATION_STARTUP.json` 和 `definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md` 为阶段入口；不预加载普通 `00_CURRENT_NATIVE_FOUNDATION.md`、已取得的下游成果和工具菜单。只有自己已形成问题且允许的相关定义或工具，才沿原 FREE 角色合同按需查找。Phase B 使用其原有对照程序。
- GitHub 文件内容、可核验来源、版本与实际依赖胜过缓存和摘要。仅有目录、commit 哈希或“已读”标签并不等于模型已经取得定义正文。

## 中控台永久丢失

可以从 GitHub 的现存项目入口和科研成果开始新的会话，复用已发布的前沿做证明、反例或实验。旧 SID、RUN、租约和 Activity 编号丢失不会使数学文件失效。

**独立科研**和**正式共享运行权**必须区分：没有当前有效 CLAIM 时，可以做推理并向已有授权的 `research_notes/portable_direct/` 等独立科研目录**新建非覆盖式文件**；新文件引用真实先前任务/前沿，仅表示科研材料，不冒称原 CLAIM、正式 PROGRESS、Result 或 Review。已有 Task 的当前独占执行、受保护成果更新、迁移、审查和终结仍遵循 `control_plane/current_control_authority.json` 及正式状态机。既有明确拒绝、用户取消和来源信息防火墙继续有效。

## 保存及恢复

1. 通过实际获准的 GitHub 写权限，以唯一文件路径或既定非覆盖方式发表原始科研内容；必要时在独立分支中保存并明确标记尚未合并。发布者应保存内容、来源、必要输入/验证范围，不能假报数学证明或测试成功。
2. 取得**真实**的仓库、commit、path 和完整字节读回。提交已发布并验证，与 Activity、索引、正式 Task 关联是互相独立的事实。
3. 原远端请求若超时或回包丢失，先按已知原请求、目标路径和字节只读核实；不换身份、路径或请求 ID 盲目重放同一副作用。新独立成果可以另行保全，但不得冒充原正式状态成功。
4. 中控台恢复后从现有 GitHub 原件建立索引、候选研究关系，并由现有合法角色判断正式任务接纳；不要求重做已核验数学或恢复旧失效 SID 来“证明内容存在”。

## 谁需要额外验收

每个具体 Chat、Sites、Codex 或网站端，都需证明自身能在**不调用中控台**的情况下直接访问 GitHub 并在已有权限下发布及读回；若能力不足，只报告该端支持的读/写范围，不以另一个端的测试替代。GitHub Issue Bridge 若依赖中控台消费者，不算独立回退。私钥、GitHub 凭据与未发表唯一载荷不放入公开仓库。

控制台失效期间可以继续科研，但不可据此推出失效服务已安全恢复、旧写者被合法退役或存在新有效任务 owner。完整工程验收以独立会话实际读取、产出、保存和新会话再取回为准。
