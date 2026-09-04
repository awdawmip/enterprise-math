# \(P_{46}\) 的端同态定义域、完整代数单值群与 Sato–Tate 群

Status: `FREE_RESEARCH / DERIVED DESCENT-AND-COMPONENT THEOREM / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units:

- `EM-FREE-F6D046-R28-P46-ENDOMORPHISM-FIELD-QI`
- `EM-FREE-F6D046-R29-P46-FULL-MONODROMY-NORMALIZER`
- `EM-FREE-F6D046-R30-P46-FULL-SATO-TATE-U4-C2`

## 1. 输入

沿用已经独立闭合的结果：

\[
P_{46}=\operatorname{Prym}(C_{46}/E),\qquad \dim P_{46}=4,
\]

\[
\operatorname{End}_{\overline{\mathbf Q}}(P_{46})=\mathbf Z[i],
\qquad
\operatorname{End}^0_{\overline{\mathbf Q}}(P_{46})=K:=\mathbf Q(i),
\]

\[
\operatorname{MT}(P_{46})=\operatorname{GU}_K(V,h),
\qquad
\operatorname{Hg}(P_{46})=\operatorname{U}_K(V,h),
\]

其中 \(h\) 的实 signature 为 \((3,1)\)，且对每个 \(\ell\)，

\[
G_\ell^\circ=
\operatorname{GU}_K(V,h)_{\mathbf Q_\ell}.
\]

曲线可写成

\[
C_{46}:\quad
v^2=A(t),\qquad
m^2=-\frac1{288}vD(t),
\]

其中

\[
A(t)=t^4+24t^3+192t^2+528t+144,
\qquad
D(t)=t^2+12t+24.
\]

在 \(\mathbf Q(i)\) 上有 order-\(4\) deck automorphism

\[
\boxed{
\sigma(t,v,m)=(t,-v,im).
}
\]

它满足

\[
\sigma^2(t,v,m)=(t,v,-m),
\qquad
\sigma^4=1.
\]

其在 Prym 上的作用记为 \(I\)，于是 \(I^2=-1\)，并生成已经证明的 \(\mathbf Z[i]\)-端同态环。

## 2. 端同态定义域恰为 \(\mathbf Q(i)\)

令 \(c\in\operatorname{Gal}(\overline{\mathbf Q}/\mathbf Q)\) 为复共轭。对 \(\sigma\) 的系数作共轭得到

\[
{}^c\!\sigma(t,v,m)
=(t,-v,-im)
=
\sigma^{-1}(t,v,m).
\]

故在 Prym 端同态环上

\[
cIc^{-1}=-I.
\]

因此 \(I\) 不在 \(\mathbf Q\) 上定义，而在 \(\mathbf Q(i)\) 上定义。又因

\[
\operatorname{End}_{\overline{\mathbf Q}}(P_{46})
=
\mathbf Z[I],
\]

所有几何端同态均已在 \(\mathbf Q(i)\) 上定义，不可能需要更大的域。于是最小端同态定义域为

\[
\boxed{
K_e(P_{46})=\mathbf Q(i).
}
\]

相应的 Galois 作用

\[
\operatorname{Gal}(K_e/\mathbf Q)
\longrightarrow
\operatorname{Aut}_{\mathbf Q\text{-alg}}(K)
\]

把复共轭送到 \(i\mapsto-i\)，且这是同构 \(C_2\simeq C_2\)。

## 3. 完整 \(\ell\)-adic 代数单值群

令

\[
G_\ell=
\overline{\rho_\ell(G_{\mathbf Q})}^{\mathrm{Zar}}
\subseteq
\operatorname{GSp}(V_\ell).
\]

Galois 对几何端同态的共轭作用给出

\[
\rho_\ell(\gamma)I\rho_\ell(\gamma)^{-1}
=
\gamma(I),
\]

所以 \(G_\ell\) 位于 \(K_\ell:=K\otimes\mathbf Q_\ell\) 的 normalizer 中：

\[
G_\ell
\subseteq
N_\ell:=N_{\operatorname{GSp}(V_\ell)}(K_\ell).
\]

normalizer 对 \(K_\ell\) 的共轭作用给出正合列

\[
1\longrightarrow
L_\ell
\longrightarrow
N_\ell
\longrightarrow
\operatorname{Aut}_{\mathbf Q_\ell\text{-alg}}(K_\ell)
\longrightarrow1,
\]

其中

\[
L_\ell=
\operatorname{Cent}_{\operatorname{GSp}(V_\ell)}(K_\ell)
=
\operatorname{GU}_K(V,h)_{\mathbf Q_\ell}.
\]

无论 \(K_\ell\) 是二次域、分裂代数还是在 \(2\) 处分歧，右端自同构群均为 \(C_2\)。

R26B 已用 \(p=17,29\) 的双素数最大 Frobenius 环面直接证明

\[
G_\ell^\circ=L_\ell
\quad\text{对所有 }\ell.
\]

另一方面，复共轭的像对 \(I\) 作 \(I\mapsto-I\)，所以 \(G_\ell\) 确实命中 normalizer 的非平凡分量。既然 \(N_\ell/L_\ell\) 只有两个元素，立即得到

\[
\boxed{
G_\ell=N_\ell
=N_{\operatorname{GSp}(V_\ell)}(K_\ell)
\quad\text{对所有 }\ell.
}
\]

特别地，

\[
\boxed{
\pi_0(G_\ell)\simeq C_2
\simeq\operatorname{Gal}(\mathbf Q(i)/\mathbf Q).
}
\]

这把上一阶段只确定的连通单值群提升为完整代数单值群。

## 4. twisted Lefschetz / algebraic Sato–Tate 群

在 symplectic 层定义 twisted Lefschetz group

\[
\operatorname{DL}_{\mathbf Q}(P_{46})
=
\coprod_{\tau\in\operatorname{Gal}(K_e/\mathbf Q)}
\left\{
 g\in\operatorname{Sp}(V):
 g\alpha g^{-1}=\tau(\alpha)
 \quad\forall\alpha\in K
\right\}.
\]

因为 \(K_e=K=\mathbf Q(i)\)，这是 \(K\)-作用在 \(\operatorname{Sp}(V)\) 中的完整 normalizer：

\[
\operatorname{DL}_{\mathbf Q}(P_{46})
=N_{\operatorname{Sp}(V)}(K).
\]

其恒等分量是

\[
\operatorname{DL}_{\mathbf Q}(P_{46})^\circ
=
\operatorname{Hg}(P_{46})
=
\operatorname{U}_K(V,h).
\]

本对象已经证明为 fully of Lefschetz type，且 Mumford–Tate 猜想成立。由 Cantoral Farfán–Commelin 的 Mumford–Tate \(\Rightarrow\) algebraic Sato–Tate 定理，存在 \(\mathbf Q\)-群 \(\operatorname{AST}_{\mathbf Q}(P_{46})\)，其各 \(\mathbf Q_\ell\)-基变换等于 symplectic \(\ell\)-adic 单值群。上一节已把这些群逐个识别为 normalizer，故忠实平坦基变换后可检验的闭子群等式给出

\[
\boxed{
\operatorname{AST}_{\mathbf Q}(P_{46})
=
\operatorname{DL}_{\mathbf Q}(P_{46})
=
N_{\operatorname{Sp}(V)}(K).
}
\]

从而

\[
\boxed{
\pi_0(\operatorname{AST}_{\mathbf Q}(P_{46}))
\simeq C_2.
}
\]

这也与 fully Lefschetz type 的 component theorem 一致：恒等 twisted-Lefschetz 部分连通，而最小端同态定义域的 Galois 群为 \(C_2\)。

## 5. 正确的 Sato–Tate 连通分量

必须再次区分：

\[
\operatorname{Hg}(P_{46})(\mathbf R)=U(3,1)
\]

的实最大紧子群 \(U(3)\times U(1)\)，描述的是 Hermitian 对称域；Sato–Tate 群则取

\[
\operatorname{Hg}(P_{46})(\mathbf C)
\simeq GL_4(\mathbf C)
\]

的紧实形式。因此

\[
\boxed{
\operatorname{ST}(P_{46})^\circ\simeq U(4).
}
\]

这是对前一阶段临时写成 \(U(3)\times U(1)\) 的明确纠正。signature \((3,1)\) 仍然控制 PEL/Hodge 域，但不会改变复代数群 \(GL_4\) 的紧形式。

## 6. 完整紧群的显式 normalizer 模型

在复化标准表示中写

\[
V_{\mathbf C}=W\oplus W^\vee,
\qquad \dim W=4.
\]

将 \(U(4)\) 嵌入 \(USp(8)\)：

\[
\iota(A)=
\begin{pmatrix}
A&0\\0&\bar A
\end{pmatrix}.
\]

取

\[
J=
\begin{pmatrix}
0&I_4\\-I_4&0
\end{pmatrix}.
\]

则

\[
J^2=-I_8,
\qquad
J\iota(A)J^{-1}=\iota(\bar A).
\]

所以

\[
\boxed{
N_{USp(8)}(U(4))
=
\iota(U(4))\sqcup\iota(U(4))J.
}
\]

由于 \(4\) 为偶数，该扩张可分裂。令

\[
B=
\begin{pmatrix}
0&I_2\\-I_2&0
\end{pmatrix}
\in U(4),
\qquad B^2=-I_4,
\]

并设

\[
S=\iota(B)J.
\]

则

\[
S^2=I_8,
\]

且

\[
S\iota(A)S^{-1}
=
\iota\!\left(B\bar A B^{-1}\right).
\]

因此，至多差 \(USp(8)\) 内共轭，完整 Sato–Tate 群为显式半直积

\[
\boxed{
\operatorname{ST}_{\mathbf Q}(P_{46})
\simeq
U(4)\rtimes_{\alpha}C_2,
\qquad
\alpha(A)=B\bar A B^{-1}.
}
\]

其外自同构类就是复共轭；不同的 \(B\) 选择只改变内自同构共轭，不改变群的共轭类。特别地，

\[
\boxed{
\pi_0(\operatorname{ST}_{\mathbf Q}(P_{46}))\simeq C_2.
}
\]

## 7. 精确边界

本结果确定的是 algebraic/compact Sato–Tate 群本身及其分量。它不自动证明按 Haar 测度的解析 equidistribution；广义 Sato–Tate 等分布仍需要相应 automorphy 或 \(L\)-函数解析性质。

必须区分：

\[
\operatorname{Hg}(\mathbf R)=U(3,1),
\]

\[
\operatorname{ST}^\circ=U(4),
\]

\[
\operatorname{ST}=U(4)\rtimes C_2.
\]

前者是非紧实 Hodge 实形式，后两者是复代数群的紧实形式及其 arithmetic component extension。

## 8. 方法复用、公理门与分类

复用状态：

- R17/R18 的显式 deck automorphism：`REUSE_APPLIED`；
- R23 的 \(\operatorname{End}=\mathbf Z[i]\)：`REUSE_APPLIED`；
- R26B 的完整连通单值群与 Mumford–Tate 等式：`REUSE_APPLIED`；
- Mumford–Tate \(\Rightarrow\) algebraic Sato–Tate：`REUSE_APPLIED_EXTERNAL_THEOREM`；
- twisted Lefschetz component formalism：`REUSE_APPLIED_EXTERNAL_THEOREM`；
- compact normalizer block model：专用显式证书，不建立新全局工具族。

分类：

\[
\texttt{DERIVED\_ENDOMORPHISM\_FIELD\_THEOREM},
\]

\[
\texttt{FULL\_MONODROMY\_NORMALIZER},
\]

\[
\texttt{SATO\_TATE\_U4\_SEMIDIRECT\_C2},
\]

以及

\[
\texttt{NOT\_NEW\_AXIOM / NOT\_FOUNDATION / P000\_UNCHANGED}.
\]

## 9. 参考基础

- V. Cantoral Farfán and J. Commelin, *The Mumford–Tate conjecture implies the algebraic Sato–Tate conjecture of Banaszak and Kedlaya*.
- G. Banaszak and K. Kedlaya, *An algebraic Sato–Tate group and Sato–Tate conjecture*, Indiana Univ. Math. J. 64 (2015).
- G. Banaszak and V. Cantoral Farfán, *A remark on the component group of the Sato–Tate group*, Research in Number Theory 11 (2025), together with its 2025 correction.
- R. Guralnick and K. Kedlaya, *Endomorphism fields of abelian varieties*, Research in Number Theory 3 (2017).
