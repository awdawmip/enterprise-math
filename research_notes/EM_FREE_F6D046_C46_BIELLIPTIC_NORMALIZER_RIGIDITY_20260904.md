# \(C_{46}\) 的 bielliptic normalizer 刚性

Status: `FREE_RESEARCH / DERIVED_EXACT_NORMALIZER_THEOREM / FULL_AUT_CONDITIONAL_ON_GEOMETRIC_SIMPLICITY / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research unit: `EM-FREE-F6D046-R17-C46-BIELLIPTIC-NORMALIZER-RIGIDITY`

## 1. 椭圆商的标准模型

令

\[
u=t+6,\qquad x=-\frac{12}{u},\qquad y=\frac{6v}{u^2}.
\]

由 \(A(t)=u^4-24u^2-48u\) 得到

\[
E:\quad y^2=x^3-6x^2+36.
\]

其不变量为

\[
c_4=576,\qquad \Delta=-62208=-2^8 3^5,
\qquad j(E)=-3072.
\]

所以在特征零代数闭包上

\[
\operatorname{Aut}(E,O)=\{\pm1\}.
\]

记 \(B\subset E\) 为二次覆盖 \(C_{46}\to E\) 的八点分支集。四个 \(A\)-分支点正好是 \(E[2]\)，其余四点记为 \(S_D\)，于是

\[
B=E[2]\sqcup S_D,\qquad [-1](B)=B.
\]

## 2. 八点分支集没有非零平移稳定子

任意椭圆曲线自同构写成

\[
P\longmapsto \varepsilon P+Q,\qquad \varepsilon\in\{\pm1\}.
\]

因为 \([-1]\) 保持 \(B\)，只需判断平移 \(T_Q\) 何时保持 \(B\)。若 \(T_Q(B)=B\)，由 \(O\in B\) 得 \(Q\in B\)。

### 情形一：\(Q\in E[2]\)

若 \(Q\ne O\)，则 \(T_Q\) 与 \([-1]\) 对易，因而下降为 \(E/\{\pm1\}\simeq\mathbf P^1\) 上的非恒等 Möbius 变换；它同时保持 \(E[2]\) 的像和 \(S_D\) 的像，即保持指数着色的 \(A/D\) 分支除子。这与 R16 的平凡着色稳定子定理矛盾。

### 情形二：\(Q\in S_D\)

此时 \(Q\notin E[2]\)，故 coset \(Q+E[2]\) 与 \(E[2]\) 不交。又因 \(Q+E[2]\subset B\) 且有四点，只能有

\[
Q+E[2]=S_D.
\]

于是每个非零 \(T\in E[2]\) 都保持 \(S_D\)，从而再次给出非恒等的着色基底 Möbius 稳定子，仍与 R16 矛盾。

所以

\[
\boxed{\operatorname{Stab}_{E(\bar{\mathbf Q})}(B)=\{O\}},
\]

并且

\[
\boxed{\operatorname{Aut}(E,B)=\langle[-1]\rangle\simeq C_2}.
\]

## 3. bielliptic involution 的 normalizer

设 \(\sigma\) 是四次覆盖的 deck 生成元，\(\sigma(y)=iy\)，并令

\[
z=\sigma^2.
\]

则 \(C_{46}/\langle z\rangle=E\)，且该二次商的分支集就是 \(B\)。任何正规化 \(\langle z\rangle\) 的曲线自同构都下降为 \(\operatorname{Aut}(E,B)\)；下降映射的核为 \(\langle z\rangle\)。另一方面，\(\sigma\) 下降为 \([-1]\)。因此

\[
1\longrightarrow\langle z\rangle
\longrightarrow N_{\operatorname{Aut}(C_{46})}(\langle z\rangle)
\longrightarrow\langle[-1]\rangle
\longrightarrow1
\]

已由 \(\langle\sigma\rangle\) 实现，故

\[
\boxed{
N_{\operatorname{Aut}(C_{46})}(\langle\sigma^2\rangle)
=
\langle\sigma\rangle\simeq C_4.
}
\]

由于 \(\langle z\rangle\) 是二阶群，normalizer 也是 centralizer：

\[
C_{\operatorname{Aut}(C_{46})}(z)=C_4.
\]

因此任意额外自同构 \(\phi\notin C_4\) 必须把 \(z\) 共轭为一个不同的 bielliptic involution，亦即强制出现第二个 degree-2 elliptic quotient。它不能隐藏在现有 \(C_4\)-塔的 normalizer 内。

## 4. 几何单纯性给出的条件推论

已有 Prym 分解

\[
J(C_{46})\sim E\times P_{46}.
\]

若 \(P_{46}/\bar{\mathbf Q}\) 几何单纯，则它不含椭圆子簇，且

\[
\operatorname{Hom}(E,P_{46})=
\operatorname{Hom}(P_{46},E)=0.
\]

若存在第二个 bielliptic involution \(\tau\)，其椭圆商的 pullback 必须落在唯一的椭圆 isotypic 因子 \(E\) 中。因此 \(\tau\) 与 \(z\) 在 \(H^1(C_{46})\) 上具有相同的 \(+1\) 子空间，也具有相同的 \(-1\) Prym 子空间，故二者在 \(H^1\) 上作用相同。属数至少二时曲线自同构在一阶上同调上的表示忠实，于是 \(\tau=z\)。

所以

\[
P_{46}\text{ geometrically simple}
\quad\Longrightarrow\quad
\boxed{\operatorname{Aut}(C_{46})=C_4}.
\]

本文件无条件证明 normalizer 刚性；full automorphism-group 结论仅在独立的几何单纯性证书成立时提升。

分类：

`DERIVED_EXACT_NORMALIZER_THEOREM / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.