# PREFIX-718-R6 — complementary terminal-influence certificate for the frozen Gamma maximum

Date: 2026-11-12 (Asia/Shanghai). Parent: PREFIX-675. Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Previous exact sources: PREFIX-710, 713, 714, 716, 717. Status: AUTHOR_PROVED / EXACT_INTEGER_GAMMA_PROBE / UNREVIEWED / NOT_ADMITTED.

**Scope.** The auxiliary observer D=[0,1/2]^2 with Y(p,z)=max(T_p,T_z), independent conditional Gamma(N_p,1) and Gamma(N_z,1) completion clocks. The correct Gamma maximum is used, not the stopping-count maximum. This is not an X6 native spatial plane.

## 1. Theorem: complementary endpoint lower slope

For a closed coordinate rectangle R=[a,h], write mu(x)=E[Y(x)], M2(x)=E[Y(x)^2], W(x)=M2(x)-mu(x)^2 and f_t(x)=W(x)-t mu(x), t>=0. Set m=mu(a), w=W(a), delta=mu(h)-m, B=M2(h)-M2(a). The preceding exact Gamma influence decomposition provides a positive starting-corner upper influence slope C>0:

    M2(x)-M2(a) <= C*(mu(x)-m).

Put u=mu(x)-m. The new ingredient is a **terminal** positive lower slope ell>0. For every x in R, the same frozen positive-influence decomposition along the path x -> h gives

    M2(h)-M2(x) >= ell*(mu(h)-mu(x)) = ell*(delta-u).

Consequently the true second moment obeys the two-sided envelope

    M2(x)-M2(a) <= min(C*u, B-ell*(delta-u)).

For any real t>=0 this yields the uniform closed-cell upper bound

    f_t(x) <= E_new,R(t)
       = w-t*m + max_{0<=u<=delta} {
           min(C*u, B-ell*(delta-u)) - (2*m+t)*u-u^2 }.

The earlier PREFIX-716 bound E_old,R(t) used min(C*u,B). Since ell>=0, E_new,R(t)<=E_old,R(t). Both inequalities are about the same exact Gamma-clock model.

**Derivation of ell, preserving the correct endpoint direction.** On the exact 384-grid, let a<=p<=b and c<=z<=d denote integer indices (physical parameters index/768). From the frozen Gamma survivor kernel, define the positive coordinate influence vectors
A_n(k)=LZ-K0[k][n] and H_n(k)=2(n+1)LZ-K1[k][n], n=0,...,188.
Both are nonincreasing functions of the *other* clock parameter by the existing coordinatewise survivor monotonicity. For indices u<=v define exact rational bounds

    rmax(u,v)=max_n H_n(u)/A_n(v),
    rmin(u,v)=min_n H_n(v)/A_n(u).

A positive coordinate update with the other clock within [u,v] has ratio (delta M2)/(delta mu) between rmin(u,v) and rmax(u,v), because its total is the nonnegative weighted sum of the 189 individual survivor increments. The earlier starting-corner upper slope can be selected as

    C=min(max(rmax(c,c),rmax(a,b)),
          max(rmax(a,a),rmax(c,d))).

For the **terminal x->h segment**, choose the lower slope

    ell=max(min(rmin(c,d),rmin(b,b)),
            min(rmin(a,b),rmin(d,d))).

These two minima correspond to updating p first or z first, respectively. Both full coordinate-update paths are admissible for every x in R; taking the maximum preserves a valid lower bound. This terminal formula differs from the initial-corner lower slope. Exact checks confirm 0<ell<=C and ell*delta<=B<=C*delta for every tested rectangle.

## 2. Finite exact optimization and real-q coverage

The function of u inside E_new,R is a continuous concave piecewise quadratic. Its only affine-piece breakpoint when C>ell is

    u0=(B-ell*delta)/(C-ell),

which belongs to [0,delta] by the endpoint inequalities. Its maximum is exactly the maximum over endpoints u=0,delta, breakpoint u0, and any in-range vertices (C-2*m-t)/2 and (ell-2*m-t)/2. The equality case C=ell is a single quadratic piece.

Two actual feasible comparator points are e_A=(0,149/1000) and e_B=(0,146/1000). Their exact Gamma witness functions cross at rational t*=(W(e_A)-W(e_B))/(mu(e_A)-mu(e_B)) in (23/100,24/100). By PREFIX-717's convex-envelope theorem, strict comparison of max(f_t(e_A),f_t(e_B))-E_new,R(t) at t=0, t=t*, and t=1/2 certifies all real 0<=t<=1/2, hence all finite real q>=2.

## 3. Completed frozen-science computation

The local Python Fraction implementation reconstructs 189 stopping-survivor rows, including exactly 9,529 nonzero coefficient cells, with the original fixed width predicate from frozen input f42f2906d77f24085c123f3ccfe9667d41caa96d. It reuses the corrected exact Gamma two-clock moment kernel and moment influences of PREFIX-716. The published self-contained checker is constructed from the immutable PREFIX-716 script plus the new terminal-sloped certificate.

Two disjoint, bounded windows of 384x384 fine-cell indices were scanned, with no floating-point admission check:

- Window A: [36,48) x [110,123), 156 candidate cells, 28 new half-square certificates.
- Window B: [25,56) x [123,141), 558 candidate cells, 47 new half-square certificates.

A new cell is recorded only when the preceding *two-witness old coupled* envelope has at least one nonpositive comparison at the three exact witness-switch points, while the new envelope is strictly below the feasible comparator at all three points. The 75 exact representatives are in PREFIX718_R6_RESULTS.json, with complete list digest 31a2225e3da3c3c35515caddd297eeb3e66942062ae5ecb5a980c507cfa97cf1. Symmetry of the independent clocks gives 75 additional reflected ordered cells, totalling **150**.

These cells are disjoint from the PREFIX-712 base because its box upper bound is weaker than E_old while its e0 comparator is no stronger than the two-witness maximum; they are disjoint from the PREFIX-713 original e0 coupled cells and the PREFIX-716 e_A coupled additions by the same nonpositive old gap witness. The separate PREFIX-713 multi-competitor 20 all-q cells are checked for exact coordinate disjointness. Therefore the inherited 138868 ordered all-q cells plus these 150 new cells yield

    certified cells >= 139018 of 147456,
    certified relative area >= 69509/73728 = 94.27761501736111...%.

The smallest new three-point gap in the exact tested set exceeds 130048/1000000, yielding for each new closed cell and every real q>=2 a feasible comparator e(t) with

    V_q(e(t))-V_q(x) > (130048/1000000)*q^2.

This is an author-checked area lower bound, not an exhaustive location of the mother objective's global maximum. The exact local runner returned ALL_CHECKS_PASS PREFIX718-R6 with counts 28 and 47; the separate remote CI workflow has not been executed during this publication.

## 4. Preservation, claim boundary, and next step

Deliverables: this proof, PREFIX718_R6_TWO_SIDED_GAMMA.py (full stand-alone exact reproducer), PREFIX718_R6_RESULTS.json (75 coordinates, scope and counters). Prior mathematical source remains frozen. These are plain research-source artifacts and do not assert an authenticated shared-task CLAIM, new formal Result/Review, or theorem admission.

Next: extend this terminal-influence certificate to nearby unexcluded cells and refine near the transition between strict exclusion and possible maxima, then use exact boundary derivative or root-isolation arguments to solve the actual PREFIX-675 global optimizer problem.