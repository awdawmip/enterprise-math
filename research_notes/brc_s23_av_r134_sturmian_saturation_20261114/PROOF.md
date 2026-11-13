# R134 — Sturmian mechanical-word reduction and uniform cubic saturation

Date: 2026-11-14 Asia/Shanghai. Independent author-side S23 auxiliary mathematics. Frozen input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.

Predecessors: R131 @735fce0fc6fc481a703faf79caf65ba9af10b7cb; R132 generic lift @29f5e5ef7ef868037a814fb7d29806be3de4e54b; R133 uniform lift @66ea81c724cc353b7735b765ef2ce2241e428723. Researcher attribution is independent from any formal CLAIM/Review.

## Exact model and telescoping lemma

Fix integers K>=1,m>=1. On 0<theta<1, consider the S23 auxiliary observer

S_i^(K)(theta)=1[{(K+i)theta}<theta], i=0,...,m-1.

For real z and 0<theta<1, floor(z)-floor(z-theta)=1[{z}<theta], including exact equality boundaries. Hence

S_i^(K)(theta)=floor((K+i)theta)-floor((K+i-1)theta).

Putting rho={(K-1)theta} gives the standard lower mechanical-word representation

S_i^(K)(theta)=floor(rho+(i+1)theta)-floor(rho+i theta).

For each substring of length ell, its number of ones is the difference of two floors separated by ell*theta and therefore belongs to {floor(ell*theta),ceil(ell*theta)}. Any two equal-length substrings differ in their number of ones by at most one. Consequently every realized word is a finite balanced (Sturmian-factor) word, including rational singleton phases.

## Universal coefficient-independent cubic bound

Let St_m be the set of length-m factors of all irrational Sturmian sequences. The classical Mignosi counting theorem (1991) states

F_m=|St_m|=1+sum_{q=1}^m (m+1-q)*phi(q)=Theta(m^3),

where phi denotes Euler's totient. Therefore H(K,m), the number of distinct words in the tied-parameter S23 family, satisfies H(K,m)<=F_m for every K>=1.

Independently, the m+1 floors with slopes n=K-1,...,K+m-1 change only at theta=p/n. The number C of distinct interior cuts is at most sum_{n=K-1}^{K+m-1} max(n-1,0) <=(m+1)(K+m). Between cuts and at each singleton cut the word is constant, giving

H(K,m)<=min(F_m, 1+2(m+1)(K+m)).

These statements sharpen the distinction between R131's Omega(K) chronological cuts (already for fixed m=3) and the number of distinct words. The Mignosi formula is prior literature, not a newly claimed enumeration formula.

## Uniform saturation theorem R134

For every m>=1 and every integer K>=4m^3+2,

{ S^(K)(theta) : 0<theta<1 } = St_m,

hence H(K,m)=1+sum_{q=1}^m (m+1-q)phi(q).

**Proof.** Fix any w in St_m. Standard mechanical coding of an irrational Sturmian sequence gives an irrational alpha in (0,1) and some intercept rho with w_i=floor(rho+(i+1)alpha)-floor(rho+i alpha). Choose the adjacent Farey fractions a/b<c/d of order m whose open interval contains alpha. Their denominators b,d are at most m, and no rational with reduced denominator <=m lies inside that interval.

The circular order of the m+1 intercept breakpoints {-j alpha}, j=0,...,m, is constant inside this Farey interval: a collision between distinct j,k would mean (j-k)alpha is integral, a forbidden rational with denominator at most m. The word attached to each intervening intercept sector stays constant under continuous variation of alpha. Set alpha_0=(a/b+c/d)/2=(ad+bc)/(2bd). The target w is attained on one open intercept gap J at alpha_0.

Write D=2bd<=2m^2. Since every breakpoint at alpha_0 belongs to the rational lattice (1/D)Z/Z and the m+1 points are distinct, each open gap length is >=1/D. Choose rho_0 as the midpoint of the gap J. For all j=0,...,m,

dist(rho_0+j alpha_0,Z)>=1/(2D)>=1/(4m^2).

Set eta=1/(8m^3). For |theta-alpha_0|<eta, every rho_0+j theta changes by less than m*eta=1/(8m^2), so it crosses no integer. Thus the same w is produced at the fixed intercept rho_0 for all such theta. The interval I=(alpha_0-eta,alpha_0+eta) lies in (0,1): alpha_0 lies at least 1/(2m^2) from either endpoint.

Put L=K-1>4m^3. The real interval L*I has length 2L*eta>1 and hence contains some N+rho_0 with integer N. Take theta=(N+rho_0)/L in I. Then {(K-1)theta}=rho_0 and the tied S23 output equals w. This theta is rational because the Farey endpoints and midpoint rho_0 are rational. Every St_m word is realized; the reverse inclusion follows from the telescoping lemma. QED.

The uniform 4m^3+2 bound is sufficient, not minimal. It covers the full finite Sturmian language, including words that appear at exact rational singleton phases; no assumption of a generic source word is needed.

## R133 finite-checker audit: a concrete sign error

At R133 @66ea81c7, the line arrangement consists of y+i*alpha=k and y+j*alpha=h. Their crossing is alpha=(h-k)/(j-i), but check_r133.py uses Fraction(k-h,j-i), with the opposite sign. At m=4 this omits actual critical alpha values 2/3 and 3/4. Its printed generic word count 12 is incomplete; independent exact Farey/intercept sector enumeration gives 14, with the omitted patterns 0110 and 1111. For example generic rational witnesses (alpha,y)=(2/3,5/6) and (5/6,2/3) respectively have no integer equality y+j alpha for -1<=j<=3. This is an observed finite-coverage bug; it does not invalidate R133's separate rational-polygon sufficient-threshold proof. Original historical files are preserved.

## Verification and provenance

Companion check_r134.py evaluates the original fractional observer and its floor increment with Python Fraction, independently enumerates all exact theta cut atoms for fixed K, and obtains the classical two-parameter word set using Farey slope slabs and exact intercept chambers. Its result is in verification_r134.json: R134_STURMIAN_SATURATION_EXACT_PASS, m=2..9, 320 summed distinct two-parameter words, 1450 fixed-K crosschecks and 150 exact boundary/large-K comparisons. K=60 realizes the full classical language for each tested m. The finite checks assess the implementation; the theorem follows from the proof.

Citation: Filippo Mignosi, *On the Number of Factors of Sturmian Words*, Theoretical Computer Science 82(1), 71–84 (1991), DOI 10.1016/0304-3975(91)90172-X. https://dblp.org/rec/journals/tcs/Mignosi91

Next research: characterize the exact smallest saturation K as a function of m; design a coefficient-bit-efficient rational witness generator without traversing Omega(K) chronological events. This auxiliary mathematical result does not assert native X6 Cell/Link/Port event permission.
