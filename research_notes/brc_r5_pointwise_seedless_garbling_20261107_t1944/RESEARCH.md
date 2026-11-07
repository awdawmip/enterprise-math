# R5 — Exact pointwise seedless lifts from explicit two-measure transports

Date: 2026-11-07 (Asia/Shanghai). This author-side result continues PR #1767 at predecessor commit f20b9a0bdc8c1fc8f69a2abeb7c231181d1a0d27 (four-observer convex-hull equality). Frozen scientific inputs remain GLOBAL a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. Current behavioral sources, ACTIVE worldview and P000 were read separately. STATUS: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Frozen model

A legal FULL_HIST flow x=(g,a,b,u,v,w,z) satisfies 0<=a,b<=g<=1, 0<=u<=13a/40+b/80, 0<=w<=3a/40+21b/80, 0<=z<=a/10, and 0<=v-z<=9b/40. Seven likelihood ratios are r=(1/10,1/2,3/4,1,5/4,3/2,19/10), with Q stopping masses M_0,...,M_6 given exactly in VERIFY.py, following the predecessor's pinned formulas. Both Q and P stopping masses are normalized, with P mass r_j*M_j at key j. For declarations 0<=d_j<=1, e_Q=sum_j M_j*d_j, 1-e_P=sum_j r_j*M_j*d_j, and W=(e_P,e_Q,T_P,T_Q). The seedless-LR condition is 9*b*z=4*a*(v-z); FULL_HIST allows the two history split rates independently.

A single-process lift is one legal seedless flow y and one seven-component declaration vector d' producing exactly the same W, without a mixture over multiple seedless strategies. In each theorem below, the seedless flow y depends only on x, while d' is constructed linearly from d through an explicit nonnegative two-measure joint-mass transport.

## Theorem A — general nonnegative-residual region has pointwise seedless lifting

For EVERY real legal FULL_HIST flow x satisfying R=9*b*z-4*a*(v-z)>=0 and EVERY real declaration vector d in [0,1]^7, there is one legal seedless-LR strategy (y,d') with W(y,d')=W(x,d). This includes a=0, b=0 and g=0 boundary cases.

Let c=a/10+9b/40. If c=0, a=b=v=z=0, and x is already seedless. Otherwise define zs=(a/10)*v/c and y=(g,a,b,u,v,w,zs). Since 0<=v<=c, y is legal and seedless. Directly, z-zs=R/(4a+9b)>=0. Put delta=(247/1620)*(z-zs). Holding g,a,b,u,v,w fixed while replacing z with zs changes exactly three Q stopping masses:

M_0(y)=M_0(x)+delta; M_6(y)=M_6(x)+delta; M_3(y)=M_3(x)-2delta.

All other M_j and BOTH stop times remain unchanged. These identities follow from the coefficients 47/180 and 67/162 in M_0,M_6, whose difference is -247/1620, and the corresponding opposite double change in M_3.

Construct a 7-by-7 nonnegative Q joint-mass matrix J, with row i indexing y's LR key and column j indexing x's LR key. The only nonzero entries are J_00=M_0(x), J_03=delta, J_66=M_6(x), J_63=delta, J_33=M_3(y), and J_jj=M_j(y) for j=1,2,4,5. Each row sum is M_i(y), each column sum M_j(x), and each likelihood-ratio-weighted column sum equals r_j*M_j(x), because r_0+r_6=2*r_3=2. For every d set d'_i=(sum_j J_ij*d_j)/M_i(y) for a nonzero row and 0 otherwise. All d'_i lie in [0,1]. The Q column and P weighted-column equalities imply that both errors are exactly preserved; times are already identical. QED.

Thus all nonnegative-residual source strategies are pointwise four-observer equivalent to single seedless-LR strategies. This is a stronger statement than mere equality of closed convex hulls.

## Theorem B — complete real symmetric zero-third-stage fiber, both residual signs

For ALL real z,v with 0<=z<=1/10 and z<=v<=z+9/40, let x=(1,1,1,0,v,0,z). For EVERY d in [0,1]^7, there is a SINGLE legal seedless strategy (y,d') with W(y,d')=W(x,d). The stop times are T_P=T_Q=3+v. This covers the positive, zero and negative residual halves of the entire two-parameter fiber.

When 13z>=4v, use Theorem A. When D=4v-13z>0, set h=D/20 and
y=(1,1-h,1-h,0,v+h,0,4*(v+h)/13).

Legality follows from D<=9*(1/10-z), so 0<h<=9/200, and from v+h<=13*(1-h)/40. The latter inequality is equivalent to h<=(13-40v)/53: its right side is at least (40/53)*(1/10-z), whereas h<=(9/20)*(1/10-z) and 9/20<40/53. The seedless identity holds because z_new=4*(v+h)/13 and v_new-z_new=9*(v+h)/13 with a_new=b_new=1-h. Both times are 3+(v+h)-h=3+v.

Define the positive rational coefficients
A=107/16200, C=27/1600, B=1/40, E=1909/64800,
alpha=(5/13)*C=27/4160, beta=(8/13)*C=27/2600,
gamma=A-alpha=193/1684800, eta=B-beta=19/1300.

Direct substitution yields the seven exact Q mass differences
M(y)-M(x)=D*(A,-C,B,-E,B,-C,A).
Moreover, alpha+beta=C and 2*(gamma+eta)=E, with alpha,beta,gamma,eta all nonnegative.

Here is a complete EXPLICIT transport J from the y LR keys (rows) to the x keys (columns). Row 0 sends Q masses M_0(x), alpha*D and gamma*D to columns 0,1,3. Row 6 sends M_6(x), alpha*D and gamma*D to columns 6,5,3. Row 2 sends beta*D and eta*D to columns 1,3; row 4 sends the same masses to columns 5,3. Rows 1,3,5 send their entire y Q masses to the identically numbered x columns. All other entries vanish.

The listed Q mass differences give the exact row sums M_i(y) and column sums M_j(x). At target LR 1/2, the incoming source LR-weighted mass is ((1/10)*alpha+(3/4)*beta)*D=(1/2)*C*D. The symmetric calculation at target LR 3/2 gives (3/2)*C*D. At LR 1, the incoming endpoint pairs have LR sums 1/10+19/10=2 and 3/4+5/4=2, so their Q/P ratio is exactly 1. The remaining columns retain their native LR. Thus all weighted column sums equal r_j*M_j(x), including the center. Using d'_i=(sum_j J_ij*d_j)/M_i(y), with 0 for zero-mass rows, preserves the two errors for EVERY real declaration vector and does not introduce a process-level external random mixture. QED.

Two exact test points: positive-residual x=(1,1,1,0,1/10,0,1/10) lifts to y=(1,1,1,0,1/10,0,2/65) with times 31/10. Negative-residual x=(1,1,1,0,9/40,0,0) lifts to y=(1,191/200,191/200,0,27/100,0,27/325) with times 129/40. Both constructions lift all real declarations.

## Validation, limits and research significance

VERIFY.py executes the exact rational mass/stop formulas, affine coefficient identities for the symmetric family (basis in v,z), both types of 7x7 joint-mass transport, P/Q normalization, seedless flow constraints, and exact equality of all four observations over bounded rational tests. EXACT_OUTPUT.txt is its actual stdout. The all-real statements are proved by the displayed algebra, positivity and transport, not by extrapolation from a grid.

This constructs an exact observer-preserving history-erasure map for a full seven-dimensional half-cone of legal flows and a complete two-dimensional fiber on the opposite half. The larger nonconvex R5 mother question K_FULL=K_SEEDLESS over ALL legal flows and all declarations remains open, specifically for negative residual with general g,a,b,u,w. This observer is a local finite P/Q-BRC toy model; no native X6 dynamics equivalence is asserted. The native Source control channel reported BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false, so current active owner/CLAIM and independent mathematical admission remain unconfirmed. The repository artifact is author-side research evidence.

Source provenance: predecessor research_notes/brc_r5_four_observer_convex_hull_20261107/RESEARCH.md and VERIFY.py at immutable f20b9a0bdc8c1fc8f69a2abeb7c231181d1a0d27; pinned GLOBAL a01383f825ef9d43b4b754254303298c64041568; pinned EM 86149263e38c22292c9def1e0f69092efa1be77e; current normative context in docs/RESEARCH_CONTINUATION_PROTOCOL.md, project portable protocol and research_priorities/research_method.json. P000 remains unchanged.
