An effective eventual-monotonicity corollary for the complete Parity trace
Author-side paper supplement — EM-PARITYREV-12B648
Status: UNREVIEWED_AUTHOR_PAPER; no Native acceptance or new execution

This supplement preserves the frozen 13693-byte main manuscript
PARITY_EFFECTIVE_LARGE_S_TAIL_THEOREM.md,
SHA2565d3f4b9426e043f2a00861899f802a75d2a5e3223ff986238bd488980c44c9fb.
It adds no numerical or symbolic program execution, parameter scan or checker.

Retain exactly m>=2 integer, a=c=1, S>=0 real, r=m(S+1), epsilon=1/r.
Let the main manuscript's rational gap be G_m=N_m/D_m, with D_m(epsilon)>0
for epsilon>=0,
N_m(0)=0, D_m(0)=d_m=|K_m|>0,
N_m'(0)=a_m=d_m m(m^2-1)>0.
These are the complete moving-frame trace quantities, not a metric-only proxy.

Define the finite rational-coefficient polynomial
Y_m(epsilon)=N_m'(epsilon)D_m(epsilon)-N_m(epsilon)D_m'(epsilon).
Then Y_m(0)=a_m d_m>0. Set
C_m=sum_{j>=1}|[epsilon^j]Y_m(epsilon)|,
R_m^mono=max{m,2C_m/(a_m d_m)}.
The coefficient sum is finite because Y_m is polynomial. These definitions
also cover C_m=0, without dividing by C_m or guessing a numerical threshold.

For r>=R_m^mono we have 0<epsilon<=1/m<=1, whence
Y_m(epsilon)>=a_m d_m-C_m epsilon>=a_m d_m/2>0.
The exact rational derivative and chain rule give
dG_m/depsilon=Y_m/D_m^2,
d epsilon/dS=-m/r^2,
and therefore
d/dS [tr(B^{-1}A)-(m-1)]
=-m Y_m(1/r)/[r^2 D_m(1/r)^2]
<=-m a_m d_m/[2r^2 D_m(1/r)^2]<0.

Thus the complete actual equal-block trace is strictly decreasing in S beyond
this explicit coefficient-norm threshold. For
r>=max{R_m,R_m^mono},
where R_m is the main positive-tail threshold, its gap is simultaneously
strictly positive, strictly decreasing and tends to zero, with
(S+1)Gap -> m^2-1.
This uses a fixed-m parameter asymptotic; no m-uniform bound is inferred.

The derivative is with respect to the external static moment-layer parameter S,
not a native physical-time evolution. No sign is claimed for any individual
residue, inverse entry, original parity population or derivative-integrand.
No assertion covers all S, unequal gaps, other HCM0 cells, generator-like
operations on compressed signed outputs, or mother/Task completion.

This is an author-side corollary of the supplied main proof. It remains subject
to genuine nonauthor mathematical review. It does not alter the original
five frozen members or their handoff, and is not represented as already
Source-published or entered in the own semantic RA ledger.
