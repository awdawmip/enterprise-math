# D25 / SECOND-DIGIT-LIFT — Original terminal central-binomial normalizer and sharp p³ precision witnesses

2026-10-24. TASK_RESEARCH, author-side exact algebra plus local finite certificates; **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NATIVE_BENCHMARK_NOT_RUN**. No native Researcher claim, run, checkpoint, freeze, Result, independent review, or CM/divided-power admission is represented by this note.

**Mother question:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. **Frozen mathematical Source pin:** c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Provenance: original on-hour author lane chatgpt-research-onhour-enterprise-math-20260923; **not** CONTROL_PLANE_MAINTENANCE chatgpt-hourly-enterprise-math-20260921 and not the distinct hourly Researcher. Do not import three old UR staging objects into D25.

## Original object and strict inherited dependencies

For m>=1 set p=6m+1, and retain the exact original source terms

$$
A_m=\frac{(6m)!}{3^{6m}((2m)!)^3},\qquad R_{m,0}=1,\qquad
\frac{R_{m,n+1}}{R_{m,n}}=
\frac{(4m+2n+1)(3n+1)(3n+2)}
{36(n+1)(2m+n+1)(4m+n+1)},
$$

$$
S_m=A_m\sum_{n=0}^{4m}(6n+2p-1)R_{m,n}.
$$

Inherited, not re-credited: full-original third-digit two-jet and p-divisibility in
research_notes/portable_direct/20261024_onhour_d25_full_original_terminal_uniform_padic_two_jet.md
@ db1621f2d71ebbcc59c03966c9c3e66b1c03a5a0; the fixed-p five-port WZ and original two-seam Gosper certificates; all 575 previously checked target primes in p mod24={13,19}; and the distinct other-author cubic-binomial harmonic lift in
research_notes/portable_direct/20261024_hourly_d25_exact_cubic_binomial_harmonic_all_order_lift.md
@ 74149f00837573d26541e1a31dff5f30ca090b6d.
The original native benchmark and SOURCE-specified CM representative are still not provided by these author computations.

## Theorem A — an exact Q-normalizer with no prime assumption

Set B_m=binom(4m,2m). For **every integer m>=1**, not assuming p prime,

$$
\boxed{\frac{A_m}{B_m}
=\frac{1}{3^{p-1}}\prod_{j=1}^{2m}\left(1-\frac pj\right).}\tag{A}
$$

**Proof:** Direct factorial cancellation gives

$$
\frac{A_m}{B_m}
=\frac{(6m)!}{3^{6m}(2m)!(4m)!}
=\frac{\prod_{j=1}^{2m}(p-j)}{3^{p-1}(2m)!}.
$$

Since 2m is even, factoring (-j) from each factor produces (A) with positive sign. This equality is exact in Q, contains all the original A_m normalization, and has no unstated modular approximation.

If p=6m+1 is prime, all j<=2m are p-units. With the **integer** Fermat quotient b=q_p(3)=(3^{p-1}-1)/p and H_{2m}=sum_(j=1)^(2m)1/j, expanding the *exact finite product* proves for every such prime

$$
\boxed{\frac{A_m}{B_m}\equiv
1-p\{b+H_{2m}\}\pmod{p^2}.}\tag{B}
$$

Now **consume, without re-proving/re-crediting**, the separate hourly author's all-prime harmonic theorem H_{2m}≡-3b/2 (mod p). Combining it with (B) yields the narrower composed author theorem

$$
\boxed{A_m\equiv B_m\left(1+\frac p2b\right)\pmod{p^2}.}\tag{C}
$$

The prior harmonic theorem is source-attributed and itself unreviewed; it is a transparent dependency of (C), while (A)–(B) do not depend on it.

## Exact interface to the open original two digits

Use the previously defined **original** J_0(m),J_1(m), including the n=m and n=2m seam, and the inherited source-faithful terminal relation

$$
S_m\equiv pA_m\{J_0+pJ_1\}\pmod{p^3}.
$$

Define q=q_p(2)=(2^{p-1}-1)/p. Combining (C) with the exact identity
(4/3)^{p-1}=(1+pq)^2/(1+pb), the still-open original target is equivalent **given the inherited two-jet and harmonic theorem** to

$$
\boxed{
B_m\bigl[J_0+p(J_1+\tfrac12 bJ_0)\bigr]
\stackrel{?}{\equiv}
1+p(2q-b)\pmod{p^2}.}\tag{D}
$$

Thus the smallest *unproved* first-digit obligation can be typed as

$$
\boxed{B_mJ_0\stackrel{?}{\equiv}1\pmod p,}\tag{E}
$$

followed by the genuine second normalized digit in (D), with the original CM/divided-power representative and native benchmark remaining separate. Equations (A)–(D) do **not** prove either (E) uniformly or the entire original supercongruence.

**BRC COMPOSE_APPLIED / REUSE_APPLIED:** retain original source n, exact signed rational terms, seam labels and p-adic valuation/unit jets until applying the declared S_m/p mod p² observer. Moving from factorial normalization A_m to B_m is justified only by the exact identity (A) and its stated precision; no blanket signed-mass cancellation, auxiliary CM conductor substitution, or native X6 dynamics is asserted. P000's six native spatial axes plus separate time are unchanged.

## A genuine negative result: original target cannot universally strengthen to p⁴

The **unchanged** source endpoint at p=13 (m=2) has the exact rational value

$$
S_2=\frac{12854999453611128788975}{7772129990182032113664}.
$$

Independent direct Fraction accumulation of all nine original terms (n=0,...,8) and unit-preserving modular reduction yields

$$
S_2\equiv19448,\quad
13(4/3)^{12}\equiv21645\pmod{13^4=28561},
$$

hence

$$
\boxed{S_2-13(4/3)^{12}
\equiv 12\cdot13^3\not\equiv0\pmod{13^4}.}\tag{F13}
$$

For the other hard-target class p=19 (m=3), the original exact sum is

$$
S_3=\frac{1274954291994799670874173419390525}
{770837094750179348605289078194176},
$$

and

$$
\boxed{S_3-19(4/3)^{18}
\equiv8\cdot19^3\not\equiv0\pmod{19^4}.}\tag{F19}
$$

These are **strict fully exact finite counterexamples to a universal p⁴ upgrade**, not to the original p³ target. They hold separately in both required residue classes; no extension to all primes or a proof of universal exact valuation 3 is claimed.

## Additional finite exact evidence beyond the inherited 575 target primes

A new local C++17 exact modular program independently constructs the **original unmodified terms** with two representations: (i) p-free factorial products and explicit p-adic exponents; (ii) the original recurrence with per-step p-adic exponent stripping and modular inverses. All products are integer arithmetic, using unsigned 128-bit multiplication for the modular products, and no floating point. The temporary prime power is p^4 (for p<=20000 it fits an unsigned 64-bit modulus), retaining the third residual digit.

For **all 1124 primes p<=20000 satisfying p≡1 mod6**, each reconstructed original source endpoint agrees between both arithmetic paths. Exactly **549 newly tested primes** belong to the formerly untested classes p≡1 or 7 mod24; the other 575 are the previously covered target classes and are recorded as regression, not novel prime coverage. The class counts are:

| p mod 24 | 1 | 7 | 13 | 19 |
| --- | ---: | ---: | ---: | ---: |
| exact prime count | 267 | 282 | 288 | 287 |

All **1124 finite tests** satisfy S_m−p(4/3)^{p−1}≡0 (mod p³), and all have a **nonzero** third residual coefficient (S_m−target)/p³ mod p. Finite observation only; no all-prime extension beyond the frozen target is established, and the 575 target tests are not represented as first-time tests. Sample exact residual coefficients: p=7:5; p=13:12; p=19:8; p=31:24; p=37:19; p=211:89. Direct Python Fraction checks on these six independently verify the coefficients.

**Program persisted separately:**
research_notes/portable_direct/20261024_onhour_d25_all_prime_p4_20k_original_check.cpp.
New normalization-specific Python Fraction checker:
research_notes/portable_direct/20261024_onhour_d25_central_binomial_normalization_check.py.
The latter independently verifies (A) for integer m=1,...,11 including composite 6m+1, checks (B)–(D) and the inherited J0/J1 composition for 25 primes p<=241 in all four modulo-24 classes. It treats observed (E) as finite regression, not universal proof. Complete 1124-row CSV was generated locally and retained as a conversation artifact, **not claimed Source-published**. Source code is available as GitHub author evidence and is not Source's native benchmark.

## Continuation / not-done / actual control scope

- Completed author mathematics: exact identity (A), all-prime (B), declared-dependency (C)–(D), and explicit p⁴ disproof witnesses (F13), (F19). Completed finite computation: 549 new non-target primes; 1124 total p³/p⁴ reads; no p⁴ coincidences in this finite range.
- Do not re-do: D24 accepted unit reciprocity; inherited WZ/LOW/HIGH and full-original two-jet; 575 old target-prime checks; other-author cubic harmonic proof; already completed author finite integer checks.
- Smallest genuinely **open** mathematics: prove or rigorously falsify B_m J0≡1 (mod p) for target classes using source-specific exact LOW/HIGH/CM data, then discharge the second normalized digit (D) and its CM/divided-power representative. Do not replace the original native benchmark input, semilinear direction or independent review with Python/C++ tests.
- Current Sites gateway 0.6.11 is read-only for this subject (research_authority_granted=false; executor_binding_configured=false). Read of the original failed 2026-10-07 session start request via control_result returned CONTROL_REQUEST_NOT_FOUND in this client; the historical #1539 support issue remains OPEN. No request replay, alternate identity, borrowed maintenance session, source claim/open/run, Source checkpoint, Result/freeze or review was performed. These portable GitHub files do not create role-based execution authority.
- Preserve the source pin, task publication, scheduler, phase, enabled and notification behavior unchanged. Source repair remains the responsibility of Enterprise Math issue #1539. Resume actual canonical continuation only with lawful subject/session authorization and current exact receipts; old UR staging remains independent. Parent D25/LIFT is still OPEN.
