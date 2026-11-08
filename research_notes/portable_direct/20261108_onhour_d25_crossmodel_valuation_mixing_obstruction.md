# D25 / Original 216–2304 valuation-grade comparison: a source-mixing obstruction

Date: 2026-11-08 Asia/Hong_Kong. TASK_RESEARCH author-side; **exact grade-2 identity PROVED, exact p=13 restricted-transfer counterexample PROVED, 301-prime exact computation executed, UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Logical lane chatgpt-research-onhour-enterprise-math-20260923; *not* maintenance chatgpt-hourly-enterprise-math-20260921.

## Original objects and new exact second-model band identity

For primes p>3 compare the unchanged original weighted truncated sums

W_p = sum(n=0..p-1) (6n+1) (2n)!(3n)! / [(n!)^5 216^n],

V_p = sum(n=0..p-1) (8n+1) (4n)! / [(n!)^4 2304^n].

Guo–Zudilin, A q-microscope for supercongruences (https://arxiv.org/abs/1803.01830, Theorem 1.1), proves V_p = p*(-3/p) (mod p^3), all p>3. Our previous direct 216 result verified the corresponding W_p congruence through 10000 as a finite **conjectural** pattern, not a proof. The frozen mother requires W_p=p mod p^3 for p mod24=13,19, equivalently original Delta_p-R_p=0 mod p.

Define original-index valuation grades e_W(n)=floor(2n/p)+floor(3n/p), e_V(n)=floor(4n/p). The scalar weights may raise actual valuation; the grades denote coefficient provenance, *not* the valuation of every weighted summand. The W model has e=2 on ceil(p/2)..floor((2p-1)/3). The V model has e=2 on N=(p+1)/2 through L=floor((3p-1)/4). Other grade >=3 terms vanish mod p^3.

**Theorem (all p>3, exact modulo p):** the V grade-2 aggregate divided by p^2 equals

T_V(p) = 2 sum(n=N..L) (8n+1)*(4n-2p)! / [(n!)^4 2304^n] (mod p).

Proof: for 2p<=4n<3p, there are exactly two p factors (p,2p) in (4n)!. After dividing by p^2, the nonzero factors comprise two complete Wilson blocks and (4n-2p)!; the removed multiples contribute 2, so (4n)!/p^2 = 2*(4n-2p)! mod p. n! and 2304 are p-units. QED.

Writing r=n-N, R=L-N and using Pochhammer symbols yields the exact independent finite hypergeometric readout

T_V(p) = 4/[N!^4 2304^N] * sum(r=0..R) (8r+5)
        * (3/4)_r (1)_r (5/4)_r / [(3/2)_r^3 9^r] (mod p).

Proof: the starting shifted factorial is (4N-2p)!=2!; the ratio of consecutive unweighted terms is
(4r+3)(4r+4)(4r+5)(4r+6)/[2304 (r+3/2)^4]
= (r+3/4)(r+1)(r+5/4)/[9(r+3/2)^3].
The range avoids denominator zeros, giving the displayed exact finite identity. This **does not** prove T_V(p)=0 for every prime.

## Exact observer-compatible diagonal transfer falsifier

Independent original-binomial arithmetic at p=13 produces the source-typed grade 0,1,2 aggregates mod 2197:
W: (780,1937,1690); V: (325,1885,0).
Thus W grade-2 digit = 1690/169=10 mod13, whereas V grade-2 digit =0. V's individual grade-2 digits are (7,0,6), a nontrivial cancellation. It follows rigorously that **no c in F_13^× can map the V grade-2 aggregate to the W grade-2 aggregate by a grade-preserving scalar observer map**. Any diagonal, output-commuting unit-only grade-2 transfer fails at p=13, even though both full totals agree mod p^3. This is a counterexample ONLY to that explicit proposed transfer mechanism, not to unrestricted Fricke/isogeny/Cartier maps.

Further same-original exact witnesses (all grades are residues mod p^3):
- p=19: W=(5662,4826,3249), V=(6384,494,0); W grade-2 digit 9, V digit 0.
- p=373: W=(28094360,38687933,37008314), V=(45069217,6826273,0); W grade-2 digit 266, V digit 0, p^3=51895117.

For these examples equality of full sums modulo p^3 requires **cross-grade reallocation**: V lower-grade sum minus W lower-grade sum equals the W grade-2 contribution (as V's grade-2 total vanishes). At p=373 the required repair is 266*p^2 mod p^3. This is a BRC observer/provenance distinction: the signed aggregate equality is weaker than equality of each original valuation-grade observer.

An all-prime W=V congruence at p^4 is also false: exact (W-V)/p^3 modp equals 11 at p=13, 6 at p=19 and 114 at p=373 (at p373 W modp^4=11832087049, V=5916043711). These are explicit numeric counterexamples to the *stronger* claimed congruence, not claims about a fourth-digit universal formula.

## Exact executed validation

Standalone standard-library reproducibility file: research_notes/portable_direct/d25_crossmodel_band_transport_check_20261108.py.
It checks **all 301 primes from 5 through 2000**, including **77 frozen target primes**. Independent V e=2 shifted factorial recurrence agrees with original p-free factorial accumulation for all 301. Observed: all 301 have T_V(p)=0; all 301 have W-V=0 mod p^3; all 77 frozen targets have W grade-2 aggregate !=0. Original complete binomial sums independently match both p-free implementations at p=5,11,13,19,37,43,211,373. Universal vanishing and equality remain **FINITE_OBSERVATIONS**, not proved theorems. The previous 1227-prime W scan is consumed, not repeated.

## Research continuation and exact native debt

New portable next question: prove or falsify T_V(p)=0 for all p>3 using the proved terminating 3F2 readout; then construct an actual W/V source-preserving p^3 transformation with explicit lower-grade-to-tail repair (or its first precise counterexample). Do not replace the frozen original mother objective with an all-prime conjecture.

Original mandatory benchmark https://github.com/awdawmip/enterprise-math/issues/1559 remains OPEN/PENDING_OWNER/NOT_EXECUTED: authentic p=373 same-original-class H0/B0 divided-power [X]U mod139129, rank, Frobenius direction/eta, signed Green/Hesse kappa and original Delta-R; source-bound raw data and independent check; then p=19. Neither these scalar computations nor the proven arithmetic band identity are the native experiment.

Source original target_request_id: onhour11-20261106-1400-exact-research-lane-continuation. This turn exact Source status, own checkpoint and old receipt return BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE; operation_sent=false. Local Site diagnostic CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false. Do not replay original request, adopt maintenance lane/session or claim Source Researcher/claim/run. Missing native capability must be recovered via separate Site-bound backend client/credential and authorized p373 executor; no scheduler state changed.

**Status:** AUTHOR_SIDE_EXACT_FORMULA_PROVED / RESTRICTED_P13_COUNTEREXAMPLE_PROVED / EXACT_301_PRIME_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
