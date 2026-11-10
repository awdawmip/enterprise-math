# PREFIX-658-R6 — Full-domain symmetry octant and enlarged BRC variance competitor orbit

Date: 2026-11-10 Asia/Shanghai. Research mode: independent TASK_RESEARCH / portable derivation.
Status: AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.

## Problem, model and current frontier

For the frozen signed 189-layer two-information-direction BRC first-stop statistical observer, the full parameter domain is (p,z) in [0,1]^2, including limit-probability endpoints (PREFIX-620/621). Define Y=max of the two independent Poissonized stopping clocks; mu=E Y, H=E[Y^2]/2, W=2H-mu^2 and V_q=q^2 W-q mu. Actual sampling slots are q=12 and q=24, and the inherited analytic interpolation considers every real 12<=q<=24.

PREFIX-655/656 certified strict maxima at two corners of small rectangles B. A concurrent extension (commit c470f3b7ad01c51cb9a1622a80da38d477d21dcb) certified the maxima M'_q=V_q(L,a') of B'=([L,1/6]×[a',b]) union ([a',b]×[L,1/6]), where L=3/20, a'=622575/4194304 and b=38913/262144. The other, independent PREFIX-657 study proved a strictly larger exact-variance competitor P=(L,1/8) by a 189-layer Fraction replay; its domain/B' addendum is commit 5240e656a799d5cc7b6c4311998ba0aa0902514a. Our work continues the later combined frontier.

Question: enlarge an exact continuous competitor region and reduce the full parameter search using the original branch-symmetric survivor law, without rerunning the already verified 189-layer calculation.

## Theorem 658.1 — Eightfold symmetry, octant and polynomial invariants

For all p,z in [0,1] and all q in [12,24],

    V_q(p,z)=V_q(1-p,z)=V_q(p,1-z)=V_q(z,p).

Thus every full-domain maximum has a representative in the octant 0<=p<=z<=1/2, and maximizing V_q on [0,1]^2 is equivalent to maximizing it on this closed triangle. A generic point 0<p<z<1/2 generates exactly eight distinct maximizing-equivalent points by these transformations.

There exists a symmetric bivariate polynomial G_q(X,Y), with degree at most 188 in each argument, such that

    V_q(p,z)=G_q(p(1-p),z(1-z)).

Thus V_q is also a polynomial in the elementary invariants e1=p(1-p)+z(1-z), e2=p(1-p)z(1-z), and partial_p V_q=(1-2p) partial_X G_q.

Proof. The exact first-passage survivor path counts A_n(k), 0<=n<=188, satisfy A_n(k)=A_n(n-k): flipping all signs leaves the confidence-width test and first-stop event invariant; PREFIX-620 independently exhaustively certified this finite pathwise symmetry. Therefore s_n(p)=sum_k A_n(k)p^k(1-p)^(n-k) satisfies s_n(1-p)=s_n(p). In the frozen double-direction Poisson moment kernels, mu and H are symmetric in the two survivor sequences and individually invariant under their sign-flips. The same holds for V_q. A continuous function on compact [0,1]^2 attains its maximum; independently reflecting each coordinate into [0,1/2] and then swapping reduces its search to the octant. Degrees of mu,H in either variable are <=188; degrees of V_q=q^2(2H-mu^2)-q mu are <=376. An invariant polynomial under p↦1-p is an even polynomial in p-1/2, hence a polynomial in p(1-p), of degree at most 188; apply this independently in z and use swap symmetry. The derivative identity follows by chain rule. QED.

## Theorem 658.2 — Strict full-domain square competitors and eight disjoint images

Let

    L=3/20, Z=1/8, P=(L,Z), r=61/16777216,
    S=[L-r,L+r]×[Z-r,Z+r].

For *every* (p,z) in the closed square S, strict rational inequalities hold:

    V_12(p,z)-M'_12 > 2065563603/52428800 > 39,
    V_24(p,z)-M'_24 > 3936536071/131072000 > 30.

For every real 12<=q<=24 and all (p,z) in S, V_q(p,z)-M'_q>15. By Theorem 658.1 the identical comparisons hold on each of the eight mutually disjoint reflected/swapped squares in [0,1]^2.

The earlier one-sided rectangle C=[L-2^-19,L+2^-19]×[Z,Z+2^-19] is contained in S. One S has area (2r)^2, exactly 3721/512=7.267578125 times area(C)=2*(2^-19)^2. The total eight-square area is 3721/64 times area(C). All these squares lie in the original full parameter domain, and strictly exceed the previously certified B' maximum. The global variance maximum outside these specified regions remains the mother objective.

Proof. The binomial event-score bound established in PREFIX-643 gives

    |s_n'(u)| <= (1/2) sqrt(n/(u(1-u))).

On u∈[63/512,1/6], u(1-u)>47/441 and n<=188, so this derivative is strictly below 21. On that entire interval the inherited nonnegative Poisson survivor kernel bounds give |mu_i|<3969, |H_i|<377055 and mu<378, hence |W_i|<3754674. Therefore for each coordinate |partial_i V_q|<K_q=q^2*3754674+q*3969; K_12=540720684 and K_24=2162787480. The entire S is inside this extended interval for both coordinates, including z<1/8, so integrating along two coordinate segments gives V_q(p,z)>V_q(P)-2rK_q.

The 189-layer exact witness from PREFIX-657 proves V_12(P)-M_12>4100.310 and V_24(P)-M_24>16272.968. By the separately proven B' extension and the derivative bounds, M'_q-M_q<K_q*2^-22, giving strictly

    V_12(P)-M'_12>4100.310-K_12*2^-22
                       =104107662189/26214400;
    V_24(P)-M'_24>16272.968-K_24*2^-22
                       =1032671676473/65536000.

Subtracting 2rK_q from these bounds is an *exact* rational calculation:

    104107662189/26214400 - 2r*540720684
         =2065563603/52428800>39,
    1032671676473/65536000 - 2r*2162787480
         =3936536071/131072000>30.

For a fixed point, (V_q(p,z)-M'_q)/q is affine in q, because M'_q=V_q(L,a'). Endpoint positivity therefore covers all real q in [12,24]. Multiplying by q>=12 and taking the smaller normalized endpoint gap gives the uniform >15 bound. Reflecting and swapping the square preserves V_q; the centers occupy four disjoint coordinate bands, since Z+r<L-r and L+r<1/2. The eight squares are pairwise disjoint. The area identity follows directly from r=61/2^24. QED.

## Scope, method, validation, next problem

The companion stdlib fractions.Fraction script executes 51 exact implication checks and the result JSON records every displayed strict gap. It reuses exact predecessor point and B' bounds; this turn performs no new 189-layer replay or 96-port original native run. No mathematical acceptance, formal shared CLAIM/Result/Review or reviewer independence is inferred.

BRC reuse: COMPOSE_APPLIED. Carrier: frozen signed branch-multiplicity survivor counts; observer: first-stop sampling variance; operations: sign-flip path involution, Poisson max survivor kernel, rational bound transport, and q-affine interpolation. The two observer probabilities are not native spatial axes or a two-dimensional plane.

Next discriminating unit: perform certified adaptive interval elimination on the triangular chamber 0<=p<=z<=1/2, using the P witness as a strict lower baseline, preserving current certified boxes. Test z=0 and unequal-coordinate ridges as possible better competitors, then subdivide unresolved cells. The mother objective is the full [0,1]^2 variance maximum for q=12 and 24, currently open.

Frozen dependencies: PREFIX-620/621 domain and finite survivor symmetry; PREFIX-643 score lemma (ae7872ca18676397fcc0dd9424fb77e08928bee7); PREFIX-655/656 corners (3dc372940c317cf540c96fc02b55284462549bac, 5352d203d66148eb8262ff1c38d49d3f1700f510); independent PREFIX-657 exact P witness (04c8f9a231545af52e2888d255dcfe54143587e9); full-domain/B' comparison (5240e656a799d5cc7b6c4311998ba0aa0902514a); concurrent B' extension (c470f3b7ad01c51cb9a1622a80da38d477d21dcb).