# X6 observer VI — sharp finite-horizon Port-language stabilization and delayed source residual

Date: 2026-11-19 (Asia/Shanghai). Result class: author-side exact theorem, with separately checked finite conditional models; independent mathematical review pending. Research line RS-X6-NATIVE-TIME-DYNAMICS; immutable publication TP2-91D4A7C2F63805BE21A3. Scientific foundation: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 verified at this pin). Current behavioral requirements were read independently from current main.

This paper continues the exact full-completion source-language result in research_notes/portable_direct/2026-11-19_x6_resource_language_residual_exact_r4.md, proof at commit a7cfb8e629921331f3f465005f8195f361918bf1, with independent prior Activity evidence RA-545183ADD4EF71C3E4698AEE. Historical role EM-X6-214D9C and SID MCP-d467c19ce42d4d7fa65a3901db1cf6b2 are predecessor provenance, not a claim that this run has inherited a private capability or a live formal Task CLAIM.

## Exact conditional source-labelled Boolean BRC model

Let a,b>=1 be terminal A/B event counts and p_A,p_B>=1 their exact decorated local periods. Let Q be a finite Port-controller state set, q0 its initial state, and delta a deterministic partial map Q x {A,B} -> Q. A state is s=(i,j,q), with 0<=i<=a, 0<=j<=b and event rank k=i+j. Source-labelled append changes its count and q, subject to the capacity and optional count-dependent guards; no silent steps. Every terminal (a,b,q) is accepted. The statements also hold for an explicitly chosen subset of accepted terminal controller states.

A typed Boolean BRC branch is the pair (ordered source word, controller state). Its Boolean reachability support projects to (count_A, count_B,q). Guarded append of either named source commutes with this support projection because source enablement and successors are determined by the projected state. This correspondence is for source-labelled Boolean future reachability, not branch multiplicities or signed/amplitude physics. It uses integer exact event order; event rank is not physical duration.

Let R_k^+ be the reached states with at least one accepted full completion to the terminal capacities. Define C(s) as the nonempty set of complete remaining source words, all of length H=a+b-k. For a horizon h>=0, define the productive future prefix language

 L_h(s) = {u : |u|<=h and there exists v with uv in C(s)}.

Dead-end attempts are excluded by the declared productive observer. Let O(s)=(k, i mod p_A, j mod p_B). This deliberately hides the current controller state and exact counts.

## Theorem A. Optimal extra information at any finite horizon

At a fixed rank k and observed value o, let D_h(o) be the set of DISTINCT languages L_h(s) over s in R_k^+ with O(s)=o. Then

 M_h(k)=max_o |D_h(o)|,
 b_h(k)=ceil(log_2 M_h(k)), taking b_h(k)=0 if M_h(k)=1.

The quantities M_h(k),b_h(k) are nondecreasing in h and constant for h>=H. At full horizon, with P=lcm(p_A,p_B), and N(i,j) the number of distinct complete languages C(i,j,q) over productive controller states with count pair (i,j),

 M_H(k)=max_{0<=r<P} sum_{0<=i<=a, 0<=k-i<=b, i congruent r (mod P)} N(i,k-i).

Proof: An h-future-lossless selector must separate every pair of distinct productive prefix languages inside the same known observer fiber, requiring at least |D_h(o)| codes; indexing these language classes attains that bound. Since truncating L_{h+1} to lengths <=h yields L_h, successive partitions only refine; this proves monotonicity. Each accepted full continuation has length exactly H, and its entire productive prefix set is equivalent to the full completion language C(s); thus stabilization occurs at H. For two different exact count pairs with the same k, any full completion from (i,j) contains precisely a-i A symbols; hence their nonempty complete languages are distinct. At fixed k the phases agree precisely if i-i' is a multiple of P. Summing per-count complete-language classes over each phase residue proves the last formula. QED.

The count-wise SUM in that final formula is only justified for the full future. Short horizons can merge different exact count vectors. Exact example: no Port guard, a=b=3, p_A=p_B=2, rank k=2. Both (0,2) and (2,0) observe (2,0,0). Both have L_1={epsilon,A,B}; L_2 differ because BB is unavailable from (0,2), whereas AA is unavailable from (2,0). Consequently the mixed-count observed fiber needs 0 extra bits at horizon one and 1 extra bit at horizon two. Treating the full-future count-sum as a one-step bound would overstate the residual.

## Theorem B. A sharp one-step-early full-future certificate

Let H=a+b-k>=1. If P=lcm(p_A,p_B)>=2, then for ANY two productive states s,t with the same O, equality L_{H-1}(s)=L_{H-1}(t) is equivalent to C(s)=C(t). Therefore

 M_{H-1}(k)=M_H(k), and b_{H-1}(k)=b_H(k).

If the exact counts (i,j) are themselves part of the observer, the H-1 result holds for all P. For P=1, the general bound H is necessary in some models.

Proof: Equality of complete languages plainly implies equality of their productive prefix languages. Conversely assume the (H-1)-prefix languages are equal and nonempty. Choose a common word u of length H-1; one exists because both states have productive full completions. From either state, u can reach completion by one last A or B. Thus a-i-count_A(u) and a-i'-count_A(u) are EACH in {0,1}; hence |i-i'|<=1. Since the same local phase observation makes P divide i-i', P>=2 implies i=i', whence j=j'. For every productive word u of length H-1 from the now-identical exact count vector, its final required source label is UNIQUELY fixed by the remaining A/B quota. Equality of productive (H-1)-prefix sets therefore forces identical full continuation sets. When exact counts are observed, the same uniqueness argument begins directly at i=i'. For H=0 all productive full languages are {epsilon}. QED.

Sharpness for every m>=2: choose a=b=m and p_A=p_B=m+1. Two legal first-two-event prefixes AB and BA have identical exact counts (1,1) and phases. A finite deterministic controller stores which source occurred first (mode A for AB, mode B for BA). Both modes now permit EXACTLY the common word w=(AB)^(m-2) of length H-2=2m-4. At this point both have remaining quotas (1,1). Mode A permits A and mode B permits B as their next event; each then must take the other source to reach (m,m). Their complete futures are respectively wAB and wBA. Hence their productive prefix languages agree through H-2 and first differ at H-1. At rank k=2 the only two productive observer states are the two modes, giving

 M_{H-2}(2)=1, M_{H-1}(2)=2; b_{H-2}(2)=0, b_{H-1}(2)=1, H=2m-2.

Thus no model-size-independent bounded lookahead can certify permanent erasure of Port source history, and the H-1 universal guarantee is sharp even when the two histories share the exact source counts.

Necessary P=1 boundary: set a=b=1, p_A=p_B=1 and allow both source orders. At rank k=1, states (1,0) and (0,1) have the same observation, L_0={epsilon} in both, but L_1={epsilon,B} versus {epsilon,A}. Here H=1 and horizon H-1 cannot distinguish the two full futures.

## Exact algorithm and execution evidence

Define a canonical productive prefix-language signature recursively. An unproductive state receives null. A productive state at h=0 receives the canonical epsilon-only signature. At h>0, its signature is the ordered tuple of pairs (source x, signature of the productive successor under x). Include the empty word at every productive node. Since the append is deterministic for each named label, induction on h proves signatures equal iff their L_h languages are equal. Hash-consing canonical signature IDs yields the exact M_h from the reached typed BRC state support in O(H*|S|*|alphabet|) constructed nodes, aside from hash-map overhead, where |S|<=(a+1)(b+1)|Q|. Expanding complete suffix strings is reserved for bounded independent checking.

Source code: x6_resource_horizon_brc_verify.py (Python 3 standard library; typed source-labelled branches, Boolean support, signature DAG, exact exhaustive comparisons). Full output: x6_resource_horizon_brc_results.json. Command was executed locally: python3 x6_resource_horizon_brc_verify.py > x6_resource_horizon_brc_results.json; assertions PASS.

Exact finite domain: ALL 81 partial deterministic controllers on two Port states (each of four state/source edges is absent, to state 0 or to state 1), all 9 capacity pairs a,b in {1,2,3}; 729 models, of which 351 have a full completion. At every rank, every possible horizon and both local period pairs (2,2),(2,3), the explicit provenance-word branch carrier projects to the derived state support, hash-consed signatures agree with independently enumerated exact completed-word productive prefixes for every reachable productive state pair, and both calculations give identical M_h. Monotonicity, the full r4 count-sum and the universal M_{H-1}=M_H were checked. There are 216 rank/phase profiles (counted with the two periods separately) in which full-future distinctions exceed those at h=0.

Additional exact certificates: unbounded-delay controller d=0..10; near-terminal sharpness m=2..9 (first difference exactly H-1); one-event P=1 boundary; mixed-count one-versus-two-step alias. These are bounded checks of explicitly proved arbitrary-parameter statements, not extrapolation.

Executed local source SHA256: f29942e7bd9ef4955363f635cb02fe46f68aa461e3bd91941605ca137f1c41cf. Executed local full JSON SHA256: b3b5dd9cac05bb339e0531742a6e51862995f5c30310e6f7a735ff164bb0d23a.

## Native X6 meaning and next scientific task

Frozen P000 assumes six signed native Cell displacement axes and a separate ordered time coordinate, with primitive nonzero stable balance satisfying TRIADIC_CLOSURE_E. The two A/B symbols represent two HYPOTHETICAL already-admitted typed triadic event families. The theorem is conditional event/Port observer mathematics; the needed bridge to an actually admissible native Port update has not yet been established. The exact next discriminating test is to recover a frozen task-approved real Cell/Link/Port guard and named occupancy/release transition, identify two candidate histories at equal six-coordinate, phase and exact source-count observation, then calculate the FIRST horizon at which their allowed productive source future languages split. If no split occurs, provide a scoped factorization certificate for this exact native event family. Signed interactions require typed signed BRC evidence; positive Boolean support alone is intentionally scoped to reachability.

## Source/authority

Native continuation read research2-20261119-0308-x6-continue-read-v1 was reconciled as FAILED/SOURCE_TREE_BLOB_SIZE_INVALID; the read failed during Source materialization, with no formal new Task, CLAIM or run. A historical successful own-line registration is research2-20261119-0113-native-self-register-v1 (EM-X6-214D9C / RA-545183ADD4EF71C3E4698AEE). A fresh Site recovery lookup for historical SID MCP-d467c19ce42d4d7fa65a3901db1cf6b2 returned BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false; current active owner and run-local authenticated execution capability therefore remain unconfirmed. This preservation is independent portable scientific work, not a new CLAIM, native PROGRESS, Activity checkpoint, mathematical Result or independent Review. Reconcile the actual original execution/owner before any protected source attribution.
