# S23 conditional AV, n=3: continuous-domain minimax gap at most 4.9×10⁻¹⁰

Date: 2026-11-07. Status: author-side exact constructive proof; independent mathematical review and native formal CLAIM pending.
Scientific input (immutable): `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Continuation: Draft PR #1777, predecessor certified upper bound `593454349/2500000000` at `45bf9db19c873f03e664e1650ac8191d4b2b3f8e`.

## New theorem

Let `a,c` be **arbitrary real numbers** in `[1/2,7/8]`, let `z=(1-a)c`, and let
`P_(a,c)=(a,z,(1-a)(1-c))`, `B_z=(z,1-z)`.
The same hidden parameter pair governs all three conditionally independent observations. Define

`δ₃=inf_{L: {0,1}³→{0,1,2}³ row-stochastic} sup_{a,c∈[1/2,7/8]} TV(P_(a,c)^⊗3, B_z^⊗3 L)`.

Then the explicit rational `4×10` kernel in `VERIFY.py`, with denominator `10^14`, satisfies the **all-real** bound

```text
5211/21952 <= δ₃ <= 8142187516807/34300000000000
                     = 5211/21952 + 49/100000000000
                     = 0.23738156025676384... .
```

Thus the **remaining rigorous minimax interval is at most `49/100000000000 = 4.9×10⁻¹⁰` wide**, improving the preceding `154207/857500000000 ≈ 1.79833236×10⁻⁷` gap by a factor of about `367.0`. The all-real uniform upper itself improves by exactly `6151473/34300000000000` against the previous certificate.

The lower bound is the pre-existing exact two-point fiber theorem: `(a,c)=(1/2,1/2)` and `(5/7,7/8)` both have `z=1/4`; their ternary three-observation total-variation distance is `5211/10976`, while their compressed three-observation laws coincide. The triangle inequality implies half that distance as a lower bound for every fixed kernel. The verifier independently checks this exact distance using ten histogram masses.

## Explicit kernel and the full 8×27 lift

Let `H={(h0,h1,h2)∈ℕ³:h0+h1+h2=3}`, lexicographically ordered as in `VERIFY.py`, and `m(h)=3!/(h0!h1!h2!)`. For input binary words `y` with `k` non-`z` symbols, and ternary ordered words `x` of histogram `h`, put

`L(y,x)=K[k,h]/(10^14 m(h))`.

The exact integer matrix `K` has four rows and ten histogram columns:

```text
[0,0,0,100000000000000,0,0,0,0,0,0]
[0,0,0,0,0,0,1747112991682,0,98252887008318,0]
[121269627318,444444444444,11084232590318,0,22195343701318,12471322964682,16568032896677,31974633557918,10312735866,5130407481459]
[5375704166,0,26622927530,0,26878520682,0,5071818328318,2418691424318,32373716247318,60076896847668]
```

The verifier checks each row sums **exactly** to `10^14`, entries are nonnegative, and `sum_h m(h)=27`. Hence `L` is an admissible parameter-independent stochastic map from all eight ordered binary observations to all 27 ordered ternary outputs. Independent permutation symmetrization (proved in the predecessor) justifies this representation for the present marginal TV minimax. The ten histogram masses with their multiplicities retain the original ordered-output loss.

## Exact continuous Bernstein certificate

Define `p=(a,z,(1-a)(1-c))`; `w_k(z)=binom(3,k)z^(3-k)(1-z)^k` for `k=0,1,2,3`. The ten signed histogram residuals are

`R_h(a,c)=m(h)p0^h0 p1^h1 p2^h2 − Σ_k w_k(z) K[k,h]/10^14`.

Their sum vanishes, therefore `TV(P^⊗3,B^⊗3 L)=E_K(a,c)=Σ_h max(0,R_h(a,c))`.

Each `R_h` has degree at most three in `a` and separately in `c`. Parametrize the box by `u=(a−1/2)/(3/8)`, `v=(c−1/2)/(3/8)`; both lie in `[0,1]`. Express each residual in the tensor product Bernstein basis of bidegree `(3,3)`:

`R_h(u,v)=Σ_{i,j=0}³ β_{hij} B_{i,3}(u) B_{j,3}(v)`.

The control coefficients are obtained by **exact rational inversion** of the four-node Bernstein evaluation matrix at nodes `0,1/3,2/3,1` in each coordinate. `VERIFY.py` checks three further exact non-node interpolation identities.

For any Bernstein block, positivity and partition-of-unity of the Bernstein weights, and convexity of the positive-part map, imply

`E_K(u,v) <= max_{i,j∈{0,1,2,3}} Σ_h max(0, β_{hij})`.

Midpoint de Casteljau subdivision creates exact rational child controls; the algorithm uses only unbounded integers and `Fraction`, with an integer denominator scaling factor eight per split. It begins on the entire unit square, alternates splitting u and v, and accepts a block only if the *exact rational* Bernstein hull is at most

`T=5211/21952+49/100000000000=8142187516807/34300000000000`.

The **executed** verifier passes with **53 bisections, 54 accepted covering blocks, and maximum depth 31**. Its maximum accepted rational hull is

`437891688978256634422345524497297 / 1844674407370955161600000000000000`
`≈ 0.23738156025178633 < T`.

The accepted blocks partition the full unit square including all boundary segments, so the bound applies to **every real lawful parameter pair**. Numerical discovery and approximate LP were used only to find this rational candidate; the certificate above and row normalization prove the theorem without trusting the optimizer. `RUN_EVIDENCE.txt` contains actual complete stdout from the source `VERIFY.py` (Git blob `7a12892c902bc8d668498b74a94e0991fa08700c`), executed in this research turn.

## Scope, provenance, next question

This is a conditional-AV **auxiliary observer** construction and exact deterministic certificate. The BRC-relevant typed branch/provenance information is retained by the 27 ordered outcomes, exact histogram multiplicities, and one shared hidden parameter; the reduction is justified for the declared output marginal TV observer. It does not alter P000 or ACTIVE worldview, and the source pin remains frozen. Transfer to the six-source/ten-label S23 mother `R_beh(k,10)` requires its lawful observer/encoder/decoder bridge.

The mathematical gap is now `4.9×10⁻¹⁰`. Highest-information continuation: determine whether `δ₃=5211/21952` by constructing a rational kernel whose continuum certificate reaches that exact value, or prove a strictly larger finite-support rational dual lower bound. Independently audit this certificate; the research artifact remains unreviewed. Native gateway state and task-list calls in this turn returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false`; formal Owner, CLAIM and Research-Activity-ID remain unconfirmed.
