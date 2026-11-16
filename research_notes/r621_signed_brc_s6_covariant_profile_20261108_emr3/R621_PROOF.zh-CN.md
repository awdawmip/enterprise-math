# R621｜冻结 signed BRC 十二支路的 S₆ 协变方向框架与闭路分级计数

Date: 2026-11-08; AUTHOR / UNREVIEWED / NOT_ADMITTED.

## 1. Scientific input and typed scope

Freeze R462 signed BRC K/J→B→D at commit `18783e01e3646c72b7aab3b16d3f565e83e6446f`, K implementation blob `7fa7a762f758b30c6090468ac43487daa34abad8`, theta=0, B₀=1+t. The original twelve K_i ∈ Z[t] satisfy ν_t(K_i)=i−1 and leading integers
`(2,-1,-8,-11,6,53,106,119,83,36,9,1)`.
The verification script actually recomputes all twelve polynomials from the R462 binomial formula.

Use P000's six-axis X6 spatial Cell torsor and pure adjacency ±e_j with its registered finite S₆ positive-axis permutation skeleton. Retain R619/R620's *experimental* label decoration `2j−1 ↦ +e_j; 2j ↦ −e_j`, j=1,…,6. A B₀-source word w retains order, spatial displacement z(w), source level s(w)=Σi, and original signed weight W(w)=∏K_i(t). Internal fields and separately typed time are not presumed to be determined by this decoration.

Question: which exact representation lets original anisotropic K profile coexist with the P000 S₆ permutation skeleton, and what are the exact graded counts of closed sources?

## 2. Theorem A — fixed K-label scalar invariance fails

Let P_j=(K_(2j−1),K_(2j)) be the ordered +/− profile of axis j. Under an axis permutation exchanging axes 1 and 2, the step +e₁ goes to +e₂, but K₁=2+3t has valuation 0, while K₃ has valuation 2. Therefore a fixed, unchanged scalar assignment of these K labels cannot be invariant under all S₆ axis permutations.

Even on two-step closed paths, (+e₁,−e₁) has s=3, ν=1, leading coefficient −2, while (+e₆,−e₆) has s=23, ν=21, leading coefficient 9. The obstruction applies precisely to an *unchanged* coefficient profile, not to an oriented or explicitly anisotropic extension.

## 3. Theorem B — exact 720-state S₆-covariant extension and interface-specific optimality

Let G=S₆ act on ±e_j by permuting j while retaining sign. Take an internal orientation π∈S₆: base coefficient axis k resides at spatial axis π(k). Define

`i_π(+e_j)=2π⁻¹(j)−1`, `i_π(−e_j)=2π⁻¹(j)`,
`F_π(a)=K_(i_π(a))`, `q_π(a)=i_π(a)`.

Define a formal ordered decorated X6 path state H=(z,w,π,s,W), with initial (0,empty,id,0,1), and exact single-step update

`T_a(z,w,π,s,W)=(z+a,w·a,π,s+q_π(a),W·F_π(a))`.

For g∈G, act simultaneously as
`g·(z,w,π,s,W)=(gz,gw,g∘π,s,W)`.
Then `(g∘π)⁻¹(g(j))=π⁻¹(j)` gives `i_(gπ)(ga)=i_π(a)`. Hence the exact intertwining law

`T_(ga)(gH)=g(T_a H)`

holds for every H, a, g. Induction proves covariance for every finite ordered path; scalar K, s, signed amplitude, endpoint relation and ordered provenance are exactly preserved under simultaneous profile rotation.

**Minimum orientation-state capacity for this interface.** The six ordered profiles P_j are pairwise distinct, since the plus valuations 0,2,4,6,8,10 differ. Thus `Stab_G(P)={id}` and `|G·P|=6!=720`. Any profile-equivariant finite internal-state interface that outputs P in one state must include states mapping onto all 720 distinct rotated profiles. It therefore requires at least 720 distinguishable states. The constructed π has exactly 720 and attains the bound; fixed-width encoding takes exactly `ceil(log₂720)=10` bits (e.g., factoradic permutation rank 0..719). This is a conditional result about *profile orientation*, not a blanket lower bound for all native memory.

For future operations consisting only of these scalar K updates and (z,s,W,π) readouts, one may omit explicit w and still obtain a closed update. Ordered source selection instead requires w or an exact source encoding (R618). π is internal state, never a seventh spatial axis. The S₆ skeleton is the registered P000 axis-permutation subgroup, not a claim of complete native rotation dynamics.

## 4. Theorem C — exact graded closed-source generating function and integer DP

For coordinate-closed words, the positive and negative counts on axis j coincide; call both r_j≥0. Set `R=Σr_j`, `h=Σ(j−1)r_j`. R620 proves `s=3R+4h`, `ν=R+4h`; for fixed r there are `(2R)!/∏(r_j!)²` distinct words. Put

`a_j=alpha_(2j−1)alpha_(2j)=(-2,88,318,12614,2988,9)`.

Define the integer number of words `C_(R,h)` and the signed sum `L_(R,h)` of the **individual word leading coefficients**, with constraints Σr=R, Σ(j−1)r=h:

`C_(R,h)=Σ (2R)!/∏(r_j!)²`,
`L_(R,h)=Σ (2R)! ∏a_j^(r_j)/∏(r_j!)²`.

As formal power series in Q[[u,x]], the exact generating functions are

`Σ C_(R,h)u^R x^h/(2R)! = ∏_(j=1)^6 Σ_(k≥0) u^k x^((j−1)k)/(k!)²`,
`Σ L_(R,h)u^R x^h/(2R)! = ∏_(j=1)^6 Σ_(k≥0) a_j^k u^k x^((j−1)k)/(k!)²`.

Proof: selecting k_j copies from factor j enforces precisely the R and h constraints, while (2R)! accounts for ordering the 2R signed steps. This is a formal factorial identity; no numerical Bessel/trigonometric computation is used.

An integer recurrence reuses the existing X6 balanced ±-step combinatorial formula. Insert k pairs of a *new* axis into a previously balanced path of length 2r. The number of shuffles is

`M(r,k)=binom(2r+2k,2k)binom(2k,k)`.

Starting with C=L=1 at (r,h)=(0,0), update a previous (r,h) to (r+k,h+(j−1)k), adding C·M to the count and L·M·a_j^k to the signed total. It is exact for all R,h with standard arbitrary precision integers.

Reflect axes j↔7−j; r is permuted, the number of words unchanged, and h maps to 5R−h. Therefore `C_(R,h)=C_(R,5R−h)`. For R≥1 each `0≤h≤5R` has C>0 by R620's constructive digit decomposition.

Level 21: (R,h)=(7,0) gives v=7, C=3432, L=−439296; (R,h)=(3,3) gives v=15, C=920, L=−17585440, total 4352 ordered closed words. L is a **graded sum of source leading terms**, not necessarily a coefficient of the whole B_s after J terminals and higher-order contributions.

## 5. Corollary D — eventual exact noncancellation at each fixed h

Let (R)_k denote falling factorial. For fixed h≥0, any tuple (k₂,…,k₆) with Σ(j−1)k_j=h has K=Σk_j≤h. For R≥h,

`L_(R,h)=binom(2R,R)(−2)^R Q_h(R)`,

`Q_h(R)=Σ_(k₂,…,k₆) (R)_K² ∏_(j=2)^6 [(a_j/(−2))^k_j/(k_j!)²]`,

with the same h constraint. Q_h is a rational polynomial in R. The only tuple with K=h is k₂=h and all other k=0; it yields degree 2h with nonzero leading coefficient `(−44)^h/(h!)²`. Every other tuple has K≤h−1 and degree ≤2h−2. Thus Q_h has exact degree 2h and, for each fixed h, there is some finite R_h such that every integer R≥R_h has L≠0 with sign `(−1)^(R+h)`.

Exact low-order polynomials:
`Q_0=1`;
`Q_1=−44R²`;
`Q_2=R²[484(R−1)²−159]`.
The finite search found no zero L among all 1≤R≤27 and 0≤h≤5R; the universal theorem above is the fixed-h eventual result, with no uniform-in-h threshold asserted.

## 6. Verification, reuse and next unit

`R621_VERIFY.py` reconstructs all 12 original signed K branches exactly, tests all 720 orientations and five S₆ adjacent transpositions, checking 43,200 single steps and 518,400 length-two full-polynomial equivariance instances. It verifies the closed-source integer DP, reflection symmetry and fixed-h (h≤2) formulas for R≤27, plus level21 aggregate results. Exact execution evidence in `R621_EVIDENCE.json`, PASS `R621_S6_COVARIANT_PROFILE_EXACT_PASS`. Full-length claims are proved algebraically above.

Concrete reuse: P000 X6 Cell torsor §3/§9/§10 (native pure adjacency, S₆ skeleton, balanced-path exact count), R616 noncommutative source carrier, R620 closed-source semigroup, and frozen R462 binomial K operator. Resolution: `REUSE_APPLIED` and `EXTEND_EXISTING_TOOL` for the graded count implementation.

Next: examine registered native joint packet/field/time update operators for an admissible internal profile-orientation field and test a nontrivial operator commuting with the G action. A failure should be preserved with an exact operator-level witness. The construction is an exact formal decorated pure-X6 path bridge; legal native field dynamics and Driver admission are independent open questions.
