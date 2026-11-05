# D25: exact Puiseux branch-coset cancellation and Frobenius shell sign

2026-11-05 TASK_RESEARCH; task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, scientific source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Author-side proof; UNREVIEWED / NOT_ADMITTED. Depends on the prior exact positive high-CM branch hypergeometric transport published at `research_notes/portable_direct/20261105_onhour_d25_positive_cm_branch_exact_period_transport.md`.

## Exact Puiseux expansion

Use the high real branch J3(u_+(z))=J4(v_+(t(z))) defined in the preceding theorem, with u_+=(1+sqrt(1-z))/2 and v_+=(1+sqrt(1-t))/2. Let x=sqrt(z), and write t=x^3 U(x). The two rational j expansions at the infinite cusp are

G(z)=z^3 J3(u_+(z))=1259712-1469664 z+317844 z^2-702 z^3+O(z^4),
H(t)=t^2 J4(v_+(t))=65536-53248 t+2816 t^2+O(t^3).

The exact algebraic equation is `G(x²)U(x)²=H(x³U(x))`. Solving coefficient-by-coefficient on the positive branch gives

**t(z)=(32 sqrt(3)/243) z^(3/2) [1+(7/12)z-(13 sqrt(3)/243)z^(3/2)+(83/216)z²+O(z^(5/2))].**

The leading coefficient is fixed positively by 65536/1259712. The expressions have been verified by exact symbolic polynomial coefficient matching.

## Noninteger branch cancellation in the gauge

The exact positive gauge from the prior theorem is
`M(z)^2=3 t sqrt(1-t)/[2 z sqrt(1-z) t']`.
Substituting the Puiseux series and taking its positive square root gives

`M(z)^2=1+z/9-(sqrt(3)/81)z^(3/2)+(5/108)z²+O(z^(5/2))`,
`M(z)=1+z/18-(sqrt(3)/162)z^(3/2)+(7/324)z²+O(z^(5/2))`.

Meanwhile for F_B(t)=2F1(1/8,3/8;1;t),

`F_B(t(z))=1+(sqrt(3)/162)z^(3/2)+O(z^(5/2))`.

Therefore the signed half-integer coset cancels *between two separately nonzero contributions*:

`M(z) F_B(t(z))=1+z/18+(7/324)z²+O(z^(5/2))`,

exactly the first three coefficients of `2F1(1/6,1/3;1;z)`. This is a finite formal-Puiseux certificate of the branch mechanism behind the exact analytic transform; it is not based on floating-point approximation.

## Frobenius provenance linked to the previously established upper shell

Let alpha=32 sqrt(3)/243. For primes p>3 with p≡13 or 19 (mod24), the reduction of the leading Puiseux coefficient in F_{p²} satisfies sigma(alpha)=(3/p)alpha, where sigma(x)=x^p. Quadratic reciprocity gives

(2/p)=-1 for both classes;
(3/p)=+1 if p≡13 (mod24), and (3/p)=-1 if p≡19 (mod24).

The previously proved *finite* upper-shell first-unit ratio for the original 216/2304 models was

`A0/B0=4(6/p)=-4(3/p) (mod p)`.

Thus the **same quadratic character** indexing Puiseux leading-branch Frobenius governs the shell sign, with the explicit factor -4:

`A0/B0=-4 sigma(alpha)/alpha (mod p)` (interpreted in F_{p²}, with the ratio in F_p).

This is an exact character-level bridge between two separately sourced observers. It does not itself prove a finite mod p³ transformation or identify native H0/B0 Frobenius; retain the original signed half-endpoint carry/upper shell and independent native p373 benchmark.

## Reproduction and next action

The exact symbolic script `d25_positive_j_puiseux_check_20261105.py` checks the normalized j expansions, Puiseux coefficients, gauge expansion and signed z^(3/2) cancellation. It was executed with all assertions passing.

Next actionable scientific step: use the half-integer exponent coset and the above quadratic character to attempt a finite terminating 216→2304 p-parameter operator/carry formula at p=13 and p=19, without identifying this local Puiseux Frobenius with native crystalline Frobenius. Frozen mother target remains Delta_p-R_p≡0 (mod p) for p≡13,19 (mod24); fixed p373 divided-power [X]U mod139129 and independent replication remain support Issue #1559 pending actual executor.

Research conversation ID `chatgpt-research-onhour-enterprise-math-20260923` is separate from control maintenance. Source CLAIM/run/Result are not asserted.