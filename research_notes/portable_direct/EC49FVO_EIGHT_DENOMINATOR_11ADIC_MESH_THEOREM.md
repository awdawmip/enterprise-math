# EC49FVO — Eight-denominator 11-adic projective phase mesh

2026-11-21 Asia/Shanghai. Scientific status: AUTHOR_PROVED / EXACT_INTEGER_PERIOD_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED.
Provenance: frozen BRC16943 Bernoulli observation; direct scientific parent EC49FVN at awdawmip/enterprise-math@291b092c120755abfd3fe450904617a1808d7e32. Portable independent research, not an authenticated shared CLAIM, Result or Review.

## Exact frozen observer and certificate

Retain the rational functions

\[
U=\frac{4822040484}{8132285009},\quad \gamma=\frac{141024}{1653649},\quad L_a(x)=\frac{637-3x}{637},\quad L_b(x)=U(1+\gamma x),
\]
\[
a(x)=1-(1-x)L_a(x),\quad b(x)=1-(1-x)L_b(x),\quad
t(x)=\frac{\log R(x)}{\log S(x)}.
\]

For positive integers h,n, use the existing projective no-root implication:
\[
H_{h,n}(z)=\frac{a(z)^h L_a(z)^n-b(z)^h L_b(z)^n}{L_a(z)-L_b(z)}
\quad\text{has no root in }\mathbb P^1(\mathbb F_{11})
\]
implies that t(x) is not h/(h+n) for **any** rational observer width x in (0,1). The divided difference is a polynomial because a-b=-(1-z)(L_a-L_b). Including the projective point at infinity covers rational width denominators divisible by 11. This is a conclusion in the frozen *derived Bernoulli observer*, not a native Heartbeat X6 experiment or proof of the upstream FUQ/FUR composite-minimax equivalence.

## Construction

For every integer j>=7, put k=2^j and select eight integer denominators (all <=k):
\[
D_j=\{k,\;7k/8,\;13k/16,\;k/2,\;k/4,\;k/8,\;k/16,\;7k/16\}.
\]
Let T_j consist of all reduced fractions h/d strictly between 0 and 1, with d in D_j, gcd(h,d)=1 and a complete p=11 no-root certificate for exponent pair (h,d-h). Distinct reduced denominators yield distinct phases. Let S_H contain *all* certified excluded reduced phases of denominator at most H.

### Theorem A (effective covering)

The maximum distance between consecutive points of T_j together with 0 and 1 obeys
\[
\boxed{\Delta_j\le\frac{455}{91k}=\frac5k}.
\]
The bound is **attained** for every j>=10; for j=7,8,9 the respective exact maximum gaps in the integer y chart below are 364,390,416. Thus for every integer H>=128 and every real interval I contained in [0,1],
\[
\boxed{|I|>10/H\ \Longrightarrow\ I\cap S_H\ne\varnothing.}
\]
This lowers EC49FVN's 122/(7H) threshold to 10/H (a 26/61, approximately 42.62%, decrease), keeping the order 1/H.

### Theorem B (explicit local intensity)

For every j>=7 and each half-open real interval I=[a,b) contained in [0,1], w=b-a,
\[
\boxed{\#(T_j\cap I)=\frac{61}{88}kw+E_j(I),\qquad |E_j(I)|\le\frac{684}{77}.}
\]
The exact *full-period* discrepancy oscillation is 684/77 for odd j and 1088/143 for even j. The former three-denominator intensity was 5k/11=40k/88. The new bounded-error constant is larger than the former 976/143; the improvements here concern gap and intensity.

### Theorem C (joint effect within a finite menu)

Keeping the old three denominators fixed, allow any subset of the additional five: k/2, k/4, k/8, k/16 and 7k/16. The full eight-denominator family has worst-case cyclic integer-chart gap 455 across twenty exponent states. Any proper subset has worst-case gap at least 546. Deleting one additional denominator from the full family, in the order just stated, yields worst-case gaps
\[
(600,\ 546,\ 696,\ 630,\ 637).
\]
This is a finite-menu optimum only; arbitrary denominator families remain open.

## Proof with an exact finite certificate

**(1) p=11 mask.** Enumerate all eleven affine field points. The one divided-difference singular point is z=3, where a=b=L_a=L_b=10 mod 11. Its quotient value is
\[
L_a^{n-1}a^{h-1}\big(n\,a-h(1-z)L_a\big),
\]
nonzero exactly if 9h+10n is nonzero mod 11. At the other ten affine points and the projective point at infinity, nonvanishing depends only on (h,n) mod 10. Explicit exhaustive arithmetic gives 44 acceptable nonsingular exponent pairs among 100 modulo-10 pairs; impose the additional linear mod-11 condition. Thus the full no-root predicate depends only on (h,n) modulo 110. An independent complete projective evaluator confirms equality with this compact predicate for all 12100 positive pairs 1<=h,n<=110. The attached verifier includes the exact field formulas, zero handling and the infinity point.

**(2) One integer coordinate.** Each denominator is d=r*2^(j-e), with
\[
(r,e)=(1,0),(7,3),(13,4),(1,1),(1,2),(1,3),(1,4),(7,4).
\]
For a reduced phase h/d set y=91*k*h/d=(91*2^e/r)h. The eight integer step factors are
\[
91,\ 104,\ 112,\ 182,\ 364,\ 728,\ 1456,\ 208.
\]
Since j>=7>e and r is odd, gcd(h,d)=1 iff gcd(h,2r)=1. For each layer the periodic residue mask is determined by h modulo 110, d-h modulo 110, and gcd(h,2r)=1. Consequently its integer y period divides
\[
\frac{91\,2^e}{r}\operatorname{lcm}(110,r)\mid M,\qquad M=160160.
\]
The exponent-state dependence repeats after 20 increments of j because 2^(j+20)=2^j modulo 110 for all j>=1.

**(3) Exhaustive common-period computation.** For each of the 20 exponent states j=11,...,30, enumerate every possible admissible positive h in one y-period for each layer, union the exact integer coordinates and sort. Every state has precisely 1220 distinct coordinates in [0,M); every state's maximum cyclic adjacent gap equals 455. Compute also each of five leave-one-out cyclic maxima, obtaining exactly (600,546,696,630,637). Since removing points cannot shrink a maximum gap, every proper subset has a maximum at least min(600,546,696,630,637)=546. This proves Theorem C.

**(4) From period to a finite denominator.** The exact mask points with 0<y<91k correspond one-for-one to the allowed reduced numerators 1<=h<d. Restriction of a periodic point set to the interval (0,91k) with endpoints added cannot create a gap longer than its cyclic-period maximum 455. Direct enumerations give gaps 364,390,416,455 for j=7,8,9,10. The j=11 direct maximum is 455; for j>=12, the chart length 91k>2M necessarily contains at least one full worst-case cyclic gap. Hence the precise gap formula in Theorem A. Choose j=floor(log2 H), so k<=H<2k; 5/k<10/H. An interval longer than the largest possible point gap must meet T_j, proving the all-interval implication.

**(5) Local counting.** The exact periodic chart density is rho=1220/160160=61/8008; under y=91k*phase this becomes rho*91k=61k/88. Set F_j(y)=number of periodic-mask coordinates in [0,y) minus rho*y, periodically extended. Its extrema occur immediately before and after its integer jump coordinates y_i, with values i-rho*y_i and i+1-rho*y_i. All extrema are exact rationals; across the twenty states their oscillations are 684/77 (odd j) and 1088/143 (even j). Thus the count in any [a,b) differs from the main term by at most 684/77, proving Theorem B.

## Reproducibility and scope

Companion files: EC49FVO_EIGHT_DENOMINATOR_MESH_VERIFY.py and EC49FVO_EIGHT_DENOMINATOR_MESH_OUTPUT.txt in the same research_notes/portable_direct directory. Python standard library only, exact integer finite-field and Fraction arithmetic. The checker tests 12100 direct projective predicate pairs, all 20 complete period states, full point counts, gaps, rational discrepancy, five layer-deletion tests, direct finite denominators j=7,...,13 and small-chart mask equality; it returns ALL PASS. This is an exhaustive finite certificate plus a mathematical periodic reduction, not an extrapolation from sampled widths.

P000 V5, the ACTIVE Heartbeat six-dimensional spatial worldview and joint-relation residual-preservation constraint remain unchanged. Independent review, canonical Result/Working Truth and native FUQ/FUR transfer remain pending.

## Next unit

Explore finitely checkable improvements with rational ratios 13/32 or 7/32, or multi-prime projective masks, while keeping each changed chart period explicit. Investigate certificate proportion in moving intervals at the sharp O(1/H) scale; covering existence and proportional local density are distinct targets.
