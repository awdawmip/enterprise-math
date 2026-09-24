# Heartbeat67 — common instruments, four-code obstruction and correlated-record recovery

Progress-Event-ID: HEARTBEAT67-COMMON-READER-20260925-67C4
Status: SAME_AUTHOR_CONDITIONAL_MODEL / ACTUAL_TYPED_BRC / NOT_ADMITTED
Researcher-ID: none newly assigned. Research-Activity-ID: unavailable. Earlier session registration was safety-blocked; this turn did not retry, bypass, borrow a closed identity, or fabricate pre_final approval.

## Scope and durable frontier

Continue Stage66 cumulative 2b85d54e3f2016acb071620da1b3d7645c7a677f; mounted parent bundle SHA256 ad0ff506ab5e8b48c8e9c9a3e1af026c67a02dff9ad2ef50ba4c166ee21bd6b1 verified. Global read c1c464c3e8e71f4312bbde67ab0488b851747438; source/control read c47e13e4aba0e006366f989d6334d443f6333ae3. Unchanged bootstrap/manual/P000/worldview/BRC-only and Stage66 source blobs were reused. Six native spatial axes, source identity and residual fidelity are unchanged. Four code states and qubit pointers are equal-energy internal registers, not additional spatial directions. Full old material/ports/Gauss field/bank/live returning receivers remain in S. New record preparation sigma_AI may be mixed/correlated across records, but is initially independent of S and its reference. Initial S/apparatus correlations require the full apparatus-valued blocks, not the factorized channel formula below.

## 1. Common outcome criterion

Actual controlled record unitary V=sum_i |i><i| tensor V_i. A is accessible record, I inaccessible. A single physical POVM E_r gives H^r_ij=Tr[(E_r tensor I) V_i sigma_AI V_j*]. The raw code/full-field instrument is J_r(rho)_ij=H^r_ij rho_ij. Every H^r is PSD by the Hilbert-Schmidt Gram construction; sum_r H^r_ii=1. Noisy classical reports use sum_r C(y|r)H^r, with weights applied once. Normalize ALL blocks by the same likelihood and use the posterior in the next operation.

After outcome-dependent diagonal phases d_ri, corrected multiplier R_ij=sum_r d_ri conjugate(d_rj)H^r_ij. Exact correction of every unknown code/reference input is equivalent to R=all-ones. A sum of PSD matrices with rank-one output forces EACH corrected outcome onto that same one-dimensional support. Necessary and sufficient: H^r_ij=p_r conjugate(d_ri)d_rj, p_r>=0, sum p_r=1. Equal outcome weights for all configurations AND consistent rank-one phases are required. Independently maximizing every pair does not give a common instrument.

## 2. Four legal rational records: all pairs recover, all four do not

Conditional pointer vectors are v0=(1,0), v1=(0,1), v2=(3/5,4/5), v3=(3/5,4i/5). Actual full unitary blocks I,X,F,diag(1,i)F generate them from one ready pointer; F=[[3/5,4/5],[4/5,-3/5]]. Non-ready columns and true adjoints were tested too. No invalid Gram matrix is introduced.

For any effect E=[[a,z],[conjugate(z),b]], equal outcome probabilities for v0,v1 require a=b; adding v2 requires Re(z)=0; adding v3 requires Im(z)=0. Thus a nonzero correcting effect would have to be aI. Because the vectors span the qubit, its induced H has rank2, contradicting the rank-one criterion. No pointer POVM followed by phase-only code feedback can perfectly restore all four unknown configurations. Any sequential pointer-only measurement reduces to such a POVM. This is a restriction on this fixed instrument/access class, NOT fundamental irreversibility, and not a bound against new coherent source-pointer interactions or amplitude re-preparation/filtering.

Actual pair protocols: pointer Y measurement plus rational-complex phase feedback restores code subspace {0,1,2}; X restores {0,1,3}; Z restores {2,3}. All six pairs were executed at four relative phases with an entangled reference and entire density equality. They require DIFFERENT settings. X/Y/Z name internal pointer observables, not native spatial axes. Rational Naimark gates avoid numerical square-root eigenvectors.

For the balanced four-code state prepared by actual H4 (entries +/-1/2), return-to-preparation probabilities are: unread109/200; common X or Y37/40; common Z29/40; complete coherent joint inverse1. Y restores all first-three cross terms but leaves code3 cross terms multiplied by4/5. Its plus outcome probability is1/2 for each of codes0,1,2 and49/50 for code3, so the result still reveals the fourth configuration. All samples count; neither initial-state replacement nor selected successful subensembles are used.

## 3. A strict quantitative bound for EVERY allowed POVM

Refine E_r=t_r|q_r><q_r|, norm q_r=1, sum t_r=2. With p_i=|<q|v_i>|^2 the entanglement fidelity for the maximally entangled four-code/reference test obeys F_e <= sum_r t_r(sum_i sqrt(p_i))^2/16. Same expression is the balanced-code echo for phase-only correction. The Cauchy gap equals sum_(i<j)(sqrt(p_i)-sqrt(p_j))^2 >= sum_(i<j)(p_i-p_j)^2/4.

Actual BRC pointer densities give Bloch rows (0,0,1),(0,0,-1),(24/25,0,-7/25),(0,24/25,-7/25). These are auxiliary two-state algebra coordinates, not space coordinates. The positive BRC two-layer Gram graph gives S=sum_(i<j)(r_i-r_j)(r_i-r_j)^T=[[1728,-576,-336],[-576,1728,-336],[-336,-336,5196]]/625.

Exact certificate: 625 n^T S n=816||n||^2+576(nx-ny)^2+336(nx-nz)^2+336(ny-nz)^2+3708nz^2 >=816||n||^2. For unit n, sum_(i<j)(p_i-p_j)^2>=204/625. Summing outcome weights yields F_e<=4949/5000<1. This ceiling is conservative, not the computed optimum, and is not inferred from testing X/Y/Z. No eigensolver or numerical continuous optimization. A uniform complete-record test-state perturbation of trace distance delta can raise the bound by at most delta; no laboratory calibration error was estimated. Full joint V* still restores exactly and was actually executed.

## 4. Mixed correlated records can admit one common recovery

If all accessible conditional record unitaries commute, their common spectral projectors P_lambda satisfy V_i P_lambda=exp(i theta_i,lambda)P_lambda. For arbitrary mixed/correlated sigma, the induced H^lambda_ij=p_lambda exp(i(theta_i,lambda-theta_j,lambda)), with p_lambda=Tr(sigma P_lambda). This obeys the common criterion and restores unknown S/reference after phase feedback. An unaccessed purification may remain conditioned/dephased; the claim is NOT reset of all apparatus registers.

Actual locally prepared example: sigma_corr=(|00><00|+|11><11|)/2 versus sigma_prod=I4/4. Both pointer marginals are I/2. A ready four-state preparation register, actual rational H4 and controlled copies generate pure purifications; no numerical random mixture or reset. Conditional V_i=F^bit0 tensor F^bit1. Single-pointer overlap Tr(sigma_local F)=0 in both, but the code00/code11 JOINT overlap is9/25 for sigma_corr and0 for sigma_prod. Multiplying marginals incorrectly deletes the former residual.

The actual two-pointer eraser and phase feedback recover the ENTIRE four-code/reference state in both preparations. Correlated reports ++ and -- each have probability17/50, +- and -+ each4/25; independent preparation gives1/4 each. All outcomes included. A spanning preparation set and an entangled four-code/reference state were checked, not only one histogram.

## 5. Code size belongs in the effective-collapse certificate

For a valid d-code Schur matrix with |C_ij|<=gamma off diagonal, arbitrary source/reference input obeys trace distance to full nonselective code dephasing <=min(1,(d-1)gamma/2). Proof: positivity gives ||rho_ij||_1<=sqrt(p_i p_j), then sum the blocks. If every off-diagonal coefficient is the same real gamma, the sharp worst-case bound is gamma(1-1/d), attained by the balanced code state. An average over d diagonal phase unitaries gives the upper bound.

For a SEPARATE uniform four-code channel family, actual BRC C4 probability flags have weights (1+3c)/4,(1-c)/4,(1-c)/4,(1-c)/4. After m independent physical rounds, off-diagonal gamma=c^m. At c3/5, two-code gamma/2 passes tolerance1/10000 at17, but uniform four-code3gamma/4 needs18; general four-code3gamma/2 needs19 in this example. This is NOT a claim that the qubit-pointer counterexample has uniform overlaps. It does not count HTTP retries or copies of old symbols. Common future channels preserve the unselected error bound; rare conditioning can amplify it and future access to a hidden record changes scope. Nonselective dephasing is not a derivation of one objective outcome.

## 6. Reader and actual native-field execution

CommonInstrumentReader constructs a whole outcome family from actual BRC marker/measurement/feedback columns, preserves full-field blocks, applies noisy-report probabilities once, and writes back the normalized posterior. It refuses a fictitious pairwise_best setting. Snapshots passive, same-event retry idempotent, conflicts atomic. Sixteen three-step ideal/noisy histories match full apparatus propagation as raw likelihoods and whole conditioned states.

Inherited twelve-neighbor stored fibre weight4/625 is retained. Added equal-energy four-code register and pointer are local internal modes. Actual H4 plus a local bank-controlled phase, marker and Y correction give72 marked endpoints,192 corrected endpoints,2304 full-field/code density pairs, matching the complete instrument. Additional native movement gives384 endpoints. All retain Gauss D ell=delta_xplus-delta_xminus, same source identity, separation<=1 and declared energy3; pointer/code degeneracy does not make preparation/control free. Correlated mixed correction restores this full field/code state and keeps3072 apparatus endpoints. Actual marker and native-motion inverses pass.

## Execution, delivery, sources and boundary

238 grouped named checks,30 actual unchanged canonical BRC core calls per final process. Core bc7babbb9e890f6d5a7094430a5fbdccf66c77ad:src/enterprise_math/brc_weighted_recurrent.py, blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb, SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26. Existing C4 pair observer and native stages reused. New Q(i) gate compiler uses actual positive recurrent powers, not ordinary numerical propagation. Positive amplitude branches, phases, probabilities and full endpoints remain typed.

Cumulative10b008d2945fd27e966ae00a45ecf396d043a3fc; entrySTART_HERE_STAGE67.md; stage67/common_reader.py,run.py,PROOF.md,RESULTS.json,BRC_CONTRACT.json,PROVENANCE.json,MANIFEST.json. Fresh LOCAL clone replay exactly matches all scientific fields, excluding only elapsed_ns recursively; original5440459699ns and replay4972016983ns retained.1268 inherited files unchanged;8 manifest hashes and git fsck pass.

Bundle BRC_Heartbeat_common_reader_stage67_20260925.bundle:38103933bytes,SHA256cc22b11a37cd57e83ed41e203dc1edf703d2e3e59aaad2bbf6b3cd8758d7e68a. Drive1rCy1dGN-js2vJBbziGPnpfFPfcYNJ9tV uploaded/fetched; returned bytes compared IDENTICAL. ProofSHA2561df2a0edec8e957cad188299f621dd1498af6ce7a8d714ed85f513cd654d4337; codeSHA256e81ad11f3170db9f29714a85e826a5fecc22da1871eb572c84f6ceea91cde9b9; resultsSHA256c39148bcf488cff36b24225e9ebf31c849d3c4e2f6726be5ffa1290ae72bee52.

Primary sources: Gregoratti-Werner quant-ph/0209025v1 abstract; Buscemi-Chiribella-D'Ariano quant-ph/0611070v1 parsed PDF sections2-3 (screenshot attempts cache-miss, no successful visual audit); Helm-Strunz0910.5364v1 abstract; Trendelkamp-Schroer etal1110.4806v1 abstract. General environment-assisted correction and non-random-unitary dephasing in dimension4 are prior art. No exhaustive novelty claim or dedicated-provider retrieval. Same-author proof/code/replay, no independent review, Lean, empirical fit, GUI/HTTP test or remote reader deployment.

NEXT: optimize one physically restricted common reader with independently calibrated mixed-record error, then a local many-port propagation/capture experiment with held-out input. Do not repeat the six-pair/common obstruction as new work. Native phase/Born origin, autonomous timing, preparation/recycling costs and geometry-derived spatial fringes remain open. Evidence preservation does not close the broad physics objective or repair the unavailable activity registration.
