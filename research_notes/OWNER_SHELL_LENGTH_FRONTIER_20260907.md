# signed X6 平方距离壳的最短词长度锐界：全 N 构造

状态：`ANCHOR_EXPOSED / ALL_N_CONSTRUCTIVE_RESULT / MENG_SUN_TYPED_REUSE / NOT_FOUNDATION`。

辅助工作包 `/root/exact_solver`，2026-09-07。不是正式 task、Researcher-ID、claim 或新工具 family。本报告关闭已冻结 scout 候选 A 的全称数学接口；不更改 P000、signed 原生坐标或旧 BRC 接口。

## 1. 精确结论与既有工具

固定同一 raw signed X6 anchor，令

\[
S_N=\{z\in\mathbb Z^6:\sum_i z_i^2=N\},\qquad
L_{\max}(N)=\max_{z\in S_N}\sum_i|z_i|,
\]

\[
U(N)=\max\{k\in\mathbb Z_{\ge0}:k^2\le6N,\ k\equiv N\pmod2\}.
\]

**对每个整数 `N>=0`，均有 `L_max(N)=U(N)`。** 以下按六个余类给完整构造，不需要 `N0` 阈值，也不需要有限前缀补证。

对任意端点，Cauchy–Schwarz 给 `(sum |z_i|)^2<=6N`，逐项整数奇偶给 `sum |z_i|≡N (mod2)`，所以 `L_max<=U`。只需构造六个非负整数，和为 U、平方和为 N。构造同时证明所有壳非空。

本任务复用 `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` 的原生 `spatial_norm_squared`、`shortest_event_count`、`shortest_path_multiplicity`、`endpoint_multiplicity`，以及同目录 `x6_signed.py` 的无损坐标与切片接口。覆盖入口已经在 `OWNER_NEXT_FRONTIER_SCOUT_20260907.md` 冻结；不重做固定端点的旧长度公式，也不把本轮构造称为新 BRC 代数。

## 2. 一手引理的完整前提及复用范围

已直接读取 Meng–Sun，*Sums of four polygonal numbers with coefficients*，Acta Arith. 180(3) (2017)，229–249，Lemma 2.4、式 (2.2) 与完整证明（印刷页 235–236）。[期刊原文](https://www.impan.pl/shop/en/publication/transaction/download/product/92360)，[作者 arXiv v4](https://arxiv.org/abs/1608.02022v4)。

使用大写 A、B 避免与下面的辅助中心 b 混淆。该引理的精确合同是：正整数 A、B 满足

\[
B^2<4A,\qquad 3A<B^2+2B+4,
\]

且满足以下之一：A、B 都奇；或者 `A≡2 (mod4)` 且 B 偶。则存在四个**非负整数**，和为 B，平方和为 A。本题只使用全奇分支；不删除严格不等式，不把非负性替换为任意有符号表示。

该现成引理并未按原生六轴壳的 U(N) 原样陈述结果，但下节六余类输入表完全将本题归入它。因此结果分类是既有固定和四平方定理的 typed reuse 与 native consumer 构造，不宣称原创一般数论定理或数学优先权。找到这条完整覆盖后停止另开通用二次型/大参数搜索路线。

## 3. 六余类的全称构造

记 `k=U(N)=6b+r`，其中 `b>=0,0<=r<6`，并定义

\[
N=6b^2+2br+r+2t.\tag{1}
\]

首先 t 是非负整数。奇偶条件保证 `N-(6b²+2br+r)` 是偶数；而

\[
N-(6b^2+2br+r)\ge -\frac{r(6-r)}6\ge-\frac32.
\]

不小于 `-3/2` 的偶整数必非负。这里没有预先假设六整数表示存在，也没有循环使用待证结论。

由于下一个同奇偶候选 `k+2` 已超出上界，`6N<(k+2)²`。代入 (1) 得

\[
12t<24b+r^2-2r+4.
\]

因 t 为整数，

\[
0\le t\le2b\quad(r=0,1,2,3,4),\qquad
0\le t\le2b+1\quad(r=5).\tag{2}
\]

若 `r=0,t=0`，直接取六个 b，覆盖 `N=6b²`，包括零壳。以下排除这个完全平衡情形。

先固定最后两项 p、q，令剩余四项的所需和与平方和为

\[
B=k-p-q,\qquad A=N-p^2-q^2,\qquad D=4A-B^2.
\]

采用下面的确定表：

| r 与条件 | (p,q) | B | D | 由 (2) 给出的 `(B+4)²-3D` 正下界 |
|---|---|---|---|---|
| 0，t>=1 | (b,b+1) | 4b-1 | 8t-5 | `16b²-24b+24` |
| 1 | (b,b) | 4b+1 | 8t+3 | `16b²-8b+16` |
| 2 | (b,b+1) | 4b+1 | 8t+3 | `16b²-8b+16` |
| 3 | (b,b) | 4b+3 | 8t+3 | `16b²+8b+40` |
| 4 | (b,b+1) | 4b+3 | 8t+3 | `16b²+8b+40` |
| 5 | (b+1,b+1) | 4b+3 | 8t+3 | `16b²+8b+16` |

逐行只是代入 (1) 的恒等式。第一行由 `1<=t<=2b` 得 b>=1，故 B 正；其他行 B 显然正。所有 B 奇，D 均为正且 `D≡3 (mod8)`，因而 `A=(B²+D)/4` 是正奇整数。

表内下界全部严格正。前两类可以分别写成

`(4b-3)²+15`、`(4b-1)²+15`，

其余两类在 b>=0 时每项非负且常数正。因此

\[
B^2<4A,\qquad 3D<(B+4)^2.
\]

由 `4A=B²+D`，后一个不等式恰好等价于 `3A<B²+2B+4`。Meng–Sun Lemma 2.4 的全部前提均已核验，包括两项严格性、正整数域和奇偶分支。

所以有四个非负整数 `a1,...,a4` 满足和 B、平方和 A。追加 p、q 后得到

\[
\sum_{i=1}^6a_i=k=U(N),\qquad\sum_{i=1}^6a_i^2=N.
\]

与上界结合，全 N 结论完成。不存在留待枚举的余类或小参数缺口。

## 4. 可执行构造与有限资源含义

窄 helper：`experiments/owner_shell_length_20260907/shell_length.py`。核心接口为

```python
upper_length(N)
reduction_parameters(N)
construct_endpoint(N, signs=(1,)*6, search_budget=1_000_000)
verify_endpoint(N, endpoint)
certificate(N, signs=(1,)*6, search_budget=1_000_000, brc_event_budget=4000)
```

非平衡时 D 恒为 `3 mod8`。沿原引理证明，可取三个奇整数平方和为 D，将每个根的符号选择为与 B 同余模 4，再用式 (2.6) 的整数变换生成四项。其非负性来自刚已核验的严格上界；helper 仍逐项重新核算四项非负、和 B、平方和 A，而后通过原 signed BRC 复核完整六项端点。

三平方子程序只枚举正奇数 `x<=y<=z`，界为 `x<=isqrt(D/3)`、`y<=isqrt((D-x²)/2)`，最后以整数平方根验证 z。每个三平方表示均可排序且必全奇，因此有限候选域完备；三平方定理保证域内有解。这里没有扩大固定 N 的六项壳分拆枚举，更没有以“没搜到”宣告反例。

由表可得 `D<=16b+11=O(sqrt N)`，候选对子数 `O(D)`，所以这是关于数值 N 的有限伪多项式构造，不宣称关于 `log N` 的快速算法。中途触发显式候选预算会抛出 `ResourceLimit`，CLI 返回 `RESOURCE_LIMIT`；这不否定数学存在性。

最短词数使用原 `shortest_path_multiplicity`，并与原 `endpoint_multiplicity(k,z)` 比较。固定六轴的最短词在每轴只使用一个符号，所以词数不超过 `6^k`，十进制位数至多 `floor(k log10 6)+1`，为 `O(k)`；词数本身可以随 k 指数增长。该读出有独立事件数预算：超限时保留已验证端点，同时该读出返回 `RESOURCE_LIMIT / EVENT_BUDGET` 与精确阶乘比表达式。显式调高事件预算后，若 Python 的整数十进制转换限制触发 `ValueError`，同样保留顶层 `ENDPOINT_VERIFIED`，仅将词数读出标为 `RESOURCE_LIMIT / DECIMAL_CONVERSION_LIMIT`，保留精确阶乘比及已算整数的位长度。程序不更改解释器的转换限制，也不以近似数冒充词数；默认 4000 事件预算保持该十进制输出在默认限制以内。

`verify_endpoint` 的外部输入为 N 与实际 raw signed z。端点必须是显式六项 `list` 或 `tuple`，先检查类型和长度，再检查整数坐标；拒绝 generator 等任意 iterable，且不消费其中元素。它只验证这个端点的 N 与最短长度恰等于 U(N)，不把一次 `valid` 当成全称定理的执行证明，也不依赖 construction 字段的自报结论。

## 5. 辅助均值、common-depth 与 signed 标签

b 是**非负幅度**平均值附近的计算中心，不是原生 common-depth。构造返回的 signed 端点为 `z_i=epsilon_i a_i`，其中每个 epsilon_i 为显式 ±1。它们的 N、最短长度相同，但一般是不同 raw Cell：改变非零幅度上的符号会改变 Cell，改变零幅度上的符号则不会。零壳的全部符号选择均给同一 anchor。没有将符号遗忘后的幅度向量替代原生身份。

输出仍以原生接口计算

`h=min z_i`、`R=can6(z)`、`z=R+hD_native`，

其中 `D_native=(1,1,1,1,1,1)` 是已有复合方向。这里的 D_native 与第 3 节临时整数判别量 D 不是同一个对象，更不是第七空间轴。

对任何 signed 输出准确保留

\[
N=6h^2+2h\sum R_i+\sum R_i^2,\qquad
\sum z_i=6h+\sum R_i,\qquad
\ell(z)=\sum_i|h+R_i|.
\]

只有全部坐标非负时才可以把最后一式替换为 `6h+sum R_i`。helper 同时保存真正 h、完整 R、raw signed z、二十张 can3 与每张的共同 offset、三条遗漏 signed 坐标；原生 inverse 接口逐张重建完整端点。

实际 `N=25` 构造得到幅度 `(3,0,2,2,2,2)`，辅助 b=1，而幅度本身的 common-depth=0。取显式符号 `(1,-1,1,-1,1,-1)`，返回

`z=(3,0,2,-2,2,-2)`、`h=-2`、`R=(5,2,4,0,4,0)`。

原 BRC 精确核验 `N=25,ell=11`，最短词数为 `11!/(3!(2!)^4)=415800`。原 scout 的另一个达到者 `(3,3,2,1,1,1)` 词数为 554400；两者达到同一个最坏最短长度，并不要求路径 multiplicity 相同。此处没有合并这两个原生端点。

## 6. 精确运行与来源绑定

```powershell
python -B experiments/owner_shell_length_20260907/shell_length.py 25 --signs 1 -1 1 -1 1 -1 --output experiments/owner_shell_length_20260907/signed_N25.json
python -B experiments/owner_shell_length_20260907/validate_selected_cases.py
```

实际结果：`ENDPOINT_VERIFIED`；选择性验证 `PASS`。后者只选 b∈{0,1,2,17}、全部六个 r、t 的下端/1/上端，共 61 个输入来检查公式分支实现与原 BRC；它不是 N 的前缀扫描，也不承担全称证明。还验证零壳空词数为 1、零坐标符号不区分 Cell、signed common-depth、20 个联合切片、错误端点/非法输入、零候选预算与独立 BRC 读出预算。独立审计发现的两项真实实现边界已修复，并补精确定点检查：无界 generator 被拒且消费数为 0；`N=6000000,search_budget=0,brc_event_budget=6000` 的平衡端点 `(1000,)*6` 仍为 `ENDPOINT_VERIFIED`，在当前默认 4300 位限制下仅十进制词数读出为资源不足，解释器限制保持不变。

| 文件 | SHA-256 |
|---|---|
| 复用 `signed_brc.py` | `6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4` |
| 复用 `x6_signed.py` | `e48b6f2133edc588fde98b1b0f02ce27fecda915b152b7901300898920d52b8e` |
| `shell_length.py` | `c77bc6342eb5c78072ccea1b70dc0ee90a6dd7676aab4d3de1aa9928c2f67065` |
| `validate_selected_cases.py` | `5c8c8322971904f58af26bf53ec88abdbeb1ba2965355e96e4d1391d2ac76ba0` |
| `validate_selected_cases.json` | `81df5c43c80cd7b459aac2a5d61c47d8accf0efb7cf5e97b42fdb187e3c642bf` |
| `signed_N25.json` | `e385117ced049f7aa7b6bf672b7fe1c6436306241e0b89d885e19ce30f022e0d` |

结论止于原生 component quadratic readout 固定时最短 primitive 词长的最大值及精确达到者。不改变原生正角、P000 或空间本体，不注册新工具 family，不自动启动 scout B；无提交、remote 或官方 publication 操作。

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
