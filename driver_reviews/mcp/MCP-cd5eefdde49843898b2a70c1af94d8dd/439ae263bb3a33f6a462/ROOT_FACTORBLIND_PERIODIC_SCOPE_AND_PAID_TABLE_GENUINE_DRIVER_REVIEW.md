# Fixed-period negative scope and paid explicit-wheel lower bound

Driver-ID: EM-DVR-FBF223 / CONTROL_PLANE
Driver-Session: MCP-cd5eefdde49843898b2a70c1af94d8dd
Driver-Authority: DA-A1DB35C00ED2F8C2A9FA
Task: RS-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE
Publication: TP2-A712090E5314373E5447
Frozen-Result: RR-C5769D6B237D02BFF025
Status: CURRENT_DRIVER_MATHEMATICAL_REVIEW_REPORT / NO_TASK_COMPLETION_REQUEST / PARENT_OPEN

Root is reviewing the existing return as the original current Driver; no new research execution claim or actor is created. Root's disclosed prior identities are EM-DVR-FBF223,EM-DVR-4C90FB,EM-DVR-C1A1D9,EM-DIRECT-E1F2B6,EM-DIRECT-FA0C27,EM-DIRECT-49ADE6. The original frozen author is EM-SMSB1-73D4C2. The auxiliary reader /root/backlog_latest_status_audit is UNKNOWN / DIRECTED_NONBLIND and grants no native authority. Root and auxiliary reader have read the existing return; no blind or clean-room replication is claimed. This note separates the old preserved result from a new conditional Root review lemma.

## Exact current evidence

Own actual continuation559 (real bridge issue5011,terminalcomment6135764562) provides an unrestricted verified Driver-review view and reports FROZEN_RETURN/AWAITING_REVIEW with no live claim. It grants no researcher execution. Immutable Source406f74e0e2fa833389245ebb26fc24e6e777679b was cold-fetched for13 complete files90345B; every length/SHA256/Git blob is verified. This includes the full original RR,publication,Taskbook and all10 RR outputs64999B. The old600-case and1400-row checker results are retained; none is rerun here.

Original RR SHA2561149fb488e66bdff40cd52b79b1566400c4691b8254ec884aa113a4a4d7c934f / Git blobd843b127e82605255e394a21db6a3728db0c0d6d. Original Taskbook16534B,SHA25650934aad4f07e43f52ff6970387392fb9d91d58cda2d98b6015fdd8a30222779,blob b4f6de7d80bf30345ad827e280affff7a4be2ebc. Original return15896B,SHA25627359fab6b2faeeb7cd1528d1473e37e67f359bfdd601f31a693521984a41eff,blob1d0d102aadecfce49938ef45ecd0992ea209bfc4.

The raw verdict remains NEGATIVE_BOUNDARY. Preserve its hard-target disposition verbatim:

> NO_S1_NO_S2_NO_S3. Exact closure: every fixed finite factor-blind Fermat-offset filter periodic with fixed period M and retaining the true offset T necessarily retains at least floor(T/M)+1 candidates through T, so it cannot yield o(T) candidate count. Empirical closure: the frozen SHELL_RESIDUE_QR_CONDITIONAL_V1 feature family loses high-recall multiplicative-shell localization on the 600-case adversarial challenge; exact search wrapping is noncompetitive outside the near-twin regime, where matched Fermat is already stronger.

## 1. Independent reconstruction of the old exact boundary

For odd semiprime N=pq with3<=p<=q, define c=ceil(sqrt(N)),T=(p+q)/2-c,B=(q-p)/2. Then (c+T)^2-N=B^2. A per-N offset predicate F_N on nonnegative integers has periodM if F_N(t+M)=F_N(t). Fixed finite moduli have common period their lcm. If F_N(T)=1, induction gives F_N(T-jM)=1 for every0<=j<=floor(T/M). Consequently the distinct candidates retained in0..T number at leastfloor(T/M)+1. This proves the exact finite statement, and Omega(T) when one commonM is fixed whileT grows.

One explicit unbounded parameter family is N_q=3q for odd primesq>=5. Its T_q=(q+3)/2-ceil(sqrt(3q)) tends to infinity, since T_q>=q/2+1/2-sqrt(3q). Any fixed-period full-recall predicate therefore has candidates/T_q>=1/M. This family establishes the parameter range for the candidate-count result. It is trivially factored by trial division3 and supplies no factoring complexity lower bound.

The no-go does not exclude fixed-factor compression (the oldM=27720 wheel actually achieves finite constant factors), variableM, nonperiodic/adaptive rules or99% distributional recall. The full30-dimensional feature family includes N-size information and shell quantities and is not itself an offset-periodic predictor class. The three coarse fingerprint collisions do not establish full-feature indistinguishability. The frozen RF/KNN600-case high-recall failure is finite empirical evidence about those frozen methods, not every predictor on those features. N-derived determinism preserves information without proving that an algorithm cannot improve computational cost.

## 2. New Root contribution: growing period with a paid explicit table

This new lemma is derived during the current Driver review; it is absent from the original RR and does not amend its pins, verdict or manifest.

Fix a single instance, integersT>=0,M>=1, and a predicateF_N with periodM andF_N(T)=1. LetC_N(T) count its retained offsets in0..T. Suppose the evaluated implementation, for this instance, explicitly constructs allM cells of a complete period table and scans every retained offset throughT. The accounting charges at leastlambda>0 per constructed cell andmu>0 per scanned retained candidate, without free preprocessing or cross-instance amortization. Lambda andmu are constants in the declared accounting model. Construction and checking are distinct additive operations; a shared operation is not charged twice. Then

    W_N(T)>=lambda*M+mu*C_N(T)
           >=lambda*M+mu*ceil((T+1)/M)
           >=lambda*M+mu*(T+1)/M
           >=2*sqrt(lambda*mu*(T+1)).

Proof: writeT=aM+r with0<=r<M. The original periodic argument suppliesa+1 candidates, anda+1=ceil((T+1)/M)>=(T+1)/M. Add the stipulated explicit-table cost, then apply AM-GM to the two positive terms. This holds for everyM, includingM=M(N) chosen from public data or adaptively before this table is built. T=0 is covered by the same integer endpoint. No experiment or factor label is needed to prove the inequality.

The unconstrained positive-real relaxation is minimized atM=sqrt(mu*(T+1)/lambda). WithM>=1 its relaxed minimum is instead at1 ifmu*(T+1)<=lambda. This only describes the lower-bound tradeoff; it neither constructs a factor-blind filter with one true residue nor asserts exact integer-optimum rounding or attainment of the bound. M is chosen by the actual implementation and T remains hidden.

This is a lower bound for the specified explicit-table-plus-enumeration implementation, not for all factorization algorithms. Compressed CRT/implicit tables, rank/select or batch treatment without inspecting each retained offset, reused/amortized tables, and algorithms that exploit more than this predicate require distinct accounting and are not excluded. The inequality permits square-root-scale improvement over a linear Fermat scan; it does not prove such improvement is achieved or rule out constant-factor gains. It does not grant S1,S2 orS3.

## 3. Actual scope judgment and next direction

The existing result is mathematically sound at its stated exact-periodic and frozen-empirical negative scope. The Taskbook's unique third success alternative reads:

> 3. **Exact negative closure：** 证明一个覆盖目标 feature class 的 no-go，或构造足够强的无限/参数化反例族，解释为何该类 N-derived shell observable 不可能产生所需 localization/search gain。

A review may accept the raw limited NEGATIVE_BOUNDARY without asserting all allowed N-derived feature mechanisms are impossible. The periodic theorem covers the periodic class; the600-case experiment does not extend that theorem to arbitrary predictors on SHELL_RESIDUE_QR_CONDITIONAL_V1. The new paid-table lemma remains conditional on the declared implementation, and does not supply missing universal coverage or a full total-cost benchmark. Task completion is not claimed in this report; any current native disposition and followup must be checked against the exact Task contract and actual review flow.

The scientifically useful remaining direction is to test whether a factor-blind implicit/CRT wheel can construct or index surviving classes with preprocessing sublinear in the full period, and whether its complete paid search cost beats an equally optimized matched residue-wheel/Fermat comparator beyond near-twins. This is a scope proposal, not a published new Task or a positive method. Existing residual-priority/Hart taskbooks are preserved without duplicate dispatch. Nonperiodic/adaptive/algebraic bridges and the mother factoring objective remain OPEN. No Foundation,Working Truth,L4 or General Math Tool promotion is requested.

Auxiliary mathematical review of the new explicit-table lemma: UNKNOWN / DIRECTED_NONBLIND,3404B,SHA25662d3c4623b61a050bdb9f63de8c8a23f45ca44a9e746d4a2f470050d2818e803,Git blob104f187c1e75270a6d324a73c9f25d52c20e19ef. It independently checks the integer endpoint and positive additive cost proof, including the constrained relaxation boundary; it grants no native acceptance. The existing scientific return is reviewed for ACCEPTED at its raw scoped negative boundary with NONE as destination. The whole Task negative-alternative satisfaction and actual native review record are distinct facts; no followup_spec or Taskcompletion is requested here.
