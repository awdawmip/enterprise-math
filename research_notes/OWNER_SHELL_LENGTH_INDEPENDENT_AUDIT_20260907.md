# signed X6 平方壳长度锐界：独立交叉审计

状态：`PASS_AFTER_RESOURCE_FIXES / ALL_N_MATHEMATICAL_ARGUMENT_CHECKED / AUXILIARY_ONLY`。

辅助工作包 `/root/stability_research`，2026-09-07；`ANCHOR_EXPOSED`，不是正式 task、claim、V2 审稿或 Foundation。Global Knowledge 有效读取租约仍为 `main@4fa7d7d0c19a5e80a681b33c8ee2ab643ce97563`。

**结论。** 作者关于所有 `N∈Z_{≥0}` 的

`max_{Σz_i²=N} Σ|z_i| = max{k≥0:k²≤6N,k≡N (mod2)}`

证明成立。六行余类表、t 上界、Meng–Sun 引理的严格条件、三平方到四项的符号变换和零壳均已交叉核对。构造器初审发现的两个资源/API 问题由作者修复；最终独立局部检查通过。本审计没有做 N 前缀枚举，没有修改作者或 canonical 文件。

## 1. 来源与准确复用合同

逐段阅读作者 `OWNER_SHELL_LENGTH_FRONTIER_20260907.md` 和 `experiments/owner_shell_length_20260907/shell_length.py`，并复核已存在的 `signed_brc.py` 与 `x6_signed.py` 相应 consumer。前者实际提供平方和、最短事件数和精确词数；后者提供 signed Cell、common-depth 与各切片的无损重建。没有新造底层 BRC。

已独立打开 [Meng–Sun 期刊原文](https://www.impan.pl/shop/en/publication/transaction/download/product/92360)，核对印刷页 235–236 的 Lemma 2.4、式 (2.2)、式 (2.6) 及非负性证明；也核对 [作者 arXiv v4](https://arxiv.org/pdf/1608.02022v4)。所用引理确实要求正整数 A、B、`B²<4A`、`3A<B²+2B+4`，并附奇偶条件。本任务只用 A、B 全奇的分支，不需要偶分支、渐近阈值或其他附加假设。

原论文称该全奇分支为 Cauchy’s Lemma。这里是准确的既有引理复用与六轴输入构造，不把经典固定和平方和方法或原生固定端点词数公式当作新基础理论。

## 2. t 范围与六行恒等式

令 `k=U(N)=6b+r`，`0≤r<6`。Cauchy–Schwarz 和整数奇偶直接给任意壳点的长度上界 k，不依赖待证存在性。

定义 `N=6b²+2br+r+2t`。由于 `k²≤6N`，

`N−(6b²+2br+r)≥−r(6−r)/6≥−3/2`。

左侧是偶整数，所以必非负，t 是非负整数。这个步骤没有偷用“最均衡六个整数已存在”的结论。

下一个同奇偶候选 k+2 不可行，故

`12t<24b+r²−2r+4`。

各 r 的最后常数依次为 `4,3,4,7,12,19`。整数 t 因而满足 `t≤2b`（r=0..4），r=5 才是 `t≤2b+1`；特别 r=4 对应严格 `<2b+1`，不能误取端点 `2b+1`。

设固定两项为 p,q，`B=k−p−q`、`A=N−p²−q²`、`D=4A−B²`。独立展开得到下表。最后一列是在允许的最大 t 处取下界；不是若干数值样本的最小值。

| r | p,q | B | D | `(B+4)²−3D` 的统一下界 |
| --- | --- | --- | --- | --- |
| 0，t≥1 | b,b+1 | 4b−1 | 8t−5 | `16b²−24b+24=(4b−3)²+15` |
| 1 | b,b | 4b+1 | 8t+3 | `16b²−8b+16=(4b−1)²+15` |
| 2 | b,b+1 | 4b+1 | 8t+3 | 同上 |
| 3 | b,b | 4b+3 | 8t+3 | `16b²+8b+40=(4b+1)²+39` |
| 4 | b,b+1 | 4b+3 | 8t+3 | 同上 |
| 5 | b+1,b+1 | 4b+3 | 8t+3 | `16b²+8b+16=(4b+1)²+15` |

r=0 非平衡行中 `1≤t≤2b` 强制 b≥1，故 B≥3。其他行 B≥1。各行 D>0 且 D≡3 mod8，B 奇；因此 `(B²+D)/4=A` 为正奇整数。上表所有下界严格正，正好得到 `B²<4A` 与 `3A<B²+2B+4`。引理的域、两个严格不等式及全奇条件均完整满足。

r=0,t=0 必须在调用引理前分开：六个 b 直接给平方和 `6b²`、长度 `6b`。N=0 正在这个分支内，唯一端点是零向量、最短词是空词，词数为 1。没有留下小壳或零壳的条件缺口。

## 3. 三平方搜索和 Hadamard 变换

D≡3 mod8 排除了 Gauss–Legendre 三平方障碍 `4^a(8m+7)`。任何三平方表示又必全奇，因为平方模8只有 0,1,4，而和为3只能是 1+1+1。可取正根后排序为 `x≤y≤z`，因此作者搜索域

`1≤x≤floor(sqrt(D/3))`，

`x≤y≤floor(sqrt((D−x²)/2))`，

加上最后 z 的精确整数平方检查，覆盖所有可能的排序正奇三元组。此处没有漏掉必须为零或负根的情形；奇根不为零，符号稍后处理。

逐根选择符号，使 `x≡y≡z≡B (mod4)`。这保持三个平方之和 D。四个分子

`B+x+y+z, B+x−y−z, B−x+y−z, B−x−y+z`

全部被4整除。除4后的四项之和 B、平方和 `(B²+D)/4=A`，由 Hadamard 正交恒等式直接成立。

非负性不是由程序“刚好搜到正数”提供，而是

`|x|+|y|+|z|≤sqrt(3D)<B+4`。

因此每个整数四项都大于 −1，必非负。此论证对搜索找到的任意合法三平方表示成立，不需要另筛一个幸运的符号组合。作者另外逐项核算非负、和及平方和，形成实例层的可靠再验。

追加非负 p,q 即得所需六项幅度。任意显式 ±1 符号赋值保持平方和与长度，因而数学全称结论成立。结论不声称列出所有达到者，也不最大化它们的 BRC 词数。

## 4. signed 身份与共同深度

辅助 b 来自非负幅度的平均值附近，不能当作实际 signed common-depth。原生深度是 `h=min_i z_i`，残差 `R_i=z_i−h`，必须联合保留

`z=R+h(1,1,1,1,1,1)`。

对 signed 端点，长度是 `Σ|h+R_i|`，不能一般替换成 `6h+ΣR_i`。后者是 signed 坐标总和。作者记录这两种量并保持区分。

独立实例 `N=25, signs=(1,−1,1,−1,1,−1)` 返回

`z=(3,0,2,−2,2,−2)`，`h=−2`，`R=(5,2,4,0,4,0)`。

直接计算平方和25、长度11。二十条联合切片中，每条都有 can3、该三坐标的共同 offset 及另三条遗漏 signed 坐标；独立检查不用作者 inverse 函数，逐坐标重建全部 z。这里局部 visible offset 未被错误等同于全局 h。

该端点词数为 `11!/(3!(2!)^4)=415800`；另一个达到者 `(3,3,2,1,1,1)` 同壳同长度，却有不同词数554400。两者没有被宣布为同一个 Cell。

还必须保留零幅度的符号退化：改变 z_i=0 那一轴的 sign 不改变 Cell，零壳所有 sign 选择都是同一 anchor。核心代码从未乘以虚假的 `2^6` 重数；作者已把输出元数据的措辞也修正为仅非零幅度的符号改变区分 raw Cell。

`origin_anchor=(0,...,0)` 是 helper 所用共同相对 chart 的锚点坐标，不宣称全局唯一的原生中心。此单元未改变 P000、原生正角或空间维数。

## 5. 初审资源问题及已复核修复

初始 helper SHA `de84d0edf99ed68e2a2845271e1b50510029ae071ecb6c91c328875fe3483fed` 存在两个实际边界问题，均先消息作者及 root，审计员未改作者源码。

1. `verify_endpoint` 在六项长度检查前先执行 `tuple(endpoint)`。一个100项 generator 会被全部消费，无限 iterable 则没有终止保证。最终版本要求显式六项 tuple/list；本次反例 generator 被拒且消费0项。
2. 对平衡壳 `N=6000000`，b=1000、k=6000。显式允许 `brc_event_budget=6000` 时，端点早已正确构造，但十进制词数超过当前 Python 默认4300位限制，`str(count)` 抛 ValueError，导致有效端点一并丢失。最终版本在这一确切转换处捕获资源失败，仍返回 `ENDPOINT_VERIFIED`，同时词数读出为 `RESOURCE_LIMIT/DECIMAL_CONVERSION_LIMIT` 并保留精确阶乘比，没有修改解释器全局限额。

另已修正文档的输出复杂度措辞：固定六轴的最短词数至多 `6^k`，故十进制位数为 `O(k)`；词数本身可指数增长。不能把两者混为“输出长度超线性”的断言。默认4000事件下该位数上界低于当前默认转换限制。

搜索候选数预算耗尽时抛 `ResourceLimit`，不是“无表示”。独立词数预算耗尽时保留已验证端点。预算只针对声明的候选数量与词数计算/序列化，不是所有任意大输入的总内存或 wall-clock 保证；全 N 数学存在性也不承诺所有 N 都在默认实现预算内完成。

## 6. 检查器与整份输出的边界

公开 `verify_endpoint(N,z)` 从实际 N 与六个 raw signed 整数重新核对平方和、长度和 U(N)，不信 construction 中的自报字段。无效 N、布尔/浮点坐标及错误端点均被拒。

它明确只验证 `THIS_RAW_SIGNED_ENDPOINT_ONLY`，不是整份 JSON envelope 的外部证书验证器。调用者不能只验证 N,z，就假设一份经他人改写的 `construction`、`native_common_depth`、joint slices 或词数字段也已核验。本次审计对生成器源码及生成的联合字段进行了独立重算；没有扩大公开 checker 的承诺。

## 7. 独立精确验证与冻结

运行：

```text
python experiments/owner_shell_length_audit_20260907.py
```

最终结果 `PASS`，JSON 为同名前缀文件。

- 用二元整系数多项式逐项运算，核验所有六行 B、D、t 上界和 margin 下界恒等式；这不是把 b,t 代入若干数后拟合公式。
- 仅选 `(b,r,t)=(0,0,0),(1,0,1),(0,1,0),(2,2,4),(0,3,0),(1,4,2),(0,5,1)` 七个必要参数边界，对应 N 为 `0,8,1,42,3,22,7`。不是 N 的前缀扫描。
- 单独核对 N25 的 signed 身份、20个联合切片、词数与不同达到者；零壳符号退化和空词数1。
- 非平衡零搜索预算中止；独立词数事件预算；6000事件十进制资源边界保留有效端点；错误输入/端点；generator零消费。

作者的61个选择性输入检查没有在本次重新执行，也不作为全 N 证明的替代。一般结论由第2–3节的全称代数和已核验的一手引理承担。

| 来源 | SHA256 |
| --- | --- |
| `research_notes/OWNER_SHELL_LENGTH_FRONTIER_20260907.md` | `5cec9acf830ec0600b8bc7dd45f4b081f771a69da0ab7c6e43ecb53a602d8bb4` |
| `experiments/owner_shell_length_20260907/shell_length.py` | `c77bc6342eb5c78072ccea1b70dc0ee90a6dd7676aab4d3de1aa9928c2f67065` |
| 同目录 `validate_selected_cases.py` | `5c8c8322971904f58af26bf53ec88abdbeb1ba2965355e96e4d1391d2ac76ba0` |
| 同目录 `validate_selected_cases.json` | `81df5c43c80cd7b459aac2a5d61c47d8accf0efb7cf5e97b42fdb187e3c642bf` |
| 同目录 `signed_N25.json` | `e385117ced049f7aa7b6bf672b7fe1c6436306241e0b89d885e19ce30f022e0d` |
| 既有 `signed_brc.py` | `6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4` |
| 既有 `x6_signed.py` | `e48b6f2133edc588fde98b1b0f02ce27fecda915b152b7901300898920d52b8e` |
| 本独立脚本 | `8622c37f735218e0c3c5e5d2de7f28bc9b9ebaf5e9d9de0daef847d29e5b6ebd` |
| 本独立结果 JSON | `ce99879c6ec8ca3f33b7a1902509f13aa662f5f3909e751d68f986546cb71a96` |

本次仅新写独立审计笔记和 `owner_shell_length_audit` 前缀检查文件；无作者源码、remote、catalog 或官方状态修改。
