# R5 — Source-conditioned J bridge: six-parameter four-observer classification

Date: 2026-11-02 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Provenance

Verified predecessor: awdawmip/enterprise-math@fc980ef8abab01c087fbed7b22891e852838ead1, research_notes/brc_r5_common_ray_answer_fiber_20261102_t1619/RESEARCH.md, VERIFY.py and EXACT_OUTPUT.txt. Frozen *scientific* pins unchanged: chatgpt-global-knowledge@a01383f825ef9d43b4b754254303298c64041568; enterprise-math@86149263e38c22292c9def1e0f69092efa1be77e. Current *normative* snapshots separately read at global main@f3fb0738848db1c43c2af6040c3a1f442ef7e812 and enterprise-math main@bdba5cfa529f565d303c869e19f254ae3712f446. P000, ACTIVE worldview, and project portable research protocol unchanged.

Mother objective: a strictly positive finite two-law stopping model with equal full/restricted four-observer convex hulls, but unequal actual real behavioral images. This research classifies a new source-conditioned six-parameter J bridge. Native X6 attribution remains a separate open bridge.

## Model and source-labelled BRC carrier

Start masses: I at time 1 with 1/2, J via B at time 2 with 1/4, K via C at time 3 with 1/4. I continuation splits equally to J via I and K via I. J continuation splits equally to direct time-3 answer and K via BJ/IJ. Stopping at I/J/K answers P at times 1/2/3. K continuing answers at time 4 or 5, with time-5 probability p=1/2 under law P, q=1/3 under law Q. These are the exact predecessor's graph and positive time kernels.

J direct answer Q under P law has probabilities v_B-alpha and v_I-alpha for B/I sources, while under Q law the probabilities are v_B and v_I. K continuation answers Q under both P/Q laws with source probabilities u_C,u_I,u_B,u_B for C,I,BJ,IJ. The real six-parameter domain is alpha ≠ 0 and all of v_B,v_I,v_B-alpha,v_I-alpha,u_C,u_I,u_B strictly in (0,1).

FULL stop policy (x,j_B,j_I,k_C,k_I,k_BJ,k_IJ) ranges over [0,1]^7. LR requires j_B=j_I=y and all four K stop parameters equal z, giving [0,1]^3. Exact observers O=(e_P,e_Q,T_P,T_Q), where e_P is P(answer P), e_Q is Q(answer Q).

Retain distinct BRC positive source masses:

~~~text
D_B=(1-j_B)/8; D_I=(1-x)(1-j_I)/8; D=D_B+D_I.
w_C=1/4; w_I=(1-x)/4; w_BJ=D_B; w_IJ=D_I.
C_s=w_s(1-k_s); C=sum_s C_s.
U=u_C*C_C+u_I*C_I+u_B*(C_BJ+C_IJ).
R=v_B*D_B+v_I*D_I.
~~~

Independent probability-flow enumeration yields, for EVERY real behavioral policy:

~~~text
e_P=1-(v_B-alpha)*D_B-(v_I-alpha)*D_I-U;
e_Q=R+U;
T_P=5/2-3*x/4+2*D+3*C/2;
T_Q=5/2-3*x/4+2*D+4*C/3.                        (1)
~~~

Because alpha≠0, the observer recovers all three affine coordinates

~~~text
D=(e_P+e_Q-1)/alpha; C=6(T_P-T_Q);
x=(4/3)*(5/2+2*D+3*C/2-T_P).                     (2)
~~~

The map O <-> (x,D,C,e_Q) is an affine bijection. Exposed-face reasoning below acts on the original four-dimensional observable information, not a lossy projection.

## Theorem — complete classification for all real six-parameter inputs

For every parameter satisfying the strict domain above,

~~~text
conv O(FULL)=conv O(LR)
       IFF v_B=v_I AND u_C=u_I=u_B.              (3)
~~~

Whenever the right-hand side holds, the ACTUAL real behavioral observation sets are equal:

~~~text
O(FULL)=O(LR).                                    (4)
~~~

Proof of necessity in three exact exposed faces:

(1) x≥0 and C≥0. The face x=C=0 is exposed by -(x+C). On its LR part x=0,z=1, so D=(1-y)/4 and e_Q=(v_B+v_I)*D/2. The FULL vertex (x,j_B,j_I,k_C,k_I,k_BJ,k_IJ)=(0,0,1,1,1,1,1) lies there with D=1/8, e_Q=v_B/8. Its source-fibre defect is (v_B-v_I)/16. Any convex representation by LR points on an exposed face uses only LR points of that face; equality of convex hulls therefore forces v_B=v_I. Because alpha is common, the P-law J direct kernels also become equal.

(2) x=D=0 is exposed by -x-D. LR then has x=0,y=1, C=(1-z)/2 and e_Q=(u_C+u_I)*C/2. FULL (0,1,1,0,1,1,1) lies on the face with C=1/4 and e_Q=u_C/4. The exact defect is (u_C-u_I)/8, forcing u_C=u_I under convex-hull equality.

(3) All policies satisfy x+4D ≤ x+(2-x)/2 = 1+x/2 ≤3/2, with equality at x=1,j_B=0. On this exposed face LR has y=0, D=1/8, C=3(1-z)/8 and e_Q=v_B/8+(2u_C+u_B)*C/3. FULL (1,0,1,0,1,1,1) has C=1/4 and e_Q=v_B/8+u_C/4. The exact defect (u_C-u_B)/12 forces u_C=u_B.

For sufficiency, if v_B=v_I=v and u_C=u_I=u_B=u, all J direct and K continuation answer kernels are source independent for each measure, as are the K time kernels. Given arbitrary real FULL stop probabilities, keep x and put

~~~text
y=[j_B+(1-x)*j_I]/(2-x);
z=[sum_s(w_s*k_s)]/[sum_s w_s].                   (5)
~~~

Both denominators are positive across the policy cube. LR reproduces D, total K arrival and C, and hence R=vD and U=uC and every coordinate in (1). Since LR⊂FULL, the ACTUAL observation images and hulls coincide. QED.

## Nondegenerate strictly positive mixed-source separator

Take (v_B,v_I,alpha,u_C,u_I,u_B)=(3/5,13/20,1/5,1/2,1/4,1/3). Thus J direct Q-answer probabilities are respectively (2/5,9/20) under P and (3/5,13/20) under Q; all natural conditional probabilities are strictly positive.

For n=(35,23,27,-27), substitute the exact map (1). For EVERY real FULL strategy,

~~~text
n·O-35=-D_B/5-4*D_I/5-3*C_C/2+3*C_I/2+(C_BJ+C_IJ)/2. (6)
~~~

Using 0≤C_I≤(1-x)/4, 0≤C_BJ≤D_B≤1/8, 0≤C_IJ≤D_I and C_C≥0 gives the pointwise upper bound

~~~text
n·O-35 ≤ 3*(1-x)/8+3*D_B/10-3*D_I/10 ≤33/80.  (7)
~~~

FULL (0,0,1,1,0,0,1) attains this value with

~~~text
W=(203/240,43/240,53/16,13/4), n·W=2833/80. (8)
~~~

For LR set s=(1-y)/8. Then D_B=s, D_I=(1-x)s. If z=1, (6) equals -s/5-4(1-x)s/5≤0. If z=0, (6) equals 3xs/10-3x/8≤-27x/80≤0. For real z, the objective is affine in 1-z, hence both endpoint inequalities imply n·O≤35. An LR policy attains 35. Consequently, for every real policy,

~~~text
h_FULL(n)=2833/80; h_LR(n)=35; gap=33/80.
dist_Linf(W,conv LR)≥gap/||n||_1=(33/80)/112=33/8960. (9)
~~~

Exact rational rank evidence at this parameter point: the LR corner-base affine determinant on (000,001,010,011,100) is 1/30720. The FULL Jacobian minor at all behavioral parameters 1/2, with columns (x,j_B,k_C,k_I), is -1/40960. Both are nonzero. The LR convex hull has affine dimension four; the FULL real behavioral image contains an open subset of R^4 (fix the other three parameters and apply the inverse function theorem).

## Verification and next problem

VERIFY.py uses standard-library Fraction, a second independent terminal-path probability-flow implementation, all 128 FULL/8 LR deterministic strategies on eight exact rational six-tuples (including a negative alpha case), observer inverse and face residuals, 120 nonbinary aggregation tests, integer-normal support and two four-dimensional determinants. Captured EXACT_OUTPUT.txt reports PASS_EXACT_R5_J_SOURCE_BRIDGE_CLASSIFICATION with 5,415 counted exact assertions. The real-domain theorem and exact support gap are established by the preceding algebraic proof; finite exact tests check the implementation and sampled cases.

New structural result: common nonzero J law-contrast exposes a third independently measurable J-source fibre while retaining both K-source fibres. A new candidate with unequal law-specific J contrasts alpha_B≠alpha_I or unequal K answer probabilities under P/Q changes (2) and is the next precise possible compensation route. Test complete 128-to-eight rational hull certificates (or Farkas separating normals), then actual-image nonmembership if hull equality is obtained.

Authenticated GitHub connector actor awdawmip has admin/push access. Native Enterprise Math service 0.6.11 reported research_authority_granted=false and executor_binding_configured=false; active owner query returned CONTROL_QUOTA, so no canonical CLAIM/Result/Driver review authority or mathematical admission is claimed. Preserve the frozen scientific pins, source identity and full evidence.
