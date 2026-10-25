# R4-EC33: refined source-label finite BRC certificate and maximal hidden label defect

**Author-side theorem and exact integer evidence; not independently Driver-reviewed or mathematically admitted.** Date 2026-10-26. This note contains complete mathematical arguments and exact verification scope. No P000 native-heartbeat test was performed.

## Frozen source and scope

- GLOBAL_KNOWLEDGE_V1 canonical main read snapshot: a197792a7db5d01e0f517fde56d717be4bfb56c5; P000 canonical Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE_LOCKED, original blob metadata verified.
- Enterprise Math Source control snapshot at selection: main@647360751350296b14f3bb26b984d8e75a271b03. Current portable protocol: docs/PORTABLE_RESEARCH_PROTOCOL.md. Predecessor EC32 exact finite scalar word certificate: fa0cc318e99c1201b1e31299a8cc38daa2ff62ed, research_notes/r4_ec32_finite_source_bridge_20261026/EC32_FINITE_SOURCE_BRIDGE_CERTIFICATE.md.
- Native dispatch attempt returned CONTROL_QUOTA. Current native task owner/CLAIM is unknown; this is independent direct author research, not claimed task takeover. GitHub login awdawmip; locally assigned Researcher-ID EM-DIRECT-6C33R4. Research-Activity-ID RA-EMR4-20261026-0636-EC33LABEL was created and read back on main at 5bceebd41d6da23160199fec768493923a25ba51; it grants no TASK/CLAIM/Driver authority.
- BRC type: nonnegative rational/integer **source-labelled alternative edges**, ordered path composition, exact positive multiplicity, and selectable observed source labels/terminal ports. Formal differences of two observer values do not create signed source branches. The counterexample is an abstract one-operation BRC source system; no fixed native X6 heartbeat transition, physical phase, native residual or time step is claimed.

## Theorem A: finite joint source-label/terminal-port equivalence certificate

Let Σ be a finite shared operation alphabet, Λ a finite shared *observable source-label* alphabet and T a finite shared terminal-port set. System i=1,2 has d_i finite residual states, initial row α_i over Q≥0, transition matrices M_i,(a,ℓ) over Q≥0 of size d_i, and terminal columns β_i,p over Q≥0. Each matrix entry sums the positive multiplicities of **distinct microscopic source alternatives** bearing the declared operation a and observable label ℓ; different microscopic sources may intentionally share an observed label.

For v=((a₁,ℓ₁),…,(aₖ,ℓₖ)) define F_i(v,p)=α_i M_i,(a₁,ℓ₁)…M_i,(aₖ,ℓₖ) β_i,p. Empty v is allowed. If F_1(v,p)=F_2(v,p) for every p∈T and every refined word |v|≤d_1+d_2−1, equality holds for **all** finite refined words, at every port.

**Proof.** In Q^d with d=d_1+d_2 form α*=(α_1,−α_2), M*_(a,ℓ)=diag(M_1,(a,ℓ),M_2,(a,ℓ)), and β*_p=(β_1,p,β_2,p)ᵀ. Then α*M*_v β*_p=F_1(v,p)−F_2(v,p). Define V_k=span_Q{α*M*_v: |v|≤k}. The spaces are nested and dim≤d. If V_(k+1)=V_k, every transition sends V_k into itself, hence V_k contains **all** later reachable rows. Unless the initial row vanishes, at most d−1 strict dimension increases are possible, so V_(d−1) is already the total reachable span. The hypotheses make each generating row orthogonal to all β*_p; linearity gives the same for every reachable row and every port. For zero initial row the conclusion is immediate. QED.

Every observer that is a common weighted linear sum of fixed-length joint *operation/source-label trace/port* source counts is therefore preserved, including label histograms and any corresponding normalized distribution with positive denominator. This does **not** establish microscopic label identity, internal state isomorphism, phase fidelity, or native-X6 correspondence absent a declared compatible alphabet, labelled transitions, full residual closure, slice and port map.

The EC32 exact rational reachable-row basis method is reused verbatim on refined alphabet Σ×Λ; testing its basis against each β*_p gives an exact compact all-depth certificate. The dimension cutoff remains d_1+d_2−1 despite the larger number of refined letters.

## Theorem B: scalar counts can agree at every horizon while labelled distributions separate maximally

Fix any integer H≥1. Use one operation A and observed source labels R,B; there is one terminal port and each terminal residual state contributes weight 1.

U has one state, with one R-labelled source choice and one B-labelled source choice looping back.

V_H has H+1 states 0,…,H, starting at 0. At state r<H, there is one R edge and one B edge, each going to r+1. At state H there are two **distinct microscopic R source choices** returning to H and no B edge. This is a positive integer BRC carrier; the two microscopic red choices have the same *observed* class R, not the same underlying identity.

**Unlabelled equality.** In each system the aggregated A transition M_A=M_R+M_B has every row sum exactly 2. Thus for every n≥0 the total positive-source count for operation word A^n is exactly 2^n in **both** systems. Hence even an all-word scalar EC32 equivalence certificate would pass for this observer.

**Exact labelled counts.** For a length-n observed label word ℓ∈{R,B}^n, U has f_U(ℓ)=1. In V_H all labels in the first min(n,H) steps have one available microscopic choice per label, and the counter reaches H after H steps. Therefore

- if n≤H then f_V(ℓ)=1;
- if n>H and ℓ_(H+1)=⋯=ℓ_n=R, then f_V(ℓ)=2^(n−H);
- otherwise f_V(ℓ)=0.

This follows by direct multiplication of the positive path-edge multiplicities, with no cancellation or asymptotic approximation. In particular all refined source-label histograms match through horizon H. They first differ at length H+1: word R^H B has U/V counts (1,0) and word R^(H+1) has (1,2). Since the state dimensions are 1 and H+1, Theorem A's generic cutoff is H+1, precisely the first disagreement. Thus the cutoff is **sharp even among pairs with identical unlabelled word counts at every horizon**.

**Exact total-variation defect.** Normalize by the 2^n positive microscopic branches, not by the number of distinct label strings. U has uniform distribution over all 2^n labels. For n>H, V_H is uniform on the 2^H words whose last n−H labels are all R (each such word has 2^(n−H) microscopic source branches). Hence

TV_n = (1/2) Σ_ℓ |Pr_U(ℓ)−Pr_V(ℓ)| =
  0 for n≤H, and 1−2^(H−n) for n>H.

The event “the last n−H labels are all R” attains that distance: its U probability is 2^(H−n), V probability is 1. In particular lim_(n→∞) TV_n=1, despite *exact equality of all scalar positive-source counts*. This is observer-induced information loss, not roundoff, not negative BRC mass and not demonstrated native physics.

## Verification and exact reused code

The independent exact Python positive-branch verifier enumerated H=1,…,8, 16,312 refined label words, 152 independently aggregated-state DP checks, 76 totals and 32 nonzero exact rational TV checks: **PASS**. Evidence in EC33_REPORT.json; source in EC33_verify.py.

The unmodified EC32 rational-basis implementation at Git commit fa0cc318e99c1201b1e31299a8cc38daa2ff62ed (Git blob 5eb598b8f6fdcb9fd26da148090ead079d94cd3e; SHA256 604233139ed6fd2e2db491de3f661b37ae0af98d0e1fecf38c180e561d3f983d) was executed directly after setting its accepted alphabet to (R,B). Each H=1,…,8 produced reachable rank H+2 and first nonzero witness at H+1: **PASS**. Reproduction driver in EC33_span_reuse.py and structured evidence in EC33_EC32_SPAN_REPORT.json. The unchanged EC32 original source is referenced, not duplicated as a new project source; the downloadable offline zip includes it for cold-start replay.

BRC tool resolution: **REUSE_APPLIED + REUSE_EXECUTED + EXTEND_EXISTING_TOOL** (EC32 rational-span method with source-label/port-refined observer), not a new general-purpose tool family. Exact universal claims are proved algebraically above; finite computational checks only validate declared instances.

## Boundary and next mathematical question

P000 remains ACTIVE_LOCKED, with six native spatial axes, a genuine 3D research slice, a third component that cannot be silently dropped, independent time, and fixed_heartbeat_program=null. No native source-labelled heartbeat update, source-fibre correspondence, allowed future word/port schema or finite residual state bound was established. Therefore the status is AUTHOR-SIDE AUXILIARY MATHEMATICS; NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION; independent Driver review and formal Source Result still pending.

**Next test:** obtain exact authorized native X6 source-labelled transition operations and finite observed label/port typing; prove transition closure and dimension bound (or a compositional label-respecting bisimulation), then apply Theorem A to the native matrices *by label* and test full joint observer rather than summed scalar counts. Carry unobserved microscopic provenance as residual when the supplied labels collapse distinct source branches.
