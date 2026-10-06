# signature 2/3/4/6 的中心 character 立方、genus-9 同时线性化覆盖与偶次张量盲点

Status: `FREE_RESEARCH / DERIVED_FOUR_SIGNATURE_CHARACTER_CUBE / EXACT_LINEARIZATION_DEGREE_AND_GENUS / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Parent candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN`
Research unit: `EM-FREE-F6D046-R5-FOUR-SIGNATURE-CHARACTER-CUBE`
Blindness status: `ANCHOR_EXPOSED / PHASE-B CONTINUATION`

## 0. 结果

R4 在 `X0(12)` 上比较 signatures `2,3,4`，得到独立 quadratic characters `chi2,chi4`。加入 `U_6(w)=2F1(1/6,5/6;1;w)` 后，在将 signature 6 projectivization 与 signature 3 的 `(infinity,infinity,3)` triangle local system 作标准 marking 同一化的前提下，signature 6 引入第三个独立二次 character `chi6`，而不是 `chi2 chi4`。

signature 6 在 `X0(12)->X0(3)` 上方两个 index-3 的 order-3 原像处有中心 monodromy -I：`{1/6,5/6}` 经 e=3 变成 `{1/2,5/2}`。signature 3 则变成 `{1,2}` 与 +I。故 chi6 的紧化分支集 B6 有两个内部点。

R4 的 B2 是两个 cusps，B4 是四个 order-2 内部原像；B2、B4、B6 两两不交。于是 `<chi2,chi4,chi6> ~= (Z/2)^3`。四个经典 signatures 对应 cube 顶点 `0,chi2,chi4,chi6`，不是 Klein four subgroup。

共同 kernel cover 最小次数为 8。紧化后总分支点数 `2+4+2=8`，每点 inertia C2；Riemann--Hurwitz 给出 `g=9`。七个非平凡 quadratic intermediate covers 的 branch counts 是 `2,4,2,6,4,6,8`，genera 是 `0,1,0,2,1,2,3`，总和 9。

所有 transition characters 仍严格满足 cocycle，新增的是 H1 character rank 从 2 增至 3，而非 higher associator。

所有偶次 homogeneous tensor functors 都看不见这三个 characters：`Sym^(2k)(chi tensor L)=Sym^(2k)L` 且 `wedge^2(chi tensor L)=wedge^2 L`。所以 Clausen squares 与 Wronskian determinant lines 可在四种 signature 间一致，而线性 period carriers 仍需 degree-8 genus-9 cover 才能同时选定。只观察面积、Gram/symmetric-square 或其他偶次张量 readout，原则上无法恢复 quadratic spin/phase lift。

## 1. signature 6 的局部 lift

Gauss 方程 H_a 的指数为 `0:{0,0}`, `1:{0,0}`, `infinity:{a,1-a}`。a=1/3 时三重拉回把 `{1/3,2/3}` 变成 `{1,2}`，monodromy +I；a=1/6 时把 `{1/6,5/6}` 变成 `{1/2,5/2}`，monodromy -I。两者 projective order 都是 3，但 SL2 lift 相差中心符号。

X0(12)->X0(3) 次数 6，source torsion-free，所以 order-3 point 有两个三重原像；这就是 B6。

## 2. character independence

围绕 B2、B4、B6 单点的小环分别给联合 character 值 `(-1,+1,+1)`, `(+1,-1,+1)`, `(+1,+1,-1)`。故 `Phi=(chi2,chi4,chi6)` 满射到 `(Z/2)^3`。

## 3. simultaneous linearization

任何同时平凡化四个 relative characters 的连通覆盖，其基本群包含 ker Phi，故次数至少 8；共同 kernel cover 达到下界。

在 genus-zero X0(12) 上，八个 branch points 每个在 degree-8 cover 中贡献 4：`2g-2=8*(-2)+8*4=16`，所以 g=9。

## 4. 四对象 cocycle

令 chi_(3)=1, chi_(2)=chi2, chi_(4)=chi4, chi_(6)=chi6，并定义 `chi_ij=chi_(i)chi_(j)^-1`。任意三元组均有 `chi_ij chi_jk=chi_ik`；任意四元复合严格结合。因此 obstruction 是 `H1 rank 3 / H2 associator 0`。其余四个 cube vertices 是合法 quadratic twists，但本轮不把它们命名为新的 classical signatures。

## 5. 偶次张量盲点

对次数 d 的 homogeneous polynomial functor P_d，`P_d(chi tensor L)=chi^d tensor P_d(L)`。d 偶时 quadratic twist 消失，d 奇时保留。

- Sym^2 是 Clausen rank-3 carrier，抹去全部中心 characters；
- rank-2 determinant/Wronskian line 是 wedge^2 L，也抹去 characters；
- period vector、first jet 和 odd-degree carriers 保留 character；
- vector-covector scalar pairing 的 twists 抵消，所以 1/pi 标量本身也看不见 linear-lift ambiguity。

因此原始 Wronskian 解释与当前 character cube 相容：1/pi 可是跨 signature 的共同守恒面积，而周期向量仍有三个独立 quadratic holonomies。

## 6. P000 边界

只检查偶次/二次 readouts 可能产生全局兼容的假象，却遗漏 linear/spin lift obstruction。若 P000 六维切片结构需要区分中心符号，必须另带 odd-degree 或 sign-sensitive transport 数据。本结果不推出物理 spin 结构，也不决定六维补空间。

## 7. 审计

T9 Holonomy/Cocycle/Gluing: `REUSE_APPLIED`。T7 Finite Symmetry/Equivariance: `COMPOSE_APPLIED`。新工具：`NO_NEW_TOOL_FAMILY`。公理门：`REJECT_AS_NEW_AXIOM / DERIVED_FOUR_SIGNATURE_CHARACTER_CUBE / EXACT_EVEN_READOUT_NO_GO / NOT_FOUNDATION`。
