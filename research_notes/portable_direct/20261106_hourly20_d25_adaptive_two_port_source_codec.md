# D25 — an optimal adaptive two-port first-jet source codec

Date: 2026-11-06. Lane: TASK_RESEARCH author-side portable mathematical result; logical lane label `chatgpt-research-hourly-enterprise-math-20260923` (configured, not a platform attestation). Maintenance lane `chatgpt-hourly-enterprise-math-20260921` not used. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Status: AUTHOR-DERIVED PROOF / EXACT LOCAL VERIFICATION / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.

## 1. Observable and exact statement

For a prime `p=6m+1>=7`, put `s=(2m,3m,4m)` and let
`U_j(x)=(-1/2)^j ∏_{i=1}^3 binom(s_i+x_i,j)` for `0<=j<p`; `F_p(x)=Σ_{j=0}^{p-1}(6j+1)U_j(x)`. All derivatives below are evaluated at `x=0`, and the first-order scalars take values in `F_p`. The `U_j` are polynomials with `j!` invertible modulo `p`.

Let `T=∇F_p(0)`, `g_j=∇U_j(0)`, and for any source perturbation `δ∈F_p^3` define its first-digit responses
`A(δ)=(F_p(p(v+δ))-F_p(pv))/p mod p`,
`P_j(δ)=(U_j(p(v+δ))-U_j(pv))/p mod p` (any fixed integral `p`-adic lift `v`).
Then `A(δ)=T·δ` and `P_j(δ)=g_j·δ`, independently of `v`.

**Theorem (adaptive minimal source codec).** Whenever `T≠0`, there exists a pair `1<=a<b<=3` such that
`δ ↦ (A(δ),P_a(δ),P_b(δ))`
is an `F_p`-linear bijection of `F_p^3`. It is constructive: calculate the following exact determinants in the listed order and take the first nonzero one,

```
d12 = (  8*T1 -   27*T2 +   20*T3) /     62208,
d13 = (245*T1 -  810*T2 +  590*T3) /   3779136,
d23 = (4480*T1 -14175*T2 +10000*T3) / 725594112    (mod p).
```

These denominators are units for `p>=7`. Invert the `3×3` matrix with rows `T,g_a,g_b` to recover `δ`; then every other labelled first-jet port `g_j·δ` is computable, in particular for all `j<p`. For arbitrary source perturbations, three `F_p` scalars are necessary (cardinality `p^3>p^2`). Thus the codec uses the **minimum number of first-digit scalar outputs**, including the existing aggregate weighted scalar.

If `T=0`, the three labelled ports `(P_1,P_2,P_3)` still recover `δ` exactly and are again optimal among scalar first-digit outputs.

This is a source-preserving **first-order** codec for the specified source parameters and observers; higher-order jets and original native H0/B0 obligations retain their own separate evidence.

## 2. Proof with rational certificate

Since `6m+1=p`, the three base parameters reduce to `(-1/3,-1/2,-2/3)` in `F_p`. Direct polynomial differentiation for `j=1,2,3` gives the rational matrix `G=(g1;g2;g3)`:

```
[-1/6,        -1/9,         -1/12     ]
[-25/576,     -5/162,       -7/288    ]
[-325/23328,  -805/78732,   -385/46656]
```

Exact rational calculation gives

`det G = -5 / (2^12 * 3^11) = -5/725594112 ≠ 0 (mod p)`,

for every prime `p>=7`. Direct cross products, without numerical fitting, give

```
g1×g2 = (8,-27,20)/62208
g1×g3 = (245,-810,590)/3779136
g2×g3 = (4480,-14175,10000)/725594112.
```

The three cross products are linearly independent because `G` is invertible. Therefore any nonzero `T` has a nonzero dot product with at least one, and the corresponding `3×3` observation matrix is invertible. Polynomial Taylor expansion mod `p²` proves the declared response identities. The field-cardinality argument proves optimality. The same invertibility of `G` proves the `T=0` clause. QED.

## 3. Exceptional-source repair and exact arithmetic

The previous result `∇U1×∇U2=(8,-27,20)/62208` showed a two-port defect at `p=109`. Here the complete remedy is explicit: `T=(50,2,59)`, and `(d12,d13,d23)=(0,77,64) mod 109`. Thus the ordered selection chooses ports `(1,3)`. For `δ=(8,-27,20)`, direct 109-term evaluation modulo `109²` gives the three normalized responses `(A,P1,P3)=(0,0,104)`, from which the inverse matrix returns `(8,82,20)` modulo 109.

Additional direct complete-sum tests of nontrivial perturbations, each using independent polynomial recurrence modulo `p²`, passed at `p=7,13,19,79,211,229,373,1093`. For `p=373` and `δ=(8,-27,20)`, the responses `(10,0,0)` recover `(8,346,20)`. These tests do not substitute for the rational proof.

A finite exhaustive **prime scan** over all 330 primes `p<=5000, p≡1 (mod 6)` yielded `T≠0` for all 330; lexicographic pair selection used `(1,2)` for 329 primes and `(1,3)` for `p=109`. Pair-singular primes in this range: `d12=0` only for 109; `d13=0` none; `d23=0` for 7,79. The theorem itself does not rely on this finite census or assume universal nonvanishing of `T`.

Executed local source in this run: `d25_adaptive_two_port_20261106.py`. It checks the exact rational determinant and cross products, all 330 prime pair tests, and nine direct mod-`p²` recovery certificates, with no floating point.

## 4. Meaning for BRC and active objective

Earlier proved single-port quadratic-observer collisions, including the 229-isotropic fiber and 109 two-port rank defect, establish concrete first-/second-digit information loss under specified readouts. This constructive theorem gives a minimal **first-jet repair** by retaining the weighted first digit and adaptively selecting two labelled first-digit ports. The input is the original three-source tangent, not a replacement for the mother congruence. It gives a faithful typed projection for all labelled first-order source changes and any subsequent **linear** first-order observer of those changes.

Mother objective remains `Δ_p-R_p ≡ 0 (mod p)` for `p≡13,19 (mod 24)`; frozen 373 H0/B0, `[X]U mod p²`, Frobenius, `η,κ`, independent review remain open. Next science unit: attempt symbolic finite-sum/WZ reductions of `T1+T3=0` and `k_p+3q_p(2)=0`; separately test whether the minimal first-jet codec supports the compensated `Θ_p` observer without losing required second-order provenance.

## 5. Control provenance

At this run's authenticated service 0.6.11 read: original read requests `em-h20-20261106-1324-d25-task-r13`, `em-h20-20261106-1324-d25-cont-r13` were reconciled by original request ID to `QUEUED`, with historical `EVENT_COLLECTION_IO` progress and no terminal Source packet. Current connection exposes `em_status`, `em_control_result`, `em_control_reconcile` but not callable own `recovery_status` or `session_preserve_staging`; the latter appears only in the advertised contract. Old service staging and legal successor identity are unverified; no new session, claim, open, Result, freeze, review or native checkpoint was made. Existing support: Enterprise Math issue #1558. The portable author evidence is neither accepted mathematics nor Source owner progress.
