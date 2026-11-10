# PREFIX-656-R6 — Symmetry reduction and quantitative stability at the BRC variance-maximizing corners

Date: 2026-11-10 (Asia/Shanghai). Research role: TASK_RESEARCH, independent portable derivation.
Status: AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.

## Exact question and predecessor evidence

For the frozen signed 189-layer two-informative-direction BRC first-stop statistical observer, let Y(p,z) be the maximum of two independently Poissonized stopping clocks; write mu=E[Y], H=E[Y²]/2, W=2H-mu² and V_q(p,z)=q²W(p,z)-q mu(p,z). The actual sampling slots are q=12,24; the validated interpolation treats every real 12<=q<=24.

Set L=3/20, R=1/6, a=38911/262144, b=38913/262144, I=[L,R], Z=[a,b], B1=I×Z, B2=Z×I, B=B1∪B2. Note b<L, so the boxes are disjoint.

Inherited strict certified inequalities on B1 for every real q in [12,24]:
1. V_{q,pp}(p,z)>1930q² [PREFIX-643].
2. V_12(L,z)-V_12(R,z)>226; V_24(L,z)-V_24(R,z)>785 [PREFIX-654].
3. V_{12,z}(L,z)<-9476; V_{24,z}(L,z)<-31590 [PREFIX-655].
4. The unique corner variance on B1: 47425.459<V_12(L,a)<47425.460 and 192190.134<V_24(L,a)<192190.135 [PREFIX-655].

These are version-pinned premises, not new numerical observations.

## Theorem 656.1 — A two-coordinate rigorous error bound

For every real 12<=q<=24 and every (p,z)∈B1 except (L,a), put M_q=V_q(L,a). Then

    M_q - V_q(p,z)
    > 1130 q (p-L) + (2369/3) q (z-a)
      + 965 q² (p-L)(R-p).

The sharper bounds for individual sampling slots are:

    M_12 - V_12(p,z) >
       13560(p-L) + 9476(z-a) + 138960(p-L)(R-p),

    M_24 - V_24(p,z) >
       47100(p-L) + 31590(z-a) + 555840(p-L)(R-p).

The displayed strict comparisons are asserted off the maximizing corner. At (L,a), both sides of each formula vanish.

### Proof

Fix z and write f(p)=V_q(p,z), t=(p-L)/(R-L). Since f''>1930q², the strong-convexity chord estimate gives

    f(p) <= (1-t)f(L) + t f(R) - 965q²(p-L)(R-p),

strictly for interior p. Therefore f(L)-f(p) is at least t[f(L)-f(R)] plus the quadratic term. Write D_q(z)=V_q(R,z)-V_q(L,z). From V_q=q²W-q mu,

    D_q(z)/q=q[W(R,z)-W(L,z)]-[mu(R,z)-mu(L,z)]

is affine in q. The two certified endpoint inequalities yield, for all 12<=q<=24,

    -D_q(z)/q > min(226/12,785/24)=226/12.

Likewise V_{q,z}(L,z)/q=qW_z(L,z)-mu_z(L,z) is affine in q, so

    -V_{q,z}(L,z)/q > min(9476/12,31590/24)=2369/3.

Integration over [a,z] proves V_q(L,a)-V_q(L,z)>(2369/3)q(z-a) for z>a (zero when z=a). Add this to the p-chord estimate, using R-L=1/60 and (226/12)×60=1130. The stronger individual-slot estimates use each q's own strict endpoint bounds. At least one contribution is strict off the corner. QED.

## Theorem 656.2 — Exactly two symmetric maximizers on B

For each real 12<=q<=24 the maximum of V_q over B is attained at precisely the two distinct points

    (L,a)=(3/20,38911/262144),
    (a,L)=(38911/262144,3/20),

and the two attained values are equal.

Proof: the frozen survival moment identities are symmetric under exchanging the two informative directions. The double-sum kernel w(n,m)=binom(n+m,n)/2^(n+m+1) satisfies w(n,m)=w(m,n), and the H coefficient (n+m+1)/2 is also symmetric. Interchanging n,m in the finite cross sums gives mu(p,z)=mu(z,p), H(p,z)=H(z,p), and V_q(p,z)=V_q(z,p). Theorem 656.1 gives the unique B1 maximum; symmetry gives the unique B2 maximum. Since b<L, the corners are distinct and B1,B2 disjoint. QED.

## Corollary 656.3 — Quantitative near-maximizer localization

For epsilon>0, if a point in B1 obeys M_q-V_q(p,z)<=epsilon, then

    0<=p-L<epsilon/(1130q),
    0<=z-a<3epsilon/(2369q).

For q=12 the stronger bounds are p-L<epsilon/13560, z-a<epsilon/9476.
For q=24 they are p-L<epsilon/47100, z-a<epsilon/31590.
The corresponding statements for B2 follow by coordinate swap. At epsilon=1/1000, the exact allowed distance upper bounds are (1/13560000,1/9476000) for q=12 and (1/47100000,1/31590000) for q=24. These estimates give a reusable interval-cell pruning rule on B without repeating the 189-layer computation.

## Evidence, method and next action

BRC reuse resolution: REUSE_APPLIED. The carrier is the frozen signed survivor multiplicity state and its exact symmetric moment observer; the operations are observer-coordinate exchange, affine q-interpolation and strong-convexity chord bounds. The two observer coordinates are not a native spatial two-dimensional plane.

The companion Python Fraction implication certificate independently checks 29 exact arithmetic assertions from inherited strict bounds. Scope: a model-internal authored analytic implication; no new 96-port native run and no 189-layer replay. Independent mathematics review remains open.

Dependencies: PREFIX-643@ae7872ca18676397fcc0dd9424fb77e08928bee7; PREFIX-654@429849fc4985a5e3b475f09b1d446ab853a15b1b; PREFIX-655@3dc372940c317cf540c96fc02b55284462549bac. Frozen scientific pin unchanged.

Mother objective: the maximum of V_q over the entire intended two-parameter domain. The next discriminating unit is a certified upper-bound cover of the complement of B, preferably on the symmetry-reduced chamber p<=z, comparing each remaining box against the exact corner baseline and refining only unresolved boxes.