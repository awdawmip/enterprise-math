# Bounded read-review of the reciprocal-D cutoff proof

Reviewed: `FINITE_RECIPROCAL_D_REFLECTION_AND_CM_CUTOFF_SOURCE.md`.
Status: PASS / NO CORRECTION NEEDED / ORIGINAL SCALAR COMPARISON OPEN.
This reviews the reflection domains, fixed-C endpoints, actual M_R
source, both partial Green normalizations, equations (15)-(16), cutoff
ranges and inherited corrections. It introduces no new research or
checker run. The main 52 and independent 38 checks remain the reported
verification.

The eta/e reflection uses precisely eta_1,...,eta_N and e_0,...,e_(N-1).
Its ratio propagation stops at j=N-2, so neither eta_0, t_(N+1) nor e_N
is introduced. The actual first endpoint eta_1=1/40 fixes eta_N e_(N-1),
and the reflected C coefficient gives cbar_(N-1)=-1/5. The separate
cbar_N=0 degree convention correctly handles the zero forward coefficient
in the last row. The reciprocal all-row source product is 1/72, giving
the prescribed forcing 1/9 after the factor 8; it requires no e_N.

The finite C double-prefix exchange and literal old binomial reduction
are consistent with the fixed carrier. In particular
(-1)^r binom(N,r)=(1/2)_r/r! on 1<=r<=N, with unit factorial divisors,
so the asserted old weight is 4t_r and stays nonzero at r=N. No
individual original and connected partial polynomial is equated by this
weight identity; their full carrier value is the same fixed C.

The actual M_R source retains its original triangle and every r=1,m
endpoint. Its q_r is the unchanged W_m/g term minus the literal OLD-R
coefficient tail. At r=m it is t_m(1/g-a_m), exactly the last prefix
diagonal. At r=1 the omitted-low-index contribution is preserved. The
CM rewrite with +P_r has the correct sign. All r t_r divisors are units,
and no new D_0 or Z_(m+1) term occurs.

The original partial Green source in (11) has the correct negative
coefficient and the zero endpoint w=0. At CM its boundary has factor
1/4, so integration gives the positive 1/9 in (12). Its first resolvent
value Q_1=(9/10)V'_* follows from D_1=1/10. The stated resolvent
recurrence follows by subtracting adjacent partial K polynomials and
using D_r r^2 d_r=2^(r-1)/18; it has the correct V'_*/2 source and
uses no Q_0.

The connected source in (13) has coefficient -1/72. Its correct upper
normalization is z=1; the separately displayed value -eta_r/2 at z=0
is correctly retained rather than silently set to zero. This endpoint
orientation gives the negative 1/18 in (14). Both partial concomitants
have degree at most m+r<=4m<p and all actual i+r denominators are units,
including r=N. No C or derivative inverse is used.

The cutoff split is exact: r<=m maps to 2m<=s<=N-1, while m+1<=r<=N
maps to 0<=s<=2m-1. Both are retained in (15). Since
tau=2eta_N V'_*(C_tail+C_prefix), the subtraction M_R-3tau produces
the factor -6V'_* in both ranges. Moving this proved combination into
the prior residual gives precisely (16), with no missing factor 2 or g.

The earlier odd degree-p term, cubic x^p correction and full finite-log
complement remain in their preserved dictionaries. The degree<p partial
Green identities correctly claim no removal of those corrections. The
paper leaves F_CM and all remaining pairings unevaluated and states no
zero/nonzero scalar residual. Literal g and all OPEN parent boundaries
are consistent throughout.
