# Stage442-B — Exact implicit support counting for two native-X6 defect histories

Date: 2026-11-05. Status: AUTHOR_SIDE_PROOF / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED. Parent: Stage441-B, Git commit 8f360d4cd7fcbb0b6842ec1718451d4c9ebbd746. Frozen science: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative rules are read independently of these frozen scientific pins. Researcher EM-DIRECT-DDEF12, activity RA-2C870CC708F509E5B5D108CE. No formal CLAIM, Driver review, physical heartbeat transfer, or native Result claimed.

## Exact observer and full present fiber

Let D={±E1,...,±E6} be the 12 original signed spatial directions in X6. Let A=+E1 and B=-E1. Consider arbitrary (possibly unequal) integers m,n≥3, numbers kP,kQ of nonadjacent B defects strictly inside words P∈{A,B}^m and Q∈{A,B}^n, and A endpoints. All other positions are A. Future APPEND may use **every** d∈D, not just A/B. Let the observation O=(m,n,V_P,V_Q,J_P,J_Q,K) consist of source lengths, two native six-vector endpoints, all directed adjacent direction counts J, and aligned absolute matching count K. Permit P/Q respectively pP,pQ POPs (0≤pP<m, 0≤pQ<n) and rP,rQ arbitrary labelled APPENDs; all legal interleavings and each prefix are observable. No nonempty source may become empty.

In this defect family, fixed lengths and counts kP,kQ fix both endpoint vectors and both J tables: J(A,B)=J(B,A)=k, J(B,B)=0, J(A,A)=length-1-2k. Consequently the **complete O fiber within this explicitly restricted family** is precisely the set of all such P,Q having the specified K. Write t=min(m,n), d=t-K (number of disagreements in the original overlap), N=max(m,n).

## Theorem 442.1 — Exact finite-state original-history transfer

Encode defect bits at original index i by (x_i,y_i)∈{0,1}² with B=1, A=0; absent positions contribute no bit. Endpoints are forced zero. Define the original-history transfer state (i,a,b,d',u,v), where a,b count used P/Q defects, d' counts overlap mismatches, and u,v are previous defect bits. From position i choose (x,y) subject to endpoint and nonadjacency constraints ux=vy=0, a+x≤kP, b+y≤kQ and d'+[i≤t][x≠y]≤d. Move to (i+1,a+x,b+y,d'+[i≤t][x≠y],x,y). Start from (1,0,0,0,0,0) and accept at i=N+1 with (a,b,d')=(kP,kQ,d).

Each accepted path is in bijection with one raw pair in the fixed complete O fiber. Thus the transfer's exact integer sum counts **all raw ordered pairs** without enumerating them. The number of non-position states is at most H=4(kP+1)(kQ+1)(d+1); every state has at most four outgoing transitions. In this defect family d≤kP+kQ, so H is a function of the total defect parameter alone.

## Theorem 442.2 — Output-subset determinization exactly counts the distinct future classes

Let R be the Stage439-B two-sided repair key (own removable suffixes S_P,S_Q; the original-direction cross-source APPEND exposure lists A_P,A_Q; and mutable-overlap equality bits B), with original index labels fixed by m,n,pP,pQ,rP,rQ. At index i, output λ_i(x_i,y_i) consisting of exactly the R coordinates exposed at that index, in the fixed order S_P-bit, S_Q-bit, A_P-bit, A_Q-bit, equality bit. An empty coordinate group outputs one fixed blank symbol (one symbol is emitted per index, so no epsilon ambiguity). Repeated exposures of the same letter are retained syntactically but are harmless.

Replace integer counts by a **set** of reachable transfer states for each output prefix. For an output symbol σ, take the union of all successor states reached through transfers with label σ. Denote this deterministic subset transition by Δ_i(S,σ). Let F_i(S) count distinct accepted output suffix strings. Then
F_{N+1}(S)=1 if S contains any accepting state and 0 otherwise;
F_i(S)=Σ_{σ:Δ_i(S,σ)≠∅} F_{i+1}(Δ_i(S,σ)).
The sum is over **distinct σ**, not over raw transfers, thus does not overcount different hidden raw histories sharing the same repair key. The desired exact support and sharp class-code size are
q_F=F_1({(0,0,0,0,0)}), bits=ceil(log2(q_F)).
Following lexicographically ordered nonempty transitions, cumulative F values yield exact class rank and unrank without materializing the q_F-item codebook.

Proof: Induct on the number of remaining indices. The reachable subset is exactly the set of transfer states admitting the emitted output prefix, by definition of Δ. Each accepted output string has a unique first symbol and belongs to exactly one successor prefix language. The recurrence counts its language once. Stage439-B Theorem439.1 proves, for this declared future observer and operation budgets, **equality of complete current-O history futures iff equality of R**. Therefore the language of λ output words is exactly the future-equivalence support. The categorical identification depends on that earlier author-side theorem; the automaton-language statements are independently proved here.

## Theorem 442.3 — Exact class masses and lossless raw-history recovery

Fix any accepted λ word representing a class C. Restrict the original transfer at every position i to output λ_i and replace Boolean state sets by nonnegative integer weights. Its terminal sum is M(C), the exact number of raw ordered pairs in C. Alternatively define H_i(s) as the number of accepted completions from transfer state s with this fixed remaining output word. Then H_i(s)=Σ_{transitions with λ_i} H_{i+1}(s'), with 0/1 terminal condition. Ordered (x_i,y_i) transitions and these exact suffix counts provide a bijective within-class rank/unrank for indices 0≤z<M(C). Given class rank and z the complete original P,Q are reconstructed, with Θ(m+n) output operations. A class label alone preserves only the specified future observer, not a chosen original history.

## Complexity and typed BRC interpretation

The underlying transfer has O(NH) state positions and O(NH) transitions, with integer counts bounded by 2^(m+n), hence O(m+n)-bit counts. Determinization has at most T=(N+1)2^H reachable (i,subset) nodes and at most four H examined raw transfers per node; hence O(N·2^H·H) integer/count and subset-update operations and O(N·2^H·H) subset-bit storage, before the per-integer bit cost. Counting a particular class population or within-class ranking uses O(NH) integer operations / O(NH) stored suffix entries; each integer is at most m+n+1 bits. Computing O and R from an explicit input word costs O(m+n); reconstructing a complete raw history costs Θ(m+n). As a parameterized guarantee for bounded defect counts this is fixed-parameter tractable in kP+kQ (with a potentially large double-exponential dependence on the parameter); it is **not a polynomial-time bound in unrestricted k**. No unproved universal concise closed form for q_F is asserted.

The BRC population carrier here has three different layers: Boolean reachable support (determinization), exact positive integer class mass M(C) (weighted transfer), and original path provenance (within-class index). Their distinction is necessary: summing raw transfer paths in place of distinct outputs would overcount the class support.

## Actually executed finite verifier and evidence

Run with Node.js (no third-party modules): `node REPRO_STAGE442B.js`. The script uses exact BigInt counts. Six parameter fibers were exhaustively checked against direct generation of all nonadjacent defect pairs, including arbitrary unequal lengths and reversed source roles; each raw pair is reconstructed by exact within-class rank/unrank, and each observed repair class has its exact integer mass and class rank/unrank. Results:
- (m,n,kP,kQ,K,pP,pQ,rP,rQ)=(8,8,2,1,5,2,1,1,1): 40 raw pairs, q=5, masses (16,9,9,3,3).
- (8,8,2,1,7,2,1,1,1): 20 raw pairs, q=4, masses (6,6,4,4).
- (9,7,2,1,4,2,1,2,1): 34 raw pairs, q=4, masses (15,12,4,3).
- (9,7,2,1,6,2,1,2,1): 16 raw pairs, q=3, masses (9,4,3).
- (7,8,1,2,4,1,2,1,2): 34 raw pairs, q=5, masses (12,9,6,4,3).
- (7,8,1,2,6,1,2,1,2): 16 raw pairs, q=4, masses (6,4,3,3).

An **independent full future trace tree** over the entire first L=8 K=5 fiber (40 histories) recursively includes all legal POP/APPEND interleavings and **all twelve** native APPEND letters, comparing each prefix's actual six-vectors, directed J and K. Exact subtree interning (not a collision-prone hash) traversed 40,560 distinct reachable labelled future states and 3,445 distinct subtree observation signatures; its future partition matched exactly the five automaton repair classes. This is a finite test, not a substitute for the Stage439-B general proof.

Script source: REPRO_STAGE442B.js. Actual executed canonical JSON: REPRO_STAGE442B_EXECUTED.json. No signed/complex amplitude cancellation, physical dynamics, formal checker or independent Driver acceptance is claimed.

## Next unresolved unit — Stage443-B

Try a sharper support-count bound or polynomial algorithm for kP+kQ growing with word length, using the fact that all R output symbols occupy only a bounded trailing corridor. Test whether the subset family admits an interval, convexity or smaller canonical representation; search first for a concrete pair of subsets whose merger makes different accepted languages before promoting any simplification. Also extend independent full-future trace checks to unequal-length fibers with all 12 APPEND directions and larger budgets. P000/ACTIVE worldview and frozen science remain unchanged.
