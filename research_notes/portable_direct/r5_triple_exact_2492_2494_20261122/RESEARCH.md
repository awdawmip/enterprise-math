# R5: first exact three-way period contraction (thresholds 2492–2494)

2026-11-22. **AUTHOR_EXACT_PROOF / FINITE_FIELD_FIRST_JET_CROSSCHECKED / NOT_REVIEWED**. Independent portable scientific research; no CLAIM, RUN, Result, mathematical Review or Foundation adoption.

## Frozen scalar problem and sources

The **unchanged frozen scientific input** is Enterprise Math commit 75d986aa23b68a7ecf9b29dc1006f0e322b35. This is the five-failure-event **scalar partition** observer, not a theorem about native-X6 geometry. Prices are integers p=214,...,314, multiplicities a_p are nonnegative integers, and N=sum p*a_p. Failure E_i(m) occurs when sum of a_p for p in S_i is less than m, where

- S0={214,215,216,217,218}
- S1={214,216,217,218,219,220,221}
- S2={215,216,217,218,219,220,221}
- S3={223,...,290}
- S4={296,...,312}.

Let D(q)=product over p=214..314 of (1-q^p) and F_m(q)=R_m(q)/D(q) enumerate the union of failures, with **signed, joint-event-correct** numerator R_m. M_m(O_m(N)) is the strict least period shared by the coefficient functions of degree at least 2 of [q^N]F_m(q), ignoring terms O_m(N).

Existing characterstic-zero phase proofs, both **NOT_REVIEWED**: primitive-29 and primitive-32 exact all-threshold cancellation in research_notes/portable_direct/r5_allthreshold_29_32_20261122/RESEARCH.md at Enterprise Math commit 74c74c94d7971bdd8594824b734e574f85d43fd2; primitive-43 all-threshold theorem in research_notes/portable_direct/r5_root43_allthreshold_phase_20261122/RESEARCH.md at commit c9329abecc9963667647a2774b351a33c0456b0a. The latter two establish exact root-specific zeros, not mere modular zeros. The denominator pole inventory gives universal L=229746052653717600. The only orders with pole multiplicity at least 3 carrying prime 29, prime 43 or the maximal 2^5 are respectively orders 29,43,32.

## New finite-threshold exact theorem

For each m in {2492,2493,2494},

\[
\boxed{M_m(O_m(N))=\frac{229746052653717600}{29\cdot2\cdot43}=92119507880400.}
\]

The previous paper had proved only the upper bound for these thresholds; **this turn closes the lower bound**.

**Upper bound.** The triples (m mod58,m mod64,m mod43) are respectively (56,60,41), (57,61,42), (0,62,0). These lie in the already proved zero sets {0,54,55,56,57} for 29, {0,60,61,62,63} for 32, and {0,37,38,39,40,41,42} for 43. Each corresponding denominator pole is of order 3. The zero numerator removes precisely its degree-at-least-2 contribution; other primitive orders cannot reinstate the maximal 29/43/2^5 factors. Thus the least period divides L/(29*2*43).

**Lower bound.** An independent exact finite-field first-jet calculation evaluates (R_m, q*dR_m/dq) at primitive roots of orders W={7,9,11,13,16,17,19,23,25,27,29,31,32,37,43}. For each of the three m, every order in W\{29,32,43} has either R_m≠0, or first derivative ≠0 with denominator pole order at least 4. These witnesses are sufficient to retain a pole of order at least 3 and hence a degree-at-least-2 coefficient frequency. A nonzero value after reduction at a primitive dth root in F_p, for p≡1 mod d, certifies characteristic-zero nonvanishing: cyclotomic divisibility in characteristic zero would force zero at every primitive dth root modulo p. The LCM of the 12 surviving d is exactly 92119507880400, including d16 (so the 2^4 contribution survives). The lower and upper bounds agree.

The zero finite-field R values for d29,d32,d43 are **not** used as characteristic-zero proofs; the source characteristic-zero theorems above provide those equalities.

## Independent fast exact calculation

Separate the three disjoint price blocks U={214,...,221}, S3, S4, writing R_m=1-(1-A_m)(1-B_m)(1-C_m). A is the **joint union** of E0,E1,E2; the S3 and S4 events are each individual. Let x=a214, y=a215, u=a216+a217+a218, j=a219+a220+a221. The minimum of their three joint event loads equals

\[
u+x+y+j-\max(x,y,j).
\]

Working over the first-jet ring F_p[epsilon]/(epsilon^2), represent q^p as (w^p, p*w^p). For variables X=q^214,Y=q^215,J=q^r, define P_I as the product of variables in nonempty subset I of {X,Y,J} and

\[
T(X,Y,J;t)=\frac{1}{(1-Xt)(1-Yt)(1-Jt)}
 \sum_{\varnothing\ne I\subseteq\{X,Y,J\}}(-1)^{|I|}
 \frac{P_I t^{|I|}-1}{1-P_I t^{|I|-1}}.
\]

This follows by telescoping the exact-max h-layer difference of three bounded geometric sums. Complete homogeneous sums in u and j use the ordinary three-distinct-base partial fractions h_U(u)=sum_s alpha_s (q^s)^u, h_J(j)=sum_r beta_r(q^r)^j. Thus

\[
\sum_{m\ge1}A_m(q)t^{m-1}
=\frac{D_U(q)}{1-t}
\sum_{s=216}^{218}\sum_{r=219}^{221}
\frac{\alpha_s\beta_r T(q^{214},q^{215},q^r;t)}
 {1-q^s t}.
\]

The individual-event series use D_S(q)/[(1-t)prod_{p in S}(1-q^p t)]. All are formal rational power-series identities with no independence assumption inside U. Each geometric inverse (1-a*t^h)^-1 is evaluated by the exact forward recurrence coefficient[n] += a*coefficient[n-h]. For singleton I where P_I=1 at a tested root, the apparent division by 1-P_I is canceled against the *same exact* factor of D_U **before specialization and differentiation** (essential for d43 and other relevant orders). The accompanying C++17 implementation includes that removable-singularity cancellation. It computes through m2494 in one pass per order, avoiding a 2494^3 joint-event DP.

The source VERIFY_TRIPLE.cpp was compiled and run locally with:

    g++ -std=c++17 -O2 -Wall -Wextra -Werror -fsanitize=undefined \
        -fno-sanitize-recover=all VERIFY_TRIPLE.cpp -o verify_triple
    ./verify_triple > TRIPLE_OUTPUT.csv 2> VERIFY_LOG.txt

All 13 explicit independent (R0,DR0) anchors taken from the earlier **joint-event integer DP** data at commit 74c74c94... passed. The run produced 330 selected m/d rows over 15 primitive orders and 22 thresholds; no sanitizer failure occurred. Original local CSV (331 lines including header) SHA256: 9c324a727497b23bcf79fd8a53a39398bf3dd93e709a0226a048b15220635dc8. Local C++ source SHA256: a2ded3c5ccaa7ea3bfb4a3e0905def34808e9ae321ac77450aca3470b96107a7.

### Exact nonzero witness table

Each entry is (R0,DR0) modulo p at primitive root w; the divisor d has the stated denominator pole order. The three columns correspond to m2492,2493,2494.

|d|p|w|pole|2492|2493|2494|
|--:|--:|--:|--:|--|--|--|
|7|10039|5580|14|(0,6182)|(0,5961)|(0,3352)|
|9|10009|5783|11|(0,6658)|(0,3145)|(0,115)|
|11|10099|792|9|(3786,1082)|(0,987)|(0,8319)|
|13|10037|5992|8|(0,2111)|(0,9855)|(0,4373)|
|16|10177|1750|6|(132,2757)|(5899,275)|(794,1453)|
|17|10099|4343|6|(4065,996)|(1448,7806)|(3492,2882)|
|19|10223|2301|5|(4003,206)|(367,354)|(3989,4108)|
|23|10259|4778|4|(4750,2961)|(5896,530)|(4326,3750)|
|25|10151|7216|4|(8633,8464)|(3603,9653)|(8626,827)|
|27|10099|2017|4|(0,1724)|(0,2088)|(0,61)|
|31|10169|1836|4|(0,8714)|(0,6411)|(0,666)|
|37|10139|1802|3|(7517,2888)|(8387,274)|(7971,7318)|

At d=29,32,43 the zero jets have R0=0 at all three tested thresholds, consistently with the separately proved characteristic-zero cancellation theorems.

## New exact congruence-density lemma

The **triple cancellation** classes have density 91/79808 and exact modulus 79808. The 29-zero set modulo 58 has three even and two odd residues; the 32-zero set modulo 64 has the same split. Because gcd(58,64)=2, there are 3*3+2*2=13 compatible residue pairs modulo lcm(58,64)=1856. Since gcd(1856,43)=1, all seven 43-zero phases combine, giving 13*7=91 residue classes modulo 79808. The first positive member is 2492, immediately followed by 2493,2494. This counts the three root cancellations, **not** full-period equality on all 91 classes.

## Provenance, validation scope, continuation

Model frozen at 75d986aa23b68a7ecf9b29dc1006f0e322b35a15; arithmetic exact modulo explicitly listed small primes; characteristic-zero cancellations imported from the two source author proofs; lower witnesses independently computed via a different rational GF algorithm and regression-matched to 13 published original-DP outputs. All author work: **NOT_REVIEWED**, no Lean, no formal Result, no authority change. Signed event cancellations should not be reinterpreted as positive-only BRC mass; P000 and ACTIVE worldview are preserved.

Next: extend the survivor classification to additional thresholds in the 91 triple-cancellation residue classes, and seek a symbolic all-threshold exact least-period formula or exact counterexamples. Activity record and live Task owner reconciliation remain separate from this independent scientific Source publication.
