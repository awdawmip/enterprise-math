# D25/LIFT — exact cubic-binomial identity and third-digit harmonic lift

2026-10-24 · TASK_RESEARCH portable author proof · **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

Logical research lane: chatgpt-research-hourly-enterprise-math-20260923. The maintenance lane chatgpt-hourly-enterprise-math-20260921 remains separate. Mother D25/LIFT OPEN; immutable scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

## Exact provenance, nonduplication and mathematical novelty

Consume (without recrediting) the [previous cubic-filter mod-p-squared harmonic result](https://github.com/awdawmip/enterprise-math/blob/d1ba02f53b411242a534646df00e625cc52fe723/research_notes/portable_direct/20261024_hourly_d25_cubic_filter_harmonic_lift_full_wz_cancellation_fibre.md) and the distinct [on-hour full original terminal two-jet](https://github.com/awdawmip/enterprise-math/blob/db1621f2d71ebbcc59c03966c9c3e66b1c03a5a0/research_notes/portable_direct/20261024_onhour_d25_full_original_terminal_uniform_padic_two_jet.md). The first gives h_p modulo p, not an all-order exact binomial formula or h_p modulo p²; the second treats the *full original endpoint* and is not re-credited here.

The new result is an exact rational identity **for every positive integer m**, with an integer binomial residue class eliminated by a genuine involution, plus a uniformly proved one-digit-stronger p-adic harmonic input needed for any subsequent fourth-digit original-WZ expansion.

## Theorem A — all-order exact finite identity

For any integer m≥1 let N=6m+1, n=2m, Q=(-27)^m, H_t=Σ_{k=1}^t 1/k, and let

P_r(N)=∏_{k=1}^{3r−1}(1−N/k),     1≤r≤n.

Then the following are **exact equalities in Q**; no primality is assumed:

(A1)  Q−1 = Σ_{r=1}^{n} (−1)^r binom(N,3r).

(A2)  H_n = −3(Q−1)/N + Σ_{r=1}^{n} [1−P_r(N)]/r.

Let e_a(t)=Σ_{1≤i_1<⋯<i_a≤t}1/(i_1⋯i_a), e_0=1. The **exact, finite all-order expansion**, not just an asymptotic expansion, is

(A3)  H_n = −3(Q−1)/N + Σ_{r=1}^{n} (1/r) Σ_{a=1}^{3r−1}(−1)^{a−1}N^a e_a(3r−1).

### Proof

Work in Q[z]/(z²+z+1), hence z³=1. Since (1−z)²=−3z, we have (1−z)^6=−27; consequently (1−z)^N=Q(1−z). For s∈{0,1,2} put A_s=Σ_{0≤j≤N, j≡s (mod3)}(−1)^j binom(N,j). Reducing the binomial expansion modulo z²+z+1 gives

(A_0−A_2)+(A_1−A_2)z = Q−Qz,

so A_0−A_2=Q. The involution j↦N−j preserves the class j≡2 (mod3), preserves binom(N,j), and reverses sign because N is odd. It has no fixed integer since N odd. Therefore A_2=0 **exactly**. The class A_0 includes j=0 with contribution 1 and remaining j=3r, 1≤r≤2m, proving (A1).

For 1≤j<N the exact factorial identity is

(−1)^j binom(N,j)=−(N/j)∏_{k=1}^{j−1}(1−N/k).

Substitute j=3r in (A1), divide by −N/3, add/subtract H_n=Σ1/r, and obtain (A2). Expanding each finite product by elementary symmetric sums gives (A3) exactly. In particular the discarded class is genuinely zero for **this alternating-binomial observer**; no claim is made about its unlabeled individual summands.

## Theorem B — next p-adic digit of the one-third harmonic lift

Let p=6m+1≥13 now be prime and n=(p−1)/3=2m. Let b=q_p(3)=(3^{p−1}−1)/p be the actual integer Fermat quotient. In the p-local ring Z_(p) define the explicit separately labeled depth sums

U_1=Σ_{r=1}^{n} H_{3r−1}/r,

U_2=(1/2)Σ_{r=1}^{n} [H_{3r−1}²−H_{3r−1}^{(2)}]/r,

where H_t^{(2)}=Σ_{k=1}^t 1/k². All denominators are p-units: 3r−1≤p−2 and r<p.

Then **for all such primes**

(B1)  H_n ≡ −3b/2 + p(3b²/8+U_1) + p²(−3b³/16−U_2)    (mod p³),

(B2)  h_p := (H_n+3b/2)/p ≡ 3b²/8+U_1+p(−3b³/16−U_2)    (mod p²).

This lifts the previously proved h_p mod p by one additional digit. The terms U_1 mod p² and U_2 mod p form a sufficient provenance-preserving carrier for this *declared harmonic observer*, not a claimed universal minimal or CM representative.

### Proof

Since p≡1 (mod3), a primitive cubic root z lies in F_p. It has 1−z≠0, and Fermat's theorem gives Q=(-27)^m=(1−z)^{p−1}≡1 (mod p). The exact integer Q²=3^{p−1}=1+pb identifies Q as the unique square root with residue 1. Binomial expansion in Z_(p) gives

(Q−1)/p ≡ b/2−pb²/8+p²b³/16 (mod p³).

In (A2), the products satisfy

P_r(p) ≡ 1−pH_{3r−1}+p²(H_{3r−1}²−H_{3r−1}^{(2)})/2 (mod p³).

Consequently Σ(1−P_r(p))/r ≡ pU_1−p²U_2 (mod p³). Substitute in (A2) to obtain (B1). Its right side proves H_n+3b/2∈pZ_(p); dividing by p yields (B2).

For comparison with the consumed earlier theorem, U_1≡3b²/8−H_n^{(2)}/3 (mod p), hence (B2) modulo p becomes h_p≡3b²/4−H_n^{(2)}/3 (mod p). This is a strict refinement, not a second claim of the old proof.

## Author-side exact verification

(1) Direct integer binomial evaluation of (A1) **and independently formed exact rational products** in (A2) passed for each integer m=1,...,11, including composite N=6m+1. (2) Exact rational harmonic sums and independently accumulated U_1/U_2 passed (B1/B2) for all 24 primes p≡1 (mod6), 13≤p≤241. (3) A separate modular-inverse recurrence modulo p³ compared h_p with (B2) for the following primes:

| p | Actual h_p mod p² | Formula (B2) mod p² | Difference |
|---:|---:|---:|---:|
| 13 | 140 | 140 | 0 |
| 19 | 244 | 244 | 0 |
| 31 | 596 | 596 | 0 |
| 211 | 3949 | 3949 | 0 |
| 1423 | 618126 | 618126 | 0 |
| 5827 | 11813842 | 11813842 | 0 |

All checks use exact integers/rational fractions/prime-power modular inverses, never floating point. These are **author regressions**; the generality of Theorems A–B follows from the exact algebraic proof, not the finite tests. No native D25 CM benchmark, independent mathematical review or formal proof-checker run is claimed.

## BRC information boundary and durable successor

BRC COMPOSE_APPLIED: retain residue-class binomial ports until the sign-reversing involution shows the entire class-2 contribution vanishes for the *specified* quotient; only then eliminate that port. Retain U_1 and U_2 with their depth, residue and precision semantics. Cubic-root algebra is an external auxiliary finite-field proof device, not a native two-dimensional plane or a change to P000's X6 spatial premises.

This theorem supplies h_p modulo p² for a *future* fourth-digit original WZ computation. Such a computation still needs the **separate original old-edge and all four labeled new-tail terms one p-adic layer deeper**; no complete WZ fourth digit is claimed. More importantly, parent D25/LIFT still lacks an authenticated same-prime/same-primitive-class CM/divided-power representative, fixed H0/B0 coefficients, [X]U mod p² or κ observer, true semilinear map direction and source-derived normalization c_p, and the original terminal comparison. Native experiment: NOT_RUN. The on-hour full-terminal two-jet is consumed rather than repeated.

Do not re-derive the cubic-binomial involution or the prior h_p mod p lemma, rescan old cancellation primes, or replace the original CM class by the auxiliary conductor-3 character. Formal state: **portable GitHub author mathematics only, UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**; no Researcher CLAIM/run/Result/review or native Source execution authority follows from this file. The frozen scientific Source pin remains c47e13e4aba0e006366f989d6334d443f6333ae3.
