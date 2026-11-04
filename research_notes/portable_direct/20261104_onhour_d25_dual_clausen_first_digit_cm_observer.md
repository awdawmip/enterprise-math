# D25 — dual finite-field Clausen squares and exact first-digit CM-class observer

2026-11-04 Asia/Hong_Kong. **AUTHOR-SIDE PORTABLE RESEARCH / EXACT CLASSICAL-IDENTITY SPECIALIZATION / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.**

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, immutable publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923`; no maintenance-lane operation. This note consumes the original 216/2304 coefficient families, known Green two-seam and first-wall records and the Guo–Zudilin 2304 weighted supercongruence, without treating author-side work as canonically admitted.

## Original source and new first-digit observation

For every prime p>=5, let
```text
a_k = (2k)!(3k)! / ((k!)^5 216^k)
b_k = (4k)! / ((k!)^4 2304^k)
A_p = sum_{k=0}^{floor((p-1)/3)} a_k  (mod p)
B_p = sum_{k=0}^{floor((p-1)/4)} b_k  (mod p)
M_a = sum k a_k ; M_b = sum k b_k (same truncated ranges, mod p).
```
Original valuations are v_p(a_k)=floor(2k/p)+floor(3k/p) and v_p(b_k)=floor(4k/p), 0<=k<p; hence the declared ranges are precisely the nonzero-mod-p source bands. All denominators here are units.

**New testable cross-family first-digit candidate** (finite exact support, NOT universal proof):
```text
A_p = (-3/p) B_p  (mod p).                                  (C1)
```
**New candidate quadratic-character source selector** (finite exact support):
```text
A_p = B_p = 0 (mod p)   iff  (-6/p) = -1.                  (C2)
```
For p>=5, (-6/p)=-1 is precisely p mod24 in {13,17,19,23}; the D25 frozen classes {13,19} are included. The split-prime nonvanishing in (C2) is part of the candidate and is not derived from the polynomial-square theorem below. In all 1227 primes 5<=p<=10000, (C1), (C2), and the original weighted first-digit relations A_p+6M_a=0 and B_p+8M_b=0 passed via exact F_p arithmetic. The existing Guo–Zudilin weighted theorem already accounts for B_p+8M_b=0; this check does not re-claim that theorem.

Finite class table (columns count primes, zeros of A, zeros of B):
```
p mod24 | count | A=0 | B=0
1         143      0     0
5         157      0     0
7         156      0     0
11        155      0     0
13        157    157   157
17        152    152   152
19        155    155   155
23        152    152   152
```
This is **exhaustive finite computational coverage** over the specified 1227 prime inputs, not proof for every prime.

## Theorem A: original 216 source admits a genuine finite-field square (all primes p=6r+1>=7)

Write rising factorial (u)_k, and define over F_p[x]:
```text
P216,p(x)=sum_{k=0}^{2r} [(1/2)_k(1/3)_k(2/3)_k/(k!)^3] x^k
F216,p(x)=sum_{k=0}^r [(1/6)_k(1/3)_k/(k!)^2] x^k.
```
Then **as polynomials**, not only at one observed value,
```text
P216,p(x) = F216,p(x)^2    in F_p[x].                       (T-A)
A_p = F216,p(1/2)^2       in F_p.
```
Proof: Classical Clausen formal power-series identity
```text
(_2F1(a,b; a+b+1/2; x))^2
    = _3F2(2a,2b,a+b; 2a+2b,a+b+1/2; x).
```
Specialize a=1/6, b=1/3; both bottom parameters are 1. In F_p for p=6r+1, (1/6)_{r+1}=0 and (1/3)_{2r+1}=0. Reduction of the rational coefficient identity for every degree 0<=k<=2r is legal (k! unit), and the right and squared left sides have degree <=2r. Thus all coefficients coincide. The original normalized bivariate coefficient identity is retained: the p-free source a_k is precisely P216,p's kth coefficient evaluated at x=1/2.

## Theorem B: original 2304 source admits a finite-field square for p=8h+1 or 8h+3

For primes p≡1,3 (mod8), h=floor((p-1)/8), m=floor((p-1)/4)=2h, define
```text
P2304,p(x)=sum_{k=0}^{2h} [(1/2)_k(1/4)_k(3/4)_k/(k!)^3] x^k
F2304,p(x)=sum_{k=0}^h [(1/8)_k(3/8)_k/(k!)^2] x^k.
```
Then
```text
P2304,p(x)=F2304,p(x)^2 in F_p[x],                       (T-B)
B_p=F2304,p(1/9)^2 in F_p.
```
Proof: Apply the same Clausen identity with a=1/8,b=3/8. If p=8h+1, (1/8)_{h+1}=0; if p=8h+3, (3/8)_{h+1}=0; in either case the 3F2 series stops mod p at k=2h+1 from its 1/4 or 3/4 parameter. Degree bounds and unit denominators give equality coefficient by coefficient. The unnormalized original b_k is the kth P2304 coefficient evaluated at x=1/9, since 256*9=2304.

For the exact D25 class p≡19 (mod24), both Theorems A and B apply simultaneously. The finite source observation A_p=B_p=0 becomes the pair of explicitly inspectable root tests F216,p(1/2)=F2304,p(1/9)=0 in F_p. At p≡13 (mod24) Theorem A applies, while P2304 remains an original finite F_p-polynomial, so a different comparison representation is needed. These squares are genuine exact algebraic reductions and the root/character classification remains the distinct open lemma.

## Executed exact computation and independent source checks

The standalone Python standard-library checker rebuilds both polynomials by their independent factorial recurrences, evaluates them at 1/2 and 1/9 with exact integer modular inverses, computes weighted first moments, checks the two character candidates and class counts for *every prime* 5..10000, and checks the entire **coefficient vector** of each Clausen square at every eligible prime <=3000:
- 216: 207 primes / 94,771 polynomial coefficient positions;
- 2304: 209 primes / 73,545 positions;
- independent direct original integer binomial coefficients: 431 terms across 12 diagnostic primes.
All checks passed. No floating-point values or high-level unverified oracle are used. The proofs of T-A and T-B are algebraic; the computed range for C1/C2 is the declared finite domain.

Representative exact first-digit values (A,B; moments M_a,M_b):
```text
p=5:   (3,2; 2,1); χ(-3)=-1, χ(-6)=+1
p=7:   (4,4; 4,3); χ(-3)=+1, χ(-6)=+1
p=11:  (10,1; 2,4); χ(-3)=-1, χ(-6)=+1
p=13:  (0,0; 0,0); χ(-3)=+1, χ(-6)=-1
p=19:  (0,0; 0,0); χ(-3)=+1, χ(-6)=-1
p=73:  (50,50; 16,12); χ(-3)=+1, χ(-6)=+1
p=97:  (4,4; 64,48); χ(-3)=+1, χ(-6)=+1
p=373: (0,0; 0,0); χ(-3)=+1, χ(-6)=-1
```

## Consumed and remaining D25 work

The frozen hard target remains Δ_p−R_p=0 mod p for p≡13,19 (mod24). Existing precise signed Green problem remains W216−V2304=0 mod p³; this first-digit classification and the exact square ports are new possible proof mechanisms, not substitutes for third-digit cancellation. The next direct scientific action is to derive (C1)/(C2) from an actual finite-field hypergeometric transformation or an exact common CM/trace observer; use the two separate square factors at p≡19 to discriminate candidates, and a representation for the quartic p≡13 case. If a source identity is established, lift its signed Green/first-wall defects modulo p²/p³, retaining valuation bands and endpoint coefficients. Prior 2304 half/full GZ result, two-seam theorem and first-wall λδ are consumed without repeating the scans. Original fixed p373 H0/B0 [X]U modulo139129, module rank, semilinear Frobenius, κ and independent replay remain unexecuted under enterprise-math issue #1559.

Research provenance/observer: original 216 and 2304 factorial populations each retain original k, coefficient, normalization, valuation cut, prime-class character, finite polynomial coefficients and derivative weighted moment. Their Clausen squares are first-digit algebraic **projections** with explicitly declared range and invertibility; no native-X6 H0/B0 or original p-adic higher-digit replacement is asserted. BRC reuse is exact source-labelled pairing/class discrimination with original operations. Publication is neutral author-side evidence, not Source CLAIM/run/checkpoint/Result/review.

Control status at 2026-11-04 08:02Z: Sites v0.6.11 static read-only, no authenticated Research execution authority or write relay. Historical original request `research-onhour-20261031-0205-dispatch-r15` has definitive GitHub bridge receipt kimi-query-bridge#6633 COMPLETE/FAILED/UPSTREAM_CODE_REVIEW_REQUIRED; not replayed. Three prior neutral staging sources remain separate. No current Source checkpoint or formal acceptance claimed.
