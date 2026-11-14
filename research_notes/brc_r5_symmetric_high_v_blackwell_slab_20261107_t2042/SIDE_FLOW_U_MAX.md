# R5: Exact seven-key Blackwell lift of a maximal nonzero-u, negative-history corner

Date: 2026-11-07, Asia/Shanghai. Author-side exact-rational mathematical result, pending independent review and native Source admission. Frozen scientific pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e.

## Constructive all-real theorem

The legal FULL_HIST source flow is

    x=(g,a,b,u,v,w,z)=(1,1,1,27/80,9/40,0,0).

Its history residual R=9bz-4a(v-z)=-9/10 and stopping times are (T_P,T_Q)=(543/160,57/16). For every real seven-key declaration d in [0,1]^7, a **single legal seedless LR** flow

    y=(686/705,686/705,659/705,1233/3760,347/1128,0,343/3525)

and one 7-by-7 row-stochastic calibrated Blackwell channel produce declarations d'=Kd in [0,1]^7 with exactly the same (e_P,e_Q,T_P,T_Q).

The candidate seedless flow comes from solving the two exact stopping-time equations in the legal seedless face g=a, u=13a/40+b/80, v=a/10+9b/40, z=a/10, w=0. Their unique rational solution is a=686/705, b=659/705. Hence b<=a<=1, all legal flow bounds hold, R(y)=0, and both times match.

## Explicit nonnegative rational transport

The seven likelihood keys are r=(1/10,1/2,3/4,1,5/4,3/2,19/10). Frozen Q stopping masses are

    M(x)=(20443/72000,0,0,10157/36000,0,27/80,6943/72000),
    M(y)=(1007929/3384000,0,0,421271/1692000,9/470,1197/3760,391429/3384000).

Define Q_ij from seedless input key i to full-history output key j, all unlisted entries zero:

    Q[0,0]=20443/72000; Q[0,3]=9977/1184400; Q[0,5]=16277/2961000;
    Q[3,3]=421271/1692000;
    Q[4,3]=9/470;
    Q[5,3]=3677/658000; Q[5,5]=102899/329000;
    Q[6,5]=16277/846000; Q[6,6]=6943/72000.

Direct exact rational arithmetic establishes every coefficient is nonnegative and, for all i and j,

    sum_j Q[i,j]=M_i(y),
    sum_i Q[i,j]=M_j(x),
    sum_i r_i Q[i,j]=r_j M_j(x).

Normalize each positive-mass input row to K[i,j]=Q[i,j]/M_i(y) and choose identity rows for the zero-mass keys 1 and 2. K is row stochastic. For arbitrary real d in [0,1]^7 let d'_i=sum_j K[i,j]d_j. The two column equalities respectively preserve e_Q=sum M_j d_j and 1-e_P=sum r_j M_j d_j. Both times already match, proving the four-observer equality for all real declarations (not just binary labels).

The result changes the early flow (g,a,b,u,v,z) as well as history splitting: it is a genuinely different construction from holding the early flow fixed while normalizing z. The same single y works across an entire seven-dimensional declaration cube.

## Executed evidence and scope

VERIFY_SIDE_U_MAX.py is a standalone Python-stdlib Fraction checker: it verifies source/target legality, seedless bilinear equality, exact two stopping times, all seven row equations, all seven Q columns and seven likelihood-weighted P columns, nonnegative entries, and the 128 binary seven-label tests. Its actual stdout is OUTPUT_SIDE_U_MAX.txt. The displayed exact calibrated transport proves the all-real declaration statement; finite diagnostics confirm the certificate and endpoints.

This is an author-proved exact special-case theorem for the frozen seven-key P/Q-BRC observer, not full four-observer image equality or native X6 physical dynamics. It extends the other result in RESEARCH.md in this directory to one nonzero side-flow corner. Current native backend status/owner lookup returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false; no active owner/CLAIM or mathematical admission is asserted. Next: w>0 side-flow faces, see NEXT_UNIT.md.
