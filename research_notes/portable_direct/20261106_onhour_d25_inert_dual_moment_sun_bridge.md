# D25 / 216–2304: inert-class zero/weighted two-moment bridge (2026-11-06)

**TASK_RESEARCH / author-side exact algebra + finite exact validation / UNREVIEWED / NOT_ADMITTED.**
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable source `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical Research lane `chatgpt-research-onhour-enterprise-math-20260923` is separate from the maintenance lane; this note does not assert a native claim, run or Result.

## Verifiable external source (CONJECTURE, not theorem)

Zhi-Hong Sun, *Supercongruences involving Apéry-like numbers and binomial coefficients*, AIMS Mathematics 7(2) (2022), pp. 2729–2781, **Conjecture 5.28, printed p. 2758**, DOI https://doi.org/10.3934/math.2022153; original PDF https://www.aimspress.com/aimspress-data/math/2022/2/PDF/math-07-02-153.pdf#page=30 (published online 18 November 2021).

Write `a_k=C(2k,k)^2 C(3k,k)/216^k`, `b_k=C(2k,k)^2 C(4k,2k)/2304^k` and `A_p=sum_(k<p)a_k`, `B_p=sum_(k<p)b_k`. In the source, for p mod24 = 13,17,19,23 respectively, B is conjectured to equal `p^2/(5R24)`, `p^2/(5R24)`, `-p^2/(77R24)`, `-p^2/(77R24)`, while A equals `-7p^2/(5R24)`, `7p^2/(5R24)`, `p^2/(11R24)`, `-p^2/(11R24)`, all modulo p³. The same R24 binomial product cancels. Thus the source **would imply** the uniform inert zero-moment congruence

    H_p := A_p + 7*chi_p*B_p == 0 (mod p^3),
    chi_p=(p/3), p mod 24 in {13,17,19,23}.                         (S)

This extraction is an algebraic consequence of a *still conjectural* source statement; do not claim (S) is universally proved. Frozen target p mod24=13 or 19 has chi_p=+1.

## Exact new dual-moment bridge (PROVED)

Define `D_A=sum_(k<p)k*a_k`, `D_B=sum_(k<p)k*b_k`,
`W_p=A_p+6D_A`, `V_p=B_p+8D_B`, and
`G_p=6D_A-8D_B-(1+7chi_p)B_p`. Then in Q for **any p>3**, by expansion,

    W_p - V_p = H_p + G_p.                                       (1)

The two independent (unweighted and weighted) observer residuals now give a precise two-part certificate. If (S) were established, proving G_p=0 mod p³ would suffice for original W-V; G is not presumed to vanish.

Consume the previous exact *author-side, not admitted* CM-cusp triangular transport `a_n=sum_(k<=floor(2n/3))b_k*T[n,k]` from `20261105_onhour_d25_cusp_integral_terminating_transport.md` and its `20261105_onhour_d25_signed_two_coset_weighted_k_recurrence.md`. Put `h=(p-1)/2`, `K=floor(2(p-1)/3)`, `J=floor((3p-1)/4)`; `Z_k(L)=sum_(n<=L)b_k T[n,k]`; `S_k(L)=sum_(n<=L)(6n+1)b_k T[n,k]`. Then the exact triangular identity and `v_p(b_k)=floor(4k/p)` for 0<=k<p prove

    H_p = sum_(k=0)^K [Z_k(p-1)+7chi_p*b_k]
          + 7chi_p * sum_(k=K+1)^J b_k      (mod p^3),           (2)

    W_p - V_h = sum_(k=0)^K [S_k(p-1)-(8k+1)b_k*1_(k<=h)]        (exact Q). (3)

The separately sourced 2304 full-vs-half congruence `V_p=V_h mod p³` converts (3) to W-V mod p³. Both signed transport channels and their boundaries remain retained. **Do not drop the 2304 overhang `K<k<=J`**, e.g. p=13: (K,J)=(8,9); p=19: (12,14). The source's K/J are original model cutoff positions; the auxiliary two-coordinate rational readout is not a P000-native 3D construction.

## Executed exact experiments / strength

Two independently implemented arithmetic routes: p³ modular hypergeometric term recurrences (division only by p-unit factors for k<p), and raw `math.comb` numerator products for p in {13,17,19,23,37,43,139,373}. Exhaust all **616 primes <10000** with p mod24 in {13:157,17:152,19:155,23:152}. Exact checks of H_p, G_p, W_p-V_p modulo p³ and identity (1) have zero failures. Thus **312 frozen-class primes** are included, but universal congruence and original native p373 H0/B0 are **NOT proved/executed**.

Examples (p, p³, A, B, W=V): (13,2197,1859,676,13), (17,4913,867,4335,4896), (19,6859,2888,2527,19), (23,12167,3174,7406,12144), (373,51895117,9878159,28243187,373). Each example has H=G=0 modulo p³. Actual p⁴ checks show H_p/p³ mod p is (4,2,11,13) at p=13,17,19,23, respectively; the stronger uniform p⁴ extension is disproved. Outside the Sun hypotheses, p=5 has H=84 mod125 and p=7 has H=165 mod343. This negative scope does not affect the p³ target.

Machine summary: `20261106_onhour_d25_inert_dual_moment_execution.json`; standalone executable `d25_inert_dual_moment_20261106.py`. Full 616-row JSON is included in local run evidence; its SHA256 `4990e3f21571b18629b5a4d894e1859fa03482bf6ee16c8a3e8dd06564a8705e`.

## Next smallest actual science and native frontier

Try a **joint finite k-telescoper** over the already established `Z,S` recurrences, maintaining h/K/J signed boundaries. First distinguish p=13/19 overhang contributions, then prove H and G or an equivalent direct total without assuming the source conjecture. Do not repeat all-prime scans to hide the missing uniform certificate.

Native fixed original-class p373 H0/B0 divided-power `[X]U mod139129`, true module rank, semilinear Frobenius/eta, kappa, odd signed Green/Hesse observer and independent replication remain **NOT_RUN / PENDING_OWNER**, under GitHub issue #1559. No surrogate ordinary scalar counts as completion. Previous Source request `onhour11-20261105-2200-d25-cusp-source-cont` was verified SUCCEEDED with `execution_authorized=false`; the current Source `onhour11-20261106-0001-d25-continuation-read` must be consumed exactly, not resent. Source read projection does not confer claim/session capability. Retain all frozen prior Source contributor history and independent review/admission obligations.
