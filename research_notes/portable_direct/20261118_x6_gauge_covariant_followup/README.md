# X6 — three-source signed-gauge follow-up: four-state link residual and changing-twist calibration

Date: 2026-11-18. Research: independent portable author derivation for existing Task **RS-X6-TRIADIC-CLOSURE-DYNAMICS** (publication TP2-8B7E13C5904A2D6F1142). Prior result: [fixed spatial port theorem](../20261118_x6_triad_fixed_port_5a2fbf/README.md). **AUTHOR_PROVED / FINITE EXACT CHECK / NOT_INDEPENDENTLY_REVIEWED**. This note changes no Task CLAIM, result acceptance, P000 or actual event license. The Task has another live owner; this is a distinct unshared mathematical contribution.

## Model and native boundaries

Fix one Cell anchor within native signed X6, three *distinct* oriented native axes indexed 0,1,2 cyclically, and three named signed unit sources. This is a restricted embedded X6 observer, not an independent three-dimensional native world. Let initial source signs be s_i∈{±1}, generator edge signs a_i∈{±1}, with

    Q_a(e_i)=a_i e_(i+1),  a_0 a_1 a_2=-1.       (V5)

All indices are modulo 3. A signed-frame change ε∈{±1}³ acts as

    s'_i=ε_i s_i,   a'_i=ε_i ε_(i+1) a_i.

This is the actual V5 four-twist covariant completion. Branch identity, source names, ordered events and Cell incidence remain typed; no continuum π/trigonometric operation or numerical residual is introduced. V29 PASS/TRANSFER counters are nonnegative occurrence counts, *not* signed X6 edge-frame tags.

## Theorem 1: a complete four-state, reference-independent link residual

Set r_i=s_i a_i s_(i+1). Then each r_i is invariant under the full independent signed-frame action; r_0r_1r_2=-1. Conversely, **r completely separates the frame-change orbits of (s,a)**.

Proof: if (s,a) and (t,b) give equal r, take ε_i=t_i/s_i. Then b_i=r_i/(t_i t_(i+1))=ε_i ε_(i+1) a_i. The action is free on eight s-words, so 32 pairs (8 sign words times 4 twists) comprise exactly four orbits of eight. In the canonical twist (-,-,-), r_i=-s_i s_(i+1), precisely V1R's alpha_state sector.

The four relative-sign sectors are completely recoverable with **two independently measured invariant link bits** r_0,r_1, since r_2=-r_0r_1. No binary readout can distinguish all four states with fewer than two bits. Measuring such signed links remains an explicit *observer capability*, not an automatically licensed original event.

## Theorem 2: gauge-covariant closure and Port-gate classification

Let Boolean C(s,a) and g(s,a,p), p=0,1,2, be invariant under full signed-frame change and covariant under cyclic simultaneous relabeling of the three named Port positions. Require g=1 only when C=1. By Theorem 1 these functions factor through (r) and (r,p). Under cyclic C3, four r-words split into two orbits: the singleton (-,-,-) and three words with exactly one negative sign. Thus there are exactly **4 closure predicates**. The 12 rooted pairs (r,p) split into four free C3 orbits, giving **16 rooted gates**.

For the singleton closure orbit there is one associated rooted gate orbit; for the other closure orbit there are three. Excluding a closure orbit forces its gates off; including it allows every gate selection, hence the number of coherent (C,g) pairs is

    (1+2^1)(1+2^3)=27.

This is a new **sign-and-generator-relational** candidate language. R762CA's earlier 729 coherent pairs used C3 symmetry on *sign-only* rules, without the additional full independent signed gauge. If its sign-only functions are additionally required to be invariant under that full gauge, C and g are both constant and exactly **3** coherent pairs remain. The 27 candidates are not a physical TRIADIC_CLOSURE_E permission claim.

## Theorem 3: exact four-state dynamics with a changing generator

For a first generator a, the next source signs obey s'_(i)=a_(i-1)s_(i-1). If the following generator is b (independently chosen among the four twists), define Δ_i=a_i b_i. Then

    r'_i=Δ_i r_(i-1),   Δ_0Δ_1Δ_2=+1.         (3.1)

Proof: substitute s'_i into r'_i=s'_i b_i s'_(i+1). Both a,b undergo the same gauge change, so Δ_i is gauge invariant. If b=a, Δ_i=+1 and the relative-sign state rotates: (-,-,-) stays fixed, while the other three r-states form a three-cycle. If **all four next twists** b are independently admissible, every r reaches *every* target r' in one step: choose Δ_i=r'_i r_(i-1), whose product is +1, then b_i=Δ_i a_i.

**Conditional closure consequence.** Requiring every enabled event to preserve the closure C when the following twist can be any of the four forces every *proper* nonempty C to have its gate identically zero. Among the 27 coherent pairs, exactly **19** remain: 16 gates with the everywhere-true C, plus one gate-zero choice for each of the other three C choices. This does not assume native event licensing: the real event may restrict twist changes. It pinpoints what that missing native rule must decide.

## Theorem 4: the exact price of variable-twist parity calibration

Let two consecutive scatterings independently use a^(0),a^(1), each with product -1. On one *fixed spatial axis j*, read shell signs at times 0,1,2:

    y0=s_j,
    y1=a^(0)_(j-1) s_(j-1),
    y2=a^(1)_(j-1) a^(0)_(j-2) s_(j-2).

Then the original raw reference-frame sign parity P=s_0s_1s_2 satisfies

    P=-a^(0)_j a^(1)_(j-1) y0y1y2.           (4.1)

Proof: multiply the y's and use a^(0)_0a^(0)_1a^(0)_2=-1. For *every* fixed y triple, all 4×4=16 twist pairs remain possible and determine unique s. Eight imply P=+1 and eight imply P=-1. Thus a composite calibration character K=-a^(0)_j a^(1)_(j-1) is **necessary and sufficient** beyond the three y readings. If a query reveals just one primitive signed edge from one specified event, the minimum is exactly **two queries**, and the only sufficient two-query subset among the six time-labelled edge signs is {(0,j),(1,j-1)}. The two required characters depend independently on two four-element twist sets, and knowing one edge in one set never determines another edge there.

When a^(1)=a^(0)=a, formula (4.1) becomes P=a_(j+1)y0y1y2, recovering the earlier one-bit fixed-generator result. Concrete failure of blindly using that old formula with changing twist: j=0, s=(+,+,+), a^(0)=(-,-,-), a^(1)=(+,-,+), y=(+,-,-), true P=+, whereas the old a^(0)_1 y0y1y2 gives -.

**Interpretation:** Raw P changes under a single-axis sign-reference flip. Therefore it cannot be recovered from *gauge-invariant data alone* in the absence of an external reference or an explicitly relative calibration. The observable r, in contrast, is a genuine four-valued gauge-invariant relation. This refines the experimental question: does the native event produce a calibrated signed tag K, or should the instrument instead detect the relational r?

## Precise V29/observer boundary

V29 stores (named, ordered) PASS/TRANSFER occurrence history and nonnegative M,Rin,Rout; its derived contrasts (u,Ω) are **signed count differences** and do not automatically encode physical radial sign or V5 generator sign. Under a sign-blind native scheduler, flip one unobserved axis with ε_j=+1 while transporting all generator twists by V5 covariance. The fixed-j sign stream and full named unsigned V29 history are unchanged at every time, while initial raw P reverses. This gives an all-horizon obstruction by induction, not just a finite negative search. A sign-sensitive *licensed* scheduler might expose an extra bit through the occurrence pattern; the no-go does not cover such a declared extension.

**Next exact scientific bridge:** identify a source- and reference-preserving native Cell/Link/Port ingress/egress readout that yields K or two r bits, and check actual atomicity, permission predicates, reference-frame consistency, future BRC operations and V39 loop behavior. Do not identify the independent port-read controller with a physically self-triggering primitive until such a bridge is proved.

## Reproducibility and exact sources

The accompanying \`verify_x6_gauge.py\` uses finite exact signs, named transitions and explicit V5 branch/source operations. The full local author check enumerated: 32 states, eight gauges, 4 orbit fibers of size eight, all C3 closure/gate orbit possibilities, 729/3/27/19 classifications, all r transitions, 384 variable-twist inputs (3 axes × 8 source signs × 4 × 4 twists), all 63 subsets of six primitive sign queries for each axis, 96 fixed-twist cases, and a 12-step gauge witness. All finite checks passed; the all-time no-go is the mathematical gauge proof. No native physics calibration, result admission or independent review is inferred.

Pinned project inputs:
- Prior fixed-port note Git blob \`6eddfd30d47b88e3496eeed46291cabe4885dd6a\`.
- V1R \`research_notes/X6_CELL_TRIADIC_PORT_FRAME_INTERNAL_STATE_V1_20260906.md\`, blob \`8eada27c26ba6683e771fe00c89ab67abf6b0032\`.
- V5 \`research_notes/X6_SIGNED_INTERNAL_Q_GAUGE_CORRECTION_V5_20260906.md\`, blob \`b794e6b4a037826feaf15f50eb8ba35b126ec78a\`.
- Equal-unit triadic scatter \`research_notes/X6_TRIADIC_ATOMIC_SCATTER_AND_BRC_CORRELATION_V1_20260906.md\`, blob \`51175f8eb0369aa711b7b1c847f4cd65e4b19d4e\`.
- V29 ledger \`research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md\`, blob \`6849ebd3fc776fb7da3b46627376490aba3dad99\`.
- R762CA sign-only candidates \`research_artifacts/mcp/RS-X6-TRIADIC-CLOSURE-DYNAMICS/MCP-4b2d70a97f594366a7c94a0f8b45df38/1728fedbae5e7405844b/R762CA_COVARIANT_SIGN_GATE_CLASSIFICATION.md\`, blob \`c5c7e305a5c2a30b4e99754a7f1044154a7ccc9f\`.
- Task frozen science \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\` (its P000 ontology remains unchanged).
