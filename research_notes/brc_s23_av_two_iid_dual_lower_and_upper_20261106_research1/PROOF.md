# S23/AV two-iid reverse deficiency: exact three-point dual and sharper full-box upper

2026-11-06. Author-side analytic proof / exact rational execution / independent review pending. Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Continues Draft PR #1777 at 323985a87e78abd7ca2fac0bdede9823063384dd. This is a conditional stochastic-observer model extracted from tagged S23 with six sources; it does not alter its source tags, lawful encoders, or P000.

## Theorem and quantifiers

For all real a,c in [1/2,7/8], with the other S23 parameter b arbitrary in [1/8,1/2], define z=(1-a)c, A(a,c)=(a,z,1-a-z) on stops (1,3,4), and B(a,c)=(z,1-z) on (Y,N). Two trials are conditionally independent given the SAME unknown pair (a,c). Let the single reconstruction kernel L be any row-stochastic 4-by-9 matrix, independent of a,b,c, mapping (YY,YN,NY,NN) to the ordered labels (11,13,14,31,33,34,41,43,44). Let

    delta2 = inf_L sup_{a,c in [1/2,7/8]} TV(A(a,c)⊗A(a,c), (B(a,c)⊗B(a,c))L),
    TV(P,Q) = (1/2) sum_j |P_j-Q_j|.

**Exact certified bounds:**

    1491/8125 <= delta2 <= 7573633/40000000.

The lower improves predecessor 423/2468. The upper improves predecessor 947/5000. The upper is attained as the worst error of the particular kernel below; exact minimax delta2 is still open.

## Proof of the new lower bound: three legal hypotheses and a dual test

Take theta0=(1/2,1/2), theta1=(11/16,7/8), theta2=(47/64,7/8), with P_k=A(theta_k)⊗A(theta_k) and Q_k=B(theta_k)⊗B(theta_k). Let the rational weights and signed nine-coordinate test vectors be:

    w0=4061/8125; w1=12576/56875; w2=15872/56875.
    v0=(-1,-1,+1,-1,0,+1,+1,+1,+1)
    v1=(+1,+1,-1,+1,4/35,-1,-1,-1,-1)
    v2=(+1,+1,-1,+1,-12/119,-1,-1,-1,-1).

The three nonnegative weights sum to 1; every test coordinate has magnitude at most 1. For ANY stochastic L, by duality of total variation,

    sup_theta TV(P_theta,Q_theta L)
       >= sum_k w_k TV(P_k,Q_k L)
       >= (1/2) sum_k w_k <v_k, P_k-Q_k L>
       = (C - sum_{r,j} L[r,j] d[r,j])/2,
    C = sum_k w_k <v_k,P_k>,
    d[r,j] = sum_k w_k Q_k[r] v_k[j].

Every row of L is a probability distribution, so sum_j L[r,j]d[r,j] <= max_j d[r,j]. Exact rational arithmetic yields C/2=597/3250 and the four row maxima (3/8125,0,0,0). Therefore

    sup_theta TV(P_theta,Q_theta L)
       >= 597/3250 - 3/16250 = 1491/8125.

The bound holds for every reconstruction L and every real parameter domain containing the three legal pairs. No full-square sampling inference is used.

## Constructive upper kernel

The following rows are divided by D=10,000,000; row order YY,YN,NY,NN, column order 11,13,14,31,33,34,41,43,44:

    0,0,0,0,10000000,0,0,0,0
    0,0,0,5791902,0,0,4208098,0,0
    0,5539216,663649,908246,0,1111111,0,1111111,666667
    7533509,375817,1483158,265834,0,0,341682,0,0

Every row has nonnegative entries summing to D.

## Full real-domain proof of the upper

Let the four corners theta_i be the lexicographic list of (a,c) in {1/2,7/8}². Each component of A(a,c) and B(a,c) is separately affine in a and c, hence for nonnegative bilinear corner weights lambda_i(a,c) summing to 1, we have A=sum_i lambda_i A_i and B=sum_i lambda_i B_i.

Define signed vectors F_ij=A_i⊗A_j-(B_i⊗B_j)L and G_ii=F_ii, G_ij=(F_ij+F_ji)/2 for i<j. By same-parameter two-trial expansion, the exact signed error is

    E(a,c)=sum_i lambda_i² G_ii + sum_{i<j} 2 lambda_i lambda_j G_ij.

The ten coefficients are nonnegative and sum to 1. Convexity of the half-l1 norm gives TV(E(a,c)) <= max_{i<=j}TV(G_ij) over the ENTIRE real square.

Exact ten signed-corner values (calculated from the integer kernel in VERIFY.py):

    00 7573633/40000000
    01 65751633/640000000
    02 11801581/128000000
    03 19089671/256000000
    11 163366061/1280000000
    12 94677413/640000000
    13 484712459/2560000000
    22 52992111/512000000
    23 279769961/2048000000
    33 1938849731/10240000000

All ten are <= 7573633/40000000. At theta0=(1/2,1/2), actual TV(F_00) equals that upper bound. Hence this particular L has exactly the claimed worst-case error over all reals in the legal square.

## Mathematical and source status

The two exact witnesses were discovered with numerical linear programming, but proof and verification use only rational identities plus the analytic bilinear interpolation lemma. The source-tagged conditional AV calculation is an auxiliary observation experiment. The original ten-label S23 encoder/decoder minimax risk R_beh(k,10) requires a separately verified lawful strategy mapping and correct quantifier transfer. The mathematical result here is an author-side scoped theorem, awaiting independent review and admission.

Next question: refine an exact finite-hypothesis dual and matching kernel to identify delta2; independently test a lawful bridge to the frozen ten-label mother problem.