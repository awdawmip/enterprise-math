# Owner arithmetic frontier — X6 最短路径 BRC 的完整素数幂整除谱

辅助工作包：`/root/stability_research`，本轮轮换为数论路线研究辅助。
模式：`ANCHOR_EXPOSED / TASK_HELPER / NOT_CLEAN_FREE`。
未注册正式 task、claim、Driver review；不继承其他会话权限。
Global canonical read snapshot：`4fa7d7d0c19a5e80a681b33c8ee2ab643ce97563`（owner 已验证本轮有效读租约）。
P000、current signed X6 Cell torsor 与 positive Weighted-BRC 语义沿用已读 current foundation router。

## 冻结候选（详细工具覆盖前固定，不回改）

候选比较限定三个，不扩展目录巡视：

| 候选 | 已有结果及本轮处置 |
|---|---|
| 平方根 basin 的乘法分支交互 | `BRC_MULTIPLIER_BASIN_THEOREMS_20260906.md` 已有固定乘子的精确 support/weight 律；本轮未找到强于已闭合结果的最小独立单元，暂不选择。 |
| centered-prime radius 与 near-diagonal factor slack | `centered_prime_radius.py` 已有明确假设下的闭合等价式；不重跑，也不将其提升为 Goldbach 或无条件素数对存在性。 |
| X6 最短路径计数的素数幂整除谱 | `20260906T122500+0800-x6-layer-frobenius-multiresolution-progress.md` §5 已给出正正交层 Lucas 模 p 非零位置及个数；本轮选择完整 p-adic 阶数分布，并扩到全 signed 原生壳层，保留坐标/正负方向标签。 |

**冻结问题。** 对所有 \(N\in\mathbb N_0\) 与已声明素数 p，令原生完整 signed 六轴壳层为
\(S_N=\{z\in\mathbb Z^6:\sum_i|z_i|=N\}\)。
每个端点的最短原生路径 BRC 计数是 \(C_N(z)=N!/\prod_i|z_i|!\)。研究完整整数多项式

\[
H_{N,p}(t)=\sum_{z\in S_N}t^{v_p(C_N(z))}.
\]

目标是有限进位状态与活跃轴数状态的精确转移公式，给出自足证明，
并以连续、完整的有限 N0 census 交叉核验。零次系数应退化为已有 Lucas 非零层；
更高系数区分 p、p²、p³ 等整除阶，不将已有零次结果重新包装成新结论。

人口与类型：外层 N0 全域包含0、1、偶数和合数；有限检查不得预先删去任何半径。
p 是素数参数而非被筛掉的半径。乘法结构通过精确整数阶乘商及其 prime valuation 使用；
坐标确实适用，因为端点是 current native X6 signed Cell 位移，维度固定为六。
空间端点数、最短路径数、正权 BRC 的质量/直方图及 signed 方向标签保持分层。

kill 边界：若内部已有同一 complete-valuation/full-signed 结果则转为复用，不重新立项；
若数字进位或活跃轴更新不能逐端点一一对应则否决转移式；有限吻合不能替代一般证明。
不声称素数生成、新的分解复杂度、generic semiprime factoring 突破或 Foundation 提升。

## 审计、证明与精确结果

### 1. 覆盖、去重与本轮实际增加的信息

本节在上述问题冻结后形成。有限内部检索覆盖了 existing weighted histogram、prime-valuation transfer、X6 layer Frobenius 和 root-basin 路线；不把有限检索写成全库不存在证明。

| 现有工具或结果 | 处置与实际调用边界 |
|---|---|
| `definitions/00_CURRENT_NATIVE_FOUNDATION.md` 的 signed X6、L1 距离及 multinomial 最短路径数 | `REUSE_APPLIED`：直接使用原生六轴位移及 `N!/prod(abs(z_i)!)`；没有用外部三维表示替代 X6。 |
| `src/enterprise_math/brc_histogram.py` 的 `WeightHistogram`、`histogram_serial`、`histogram_recoalesce` | `REUSE_EXECUTED`：下述程序每个数字转移调用现有正权 serial/recoalesce，终态使用现有 `prime_valuation_terms()`；不是只列出工具名。 |
| `BRC_PRIME_VALUATION_UNIVERSAL_TRANSFER_20260903.md` 的 valuation/Laurent observer | `COMPOSE_APPLIED`：以 `p^e` 编码单一素数赋值，明确为原端点权重的投影；不建立新 BRC family。 |
| 已有 positive-orthant Lucas 非零个数 | `REUSE_EXECUTED`：每个小域实例核对 `prod_j binom(n_j+5,5)`，仅作为旧结果的回归锚点。完整 signed 非零数是其带支撑大小的提升，并非不加修改地等于该乘积。 |
| multiplier scan、Pell error linearization、idempotent path closure、typed signed circuits | `NOT_APPLICABLE`：当前无固定乘子 basin、近似误差、无限闭包或路径差消去问题；数字进位是有限正权计数。 |
| generic moment transfer | `REUSE_APPLIED` 于投影后 BRC 的标准语义；不需要再造矩矩阵，不从单个投影矩恢复原权重。 |

覆盖原始结果：`owner_arithmetic_20260907_coverage.json`。

**外部精确 prior art 命中。** Eric Rowland 的 [A matrix generalization of a theorem of Fine](https://ericrowland.github.io/papers/A_matrix_generalization_of_a_theorem_of_Fine.pdf) §2、Theorem 3 已给出任意 k 个非负加数的完整 multinomial p-adic 谱的数字矩阵；该文同时给出 multinomial Kummer 公式及其 Legendre 推导。矩阵方法与一般素数赋值恒等式是已知方法。下文是自足复核和原生 signed X6 / positive BRC 的具体组成，**不声称方法新颖或全局首创**。

本轮真实局部缺口被缩小为：内部原有模 p 零/非零表不能回答完整 signed 壳层有多少端点的最短路径数恰含 p 的 e 次幂。现在有精确可运行的观察器；同时确认这是一项已有数学方法的 typed native adaptation，不是新算术理论或新公理。

### 2. 进位值公式及边界

固定 `N in N0`、素数 p，写 `N=sum_{j=0}^{L-1} n_j p^j`，按低位至高位处理；N=0 约定 L=1、n_0=0。
对每个端点令 `b_i=abs(z_i)`，写 `b_i=sum_j d_{i,j}p^j`。因 `0<=b_i<=N<p^L`，无需 L 位之外的非零数字。
进位定义为

\[
c_0=0,\quad \sum_{i=1}^6d_{i,j}+c_j=n_j+p c_{j+1},\quad c_L=0.
\]

每个 c_j 都在 `{0,1,2,3,4,5}`：若 `c_j<=5`，则分子 `sum_i d_{i,j}+c_j-n_j<=6(p-1)+5=6p-1`，因此整数 `c_{j+1}<=5`。真正的加法进位非负。
反向地，任何 L 位带标签数字数组与这些守恒式、初末零进位相容，加权求和即得 `sum_i b_i=N`；这是精确壳层条件。

自足地数 m! 中每个 p 的倍数、p² 的倍数等，得到

\[
v_p(m!)=\sum_{q\ge1}\lfloor m/p^q\rfloor
=\frac{m-s_p(m)}{p-1}.
\]

后一个等号把 m 的有限 p 进制展开代入即可逐项相加。故

\[
v_p(C_N(z))=\frac{\sum_i s_p(b_i)-s_p(N)}{p-1}
=\sum_{j=0}^{L-1}c_{j+1}.
\]

最后一步把各位守恒式不加 p^j 权重地求和，利用 `c_0=c_L=0`。
这里加的是**进位数值**，不能只数“发生进位的位数”。例如 `N=6,p=2,b=(1,1,1,1,1,1)`，N 的低位数字是 `(0,1,1)`，进位 `(3,1,0)`，赋值为 4，且 `C=720`；非零进位位置仅两个。

终态 `c_L=0` 不能省略。最小反例可取 `N=0,p=2,L=1`，两个轴数字1会产生 `c_1=1`；若接受该终态便把 L1 半径2的端点计入中心。

### 3. 42 个进位/活跃数状态的完整 signed 转移

令 r 表示当前低位前缀中**至少出现过一次非零数字**的轴数。定义

\[
U_p(x)=1+x+\cdots+x^{p-1},\qquad V_p(x)=x+\cdots+x^{p-1}.
\]

从状态 `(c,r)`，选 a 个新激活轴、转入 `(c',r+a)`，其中 `0<=a<=6-r`。当前数字为 n_j 时令 `S=n_j+p c'-c`，转移多项式为

\[
\boxed{\quad
\binom{6-r}{a}[x^S]U_p(x)^rV_p(x)^a\;t^{c'}.
\quad}
\]

负次数或超出多项式次数的系数视为0。初值 `F_0(0,0)=1`，其他为0，逐位按上式累加。最终

\[
\boxed{\quad H_{N,p}(t)=\sum_{r=0}^6 2^r F_L(0,r;t).\quad}
\]

**证明。** 对一条已处理的、带轴标签的数字历史，活跃 r 轴当前可取任意数字；新激活 a 轴必须取非零数字，剩余轴必须取0。先从未激活的 `6-r` 轴中选 a 个，再用系数抽取统计每个带标签轴的有序数字选择，正好给出上述系数。所有具有相同 `(c,r)` 的历史拥有相同续接计数，因此按 r 合并是对称计数的充分状态，无需假定不同历史有相同轴身份。每次 t 的指数是当前输出进位，上一节给出其总指数。每个完整非负六元组有 r 个非零坐标，恰有 `2^r` 个 signed 端点；零坐标只有一个符号，不可乘2。初末进位条件保证完整且不重不漏，证毕。

所以 N=0 得 H=1，N=1 得 H=12。若在某轴每次非零数字处都乘2，会把同一坐标的符号重复选择；允许在首次激活时乘 `2^a`，但那时必须取消最终 `2^r`。当前实现只用最终权重。

实际保留的终态联合观察量是 `(非零轴数 r, p-adic 阶数 e)`，同时返回其 signed histogram。固定问题的输入保留六个坐标/方向标签；**该压缩输出并不保留具体轴身份或具体正负号**。如下一问题依赖某一轴、扇区或符号关联，必须回到带标签数字历史或扩大状态，不能从本谱反演。

### 4. 与已知无符号矩阵的独立拼接恒等式

令

\[
T_{p,k}(N,t)=\sum_{b\in\mathbb N_0^k,\;\sum b_i=N}
t^{v_p(N!/\prod b_i!)}.
\]

约定 `T_{p,0}(0,t)=1`，`T_{p,0}(N,t)=0` 对 N>0。则

\[
\boxed{\quad H_{N,p}(t)=\sum_{k=0}^6\binom6k(-1)^{6-k}2^kT_{p,k}(N,t).\quad}
\]

证明可固定一个六元组，其非零支撑大小为 s。右边相当于选择允许非零的轴集 K；该元组出现在每个包含其支撑的 K 中。总系数为
`sum_{K contains supp(b)} (-1)^(6-|K|) 2^|K| = 2^s(2-1)^(6-s)=2^s`，正是 signed 提升。其 multinomial 权重不因补零而改变，故逐指数成立。N=0 的 k=0 项不能省略。

该式把本问题完全接回 Rowland 的已知 T 矩阵，也给出独立核验路径；负号只是容斥计算账本，**不是正权 BRC 的分支质量**。实际 positive BRC 程序采用上一节的非负转移，避免在 carrier 中塞入负质量。

### 5. BRC 的精确复用与观察顺序反例

当前 `WeightHistogram` 的转移分支权重取 `p^c'`、分支重数取上述非负整数系数；既有 serial 乘权重，recoalesce 合并并保留重数。终态另接权重1、重数 `2^r` 的符号分支。结果权重为 `p^e`，其计数就是 H 的 t^e 系数。

这里存在三种必须区分的对象：

1. 原生有序最短路径，每条单位步骤序列保留路径身份。
2. 固定端点聚合后的一条 declared aggregated branch，权重为整数 `C_N(z)`；到此已失去原路径 identity。
3. 再投影后的 valuation histogram，权重为 `p^v_p(C_N(z))`；到此还失去 p-coprime unit，以及本观察器显式忘掉的端点标签。

步骤2是先读取固定端点 fiber 的 path-count observer，再为这个端点声明新权重；它不等于直接对步骤1的 `WeightHistogram` 调用 `histogram_recoalesce`。后者保留权重1并增加其重数，不会自动把两个权重1改成一个权重2。

不能把步骤1中每条路径的单位权重先作 valuation，再推断步骤2的计数赋值。`N=2,z=(1,1,0,0,0,0)` 有两条路径，各自权重1、v2=0；端点聚合权重为2、v2=1。赋值不与这类质量相加交换。

即便本谱完全正确，也不等于原始 endpoint-weight histogram。`N=4` 时 `b=(3,1,0,0,0,0)` 与 `b=(2,1,1,0,0,0)` 的权重分别为4和12，v2同为2，coprime units 分别为1和3。故不能从本谱恢复原完整权重、其他素数数据或符号联合信息。

同一合数半径还给出“旧模 p 表不够”的精确反例：`b=(3,1,0,...)` 的 C=4、v2=2，而 `b=(2,2,0,...)` 的 C=6、v2=1。两者模2均为0，但仅前者被4整除。新观察确实增加了旧 Boolean divisibility 层没有的信息。

### 6. 可执行精确核验

文件：

- `owner_arithmetic_20260907.py`：已有 BRC carrier 的 42 状态组成；`signed_valuation_spectrum(N,p)` 返回 projected histogram 及 `(r,e)` 联合计数。
- `owner_arithmetic_20260907_check.py`：用整数阶乘商直接独立枚举每一个 signed 端点，不以进位递推作真值 oracle。
- `owner_arithmetic_20260907_results.json`：实际运行结果。

执行：

```powershell
$env:PYTHONPATH = 'D:/em/owner-20260907/src'
python research_notes/owner_arithmetic_20260907_check.py
```

结果 **PASS**：完整连续半径 N=0..10，参数 p=2,3,5,7，共44个 `(N,p)` 实例。实际枚举134245个 signed 端点，完成536980个端点/素数赋值检查；每一实例核对完整谱、`(r,e)` 联合谱、精确壳层总数、无符号 Lucas 常数项以及上一节容斥提升。
全部0/1/偶数/合数半径先进入 census，再标记 `zero/unit/even/prime/composite`，未使用“显然合数”删域。

明确的全谱样例：

\[
H_{0,2}=1,\quad H_{1,2}=12,\quad H_{2,2}=12+60t,
\]

\[
H_{4,2}=12+60t+600t^2+240t^3.
\]

N=4 的912个端点也可按绝对值型手验：`(4)` 12个；`(3,1)` 120个；`(2,2)` 60个；`(2,1,1)` 480个；`(1,1,1,1)` 240个。对应 C 分别是1、4、6、12、24。程序还专门验证 N6,p2 的大于1进位见证。

另在半径 `10^6+1` 和 `10^12+39`、p=2,3,5 上运行六个数字算法实例，逐一核对谱总系数与
`sum_{r=1}^{min(6,N)} 2^r binom(6,r) binom(N-1,r-1)`。这些大域实验**只核对闭式端点总数**，未冒充逐端点赋值 census 或一般证明。

实现有明确资源边界：默认 `p<=31`、至多256位；可显式调整。超出时抛 `ComputationBudgetExceeded`，不返回“数学无解”。负半径、bool/非整数、合数 p 有明确异常；合数 **N** 则合法。六个输入/预算边界检查均通过。有限状态不等于常数总内存：指数谱和精确整数位长仍随 N 增长，未给出 factoring 或次输入规模复杂度承诺。

独立数学审查：`/root/exact_solver` 复核了初末进位、carry<=5、进位值求和、active-axis 充分统计与容斥 lifting，并明确其标签遗失边界；该辅助消息审查不是正式 Driver record。一般结论由第2—4节的有限恒等式证明，实验只检查实现。

### 7. 本单元处置与真正未覆盖的下一可判别条件

处置：**本地数学单元完成 / 已有方法组成 / 不申请新工具 family 或数学新颖性。** 已补足本地 full-signed valuation 观察接口，不能以 PASS 自动续写同一算法。

仍未覆盖的一个明确母题是单位部分：对给定 `m>=1`，联合统计 `(r,e,u)`，其中 `u=(C_N/p^e) mod p^m` 且 gcd(u,p)=1。当前反例 C=4/12 已证明 e 不足以决定 u；若后续问题确需这项观察，可先核对已有 factorial-unit/Granville 类主来源，再判断是否需要有界 residue-state 扩展。没有相关问题需求时应 park；不能把当前谱或有限拟合直接当作单位谱，也不能声称得到了素数分布、素数生成或一般分解算法。

辅助工作包：`/root/stability_research`。

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
