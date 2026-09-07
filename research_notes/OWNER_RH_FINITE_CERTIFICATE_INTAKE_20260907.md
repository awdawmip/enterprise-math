# RH first-step N=8 reference 惯性证书的可执行接入审查

状态：`BOUNDED EXECUTABILITY INTAKE / REUSE FOUND / NO NEW CERTIFICATE RUN / NOT_FOUNDATION`。
日期：2026-09-07。辅助工作包：`/root/exact_solver`；非正式 task、claim、Researcher-ID。
本轮只写 intake：未重跑浮点扫描，未安装依赖，未执行长证书，未修改旧源码或冻结笔记。

## 1. 主要结论：旧对角积分缺口已有后续覆盖，reference 惯性仍需区分

可准确定位的严格程序是 `scripts/rh_log3_n8_arb_certificate.py`。它与旧 first-step 使用同一四个区间、每支前八个 Dirichlet sine 模式，共 32 维；用 Arb 球运算、闭式 Laplace 级数、Hurwitz-zeta 加速尾及严格余项球，构造 **cutoff-free 完整 Weil Gram 矩阵**，没有频率积分或 T 截断。

对应 `RH_LOG3_N8_ARB_POSITIVITY_CERTIFICATE_20260906.md` 已记录完整 eta=1 矩阵的生产 Arb 正定证书。因此不应为原 note 的“对角 [0,2000] 区间积分尚待实现”重复造一套频率积分器：同一子空间的严格 A、D 构建器已经存在。

但已记录的完整矩阵正定性不等于

`H_eta(B_ref) = [[eta^2 A, B_ref], [B_ref^T, D]]`，

`B_ref = B_prime + B_Cauchy`

在 eta<1 的负惯性证书。此 reference 刻意不包含完整 arch cross 的 regular 部分和 pole cross。五份主文件中未发现该 reference 的独立严格惯性结果；不能把 full-cross、eta=1 的旧 `CERTIFIED` 字样迁移到它。

## 2. 五份主文件及源程序追溯边界

本次只读五份主文件；额外检索只用于定位路径及工具名称，未展开其他 RH 路线。

| 文件 | 此次用途 | SHA256 |
| --- | --- | --- |
| `research_notes/RH_SINE_BASIS_ARCH_DIAGONAL_TAIL_INERTIA_CERTIFICATE_20260906.md` | 原请求的 sine 尾及惯性合同 | `aaf5d7ceda4c12e550f57533449b4d13f72fb80e6a530ca009f7ffcb210451c8` |
| `research_notes/RH_LOG2_LOG3_N8_THRESHOLD_INERTIA_DIAGNOSTIC_20260906.md` | 精确分支、prime/pole/reference 输入及旧 T=2000 浮点边界 | `68f9cac3329ceb74a30017c7275d7c8c169418e25a6e6093911043ef497f6d3b` |
| `scripts/rh_log3_n8_arb_certificate.py` | 后续可复用严格构建器，已读完整源代码 | `4e337855d8605125ded80c029022fdc950d1b92cf78ce772480a7b99b9dad49b` |
| `research_notes/RH_LOG3_N8_ARB_POSITIVITY_CERTIFICATE_20260906.md` | 同一子空间的已记录生产证书及边界 | `0ab4b8cf31fcf0574848681a93aaff6b33e4d09e657de439db7e953ead260356` |
| `.github/workflows/rh-log3-n8-arb-cert.yml` | 精确运行命令、版本及工作量上限 | `39f5741fb756543161129b8cda7046760a927d334d08da3f7dd5413fed1de446` |

旧浮点 diagnostic 没有给出其 T=2000 源程序路径。对当前 worktree 的 Python 文件作含 hidden/ignored 的限定关键词定位（`B_ref`、`B_Cauchy`、`leggauss`、`roots_legendre`、`digamma`），未定位出该旧四分支 reference 扫描源程序。因此只能确认 note 写明它采用浮点 Gauss–Legendre、浮点特征值和 cutoff/阶数差异诊断，**不能捏造其具体代码路径或断言其实际 dtype 是 numpy.float64**。这也不妨碍复用后来已保存的严格程序。

现成 strict 程序的入口及条目类型：

- 第 22 行 `from flint import arb, ctx`。
- 第 28 行 `make_basis`：超越常数、归一化、三角/指数值是 `arb`；乘法支撑端点 `aq,bq` 是 `Fraction`。
- 第 51 行 `zero_matrix`：`list[list[arb]]`，零元为精确 `arb(0)`。正交基的单位矩阵使用索引相等的精确 Kronecker 选择，不以数值积分近似 I。
- 第 106 行 `arch_partial`、第 293 行 `accelerated_tail`：严格实球矩阵。
- 第 340 行 `fixed_shift_overlap`：支撑交集决定使用 Fraction，随后公式值为 Arb 球。
- 第 352、366 行 `prime_matrix`、`pole_matrix`：可分别返回严格 finite prime/pole 球矩阵。
- 第 379 行 `interval_ldlt`：只接受每个 pivot 严格大于零；这是正定判定函数，**不是通用负惯性函数**。遇负 pivot 时返回 false 不能解释为算术错误或 reference 结论被否定。

## 3. 冻结的精确输入合同

空间窗参数是实常数 `L2=log(2)`、`L3=log(3)`、`ell_shell=log(3/2)`。保留原标签及完整顺序，不作 parity/inversion 合并：

| 标签 | 区间 | 源程序顺序，零基索引 |
| --- | --- | --- |
| S- | [-L3,-L2] | 0..7 |
| O- | [-L2,0] | 8..15 |
| O+ | [0,L2] | 16..23 |
| S+ | [L2,L3] | 24..31 |

每支 `phi_(a,ell,k)(x)=sqrt(2/ell)sin(k*pi*(x-a)/ell)`，k=1..8，支撑外为零。old 索引 O=(8,...,23)，shell 索引 S=(0,...,7,24,...,31)。最终 threshold 使用 old 然后 shell 的 16+16 顺序，必须显式记录此置换。

令完整 Weil 构造为 `M=M_arch+M_prime+M_pole`。使用严格程序时，目标对角块为

`A = M[O,O]`，`D = M[S,S]`。

它们包含各自的完整 arch 项、有限 prime 项以及 pole 项。有限 prime powers 是 `{2,3,4,5,7,8,9}`；每项权重 `Lambda(m)/sqrt(m)`，贡献 `-w_m(R_log(m)+R_log(m)^T)`。m=9 的极端相触只有零测度交集，由精确支撑判断返回零，保留在 prime-power 列表不等于声称其所有条目非零。

pole 保留两个函数 `l_+(phi)=integral phi(x)exp(x/2)dx`、`l_-(phi)=integral phi(x)exp(-x/2)dx`，矩阵为 `l_+l_-^T+l_-l_+^T`。不缩成未声明的 rank 1。

reference cross 则是

`B_ref = M_prime[O,S] + C[O,S]`，

`C_ij = -(1/2) integral integral phi_i(x)phi_j(y)/|x-y| dx dy`。

old/shell 内部支撑不相交，允许端点相接；这个 Cauchy 积分是有限的。此 B_ref **不加 pole cross，不加 arch regular cross**。完整 M 的 [O,S] 不能直接当 B_ref。

历史测试 eta 属于 `{9/10,99/100,999/1000}`，对应旧浮点负惯性候选 `{8,6,5}`。最小下一单元建议只冻结 eta=9/10，候选 q=8；这是假设待验，不能把旧计数作为验证器输入事实。

历史频率 cutoff 是精确整数 T=2000。若改用已存在的严格系列构造，则 A、D 目标仍是相同 cutoff-free 对角块，计算参数变为 `K=10000,P=10,precision=384 bits`；不存在新的频率 cutoff。K 是 Laplace 级数前缀长度，不能混称 T。

## 4. 既有 PSD 尾合同的保留方式

若仍使用旧频率截断路线，实基的条目合同必须写成

`Delta_arch(T)_(ij)=(1/pi)integral_T^infinity h(t) Re(conjugate(F_i(t))*F_j(t))dt`，

`h(t)=Re psi(1/4+it/2)-log pi`。

这是实对称 Gram。原尾 note 的 `F^*F` 简写在实基上应按此实部或等价实二分量表示读取；不能把正频率复 Hermitian 矩阵的虚部无说明地塞入原实矩阵。

对 T>max(7,8*pi/ell)，已给定理为

`0 <= Delta_arch(T) <= b(ell,8,T) I`，

`b(ell,N,T)=[16/(pi*ell)] * (3log(T)+1)/(9T^3)`

`              * sum_{k=1}^N (k*pi/ell)^2/[1-(k*pi/(ell*T))^2]^2`。

old 和 shell 分别代入 log2、log(3/2)。在 B_ref 本身固定或另有已证明区间包围的前提下，

`H_eta,infinity = H_eta,T + E`，

`0<=E<=beta I`，`beta=max(eta^2 b_old,b_shell)`。

若已严格知道 H_eta,T 有 q 个负特征值且最大负特征值 `<-beta`，则 cutoff-free 负惯性仍为 q。尾为 PSD 不会把非负值变负，但可能消除负值，故缺口条件不能删除。

历史 `1.018379e-5`、`5.092069e-5` 是公式高精度显示值；严谨执行时应以 Arb 或其他证明性外舍入包围公式，再导出有理上界，不能把显示小数本身自动当外界。finite matrix 四舍五入/积分误差与 PSD 尾是两个不同预算。

如果采用本次找到的 cutoff-free Arb A、D 构造，则它们的尾已包在条目球里，不应再叠加上述频率尾。这是复用同一目标的另一严格表示，不是把旧缺口省略。

## 5. 真正剩余的最小数值单元

### 5.1 reference 的 Cauchy cross

现成生产脚本有完整 arch cross，但没有 B_Cauchy 函数。最小可执行转换可复用其第 80 行 `ordered_distinct_laplace`。

对左支 i、右支 j，记

`L_ij(c)=integral integral phi_i(x)phi_j(y)exp(-c(y-x))dxdy`，

则

`C_ij=-(1/2)integral_0^infinity L_ij(c)dc`。

这是 `1/s=integral_0^infinity exp(-cs)dc` 的直接应用。有限支撑正弦有界，角点的 1/(u+v) 局部可积，故对绝对值也可交换；无需把符号积分假装为正分支求和。

源码已保存 L_ij 的有理-指数闭式，指数差都非正，分母为 `(c^2+alpha_i^2)(c^2+alpha_j^2)`；实正轴没有奇点。它可在新消费者中适配 `acb.integral` 来严格包围有限 c 区间；这是后续实现建议，本轮没有调用。官方 [python-flint acb 积分接口](https://python-flint.readthedocs.io/en/latest/acb.html) 要求正确处理 analytic 回调，并允许有限 eval/depth 工作量限制；这类 meromorphic 闭式由极点产生非有限球即可暴露不适用区间。上限耗尽只能返回未定，不能变成数学反证。

截断 c>=C0 的简单独立条目界为

`|(1/2)integral_C0^infinity L_ij(c)dc|`

`<= 2 norm_i norm_j alpha_i alpha_j/(3 C0^3)`。

原因是闭式的四个指数项绝对值之和<=4，分母>=c^4。old/shell 每项使用 `pi<4`、`log2>2/3`、`log(3/2)>2/5`，可统一取 `norm_i norm_j<4`、`alpha_old<48`、`alpha_shell<80`，因而条目尾 `<10240/C0^3`。这两个 log 下界也可由 `log((1+u)/(1-u))=2(u+u^3/3+...)` 的首项直接确认。

例如 C0=20000 给每个 cross 条目尾 `<1.28e-9`，16×16 cross 的算子尾可用最大行/列和给 `<2.048e-8`。这是透明但保守的可执行预算，不是已经包围有限 c 积分，也不是根据旧浮点 q 直接发证。C0 与历史 arch 频率 T 是不同变量。

### 5.2 带符号惯性及可独立核验输出

现成 `interval_ldlt` 的正 pivot 逻辑不能直接调用来数 q 个负值。最小扩展可以是所有 pivot 球都严格避开零的带符号 LDL；必要时明确置换或 2×2 pivot，不能把包含零的球误判为零特征值。

更便于独立复核的证书格式是：严格生产者导出对称矩阵的有理外包区间，验证器用精确有理合同检查惯性夹逼，不需要信任浮点 eigenvalues。

建议的最小包（下列是格式要求，不是已生成的证书）：

1. `input`：四支端点的 log-rational 表达、模式顺序、old/shell 置换、prime-power 字典、两个 pole 通道、B_ref 的明确排除项、eta 的有理数、目标为 cutoff-free 及 K/P/precision/C0 参数。
2. `construction`：所复用脚本 SHA、库/解释器版本、实际参数适用性断言、每个条目的外包上下界、独立解析尾界及其计入位置。上下界以精确有理数或 dyadic 数存储；不可把显示用的截短 midpoint/radius 文本无补偿地重新解释为球。
3. `matrix`：上三角有理区间，镜像为对称矩阵；有理中心 M 和半径 R；验证 `delta >= max_i sum_j R_ij`，从而 `||H-M||<=delta`。
4. `inertia_witnesses`：对 `M-delta I` 和 `M+delta I` 分别给有理可逆合同变换及对角/2×2 分块 D；精确验证矩阵恒等式、变换可逆和每块符号，两者负惯性必须同为 q。此时 Loewner 单调性使区间内真矩阵也有 q 个负值。
5. `result`：只允许 `CERTIFIED(q,declared_basis,declared_eta)`、`UNDETERMINED` 或 `INVALID_CERTIFICATE`。不得把资源不足或包含零的区间变成已证明的谱结论。

若走旧 T 截断路线，第 4 项的上夹逼改成 `M+(delta+beta)I`，下夹逼仍是 `M-delta I`，可一次把有限数值误差与正尾分开验证。复用 cutoff-free 生产者则 beta=0，因为尾已在条目区间。

有理后验惯性检查只证明“若输入条目区间确实包围目标，则惯性正确”。完整可独立重放还必须复算或审定第 2 项的严格条目构造；一包任意自报区间及 LDL 数字本身不够。

## 6. 环境、资源与最小下一动作

本次只读环境检查显示：当前 `python` 为 Windows CPython 3.14.6，`importlib.util.find_spec('flint')` 返回 None。numpy/scipy 可定位，但这不会提供 Arb 严格性；本轮没有安装或更改解释器。

现成 workflow 的可复用环境是 Python 3.13，`python-flint==0.9.0`，命令为

`python scripts/rh_log3_n8_arb_certificate.py --K 10000 --P 10 --prec 384`。

workflow timeout 为 15 分钟；这是已有配置上限，不是本轮实测耗时。旧生产 note 记录 Python 3.13.15、workflow run 34022226755/job 101456774145、source head d0a4eca2a49a9167848ba4d5d5cfd7eb03d355f7。本轮没有重新查询远端或重放该运行，不将历史日志视为新 reference 的证明。

工作量可先按既有算法定界：arch 前缀为 K×32²，约 1024 万个条目级 Laplace 计算；矩阵本体仅 32×32；reference 新增最多 16×16=256 个一维 Cauchy 条目，有限求积必须有单项 eval/depth 限额。两次 32 维有理或区间惯性后验检查相对小；实际壁钟和精度增长要由首个严格运行计量，不能从浮点扫描时间推测。

源码 remainder 公式还要求 `1-rho>0` 等收敛条件。当前固定 K=10000、P=10 处于已有生产合同内；适配器必须显式验证这些不等式及 K>0，不把脚本只检查 P>=6 的命令行接口当成所有 K/P 都已获证明的通用 API。

建议后续只执行一个最小单元：准备已知可用的 pinned Arb 环境；复用现成 cutoff-free A、D 和 prime 构建器；实现并导出 Cauchy cross 的严格区间；在 eta=9/10 上给完整参考矩阵及独立惯性包。首先争取 q=8，但验证器不得依赖这个候选。是否实施由 owner 根据本 intake 决定；本轮没有新增求解器或参考矩阵。

本次可以关闭的重复工作是“为同一 N=8 对角块重新开发频率区间积分”。仍未由本次五文件覆盖闭合的是“prime+Cauchy reference、eta<1 的可重放负惯性包”。不转入 Galerkin complement，不扩大到完整 H_log3，更不扩大到 RH 证明。

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
