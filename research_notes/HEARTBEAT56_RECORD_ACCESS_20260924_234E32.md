# Heartbeat56 — local record transport and an effective-commit error certificate

Progress-Event-ID: HEARTBEAT56-RECORD-ACCESS-234E32-20260924
Researcher-ID: EM-DIRECT-234E32
Research-Activity-ID: RA-977C6E764220D820C2AB78C5
Status: CONDITIONAL_MODEL_DERIVATIONS_AND_BRC_EXECUTION / NOT_ADMITTED

## Provenance and actual delivery

Continue Stage55 standalone0e8d0d46f2ab96f4d73cf355798024d90e8bb834, not its completed checks. Global read08e8fd804a16c2b6a73aa6b9dbbe274b0f92af11; control read82f3f405a994c63be5e82f1a3beb66d7b238734a. Own native registration Issue1899/requesthb56-session-20260924-73c9e1, sessionMCP-181caf355c7a42dea99ea57cf6bac308, Source39c30691aefc3c95abfb13efa0966f5d959b0cab. No formal Task/CLAIM/run/review. All prior authors retained; no independence claim. P000/X6, protected worldview and heartbeat-as-self-consistent-snapshot unchanged. N is emitted-record count and L is circuit depth, neither automatically physical time.

Cumulative standalone1155ab6e7cd9c902e45f5259ea245ceccf34c271, entrySTART_HERE_STAGE56.md. Full proofstage56/PROOF.md SHA256afa692a652a2a7a1429a1f51167a22b0da19ec4fb99553fc602b08a6093009af; resultsSHA256286e770f120f6f41e7686d18bd5ba9688323d1605c90c7ee92c28c6c921d4e2a. Implementationstage56/records.py,run.py and BRC_CONTRACT.json. BundleBRC_Heartbeat_record_access_stage56_20260924.bundle,37668961bytes,SHA256ce8d2e7cf64f80560b90caf4f367d11e8753e4bba8b3b615133ffdb87ca1100b. Drive1rLpfFAr_uZcKHj-KGF0TM3jzHlFU-VFp; actual cloud bytes IDENTICAL. Fresh clone from cloud-returned bytes replayPASS564 grouped checks/44 actual BRC core calls;1160 tracked files compared,1149 inherited files unchanged,git fsckPASS. All parent bundle refs preserved under explicit local namespaces. Frozen results and original timings unchanged. Verified2026-09-24T04:33:13.698952+00:00.

## Actual BRC route and assumptions

Unchanged canonical corebc7babbb9e890f6d5a7094430a5fbdccf66c77ad:src/enterprise_math/brc_weighted_recurrent.py; Stage45 nonnegative rational C4 cover/recurrent_mass_power; Stage50 full-endpoint character/ordered-pair observer; Stage53 rational gate compiler and fresh-record pair channel. New local record circuits use actually compiled controlled reflections, SWAP and CNOT coefficients. Positive weights, mixtures, phase and Born readout remain distinct. No pi,trigonometry,matrix exponential,eigensolver,SVD or substitute numerical propagator was run. Complex linearity,inner product,Born readout,ideal effects and the constitutive circuit remain bridge assumptions. Source/energy compatibility composes with Stage55 under commuting-projector conditions; its full mobile experiment was NOT rerun as new science.

## 1. Creating records differs from spreading an old record

An environment-only unitary W_E preserves every material marginal: Tr_E[(I tensor W_E)rho(I tensor W_E*)]=Tr_E rho. It may change recovery under restricted access,not the material reduced state itself.

For c,s>=0,c²+s²=1,one partial record has E0=|0>,E1=c|0>+s|1>. Nearest-neighbor CNOT fanout to N initially blank cells gives E0=|0^N>,E1=c|0^N>+s|1^N>; total overlap remains c at every N. N FRESH direct material-record couplings instead give E1=(c|0>+s|1>)^tensor N,overlap c^N. Calling the fanout copies independent would manufacture extra decoherence. It does not clone unknown nonorthogonal states: an isometry to independent copies would require c=c^N,impossible for0<c<1,N>1.

## 2. Recovery norm and exact commit-surrogate error

For balanced arms |Psi>=(|0,E0>+|1,E1>)/sqrt2,normalized conditional environment states,and partition E=A tensor B,define K_A=Tr_B|E0><E1| and C_A=||K_A||_1. Accessible rho_SA has offdiagonal block K_A/2.

The maximum averaged coherence recoverable by a POVM on A and result-dependent diagonal material phases,retaining ALL outcomes and allowing no material reset,is C_A. Proof: a corrected multiplier is Tr(TK_A) with T=sum_m exp(i theta_m)E_m a contraction via Naimark dilation,so its modulus is at most||K_A||_1. A unitary attaining the trace-norm variational expression and its spectral effects attain equality in finite effective dimension. This general identity is explicit PRIOR-ART REUSE: Miatto etal.1502.07030v2,p.2,Eqs3-6. Our rational examples use declared effects(I±F)/2 and C4 phase corrections,no numerical diagonalization. No universal random-state half-environment threshold is imported.

Let bar(rho)_SA be the same state with only the material crossblocks set0,as a COMPARISON STATE,not an asserted physical deletion. Then delta=(1/2)[[0,K_A],[K_A*,0]],so its singular-value pairs give D(rho,bar(rho))=(1/2)||delta||_1=C_A/2. Consequently EVERY accessible event probability differs by at most C_A/2. Any finite later adaptive accessible protocol,including its full outcome transcript,induces an initial accessible effect and obeys this same bound,provided it does not regain access or interaction with B. Unequal initial arms give|alpha beta|C_A. K independent preparations obey the telescoping bound min(1,K C_A/2); nonzero residual is not invisible with unlimited resources.

This separates maximum recovery of a retained unknown phase from re-preparing a known coherent state. Enlarging accessible A cannot reduce C_A. Actual many-to-one physics is not ruled out; the result is an operational comparison for a stated horizon.

## 3. Record structure determines the boundary

Product conditional states factor K_A=<b1|b0>|a0><a1|,hence C_A=|<b1|b0>|. N fresh records with common overlap c and k accessible give C_A=c^(N-k). Actual controlled inverse of accessible records attains this; all-outcome POVM and conditional Z feedback does likewise,including a material entangled with an independent reference. Four C4 input phases and the reference example were checked; no re-preparation or postselection is reported as recovery.

For one partial record fanned out to N cells,any missing copy gives K_A=c|0_A><0_A|,C_A=c. Accessing all gives1. For c0 a missing orthogonal copy gives exact zero within this scope; for finite N and0<c<1 fresh-record tails remain nonzero.

Counterexample to a universal all-records rule: E0=(|00>+|11>)/sqrt2,E1=(|00>-|11>)/sqrt2. Material coherence is0; access to either one record gives K=diag(1/2,-1/2),C_A=1. Its computational measurement plus conditional Z feedback restores coherence. This is a deliberately correlated preparation,not a typical-environment or autonomous-preparation claim.

## 4. Local reversible conveyor inside native X6

One degenerate-energy register resides at each integer z e1 of a chosen native axis,initially known|0>. The material logical arms are at a chart origin,not an ontological distinguished origin. One chosen round: on-site controlledF,parallel even-bond SWAP(2j,2j+1),parallel odd-bond SWAP(2j+1,2j+2). Each interaction is on-site or exactly one native edge. Even contents move two sites right per round,odd contents two sites left. Fresh known vacuum enters0; after N rounds the used records lie at2,4,...,2N.

Sparse representation lists only nonzero register bits; omitted entries mean known|0>,NOT traced or unknown. Every finite round has finite excitation support on the infinite reference tensor product; no finite reflecting box or state truncation. Both half-layers and inverse gates are executed. This is a controlled transport example,not an isotropic bath derived from P000. Registers do not change material/source positions or link load; the layer commutes with prior source/energy constraints when its logical projector does. Degenerate record energy does NOT mean preparation,control,supply or reset are free. N new resources at finite N are not one finite-resource preparation for all time.

## 5. Effective commit and local recovery costs

At snapshot after N emissions,freeze further forward transport during recovery and grant access to radius R. There are k=min(N,floor(R/2)) used accessible records. Hence C(N,R)=c^(N-k),and the event-probability error versus the crossblock-cut comparison is C/2.

Actual c3/5,N12 full state has4097 nonzero endpoints. For R0,4,12,20,24 the exact C values are531441/244140625,59049/9765625,729/15625,9/25,1. For tolerance1/100,nine missing records give19683/1953125>1/100; ten give0<59049/9765625<=1/100. AtR4 every accessible event error is at most59049/19531250. These are exact synthetic BRC predictions,not measured physical residuals. Tolerance is an observer/resource choice,not a collapse constant.

Constructive recovery for a record at p>=0: swap along p native edges to origin,undo F there,swap back. Cost2p+1 serial elementary layers; displaced intermediate records are restored,not erased. Undoing k records at2,...,2k costs2k²+3k by this nonoptimal serial construction. Reversing the full original conveyor costs3N chosen layers and returns the entire input.

Conversely,L nearest-neighbor recovery layers with final readout in radius R have backward influence region within R+L,provided classical feedback obeys the same propagation restriction. The relaxed event bound is(1/2)c^max(0,N-floor((R+L)/2)). For0<c<1,recovery of an UNKNOWN relative phase with visibility>c therefore requires R+L>=2N. Necessary,not sufficient/optimal; no layer count is a calibrated time or speed. Further autonomous record return must be included in the circuit rather than silently excluded.

## Evidence,literature and unfinished scope

564 grouped named assertions/44 canonical core calls per execution. Prior558-check pilot is preserved but not independent evidence. Tests include actual gate compilation,local transport/reversal,full state versus valid pair quotient,rank-one norm certificates,all-outcome feedback,reference entanglement,C4 phases,fresh-versus-copied records,correlated-record counterexample,N12 boundary and saturating readout. General trace-norm/cone results have symbolic proofs,not finite-test extrapolations. Same author proof/code/replay; no independent review or Lean.

Primary public evidence read: Miatto etal.1502.07030v2 official metadata/abstract and parsed p.2 recovery equations (PDF screenshot failed; no figure digitization); Chen etal.1808.07388v2 official abstract/metadata of a six-photon redundant-record simulator. The latter is qualitative context,not raw-data fitting of this conveyor.2608.03944v1 abstract was encountered but its general advertised theorem claims were not checked or used. No exhaustive novelty claim.

Dedicated query first attemptIssue1900 was definitively rejected INVALID_TURN_ID,comment5807557660; no provider execution evidenced. Corrected UUID batch996b6230-2897-4cf8-bcd2-c18740005601,turna436bc0b-1f09-4f56-930f-32c7a28256ef,Issue1904/comment5807628134 matched requestSHAa24a3193d742a10b089b9718b02759bcccb63b6624bc7ef9c95c110df9a7a6d6. Batch and two childrenCOMPLETED,2provider calls,0bridge-model calls; each returned one actual metadata/abstract row,coverage incomplete/upstream total unknown. Selected actual metadata/status in QUERY_OUTCOME.json; full originals remain at the Issue. No paper full-text cache claim.

Next: calibrate physical local record generation,nonideal propagation and accessible feedback/preparation resources,then compare multitime data. The present result gives an observer/horizon/error boundary,not a physical trigger law,unique classical outcome,Born derivation,autonomous clock/reset budget,instant signal or empirical proof of irreversible heartbeat. Broader parent research remains unfinished.
