# PREFIX-1063 — Linear upper bound for the first negative grade-two BRC difference

2026-11-24. AUTHOR_CONDITIONAL_EXACT_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED. Independent portable continuation of the original grade-two candidate BRC observer; no formal Task CLAIM, canonical kernel rerun, or new physical residual attribution. Same frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; same Stage46 chart anchor O, incoming -e1, reversal -5 (phase cover 5q), other weight 1, next incoming -d, blocked Link {O,e1} in both orientations without renormalization, exactly two negative steps. Preserve complete Cell/port/grade/sign/source observation before the parent CT contraction. Parent d91f254e8f1fc36e8f974fd5452a91144e46f570:research_notes/portable_direct/2026-11-24_r6_prefix1062_no_finite_shift_complete_monotonicity.md (blob ebc75a30458e675070dcfceef8eae9a86aa04832). The parent exact BRC packet and its computed difference witness are reused, not recomputed. The proof below is an inequality on its exact observer, not another evolution law or a classical reference calculation.

## New theorem

Write p_n=Delta_n^(2)/36^n, D(n,k)=(-1)^k forward_difference^k p_n and k_min(n)=min{k>=0:D(n,k)<0}. For the frozen candidate, for every integer n>=14,
    
    k_min(n) <= 12 + 10^35 (n-13).

In particular limsup k_min(n)/n <= 10^35, a finite bound. The constant is intentionally coarse; it does not predict the experimental slope or establish its limit. More generally the same argument gives a finite linear bound for any fixed finite-order paired-polynomial functional of the type below with a negative witness at an exponent at least its order. This strengthens the parent existence theorem: negative witnesses cannot require superlinear growth of the first negative order. It does not assert monotonicity of k_min.

## 1. Exact inherited observer

For x=Y/36, Y=SS*, S=sum_i z_i, E=x d/dx, the parent gives

    L(F)=36^-8 sum_{a=0}^4 CT[J_a (E+8)^a F(x)],
    D(n,k)=L(x^(n-8)(1-x)^k), n>=8,

where the J_a are fixed signed Laurent polynomials of the full paired Cell difference. By the parent's positive contraction norm proof,

    |L(F)| <= 36^-8 sum_a ||J_a||_1 sup_{[0,1]} |(E+8)^a F|.

This bound uses the same exact paired translation algebra. In the parent executed output the row n=13, k=13 has numerator -2416679628859956660645476296080 with denominator 36^26. Put W=2416679628859956660645476296080, f=x^5(1-x)^13. Then L(f)=-W/36^26.

## 2. Smooth finite transport window

For h=n-13>=1 and integer J=C h, with C a positive integer, let w_j=max(1-j/J,0)^4 for j>=0. Define for x>0

    Q_h[w](x)=x^h sum_{j>=0} binom(h+j-1,j) w_j (1-x)^j,
    R_h=Q_h[w].

Only j=0,...,J-1 have nonzero weights. For a constant sequence 1 the sum is 1 on 0<x<=1. The coefficients in Q_h are nonnegative and sum to one (negative-binomial expansion); the mean of j under these weights is h(1-x)/x, obtained by differentiating the geometric power series. This is an auxiliary exact binomial identity, not a random physical step.

Since 0<=1-w_j<=4j/J, it follows that

    |R_h-1| <= 4/(Cx).

For delta w_j=w_j-w_(j+1), differentiating the generating polynomial, using binom(h+j-1,j)=binom(h+j,j)-binom(h+j-1,j-1), yields the exact relation

    E Q_h[w] = (h/x) Q_(h+1)[delta w].

It holds for finite support and x>0, and iterates by the product rule. For l>=1,

    E^l R_h = sum_{r=1}^l (-1)^(l-r) Stirling2(l,r)
                  h^(rising r) x^(-r) Q_(h+r)[delta^r w].

Proof by induction: E acting on x^-r gives -r x^-r and on Q_(h+r) gives (h+r)/x Q_(h+r+1) delta; the signed Stirling recurrence follows.

The real function w(t)=max(1-t/J,0)^4 is C^3 and its fourth derivative exists a.e. with magnitude at most 24/J^4. Repeated unit interval integration of its derivatives gives for 1<=r<=4, all integer j>=0,

    |delta^r w_j| <= (4)_r / J^r,

where (4)_r is the falling factorial. The normalization of Q bounds its value by the supremum of its input sequence. Since h^(rising r)<=r! h^r for h>=1, C>=1, 0<x<=1,

    |E^l(R_h-1)| <= (1/(C x^4)) sum_{r=1}^l Stirling2(l,r) r! (4)_r.

The four constants are 4, 28, 220, 1612. Including l=0 by the earlier estimate, all l=0,...,4 satisfy

    |E^l(R_h-1)| <= 1612/(C x^4).

This weighted bound is uniform in h. In contrast, a hard truncation need not control its derivatives uniformly as h grows. The window is a proof device with nonnegative weights on actual differences.

## 3. Transfer of a negative witness to any future row at linear cost

The expansion f=sum_{j=0}^{13} (-1)^j binom(13,j)x^(5+j) gives

    |(E+8)^b f(x)| <= 2^13 * 26^b x^5.

The Leibniz formula for (E+8)^a acting on f(R_h-1) applies (E+8) to f and E to the second factor. Consequently for a<=4,

    sup |(E+8)^a[f(R_h-1)]| <= 1612 * 8192 * 27^a/C.

At x=0 both sides of the polynomial derivative expression extend continuously, so the same bound holds on the closed interval. Therefore

    |L(f R_h)-L(f)| <= (1612*8192)/(C*36^8) sum_a 27^a ||J_a||_1.

Choose C greater than 1612*8192*36^18 sum_a 27^a ||J_a||_1/W. Then L(f R_h)<0 for every h>=1. On the other hand,

    L(f R_h)=sum_{j=0}^{J-1} binom(h+j-1,j) w_j D(13+h,13+j).

Every coefficient is positive. At least one of these finitely many actual BRC difference observations is negative. Thus k_min(13+h)<=13+J-1=12+C h.

The argument generalizes to any finite order q and witness f=x^m(1-x)^k with m>=q (m>=1 for q=0); use a cutoff power at least max(q,1), control E derivatives through q and the factor x^m. If necessary a negative witness farther down an inherited row can be obtained from a separately justified parent propagation theorem. No assertion about a specific density or its zeros is required for this linear bound.

## 4. Explicit numerical constant (exact norm inequalities, no new model calculation)

Use the parent executed checker's numerator and H construction directly. For Laurent-polynomial l1 norm including t, ||S||=6, ||R=1-tS||<=7, ||L_i||=10, ||A_i||,||C(i,j)||<=45, ||K(i,h)||<=30, ||B(i,h)||<=310, ||R+B||<=317. Here A,C,K,B are exactly the parent checker's formal packet expressions; K for i=h has one coefficient 25 and five coefficients 1. Its norm is 30. U is a sum of 36 terms and V of six, so

    Nbound=7*36*45^2*317 + 25*7*6*45^2
           +10*49*45+390*49+390*343 = 164066280.

This bounds each N_j; the first factor ||1-z_1 t||<=2 was deliberately bounded by 7. In the parent's 2H construction each term of t-degree d<=5 is multiplied by S^(5-d) and the coefficients ((d+1)(d+2), -(2d+3), 1). Hence the weighted sum of l1 coefficient norms of 2H at weight 27 is at most Nbound*6^5*(42+13*27+27^2)=Nbound*7776*1122. Since J_a comes from H_1 H_1* - H_2 H_2* (parent checker uses four times J_a),

    sum_a 27^a ||J_a||_1 <= (Nbound*7776*1122)^2 / 2.

Actual integer arithmetic in this turn (proof-bound scalar only):

    N = 7*36*45**2*317 + 25*7*6*45**2 + 10*49*45 + 390*49 + 390*343
    B = (N*7776*1122)**2
    W = 2416679628859956660645476296080
    floorCplus1 = (1612*8192*B*36**18)//(2*W) + 1

Returned N=164066280, floorCplus1=57741464922880993728002841477913162. This is strictly less than 10^35, so C=10^35 suffices. All this arithmetic concerns a rigorous upper bound on the known exact packet, not a new BRC or classical trajectory. The inequality is intentionally conservative.

## Scope and next question

New proof: finite linear upper bound, with explicit constant for the frozen candidate. No new BRC model evaluations, independent review, physical inference or formal Task result. The previous finite sample suggests a much smaller slope, but no positive linear lower bound, limit or fixed-k eventual sign is proved here. Next: derive a usable slope bound by tightening the transport window against the actual grouped J coefficients, or establish local sign intervals of the paired spectral distribution and a controlled proportional-index concentration theorem. Keep the original signed branch/port structure and treat any scalar spectrum only as the inherited exact observer.
