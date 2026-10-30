# BU time-four repair: one statistical bit versus two pathwise bits

2026-10-30; author-side exact theorem, external finite BRC model, unreviewed / not admitted. Continuation of this folder's PROOF.md and its original 16 positive P/Q leaves. The post-terminal time-four readout is a declared model extension, not certified native time evolution.

Order the BU stage-three observer's four hidden fine leaves (j0k0,j0k1,j1k0,j1k1). **Conditioned on the observed BU coarse atom** their exact two-law distributions are:

P=(1/20,1/20,9/20,9/20), Q=(1/4,1/4,1/4,1/4).

## Theorem A: sharp minimal statistical sufficiency

One repair bit j is sufficient, in the *two-law Blackwell/statistical distribution* sense, for **all stochastic downstream leaf-readout kernels W(y|j,k)** that do not alter the original leaf distribution. Given j, k is fair (1/2,1/2) under P and Q alike. The law-independent stochastic decoder samples k uniformly conditional on j, then applies W. This yields the full joint (j,k,Y) distribution exactly under each law; arbitrary randomized W follows by kernel composition. It reconstructs probability laws, not the exact previously realized hidden k on the same path.

Zero repair bits are insufficient: on the BU atom P(j=1)=9/10 and Q(j=1)=1/2. Any decoder from that one state has a common distribution and cannot reproduce both values. Therefore one bit is **minimal** for statistical sufficiency for this specified class of future readouts.

The sharp *no-repair* conditional two-law reconstruction deficiency for the full four-leaf distribution is 1/5. Proof: TV(P_BU,Q_BU)=2/5, and the triangle inequality gives inf_R max(TV(P_BU,R),TV(Q_BU,R)) >= 1/5. The midpoint R=(3/20,3/20,7/20,7/20) attains equality. Since BU has coarse mass 1/4 under both laws for the explicit G0 policy and every non-BU probe output is deterministic, its global observer reconstruction radius is **1/20**. For the earlier optimal old observer strategy B=69/500,c=1039/1207, the BU-local radius is m/5=71691/12070000 where m=Bc/4.

## Theorem B: deterministic pathwise sufficient repair

If the state must **deterministically factor every Boolean function on the same realized BU leaf**, four distinct local states are necessary and sufficient: merging any pair of the four leaves prevents factorization of one singleton indicator. Thus two bits (j,k), rather than one bit, are needed for simultaneous pathwise query factoring. This does not contradict Theorem A, whose exactness concerns distributions with an allowed independent reconstruction draw.

## Exact verifier and limits

VERIFY_REPAIR.py exactly checks both conditional distributions, the universal j-to-k fair kernel, each of the 16 Boolean BU subsets, the sharp midpoint's two TV errors, and singleton separating events for every pair of leaves. The universality over all randomized future kernels is the algebraic composition argument above; the 16-query enumeration checks the finite deterministic generator family, not unbounded operation classes.

A controlled future intervention able to change the k transition may invalidate the shared fair-k decoder; formulate its causal kernel and provide either a new sufficient state or a formal counterexample. The law-level result is external finite BRC; native P000 X6 embedding and independent time dynamics remain distinct obligations. See NEXT_TASK.md for continuation.
