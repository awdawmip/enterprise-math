# 中心 lift torsor、H2/H1 两级阻碍与偶次观测重构 no-go

Status: `FREE_RESEARCH / DERIVED_CENTRAL_LIFT_TORSOR / EXACT_RECONSTRUCTION_NO_GO / STANDARD_COHOMOLOGICAL_MECHANISM / NOT_AXIOM / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Parent candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN`
Research unit: `EM-FREE-F6D046-R6-CENTRAL-LIFT-TORSOR-EVEN-READOUT-NOGO`

## 0. 主结论

对中心扩张 `1 -> mu2 -> SL2 -> PSL2 -> 1`，给定 projective local system `rho_bar:pi1(X)->PSL2`：

1. 是否存在 linear lift 的阻碍位于 `H2(X,mu2)`；
2. 一旦至少一个 lift 存在，全部 admissible lifts 构成相应 `H1(X,mu2)` subgroup 的 torsor；
3. 任意两个 lifts 的差是唯一 quadratic character chi，即 `rho1=chi rho0`；
4. 偶次数 homogeneous polynomial functor 对 chi 完全不敏感，奇次数 functor 保留 chi；
5. 所以 projectivization 加任意多偶次 tensor readouts，仍不能重构 linear lift。

若一组对象产生 character subgroup A，则所有偶次 readouts 的 reconstruction fiber 至少含 |A| 个 lifts。消除歧义必须提供 odd/sign-sensitive datum，或拉回到联合 character map 的 kernel cover，最小次数为 joint image order。

R5 有 `A~=(Z/2)^3`，所以 Wronskian、determinant、Clausen square 与全部偶次 readouts 至少有 8 元不可辨识纤维。

## 1. 两级 obstruction

projective representation 的 central-lift connecting class记为 `o(rho_bar) in H2(G,mu2)`。

- `o != 0`: 无 SL2 lift，属于 existence obstruction；
- `o = 0`: 选一个 lift rho0 后，characters chi in H1(G,mu2)=Hom(G,mu2) 作用为 chi*rho0。任意两个 lifts 的商逐点落入 center mu2，且由乘法性成为唯一 character。

若固定 puncture 的线性 conjugacy classes，只保留满足局部条件的 `H1_adm`。R4/R5 已显式给出 lifts，故共同 punctured base 上 H2 existence obstruction 为零；剩余是 H1 ambiguity。

## 2. strict transition cocycle

写 `rho_i=chi_i rho0`，则 `chi_ij=chi_i chi_j^-1`，从而 `chi_ij chi_jk=chi_ik`。pairwise transition 的三重乘积为 1。该结论依赖 lift torsor 已非空；尚未证明可 lift 的裸 projective cocycle 仍须先检查 H2。

## 3. homogeneous functor parity

对 degree d homogeneous polynomial functor P_d，中心 -I 作用为 (-1)^d，故 `P_d(chi tensor V)=chi^d tensor P_d(V)`。

- d even: quadratic twist 消失；
- d odd: twist 保留。

实例：Sym2、wedge2/determinant、Gram/bilinear forms、vector-covector scalar contraction均 even-blind；period vector、first jet、Sym3 均 sign-sensitive。一般 Schur functor只由 partition size parity 决定。

## 4. reconstruction no-go

任何只由 projectivization 和偶次 homogeneous functors 构成的数据提取器 E 都满足 `E(rho)=E(chi rho)`。若 A 非平凡，E 在 A-orbit 上常值，故 reconstruction 不可能单射。增加更多同类偶次 invariants 无效，因为整个 functor class 都把中心 mu2 商掉。

一个 odd witness 只能把 ambiguity 降到其 stabilizer；当 A 对 witness 忠实作用时才完全恢复 lift。

## 5. kernel-cover minimality

对 characters chi_i，联合映射 `Phi:G->product mu_ni`。任何使全部 characters 平凡的 connected cover 对应 H subset ker Phi，故 `[G:H] >= |im Phi|`；kernel cover 达到下界。R4 image order 4，R5 image order 8。

若 compact base genus g0、Galois group order q、每个 branch point inertia order2、共 b 点，则 `2g-2=q(2g0-2)+b q/2`。R5 取 q=8,g0=0,b=8，得 g=9。

## 6. 对 1/pi 解释的闭合

Wronskian/有向辛面积位于 determinant line wedge2 L；quadratic twist 作用为 chi^2=1。因此跨 signature 的 Wronskian 可一致，而 period vectors 仍无共同 linear trivialization。

Ramanujan operator 是 dual jet covector 与 jet vector 的 scalar pairing；dual/primal twists在标量中抵消。因此共同 1/pi 数值不是 linear-lift 等价的证据。

真正保留 linear provenance 必须记录 odd-degree carrier 或 character class。

## 7. P000 typing

P000 多切片输入应分层记录 projective carrier、H2 lift obstruction、H1 lift torsor、readout degree parity。该框架不构成新公理，也不证明 Enterprise 六维空间具有物理 spin structure。

## 8. 审计

T9: `REUSE_APPLIED`。T7: `COMPOSE_APPLIED`。Tool classification: `GLOBAL_SUBTOOL_CANDIDATE_NOT_PROMOTED / STANDARD_MECHANISM_SPECIALIZATION`。Axiom gate: `REJECT_AS_NEW_AXIOM / STANDARD_COHOMOLOGICAL_DERIVATION / EXACT_RECONSTRUCTION_NO_GO / NOT_FOUNDATION`。
