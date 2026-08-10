# R004 precision genesis — Supplement 28: multi-target structural synergy

Status: `PROVED_WIP + EXECUTABLE_REFERENCE + NONDISTRIBUTIVE TARGET INTERACTION`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_27.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 27 introduced a two-axis interaction module between observation loss and target liveness. This supplement studies several simultaneous target modules and closes the first non-distributive boundary.

## 1. Joint target defect

Let U be the current observation row module and let W1,W2 be two target row modules. The joint target is their sum

`W12=W1+W2`.

The defect mass is

`delta(U,W)=mu(W)-mu(U cap W)`.

Ordinary inclusion-exclusion using only W1, W2 and their intersection is not sufficient because, in a modular but non-distributive subgroup lattice,

`U cap (W1+W2)`

can strictly contain

`(U cap W1)+(U cap W2)`.

## 2. Structural synergy module

Define

`S_U(W1,W2) = (U cap (W1+W2)) / ((U cap W1)+(U cap W2))`.

This quotient is zero exactly when U-intersection distributes over this particular target sum.

Using

`mu(W1+W2)=mu(W1)+mu(W2)-mu(W1 cap W2)`

and the corresponding subgroup-sum identity inside U gives

`delta(U,W1+W2)`
` = delta(U,W1)+delta(U,W2)`
`   - delta(U,W1 cap W2)`
`   - mu(S_U(W1,W2))`.

Thus naive inclusion-exclusion overcounts joint missing structure by exactly the synergy module.

## 3. Minimal XOR-style example

Over `F_2^2`, let

`U=<e1+e2>`,

`W1=<e1>`,

`W2=<e2>`.

Then

`U cap W1=U cap W2=0`,

so both individual target defects have mass 1 and the target intersection defect is 0.

But

`U cap (W1+W2)=U`,

so the synergy mass is 1 and the joint defect is only 1.

The current observation knows a cross-target combination without knowing either target component separately.

## 4. Individual and overlap summaries do not determine joint precision

Compare two systems with the same targets W1,W2.

### System A

`U=0`.

Then

`delta(W1)=1`, `delta(W2)=1`, `delta(W1 cap W2)=0`,

and the joint defect is 2.

### System B

`U=<e1+e2>`.

The same three individual/overlap defect masses are still `(1,1,0)`, but the joint defect is 1 because the synergy module has mass 1.

Therefore even all individual target masses plus their ordinary overlap mass do not determine joint target precision. Relative embedding into the current observation matters.

The same warning applies to invariant profiles: summaries of isolated targets cannot recover cross-target position.

## 5. Relation to earlier coupled-observable results

This is the linear/module form of a phenomenon already seen earlier in R004: a coupled observable can preserve a joint combination that is invisible from marginal coordinates.

The module quotient `S_U` is an exact measure of that coupling at the target/observation level.

## 6. Validation

Independent exact checks over **6,000** random small 2- and 3-power subgroup systems verified

`delta(U,W1+W2)=delta(U,W1)+delta(U,W2)-delta(U,W1 cap W2)-mu(S_U)`

with zero mismatches. 357 cases had strictly positive synergy.

These are finite exact WIP checks, not fresh full-repository CI or canonical-main claims.

## 7. Prior-art and next frontier

Subgroup modularity and failures of distributivity are prior algebra. R004's project-local addition is the identification of the distributivity-defect quotient as the correction term required by multi-target precision accounting.

For three or more targets, a Boolean-lattice Möbius formula over intersections alone cannot be assumed. The next question is whether recursive target sums admit a canonical **interaction tree** or whether different parenthesizations carry genuinely different intermediate synergy modules whose total compensation is controlled only up to extension/isomorphism data.
