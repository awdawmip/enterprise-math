# EC49FVK — exact height density among distinct reduced rational phases

2026-11-21 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_CRT_AND_MOBIUS_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED.

## Frozen science and theorem

Continues EC49FVJ in the same Draft PR #2886 under the unchanged derived Bernoulli observation pin BRC16943. Use exactly the likelihood phase t(x)=log R(x)/log S(x) for rational 0<x<1, and the already checked prime-local projective exclusion predicates for p=11,17,19,31 from EC49FVJ. P000 and ACTIVE worldview remain unchanged; full compound minimax interpretation remains dependent on FUQ/FUR.

A reduced rational candidate phase q=h/k in (0,1), gcd(h,k)=1, corresponds uniquely to the primitive ordered pair (h,n)=(h,k-h), with h,n>0 and gcd(h,n)=1. Thus counting reduced phases with denominator k<=H is identical to counting primitive ordered pairs with h+n<=H.

Let E(H) be the number of reduced h/k with 0<h<k<=H that one or more of the four projective certificates **exclude** for every rational width x. Let F(H)=sum_{k=2}^H phi(k) be the total number of distinct reduced phase values in that denominator range.

**Theorem:**
\[
\boxed{\lim_{H\to\infty}\frac{E(H)}{F(H)}
=\frac{36018427}{39813120}=0.9046873744132587\ldots.}
\]
The ratio is exactly the certified exclusion density, and provides a rigorous lower bound on the density of all impossible rational phase values for the frozen observer. The earlier unrestricted *exponent-pair residue* proportion was 421142/550715≈0.7647185931; gcd conditioning changes it materially.

For 11/17 alone the reduced-phase density is 11473/15552; adding 19 gives 168091/207360; adding 31 gives 36018427/39813120.

## Proof: primitive CRT fibers

Let Q=lcm(10,16,18,30)=720 and M=Q·11·17·19·31=79302960. The projective nonsingular base evaluations for p depend only on (h,n) modulo p-1, so on (h,n) modulo Q. Its singular derivative condition is one nonzero linear equation alpha_p h+beta_p n=0 modulo p, as established in EC49FVJ.

For a primitive pair (h,n), no prime factor of M may divide both h and n. First restrict the base residue modulo Q to gcd(h,n,Q)=1. The exact number of such base pairs is
\[
Q^2 \prod_{\ell\mid Q}(1-\ell^{-2})
=720^2(1-1/2^2)(1-1/3^2)(1-1/5^2)=331776.
\]

For each p in {11,17,19,31}, CRT residues modulo p are now independent of the base residue modulo Q and of those at all other such primes (each p is coprime to Q). Conditional on primitiveness, the pair modulo p is uniform over U_p=F_p^2\setminus\{(0,0)\}, of cardinality p²−1. The singular linear equation defines a line containing p points of F_p², of which exactly p−1 lie in U_p. Its failure probability is therefore
\[
\frac{p-1}{p^2-1}=\frac1{p+1}.
\]

For a given primitive base residue modulo Q, let J be the subset of primes at which the nonsingular projective base pattern is eligible. Independent CRT makes the conditional union probability
\[
1-\prod_{p\in J}\frac1{p+1},
\]
with the empty-set convention yielding zero.

The exact verifier reconstructs the four base pattern sets directly from the frozen rational coefficients. Exhaustive enumeration of all 331776 primitive base residue pairs gives the 16 mask counts below. Mask bit 0 denotes p=11; bit 1 p=17; bit 2 p=19; bit 3 p=31.

| mask | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| count | 26112 | 24768 | 32256 | 16704 | 9600 | 17280 | 5760 | 10368 |
| mask | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| count | 26496 | 38976 | 28800 | 36288 | 11520 | 24960 | 6912 | 14976 |

Their sum is 331776. Exact rational evaluation of the weighted sixteen-term sum gives
\[
\boxed{\frac1{331776}\sum_{j=0}^{15}N_j
\left(1-\prod_{p\in J(j)}\frac1{p+1}\right)
=\frac{36018427}{39813120}.}
\]

Finally, primitive positive lattice pairs ordered by height h+n<=H are equidistributed among the residue pairs modulo M with no simultaneous vanishing of h,n modulo any prime dividing M. For completeness: for any such fixed admissible residue pair r,s, Möbius inversion gives
\[
\#\{h,n>0:h+n\le H,\ (h,n)\equiv(r,s)\bmod M,\ \gcd(h,n)=1\}
=\frac{H^2}{2M^2}
\sum_{\substack{d\ge1\\(d,M)=1}}\frac{\mu(d)}{d^2}+o(H^2).
\]
The leading constant is positive and identical across all admissible residue pairs. An inadmissible pair (both entries zero modulo a factor of M) contains no primitive positive integer pair. Thus the limiting primitive height-ordered certificate density equals the finite primitive CRT proportion just computed. Via the reduced phase/primitive pair bijection, this is E(H)/F(H). QED.

## Reproduction and scope

The Python stdlib checker EC49FVK_PRIMITIVE_PHASE_DENSITY_VERIFY.py reuses the exact EC49FVJ rational finite-field implementation; reconstructs all four pattern sets; enumerates all 331776 primitive mod-720 base residues; verifies the sixteen mask counts and the three nested exact rational union rates; separately enumerates every reduced fraction through height 100, 300 and 600 against the four prime predicates. Exact execution stdout: EC49FVK_VERIFY_OUTPUT.txt (ALL PASS). The finite-height approximations check code; the infinite limit follows from CRT plus the Möbius equidistribution argument.

This is an author-side computer-assisted theorem and is NOT_REVIEWED; its claim is the certified proportion of excluded reduced rational phases, not equality with the set of all mathematically impossible phases. A surviving reduced fraction need not be attainable by a rational width. No formal Task CLAIM, Result, Review, or Foundation promotion arises from publication.

**Next:** assess further primes, and look for a rational-width rational phase in the remaining ~9.53% certificate complement. The reduction to a family of exact rational-point problems on the divided-difference polynomial is available from EC49FVJ.
