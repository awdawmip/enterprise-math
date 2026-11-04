# PREFIX-483 — General BRC observer kernel rank, Smith coordinates, and additive source-summary repair

Date: 2026-11-04 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. This is author-side portable research rather than an authenticated TASK Result or admitted theorem.

## Sources and declared observer

Extends PREFIX-482 (commit 02a472553377794633d2effd7a87325b695cd147) with the frozen scientific input f42f2906d77f24085c123f3ccfe9667d41caa96d. P000 Heartbeat World native X6, current ACTIVE observer-preservation requirements, the current normative-context continuation protocol and the portable research protocol apply. This is the restricted positive rational product-weight BRC ordered-path model; native six-axis identity, sign, order, provenance, multiplicity, and physical time remain separately typed. No signed/complex amplitude or physical heartbeat propagation is asserted.

Write p_i=min(u_i,v_i) for the m signed ordinary native axis pairs (m=5 in the concrete a/A,b/B,c/C,d/D,e/E model), and y_i=u_i-v_i. Length n, special count s and y determine P=Σp_i. A retained internal integer BRC observation records Mp for an arbitrary fixed matrix M in Z^{d×m} containing the all-ones row, as well as n,s,y and the KMP history q. All ordinary letters are legal, the distinguished x is legal at the beginning or after the fixed ordinary gate w. The ordinary alphabet contains a letter different from the initial letter of w.

Let H in Z^{ell×m} be the combined requested additive observers on p. For any specified positive rational direction weights A_i,B_i, include prime-valuation rows of rho_i=A_i B_i; extra verified additive occupancy/source-summary rows C may also be stacked. Completely ordered source IDs, phase and other nonlinear observations remain outside this linear class.

## Theorem A: exact minimum additive repair rank

For every integer M,H in the stated model, the smallest number of fixed-coefficient, integer-valued additive residual coordinates sufficient to recover Hp on all attainable joint BRC/KMP fibers at all lengths, and after any finite legal append, is

    r = rank_Q([M;H])-rank_Q(M) = rank_Q(H | ker_Q M).

A constructive algorithm scans rows h of H, retaining h as a row of T only when rank_Q([M;T;h]) increases. Then T has exactly r integer rows and every row h_j of H has a rational decomposition h_j=alpha_j M+beta_j T. Thus from retained (Mp,t=Tp) one reconstructs h_j p=alpha_j(Mp)+beta_j t exactly; the output is integer for every actual state. A signed native direction ±i updates p by Δp_i=1 when the appended direction opposes the previous imbalance y_i, and 0 otherwise; hence t'=t+TΔp is a direct typed BRC right-action. q evolves by its ordinary KMP transition and x reset. A count-only dynamic program on these coordinates therefore carries the corresponding rational-weight histogram and every requested additive summary.

To prove minimality, let S have b<r integer rows. Rank-nullity on K=ker_Q M provides rational z in K∩ker_Q S with Hz≠0. Multiply z by a common denominator to make z integral. Choose p≥0 large enough for p+z≥0. Realize u=v=p and u'=v'=p+z as two ordinary-only signed paths. Their n agrees because the all-ones row belongs to M; both have s=0,y=0,Mp,Sp equal. Append k=|w| identical copies of an ordinary signed symbol c distinct from the first symbol of w. Since every nonempty prefix of w begins with w[0] different from c, no suffix of length at most k of this c-run is a prefix of w; both resulting KMP states are therefore q=0. Starting from y=0, consecutive steps of the same signed c direction never increase a cancellation counter p. Thus their p difference and H(p+z)-Hp remain unchanged. Hence both legal paths share the allegedly sufficient repaired observation but differ in Hp. Contradiction. QED. This minimum is for uniform additive linear coordinates, not arbitrary variable-bit nonlinear encodings.

For an additional verified integer-linear source-summary observer C, the extra number of independent residual coordinates is exactly

    Delta r = rank_Q([M;H;C])-rank_Q([M;H]).

This is an exact observer-specific accounting rule; ordered provenance itself requires a different carrier.

## Theorem B: exact primitive Smith codec

Compute Smith normal form U M V=S with unimodular U,V and nonzero diagonal s_1|...|s_a, where a=rank M. Write c=V^{-1}p=(c_A,c_K), so the final m-a coordinates c_K are integer kernel coordinates, and let B be the last m-a columns of V. For D=HB compute L D R=diag(d_1,...,d_r,0), with L,R unimodular and d_i>0. The r integer coordinates

    t=(R^{-1}c_K)_{1:r}

form an additive, updateable, primitive kernel coordinate. Reconstruct c_{A,i}=(U Mp)_i/s_i by exact integer division for reachable input. The full requested observer is

    Hp = H V_A c_A + L^{-1}(d_1 t_1,...,d_r t_r,0,...,0)^T.

This proves full reconstruction with r coordinates without replacing actual full source histories. The nonzero Smith d_i describe the lattice congruence/index of H(ker_Z M) inside its saturation; rank alone describes dimension, while the elementary divisors describe attainable congruences. The greedy selected-row codec of Theorem A is simpler and exact, but its chosen labels need not be primitive. General Smith transforms are an algebraic construction here; the executable certificate checks exact row ranks and selected-row reconstruction rather than a generic Smith implementation.

## Native BRC examples

For the five native ordinary axis pairs, the BRC matrix is

    M=[[1,1,1,1,1],[0,1,0,2,1],[0,0,1,0,1]].

Its integer kernel has basis r1=(1,-2,0,1,0), r2=(1,-1,-1,0,1). With unit negative weights and positive weights (6,12,18,24,36), the prime-valuation observer H vanishes on both kernel vectors, giving r=0. Adding the observer p_d increases r to 1, and adding both p_d and p_e increases it to 2. Changing e's positive weight to 35 gives r=1 with sufficient t=p_e. A further query for p_e costs no additional rank; a query for p_d raises the rank to 2. The legal ordinary-only paths aAeE and bBcC share length, BRC observation and q=0, but have weights 210 and 216 under e=35.

For d=96,e=288 the defects are 4 and 8, yielding rank 1 and sufficient t=2p_d+3p_e. A hypothetical kernel-defect valuation row [2,4] has Smith invariant gcd(2,4)=2, while its primitive repair coordinate d+2e is only one-dimensional. These are exact restricted-model lattice calculations.

## Executed certificates and evidence scope

The companion executable prefix483_rank_and_smith_compact_certificate.py uses only Python standard-library exact Fractions/integers. It checks the native kernel, rational valuations for four weight assignments, observer rank 0/1/2 and 480 seeded exact integer-matrix cases. Its saved stdout ends ALL_CHECKS_PASS. A separately executed fuller author-side certificate (prefix483_universal_brc_observer_rank_certificate.py) additionally compared complete raw direction-occupancy/KMP state counts against direct BRC right-action state counts for every n=0..6, gates aab and aba, and eight weight/additive-observer scenarios. This latter execution yielded n=6 total 1,100,320 ordered legal paths for each gate, with aab joint fibers 10,711 (base), 10,863 (one extra rank), 10,940 (two); aba has 10,713, 10,865, 10,942 respectively. It checked singleton positive weights in every repaired fiber; author execution ended ALL_CHECKS_PASS. The fuller executable source and raw log are retained in the author's local evidence package; the compact repeatable certificate and its raw stdout are included in this commit. The theorem for unbounded n follows from the proofs.

Evidence scope: exact integer additive observers, X6 native BRC sign/pair updates, legal normal/x append and positive rational product weights. Exact phase, signed amplitudes, ordered provenance, physical dynamics, full native rotations and final-address serialization are separately specified future research; there is no claim that merely retaining Hp makes every source observer safe. Computing arbitrary prime valuations of large un-factored rationals and a generic SNF transform has separate input and execution cost. Neither Git publication nor an author test constitutes independent review or admission.

## Next unit

PREFIX-484: implement a generic exact Smith-with-transform certificate, checking U M V=S and L H B R=diag on nonprimitive matrices, measure concrete integer-label/coding costs, and independently study an order-sensitive source query on two paths with identical raw occupancy. Determine a minimal finite-history carrier for that query, preserving all ordered provenance until the stated future observation is proved safe.

Authority: GitHub authenticated account awdawmip has admin/push. At 2026-11-04 UTC native Sites was static_machine_readonly with research_authority_granted=false; control task listing reported CONTROL_QUOTA, session creation reported STATIC_READONLY_SCOPE_DENIED and operation_sent=false. Active TASK owner, CLAIM, Reviewer and Admission are unconfirmed/not performed.
