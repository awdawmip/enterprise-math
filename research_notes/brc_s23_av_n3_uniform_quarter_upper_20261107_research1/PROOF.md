# S23 conditional AV: exact all-real three-observation upper bound below one quarter

Date: 2026-11-07. AUTHOR_CONSTRUCTION / EXACT_INTEGER_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen science: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: Draft PR #1777, research_notes/brc_s23_av_three_iid_exact_fiber_diameter_20261106_r1/PROOF.md; previous all-real upper bound 99/343.

## New theorem

For arbitrary real a,c in [1/2,7/8], z=(1-a)c, let A=(a,z,(1-a)(1-c)) on (stop1,stop3,stop4), and B=(z,1-z) on (Y,N). The same hidden (a,c) governs three conditionally IID trials. A single parameter-independent Markov kernel K maps 8 binary words to 27 tagged words. With total variation TV=one half the L1 distance, define

    delta_3 = inf_K sup_(a,c in [1/2,7/8]) TV(A(a,c)^tensor3, B(z)^tensor3 K).

The complete rational K in KERNEL.json has denominator 1,000,000 and 42 positive entries in 8 stochastic rows. For EVERY REAL lawful a,c it satisfies the strict certified bound

    delta_3 <= 1075016402332480007/4398046511104000000
            ~= 0.24443043056009628 < 49/200 < 1/4.

Previous exact fiber lower bound 5211/21952 ~= 0.237381559766764 persists.
The new upper bound improves the previous 99/343 ~= 0.288629737609330.
Numerical linear programming on an 11x11 parameter sample found the candidate. Its candidate status is superseded by the exact continuum certificate below.

## Precise kernel semantics

Input word positions use Python itertools.product(range(2),repeat=3), with 0=Y(stop3),1=N(other). Output word positions use itertools.product(range(3),repeat=3), with 0=stop1,1=stop3,2=stop4. Every integer in KERNEL.json represents a numerator divided by 1,000,000. Unlisted entries are zero. The 8 row sums equal exactly 1,000,000, as independently checked by VERIFY.py.

## Analytic continuum extension

Put E(a,c)=TV(A(a,c)^tensor3,B((1-a)c)^tensor3 K).
For any two lawful pairs (a,c),(a',c'), the TV triangle inequality, tensor coupling and Markov contraction yield

    |E(a,c)-E(a',c')|
    <=3 TV(A(a,c),A(a',c'))+3 TV(B(z),B(z')).

A two-stage coupling of the full one-trial law chooses stop1 with probability a, otherwise stop3 with conditional probability c. It establishes

    TV(A(a,c),A(a',c'))
       <=|a-a'|+min(1-a,1-a')*|c-c'|
       <=|a-a'|+|c-c'|/2.

B is the deterministic stop3-indicator projection of A, so
TV(B(z),B(z'))<=TV(A(a,c),A(a',c')). Therefore

    |E(a,c)-E(a',c')| <= 3(2|a-a'|+|c-c'|).        [1]

Select the 257 x 257 grid

    a_i=c_i=1/2+3i/(8*256), i=0,...,256.

Every legal real pair is at most 3/4096 from a grid point in each coordinate. Equation [1] gives

    sup_real E <= max_grid E + 27/4096.              [2]

## Exact finite integer certificate

At grid indices (i,j), put D=2048, A0=1024+3i, C0=1024+3j.
The three one-trial A probabilities have integer numerators

    p=[A0*D,(D-A0)*C0,(D-A0)*(D-C0)] / D^2.

The B probabilities have numerators

    b=[(D-A0)*C0,D^2-(D-A0)*C0] / D^2.

For each of the 27 ordered full words x, let p_x be the product of its three selected p numerators. For binary word y, let b_y be the analogous product. If Knum denotes the integer kernel, then

    E_ij = [SUM_x |1000000*p_x - SUM_y Knum[y,x]*b_y|]
           / [2*1000000*D^6].

VERIFY.py checks EVERY grid point in exact integer arithmetic, retaining all 27 ordered output differences separately, with no floating-point arithmetic for its certificate. The yes-count grouping inside VERIFY.py is exact algebraic reuse. For 66,049 points and 1,783,323 output-word differences, the executed exact maximum is

    max_grid E =
    1046025373084480007/4398046511104000000
    ~=0.23783863368509628,

at indices (i,j)=(141,256). Adding 27/4096 in [2] gives exactly

    1075016402332480007/4398046511104000000
    ~=0.24443043056009628 < 49/200 < 1/4.

The integer program asserts all 66,049 enclosure comparisons and the final rational inequality; RUN_EVIDENCE.txt contains the actual stdout from the corresponding local verification. This is a rigorous **all-real** theorem because the analytic modulus [1] extends the complete finite computation over the square.

## BRC and project scope

The checked 27-word law retains tagged branch identity, positional multiplicity and a single shared hidden parameter. Its binary observer erases the stop1/stop4 distinction. BRC resolution: REUSE_APPLIED for typed positive-rational branch histograms and exact observation-fiber residuals. This auxiliary conditional-AV result makes no transfer claim for the six-source, ten-label mother target R_beh(k,10), k=4,6; the lawful encoder/decoder, source-choice and shared-b bridge remain open. P000/ACTIVE ontology is unchanged.

Gateway em_status and task-inventory requests returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false. Current Researcher-ID, native RA, active Owner and formal CLAIM are unconfirmed. GitHub-published author work is not a formal Result or Review.

## Next exact research units

Use exact interval/Bernstein subdivisions to sharpen the finite-n continuum bound with the same kernel toward its checked grid radius 0.23784; optimize a joint 8x27 kernel and seek a matching all-real lower bound. Independently test the lawful S23 ten-label mother bridge. A numerical LP candidate is an input to a certificate, not a mathematical result without one.
