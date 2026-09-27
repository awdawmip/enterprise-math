# RP10: fixed-Gram evolution and a projected two-row sampler

Progress-Event-ID: RP10-C971348E-FIXED-GRAM-20260927
Date: 2026-09-27 Asia/Taipei
Status: AUTHOR_SYMBOLIC_DERIVATION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read snapshot: c8f5fd60b87636d056cbeb8131adbc2c5c36d747
EM read snapshot: 4c0faffe3e71068bfc41a9ac617fb54669ed59a1
Scientific runtime parent: current-conversation RP9 run ZIP, not an asserted new Git commit.

## 0. Provenance, actual work, and nonclaims

The current conversation's RP9 report and Proof were read through Files. They establish an executed inverse-free coefficient path, exact same-basis equivalence on 85 stored rows, reduced short bases, and one two-checkpoint conditional experiment. They do not establish efficient basis reuse across arbitrary future words. No previous measured number is relabeled as an RP10 measurement.

During live Drive reconciliation, two additional symbolic records were discovered and consumed: document 1FVIrctxN5Ffrgfd0HK7pCtvEs9jAA5FNNZbPgxTV3PA (migration basis/leakage, linked there to project record 7c0fc0e9), and document 1vdavacWY8-LigFBgt7I_en1lNqYbf3P9TnO-MKKEMRM (RP9-B arbitrary candidate certificate and reversible short bases). They already contain [F,TF], the block Gram matrix, the exact leakage identity, and inverse-free candidate ideas. Those are antecedents, not new discoveries here. The documents describe a different RP8 cloud branch as well as the current attachment branch; their numerical payloads must not be mixed.

New contribution of this note: an explicitly DIFFERENT, directly projected coordinate target; its two-row sampling proof without online ambient-row reconstruction; an orthogonal combination of leakage and metric-quantization error; and the precise boundary for compiling multiple compressed operators. Exact common-invariant closure is given as an alternative with no operator-projection error, not as a proven small-rank property of the current bank.

container.exec, python.exec and python_user_visible.exec each returned ClientError in this turn. There was NO new BRC numerical execution, no tested implementation, no measured leakage eigenvalue, no rank/precision/speed result, no new ZIP, and no local byte-hash or restore replay. Source publication and Drive writes remain available. Mathematical identities below are author derivations conditional on the inherited typed norm/isometry contracts. P000, the actual b12 bank and the 61-mode interpretation are not changed. No classical phase, trigonometric or matrix-exponential reference was computed.

## 1. Fixed coordinate space and the inherited leakage packet

Use the inherited signed 61-mode BRC pairing J and squared norm Q. Matrix transpose denotes this coefficient algebra, not a new spatial model. Let B have r independent full-mode columns, S=range(B), and G=B^T B be positive definite. Assume current nonzero work rows have the exact representation u_h(w)=B c_h(w). Initial projection error or ambient escape rows are NOT silently absorbed into this assumption. Starting from the standard initial state requires including its direction in S; starting from a compressed RP9 checkpoint has its separately declared initial error.

For one actual time-ordered feedback word T, with T^T T=I in this carrier, form once

  H=B^T T B,
  A=G^{-1}H (implemented by solving GA=H, not necessarily by storing an inverse),
  Pi=B G^{-1}B^T,
  R_T=TB-BA,
  D=R_T^T R_T=G-H^T G^{-1}H.

Then B^T R_T=0, 0<=D<=G, and A^T G A=G-D. The transported basis TB has exactly the same Gram G; transport alone needs no new Gram factorization. But the two-arm join occupies span(B,TB), not generally span(TB).

For c=c_h(w), d=c_h(P^{-1}w), sign s_b=(-1)^b, and the actual modular permutation P,

  a_b(w)=(B c+s_b T B d)/2,
  v_b(w)=(c+s_b A d)/2,
  Pi a_b=B v_b,
  Q(a_b)=[c^T G c+d^T G d+2s_b c^T H d]/4,
  Q(a_b)-Q(B v_b)=d^T D d/4>=0.

These raw mass identities are inherited algebra from the migration record. The new target below uses them WITHOUT claiming to preserve the old ambient Q_K boundary.

## 2. New metric quantizer and explicit target change

A metric quantizer R_G must be a deterministic function of the frozen packet/history and input coordinates, independent of private walker or request order. For v, it returns q with

  q^T Gq <= v^T Gv,
  (v-q)^T G(v-q) <= tau^2 v^T Gv,  0<=tau<1.

It returns zero for zero input. One inverse-free acceptance mechanism is: propose dyadic d by coefficient significant-bit rounding; let Y=d^T Gd and C=v^T Gd. If Y,C>0, choose positive dyadic alpha<=min(1,C/Y), and test q=alpha d against the two inequalities. This has squared error no greater than norm loss. If no bounded candidate passes, retain v exactly; a strict bit-budget implementation must instead report a genuine resource failure or use an explicitly proved alternative. Exact fallback guarantees error, NOT a uniform coefficient bit bound. Small coefficient squares alone are not the metric.

Define nonterminal new rows by

  u'_(hb)(w)=B R_G(v_b(w)).

This is a NEW approximate dynamics, not an exact optimization of RP9's ambient componentwise Q_K. There is no hidden Q_K after the projection. A compatibility implementation retaining original Q_K must still reconstruct a_b, execute Q_K at the original boundary and deal with its out-of-subspace remainder. It cannot claim the reconstruction saving of this new target.

A final readout can use the raw mass formula without projecting its unobserved terminal row. This reduces the number m of projected boundaries by one. All work labels, signs, exponents and modular incidence remain explicit. There is no top-R mask; nevertheless projection or subsequent interference can make individual rows zero. Do not claim unchanged nonzero support.

## 3. Two-row sampling without an online ambient field norm

In one surviving partial trial let the latent label be W. Propose z=W or P(W) with a fresh fair coin, exactly as in the inherited two-row construction. Query only c_h(z) and c_h(P^{-1}z). Set

  S_z=c^T Gc+d^T Gd.

For S_z>0 choose bit b with

  p_b=[c^T Gc+d^T Gd+2s_b c^T H d]/(2 S_z).

The block Gram [[G,H],[H^T,G]] is positive semidefinite, so these probabilities are nonnegative and sum to one. For the chosen bit set a_mass=Q(a_b), q=R_G(v_b), q_mass=q^T Gq. Accept with

  alpha=q_mass/a_mass<=1

on positive a_mass; a zero-probability branch is never divided by. If rejected, terminate the WHOLE trial. Restart from the declared initial state, not from W or the current history. At terminal readout omit projection/quantization and accept the raw bit normally.

Induction: if incoming live mass at (h,w) is Q(u_h(w)), the proposal mass at z is S_z/2 (including proposal multiplicity when P fixes a label). Multiplying by p_b=2*a_mass/S_z and alpha gives exactly q_mass. Thus live mass is the new raw squared row norm at every step. With survival Z>0, completed output samples follow the new joint law divided by Z. Z need not be summed online. Exact rational sampling and random-source exhaustion retain their original explicit contracts.

No per-row solve GA=b, ambient 61-component row, or whole-work-field normalization occurs in these algebraic formulas after packets exist. This is NOT a claim that the coordinate-row queries or packet construction are cheap. Query recursion, label incidence, rejection and factor verification retain their real costs.

## 4. New orthogonal error combination and survival theorem

Suppose for every enabled history at depth i an actual certificate establishes

  D_h <= epsilon_i^2 G,  0<=epsilon_i<=1.

One history or a small fitted dataset is not this operator certificate. It can be checked with exact PSD methods or a conservative sufficient test during packet preparation. Missing certification cannot be silently treated as zero leakage.

For a whole field U in S, let L_i be the exact two-arm instrument, with output histories kept distinct. It is an isometry. Put M=||U||^2. The combined projection loss in BOTH bits and ALL labels is

  ell=||(I-Pi)L_i U||^2
     =(1/2) sum_w c_w^T D_h c_w
     <=epsilon_i^2 M/2.

The coefficient quantization error stays inside S, whereas the leakage is orthogonal to S. Therefore, unlike simply adding the two error bounds,

  ||L_i U - B R_G(v)||^2
  = ell + ||Pi L_i U - B R_G(v)||^2
  <= ell + tau_i^2 (M-ell)
  <= beta_i M,

  beta_i=tau_i^2+(1-tau_i^2)*epsilon_i^2/2.

This calculation is on the complete history/work/internal direct sum. It does not assume a lower bound for an individual bit probability. A nearly cancelled branch can have a large relative error; the weighted global statement remains the stated one.

Starting with unit exact V_0=U_0 in S, triangle induction and norm contraction yield

  ||V_m-U_m|| <= sum_i sqrt(beta_i),
  TV(P_new,P_exact_same_bank) <= min(1,sum_i sqrt(beta_i)).

For nonzero U_m, normalized pure-state distance is no greater than ||V_m-U_m||, and measurement cannot increase it. If the initial normalized state is already approximated, add its explicit initial distance in the corresponding comparison. Norm lower bounds give

  Z >= product_i [(1-epsilon_i^2/2)*(1-tau_i)^2].

This is survival, not factor success. For exact factor-verifier event F, P_new(F)>=max(0,P_exact(F)-sum sqrt(beta_i)); under iid whole trials with finite cost, time to a factor is E[C_trial]/(Z P_new(F)). No speed follows from the probability theorem.

Illustrative algebra only: if m=15, epsilon_i=2^-12 and tau_i=2^-13, then beta_i<3*2^-26<2^-24, hence TV to the untruncated same-bank reference <15/4096. Adding the inherited K16 target's bound15/4096 gives <15/2048 to that particular reference. THESE EPSILON CERTIFICATES HAVE NOT BEEN VERIFIED FOR THE CURRENT SEVEN/EIGHT-VECTOR BASES. tau is a metric error budget, not a claim that 13 coefficient bits suffice. No RP9 end-to-end comparison is inferred.

## 5. Exact invariant closure: how projection could be avoided

For a finite set of actual generator actions T_1,...,T_M and initial direction x_0, define

  S_* = span({x_0} union range(T_1-I) union ... union range(T_M-I)).

For s in S_*, T_j s=s+(T_j-I)s lies in S_*. Hence S_* is invariant under each generator and, because each is invertible, its inverse. With a basis B_* of this space, D_j=0 and the coordinate actions satisfy A_j^T G_* A_j=G_*. Exact ordered words can then be compiled by multiplying A_j in the original order. Gram and a preparatory factorization can be reused.

The general dimension bound is only min(61,1+sum_j rank(T_j-I)). No new small rank has been computed. If separately verified common low-rank ranges exist, they can sharpen this bound; no old-bank/other-precision range certificate is silently transferred to the b12,t16 bank. Basis construction, short integer reduction, operator coordinates and denominators must all be measured. S_* can be all61, with no dimension advantage.

This closure is for the actual LINEAR actions. The old coordinatewise ambient Q_K need not preserve it. A metric quantizer defines the new target in section2; retaining old Q_K can require ambient residual/escape coordinates and defeats any automatic closure claim.

## 6. Compression does not automatically commute with word compilation

Without exact invariance,

  A(T2 T1)-A(T2)A(T1)
  = G^{-1}B^T T2 (I-Pi) T1 B.

The right side is the part that leaves S and later returns. It cannot be dropped as an implementation detail. A symbolic padded-carrier example has B=e0 and T1=T2 the swap of e0/e1, identity on the other modes. Then A(T1)=A(T2)=0 but A(T2T1)=1. This is an algebraic interface counterexample, not a new executed native BRC fixture.

Thus a noninvariant packet must bind the FULL actual ordered phase word, or treat each added projection as a distinct new approximation boundary and charge its error and survival. Same nominal phase, hash alone, equal current norms, or generator-wise projected multiplication is not a full-word equivalence proof.

A small residual trace on one stored field also does not prove a uniform D<=epsilon^2G. For example D=diag(0,1),G=I and a field using only the first coefficient direction has zero observed leakage, while a future second-direction row loses all its acted component. State evidence and an operator certificate are different.

## 7. Cost and exact next executable unit

For a new (actual bank, complete B, exact ordered word) packet, charge r full-mode word actions, up to r^2 full BRC pairings, exact solution of GA=H, D construction/PSD verification, and all coefficient bit lengths. Known packets cost r-dimensional actions/quadratic forms, but generally O(r^2), not O(r) scalars, and H/A fractions can be long. Packet words can proliferate with t. Coordinate queries can retain the old exponential reconstruction cost. Total labels remain explicit unless separately proved otherwise. No fitting/initialization/RSS is omitted by calling the packet cached.

Next: using the exact CURRENT ATTACHMENT RP9 version, freeze one reduced basis and compute H,A,D for the first actual future words. Verify full-mode action, nonnegative raw masses and exact projected Gram masses. Test D=0 or a nonvacuous PSD leakage bound; otherwise preserve this negative result. Only then implement the distinct projected coordinate target, first on a complete small conditional tree with exact full-mode comparison, and separately benchmark packet construction plus repeated use. Do not relabel this as an equivalent RP9 implementation. Do not repeat RP9's85-row or512-output experiment as new discovery.

## 8. Actual attachment mirror, version distinction, and control

The prior current-conversation RP8 and RP9 attachment versions are now copied to Drive under folder
https://drive.google.com/drive/folders/1hz6_Oc5L2_x_gp7OSGKgcCBz6JZSoRbw
named RP8_RP9_本对话附件版本补存_20260927, inside the existing research root. Fourteen files were uploaded: each stage's run ZIP, report, proof, results, packed checkpoints, original delivery and original pending-sync record. The latter two have 原记录 in their Drive names; their historical pending status is not rewritten.

Google_Drive.upload_file rejected a manually supplied attachment reference with a validation error. The supported Files.manage_library source_file_ref upload then succeeded using the exact visible attachment snapshot IDs. This was a validation-format fallback, not an authorization bypass. Directory readback confirms all14 items. RP8 ZIP ID1W7RlQDmxmreiaFmQB_Y0f22a4xJc-OhB has35840220 bytes; RP9 ZIP ID1h76_iUbDx3uJMfiYODB-4t0z44RDX--c has54755655 bytes. No new full-hash/download/restore execution is claimed because the computation environment was unavailable. The earlier different RP8 a71213a7 cloud branch remains untouched.

RP9 report ID1eDVjRcwKVXRfsnR9lptX283XGItkjoWF; RP9 Proof ID1l5V8nqNUZAx4y3xqVi2frR6WlV0ai48Q. Source copies are not new independent experiments. This note is a faithful project landing record for the continuation and attachment availability, not upload of all historical raw bytes to GitHub.

Logical conversation remains chat-stage101-c971348e64294a5882dfc50fcc8217f1. Recovery Issue2549 returned local pointers only, source_authority_verified=false, no runs/claims/staging, original start_request_id stage101-session-c971348e-02. No new identity, RA, CLAIM, formal run/Result or admission is asserted. PRE_FINAL and final mirror receipts are recorded separately when actually returned. No schedules or sharing permissions were changed.

External context: Bravyi/Gosset/Liu, arXiv2112.08499, was checked at primary abstract level for inherited amplitude-query sampling provenance; it does not supply a cheap row oracle. Carlberg/Barone/Antil, arXiv1504.03749, primary abstract only, is general projection-based model-reduction context. Projection, invariant spaces and Gram identities are not claimed as worldwide novelty. No external theorem is substituted for the derivations above.
