# 双正支点工具的可移植独立执行审查

状态：`PASS / BOUNDED INDEPENDENT EXECUTION / PATH-ADAPTATION-V1`。

这是既有独立审查脚本的最小路径适配，不是新的数学工具、API、目录登记或正式研究处置。原消费者三文件、16 条源码/论文 pins，以及旧独立审查包均保持原字节。本包不改变 p≤2 定理、原坐标矩形取等分类或消费者输入合同。

## 运行

在包含原工具及其依赖的完整项目 checkout 中：

```text
python -B -X utf8 experiments/owner_two_positive_stability_20260908/independent_review_20260908/review_two_positive.py --root . --output ../two-positive-independent-output
python -B -X utf8 tools/check_exact_arithmetic_policy.py experiments/owner_two_positive_stability_20260908/independent_review_20260908/review_two_positive.py
```

`--root` 可以指定其他 checkout；省略时由脚本所在目录推导项目根。`--output` 必须显式提供，建议使用新的独立目录。运行生成的表、日志、源保护快照以及故意损坏的复制 fixture 都写在那里，不写原工具和论文。脚本本身没有固定的本机盘符路径，也不读取旧 TEMP 审查包。

所需独立辅助文件均在本包内：

| 文件 | 用途 |
| --- | --- |
| `review_two_positive.py` | 原 9 个独立案例、原拒绝检查、canonical 调用观察及复制源漂移测试 |
| `author_input_pins.json` | 16 条既有来源与 3 个作者文件的固定 SHA256；三文件另带字节长度 |
| `validation.json` | 本版本实际运行的参数、输出、哈希、紧凑检查结果与新旧比较证据 |
| `README.md` | 合同、运行方法及审查结论 |

root 仍须包含元数据列出的原文件和现有项目库；本包不重复分发原库或论文。19 条 pin 是本审查的明确绑定范围，不是整个项目传递依赖已全部迁移的声明。其他无关提交前进不自动使回验失效；绑定字节改变会拒绝，需要新的明确审查。

本包不收录大张的完整案例表或复制作者的 492,922 字节证书。脚本在指定 output 中重新生成独立完整表；它们不是运行输入，也不需要旧 TEMP 副本。实际本次生成的 227,160 字节案例输出与旧运行逐字相同，SHA256 为 `8377b0a65346d6b137d5820edbc6ddcb2be79d29d033ef8cf2e618af188d3375`。

## 最小适配及证据保留

旧脚本 SHA256 为 `122a87bc28a8ddbe7cb8c07b4c1e09f99ed60f2c025f3e9df8c839551bb5d78a`，旧审查回执为 `4a2377315bb15e80bf7300d7916ab88e94c0cadcc70bf10381b33bdb9e35e982`。本次没有覆盖旧文件，也没有把旧回执改称新版本执行结果。

变化只包括：

1. 用脚本相对位置及 `--root`、`--output` 替换固定本机目录。
2. 用随包提供、且在脚本中固定其哈希的 `author_input_pins.json` 替换本机完整作者 manifest。原三文件的重复全文比较改为长度加原 SHA256 检查；原 16 条 source pins 不变。原作者 manifest 哈希 `ccfdfc7365685e5e4270ca7cd9d48802993f7e627f07914abe087f68399a7105` 仅保留为历史来源，不要求该 manifest 文件存在。
3. 回执区分本次实际读取的 pin 元数据与历史 manifest 哈希；固定的 global knowledge 值明确标作脚本作者快照，不能用作未来运行的 fresh lease。

9 个辅助函数/类的 AST 均与旧版相同。从 canonical import 开始到最终回执整理之前，整个主执行、数学检查、18 个局部拒绝及复制源漂移子进程段，源文本逐字相同。实际重跑还确认：9 例完整输出、18 条拒绝及 canonical 调用计数分别相同。没有只比较摘要数量后就宣称数学检查未变。

## 数学与类型范围

输入始终是同一外部 anchor、同一带标签 raw X6 坐标图内的两个有限正人口。先聚合、抵消，再限制 Jordan 正支点数至多二；signed 差只作分析账本。共同 anchor/坐标 provenance 是调用者前提，六整数本身不证明这个前提。

独立参考值以整数逐点、逐地址累加构造全部 20 张三轴 raw 表，不调用被测 projection 函数生成期望值。消费者则真实复用 canonical Spatial6、one-positive population/raw projection/joint roundtrip 和 canonical 未求值 DIV。没有私有类型别名、普通除法、求根或新增负 BRC primitive。

既有纸面来源覆盖任意有限负支撑和正有理权：d=1、d≥3 的加权避正表界严格强于 1/4；d=2 的完整非负间隙为 `D-4M = table_gap + negative_gap`。非零等号恰为原坐标两差轴矩形的等幅棋盘差；共同抵消人口任意。执行审查不以有限例代替该纸面证明。

## 本版本实际回验

从本包真实源路径，以 Python 3.12.14、`-B -X utf8` 和显式 root/output 运行：**9 例、180 表、18 个局部拒绝与 1 个真实复制源字节漂移拒绝，exit 0，0.720949 秒**。选定的本脚本 V2 静态 gate 实际 exit 0，0.122643 秒。没有重复运行作者原 17 例构建。

案例保留了非单位矩形与 2053 位正质量、一次性迭代输入及共同抵消、等总质量但不等角权、d=1 的第三端点与负质量过量、d=4 混合点、d=6 的 can3 全消/raw 非零反例，以及 p=1、p=0、零差和 N=0。负测保留丢表/重复轴、错误 raw 地址/offset/can3/范数、丢弃显式零行、虚假原矩形/质量归一化/支持集取等、非法精确类型与真 p=3 拒绝。

观察到 canonical DIV 构造 64 次；旧 p≤1 audit 仅调用 3 次，且进入时以独立 Jordan 支撑断言 p≤1。观察窗口始于 canonical imports 之后，不覆盖历史 import-time 初始化、未执行的全部传递路径或所有 C 内部运算。静态 PASS 也不独自证明传递合规。

执行时实际观察的本地 HEAD 为 `50859d654729c56f8e4c098fa2a8605768b80edf`，tree 为 `d4567b3a5dc4c222c10ff44c03efc805af299a71`；这是冻结输入及本包候选覆盖的运行，不是 clean HEAD 或已发布输入的声明。19 个原输入的字节与 mtime 不变；旧整个独立历史包的 19 个文件也保持字节与 mtime。`validation.json` 中的绝对路径是这次运行的历史事实，不是未来重放依赖。

本版本独立脚本 SHA256：`37c831a0b51dbd6cd16e9657d3f402f7903af7deaa205ce17772639b6af3b51e`。
pin 元数据 SHA256：`57a90c8aa99f22d51cbb8bd905cf9700900ecdb4f56b081cacaf8d713841548c`。

未新增数学/API/目录注册；未声称 p≥3 扩展、完整 carrier 搜索、全仓 CI 或主线准入。最终发布和准入由 owner 单独处理。

Global-Knowledge-Sync: main@31d06a1 / GLOBAL_KNOWLEDGE_V1
