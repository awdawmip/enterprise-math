# R5 — exact signed-support obstruction for the source-sensitive diamond

Status: NONBLIND / AUTHOR_SIDE / EXACT_SYMBOLIC_DERIVATION / FRACTION_REGRESSION_PASS / UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING. Not a native Result, independent Driver Review, accepted theorem, or X6 transfer.

## Exact provenance and input

This is a targeted author-side continuation of:
- research_notes/brc_r5_diamond_observer_quotient_20261029_t0240/RESEARCH.md (blob f5175eba01989937f82cc22039a55c69fbb900d4);
- the precise heterogeneous-tail proposal in its NEXT_TASK.md (blob 78b2643a5e6805861a07f17cf3db34950daf2b59).

No previous source-blind result is reclaimed. The mathematical conclusion below is only for this precise source-sensitive candidate. In particular the general R5 mother problem remains open.

Signatures S=(1/2,1,3/2,5/2). Initial Q: forced terminal mass 1/2 at t=1,s=1/2, and alive origin masses A=B=1/4 at t=1,s=3/2. Time-1 origin Q kernels:
mu_A=(7/50,11/75,1/2,16/75),
mu_B=(17/200,23/150,3/5,97/600).
At t=2 the alive left (s=1) and right (s=3/2) kernels are:
nu_A,L=(1/2,1/6,1/4,1/12),
nu_B,L=(5/12,1/3,1/6,1/12),
nu_A,R=(17/100,23/75,1/5,97/300),
nu_B,R=(31/120,5/18,1/15,143/360).
Both branches meet at t=3,s=3/2; its source-sensitive continuation kernels to terminal time 4 are:
eta_A=(1/8,1/4,3/8,1/4), eta_B=(5/32,3/16,13/32,1/4).

All listed Q kernels are strictly positive, normalized, and have child-signature expectation equal to the parent's likelihood ratio r. The corresponding P kernel is P(s|i,r)=s Q(s|i,r)/r. Observer O=(e_P,e_Q,T_P,T_Q), with W_(t,s) the aggregate terminal Q mass and 0<=m_(t,s)<=W_(t,s) the Q mass declared P:
e_P=1-sum s*m_(t,s), e_Q=sum m_(t,s),
T_P=sum t*s*W_(t,s), T_Q=sum t*W_(t,s).
The LR policies have no persistent seed and share a continuation coin for each observed (t,s). Full-history policies can distinguish origin/path.

## Exact all-real signed support

Choose signed direction c=(7,7,-1,1). At any terminal cell (t,s), the decision linear contribution is (7-7s)m_(t,s), so the optimal declaration is P iff s=1/2 (zero effect at s=1). This holds simultaneously for every history, including arbitrary real behavioral randomizations. The optimized reward per unit terminal Q mass is

    rho(t,s)=t*(1-s)+7*max(0,1-s),

with additional constant c1=7 in the four-observer support.

Let U be the LR root continuation probability, L=U*alpha_L, R=U*alpha_R the two time-2 survival flows, and gamma the common merge continuation. Exactly

    0<=U<=1, 0<=L,R<=U, 0<=gamma<=1.

The two source-labeled Q merge arrival vectors, per unit L/R flow, are

    v=(11/1200,23/3600), w=(1/40,1/100).

Thus time-4 terminal Q mass at signature s is

    gamma * [(v_A*L+w_A*R)*eta_A(s)
           +(v_B*L+w_B*R)*eta_B(s)].

Substitution into the exact aggregate terminal mass equation and collection of rational coefficients give the identity for ALL REAL LR coin values:

    H_LR(U,L,R,gamma)
     =35/4 - (17/320)*U + (1729/14400)*L + (29/400)*R
       - gamma*[(7/25600)*L+(7/6400)*R].             (1)

The gamma coefficient is nonpositive. The L and R coefficients are strictly positive; at fixed U, L=R=U is optimal. Then

    H_LR <= 35/4 + (251/1800)*U <= 16001/1800.

Equality is attained by the legal seedless-LR policy (U,alpha_L,alpha_R,gamma)=(1,1,1,0) and the terminal declaration rule above. Therefore the exact support is

    h_LR(7,7,-1,1) = 16001/1800.                      (2)

This is a symbolic real-domain proof; finite sampling is not used to extend a bound to real values.

## Legal full-history separating witness

Use U=alpha_L=alpha_R=1 and the same terminal declaration, but at the merged t=3,s=3/2 state stop origin A and continue origin B:

    gamma_A=0, gamma_B=1.

The arriving source masses are x_A=41/1200 and x_B=59/3600. The reward per Q mass when stopping at the merge is

    rho(3,3/2)=-3/2.

Continuing to time 4 has source-dependent expected rewards

    E_etaA[rho(4,S)]=-25/16 < -3/2,
    E_etaB[rho(4,S)]=-93/64 > -3/2.

The gain from stopping A but continuing B over the LR optimum is exactly

    (59/3600)*(-93/64+3/2) = 59/76800.

Hence a valid full-history behavioral policy attains

    h_full(c) >= 16001/1800 + 59/76800 = 409661/46080,

and consequently h_full(c) > h_LR(c) and

    conv(O_full) != conv(O_LR).                       (3)

This kills the specified source-sensitive R5 candidate at the mandatory all-signed convex-hull gate BEFORE any semialgebraic real-image membership search. It is not a no-go for the general mother question, nor a proof that the real LR image is or is not convex in unrelated kernels. It does not touch P000.

## Checks, remaining frontier, governance

The accompanying VERIFY.py uses exact fractions for full terminal mass construction, P/Q normalization, objective identity, all 16 deterministic LR patterns, 1000 fixed-seed rational LR tests, and the strict full witness. CHECK.json preserves actual exact execution results. These are regressions; all-real support relies on the exact algebra in (1).

Next research discriminant: seek a different source-sensitive tail with equal support in EVERY signed 4-direction, then test actual real-image membership; or establish a stronger structural no-go. No separate official task should be published simply to revisit this eliminated kernel. Formal F7 frozen Result RR-AA38973D56330E59D315 remains awaiting legitimate, independent current Driver DA and exact-set review. Author-side GitHub publication and this branch do not grant native CLAIM/Result/Review/Follow-up/Task authority.
