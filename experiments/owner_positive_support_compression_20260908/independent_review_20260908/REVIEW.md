# Positive-support compression: bounded independent consumer review

Status: `PASS_BOUNDED_CONSUMER_REVIEW_NO_FORMAL_ACCEPTANCE`.

本次独立复核冻结程序的输入/输出合同、真实原生调用和少量有区分力的执行边界，未发现阻止该辅助 consumer 发布的缺陷。这不是正式 V2 Result review、数学结果晋升或一般输入的机器证明。此前压缩论文承担全体有限输入的证明；本包提供指定程序字节上的有限独立执行证据。

## Exact reviewed input

作者 r2 冻结清单 SHA256 为 `e96471b93542205d1046c1f84dfba8ae613c45d663e9004e33366928a7836833`。执行前独立核实该清单本身、以下三文件，以及其全部 14 个依赖的实际字节。

| 文件，相对上一级目录 | SHA256 |
| --- | --- |
| `check_positive_support_compression.py` | `f7e31ef40a2af4da1eaf0726068b212bb5efd66e82056ef91c8ee29581853660` |
| `certificate.json` | `e1d6e819678d3472acc95aa9b1655f001161dcb93a02c7e0cb47219a542e1cf5` |
| `README.md` | `5b6394b07d916c8bdf33b7577314938d0bb15337ceec395dac471f2a4ea1af14` |

依赖字节清单完整保存在 [review.json](review.json)。依赖来源可由公开 owner commit `d11e10126170335cc520fb9ce809682d76aa8bfe` 追溯；压缩论文的原始发布 commit 为 `90974735b479a6e99db769eec385b2c51a749f24`。这些是历史来源，不是对当前远端 head 的推断。复现只要求工作区内对应精确文件，不依赖作者本机的 TEMP 清单或本地独有 Git object。

## Contract and source review

逐段读取冻结 consumer、其 README，以及实际复用的一正支点程序的 pin/import、`population`、`raw_projection`、`verify_joint_projection` 和对应的原生函数。

`audit_compression` 接受两个有限的正总体。每个 atom 的 cell 必须是精确的 canonical `Spatial6` 类型，权必须是严格正的 Python `int`；分母也必须是严格正 `int`。聚合、相减和 Jordan 分离之后才计算 S，原总体中已抵消或净负的点不能继续占据正支点角色。signed 数账是辅助分析差，不是负 BRC 分支权。

非空 S 的逐轴 `max(A_i)+1` 在整数域中必为 fresh。每个正坐标值只允许自身进入该坐标纤维，因此固定正点与其质量，且不会把负质量送进正点。相同 singleton 纤维论证作用于每张 raw 投影的正地址；余下地址只有负质量合并。程序的推前实现与该已证明合同一致。空 S 使用单点常值 carrier，避免空集 `max`，零差也不构造比值。

程序按六个轴类数相乘，不枚举 carrier。`carrier_cardinality` 是容纳范围的大小，不是实际 support 数。保存的每张 raw 表仍带原地址与压缩后地址；它们可改变，范数保持。joint `(can3, common offset)` 的保真声明依赖原生 slice 和 reconstruction 的实际调用。can3 单独观察不继承此结论。低层 `pushforward` 不保证任意外来 specification 的保真；有合同的路径通过 `validated_compression` 绑定当前 Jordan 正支点和 specification。

新 ledger 只构造非负 facade 的 `DIV(1,d)`、`DIV(M,d)`、`DIV(D,d)`，没有请求商、余数、根或约分。现行 V2 允许这种未求值表示。源程序的旧一正消费者只在五个明示 p=0/p=1 兼容案例中前后各调用一次；不会用该旧定理检查 p>1。新程序没有声明双正最优常数的可执行证书。

## Actual bounded execution

仅执行一次 [review.py](review.py)，Python 3.12.14，退出码 0。脚本首先在 fresh 子进程中运行冻结程序的默认只读入口一次：18 个作者案例、360 张 raw 表、10 个拒绝输入、2 个失效边界全部重建，与冻结 certificate 精确逐字节相等。该重放没有使用 `--write`，也没有再运行作者的数学/静态测试集。

随后执行以下五个独立构造，另有三项新拒绝检查。每例的二十张表均使用独立数账核对：先分别投影两个正总体，再相减，避免仅把被审函数自身的 signed projection 结果当作 oracle。还独立核对每个输出地址及质量、Jordan P/N、实际 support、符号 carrier、未求值 DIV、D 确为二十个范数之和。

| 独立构造 | 实际结果 |
| --- | --- |
| 17 个 post-Jordan 正点，带重复共同质量及负点碰撞 | p=17；q 从 14 降至 7；support 从 31 降至 24；carrier 为 `18^6 = 34012224`，从未枚举。 |
| 交换上一例的两个总体 | p=14；q 从 17 降至 7；support 为 21；carrier 为 1000000。P/N 交换，全部二十个 raw 范数与交换前一致。 |
| 原 mu 的三个位置经聚合/抵消后仅余一个正点 | 实际 p=1，M=8，D=154；一张共享三轴投影发生异号抵消。S 从净差重算。 |
| p=3 的大整数坐标、质量和共同分母 | 坐标幅度 17001 bits、最大权 18001 bits、分母 17004 bits。精确 DIV 分母与三个结果节点均未被求值或约分；20 表通过。 |
| 较大纯负总体 | p=0；q/support 从 16 降至 1；carrier 为 1，D=20M。 |

三项拒绝检查分别是：同一 S 的 carrier 元数据被篡改、`Spatial6` 的外来子类、正 `int` 的子类权。它们实际抛出预期的精确 `ValueError`，没有修改任何源文件。作者默认回放另实际重建了旧 S 的范数丢失反例与 can3-only 范数丢失反例；本包不另重复它们。

## Actual identity and calls

独立脚本核实导入模块位置与十四个 pin，并把被调用函数的 `__code__.co_filename`、起始行及所属模块绑定到源文件。计数以函数 code object 为键，不只依据相同名称猜测复用。新增五例与三个拒绝检查的观察窗口中，实际计数包括：

| 原生或复用函数 | 调用数 |
| --- | ---: |
| `one_positive.population` | 12 |
| `one_positive.raw_projection` | 200 |
| `one_positive.verify_joint_projection` | 200 |
| `native.hidden_slice_coordinates` | 2760 |
| `native.from_hidden_slice_coordinates` | 2760 |
| `exact.division` | 15 |

新增检查没有调用旧 `audit_case` 或 signed-BRC helper。原作者默认回放的已重建调用表另完整保存在回执中，包括只在指定旧 p<=1 兼容案例中出现的 `support_size` 等调用。

此调用观察从 pin 校验及 canonical import 之后开始。有限窗口没有观察到 Fraction、商/根求值、旧 multiplicity helper 等绕行。它不证明 import-time、未执行分支、任意 C 操作或所有传递历史代码全面合规。上述函数身份、选定源阅读与实际调用是证据范围，不把 profiler 当作通用权限或算术证明器。

## Preservation and limitations

执行前、默认回放后及独立检查后，14 个依赖与 3 个被审文件的 SHA256、长度及 `mtime_ns` 全部保持。Python 全局十进制整数渲染限制一直为 4300，没有为了大整数改变进程配置。独立回执使用十六进制精确整数摘要绑定大输入；这不是宣称被审程序提供任意大整数的通用十进制 JSON 编码协议。

程序执行范围是全部二十张三轴 raw 表。论文更一般的所有坐标子集范数结论没有在本轮逐一执行。没有枚举 carrier、随机或无界搜索、LP 或求解器。有限五例不承担一般数学证明。压缩不保微观 BRC、路径数、word/history、位移/物理运动或全部线性观察。本包不建立 Task、claim、Result、WorkingTruth、Foundation、目录状态或正式接受权力。

## Reproduce and evidence binding

在含上述精确被审字节与依赖的 repository root 运行：

```powershell
python -B -X utf8 experiments/owner_positive_support_compression_20260908/independent_review_20260908/review.py
```

也可向脚本传入 repository root 作为唯一位置参数。默认根路径由本包目录布局定位。脚本仅写本目录的 `review.json`，默认子进程只读比较作者 certificate。每次复现记录实际时间、命令、脚本哈希与 stdout/stderr 哈希，因此新回执的时间和整体 SHA 可以不同；数学输入及冻结字节由内部 pin 控制。

本包所含且本次真正执行的脚本 SHA256：`d940c1f6e4efac745284a28cba77bcfde2a48ac6ee432a6f0d583417e401adf2`。

本次实际生成的回执 SHA256：`8ee1608a8e32d442fa788d797936278b50752c84439c28c9af3f1373ac5fd43e`。

本说明在执行后新增，没有对已执行脚本做字节归一化或语义改动。三个独立包文件统一为 UTF-8、无 BOM、LF、EOF LF、无行末空白；包自身的最终三文件哈希另交 owner 的出版清单绑定，避免自引用。

Global-Knowledge-Sync: main@eb09a0a / GLOBAL_KNOWLEDGE_V1
