# D25/LIFT — exact two-source endpoint cancellation through p³, with the p⁴ defect

Date: 2026-10-28, Research onhour logical lane chatgpt-research-onhour-enterprise-math-20260923.
Status: AUTHOR-SIDE / EXACT ALGEBRAIC IDENTITY / 13 EXECUTED EXACT TESTS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_EXECUTED.

## 0. Scope and consumed frontier

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Last known publication: TP2-B6F4FC938FF94941C1B7.
Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).
Reference: preceding author-side original-216 rational-Gosper proof, Enterprise Math commit c7f79d39ca57cc242320915f6d92ae244492b5d4, at research_notes/portable_direct/20261028_onhour_d25_original216_gosper_pole_endpoint.md. It proved the exact rational identity (C2) and only stated an endpoint cancellation modulo p; this note sharpens that endpoint calculation, does not rerun the Gosper search, and corrects the weaker diagnostic. Earlier D24/CM0, original valuation bands and reflective tail laws are consumed, not recredited.

Define the original scalar external arithmetic observer without changing its weight or endpoint:

\[
t_n=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},\qquad
W_N=\sum_{n=0}^{N-1}(6n+1)t_n.
\]

The symbol n is an external integer summation index and not a native X6 coordinate. The original H0/B0 divided-power benchmark is a different, still-unexecuted native object.

## 1. Exact all-integer endpoint identity

Let \(g(n)=66n^2+113n+49\). For every integer \(N\ge1\) over the rationals, define

\[
J_N:=\sum_{n=0}^{N-2}\frac{g(n)t_n}{9(n+1)^3},
\]
where the sum is empty when N=1. Then

\[
\boxed{W_N=J_N-4+(11-6N)t_{N-1}.}\tag{E1}
\]

**Proof.** Consume the exact, previously proved single-index identity

\[
W_N=(4-12N)t_N-4+
\sum_{n=0}^{N-1}\frac{g(n)t_n}{9(n+1)^3}.
\]

Use the exact original coefficient ratio

\[
\frac{t_N}{t_{N-1}}
=\frac{(2N-1)(3N-2)(3N-1)}{36N^3}.
\]

Put \(D_N=(2N-1)(3N-2)(3N-1)\) and \(g(N-1)=66N^2-19N+2\). Polynomial expansion gives the exact integer identity

\[
(4-12N)D_N+4g(N-1)=-36N^3(6N-11).
\]

Consequently the two previously separate source ports obey, *as rational numbers*,

\[
(4-12N)t_N+\frac{g(N-1)t_{N-1}}{9N^3}
=(11-6N)t_{N-1}.
\]

Substitute into the previous identity. No p-local division or modular cancellation was assumed. QED.

## 2. All-prime valuation and sharp next digit

Let p≥5 be prime. The denominator 216 is a p-adic unit. Lucas congruences and Fermat reduction yield

\[
t_p=\binom{2p}{p}^2\binom{3p}{p}216^{-p}
\equiv12/216=1/18\pmod p.
\]

Using the same exact recurrence, with \(D_p\equiv-2\pmod p\),

\[
\frac{t_{p-1}}{p^3}=\frac{36t_p}{D_p}\equiv-1\pmod p.
\]

Thus \(\nu_p(t_{p-1})=3\) exactly, and the merged endpoint in (E1) satisfies

\[
\boxed{(11-6p)t_{p-1}\equiv0\pmod{p^3},}\tag{E2}
\]

\[
\boxed{(11-6p)t_{p-1}\equiv-11p^3\pmod{p^4}.}\tag{E3}
\]

In particular, with the **unit-denominator, nonsingular** interior observer

\[
J_p=\sum_{n=0}^{p-2}\frac{66n^2+113n+49}{9(n+1)^3}
\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},
\]

the original weighted sum obeys

\[
\boxed{W_p\equiv J_p-4\pmod{p^3}}\tag{E4}
\]

and the next-digit relation

\[
\boxed{W_p\equiv J_p-4-11p^3\pmod{p^4}.}\tag{E5}
\]

The previous source's two upper-boundary ports were only *claimed* to cancel modulo p; they in fact merge into a term of valuation exactly 3 for p≠11 and valuation at least 4 for p=11. The separate sources still matter for p⁴ and for native provenance, but the original p³ target has no exceptional p-denominator summand after this exact pairing.

For frozen target primes \(p\equiv13,19\pmod{24}\), the original still-unproved LIFT is **equivalent** to

\[
\boxed{J_p\stackrel?{\equiv}p+4\pmod{p^3}.}\tag{E6}
\]

This is a target-preserving rewrite, not a universal proof of E6.

## 3. Executed independent exact certificate

Program: research_notes/portable_direct/d25_original216_p4_endpoint_cancel_guard_20261028.py, standard library only. It independently builds the original integer-binomial coefficients and the forward hypergeometric recurrence through n=p−2; checks every coefficient and the rational exact identity modulo p⁴; verifies the p³ valuation and nonunit-denominator cross multiplication for t_p; and verifies (E2)–(E5) at each of 13 primes 5,7,11,13,19,31,37,43,61,67,73,211,373.

Executed output:

PASS_D25_ORIGINAL216_ENDPOINT_P4_EXACT_BOUNDARY 13 primes

For p=373, \(p^3=51895117\) and \(p^4=19356878641\). Independently computed:

\[
W_{373}\equiv11832087049,\quad
J_{373}\equiv12402933340,\quad
(11-6p)t_{p-1}\equiv18786032354
\pmod{p^4}.
\]

Modulo p³, \(W_{373}=373\) and \(J_{373}=377=p+4\), exactly consistent with E4; the p⁴ endpoint equals \(-11p^3\) as E3 requires. These finite checks validate implementation, not E6 over all target primes.

## 4. BRC, source and next frontier

BRC resolution: COMPOSE_APPLIED. The paired boundary uses both original rational source ports, the integer n, signed 6n+1 weight, valuation of t_{p-1}, modulus/precision and the future observer W. Their sum may be quotiented away at p³ because the precise factorization (E1) proves that quotient safe for this declared observer and horizon. At p⁴ the repair coordinate \(-11p^3\) must be retained. This does not provide an observer-preserving quotient to H0/B0, native X6/Heartbeat, actual Frobenius, signed odd Green/Hesse, kappa or Delta−R.

Scientific next unit: seek a character-sum or nonlocal hypergeometric evaluation of the **nonsingular original J_p** modulo p³ for p≡13,19 (mod24), proving E6 or producing a genuine counterexample; do not repeat low-degree Gosper work and do not promote an auxiliary evaluation to native evidence.

Native highest priority remains awdawmip/enterprise-math#1559: same-original-class H0/B0 divided-power [X]U mod 139129 at p=373, actual module rank, semilinear Frobenius direction/eta, full signed odd Green/Hesse, same-definition kappa and Delta_p−R_p, reproducible raw code/inputs and lawful independent review. Verified issue was OPEN, unassigned, NATIVE_NOT_EXECUTED. This proof is not that experiment.

Authority/recovery: authenticated Site status 0.6.11 reports research_authority_granted=false and write_relay_enabled=false; five native jobs occupied the five-job active quota in this run. Original bridge recovery #6575 is only an ACTIVE session pointer with source_authority_verified=false, no own winning claims or runs, a preserved neutral staging manifest and has_more=false *at that historical read*. Original dispatch #6576 ended FAILED/TimeoutExpired. No new claim/open/dispatch/replay/Source checkpoint/Result/review was performed, and no maintenance conversation identity was used. Existing old staging remains independent. This is author-side evidence, not accepted Source progress.

Last verified D25/LIFT/JT2 frontier remains OPEN, frozen scientific Source pin and P000 unchanged. Research lane identity is chatgpt-research-onhour-enterprise-math-20260923; no scheduler/settings mutation.
