# Unit20：保存放大的只读解释与下一单元最小计划

仅读取 62733B 小 summary 与冻结 harness 的 save/计时/调用点；未打开、
解析或重算 470406865B raw。以下 raw pin 与计数来自该 summary，未由本
helper 独立读取全 raw 核验。原 owner、已完成 N、冻结代码和全部成果不变。
UNKNOWN local directed NONBLIND 辅助解释；无新研究 owner/Task/claim/run/
branch、代码实施、benchmark、补跑、Source/Native 操作或数学接受。

## 已核实的写入机制

summary 记载 `raw_atomic_saves=37`，已存文件中的 prior-write 字节计数为
14429346885；最终 raw 为 470406865B，故含最后保存的实际累计序列化字节为

    14429346885 + 470406865 = 14899753750 B。

这是最终快照大小的约 31.6741843 倍。`save` 每次都执行完整
`json.dumps(raw, indent=2)`、编码、写入、flush、fsync；后续保存不会只写
新增 calls，已经取得的大 diagnostic/audit 对象随整个 raw 重写。因此存在
明确的全量快照逻辑写量放大。该数是应用层序列化/写入字节，不是测得的
物理磁盘写量、设备放大或 I/O 秒数。

正常路径与 summary 相符的 37 次调用点分解是：

|阶段|保存次数|在总 measurement clock 内|
|---|---:|---|
|initial 与 import/preflight 后|2|否|
|六次 diagnostic 后|6|是|
|26 个完成16-call批次及预算触发的0-call批次|27|是|
|整体 validation/analysis 后|1|是|
|记录 measurement 边界后的最终保存|1|否|

共34次保存位于总计时内。416 个 returned calls 对应26个完整批次；停止于
第8轮 classic 的 repeat0 前，仍到达该空批次的 save。424 次 guard 也与
6 diagnostic guards、417 timed-call guards（含最后一次失败）和1次末尾
guard 相符。这是 summary+控制流的推导，不是读取37份历史快照的声称。
首次保存是 O_EXCL 创建，其余36次是临时文件 fsync 后 replace；计数名为
atomic 不等于此处独立证明了目录层崩溃持久性。

## 能分开与不能分开的时间

`measurement_elapsed_ns=649033674515`，比600秒多49.033674515秒；停止理由
是 `TOTAL600S_BETWEEN_CALLS_BEFORE_TIMED_CALL_8_classic480_full_MeqK_0`。
这是调用间检查的软边界：不强杀已有调用，发现预算耗尽后仍做状态保存、
整体校验/分析和必要日志保存，末尾才记录 measurement elapsed。

所有 save 都在 `plain.run` 的 wall/CPU 计时括号之外；34次在总预算内的
save、校验、export/调度等仍消耗总 clock。诊断正常返回的 wall 在
`inst.run` 后、`rec.export` 前截取；record-limit 异常路径的 envelope
timestamp 在 export 后，所以后者也不能当纯算法时间。所有诊断 save
均在其 envelope timestamp 之后。

没有逐次 JSON编码/write/fsync/replace 的耗时记录，故不能从 summary
精确拆出 I/O 秒数、把49.03秒全部归因于 I/O、或给出移除重写后的完成率。
`raw_finished_UTC` 在最终 save **之前赋值**，不是最后 fsync 完成时间；
不能用它与 measurement_finished 的微小时间差宣称最终保存近乎免费。
进程外端到端最终保存耗时在这份 summary 中也未独立计量。

Fermat 的已存诊断为30秒 cooperative offset-boundary CENSOR；两个
priority 为 record-limit CENSOR，保留字节分别67108841与67108836，且均有
pending record。这些限制发生在 save 之前。保存优化不会追认其未完成
consumer/fee/coverage，也不能由此解除删失、补齐当前矩阵或证明数学 gain。
改变 I/O 还可能改变后续调用的实际内存/cache/scheduling 上下文，不能
保证新旧调用 wall 数值不变或对当前数值事后扣时。

## 下一未填单元的最小 lossless 保存方向

1. 原 owner 在新的未填单元预冻结一个保存格式增量，保持 producer、精确
   费用、resource caps、配对规则和证据语义。将 header/参数与完成后的
   diagnostic/audit 大体分离；每个封存版本完整写一次 immutable shard。
   若后续 checker 会改动某字段，就保留新的版本或小 metadata delta，
   不能假定不可变、静默覆盖或丢弃。具体封存字段须在未来静态审核确定。
2. 各 checkpoint 只写新增 call/slot/control delta 与小 manifest；保持原
   logical checkpoint 节奏。先完整写新 shard、flush/fsync，再发布含有序
   byte/SHA/blob绑定的小 manifest。保存失败或在途写入保留待核验原件，
   不强杀、不删除半成品；恢复不得重放已有 producer。计数区分 logical
   checkpoints、实际文件写次数和所有实际序列化/写入字节。
3. decoder 必须 losslessly 恢复完整 logical raw：事件次序、joint
   predicates、operand widths、费用 event counts、entered/completed/
   pending、CENSOR reason、validation、所有 slots/calls 与状态均保留。
   不抽样 audit、不只存摘要；必要的兼容 monolithic export 最多在边界后
   单独导出一次并另付费，不能每批重建大 raw。保留当前 raw 与 Source 原件。
4. 新代码预先分别记录编码、写入/fsync/发布、export/校验的实际 wall/CPU、
   字节和阶段；在总预算内的工作仍在总预算内计费，算法计时括号保持明确。
   这些是下一单元待审核计划，尚无实施或 benchmark，未量化收益；无需也
   不允许为了证明保存效果补跑当前 N。

预期减少的是已封存证据的重复序列化/重写，不是免费消除 diagnostic 内部
记录成本或突破其上限。当前六法矩阵、各删失与 gain 判定保持原样。
这是 P000/HEARTBEAT_NATIVE_X6 下的外部整数/声明费用模型解释，未声称
物理成本等同、原生维度改变、数学接受或父目标完成。
