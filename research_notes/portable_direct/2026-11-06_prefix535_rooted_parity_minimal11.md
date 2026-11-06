# PREFIX-535 — All 48 rooted parity series have sharp minimum order eleven

Date: 2026-11-06 Asia/Shanghai. Task line: RS-X6-NATIVE-ROTATION-DYNAMICS. Frozen scientific source: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Behavioral rules: verified current GLOBAL_KNOWLEDGE_V1 and Enterprise Math P000/ACTIVE, portable research, method and owner contracts. Status: AUTHOR_PROVED / EXACT_MODULAR_AND_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Model and question

Use the four STAR native signed-X6 candidate with triples A={L1,L3,L6}, B={L1,L4,L5}, C={L2,L3,L5}, D={L2,L4,L6}. There are 48 signed directed phases s=(STAR,previous,current). Each phase has exactly three legal macro successors; each successor possesses two distinctly labeled, ordered, length-two native Cell microstep paths INNER and OUTER. A length-d population from each root s contains 6^d labeled histories.

H(w) counts occurrences of the gate aAc, equivalently two successive INNER branch choices ending at T=(A,+L1,-L3). The first-axis signed-step BRC pair observer is p1(w)=min(N1+(w),N1-(w)). For a fixed start s, define

P_s(t,q,z)=sum_{d>=0} t^d sum_{w: |w|=d, root(w)=s} q^{p1(w)} z^{H(w)}.

The scalar is a multiplicity-weighted histogram of the full ordered native-branch population. Raw path/Cell records retain provenance for other future operations.

## Theorem

Define E(u,q), F(u,q), K(u,q) by the explicit exact polynomials in PREFIX-528 and PREFIX-534, and let D(u,q,z)=E(u,q)F(u,q)-(z-1)K(u,q), of degree 11 in u. Define two rooted parity subseries

A_s(u,q,z)=sum_{n>=0}[t^(2n)]P_s(t,q,z)u^n,
B_s(u,q,z)=sum_{n>=0}[t^(2n+1)]P_s(t,q,z)u^n.

**For each of all 48 fixed roots**, both A_s and B_s have D(u,q,z) as their exact reduced denominator over Q(q,z)(u). Hence both sequences have **generic minimum eventual constant-coefficient recurrence order 11** over Q(q,z).

The generic numerator degrees are 11 for the even series at precisely the three roots (A,-L6,+L1), (B,-L4,+L1), (B,-L5,+L1), and 10 for the other 45 even series and for every one of the 48 odd series. The three exceptional even numerators have coefficient of u^11 equal to 6,879,707,136 q^5(z-1). Their initial transient extends to u^11, while minimal eventual order remains 11.

## Proof: all-length upper bound

PREFIX-534 proved the all-length identity P_s(t,q,z)=N_s(t,q,z)/D(t^2,q,z) for every root s, with N_s an integer polynomial of t-degree at most 22. It derived this by a 49-coordinate rank-one phase/return transfer, exact consecutive recurrence residuals and Cayley–Hamilton. Since the denominator is an even polynomial in t, the unique split N_s=N_even(t^2)+t N_odd(t^2) gives

A_s=N_even(u)/D(u), B_s=N_odd(u)/D(u).

Thus deg_u N_even<=11 and deg_u N_odd<=10, giving an upper bound 11 on each eventual recurrence order.

## Proof: exact lower bound

Reconstruct the frozen 48-phase graph and target gate. For q=v^2 use the transfer defined by

f_{d+1}=2 W(v) f_d+(z-1)e_T g_d,
g_{d+1}=e_T^T W(v)^2 f_d,

with W_{ij}(v)=v^(1_{axis1(current_i)}+1_{axis1(current_j)}) for a legal phase transition i->j and zero otherwise, respecting three successors. Reverse/transpose orientation is chosen consistently with rooted output. For fixed root s, the initial endpoint observer at phase i is v^(-|sigma1(current_i)-sigma1(current_s)|), where sigma1 is signed first-axis incidence. Since p1=(K1-|sigma1(end)-sigma1(start)|)/2, these weights exactly produce the fixed-root BRC-gate coefficients, with z recording the gate.

Compute the first 23 coefficients of P_s and convolve with D(t^2) to recover the numerator coefficients, for every s. Work in F_1000000007 with v=2,q=4,z=3. D has exact u-degree 11. For each of the 48 roots, Euclid's polynomial algorithm returns gcd(N_even,D)=gcd(N_odd,D)=1, all 96 tests pass. Three even numerators have u-degree 11 and 45 have degree 10, while all odd numerators have degree 10. A nonzero specialized resultant establishes coprimality over Q(q,z)[u], and the attained specialized degrees prove the exact generic degree statements. Therefore the two rooted parity fractions are generically reduced and both have minimal eventual order exactly 11.

An independent repetition in F_998244353 at v=3,q=9,z=2 gives the same 96 GCD and degree verdicts. The first specialization is sufficient for the theorem; the second checks implementation stability.

## Independent native integer validation

A separate forward exact integer dynamic program propagates each starting phase, current phase, previous INNER/OUTER bit, unsigned first-axis visit total, and gate-event count. It enumerates branch-history multiplicities by exact integer coefficients. For every one of 48 roots at macro depths d=0..7, it checks 6^d native histories and evaluates 4^p1 * 3^H directly, then compares its result modulo 1000000007 to the 49-coordinate transfer. All 384 root-depth checks pass. For the first root (A,+L3,-L1) the values at depths 0..7 are 1, 6, 36, 216, 3008, 18048, 182272, 1093632. This independently validates the semantic correspondence of the rank-one transfer and native branch paths.

## Evidence, verification scope and continuation

The companion standalone Python 3 standard-library source PREFIX535_rooted_parity_certificate.py implements the frozen phase transitions, denominator E/F/K coefficients, all 96 polynomial-GCD checks at each of the two exact finite fields, and the independent 384 rooted-depth integer comparisons. Execute from its containing directory: python3 PREFIX535_rooted_parity_certificate.py. The script prints ALL_CHECKS_PASS and writes the actual computed JSON PREFIX535_EXACT_EXECUTION.json. Native integer computation and finite-field computation are exact; no floating point, external trigonometry, pi series, or physics residual attribution appears.

The theorem covers all 48 fixed origins but only the declared one-axis BRC cancellation and aAc gate joint-histogram observer for the frozen four-STAR candidate. A branch-resolved future-state observer uses the distinct 49-dimensional linear, 51-state deterministic and original Cell/path provenance-aware representations, as proved in their own prior scopes. No new formal CLAIM/Result/Review is asserted by this author note.

The next scientific unit is a fair, measured bit-complexity/time/storage comparison of the two order-11 parity recurrences, the 49-coordinate linear lift, and the 51-state branch-aware controller, including initial numerator formation, endpoint BRC correction, output extraction, and retained Cell/branch provenance. Parent objective remains arbitrary oriented-triad C6 generators and full native X6 generated rotation dynamics.
