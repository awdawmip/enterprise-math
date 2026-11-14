# R5: Sharp equal-early-gate LR ray — exact primal/dual theorem

Date 2026-11-07 Asia/Shanghai. Status AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Frozen scientific pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. P000 and ACTIVE worldview preserved. Prior R5 frontier: bf6b1ba631aa57471ee1efecc462fb2316b84ec7, which realizes all W(h) for 0<=h<=9/2500. The carrier is the residual-preserving stopped likelihood-ratio BRC histogram; this is an auxiliary positive P/Q model, not native X6 dynamics.

## Theorem, exact domain

For the strictly positive four-stage P/Q tree at delta=1/4, take W=(e_P,e_Q,T_P,T_Q), e_P=P(declare Q), e_Q=Q(declare P), and W*=(161801/180000,6499/18000,267/80,137/40). Define W(h)=W*+h(1,1,1,-1), h>=0.

In the seedless-LR strategy class with equal early continuation g=u0=u1=t in [0,1], arbitrary pooled stage-3 LR continuation probabilities and arbitrary real randomized declarations at each stopped LR/time key, the point W(h) is achievable IF AND ONLY IF

    0 <= h <= H = 16917/4642820 = 0.00364369068798704...

This is an all-real theorem including boundaries and irrational probabilities, not an LP numerical extrapolation. H/(9/2500)=704875/696423 (>1), a 1.21363% extension. The mother FULL_HIST versus unrestricted seedless-LR four-dimensional actual-image question is open.

## Exact kernel, pooled capacities, observer map

At stage 2 the Q masses are (1/2,1/2) with LR (3/4,5/4). At stage 3 LR (1/2,1,3/2) has conditional Q rows (13/20,1/5,3/20) and (1/40,9/20,21/40). Stage-4 LR (1/10,1,19/10) has rows (509,382,9)/900 at stage-3 LR 1/2 and (9,382,509)/900 at LR 3/2. At central LR 1, history-conditioned rows are (47/180,43/90,47/180) and (67/162,14/81,67/162). Every row is strictly positive, normalized, and its LR first moment equals the parent LR; verified exactly.

When g=u0=u1=t, the history contributions to central LR=1 have ratio 4:9, giving the fixed pooled stage-4 row (11/30,4/15,11/30). The time-3 Q continuing capacities are (27t/80,13t/40,27t/80). Put X=(x0,x1,x2) with 0<=x0,x2<=27t/80 and 0<=x1<=13t/40. The stopped Q masses in LR order (1/10,1/2,1,3/2,19/10) become

    M_0.1 = (509/900)x0+(11/30)x1+(1/100)x2;
    M_0.5 = 27t/80-x0;
    M_1   = 1-t+13t/40-x1+(191/450)(x0+x2)+(4/15)x1;
    M_1.5 = 27t/80-x2;
    M_1.9 = (1/100)x0+(11/30)x1+(509/900)x2.

For each bin r define stopped Q mass E_r declared P, satisfying 0<=E_r<=M_r. Then

    e_Q = sum E_r; e_P = 1-sum r E_r;
    T_Q = 1+2t+x0+x1+x2;
    T_P = 1+2t+x0/2+x1+3x2/2.

These are affine in (t,X,E). Conversely any feasible (t,X,E) is realized by stage-3 continuation probability xj/Vj (define 0 for zero capacity) and common stopped LR declaration probability E_r/M_r (arbitrary for zero mass). Even if a stopped LR appears at multiple times, a common declaration fraction across those times achieves aggregate E_r. Hence this linear feasibility model describes the entire stated equal-gate strategy class for these observers, including t=0.

## All-real upper certificate

Let the ten coordinates be y=(t,x0,x1,x2,E_0.1,E_0.5,E_1,E_1.5,E_1.9,h). The ray target imposes

    A1=2t+x0+x1+x2+h                           = 97/40;
    A2=2t+x0/2+x1+3x2/2-h                      = 187/80;
    A3=E_0.1+E_0.5+E_1+E_1.5+E_1.9-h          = 6499/18000;
    A4=E_0.1/10+E_0.5/2+E_1+3E_1.5/2+19E_1.9/10+h = 18199/180000.

The six necessary nonpositive quantities are

    C1=x1-13t/40; C2=E_0.1-M_0.1; C3=E_0.5-M_0.5;
    C4=-E_1; C5=-E_1.5; C6=-E_1.9.

There is a direct polynomial-free exact rational identity, valid for arbitrary real y:

    232141*h = 21126*A1 -13604*A2 -83401*A3 +114010*A4
              +18878*C1 +72000*C2 +26396*C3
              +30609*C4 +87614*C5 +133218*C6.

Every C_i<=0 for every legal policy, so

    232141*h <= 21126*(97/40)-13604*(187/80)
                -83401*(6499/18000)+114010*(18199/180000)
              = 16917/20.

It follows h<=16917/4642820. This is a complete exact dual certificate. The companion VERIFY.py checks all 10 coefficient identities with Fraction.

## Exact attainment, continuous segment

At h=H set

    t=31911/33163;
    X=(3199433/18571280,31911/102040,220131/18571280);
    E=(886766809/4178538000,1415873/9285640,0,0,0).

The full stopped Q histogram is

    M=(886766809/4178538000,1415873/9285640,
       416394241/2089269000,726381/2321410,
       57150451/464282000).

Both sum M=1 and sum(rM)=1 hold exactly. X<=V, E<=M, with x1=13t/40, E_0.1=M_0.1 and E_0.5=M_0.5. The four actual observers equal W(H) by exact arithmetic.

A center realization W(0) from the predecessor has

    t0=77/80; X0=(3/16,3/10,1/80);
    E0=(1297/6000,879/6400,563/144000,0,349/96000).

Because all capacities and all four observations are affine in (t,X,E) *within the equal-gate class*, for every real s in [0,1] the convex interpolation of these two policy parameter vectors is legal and realizes W(sH). This proves the entire closed real ray segment.

## Verification and status

An independent local standard-library Python fractions.Fraction checker was actually executed, giving PASS_EXACT_R5_EQUAL_EARLY_GATE_SHARP_RAY. It checks frozen P/Q martingale kernels, stopped masses and moments, endpoint feasibility, exact observer equalities, selected interpolation points and all 10 upper-dual coefficient identities. The published VERIFY.py is an equivalent streamlined version of these checks; it has not independently been rerun byte-for-byte against the published Git blob. EXACT_OUTPUT.txt carries the actual local checker output. Universal conclusions use the displayed algebraic dual and affine interpolation proofs rather than only finite tests.

GitHub authenticated login awdawmip, repository push/admin verified. Native em_status and em_control_tasks yielded BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false; live R5 owner and CLAIM are unconfirmed. Author-side publication confers no Result/Review status. Next: vary g,u0,u1 independently and use the full seven-bin histogram/nonlinear central history mixture to seek either larger exact witness or all-real upper bound.
