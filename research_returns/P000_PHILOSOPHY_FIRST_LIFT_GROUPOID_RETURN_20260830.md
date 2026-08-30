# P000 哲学先行 Q3：`S4` Lift 群胚与选择问题重构 — Research Return

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

Researcher-ID: `EM-P000Q3-A7C531`  
Task-ID: `RS-P000-PHILOSOPHY-FIRST-LIFT-GROUPOID`  
Publication-ID: `TP2-416543D426C413DE3C3B`  
Claim-ID: `chatgpt-p000q3-20260830-1132-a7c531`  
Execution branch: `research/p000-philosophy-lift-groupoid-em-p000q3-a7c531`  
Execution base: `c8fd304565c858ae43b482bceaf5b47436624acf`

Hard target:

`P000_S4_LIFT_GROUPOID_AND_FIBER_REGIMES_EXACTLY_CLASSIFIED`

Primary terminal class:

`LIFT_GROUPOID_FINITE_CLASSIFICATION`

Secondary exact boundary:

`GEN13_SECTION_OBJECT_LAYER_RECOVERED / MORPHISM_LAYER_REQUIRES_ACTUAL_GAUGE_SEMANTICS`

## 1. Executive result

本任务把“选一个 `S4` lift”改成“研究全部 admissible lift 以及真实允许的等价”，得到一个有限 action groupoid：

\[
\boxed{
\mathbf{Lift}_{S_4}(M)
=
\Gamma_M\ltimes \operatorname{Sec}_{\mathrm{adm}}(q_M)
}
\]

其中：

- \(\widetilde G_M\) 是模型中**实际允许的 enriched automorphisms** 所生成的有限群；
- \(q_M:\widetilde G_M\to S_4\) 是冻结 carrier-axis readout；
- \(K_M=\ker q_M\) 保留，不做 quotient；
- \(\operatorname{Sec}_{\mathrm{adm}}(q_M)\) 是满足
  \(q_M\circ s=id_{S_4}\) 的 admissible **homomorphic sections**；
- \(\Gamma_M\) 不是任意形式 `Aut(\widetilde G_M)`，而是模型真实 primitive-preserving / relation-preserving / gauge self-equivalences 在 lift datum 上的**有效诱导像**；
- 箭头 \(s\to t\) 正是那些 \(\gamma\in\Gamma_M\) 使 \(\gamma_*\circ s=t\)。

这个定义有三个直接后果。

第一，Gen13 的 extension/section 语言正好给出对象层：

\[
\operatorname{Obj}\mathbf{Lift}_{S_4}(M)
=
\operatorname{Sec}_{\mathrm{adm}}(q_M).
\]

第二，群胚额外冻结了两个 Gen13 仅靠 `q/K/residue/section set` 不能恢复的量：

\[
\pi_0\mathbf{Lift}_{S_4}(M)
\]

即 gauge-equivalence classes，以及

\[
\operatorname{Aut}_{\mathbf{Lift}}(s)
\]

即某个 section 的 stabilizer / hidden symmetry。

第三，`q`、`K`、relation residues，甚至**完整 section 集合本身**仍不足以决定群胚。本文构造两个具有同一个 split extension `C2 × S4 -> S4`、同样两个 sections 的模型，但因实际 primitive-preserving gauge language 不同，一个群胚有 `pi0=1`，另一个有 `pi0=2`。因此：

\[
\boxed{
\text{ordinary extension data alone does not determine lift canonicality}
}
\]

必须把“允许什么 morphism”也作为模型结构的一部分。

本任务还得到一个尖锐的逻辑纠偏：

> “所有 lift 都同构”与“存在唯一同构类”不是四级强度中的两个独立非空层次。

若“所有 lift 都同构”按纯全称命题理解，则空群胚中它**真空为真**；若再要求至少存在一个 lift，则它与“唯一同构类”完全等价：

\[
|\pi_0\mathbf{Lift}|=1
\iff
\bigl(\operatorname{Obj}\mathbf{Lift}\neq\varnothing
\ \wedge\
\forall s,t,\ s\simeq t\bigr).
\]

真正额外的结构来自：

1. 实际 object 数是否为 1；
2. stabilizer 是否平凡；
3. 是否存在被全部 gauge 固定的 distinguished section。

## 2. Scope and P000 guards

本结果严格 downstream 于 P000 与已接受 Gen12 witness。

继续冻结：

- P000 reality = `6D discrete Cell space + 1D time`；
- 当前 carrier `S4` 只是冻结的 downstream readout，不是 bare-P000 完整 native rotation group；
- carrier vertex tag 不等于 native Cell identity；
- Gen12 的四 opaque Cells / K4 adjacency 是 existential declared model，不是 P000 root axiom；
- hidden relation phase 是本文声明模型中的 relational state，不是无语义标签，也不是 P000 必然结构；
- `K=ker q` 和 relation residue 全程保留；
- 不通过 quotient kernel 把 nonsplit model 强行改造成 exact `S4`；
- time 不进入 spatial `S4` action。

使用 group extensions、sections、torsors、action groupoids、stabilizers 属 classical machinery。本任务不提出 classical novelty claim。

## 3. Exact definition of the lift groupoid

### 3.1 Finite lift datum

对一个允许的有限 framed Full-Cell model \(M\)，冻结 lift datum

\[
\mathcal D(M)
=
(\widetilde G_M,q_M,\mathcal R_M,\Gamma_M).
\]

这里：

1. \(\widetilde G_M\) 是从 \(M\) 的实际 enriched automorphisms 中取得的有限群；
2. \(q_M:\widetilde G_M\to S_4\) 是 frozen carrier-axis readout homomorphism；
3. \(\mathcal R_M\) 表示必须被保留的 Cell / PF-10 / connection / hidden relational state 与 relation residue；
4. \(\Gamma_M\) 是实际 primitive-preserving self-equivalences 对 \(\mathcal D(M)\) 的**有效诱导作用**。

“有效诱导”意味着：若两个 presentation gauge changes 在整个 lift datum 上诱导完全相同的变换，则它们不制造两个虚假的平行箭头。这样避免把纯坐标重命名错误计成 hidden automorphism。

每个 \(\gamma\in\Gamma_M\) 诱导

\[
\gamma_*:\widetilde G_M\to\widetilde G_M
\]

满足

\[
q_M\circ\gamma_*=q_M
\]

并保留声明的 primitive/relation data。

### 3.2 Objects

定义

\[
\operatorname{Sec}_{\mathrm{adm}}(M)
=
\left\{
s:S_4\to\widetilde G_M:
s\text{ is a group homomorphism},
\ q_M\circ s=id,
\ s\text{ preserves all declared model primitives}
\right\}.
\]

这严格对应 Gen13 的 homomorphic section，而不是 set-theoretic section。

定义

\[
\operatorname{Obj}\mathbf{Lift}_{S_4}(M)
=
\operatorname{Sec}_{\mathrm{adm}}(M).
\]

### 3.3 Morphisms

对两个 objects \(s,t\)，定义

\[
\operatorname{Hom}(s,t)
=
\left\{
\gamma\in\Gamma_M:
\gamma_*\circ s=t
\right\}.
\]

composition 由 \(\Gamma_M\) 的 composition 给出，inverse 由 \(\gamma^{-1}\) 给出，所以这是有限 groupoid。

等价地：

\[
\mathbf{Lift}_{S_4}(M)
=
\Gamma_M\ltimes\operatorname{Sec}_{\mathrm{adm}}(M).
\]

这不是凭空添加形式同构：每个箭头都必须来自模型已声明的 actual primitive-preserving equivalence。

## 4. Model-isomorphism invariance theorem

### Theorem 4.1 — transport invariance

设

\[
F:M\overset{\sim}{\longrightarrow}N
\]

是允许的 model isomorphism，并诱导

\[
F_*:\widetilde G_M\overset{\sim}{\longrightarrow}\widetilde G_N
\]

满足

\[
q_N\circ F_*=q_M,
\]

同时把 \(M\) 的 primitive/relation data 和有效 gauge group 搬运到 \(N\)。

则存在自然 groupoid isomorphism

\[
F_#:
\mathbf{Lift}_{S_4}(M)
\overset{\sim}{\longrightarrow}
\mathbf{Lift}_{S_4}(N).
\]

在 objects 上：

\[
F_#(s)=F_*\circ s.
\]

在 arrows 上：

\[
F_#(\gamma)=F\gamma F^{-1}
\]

的有效诱导像。

### Proof

若 \(s\) 是 section，则

\[
q_NF_*s=q_Ms=id,
\]

故 \(F_*s\) 仍为 section。primitive preservation 随 \(F\) 搬运。

若 \(\gamma:s\to t\)，则

\[
\gamma_*s=t.
\]

共轭后：

\[
(F\gamma F^{-1})_*(F_*s)
=
F_*(\gamma_*s)
=
F_*t.
\]

所以 arrows 被正确搬运。\(F^{-1}\) 给出逆 functor，故为 groupoid isomorphism。QED.

checker 另对 `V4` affine model 做了 finite relabeling conjugacy regression，objects / `pi0` / isotropy fingerprint 完全不变。

## 5. Gen12 = rigid trivial-kernel fiber

Gen12 已接受：

\[
|\widetilde G|=24,\qquad
|Image_{axis}|=24,\qquad
K=\ker q=1.
\]

因此 \(q:\widetilde G\to S_4\) 是 isomorphism。

于是 section 只能是

\[
s=q^{-1}.
\]

所以：

\[
|\operatorname{Obj}\mathbf{Lift}_{S_4}(M_{12})|=1.
\]

又因为有效 morphism 必须在 lift datum 上满足

\[
q\gamma_*=q,
\]

而 \(q\) injective，所以

\[
\gamma_*=id.
\]

在有效 morphism convention 下，Gen12 fiber 为：

\[
\boxed{
|\operatorname{Obj}|=1,\quad
|\pi_0|=1,\quad
|\operatorname{Aut}(s)|=1
}
\]

即 `rigid / trivial-kernel / strict unique object` regression。

这不否认 Gen12 的 presentation-gauge regression；纯 presentation changes 若对 lift datum 的诱导作用相同，不被重复计为 hidden symmetry。

## 6. Split `C2` relation-phase model: multiple sections, one free orbit

从 Gen12 downstream carrier action 出发，给 enriched relational layer 加入一个实际 `C2` relation-phase symmetry：

\[
\widetilde G_2^+
=
C_2\times S_4,
\]

\[
q(k,g)=g.
\]

kernel：

\[
K=C_2.
\]

这是 split extension。

任意 section 必须写成

\[
s_\chi(g)
=
(\chi(g),g)
\]

其中

\[
\chi:S_4\to C_2
\]

为 homomorphism。

因为

\[
S_4^{ab}\cong C_2,
\]

所以：

\[
\operatorname{Hom}(S_4,C_2)
=
\{0,\operatorname{sgn}\}.
\]

因此恰有两个 sections：

\[
s_0,\quad s_{\mathrm{sgn}}.
\]

现在允许 relation-phase trivialization 的实际 gauge changes：

\[
u_\psi(k,g)
=
(k+\psi(g),g),
\qquad
\psi\in\operatorname{Hom}(S_4,C_2).
\]

它们是 over-\(S_4\) group automorphisms，并作用为

\[
u_\psi\cdot s_\chi
=
s_{\chi+\psi}.
\]

因此 action 在两个 sections 上 simply transitive。

exact fingerprint：

\[
\boxed{
|\operatorname{Obj}|=2,\quad
|\pi_0|=1,\quad
|\operatorname{Aut}(s)|=1
}
\]

这给出了 required multi-object fiber。

它区分：

- “只有一个实际 section”；
- “有多个 section，但全部由唯一 gauge arrow 相互连接”。

该群胚 categorical-equivalent 于 terminal groupoid，但**没有一个由模型本身固定的 distinguished section**：非平凡 gauge 会交换两个 objects。

所以：

`UNIQUE_UP_TO_UNIQUE_ISOMORPHISM != CANONICALLY_CHOSEN_SECTION`.

## 7. Same extension, different primitive-preserving arrows

保留完全相同的：

\[
\widetilde G=C_2\times S_4,
\quad
q,
\quad
K=C_2,
\quad
\{s_0,s_{\mathrm{sgn}}\}.
\]

但在第二个 declared model 中，把 relation-phase origin/trivialization 作为必须保留的实际 primitive relational datum。

此时非平凡 \(u_{\mathrm{sgn}}\) 不再 primitive-preserving，故有效 gauge group 只剩 identity。

于是：

\[
\boxed{
|\operatorname{Obj}|=2,\quad
|\pi_0|=2,\quad
|\operatorname{Aut}(s)|=1
}
\]

与上一节相比：

- extension 相同；
- kernel 相同；
- relation-word identities 相同；
- section set 相同；
- 只有**允许的 actual morphism language** 不同；
- `pi0` 从 1 变成 2。

因此得到 exact non-reconstruction theorem：

### Theorem 7.1

数据

\[
(q,K,\text{relation residues},\operatorname{Sec}(q))
\]

不足以恢复

\[
\mathbf{Lift}_{S_4}(M).
\]

必须额外知道 actual primitive-preserving equivalence action \(\Gamma_M\)。

这是 Q3 相对“普通 section 集合”真正增加的信息。

## 8. Unique section with nontrivial automorphism

取

\[
\widetilde G_3^+
=
C_3\times S_4.
\]

因为任何 homomorphism \(S_4\to C_3\) 都经由

\[
S_4^{ab}\cong C_2
\]

因子化，而

\[
\operatorname{Hom}(C_2,C_3)=0,
\]

所以只有一个 section：

\[
s_0(g)=(0,g).
\]

但 relation phase inversion

\[
u(k,g)=(-k,g)
\]

是非平凡 over-\(S_4\) automorphism，并固定 \(s_0\)。

故：

\[
\boxed{
|\operatorname{Obj}|=1,\quad
|\pi_0|=1,\quad
|\operatorname{Aut}(s_0)|=2
}
\]

因此：

`UNIQUE_OBJECT != AUTOMORPHISM_FREE_UNIQUE_OBJECT`.

这构成 required nontrivial automorphism fiber。

## 9. Connected multi-object fiber with nontrivial isotropy

再取

\[
K=V_4=C_2^2,
\qquad
\widetilde G_V^+=V_4\times S_4.
\]

sections 对应

\[
\operatorname{Hom}(S_4,V_4)
\cong
\operatorname{Hom}(C_2,V_4)
\cong V_4,
\]

故有 4 个 objects。

允许完整 affine relation-phase gauge：

\[
u_{\beta,w}(k,g)
=
(\beta(k)+\epsilon(g)w,g),
\]

其中

\[
\beta\in GL(2,2),\quad
w\in V_4,\quad
\epsilon(g)=\operatorname{sgn}(g)\in C_2.
\]

于是 gauge group 为

\[
V_4\rtimes GL(2,2)
\]

阶数

\[
4\cdot 6=24.
\]

它在 4 个 sections 上 transitive，每个 stabilizer 为

\[
GL(2,2)\cong S_3
\]

阶数 6。

所以：

\[
\boxed{
|\operatorname{Obj}|=4,\quad
|\pi_0|=1,\quad
|\operatorname{Aut}(s)|=6
}
\]

这把“多个 choices”和“hidden isotropy”同时显式化。

## 10. Empty fiber with one-relation obstruction

构造 parity pullback：

\[
\widetilde G_2^-
=
\left\{
(z,g)\in C_4\times S_4:
z\bmod 2=\epsilon(g)
\right\},
\]

其中

\[
\epsilon:S_4\to C_2
\]

为 permutation parity。

乘法继承自 direct product：

\[
(z,g)(w,h)
=
(z+w,gh).
\]

readout：

\[
q(z,g)=g.
\]

kernel：

\[
K
=
\{(0,e),(2,e)\}
\cong C_2.
\]

所以它与 split model \(C_2\times S_4\) 具有完全相同的：

- total order `48`；
- kernel order `2`；
- quotient `S4` order `24`；
- 每个 readout fiber size `2`。

现在取冻结 Gen12/V13 的

\[
b=(AB),
\]

它是 odd transposition。

任意 \(B\in q^{-1}(b)\) 都有 \(C_4\) coordinate \(z\) 为 odd，即 \(z=1\) 或 \(3\)。

于是：

\[
B^2
=
(2,e)
\neq
(0,e).
\]

而 \((2,e)\) 正是非平凡 central kernel element。

因此若存在 homomorphic section \(s\)，则

\[
s(b)^2
=
s(b^2)
=
s(e)
=
e,
\]

与上式矛盾。

所以：

\[
\boxed{
\operatorname{Sec}_{\mathrm{adm}}(q)=\varnothing
}
\]

以及

\[
\boxed{
\mathbf{Lift}_{S_4}(M)=\varnothing.
}
\]

这不是 quotient 后的伪 obstruction，而是 retained relation residue：

\[
\boxed{
z_b=B^2=(2,e)\in K
}
\]

对每个 possible \(B\) 都不可消去。

checker 进一步验证：

- `a=(BCD)` 的 lift residue 可取 `0` 或 `2`，其中 `0` 可被选择；
- `b^2` residue 永远为 `2`；
- `(AB)^4` residue 为 `0`；
- 因此单独 frozen relation `b^2` 已足以杀死 section。

## 11. Minimal-difference certificate

定义：

\[
M^+:\ C_2\times S_4\to S_4,
\]

\[
M^-:\ \widetilde G_2^-\to S_4.
\]

二者均：

\[
|\widetilde G|=48,\quad
|K|=2,\quad
|S_4|=24,
\]

每个 quotient fiber 都有 2 个元素。

差异可以由**一个冻结 defining relation** 读出：

在 \(M^+\) 中，对任何 transposition lift \(B\)，

\[
B^2=e.
\]

在 \(M^-\) 中，对任何 transposition lift \(B\)，

\[
B^2=(2,e)\neq e.
\]

因此这给出一个 one-relation minimal-difference certificate：

`SAME 48/2/24 CARDINALITY PROFILE + DIFFERENT b^2 RELATION RESIDUE`.

这里“minimal”指**证书只需一个 defining relation word**，不主张在所有有限群扩张中证明了绝对最小群阶。

## 12. Exact hierarchy of existence / isomorphism / rigidity

对任意有限 lift groupoid \(\mathcal L\)，定义：

### E — existence

\[
E:
\operatorname{Obj}\mathcal L\neq\varnothing.
\]

### A — all lifts are isomorphic

按字面全称：

\[
A:
\forall x,y\in\operatorname{Obj}\mathcal L,\quad x\simeq y.
\]

注意：空群胚中 \(A\) 真空为真。

### U — exactly one isomorphism class

\[
U:
|\pi_0(\mathcal L)|=1.
\]

### R — one actual object and no nontrivial automorphism

\[
R:
|\operatorname{Obj}\mathcal L|=1
\quad\text{and}\quad
|\operatorname{Aut}(x)|=1.
\]

则 exact logic 为：

\[
\boxed{
U\iff E\wedge A
}
\]

以及

\[
\boxed{
R\Rightarrow U\Rightarrow E.
}
\]

故若把“所有 lift 同构”解释为**非空且 pairwise isomorphic**，它与“唯一同构类”完全相同，而不是另一级。

各 finite witnesses：

| model | E | literal A | U | R |
|---|---:|---:|---:|---:|
| nonsplit parity `C4` pullback | 0 | 1 (vacuous) | 0 | 0 |
| split `C2`, frozen gauge | 1 | 0 | 0 | 0 |
| split `C2`, full gauge torsor | 1 | 1 | 1 | 0 |
| split `C3`, inversion gauge | 1 | 1 | 1 | 0 |
| Gen12 `K=1` | 1 | 1 | 1 | 1 |

所以原任务要求的四种措辞可以全部精确安置，但其中第二、第三只通过“空集真空性”才有逻辑差异。

## 13. Canonicality refinement

群胚还允许区分三种常被混用的“唯一”。

### 13.1 Unique isomorphism class

\[
|\pi_0|=1.
\]

只表示任何两个 choices 存在某个 arrow。

### 13.2 Unique up to unique isomorphism

要求 connected 且每个 isotropy trivial。

split `C2` full-gauge torsor 满足它：

- 2 个 objects；
- 任意两 object 之间恰有一个 gauge arrow；
- 但没有 distinguished object。

### 13.3 Strict rigid object

要求：

\[
|\operatorname{Obj}|=1,\quad
|\operatorname{Aut}|=1.
\]

Gen12 regression 满足。

因此：

\[
\text{unique up to unique iso}
\not\Rightarrow
\text{canonically selected actual section}.
\]

如果“canonical section”定义为被全部有效 model gauges 固定的 actual object，则 split `C2` torsor没有 canonical section，因为非平凡 gauge 交换两个 sections。

## 14. Relation to Gen13 extension/section language

Q3 与 Gen13 的关系可以精确写成：

### Theorem 14.1 — object-layer equivalence

对每个 declared model \(M\)：

\[
\operatorname{Obj}\mathbf{Lift}_{S_4}(M)
=
\operatorname{Sec}_{\mathrm{adm}}(q_M).
\]

故：

\[
\mathbf{Lift}_{S_4}(M)\neq\varnothing
\iff
q_M\text{ admits an admissible homomorphic section}.
\]

因此 groupoid language **不产生新的 section existence theorem**。

### Theorem 14.2 — moduli quotient

\[
\pi_0\mathbf{Lift}_{S_4}(M)
=
\operatorname{Sec}_{\mathrm{adm}}(q_M)/\Gamma_M.
\]

### Theorem 14.3 — isotropy

\[
\operatorname{Aut}_{\mathbf{Lift}}(s)
=
\operatorname{Stab}_{\Gamma_M}(s).
\]

### Strict-difference theorem

若 Gen13 数据只记录：

\[
(q,K,\text{residues},\operatorname{Sec}_{\mathrm{adm}}),
\]

则不能恢复 Q3 groupoid。

split `C2` full-gauge model 与 split `C2` frozen-gauge model 是 exact counterexample：所有上述 object-level data 相同，但

\[
|\pi_0|=1
\]

与

\[
|\pi_0|=2
\]

不同。

如果未来 Gen13 schema 显式加入完整 actual \(\Gamma_M\)-action，则 Q3 groupoid 只是该数据的 action-groupoid repackaging；在那个增强后的语言里，Q3 不再增加数学内容。

因此当前最精确的边界是：

`GEN13 EXTENSION/SECTION = OBJECT LAYER`

而

`Q3 LIFT GROUPOID = OBJECT LAYER + ACTUAL EQUIVALENCE ACTION`.

## 15. What the groupoid upgrade does and does not buy

它**确实增加**：

1. noncanonical choice 的精确 object/orbit 表述；
2. hidden symmetry 的 stabilizer 表述；
3. empty fiber、multi-section torsor、disconnected choice space、orbifold-like isotropy 的统一分类；
4. 对“canonical section”错误升级的直接反例；
5. 一个 invariant functorial language，能在 model isomorphism 下搬运。

它**不增加**：

1. 新的 bare-P000 root primitive；
2. 新的 `S4` existence theorem；
3. 对 extension splitting 的 classical replacement；
4. 对 Gen13 `q/K/residue` obstruction 的绕过；
5. 通过 formal isomorphism 洗掉 actual relation residue 的权限。

所以本任务没有落入 `GROUPOID_REFORMULATION_COLLAPSES_TO_ORDINARY_EXTENSION_THEORY` 的完全 kill：群胚在**存在性对象层**确实只是 section language，但在**canonicality/morphism 层**增加了 Gen13 当前 taskbook 未冻结的 actual equivalence action。

同时它也不是新型 groupoid theory：所用 action-groupoid machinery 本身完全 classical。

## 16. Deterministic checker

Checker:

`research_checks/P000_PHILOSOPHY_FIRST_LIFT_GROUPOID_CHECK_20260830.py`

Atlas:

`research_artifacts/P000_PHILOSOPHY_FIRST_LIFT_GROUPOID/P000_S4_LIFT_GROUPOID_ATLAS_V1.json`

Exact local execution:

```text
PASS P000_PHILOSOPHY_FIRST_LIFT_GROUPOID_CHECK
carrier_S4_order=24
gen12=objects:1,pi0:1,isotropy:1
split_C2_torsor=objects:2,pi0:1,isotropy:1
split_C2_frozen_gauge=objects:2,pi0:2
split_C3=objects:1,pi0:1,isotropy:2
split_V4_affine=objects:4,pi0:1,isotropy:6
nonsplit_C4_parity=objects:0,b2_residue:central_kernel_2
minimal_difference=split_C2_vs_parity_C4_pullback_same_48_2_24_profile_single_b2_relation
strength_boundary=pairwise_isomorphic_vacuous_on_empty;nonempty_pairwise_iff_unique_pi0
model_isomorphism_invariance=PASS
```

checker 精确枚举 frozen carrier generators：

\[
a=(BCD),\qquad b=(AB)
\]

并独立验证：

\[
a^3=b^2=(ab)^4=e,
\qquad
|\langle a,b\rangle|=24.
\]

然后逐一枚举上述有限 extension 的 candidate lifted generators / sections、relation residue、orbits 和 stabilizers。

## 17. Hard-target disposition

Hard target:

`P000_S4_LIFT_GROUPOID_AND_FIBER_REGIMES_EXACTLY_CLASSIFIED`

本任务在声明 finite relation-phase model class 上完成：

1. **严格定义 objects / morphisms**：完成；
2. **model-isomorphism invariance**：证明并 checker regression；
3. **Gen12 rigid/trivial-kernel fiber**：完成；
4. **multi-object fiber**：split `C2`，2 objects / one free orbit；
5. **nontrivial automorphism fiber**：split `C3`，one object / isotropy `C2`；另有 `V4` / isotropy `S3`；
6. **empty fiber**：nonsplit parity `C4` pullback；
7. **minimal-difference certificate**：same `48/2/24` profile，single `b^2` residue 区分；
8. **四种强度逻辑关系**：完成，并发现 nonempty 时 pairwise-isomorphic 与 unique-iso-class 等价；
9. **Gen13 relation theorem**：objects 等价于 sections；morphisms 严格依赖 actual gauge semantics；
10. **relation residue retention**：完成，无 quotient。

因此 terminal：

\[
\boxed{\texttt{LIFT_GROUPOID_FINITE_CLASSIFICATION}}
\]

## 18. Recommended next control-plane move

最值得继续的不是再造一个普通 extension witness，而是把 Q3 与刚完成的 Q2 probe obstruction 接起来：

Q2 已证明 fixed-radius local probes 无法在一般 finite Cell class 上重构 native global identity；Q3 则证明“所有 lift choices + path of equivalences”天然形成 groupoid，并且 object-only observation 不足以恢复 morphism structure。

因此下一步可测试：

`P000 PATH/GROUPOID TRANSPORT PROBE AS A NONLOCAL SEPARATING OBSERVABLE`

具体问：

> 是否存在一个 P000-native、不过度携带 full identity 的有限 path/transport probe，能读取 Q3 的 orbit/stabilizer 或 holonomy residue，从而杀死 Q2 的 fixed-radius indistinguishability family？

这是比继续增加 local radius 更有结构价值的方向。

同时必须保持：

- 不把 carrier `S4` 升级成 bare-P000 native group；
- 不把 relation-phase toy model 升级成 root reality；
- 不把 groupoid vocabulary 当 novelty；
- 不在 morphism 语义未给定时从 `q/K` 猜 arrows。
