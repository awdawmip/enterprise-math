# R5 supplement — exact two-dimensional tail-declaration lift from a negative-residual corner

This addendum *continues* `RESEARCH.md`, whose all-real pointwise single-process lift covered all `R=9bz-4a(v-z)>=0`. It treats a substantial family from the previously unresolved `R<0` sector without asserting global image equality.

**Theorem (all-real two-dimensional rectangle):** Consider the FULL_HIST flow
`x=(g,a,b,u,v,w,z)=(1,1,1,0,9/40,0,0)`.
It has `R=-9/10` and `T_P=T_Q=129/40`. Let its seven declarations be zero except `d_0=s`, `d_6=t`, with arbitrary real `s,t in [0,1]`. Every resulting four-observer point is achievable by one seedless LR process, simultaneously for the full real rectangle `[0,1]^2`:

`W(s,t)=(1-(67/720)(s/10+19*t/10), (67/720)(s+t),129/40,129/40)`.

**Constructive proof:** The frozen affine mass formulas give `M_0(x)=M_6(x)=67/720`. Choose the different seedless flow
`y=(1,19/20,19/20,0,11/40,0,11/130)`.
All legality inequalities hold, `9*b*z=4*a*(v-z)`, and the two times are `T_P=T_Q=129/40` again. Direct calculation yields `M_0(y)=M_6(y)=121/1200`. Thus the ratio
`q=(67/720)/(121/1200)=335/363` belongs to `(0,1)`.
Set seedless declarations `d'_0=q*s`, `d'_6=q*t`, all others zero. Then the new Q error and P-weighted Q error coincide with the original because the same LR=1/10,19/10 tail nodes are used and their masses have been increased by the factor `1/q`. Both times coincide by construction. This is a direct all-real two-parameter algebraic identity, and neither convexification nor an external random mixture is used.

**Scientific consequence:** Even the R<0 history-extreme corner does not automatically supply a nonconvex four-observer separation. Its entire two-tail declaration rectangle is explicitly contained in the seedless image at the same times. Crucially, this lift **changes the early flows** `a,b,v,z`, unlike the fixed-early-flow correction in `RESEARCH.md`. Hence the next nonconvex search must allow *all* early seedless flows to adjust.

`VERIFY_REVERSE.py` executes exact `Fraction` checks of legality-relevant equalities, moment/timing identities, exact masses, the declaration scale, and 16 sampled rational pairs as diagnostics. `OUTPUT_REVERSE.txt` is the captured stdout. The all-real claim follows from the displayed linear identities, not the 16 sample checks.

**Next unit:** move beyond the two extreme-node declaration rectangle at the reverse corner. Include central/intermediate node declarations and impose the full four-observer vector plus legal seedless bilinear constraints. Either find a valid explicit seedless lift or a global exact polynomial infeasibility certificate. Distinguish observer pointwise image equality from previously proved convex-hull equality, and preserve the current frozen scientific pins. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.