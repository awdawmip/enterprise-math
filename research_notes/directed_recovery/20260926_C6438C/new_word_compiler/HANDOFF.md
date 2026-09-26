# 新对话续接入口：完整原生字 Shor 模拟

状态：AUTHOR_EXECUTED_BOUNDED_CASES / SHARED_CONTEXT / UNREVIEWED /
NOT_ADMITTED。研究员 `EM-DIRECT-C6438C`，本次执行活动
`RA-CAAAC604CB513AEA8BBC1DFC`。本文件记录成果和可直接推进的下一步；
发布 Source、文件清单及最新任务状态以本包发布元数据为准。

## 已经完成什么

目前有一条明确的新算法：固定 H4/sign/swap 原生字母表和全部 61 个载体
坐标，允许有限字长与代数证书观察深度随所需精度增加。对任意有限宽度和
正有理误差，已有作者证明给出满足完整载体算子误差的有限词，并证明公平
搜索最终能找到严格证书。它已接入原始 CF 后处理和递归完整分解接口。
这不是一次性冻结字库覆盖所有精度，也不是多项式时间经典分解结论。

旧 K33 固定字库的“无法在任意宽度统一保证强 TV 逼近”结果继续成立。
新算法按请求改变有限字长，因而不沿用旧反例所需的固定有限相位积集合。
读取 `STRONG_SHOR_COMPILATION_THEOREM.md` 可看到完整误差与成功率推导。

实际证据已经到以下程度：

| 层次 | 已执行结果 |
| --- | --- |
| 原生字与证书 | 全部 61 列、逆、Gram、实际 BRC 严格误差观察；编译预算耗尽可返回 PARTIAL |
| 小宽度流式集成 | N15/t4、N21/t6 与同一实际词完整电路的全部联合振幅精确一致；逆恢复通过；6724 次 BRC 核调用 |
| 完整分解 | N225 保留 `15^2` 编译断点后完成 `3^2*5^2`；N21 完成 `3*7`；零相位失败保留未决余因子；16991 次 BRC 核调用 |
| 跨进程 CLI | N15 第一个进程 PARTIAL，第二个进程读取编译游标后 COMPLETE `3*5`；素数证书与乘积账本通过确定性验证 |
| 四平方直接构造 | 相邻交付单元完成 m3、delta=1/4；190 个索引原生字展开为 8114 个规范字；全 61 列严格证书与 PARTIAL/新进程续接通过 |

每条动态相位传播都使用实际原生词。代数理想目标只用于符号证明和证书
观察，不作为传播矩阵，不运行理想 QFT 来制造实际结果，不删除残差。
旧 target32/vector64 种子保持原样；新观察深度属于明确声明的新编译器配置。

## 从哪些文件读起

先读本文件和 `COMPILED_FACTORIZATION_NOTE.md`，即可区分已完成结果、
概率条件与续接语义。需要复核时按具体问题读取：

1. 数学闭合：`FIXED_ALPHABET_DENSITY.md`、`EFFECTIVE_COMPILER_CLOSURE.md`、
   `STRONG_SHOR_COMPILATION_THEOREM.md`。
2. 实际编译器：`certified_word_compiler.py`、`CERTIFIED_WORD_COMPILER_NOTE.md`、
   `CERTIFIED_WORD_COMPILER_SUMMARY.json`；源码 SHA256 为
   `e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d`。
3. 流式接入：`compiled_streaming.py`、`COMPILED_STREAMING_PROOF.md`、
   `COMPILED_STREAMING_SUMMARY.json` 和对应完整 `.json.gz`。
4. 完整分解：`compiled_factorization.py`、`compiled_factorization_core.py`、
   `run_compiled_factorization.py`、`COMPILED_FACTORIZATION_SUMMARY.json`。
5. 实际跨进程断点与终点：`CLI_COMPILE_PARTIAL_N15.json.gz` 和
   `CLI_RESUMED_N15.json.gz`；后者解压 payload SHA256 为
   `0a7aa7c29cdf81d41b542e0f5561bffe123bfc488335bef925f2d8539b0bb322`。
6. 已完成的直接构造实例：
   `../direct_word_compiler/DIRECT_WORD_EXECUTION_NOTE.md`，以及该目录的完整
   `DIRECT_WORD_CERTIFICATE.json.gz` 和游标负控制证据。

以上是包内相对路径。当前工作副本位于
`D:/em/TEMP/sep26-shor-general/new_word_compiler/`；它是定位事实，
不是对后续对话运行位置的限制。使用本包发布时记录的仓库、Source 和
校验清单，也可以定位同一份材料。

## 怎样继续一个编译断点

Python 接口是
`factor_integer_compiled(N, rng, phase_cursors=..., compiler_pair_budget=..., observer_start_bits=...)`。
传入上次结果的 `native_word_compiler.phase_cursors`，保持相同证书源码、
目标、种子策略与观察配置，增加本次有限 `compiler_pair_budget` 即可。
编译器会检查这些绑定；不能把旧源码游标改个标签冒充当前证书。

CLI 提供 `--resume-cursors-from <上次结果.json.gz>`。N15 的跨进程续接已经
完成，应先读取上述终点证据；只有需要复核执行时才重复该演示。其复现参数
为 `--failure-bits 2 --attempts 8 --compiler-pairs 32
--observer-bits 48 --seed 20260926`，从冻结的
`CLI_COMPILE_PARTIAL_N15.json.gz` 读取游标，把结果写到新的文件名。
准确的 PowerShell 调用示例见 `COMPILED_FACTORIZATION_NOTE.md`。
也可在现有 Python 进程中直接调用接口，不依赖该命令行形式。

这里续接的是相位编译进度。CLI 不恢复 RNG 内部状态、尚在运行的递归
队列或完整随机转录；它重新启动分解调用并使用已验证的编译进度。
旧素数与乘积账本仍然是可核对成果，新调用不会把其内容直接当作可信活动
状态导入。若要实现这些更完整的恢复语义，应作为明确的新研究/实现单元，
保留当前已通过的游标合同。

编译得到 PARTIAL 时保存结果和游标，再从该点推进；不要运行缺相位的程序。
尝试预算耗尽则保留未决余因子及其重数；失败的 Shor 尝试不是素性证明。
定时任务或新对话可以用完成的有限调用作为持久断点，无需重新寻找研究方向。

## 概率字段应怎样解释

CLI N15 演示使用软件 seed 和 8 次尝试上限，少于该节点证书预算 172。
因此 `budgets_meet_uniform_random_bound=false`，确定性核验也明确报告
`stochastic_budget_verified=false`。这些字段没有否定已验证的 `3*5=15`
及素性证书；它们拒绝把短演示当作完整随机保证。

作者定理要求新鲜、条件均匀的底数与读出随机源，并在每个节点采用足够的
尝试预算，才得到递归重试失败上界 `2^-s`。默认接口计算相应预算；外部
随机源本身仍不是由乘积账本证明的。单次终端 TV 证书也不自动覆盖整个
多次重试转录；若新任务要求该转录的 TV 精度，需要另分配可累加的误差预算。

## 下一个有价值的研究结果

第一优先是把 `CONSTRUCTIVE_FOUR_SQUARE_FRONTIER.md` 的构造路线推广为
接受任意合法 m 和正有理 delta 的直接构造器。作者符号构造使用相同
61 维载体，以四平方补全得到单位法向量，再由冻结 `synthesize_unit`
产生有限 H4/sign/swap 词；显式观察深度与长度界已给出。

相邻 `../direct_word_compiler/DIRECT_WORD_EXECUTION_NOTE.md` 已完成独立候选
`m=3, delta=1/4`：实际余量 `K=3071` 的四平方证据为 `(1,55,3,6)`，
生成 190 个索引字与 8114 个规范字，全 61 列和严格误差核验通过，并有
PARTIAL/新进程续接及游标负控制。完整 payload SHA256 为
`d29cd6b789cc07eafe430117c31b3e5fe918cda041550ea6e0b1894154a5ab82`。
该实例是本次交付的已完成证据，不应把重复执行它当作下一项研究成果。
当前直接 CLI 仍固定该实例；任意 m/delta 参数接口、相应通用断点与新实例
是尚未完成的增量，公平枚举编译器继续作为一般后备。

后续对话先核对最新发布元数据，避免重做已发布单元；随后可按以下明确成果
推进通用实现和一个新的有限实例：

1. 在新工作目录把直接构造器参数化，按输入 `(m, delta)` 推导 B 与观察
   深度，并把这些参数和资源游标绑定到证书。选择区别于已完成 m3 实例的
   公开请求，构造闭区间端点和两个向下取整坐标，保存实际算术回执与配置。
2. 完成非负整数余量的四平方证据，保存搜索/算术断点，证明完整法向量的
   单位范数；区分候选生成与实际 BRC 验证。
3. 由原生综合程序生成词，交给现有完整 61 列/逆/Gram/严格误差核验；只在
   CERTIFIED 后进入现有流式与完整分解接口。
4. 报告误差、字长、实际调用数与未决问题。若预算在中途结束，交付具体游标
   与已经得到的算术证据，下一次继续该有限步骤。

这项工作可由读取到本包的任意对话续接。选择当前可用且获授权的代码、
文件、仓库或 MCP 路径完成上述成果；单个入口失败时保留内容和定位信息，
使用其他可用入口推进，不把工具名称或运行环境写成数学任务的前置门槛。
确需不同载体、传播规则或源码时，把变更单列并重新绑定证书，保留本包。

## 交付与结论边界

继续工作时记录使用的包版本/Source、输入、参数、产物路径及内容 hash，
从而让下一对话能定位同一断点。新的实测写入新的证据文件，保留冻结原包、
旧 K33 结果和微补丁之前的归档。root 负责本包最终元数据、打包与发布；
本文件不预先声称这些外部写入已经完成。

所有结果仍是共享上下文内的作者证明或作者实测，尚未独立 admitted。
没有宣称高效经典 Shor 模拟、物理 Born 规则推导或自主六空间轴布局完成。
真实的研究增量是可核验的数学推导、完整有理证书和执行结果。

Global-Knowledge-Sync: main@8446003 / GLOBAL_KNOWLEDGE_V1
