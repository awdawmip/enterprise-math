# D25: an exact binomial–harmonic–dual-tail p² certificate for the p≡13 branch

2026-11-01. **AUTHOR-SIDE / PROVED FINITE ALGEBRAIC IDENTITY / EXECUTED EXACT REGRESSION / UNREVIEWED / NOT_ADMITTED / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_RUN.**

Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Research logical lane: chatgpt-research-onhour-enterprise-math-20260923. Do not adopt maintenance identity chatgpt-hourly-enterprise-math-20260921.

## Scope and pre-existing evidence

The original unresolved target is the weighted 216-series A_p≡p (mod p³) for primes p≡13,19 (mod24). The experimental stronger affine 216/2304 congruence modulo p⁴ is not proved. The 2304-model supercongruence B_p≡p(-3/p) (mod p³) is an *external proved theorem* (Guo–Zudilin, Advances in Mathematics 346 (2019), https://arxiv.org/abs/1803.01830). Previous unreviewed Enterprise Math work obtained a CM(-24) mod-p selector for the beta Gauss factor, the 19-class beta signed p³ boundary formula, and original 216 signed upper-port formulas. These are reused at their exact scope, not re-proved or accepted here. In particular the conjectural p≡13 mod24 relation G_p≡0 (mod p²) remains open.

## New theorem (every prime p>7, p≡5 mod8)

Define
\[
a=\frac{5p-1}{8},\quad b=\frac{7p-3}{8},\quad
d=b-a=\frac{p-1}{4},\quad
\beta_k=\frac{(1/8)_k(3/8)_k}{9^k(k!)^2},\quad
G_p=\sum_{k=0}^{p-1}\beta_k.
\]
In the p-local integers define H_n=Σ_{j=1}^n 1/j modulo p (H_0=0), and
\[
c_k=\binom ak\binom bk9^{-k},\qquad
J_p=\sum_{k=0}^{a}c_k\pmod{p^2},
\]
\[
C_p=-\frac18\sum_{k=0}^{a}c_k\{5(H_a-H_{a-k})+7(H_b-H_{b-k})\}\pmod p.
\]
Define a different, *dual-tail* sequence by R_0=1 and
\[
R_r=R_{r-1}\frac{(8r)(8r+2)}{9(8r+7)^2},
\quad 1\le r<d,
\quad
V_p=\frac{10}{441}\binom ba9^{-a}\sum_{r=0}^{d-1}R_r\pmod p.
\]
Every displayed denominator is a p-unit. The exact source-separated congruences are
\[
\boxed{\sum_{k=0}^{a}\beta_k\equiv J_p+pC_p\pmod{p^2},}
\]
\[
\boxed{\sum_{k=a+1}^{b}\beta_k\equiv pV_p\pmod{p^2},\qquad
\sum_{k=b+1}^{p-1}\beta_k\equiv0\pmod{p^2}.}
\]
In particular,
\[
\boxed{G_p\equiv J_p+p(C_p+V_p)\pmod{p^2}.}\tag{1}
\]
Here \(R_r=9^{-r}(1)_r(5/4)_r/(15/8)_r^2\), so the dual tail is a truncated _3F_2(1,1,5/4;15/8,15/8;1/9), **not** the original beta series and not a native H0/B0 certificate.

### Complete proof

The exact identities \(1/8=-a+5p/8\) and \(3/8=-b+7p/8\) give, for 0≤k≤a (all j−a and j−b nonzero modulo p),
\[
\beta_k\equiv\frac{(-a)_k(-b)_k}{9^k(k!)^2}
\left(1+\frac p8\left[
5\sum_{j<k}\frac1{j-a}+7\sum_{j<k}\frac1{j-b}
\right]\right)\pmod{p^2}.
\]
Because \((-a)_k(-b)_k/(k!)^2=\binom ak\binom bk\) and
\(\sum_{j<k}(j-a)^{-1}=-(H_a-H_{a-k})\), with the corresponding b identity, summing gives the first source congruence.

The exact recurrence
\[
\frac{\beta_{k+1}}{\beta_k}=
\frac{(8k+1)(8k+3)}{576(k+1)^2}
\]
has exactly two exceptional indices in 0≤k≤p−2: \(8a+1=5p\), \(8b+3=7p\). Since p>7, each supplies exactly one p factor. All denominators are p-units. Hence \(v_p(\beta_k)=0\) for k≤a, equals 1 for a<k≤b, and equals 2 for b<k<p. This proves that the high zone cannot contribute modulo p².

Modulo p the numerator Pochhammers satisfy \((1/8)_a\equiv(-a)_a\) and \((3/8)_a\equiv(-b)_a\), so
\(\beta_a\equiv\binom ba9^{-a}\pmod p\). One exceptional recurrence step gives
\[
\frac{\beta_{a+1}}p\equiv\frac{5\cdot2}{576(7/8)^2}
\binom ba9^{-a}
=\frac{10}{441}\binom ba9^{-a}\pmod p.\tag{2}
\]
For r=1,...,d−1, apply the same coefficient recurrence at k=a+r. Reducing factors modulo p gives
\[
\frac{\beta_{a+1+r}/p}{\beta_{a+r}/p}
\equiv\frac{(8r)(8r+2)}{9(8r+7)^2}\pmod p.
\]
The denominator is nonzero: 0<8r+7<2p and 8r+7=p is impossible since p≡5 mod8. Combining this recurrence with (2) gives the middle-zone identity and completes (1). No assumption of the unproved p² annihilation was used. QED.

## New precise p13 obligation and sharp witnesses

For p≡13 mod24, previously established **mod-p** CM selection identifies G_p≡0 (mod p), hence J_p≡0 (mod p). In this class the stronger unresolved statement G_p≡0 (mod p²) is *equivalent* to:
\[
\boxed{\frac{J_p}{p}+C_p+V_p\equiv0\pmod p.}\tag{3}
\]
The division J_p/p is performed on its mod-p² representative. Equation (3) is **not proved here**. It is the next finite binomial–harmonic–dual-tail cancellation to attack using Jacobi/CM involutions or to falsify.

Exact residues, from independent integer implementations:

| p | J_p mod p² | J_p/p mod p | C_p | V_p | G_p mod p² |
|---:|---:|---:|---:|---:|---:|
| 13 | 104 | 8 | 6 | 12 | 0 |
| 37 | 555 | 15 | 34 | 25 | 0 |
| 61 | 3233 | 53 | 2 | 6 | 0 |
| 109 | 1853 | 17 | 91 | 1 | 0 |
| 373 | 27975 | 75 | 66 | 232 | 0 |
| 541 | 5410 | 10 | 61 | 470 | 0 |

For p=13 the three selected p-digit residues are 8,6,12, all individually nonzero, with 8+6+12=26≡0 mod13. For p=373 they are 75,66,232, summing to 373; again no source can be silently deleted. The naive shortcut J_p≡0 (mod p²) is **disproved** by p=13 (J_p=104 mod169) and p=373 (J_p=27975 mod139129). The distinct split-class control p=29 gives J_p=403, C_p=8, V_p=17, G_p=287 modulo 841, in particular G_p=26 mod29≠0.

## Typed BRC reuse and executed scope

The carrier is the sequence of p-integral rational beta coefficients with original index, binomial/harmonic deformation labels and exact valuation. The three ports [0,a], [a+1,b], [b+1,p−1] retain their signed/valuation first lifts. The *terminal observer* is G_p modulo p²; the terminal sum alone does not preserve the derivative/weighted-H observer or either original 216 signed cutoff. This applies BRC's provenance/quotient discipline concretely, without importing a new X6 spatial structure.

Executed stdlib script: research_notes/portable_direct/d25_beta_p13_binomial_harmonic_tail_20261101.py. It verified all **109 primes p≤3000 with p≡5 mod8**, including **53 primes p≡13 mod24**, testing the separate three source identities, endpoint (2), combined (1), and independent factorial numerator coefficient cross-checks at p=13,29,37,61,373. Every assertion passed. Finite checks support, but do not prove, the infinite-class conjecture (3). No Lean check, native H0/B0 divided power [X]U mod139129, Frobenius, rank, signed odd Green/Hesse, κ or independent replication was executed.

## Exact continuation

Mother: complete original weighted216 A_p≡p modp³ on p≡13,19 mod24. Highest new immutable author-side frontier: theorem (1) and its source-separated proof for every p>7,p≡5 mod8; tested sharp sources and explicit conjectural cancellation (3). Do not redo p19 beta p³ signed reflection or original 216 high I3–I5 formulas. Next mathematical action: attempt a finite Jacobi/CM proof (or falsifier) of equation (3), and then the original 216/2304 bridge preserving p13 and p19 branches. Separate native p373 benchmark: Enterprise Math Issue #1559, still without authenticated execution/claim in this context; required original H0/B0, semilinear direction, actual module rank, odd Green/Hesse, κ, Delta-R and independent check remain **PENDING_OWNER/NOT_RUN**.

This client directly read em_status v0.6.11 (research_authority_granted=false, executor_binding_configured=false); its checkpoint_list returned ACCESS_DENIED, and local em_control_result lookup for the earlier bridge request research-onhour-20261031-0205-dispatch-r15 returned CONTROL_REQUEST_NOT_FOUND (client scope), **not** a reversal of the historical bridge report UPSTREAM_CODE_REVIEW_REQUIRED. No own current winning Source claim/run or Result is asserted, no request replayed, and none of the three old staging artifacts is merged into accepted results. P000, ACTIVE worldview, frozen scientific pin and task schedule/notification settings unchanged.