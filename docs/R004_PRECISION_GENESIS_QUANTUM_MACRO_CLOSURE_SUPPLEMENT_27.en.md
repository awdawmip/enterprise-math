# R004 precision genesis — Supplement 27: structural defect diamond and premature-collapse debt

Status: `PROVED_WIP + EXECUTABLE_REFERENCE + P-ADIC INTERACTION LAW`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_26.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplements 20 and 23 made the linear Structural Target defect an exact p-adic module with chain-additive mass. Supplement 24 then identified semantic last use. This supplement connects those results in a two-axis law: **what the current representation knows** and **what the remaining future still needs** interact through a canonical finite p-group.

## 1. Two axes

Let `R=Z/p^K`. Use row-submodule coordinates:

- `U=Row(A)` for the current/finer observation;
- `U' subseteq U` for a coarser observation;
- `W=Row(B)` for a stronger target requirement;
- `W' subseteq W` for a weaker remaining target requirement.

The Structural Target defect is

`D(U,W)=(U+W)/U`.

Let `mu(M)=log_p |M|` for a finite p-group. Then

`delta(U,W)=mu(D(U,W))`.

For finite subgroups,

`|U+W||U cap W|=|U||W|`,

so

`delta(U,W)=mu(W)-mu(U cap W)`.

Thus target defect is exactly the target mass not already contained in the observation-target intersection.

## 2. Opposite monotonicities

If observation is coarsened,

`U' subseteq U`,

then

`delta(U',W)>=delta(U,W)`.

If the future target is weakened,

`W' subseteq W`,

then

`delta(U,W')<=delta(U,W)`.

So representation loss and semantic retirement move the same defect coordinate in opposite directions.

## 3. Observation-loss increment modules

The additional target defect created by coarsening observation from U to U' while target W remains live is

`J_W=(U cap W)/(U' cap W)`.

For the weaker target W',

`J_(W')=(U cap W')/(U' cap W')`.

There is a canonical injection

`J_(W') -> J_W`,

because an element of `U cap W'` that becomes zero modulo `U' cap W` already lies in `U' cap W'`.

Define the **structural interaction module**

`I = J_W / J_(W')`.

It has the explicit form

`I ~= (U cap W) / ((U' cap W) + (U cap W'))`.

Hence

`0 -> J_(W') -> J_W -> I -> 0`.

## 4. Target-retirement increment modules

The defect removed by weakening the target W to W' while observation is U is

`L_U=(U+W)/(U+W')`.

Under the coarser observation U' it is

`L_(U')=(U'+W)/(U'+W')`.

There is a natural surjection

`L_(U') -> L_U`.

Its kernel is canonically isomorphic to the same interaction module I. Thus

`0 -> I -> L_(U') -> L_U -> 0`.

The same finite p-group therefore measures both:

- how much **extra observation-loss defect** exists only because the stronger target W is still live;
- how much **extra target-retirement benefit** appears after the observation has already been coarsened.

## 5. Four-point law

Taking p-exponent masses yields

`mu(J_W)=mu(J_(W'))+mu(I)`

and

`mu(L_(U'))=mu(I)+mu(L_U)`.

Equivalently,

`delta(U',W)+delta(U,W')-delta(U,W)-delta(U',W') = mu(I) >= 0`.

This is an exact four-point cross-supermodular law on nested observation/target submodules.

Supplement 20 showed that defect as a function of arbitrary hidden coordinate sets is neither generally submodular nor generally supermodular. There is no contradiction: the stronger law appears only after moving to the correct typed coordinates `observation submodule x target submodule`.

## 6. Premature-collapse debt

Suppose the target distinction `W/W'` will soon become dead.

If observation is coarsened **before** target retirement, the new defect paid is `J_W`.

If the target is weakened first and the same observation coarsening happens afterwards, the new defect paid is only `J_(W')`.

The exact additional price of collapsing too early is

`mu(I)=mu(J_W)-mu(J_(W'))`.

Therefore I is a typed **premature-collapse debt module**.

The smallest example is over `F_2^2`:

`U=W=<e_1>`, `U'=W'=0`.

Coarsening observation while `e_1` is still a live target direction costs one bit of structural defect. Retiring that target direction first makes the same later observation collapse free.

Over `Z/2^K`, choosing `U=W=<2^t e_1>` gives interaction depth `K-t`; the penalty is genuinely p-adic, not only rank-one.

## 7. Connection to backward semantic liveness

Supplement 24 said: do not erase a certificate distinction before its last future-sensitive use.

This supplement adds a resource theorem:

> even when an early collapse could later be repaired, performing it before semantic last use incurs exactly the interaction-module debt `I`.

Thus the compiler now has both:

- a correctness reason to delay collapse while a distinction is live;
- an exact p-adic cost for collapsing prematurely and repairing later.

## 8. Validation

Independent exact checks include:

- **6,000** random subgroup rectangles over small 2- and 3-power ambient modules: defect intersection identity, opposite monotonicities and nonnegative four-point interaction all held; 657 cases had strictly positive interaction;
- **1,500** additional random p-group rectangles: observation-loss and target-retirement short exact sequences matched exponent masses;
- **900** random rectangles: the explicit interaction quotient profile matched the kernel profile of `L_(U')->L_U`, not only total cardinality.

These are finite exact WIP checks, not fresh full-repository CI or canonical-main claims.

## 9. Prior-art and next frontier

Finite subgroup product/intersection cardinality, modular-law quotient identities and butterfly/second-isomorphism style arguments are prior algebra. R004's project-local addition is the interpretation of their common quotient as the interaction between representation loss and future target liveness in the typed compiler.

The next frontier is **multi-target interaction**. With several future target modules `W_1,...,W_m`, can the premature-collapse debt be decomposed by a Möbius/inclusion lattice of target overlaps without double-counting shared structure? Any such decomposition must remain integer/module-valued and must not assume distributivity of the subgroup lattice where it fails.
