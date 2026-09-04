# \(P_{46}\) 的着色分支稳定子：平凡 \(\mathrm{PGL}_2\) 对称与分裂边界

Status: `FREE_RESEARCH / DERIVED_EXACT_OBSTRUCTION / TRIVIAL_COLORED_BASE_STABILIZER / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research unit: `EM-FREE-F6D046-R16-P46-COLORED-BRANCH-STABILIZER`

## 1. 问题

mixed cyclic-quartic 曲线可写成

\[
C_{46}:\quad y^4=A(t)D(t)^2
\]

（非零四次幂常数不影响分支型），其中

\[
A=t^4+24t^3+192t^2+528t+144,
\qquad D=t^2+12t+24.
\]

四个 \(A\)-根具有分支指数 \(1\bmod4\)，两个 \(D\)-根具有分支指数 \(2\bmod4\)。若存在保持该指数着色的非平凡基底 Möbius 对称，它会给出额外曲线自同构并可能触发 Kani--Rosen 型分解。

## 2. 标准化

令

\[
u=t+6,\qquad s^2=12,\qquad x=\frac{u-s}{u+s}.
\]

两个 \(D\)-根 \(u=\pm s\) 被送到 \(x=0,\infty\)。任何保持无序点对 \(\{0,\infty\}\) 的 Möbius 变换只有两型：

\[
x\mapsto\lambda x,
\qquad
x\mapsto\frac{\lambda}{x}.
\]

把 \(A=u^4-24u^2-48u\) 拉回并清除分母：

\[
\widetilde A(x)=(1-x)^4A\!\left(s\frac{1+x}{1-x}\right)=\sum_{k=0}^4a_kx^k,
\]

其中

\[
\begin{aligned}
a_0&=-144-48s,&a_1&=576+96s,\\
a_2&=1440,&a_3&=576-96s,\\
a_4&=-144+48s.
\end{aligned}
\]

在 \(s^2=12\) 下五个系数均非零。

## 3. 缩放型

若

\[
\widetilde A(\lambda x)=\mu\widetilde A(x),
\]

常数项给出 \(\mu=1\)，一次项给出 \(\lambda=1\)。故缩放型只有恒等变换。

## 4. 反演型

若

\[
x^4\widetilde A(\lambda/x)=\mu\widetilde A(x),
\]

比较 \(x^2,x^3,x^4\) 系数可得必要条件

\[
\mu=\lambda^2=\frac{a_0}{a_4},
\qquad
\lambda=\mu\frac{a_3}{a_1},
\]

从而

\[
a_0a_3^2=a_1^2a_4.
\]

但精确计算

\[
a_0a_3^2-a_1^2a_4=(-48)\,96^2\,24s\ne0.
\]

所以反演型不存在。

## 5. 定理与边界

\[
\boxed{\operatorname{Stab}_{\mathrm{PGL}_2}(\operatorname{div}_{\mathrm{branch}}^{\mathrm{colored}})=1.}
\]

因此，任何正规化既有 \(C_4\) deck 群的曲线自同构，在基底上的像都是恒等；其 normalizer 不会从基底 Möbius 对称获得额外生成元。特别地，不能用一个隐藏的分支点置换直接解释 \(P_{46}\) 的进一步 product decomposition。

严格边界：

- 这只控制正规化 deck \(C_4\) 的自同构；
- 尚未证明 deck \(C_4\) 在完整自同构群中是特征子群；
- 即使完整曲线自同构群恰为 \(C_4\)，也仍可能存在不来自自同构的代数 correspondence；
- 因而该结果支持但不替代 \(P_{46}\) 的几何单纯性／endomorphism-algebra 判定。

分类维持：

`DERIVED_EXACT_OBSTRUCTION / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.