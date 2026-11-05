# R5: rational face-stationary certificates for the single quadratic likelihood-ratio gate

Date: 2026-11-06 (Asia/Shanghai)
Classification: AUTHOR_PROVED / EXACT_MODEL_SPOTCHECK / UNREVIEWED / PORTABLE_ONLY.

## Objective and inherited exact input

R5 mother target: find a strictly positive rational finite P/Q stopping tree whose four-observer FULL_HIST and seedless LR convex hulls coincide but whose actual real-behavior observation images differ. Retain frozen scientific pins GLOBAL \`a01383f825ef9d43b4b754254303298c64041568\`, EM \`86149263e38c22292c9def1e0f69092efa1be77e\`. This paper is about an auxiliary likelihood-ratio/BRC observer, not native X6 dynamics. Continue EM \`57f7d654e5dd002567e0b0d333937e6e38f3b4cb\` (the scalar gate), with earlier exact convex-hull evidence \`fed51a882c12831a889cd5437da5d1dc564fd673\` as author-side predecessor.

For the fixed delta=1/4 tree, let v=(g,u0,u1,X0,X1,X2,J), A=u0/10, B=9u1/40, alpha=47/180, beta=67/162. For each observed W=(eP,eQ,TP,TQ), the predecessor constructs a *bounded rational polytope* K(W) from affine flow bounds, two time equalities, four central-split inequalities, and fourteen zonotope halfspaces. In that model:

    W in O4(FULL_HIST)  iff K(W) is nonempty,
    W in O4(seedless LR) iff some v in K(W) has F(v)=0,
    F(v)=(A+B)J-X1(alpha*A+beta*B).

The issue is exact global sign testing of this one rational quadratic over K(W).

## Theorem 1: rational quadratic extrema have rational witnesses

Let K be any nonempty bounded rational polytope in R^n, possibly lower-dimensional, and q(x)=1/2 x^T H x+c^T x+d a quadratic polynomial with *rational* symmetric H,c,d. Both min_K q and max_K q are rational numbers, and each is attained at a rational point of K.

Proof. Choose an actual minimizer x. Let G be the unique minimal face of K whose relative interior contains x, and choose a rational basis B_G for the tangent space lin(G-G). Since x is relatively interior to G, for every tangent b, the directional derivative vanishes: b^T(Hx+c)=0. Thus x is in

    S_G={z in G : B_G^T(Hz+c)=0}.

S_G is a nonempty bounded *rational polytope* defined entirely by rational linear constraints; it has at least one rational point r. For any z,r in S_G, with w=z-r tangent to G,

    q(z)-q(r)=1/2 w^T[(Hz+c)+(Hr+c)]=0,

because each gradient annihilates all tangent directions. Hence q(r)=q(x)=min_K q is rational. Apply the same argument to a maximizer. This proof covers 0-dimensional faces and degenerate polytopes without genericity assumptions. QED.

**Exact algorithm.** Enumerate the finite faces G of K. For each, solve the *linear* rational feasibility problem S_G. On a feasible stationary face, evaluate q at any rational solution r_G. The smallest and largest of these exact rational values are the global extrema: they include actual extremizing faces and every candidate is feasible. A face need not be explicitly described as an irredundant facet list: enumerate active subsets of original inequalities and apply rational linear algebra and rational LP. This is a finite exact method, not a polynomial-time claim; face enumeration may be exponential and rational bit complexity remains relevant. Only rational linear feasibility plus rational arithmetic is required to decide the two signs.

## Theorem 2: exact rational-target R5 membership and quadratic-algebraic policy

Assume the inherited scalar-gate lift is exact for the fixed rational P/Q tree. Let W be a rational four-observer vector. There is a finite exact decision procedure for W in O4(FULL_HIST) and W in O4(seedless LR) using rational linear feasibility and face-stationarity, followed (for an attainable LR target) by a single polynomial root of degree <=2.

Proof. Build K(W) using rational coefficients. Its emptiness is rational linear feasibility. If nonempty, Theorem 1 supplies *rational* minimizer p and maximizer q of F. By continuity of F on the segment [p,q],

    W in O4(seedless LR) iff F(p)<=0<=F(q).

If either endpoint has F=0, use it directly. Otherwise F((1-t)p+tq) is a rational polynomial of degree at most 2 whose values have opposite signs at t=0,1. A root t in (0,1) is real algebraic over Q with degree at most 2. The corresponding v has coordinates in Q(t). The seven-ratio declaration constraints are linear with data in the same ordered field Q(t); their nonempty bounded fiber has a solution in that field by rational/ordered-field Gaussian elimination and linear feasibility. The reconstructed continuation and declaration action probabilities are also in Q(t), using arbitrary legal values on zero-mass keys. Thus every rational target in the LR image admits a legal strategy with action probabilities in a real algebraic extension of degree <=2. The algorithm decides membership over *all real behaviors*, not a fixed probability grid. QED.

The quadratic degree bound is genuinely useful: an arbitrary rational quadratic can have an irrational zero; q(t)=t^2-1/2 on [0,1] is a simple example. Rational *extremal certificates* remain available even in that situation.

## Theorem 3: existence of rational gap witnesses

For any finite rational P/Q stopping tree with unrestricted history-dependent behavior, O4(FULL_HIST) is a rational polytope (occupancy-mass linearization). The seedless LR real-behavior image is compact, being the continuous image of a finite product of closed action simplexes. Hence

    O4(FULL_HIST) \ O4(seedless LR) is nonempty
    iff some *rational* W is in that difference.

Proof. If x is a FULL point outside the compact LR image, it has an open neighborhood disjoint from LR. Rational points of the rational polytope FULL are dense in FULL, including within its faces (rational vertices and rational convex combinations), so one lies in that neighborhood. The converse is immediate. QED.

**Consequence.** For the fixed delta=1/4 model, a concrete rational target W with K(W) nonempty and *strictly positive min F* or *strictly negative max F* is a complete all-real image-gap certificate. An enumerated search over rational points is a semidecision method for image inequality; equality still requires a global argument. The prior equal-convex-hull claim is an independent inherited scientific dependency for the stronger R5 mother target.

## Exact model sanity check (not a gap claim)

With g=u0=u1=1, X0=X2=0, X1=13/80, put A=1/10, B=9/40. The FULL central-split constraints permit

    J_low=3367/64800, J_LR=143/2400, J_high=871/12960.

The scalar gate has the exact values

    F(J_low)=-3211/1296000, F(J_LR)=0, F(J_high)=3211/1296000.

With all stopped histories declaring Q, *all three* have the same four-observer target

    W=(eP,eQ,TP,TQ)=(1,0,253/80,253/80).

The terminal ratio masses are nonnegative, sum to 1 and have LR-weighted sum 1. The middle lift is an explicit seedless LR realization of W. This demonstrates why checking one arbitrary FULL lift with F != 0 is not an image-gap certificate: all feasible lifts K(W) matter.

## Validation, scope, and next research unit

VERIFY.py performs an exact symbolic face-stationarity enumeration on four low-dimensional rational polytopes (indefinite triangle, convex square with interior minimum, lower-dimensional line, and quadratic irrational root) and uses Fraction to verify the three fixed-model lifts and scalar residuals. Executed local output is in EXACT_OUTPUT.txt. Analytic Theorems 1-3 are independent of the enumerator; no 7D K(W) extremum was executed in this run.

Next: generate rational W in the inherited exact hull, assemble K(W), and implement a scalable exact active-face stationary search; output rational p_min,p_max plus rational active constraints or sign certificates. Prioritize rational targets in facet/interior regions away from earlier explicit reachable patches. A sign-definite F on K(W) closes the image-gap half of R5; exact sign crossings give explicit degree-2 LR strategies and can guide a global covering theorem. Preserve task/owner/claim authority and the frozen scientific pins.