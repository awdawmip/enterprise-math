# EC48 — Exact finite rational face certificate for K-memory BRC observers

**Status:** author-side theorem and reproducible finite verification; native CLAIM/Guard/Driver/acceptance NOT obtained. **Scope:** strictly positive rational two-stage BRC source-count experiments, finite histories and future labels, binary terminal decision, stochastic PRIVATE encoder and decoder, two-error coordinates. Not a native X6 heartbeat evolution theorem.

## Provenance and locked assumptions
- Account GLOBAL_KNOWLEDGE_V1 canonical read: `awdawmip/chatgpt-global-knowledge@d1dd5aa7e590ab3dec37f1f4eb2851770df489c8`; `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, project router, P000 projection (matched original SHA-1 `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`), ACTIVE `我眼中的世界.md`, math/code and BRC policies.
- Enterprise Math source control pin: `awdawmip/enterprise-math@0929779757189d61ebfa1e815d8c5a31fd95f6df`; `docs/PORTABLE_RESEARCH_PROTOCOL.md`, `docs/CHATGPT_ORDINARY_CONTROL.zh-CN.md`.
- Inherited scientific input: EC47 immutable author-side manuscript `85a523ba6a887395c47d924fe037f772242f6a25:research_notes/r4_ec47_threshold_memory_20261026/EC47_THRESHOLD_MEMORY_ROC_REGION.md`; use its two-stage positive-source experiment, not a presumed accepted Foundation theorem.
- Native task/owner enumeration returned `CONTROL_QUOTA`, so present active owner, task availability, service session, exact native CLA​IM and independent review are unknown. This work is a separately named candidate, with no takeover.
- P000 remains `ACTIVE_LOCKED`: six native discrete spatial axes plus one independent time; no fixed heartbeat transition; three-coordinate slice/native bridges are unproved. BRC here retains positive integer provenance and future-label multiplicity; no signed cancellation, physical attribution or classical heartbeat dynamics.

## Model
Let nonempty finite history set H, future label set Y, integer K≥1 and strictly positive rational distributions p(h,y), q(h,y), each summing to 1. Equivalently, positive integer source counts P(h,y), Q(h,y) with the same total M; then p=P/M, q=Q/M. A K-memory observer uses a private stochastic history encoder π(m|h) (row-stochastic) and terminal decoder u(m,y)∈[0,1]. Its error/ROC pair (α,β) is

α=Σ_(h,y,m) p(h,y)π(m|h)u(m,y),  β=Σ_(h,y,m) q(h,y)π(m|h)u(m,y).

Write S_K for its attainable pairs. With full history, the zonotope is Z={(Σp w,Σq w): 0≤w(h,y)≤1}. Always S_K⊆Z. A fresh public random seed shared by encoder and decoder is **not** granted: it would trivially produce conv(S_K) and obscure the question.

For λ>0 put d_λ(h,y)=P(h,y)−λQ(h,y), and define the exposed maximal face F_λ={z∈Z: α−λβ=Σ_(d>0)d/M}. Set J_0={(h,y):d=0}, Q_0=Σ_(J_0)Q(h,y), Q_+=Σ_(d>0)Q(h,y).

## Theorem EC48.1 — exact union-of-intervals formula, all finite H,Y,K

Enumerate **labelled** deterministic K-colorings c:H→{1,…,K}. A coloring is admissible at λ if no memory m and future label y simultaneously receive a history with d_λ(h,y)>0 and a history with d_λ(k,y)<0. For each admissible c define:
- Pos_c(m,y): some h of color m has d(h,y)>0;
- Neg_c(m,y): some h of color m has d(h,y)<0;
- Z_c(m,y)=Σ_{h:c(h)=m,d(h,y)=0} Q(h,y);
- L_c=Σ_{m,y:Pos_c(m,y)} Z_c(m,y);
- U_c=Σ_{m,y:¬Neg_c(m,y)} Z_c(m,y).

Construct an undirected **compatibility graph** Γ_λ,K on admissible colorings: c—c′ precisely when, for every (m,y), the **union** of histories assigned color m by c or c′ contains no strictly positive AND strictly negative d_λ at that future label. Let C run over the graph's connected components, with L_C=min_{c∈C}L_c and U_C=max_{c∈C}U_c. Then the complete set of β-coordinates of S_K∩F_λ is EXACTLY

**B_K(λ) = (1/M) · [ Q_+ + ⋃_(components C) [L_C,U_C] ].**

An empty coloring set yields an empty face intersection. All endpoints are rational, and the formula includes **every real-valued privately stochastic encoder and decoder**, not merely deterministic quantizers.

**Proof.** Since each cell contributes d·(πu) and 0≤πu≤π, equality to the unrestricted support maximum forces u(m,y)=1 whenever π(m|h)>0 and d(h,y)>0; likewise u(m,y)=0 if d(h,y)<0. In particular, for a deterministic coloring c, the iff condition is admissibility, and all decoder variation left by neutral cells yields exactly β·M∈Q_++[L_c,U_c], a closed interval.

Two compatible colorings c,c′ have a common strict-sign-consistent decoder u*: choose 1 wherever the union forces positive, 0 wherever it forces negative, and any value elsewhere. For each history independently, π_t(m|h)=(1−t)1_{m=c(h)}+t1_{m=c′(h)}, 0≤t≤1. Every such policy remains on F_λ; its β is a continuous affine interpolation between one point of the c interval and one point of the c′ interval. Inside a single deterministic coloring, changing free u continuously covers its whole interval. Thus every graph edge connects two intervals through attainable face points. Concatenating paths shows that **each** connected component contributes the full interval from its minimum L to maximum U.

Conversely, let (π,u) attain F_λ and let E_h={m:π(m|h)>0}. Every deterministic selection c(h)∈E_h is admissible, and every two such selections are compatible, since the union is contained in the strict-sign-consistent support E. The product decomposition π(m|h)=Σ_c (∏_h π(c(h)|h))1_{m=c(h)} expresses β as a convex combination of β(c,u), each lying in [Q_++L_c,Q_++U_c] for colorings all contained in a **single** Γ component. Hence this β lies in that component interval. Both inclusions follow. □

## Theorem EC48.2 — finite necessary and sufficient FULL-region test

Let R={P(h,y)/Q(h,y):h∈H,y∈Y}, a finite set of positive rational ratios. Then

**S_K=Z  ⇔  for EVERY λ∈R, ⋃_C[L_C,U_C]=[0,Q_0].**

The union is the actual union, not its convex hull: merge overlapping intervals and detect uncovered open gaps. This is an integer/rational combinatorial certificate; it replaces the general real quantifier-elimination route mentioned in EC47 for this exact two-stage, two-output model.

**Proof.** Z is the Minkowski sum of positive vectors (p(h,y),q(h,y)) scaled by [0,1], hence a compact centrally symmetric zonotope. Every nontrivial edge has slope q/p and belongs either to some maximal α−λβ face λ=P/Q>0 or its central reflection. Both Z and S_K are centrally symmetric about (1/2,1/2): replace u by 1−u. Thus all boundary edges of Z are attained exactly iff the maximal faces F_λ (λ∈R) are attained exactly. Moreover S_K is star-shaped at (0,0): replace u by tu for 0≤t≤1. Every point z in Z is a scalar multiple of a boundary point of Z along the ray from the origin (with the origin trivial). Therefore containing every boundary point implies containing all of Z. Necessity is immediate; Theorem EC48.1 gives the finite edge certificates. If all ratios coincide, Z is a line segment and the same exposed-face test covers it. □

**Finite complexity:** enumerate at most K^{|H|} colorings per ratio, inspect |H||Y| strict signs, build at most O(K^{2|H|}) compatibility pairs and merge integer intervals. Exponential in histories (and K), but finite with no approximate optimization, nonlinear-real QE or assumption of cheap bit complexity.

## EC48.3 — randomized encoder is genuinely required to fill some exposed faces

Take H={A,B,C}, Y={x,y,z}, and raw positive source matrices

P_raw = [[4,2,2], [4,4,4], [4,1,1]],  Q_raw = [[1,1,1], [1,1,1], [1,1,1]].

Common-denominator integer counts are P=9·P_raw and Q=26·Q_raw, total M=234 under each hypothesis. At λ=9/13 the three x-cells and B's y,z-cells have d>0; C's y,z-cells have d<0; A's y,z-cells are neutral. The two memory states must separate B and C. A deterministic encoder can place A with B (neutral mass 52) or with C (neutral mass 0), and **there is no third deterministic face value** even with a randomized terminal decoder. But private randomized encoding of A with probability t to B's memory and 1−t to C's memory, with fixed forced decoders, produces

(α_t,β_t)=((180+36t)/234,(130+52t)/234), 0≤t≤1,

and all these pairs satisfy α_t−(9/13)β_t=5/13. Thus B_2(9/13) is the entire interval [130/234,182/234], rather than only its endpoints. This is NOT a counterexample to S_2=Z; it is a rigorous warning against testing only deterministic encoders on face interiors. It also verifies the compatibility-edge mechanism in EC48.1.

## Execution evidence and open frontier

Reproducible source: `EC48_verify.js`; deterministic exact report: `EC48_REPORT.json`. BigInt checks cover 768 positive-source instances / 4092 exposed ratios with 3035 nonempty-face interval verifications; K=|H| full-memory regressions (192), K=1 collinear-likelihood regression (288), plus the precise witness. These are finite consistency tests, not a proof of the universal theorem. No original X6 dynamics, numerical heartbeat experiment, full repo suite, native Guard or independent Driver run is asserted.

**What remains open:** Does equality conv(S_K)=Z force S_K=Z for every fixed K≥2? This note gives an executable necessary/sufficient finite test per instance but makes NO universal yes/no claim. Find a smallest positive-source witness with multiple disjoint uncovered compatibility-face intervals while both extreme face endpoints remain reachable, or prove the interval-gap obstruction impossible for every λ,K; then generalize to stop/continue dynamics and all four observers (e_P,e_Q,t_P,t_Q). Native transfer separately requires the actual update map, six-axis/slice embedding, third-coordinate semantics, and preserved source readout/operations.

**BRC interface use:** REUSE_APPLIED — EC47 positive integer history–future labelled source carrier and exact threshold sign graph, now extended by compatibility graph tracking privately randomized histories without dropping provenance.
