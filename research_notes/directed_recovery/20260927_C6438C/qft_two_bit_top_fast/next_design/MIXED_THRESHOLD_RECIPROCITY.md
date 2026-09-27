# Threshold reciprocity and a spline reduction for the mixed two-bit sum

Status: SYMBOLIC / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED. No scientific module, host numerical test, new literature query, or remote write was used. This note proves reductions and a precise remaining interface; it does not claim a terminating general mixed-floor algorithm.

## 1. Source and notation

Read in full:

- `../sep27-qft-two-bit-period-extension/PERIOD_EXTENSION.md`, SHA256 `97d2011a41a2f0a8416151955daa4b08f448ab38336b9214e29d8a5208bbd3b6` (especially its (3), (4), (6), (9)).
- `../sep27-qft-two-bit-top-general/TOP_BIT_GENERAL_MODULUS.md`, SHA256 `880fb9d90f9258e0b96f6f47281bd711b11bd2ec515bddb6a6212cf45266ee89`.
- New symbolic single-floor extension `../sep27-qft-floor-degree-five/DEGREE_FIVE_RECIPROCITY.md`, SHA256 `1453444f21c113c0d1819328b731031d0fe296e25756caac7e94d9cf628047b6`. It is not an implemented extension of the frozen degree-three runner `633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2`.

Use V=2^ell, p=2V, U=2^k, P=2U, m=P/p=U/V, M=P/V=2m, L=HP=2^g, C=HM=L/V. Since ell<k, m is even and at least two. Consider one nonempty canonical progression

    d_j=b+Rj, 0<=j<n, b>=0, R>0, D=b+R(n-1)<L.

An empty progression is returned before the formulas involving D. Let

    S_u(t)=sum_(0<=j<t) j^u, t>=0,
    Delta_a(v)=v^a-(v-1)^a.

The convention x^0=1 includes x=0, so Delta_0=0. All powers, ceilings, range counts, polynomial coefficients and exact divisions are paid typed operations in any future implementation.

## 2. Exact threshold reciprocity for a generic required mixed moment

For epsilon,zeta in {0,1}, define, also as right-continuous functions of a real variable x,

    A(x)=floor((x+epsilon U)/P),
    B(x)=floor((x+zeta V)/p),
    F(x)=A(x)^a B(x)^c.

The target is T=sum_j j^u F(d_j), for the fixed-degree indices required by period extension (u<=1 and u+a+c<=5). A changes only at coarse thresholds x=P k-epsilon U; B changes only at fine thresholds x=p y-zeta V. Retain only thresholds in (b,D]. Therefore the exact index ranges are

    k=A(b)+1,...,A(D),
    y=B(b)+1,...,B(D).                                 (1)

Empty ranges contribute zero; neither range is proposed as an execution loop.

At a coincident threshold, perform the coarse update before the fine update. Coincidence occurs only for zeta=0. The fine jump is then evaluated with the new A, and the coarse jump with the old B. Put

    A_y=floor((y+epsilon*m/2-zeta)/m),
    B_k^- = m*k-epsilon*m/2-(1-zeta),
    J_f(y)=ceil((p*y-zeta*V-b)/R),
    J_c(k)=ceil((P*k-epsilon*U-b)/R).                    (2)

The threshold restriction gives 1<=J_f,J_c<=n-1. These heights are never negative, and no clamp is being silently dropped.

Why (2) is exact: at a fine threshold,

    A_y=floor((y+epsilon*m/2-zeta/2)/m).

Its numerator before the half shift is an integer. For zeta=1, floor((v-1/2)/m)=floor((v-1)/m), giving the displayed expression. Immediately before a coarse threshold, the fine quotient equals m*k-epsilon*m/2-1 when zeta=0, and m*k-epsilon*m/2 when zeta=1. This is a left-limit calculation; substituting B at the boundary for B^- would double-count tied jumps.

The respective increments of F are

    A_y^a Delta_c(y),
    Delta_a(k) (B_k^-)^c.

At a tie their sum is the exact product increment because

    [k^a-(k-1)^a](y-1)^c + k^a[y^c-(y-1)^c]
      =k^a y^c-(k-1)^a(y-1)^c.

Each threshold contributes its increment to precisely the sample indices j>=J. Interchange these finite sums and use telescoping of the total increments from b to D. The result is

    T = S_u(n) A(D)^a B(D)^c
        -sum_y A_y^a Delta_c(y) S_u(J_f(y))
        -sum_k Delta_a(k)(B_k^-)^c S_u(J_c(k)).         (3)

This identity also handles n=1 (both ranges empty), a=0 or c=0, and thresholds landing exactly at an observed d_j. For u=0, S_0(J)=J; for u=1, S_1(J)=J(J-1)/2. The combined numerator must be divided exactly; individual terms need not be integral after a rational coefficient expansion.

### What (3) closes, and what it does not

The coarse correction contains only an ordinary single floor:

    J_c(k)=floor((P*k-epsilon*U-b+R-1)/R).

Its other factors are polynomials in k of degree at most a-1+c. Expanding S_u raises the floor degree to at most u+1, so total degree stays <=u+a+c<=5. Shifting the finite k interval to zero origin also preserves that bound. The newly proved degree-five single-floor recurrence therefore suffices symbolically for this half of (3). Degree four/five is not already callable in the frozen degree-three implementation.

The fine correction becomes a finite linear combination of

    Q[alpha,beta,gamma](N;m,c0;R,p,B0)
       =sum_(0<=j<N) j^alpha
          floor((j+c0)/m)^beta
          floor((p*j+B0)/R)^gamma.                    (4)

For y=y0+j, c0=y0+epsilon*m/2-zeta and B0=p*y0-zeta*V-b+R-1. Its initial indices satisfy alpha<=c-1, beta=a, gamma<=u+1 and alpha+beta+gamma<=5. If c=0 there is no fine correction. If a=0 this too is ordinary single-floor work. The genuinely mixed case remains (4).

This reduction isolates one unit-slope floor, rather than two independent slopes, and charges no scan of P/p or V/gcd(V,R). It does not establish that (4) can be evaluated by the current ordinary-floor routine.

## 3. Direct reduction of the particular ten-moment combination

There is a more focused alternative to expanding all ten inputs separately. Let B(z) now denote the compressed single-high-bit overlap on length C=HM, including its explicit empty endpoint B(C)=0. This B is different from the generic fine quotient B(x) in section 2; only the overlap meaning is used from this point onward.

On z=qM+s, 0<=s<M, the already proved period formula gives, with H-q denoted by Cq,

    B(z)=Cq*M+(1-4Cq)s,               0<=s<=m,
    B(z)=M(2-3Cq)+(4Cq-3)s,          m<=s<=M.          (5)

The pieces agree at m and with the next period at M. The original two-bit overlap has the stretch identity

    A_L(d)=(-1)^z[(V-t)B(z)-tB(z+1)],
    d=Vz+t, 0<=t<V.                                   (6)

For the proof only, extend this as a continuous, piecewise linear function of real d in [0,L], with value (-1)^z V B(z) at each knot Vz. This is an exact symbolic interpolation of the original integer formula, not a floating evaluation or an altered propagator.

Its initial value is L and its initial slope is

    s0=-(B(0)+B(1))=4H-1-2C.

At an interior knot Vz the right-minus-left slope jump is

    kappa_z=-(-1)^z[B(z-1)+2B(z)+B(z+1)]
           =-4(-1)^z B(z)-(-1)^z Delta2B(z).           (7)

Away from z=l*m, B has the same affine piece on [z-1,z+1], so Delta2B=0. For 1<=l<=2H-1, compare the adjacent slopes in (5):

    Delta2B(l*m)=4(-1)^l(l-2H).                        (8)

Indeed l=2q+1 gives 8(H-q)-4 at a half-period; l=2q gives -8(H-q) at a period boundary. Since m is even, (-1)^(l*m)=1. No endpoint jump at z=0 or C is included.

The standard hinge expansion follows directly by matching the initial value, initial slope and every slope jump:

    A_L(d)=L+s0*d+sum_(1<=z<C) kappa_z (d-Vz)_+,
    x_+=max(x,0).                                     (9)

It is an identity on [0,L]. Only d<L is sampled. A term exactly at d=Vz is zero; it is not an evaluation of a nonempty overlap beyond its support.

Define the common truncated progression kernel

    G(theta)=sum_(0<=j<n) (d_j-theta)_+.

For theta<=b it equals n(b-theta)+R*n(n-1)/2. For theta>D it is zero. For b<theta<=D, let

    J=ceil((theta-b)/R) in [1,n-1].

Then

    G(theta)=(n-J)(b-theta)
                 +R[n(n-1)-J(J-1)]/2.                (10)

At theta=D the value is zero even though its J is n-1. One may include that zero term or explicitly omit it with a typed endpoint proof. The general clamped definition is J=max(0,min(n,ceil((theta-b)/R))); the three ranges above are the justified way to avoid negative heights. No formula for an unclamped negative J is used.

Substitute (7)-(8) into (9), then interchange finite sums. Since G vanishes beyond D, the whole original progression sum is exactly

    sum_j A_L(d_j)
      =nL+s0*sum_j d_j
        -4 sum_(z=1)^floor(D/V) (-1)^z B(z) G(Vz)
        +4 sum_(l=1)^floor(D/U) (-1)^l(2H-l)G(Ul).     (11)

This is a reduction of the actual linear combination (6) of PERIOD_EXTENSION, not a request for every universal mixed moment. Its endpoint term uses sum_j d_j=nb+R*n(n-1)/2. Both knot ranges are valid interior ranges because D<L: z<=C-1 and l<=2H-1. No long knot range in (11) is claimed free to enumerate.

### The coarse correction is already an ordinary degree-three problem

Split its l range at floor(b/U) and then by parity l=2j+nu. This is a fixed two-way parity split, not a split into U or P residue classes. In the prefix theta<=b, G(Ul) is linear in l. In the active range it is a polynomial in l and

    J=floor((U*l-b+R-1)/R)

of total degree at most two. Multiplication by 2H-l raises that bound to three. Thus each active parity subsequence needs one ordinary degree-three table; prefix terms are polynomial sums. Ranges and parity counts must be computed exactly. This part can in principle use the actual existing degree-three family, but no execution has been performed here.

### The fine correction reduces to at most four auxiliary parameter families

Split z at floor(b/V) and by z=2y+nu. The parity sign is then the fixed sign (-1)^nu. Define

    q=floor(z/M), delta=floor((z+m)/M)-q.

Collecting (5) in global z gives

    B(z)=M[H+(4H-2)q-4q^2
               +delta(2-4H+(8-8H)q+8q^2)]
          +[1-4H+4q+delta(8H-4-8q)]z.                 (12)

The same-scale indicator products q^a*delta can be replaced by neighboring coarse-floor power differences through degree three, exactly as in the frozen proofs. On each parity subsequence,

    q=floor(y/m),
    q+delta=floor((y+m/2)/m),
    J=floor((p*y+V*nu-b+R-1)/R).                      (13)

In the prefix Vz<=b, G is linear in z. Hence (12) times G is an ordinary single-floor polynomial of total degree at most four after removing delta. This is symbolically covered by the degree-five extension, not by a claim that the old degree-three API already supplies it.

In the active range b<Vz<=D, (10) is quadratic in z,J. Therefore the remaining terms are of type (4), with total degree at most five, initial alpha<=2, beta<=3, gamma<=2. There are only two parity choices and two coarse offsets 0,m/2: at most four auxiliary parameter families for one original progression (with finite interval shifts absorbed into c0 and B0). This counts parameter families, not four primitive operations or four already available tables. The individual indices and coefficients are a fixed expansion independent of H,m,V and R. The two modular orientations still must both be retained; their counts are not included in this one-progression bound.

Thus the special combination has a concrete remaining kernel: a piecewise affine overlap envelope times a quadratic threshold sum. The coarse correction closes with the current mathematical degree-three contract, and the fine-prefix correction with the proved prospective degree-four/five contract. Only the active fine correction needs the mixed unit-slope interface.

## 4. Why a bounded moment list is not yet a descending algorithm

For (4), ordinary quotient/remainder normalization of p and B0 modulo R gives

    floor((p*j+B0)/R)=A*j+B+floor((a*j+b0)/R),
    0<=a,b0<R.

Expansion preserves total degree five. It can introduce larger alpha than the initial subset, so a simultaneous backend should allow the full degree-five family (at most 56 index triples). Likewise normalizing c0 modulo m is harmless. These are finite algebraic rewrites, not a proof of recursive progress.

Transposing the second floor of (4) evaluates the first near thresholds (R*y-b0)/a. This introduces a coarse denominator m*a together with denominator a. Without prior reduction, a=p may occur, and m*a=mp=P restores the original large dyadic scale. In particular the allowed symbolic regime p<R<P makes p normalization do nothing. A second transpose can return to denominators (P,p) and slope R, with boundary-shifted offsets. A measure based only on the displayed maximum denominator therefore has not decreased. Cache lookup can detect repeated parameter states, but does not produce their unknown values.

When normalization replaces p by a<p in some branches, m*a is smaller than mp. That is a genuine local improvement, but it is not a global argument: after transposition offsets and other parameters have changed, and not every allowed input enters such a branch. No policy of alternating these identities has been proved acyclic here. A fixed number of children at each node would also be insufficient by itself; a binary recursion with logarithmic depth can still have polynomial-in-scale rather than polynomial-in-bit-length leaves unless states merge with a proved bound.

Accordingly, neither formula (3) nor (11) is presented as a completed polynomial-bit mixed evaluator. They are exact transformations and precise interface reductions. They do not prove that the mixed problem is hard, that these moments are algebraically independent, or that a different cancellation cannot close the special combination.

## 5. Minimal continuation contract and evidence boundaries

A focused next mathematical target is an evaluator for (4), with strict N>=0, m>=1, R>=1, p>0, signed c0/B0 and fixed total degree <=5, plus a proof that its number of distinct parameter states is polynomial in input bit length. The initial special-combination calls have the narrower indices and dyadic m,p specified above. Generalizing inputs may be convenient for closure, but cannot substitute for proving it.

A satisfactory recurrence must state its exact endpoint convention, normalization, child parameters, a well-founded decreasing measure, and an aggregate state-count bound. An alternative is an algebraic elimination of only the fixed linear combination in (11). Merely invoking a fixed-dimensional counting theorem, enumerating V/gcd(V,R), or traversing all P/p periods is not such a recurrence.

The immediately implementable *new* part, after separate source review and typed execution authorization, is the single-floor degree-four/five extension proved by the coordinator. This note has not implemented it. A typed checker for (3) or (11) would be a bounded validation task, with actual paid endpoints, full signed receipts, exact halves, ordinary/mixed dependency pins and no host reference. It should distinguish proof-bound empty ranges from unevaluated missing mixed values, retain failed work, and never return an approximate answer under an exact schema.

For scalar modular correlation, the heads remain r and R-r (0 and R at r=0), with duplicate half-modulus orientations retained and original normalization 4^-g. Supplied R and any group address remain paid external information. These symbolic identities do not give unknown-order discovery, growing-mask compression, matrix-valued chronological correlation or full Shor sampling.

Global-Knowledge-Sync: main@6e443c7 / GLOBAL_KNOWLEDGE_V1
