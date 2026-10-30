# BRC N=4 — unrestricted stochastic three-code sharp minimax

2026-10-31 (Asia/Shanghai). AUTHOR_ANALYTIC_PROOF / UNREVIEWED / NOT_ADMITTED. Fixed GLOBAL_KNOWLEDGE_V1 main@59d5d56fb822c634b268128ae4ae1d1b15f29d13 and Enterprise Math main@92ea1758627b6620538af4acadc1163fd56ef6d8. Direct continuation of PR #1757 commit d11461c27eae8e932a674dbba6684a3879875b0f (R4 = 1/5). No native CLAIM, Result, Driver review or external Heartbeat dynamics are asserted.

## Exact experiment and observer

The original BRC N=4 experiment has 16 strictly positive leaves under each of P and Q, and eight prepared inputs (S,b), S in {AU,AV,BU,BV}, b in {P,Q}. Each third-stage class has two equally likely conditional fourth-stage K leaves. AV_P/AV_Q have identical conditional futures and BV_P/BV_Q likewise. The six distinct prepared conditional distributions, with rows AU_Q,AU_P,AV,BU_Q,BU_P,BV and columns AU0,AU1,AV,BU0,BU1,BV, are:

M = (1/20) [
 [10,10,0,0,0,0],
 [9,11,0,0,0,0],
 [0,0,20,0,0,0],
 [0,0,0,10,10,0],
 [0,0,0,2,18,0],
 [0,0,0,0,0,20]
].

P/Q original leaf-pair counts are AU_P=(9,11), AU_Q=(10,10), AV_P=(5,5), AV_Q=(20,20), BU_P=(3,27), BU_Q=(15,15), BV_P=(30,30), BV_Q=(15,15); each pair value is duplicated at the two fair K leaves. Each law sums to 240 across all 16 leaves. The six class likelihood ratios are 9/10,11/10,1/4,1/5,9/5,2; they are distinct.

The common encoder E maps each of eight preparations to at most three symbols stochastically, before J and before the future legal policy is chosen. For each policy H the decoder D_H may itself be stochastic and policy-specific. Its target is the entire public terminal record O=(T,Decision,Z_BU), with BU-only sensor Z=J xor Bernoulli(epsilon), absent outside BU. This is distributional reconstruction, not same-realized-path recovery. Let F range over all lawful adaptive S23 or S2 policies and define

R3(F;epsilon) = inf_{E (row stochastic; <=3 symbols)} sup_{H in F} inf_{D_H} max_{x (8 preparations)} TV(L_H(.|x), (E D_H)(.|x)).

## Theorem

For every real 0 <= epsilon <= 1/2,

R3(all lawful S23;epsilon) = R3(all lawful S2;epsilon) = **1/2**.

This is exact for arbitrary cross-source randomization of the common encoder, and policy-dependent randomized decoders.

## Lower bound for every stochastic three-symbol encoder

Restrict E to the six representative rows, yielding a 6-by-3 row-stochastic matrix (the full eight rows remain covered by the final max). The four-dimensional subspace W of R^6 consists of w=(a,a,b,c,c,d). The linear map W -> R^3, w -> w^T E, has a nonzero kernel, because dim W=4>3. Choose any nonzero w in that kernel. Stochasticity E*1=1 implies sum_i w_i=2a+b+2c+d=0.

Direct exact multiplication gives

w^T M = (19a/20,21a/20,b,12c/20,28c/20,d).

The two AU coordinates share the sign of a; the two BU coordinates share the sign of c; provenance groups have disjoint class supports. Therefore the L1 norm is preserved EXACTLY:

||w^T M||_1 = 2|a|+|b|+2|c|+|d| = ||w||_1.

Moreover sum_j (w^T M)_j=0. Every subset A of the six likelihood classes defines a **lawful** H_A: continue all preparations at stage two, stop all at stage three, choose terminal Decision=P precisely on classes in A. The six ratios are distinct, so the equal-likelihood-ratio S23 constraint is satisfied; the S2 equal-continue AU/BU constraint is also satisfied. There are exactly 64 such lawful tests, none observing K.

Under H_A, actual Decision=P probabilities form M*1_A. Let d_A in [0,1]^3 denote the code-specific Decision=P probabilities of the decoder for H_A. If full-public-record TV errors are uniformly <=delta, then for each prepared row i the absolute difference of these decision event probabilities is <=delta. Because w^T E=0, for every A,

|w^T M*1_A| = |w^T(M*1_A-E*d_A)| <=delta*||w||_1.

For any zero-total signed vector v, max_A |sum_{j in A} v_j| = ||v||_1/2. Hence using all 64 **legal** H_A gives

delta >= ||w^T M||_1/(2||w||_1) = 1/2.

Unattained decoder infima are treated by using delta+eta and sending eta down to zero. The argument uses only a measurable event of the COMPLETE public record and is unaffected by the real epsilon value. It applies to S23 and, by inclusion of these H_A, to S2.

## Upper bound for every lawful adaptive policy

Use exactly three deterministic code symbols CA, CB, CV. Both AU preparations map to CA and its common reconstructed class distribution is (19,21)/40 over (AU0,AU1). Both BU preparations map to CB and reconstruct (12,28)/40 over (BU0,BU1). Both AV and BV preparations map to CV and reconstruct AV with probability 1/2 and BV with probability 1/2. Draw the declared fair K leaves and applicable BU sensor from these reconstructed futures, then execute the **same** chosen causal policy H and its randomization.

On the complete six-class future, the six representative row total-variation errors are exactly

(1/40, 1/40, 1/2, 1/5, 1/5, 1/2).

The duplicate AV and BV preparations have the same bounds. Fair K, sensor, legal stopping, decisions and adaptive randomization are shared stochastic postprocessings of the complete labeled future, so data processing bounds every full terminal-record error by 1/2 for all S23/S2 H and real epsilon. The same encoder works regardless of H. Combining bounds proves R3=1/2.

## General BRC provenance-group obstruction (proved lemma)

For a row-stochastic experiment M whose rows are partitioned into G nonempty provenance groups with pairwise DISJOINT output class supports, and a policy language containing every binary output-class subset test, every stochastic k-symbol common encoder with k<G has worst-case max-row decision-event TV >=1/2, even with test-dependent stochastic decoders. Proof: the G-dimensional row vectors constant on each group have nonzero intersection with ker(E^T), since rank(E)<=k<G. For such w, stochasticity makes sum w=0; positivity and disjoint supports preserve ||w^TM||_1=||w||_1. Taking the maximizing legal subset yields 1/2. This lemma is a LOWER bound only; our BRC experiment separately supplies the matching three-symbol reconstruction. It identifies the exact branch provenance irrecoverable under all class-subset future queries.

## Verification and scope

VERIFY.py (Python standard-library Fraction) was actually executed. It checked original P and Q 16-leaf strict positivity and normalization; all 64 lawful third-stage decision subsets for 6 input rows and 4 exact sensor noise levels (1536 COMPLETE public-output TV checks); the displayed 3-code future-error vector; group-constant kernel witnesses for ALL 729 deterministic 6-row 3-symbol encoders and 256 seeded exact rational stochastic encoder examples. Marker: PASS_BRC_N4_UNRESTRICTED_THREE_CODE_SHARP_20261031; see RUN_EVIDENCE.txt. Universality over stochastic E, real epsilon and adaptive H follows from the ANALYTIC proof above, not from the finite tests.

This is a model-conditional finite statistical-experiment theorem within typed positive-rational BRC, using lawful source/branch/observer operations. It does not derive a physical six-axis Cell transition or an independent time law from P000. The P000 ACTIVE locked research worldview and existing theorem-admission roles are unchanged.