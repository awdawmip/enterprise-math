# Mixed Prym \(P_{46}\) 的算术审计：好约化、\(\mathbf Q\)-单纯性与几何边界

Status: `FREE_RESEARCH / DERIVED_ARITHMETIC_THEOREM / Q_SIMPLE / GEOMETRIC_SIMPLICITY_OPEN / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Parent candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN`

Research unit: `EM-FREE-F6D046-R14-P46-ARITHMETIC-AUDIT`

## 0. 结论

对 R11 留下的四维 mixed Prym，取

\[
E:\ v^2=A(t),\qquad C_{46}:\ m^2=-\frac1{288}vD(t),
\]

其中

\[
A=t^4+24t^3+192t^2+528t+144,
\qquad D=t^2+12t+24.
\]

本轮得到：

1. 该模型的判别式、交点和分母所涉及的坏素数仅为 \(2,3\)，故所用 \(p=5,7,11,13\) 均为好素数；
2. \(C_{46}\to E\) 在八个不同点分歧，故 \(g(C_{46})=5\)，\(\dim P_{46}=4\)；
3. 在 \(p=7\) 处，完整 degree-8 Frobenius 多项式
   \[
   P_7(T)=1+5T^2+245T^6+2401T^8
   \]
   在 \(\mathbf Q[T]\) 上不可约；附带检查器给出有限域 Rabin 不可约证书；
4. 因此 \(P_{46}\) 在 \(\mathbf Q\) 上单纯；
5. 这不等价于在 \(\overline{\mathbf Q}\) 上单纯。几何因子若被 Galois 传递置换，整体仍可能在 \(\mathbf Q\) 上单纯。因此绝对单纯性仍需一个绝对单纯好约化或独立的 endomorphism/correspondence 定理。

本轮没有重新开启公理门。

## 1. 好约化与 genus

精确算术为

\[
\operatorname{disc}(A)=-2^{16}3^5,
\]

\[
\operatorname{disc}(D)=2^4 3,
\]

\[
\operatorname{Res}(A,D)=-2^8 3^3.
\]

常数 \(288=2^5 3^2\)。所以除 \(2,3\) 外，四个 \(A\)-根、两个 \(D\)-根及相应 sheets 均保持分离。

在 \(E\) 上：

- 每个 \(A\)-根给出一个 \(v=0\) 点，函数 \(vD\) 在该点具有奇 valuation，共四点；
- 每个 \(D\)-根在 \(E\) 上有两个点，函数 \(vD\) 各有奇 valuation，共四点；
- 两个无穷远点的 pole order 为偶数，不分歧。

故分歧点数为 \(8\)。Riemann--Hurwitz 给出

\[
2g(C_{46})-2=2(2g(E)-2)+8=8,
\]

即

\[
\boxed{g(C_{46})=5,\qquad \dim\operatorname{Prym}(C_{46}/E)=4.}
\]

## 2. 完整局部多项式

由 \(n=1,2,3,4\) 的点数以及

\[
s_n(P_{46})=N_n(E)-N_n(C_{46})
\]

和 Newton 恒等式恢复：

\[
P_5(T)=1-30T^4+625T^8,
\]

\[
P_7(T)=1+5T^2+245T^6+2401T^8,
\]

\[
P_{11}(T)=1+4T^2+22T^4+484T^6+14641T^8,
\]

\[
\begin{aligned}
P_{13}(T)
={}&1+25T^2-40T^3+328T^4-520T^5\\
&+4225T^6+28561T^8\\
={}&(1+4T+13T^2)\\
&\cdot(1-4T+28T^2-100T^3+364T^4-676T^5+2197T^6).
\end{aligned}
\]

这些多项式全部满足 dimension-4 Weil functional equation。

## 3. \(\mathbf Q\)-单纯性定理

### 定理

\[
\boxed{P_{46}/\mathbf Q\text{ 是单纯阿贝尔四维簇。}}
\]

### 证明

检查器对 \(P_7\) 搜索一个不整除首项的辅助素数 \(\ell\)，将其首一化后验证 degree-8 Rabin 判据

\[
T^{\ell^8}\equiv T\pmod{P_7},
\]

\[
\gcd(P_7,T^{\ell^4}-T)=1.
\]

故 \(P_7\) 模 \(\ell\) 不可约，从而在 \(\mathbf Q[T]\) 上不可约。因此 \(p=7\) 约化在 \(\mathbf F_7\) 上单纯。

若 \(P_{46}/\mathbf Q\) 有非平凡 \(\mathbf Q\)-isogeny 分解 \(B\times C\)，则在共同好约化处，Tate module 和 Frobenius 特征多项式相应分解，迫使 \(P_7(T)\) 在 \(\mathbf Q[T]\) 上分解，矛盾。证毕。

## 4. Gaussian semilinear 解释

几何 deck 生成元 \(\iota:r\mapsto ir\) 在 \(\mathbf Q(i)\) 上定义。对 \(p\equiv3\pmod4\)，Frobenius 满足

\[
F\iota F^{-1}=\iota^p=\iota^{-1},
\]

所以交换 \(+i\) 与 \(-i\) eigenspaces，奇次 Frobenius traces 消失，局部多项式成为 \(G_p(T^2)\)。这解释了 \(p=7,11\) 的偶次幂形状，也解释了这些约化在平方扩域上可能出现等幂分裂。

对 \(p\equiv1\pmod4\)，Frobenius 保持两个 Gaussian eigenspaces，局部多项式在 \(\mathbf Q(i)[T]\) 上表现为一对共轭 degree-4 因子。\(p=13\) 的有理 degree \(2+6\) 分解是特殊约化现象，不能提升为特征零的有理分解，因为 \(p=7\) 已排除后者。

## 5. 不能越过的边界

\[
\mathbf Q\text{-simple}\not\Rightarrow\overline{\mathbf Q}\text{-simple}.
\]

若若干几何因子被 \(\operatorname{Gal}(\overline{\mathbf Q}/\mathbf Q)\) 传递置换，则特征零整体仍可能在 \(\mathbf Q\) 上单纯，惰性素数的 \(G_p(T^2)\) 形状也与此兼容。

下一严格判据为：

- 找到一个好素数，其约化经单位根比值排除后可认证为绝对单纯；或
- 构造一个非平凡几何 correspondence/endomorphism，证明实际分裂。

分类：

`DERIVED_ARITHMETIC_THEOREM / Q_SIMPLE / ABSOLUTE_SIMPLICITY_OPEN / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.

## 6. 工具复用审计

现有 holonomy、有限对称和喷流工具用于上游类型化；当前仓库未发现能直接输入该 genus-5 cyclic-quartic/Prym 模型并输出完整有限域 local polynomial 的现成执行接口。本轮检查器按 `RESULT_ONLY` 处理，不注册新全局工具族。