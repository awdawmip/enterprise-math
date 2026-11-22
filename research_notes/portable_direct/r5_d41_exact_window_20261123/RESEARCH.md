# R5 — Exact 41-order disappearance window, return at m=83, and residue-class counterexample

Date: 2026-11-23 (Asia/Shanghai). Status: **AUTHOR_EXACT_FINITE_PROOF / NOT_REVIEWED**.
Research mode: independent portable scientific continuation. No formal shared CLAIM, native X6 theorem, BRC theorem or formal Result is asserted.
Frozen science: `awdawmip/enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15`.
Direct predecessor: `5280a3eda9a9aa50afeed540e1f22921a9bd732e:research_notes/portable_direct/r5_linear_second_drop_m78_20261123/RESEARCH.md`.
Additional finite-jet verifier reused verbatim as mathematics, not re-published: `882ac53313bd4536df22f2bd963002bc1304aa29:research_notes/portable_direct/r5_linear_first_drop_20261123/VERIFY_FIRST_DROP.cpp`.

## Definitions and precise new theorem

Use exactly the frozen five-event scalar model, integer price set `214..314`, and failures `S0=214..218`, `S1={214,216,217,218,219,220,221}`, `S2={215,216,217,218,219,220,221}`, `S3=223..290`, `S4=296..312`. Let `R_m(q)/D(q)` be the counting generating function, with `D(q)=product_{p=214}^{314}(1-q^p)`; let `M_m^(>=1)` denote the least simultaneous quasipolynomial period of all positive-degree coefficients (discard only degree-zero term). Put
`Lambda=814202665467037976682352800`.

**Theorem (new extension, exact finite integer proof):**
```
M_m^(>=1)=Lambda/41=19858601596757023821520800 for every integer 78<=m<=82.
M_83^(>=1)=Lambda.
```
The first case m=78 is a recalled predecessor result; **m=79,80,81,82 and m=83 are the new mathematical cases here.** Thus the 41-factor absence persists for five consecutive thresholds and reappears at 83.

**Counterexample to 41-residue-only classification:** `78 ≡ 119 ≡ 37 (mod 41)`, but the primitive-order-41 numerator vanishes at m=78, whereas `R_119(zeta_41) != 0`. A new independent mod-83 primitive-root witness gives `R_119(4) = 26 (mod 83)`, with `4^41=1 (mod83)` and `4 != 1`. Hence the 41-adic period factor is absent at 78 but present at 119. In particular it is false that this coefficient-period factor is decided solely by `m mod 41`. The exact phase relation across general m is still open.

## Exact 41-cyclic integer computation

Let `A_m(q)` be the seven-term signed inclusion-exclusion numerator of the **first three overlapping events**, with true simultaneous constraints. Work in
`T=Z[x]/(x^41-1)`; store each residue polynomial as 41 signed integer coefficients indexed by exponent modulo 41. For each nonempty mask `I subset {0,1,2}`, let `U_I=union_{i in I} S_i`. For configurations `a_p>=0 (p in U_I)` satisfying `sum_{p in S_i} a_p < m` for all `i in I`, sum `x^(sum p*a_p)` in T. Multiply by `product_{p in U_I}(1-x^p)`. Alternate signs `(-1)^(|I|+1)` and sum over all 7 masks; this equals `A_m(x)` in T by exact inclusion-exclusion, with no independent-event assumption.

The accompanying `VERIFY_D41_CYCLIC.cpp` implements that finite enumeration by multidimensional unbounded-knapsack DP. The DP state is the vector of selected-event total counts, each in `[0,m-1]`; each item increments the coordinates for events containing it, and shifts the cyclic polynomial by `price mod 41`. The full ring calculation is **exact integer arithmetic** (not a floating approximation or an inference from many finite primes). For `m<=83`, every intermediate cyclic coefficient magnitude is bounded by `7*2^8*m^8 <= 4036107679993161472 < 2^63-1`: each selected event's support has at most 8 coordinates, each contributing fewer than m copies; polynomial expansion has at most `2^8` monomials per configuration, and 7 inclusion-exclusion masks. Optimized and `-fsanitize=undefined` compiled executions agreed for m=78..83.

The exact 41-tuples returned:
```
m   cyclic coefficients of A_m modulo (x^41-1)     conclusion
78  all 41 zero                                     Phi_41 | A_78
79  all 41 zero                                     Phi_41 | A_79
80  all 41 zero                                     Phi_41 | A_80
81  all 41 zero                                     Phi_41 | A_81
82  all 41 zero                                     Phi_41 | A_82
83  nonconstant: coefficient[0]=2, [1]=-1          Phi_41 does not divide A_83
```
For m=78..82, `S3` has 41-multiples 246 and 287, so `B_m(zeta_41)=0` for all m; the `S4` complement-residue lemma gives `C_m(zeta_41)=0` for these five residues `m mod41=37,38,39,40,0`. Therefore `R_m(zeta_41)=A_m(zeta_41)=0` at all primitive 41st roots. The denominator `D` has exactly two 41-divisible prices. Thus the primitive-41 double pole disappears and contributes no positive-degree quasipolynomial term.

For m=83, do **not** infer `R_83` from `A_83` alone: `C_83` need not vanish at this residue. The independent complete five-event Hasse computation at primitive 41st root `4 in F_83` instead gave `R_83(4)=31 (mod83)`, proving nonzero in characteristic zero and hence retention of the 41 double pole.

## Complete-period equality via independent lower witnesses

For each m=79..83, rerun the pinned predecessor `VERIFY_FIRST_DROP.cpp` unmodified in mathematical semantics, applying its exact 19-row order/root/prime table and two-jet truncation. The 18 covering orders are `{32,54,25,49,11,13,17,19,23,29,62,37,41,43,47,59,61,73}`; order 27 is an auxiliary. A nonzero `[t^j]R_m(zeta_d(1+t)) mod p` with `j<=n_d-2` proves a characteristic-zero pole of order at least two and therefore `d|M_m^(>=1)`. The accompanying CSV gives all 95 independently calculated exact finite-field values for m=79..83.

For m=79..82, all 17 covering orders except 41 retain valid nonzero jets. Their lcm is `Lambda/41`. For m=83, all 18 survive, whose lcm is `Lambda`. Separately enumerate every positive integer order d for which `n_d=#{p in [214,314]:d|p}>=2`; exactly 68 orders occur and their lcm is `Lambda`. The only such order divisible by 41 is d=41, with n_41=2. Removing that pole lowers the universal upper bound to `Lambda/41`, matching the lower-bound witnesses. For 83 the universal upper bound itself matches its lower bound.

Summary of verified numeric results:
```
m=79: 17/18 covering orders survive; missing 41; lcm=19858601596757023821520800
m=80: 17/18 covering orders survive; missing 41; lcm=19858601596757023821520800
m=81: 17/18 covering orders survive; missing 41; lcm=19858601596757023821520800
m=82: 17/18 covering orders survive; missing 41; lcm=19858601596757023821520800
m=83: 18/18 covering orders survive; missing none; lcm=814202665467037976682352800
m=119: finite-field nonzero witness d=41, p=83, primitive root 4, j=0, residue=26
```

## Verification boundary, source and next question

Execution: local `g++ -O3 -std=c++17` and `g++ -O1 -fsanitize=undefined -fno-sanitize-recover=undefined` for cyclic DP; the finite-field jet verifier was compiled using `g++ -O3 -std=c++17`. Integer/cyclotomic calculations are exact; the finite-prime jets supply only **nonzero witnesses**, never characteristic-zero vanishing. The characteristic-zero upper bound for m=79..82 is supplied by the independent exact cyclic integer computation.

This remains an **author-calculated finite theorem with no independent mathematical review**. Frozen scalar observer only; the P000/X6/BRC promotion and the formal shared-control owner lifecycle remain unchanged. The ongoing research question is the dependence of order-41 cancellation on the quotient `floor(m/41)` as well as `m mod41`, in particular whether an exact small-degree quotient recurrence explains the isolated window 78..82 and the counterexample 119.
