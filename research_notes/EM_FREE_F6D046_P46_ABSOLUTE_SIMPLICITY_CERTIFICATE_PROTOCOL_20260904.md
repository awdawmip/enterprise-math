# \(P_{46}\) 绝对单纯性的有限 Frobenius 证书协议

Status: `FREE_RESEARCH / EXACT_FINITE_CERTIFICATE_PROTOCOL / THEOREM_ONLY_IF_VALIDATOR_PASSES / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research unit: `EM-FREE-F6D046-R15-P46-ABSOLUTE-SIMPLICITY-CERTIFICATE`

## 1. 目标

设 \(A/\mathbf F_p\) 是 \(P_{46}\) 的一个好约化，且完整 Frobenius 多项式

\[
f_p(X)=\prod_{i=1}^{8}(X-\alpha_i)
\]

在 \(\mathbf Q[X]\) 上不可约。要把有限域单纯性提升为绝对单纯性，必须排除任意不同共轭根之比 \(\alpha_i/\alpha_j\) 为单位根。

本文件只规定可复核的有限证书；只有相应 validator 全部通过时，才允许写出 `P46_GEOMETRICALLY_SIMPLE`。

## 2. 为什么检查是有限的

若

\[
\frac{\alpha_i}{\alpha_j}=\zeta_m,
\]

则 \(\mathbf Q(\zeta_m)\subseteq\mathbf Q(\alpha_i,\alpha_j)\)。由于每个 \(\alpha_i\) 的次数至多为 \(8\)，有

\[
\varphi(m)\le [\mathbf Q(\alpha_i,\alpha_j):\mathbf Q]\le64.
\]

使用初等下界

\[
\varphi(m)\ge\sqrt{m/2},
\]

得到

\[
m\le8192.
\]

所以只需枚举有限集合

\[
\mathcal M=\{2\le m\le8192:\ \varphi(m)\le64\}.
\]

## 3. 每个 \(m\) 的精确排除

令

\[
f_{p,m}(Y)=\prod_{i=1}^{8}(Y-\alpha_i^m).
\]

其系数可由 \(f_p\) 的 Newton power sums 精确恢复。

若存在辅助素数 \(\ell\ne p\)，使 \(f_{p,m}(Y)\bmod\ell\) 为 squarefree degree \(8\)，则其判别式在 \(\mathbf Z\) 中非零；因此所有 \(\alpha_i^m\) 两两不同，特别地不存在 \(\alpha_i/\alpha_j\) 为阶整除 \(m\) 的单位根。

对每个 \(m\in\mathcal M\) 给出一个这样的 \(\ell\)，便得到有限、逐项可重算的无单位根比值证书。

## 4. 绝对单纯性推论

若 \(f_p\) 不可约，则约化在 \(\mathbf F_p\) 上单纯。若它在某个有限扩域 \(\mathbf F_{p^n}\) 上不再单纯，则 \(\pi^n\) 的共轭数目下降，故存在 \(i\ne j\) 使

\[
\alpha_i^n=\alpha_j^n,
\]

即 \(\alpha_i/\alpha_j\) 为单位根。上述证书排除了这种情形，所以该约化在所有有限扩域上单纯，亦即在 \(\overline{\mathbf F}_p\) 上绝对单纯。

好约化时，特征零几何 endomorphism 的 specialization 是单射。若 \(P_{46}/\overline{\mathbf Q}\) 有非平凡 isogeny 分解，则其非平凡有理幂等元会 specialization 到约化，迫使后者分裂，矛盾。因此：

\[
\boxed{
\text{一个通过本协议的好约化证书}
\Longrightarrow
P_{46}/\overline{\mathbf Q}\text{ 几何单纯}.
}
\]

## 5. 防误报边界

以下任何一项都不足：

- 只验证 \(f_p\) 在 \(\mathbf Q\) 上不可约；
- 只检查 \(f_p\) 不是 \(G(X^d)\)；
- 只用浮点根近似判断比值不接近单位根；
- 只检查少数几个单位根阶；
- 只在一个辅助素数下观察到一般因子型。

validator 必须重新验证：好素数、degree 8、有限域 Rabin 不可约证书、\(\mathcal M\) 的完整覆盖，以及每个 \(m\) 的 modular squarefreeness witness。

分类：

`EXACT_FINITE_CERTIFICATE_PROTOCOL / DERIVED_IF_PASSED / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.