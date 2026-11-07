# PREFIX-574：门控保留的 14 阶多项式不可约性与五态核心的特殊化缺陷

**Researcher-ID:** `EM-DIRECT-3EE30C` / `TASK_RESEARCH`  
**Research-Activity-ID:** `RA-RESEARCH6-20261108T050500-AA69DC`  
**Session-ID:** `local-em-research6-3ee30c-20261108T050500`（本地分配的稳定会话键，不是 Source-native session）  
**Science pin:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`  
**Status:** `AUTHOR_PROVED / EXACT_SYMBOLIC_CHECKED / FINITE_FIELD_CERTIFIED / UNREVIEWED / NOT_ADMITTED`

## 1. 研究边界与承接

本研究沿用冻结四 STAR 原生 X6-BRC 输入：96 个有序原生端口、6 种动作、9 种允许根；第五、第六轴仍以独立变量 \(x,y\) 保留，随后仅以其对称观察坐标
\[
u=x+y,\qquad v=xy
\]
表达交换不变的系数；门控变量 \(z\) 始终保留。没有把 \(z\) 特化为 1 来代表完整门控观察，也没有改变 P000 的原生轴、端口或坐标定义。

本轮承接：
- `research_notes/portable_direct/2026-11-08_prefix572_uniform_gate_affine_14_pair_recurrence.md`：37 类加权观察、17/20 二分、14 阶门控保留递推；
- `research_notes/portable_direct/2026-11-08_prefix573_sharp_hankel_observer_order.md`：37 个观察状态的奇、偶长度序列均达到最小阶数 14；
- `research_notes/portable_direct/PREFIX572_published_compact_certificate.py` 与 `PREFIX573_published_certificate.py`：既有精确证书。

本轮问题不是继续降低完整门控观察的标量递推阶数，而是检查 14 阶对象能否沿 \(z=1\) 的五态核心作固定谱分解，以及标准标量 companion 正锥是否成立。

## 2. 14 阶多项式的通用不可约性

从冻结的 96 端口动作边重新构造 37 类带权商，得到分区增长
\[
1\to4\to13\to21\to33\to37,
\]
其无向支撑图二分为 17 与 20 两侧。门控边仍仅由第 4、15、17 类指向第 5 类。对 17×20 与 20×17 的双步矩阵构造特征多项式，并除去既有门控无关三次因子
\[
Q_3(L)=L^3+4L^2-(32u+16v)L+192v,
\]
得到 PREFIX-572 的 monic 14 阶多项式 \(Q_{14}(L;u,v,z)\)。本轮独立重建的特征多项式有 258 个非零项，\(Q_{14}\) 有 159 个非零项。

### 定理 1

\[
\boxed{Q_{14}(L;u,v,z)\text{ 在 }\mathbb Q(u,v,z)[L]\text{ 中不可约。}}
\]

**有限域证书。** 取素数 \(p=1\,000\,003\)，作形式参数特化
\[
(u,v,z)=(9,26,13).
\]
所得 monic 14 次多项式在 \(\mathbb F_p[L]\) 中的升幂系数（从常数项到 \(L^{14}\)）为：
\[
\begin{aligned}
(&223637,153699,569254,156237,128645,18670,778724,\\
 &11058,209508,167802,663485,633859,988915,999995,1).
\end{aligned}
\]
Rabin 判据的精确模多项式运算得到
\[
L^{p^{14}}\equiv L\pmod f,
\]
且
\[
\gcd(f,L^{p^2}-L)=1,\qquad
\gcd(f,L^{p^7}-L)=1.
\]
因为 \(14=2\cdot7\)，这证明该特化在 \(\mathbb F_p\) 上不可约。

**提升论证。** \(Q_{14}\) 关于 \(L\) 是 monic，系数环 \(\mathbb Z[u,v,z]\) 是 UFD。若它在分式域 \(\mathbb Q(u,v,z)\) 中可约，则由 Gauss 引理可取正次数 monic 因子，且因系数环正规、原多项式 monic，因子可在 \(\mathbb Z[u,v,z][L]\) 中取 monic 形式。对上述参数与模数特化仍会得到同次数的非平凡因式分解，与有限域不可约性矛盾。

本结论的系数域明确为 \(\mathbb Q(u,v,z)\)。不据此声称在进一步加入 \(x,y\) 的二次扩张 \(\mathbb Q(x,y,z)\) 后仍不可约。

## 3. 五态核心只在 \(z=1\) 特化时成为谱因子

PREFIX-565 的五态门控求和矩阵记为 \(M_5(x,y)\)。令 \(Q_5(L;u,v)\) 为 \(M_5^2\) 的特征多项式；对 \(x,y\) 对称化后得到
\[
\begin{aligned}
Q_5(L;u,v)={}&L^5-4L^4-(192u+288v)L^3\\
&-(2304u^2+3456v)L^2\\
&+(-82944uv+20736v^2)L-746496v^2.
\end{aligned}
\]

另定义
\[
\begin{aligned}
S_5(L;u,v)={}&L^5-4L^4+(64u-32v)L^3\\
&-(256u^2+384v)L^2\\
&+(3072uv+256v^2)L-9216v^2.
\end{aligned}
\]

### 定理 2（特殊化因式分解与通用提升缺陷）

在 \(z=1\) 时，存在精确因式分解
\[
\boxed{
Q_{14}(L;u,v,1)=Q_5(L;u,v)\,R_9(L;u,v)
}
\]
其中
\[
\boxed{
R_9(L;u,v)=(L-4)Q_3(L;u,v)S_5(L;u,v).
}
\]

但对一般 \(z\)，以同一个五态核心 \(Q_5\) 作多项式除法，得到
\[
\boxed{
Q_{14}(L;u,v,z)
=Q_5(L;u,v)S^{\rm gen}_9(L;u,v,z)
+(z-1)R_4(L;u,v).
}
\]
其中 \(S^{\rm gen}_9\) 的 \(L\) 次数为 9、非零项数为 131；\(R_4\) 的 \(L\) 次数为 4、非零项数为 106，且与 \(z\) 无关。最短非零见证为
\[
\boxed{[L^4u^2]R_4=-12\,582\,912\ne0.}
\]

因此 \(Q_5\) 在 \(z=1\) 是 \(Q_{14}\) 的精确因子，但不是一般 \(z\) 下的因子。通用提升的首个精确除法缺陷恰好带因子 \(z-1\)。这排除了“保持同一 \(Q_5\)，只补一个九阶因子”这种固定谱分拆；并不排除带非对角耦合的 14 维实现或其他正锥。

## 4. 标准标量 companion 正交锥失败

写
\[
Q_{14}(L)=L^{14}+c_1L^{13}+\cdots+c_{14}.
\]
相应标量递推的 companion 首行系数是 \(-c_j\)。第二滞后系数精确为
\[
c_2=-4(2uz+38u+84v+z-1),
\]
故
\[
-c_2=8uz+152u+336v+4z-4.
\]
其中常数单项式系数为 \(-4\)。所以标准 monomial coefficientwise nonnegative orthant 并不被该 14 阶 companion 映射保持。

这只是对**标准坐标正交锥**的精确反例；不能据此声称不存在其他多面正锥。原 37 类转移矩阵仍是非负的，故 37 状态正实现仍然存在。

## 5. 验证范围

独立证书 `PREFIX574_irreducibility_certificate.py` 从冻结四 STAR 原生边重新构造 96 端口、9 根、37 类带权商与 17/20 二分，并精确重算 \(Q_{14}\)、\(Q_5\)、特殊化因式分解、通用除法余项和 companion 符号见证。

- 96 个原生端口、6 种动作、9 种根；
- 加权分区增长严格为 `[1,4,13,21,33,37]`；
- 门控来源 `[4,15,17]`，目标类 `5`；
- 特征多项式 258 个非零项，\(Q_{14}\) 159 项；
- \(z=1\) 除法余项严格为零；
- 一般 \(z\) 除法余项严格等于 \((z-1)R_4\)，且上述系数见证非零；
- Rabin 有限域不可约证书的两项 gcd 均为 1，\(L^{p^{14}}\) 余式等于 \(L\)；
- 全程使用精确整数/有理多项式与有限域运算，不使用浮点近似。

证书输出 `ALL_CHECKS_PASS`。完整多项式 \(Q_{14},Q_5,R_9,S_9^{gen},R_4\)、稀疏项、SHA-256 及有限域 Frobenius 余式保存在 `PREFIX574_EXACT_RESULTS.json`。

## 6. 结论边界与下一问题

本轮证明了完整门控 14 阶多项式在对称系数域上不可约；五态核心的谱因子身份仅在 \(z=1\) 的门控求和特化下成立；通用提升缺陷为 \((z-1)R_4\)。标准标量 companion 的坐标正交锥失败，但不否定其他正锥。

下一研究单元应从 37 状态非负实现诱导 14 维可观测循环模，求其与 37 维正正交锥的交锥及极射线；判定是否存在保持门控变量的 14 维正实现，或给出其最小正实现维数下界。必须保留 \(z\) 与 \(u,v\) 的独立观察，不得用 \(z=1\) 核心替代完整门控模型。

## 7. 权限与状态

GitHub 身份 `awdawmip` 对 `awdawmip/enterprise-math` 的权限实读为 `admin`。本轮 EM 原生控制网关未建立后端连接，不能确认 Source-native Researcher-ID、当前 native Owner 或 claim；本记录不建立 CLAIM、Review、Working Truth 或数学接纳。Researcher-ID 是当前对话复用的本地角色标识，活动记录中的 session key 也是本地分配键，不伪装成 Source-native session。

**Status:** `AUTHOR_PROVED / EXACT_SYMBOLIC_CHECKED / FINITE_FIELD_CERTIFIED / UNREVIEWED / NOT_ADMITTED`.
