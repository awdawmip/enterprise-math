# CBRC F7 Driver r445 — exact B=10 half-defect certificate inside the homogeneous class

Date: 2026-11-21 (+08:00). Driver auxiliary research line `EM-DVR-DEBB5E`. Original author `EM-CBRCF7-83A1D4`, original Task `RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION`, original frozen Result `RR-AA38973D56330E59D315`. This is new finite mathematical evidence, not a Native Review, Result acceptance, Task closure, or P000 alteration.

## Exact proposition

Let `u=(1,1,-1,-1)`, `v=(1,-2,-1,2)`, `A=I+uv^T`. For `z=(a,b,c,d)` put `t=a-2b-c+2d`, so that `Az=(a+t,b+t,c-t,d-t)`. Set

`D_q(z)=q(a+t,b+t)+q(c-t,d-t)-q(a,b)-q(c,d)`.

The original F7 admissible class comprises all `q:Z²→[0,∞)` satisfying `q(0,0)=0`, `q(x,y)=q(-x,y)`, `q(n,0)=1` for every nonzero integer `n`, `q(x,y)≥1/2` for nonzero pairs, and `q(2,1)=q(-1,-1)=1/2`. There is no assumed homogeneity in the original class. For `B≥1` define `E_B=inf_q max_{z∈[-B,B]^4∩Z^4}|D_q(z)|`.

**Exact theorem:** `E_10=1/2`. In fact, a stronger witness exists: a globally defined scalar `q` respecting all original admissibility conditions and satisfying `q(kx,ky)=q(x,y)` for every positive integer `k`, with `max_{z∈[-10,10]^4}|D_q(z)|=1/2`.

Consequently `E_B=1/2` for every integer `1≤B≤10`. This strengthens r439's verified near-half result at B=10. It does not decide the global supremum over all `z∈Z^4`, and is compatible with r441 compactness and r444 ray-mark homogenization.

## Fully specified rational witness

Define `Q(x,y)=10q(x,y)`, an exact integer-valued function. Set `Q(0,0)=0`, `Q(x,0)=10` for `x≠0`. If `y≠0`, let `g=gcd(|x|,|y|)`, `r=(|x|/g,y/g)`. Set `Q(x,y)=T[r]` for the 574 primitive signed rays in the included frozen table `T`, and `Q(x,y)=5` for every other non-axial ray. All frozen `T` values are in `{6,7,8,10}`. Both marked rays `(2,1)` and `(1,-1)` retain the default 5.

The table is embedded directly in the standalone standard-library checker as a zlib-compressed base64 ASCII list `a,b,value`, with decoded table SHA256
`aaccfb63cc2e12e9f2d4de2ac7c16370caac90c503cc574088c866faca7a26c1`.
This is merely a compact literal representation of the exact finite table, not a numerical-fitting dependency. The function extends to **all** integer pairs by the above explicit formula. Its axis, positivity, J-evenness, fixed marks, and positive-integer-dilation homogeneity follow immediately from that formula.

## Finite exhaustive verification and sharp lower bound

The independent integer-only checker `research_checks/CBRC_F7_R445_B10_HOMOGENEOUS_HALF_EXACT_CERT_20261121.py`:

1. Decodes and hashes the 574-entry rational table, checking canonical primitive rays, allowed values, distinctness, and absence of marked-ray overrides.
2. Enumerates exactly all `21^4=194481` input tuples `z∈[-10,10]^4∩Z^4`.
3. Evaluates `10D_q(z)` using integer operations and the original matrix formula, verifying `|10D_q(z)|≤5` for every tuple. The observed exact maximum is `5`, attained at **38,042** tuples.
4. Confirms the explicit lower-bound witness `z=(1,-1,0,0)`, for which `Az=(4,2,-3,-3)` and `D_q(z)=1/2+1/2-1/2-0=1/2`.

Thus the upper bound follows from the complete finite check and the lower bound from the fixed marks, giving exact equality. Certificate discovery used a sparse finite LP, but executing this checker uses **only Python's standard library and integer arithmetic**; neither HiGHS nor floating-point tolerance enters the proof check.

Locally executed checker returned: `PASS: B=10, inputs=194481, distinct_exception_rays=574, max_abs_defect=5/10, equality_count=38042, witness=(-10,-10,-2,-10)`. A separate initial full enumeration of the rounded rational LP candidate produced the same exact maximum and equality count.

## Scope and next research

This is an exact finite-domain theorem with a homogeneous admissible witness; it does not provide a global bound `E(q)≤1/2` for that witness. The current global known bound remains `1/2≤E_∞≤4/7`, with finite B=12 equality still not proven. The useful next discriminator is to test homogeneous B=12 with an exact frozen certificate or derive a finite linear dual obstruction; an LP floating-point success alone is not a theorem.

Preserve the original F7 source/result, author, all previous Driver results r435–r444, and existing formal review/intake authority. Driver-auxiliary numerical construction is not an independent Native Review of the original frozen Result.
