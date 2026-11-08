# R5: Complete variable-kappa low-t prism by a two-chart Blackwell seam

Date: 2026-11-08. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Exact model and claim

Continues PR #1814, frozen author-side scientific commit d3f643927a4b34fa64c9318c2d13790f1537937e. Frozen source pins remain global a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. P000 and the native X6 foundation are unchanged. This is a seven-node P/Q-BRC terminal observer theorem under its inherited declared semantics.

Use likelihood ratios r=(1/10,1/2,3/4,1,5/4,3/2,19/10), Q mass map M, terminal readout (eP,eQ,TP,TQ), and the physical capacities and seedless constraint 9*b*z=4*a*(v-z) from PR #1814. Define T=1/50, P=77/152 and D=17/2112.

THEOREM: For **every real** 0<=t<=T, 0<=p<=P, D<=q<=1, 0<=theta<=1 and 0<=kappa<=1, the lawful FULL_HIST source

    x=(1,t,1, (13*t/40+1/80)*p,
       9*kappa/40+t*theta/10,
       (3*t/40+21/80)*q, t*theta/10)

admits a lawful seedless LR target y and nonnegative 7-by-7 declaration-independent Blackwell transfer Q satisfying, for every i,j=0,...,6,

    sum_j Q[i,j]=M_i(y),
    sum_i Q[i,j]=M_j(x),
    sum_i r_i*Q[i,j]=r_j*M_j(x),
    TP(y)=TP(x), TQ(y)=TQ(x).

This yields the identical four-dimensional terminal readout for **every** randomized seven-node terminal declaration. For all real h in [0,1], the line (1-h)*x+h*y has the same target observation, using transfer (1-h)*Q+h*diag(M(y)).

Unlike PR #1814, which proved kappa<=19/20, this covers the **full kappa interval [0,1]** simultaneously with the other four old parameter bounds.

## Explicit shared seam

Set

    s(t,theta)=1-t*(37/18+4*theta/9).

For 0<=t<=1/50 and 0<=theta<=1, 19/20<=s<=1. Write X0=x(...,kappa=0), Xs=x(...,kappa=s), X1=x(...,kappa=1).

The previous G chart is

    G(x)=(1,0,1,u+23*t/160,v+37*t/80,w-17*t/160,0).

Its seam target is

    G(Xs)=(1,0,1,u+23*t/160,9/40,w-17*t/160,0),

because v(Xs)=9/40-37*t/80. Thus G(Xs) simultaneously lies on the *linear* F face

    F={g=b=1, z=a/10, v-z=9/40}.

The eight new seam rational transfer supports at t=T, p∈{0,P}, q∈{D,1}, theta∈{0,1} are contained in VERIFY_EXACT.py. The eight previous kappa=0 exact supports are copied and independently rechecked. At t=0, all anchor flows are already seedless and use exact diagonal transfers.

## Explicit F-face target for kappa=1

Define beta=p/P, and

    a1=t*[theta+(1-theta)*(7/8+(3/40)*beta)],
    v1=9/40+a1/10, z1=a1/10,
    da=a1-t, dv=v1-v(X1).

Choose

    Y1=(1,a1,1, u(X1)-3*da/8-dv/2,
        v1, w(X1)-da/8-dv/2, z1).

All Y1 belong to the same linear seedless F face. Both stopping-time differences vanish: setting dA=a1-t and dV=v1-v(X1), the identities dU=-3*dA/8-dV/2 and dW=-dA/8-dV/2 solve both linear time-preservation equations exactly.

At t=T, theta=0, p=0, a1=7/400; at p=P, a1=19/1000. At theta=1, a1=t and Y1=X1 (the source is already seedless), hence the diagonal transfer. Eight t=T F-face corner certificates are reconstructed and checked in the verifier. At t=0, Y1=X1 is also seedless.

## Exact multiaffine extension and stitching

For each anchor kappa=0, kappa=s, kappa=1 separately, the source and chosen target are separately affine in each of the four parameters (t,p,q,theta). The source masses, target masses, kernel equalities, target capacities and stopping times are linear in those flow coordinates. Therefore the usual nonnegative 16-corner multiaffine weights give a legal target and nonnegative transfer for every real t,p,q,theta. The G anchor targets stay on the linear G face {a=z=0}; F anchor targets stay on the linear F face {z=a/10,v-z=9/40,b=1}. In particular, the seam target is on *both* faces.

For t>0, if kappa<=s put lambda=kappa/s and interpolate (X,Y,Q) between the kappa=0 and kappa=s anchor triples. The resulting Y stays on G and satisfies the seedless equation.

For t>0, if kappa>=s put lambda=(kappa-s)/(1-s) and interpolate (X,Y,Q) between the seam triple and the kappa=1 triple. The resulting Y stays on F and satisfies the seedless equation.

Both interpolation weights lie in [0,1]. The source is affine in kappa, so the interpolated X is exactly the requested source. The seven row equations, fourteen column/moment equations, both stopping-time identities and physical capacity inequalities persist under nonnegative interpolation. At t=0, x is itself seedless for every kappa and uses the identity transfer. This proves the theorem for all real points, including irrational parameters and all boundaries.

## Exact certification and reproducibility

The standalone VERIFY_EXACT.py contains all 8 historical kappa=0 sparse supports (four patterns reused at two theta corners), the 8 new seam sparse supports and the 8 kappa=1 supports, as well as an exact Fraction-only rational linear solver. It reconstructs each corner's unique positive transfer, then verifies 7 target row equations, 7 source Q columns, 7 source P-weighted columns, lawful capacities, seedless, P/Q mass normalization, and both stopping-time equations.

New t=T seam/F anchors: 16 rational kernels, 167 strictly positive nonzero entries in total; minimum strictly positive entry 107/8437500. Exact checks of 161 rational mixed-domain parameters, 100 additional strict-F-region rational points and the relevant seam/end boundary corners all passed in local execution. SciPy was used only to discover supports; the published verification path needs standard-library fractions only. These finite checks verify the explicit rational certificates; the universal real extension is the algebraic interpolation proof above.

The previous kappa=19/20 barrier was a capacity face of the specific a'=z'=0 G target; the new F construction realizes the whole residual kappa interval with a'>0 and z'=a'/10 where appropriate.

## Next question and operational state

Next test expansion beyond p=77/152, below q=17/2112 and above t=1/50 using a third exact face or a larger two-face overlap. Keep source evidence, independent review and formal result admission separate; no native Task CLAIM is asserted by this author-side publication.
