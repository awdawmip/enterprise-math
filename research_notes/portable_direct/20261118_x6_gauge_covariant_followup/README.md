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


## Appendix A — sharp invariant-link readout without an external sign reference

The previous theorem reconstructs the **raw parity** P, which changes under a reference-frame sign flip. The genuine four-valued signed-Link sector r can be read more directly. For the same observations y0,y1,y2 and two consecutive generators a=a^(0), b=a^(1), put the *relative edge-change bit*

    delta=a_(j-1) b_(j-1).

Because the same signed-frame transformation multiplies a_(j-1) and b_(j-1) by the same endpoint signs, delta is **gauge invariant**.

**Theorem A1 (sharp three-read relational recovery).**

    r_(j-1)= y0 y1;
    r_(j-2)= delta y1 y2;
    r_j    =-delta y0 y2.                        (A.1)

Proof: the first relation is y0=s_j, y1=a_(j-1)s_(j-1). For the second, substitute y2=b_(j-1)a_(j-2)s_(j-2), then cancel the two a_(j-2) factors in r_(j-2)=s_(j-2)a_(j-2)s_(j-1). The third follows from r0r1r2=-1. All three right-hand pair-products are signed-frame invariants (each y_t changes by the same detector-axis reference sign). Thus known delta recovers the entire four-state relational sector without any absolute sign reference.

In particular, **it is sufficient that this single edge retains its sign from the first to second scattering**, a_(j-1)=b_(j-1), so delta=+1. The other two V5 generator edges may flip simultaneously while preserving product -1. Fixing all three generator edges is stronger than necessary.

**Theorem A2 (exact ambiguity when the next generator is independently free).** For every possible three-read word y, precisely **two** initial r-sectors are compatible with the unrestricted four-by-four two-twist model. They have the same r_(j-1)=y0y1 and opposite values of the remaining two link signs. Among the 16 microscopic (s,a,b) cases for that y, eight give each sector. One binary readout of delta is therefore both necessary and sufficient for the full r-sector.

This ambiguity **persists for arbitrary finite and infinite fixed-axis readout histories** if every later generator may independently be any V5 twist. The all-length claim is constructive. Choose either desired initial r compatible with r_(j-1)=y0y1. Set s_j=y0, choose the other two initial s signs, force a_(j-1)=y1/s_(j-1), then choose a_(j-2) to realize the desired r_(j-2), and use the product constraint to determine a_j. At each subsequent step t>=1, given current s^(t) and prescribed next detector sign y_(t+1), choose the fresh edge a^(t)_(j-1)=y_(t+1)/s^(t)_(j-1). One of the remaining edges may be chosen freely and the last is determined by their product -1. This extends the same readout history from **both** initial r sectors, however long the history is. The original source identities and signed branch words remain distinct, so the example is a fiber ambiguity, not a loss of source in the proof.

**Finite evidence.** The accompanying [named-link test](check_link_readout.py) checks all 384 two-twist inputs, all three detector axes, and for each axis all 8,192 five-step histories (8 initial signed words × 4^5 generator words). Each of the 64 six-read words has exactly two possible initial r-sectors. The [exact check summary](link_results.json) records these counts. The unbounded statement rests on the construction above, not on extrapolating from five steps.

**Scientific consequence.** The minimal native bridge is now precise: obtain either (i) a native signed edge-continuity law at the detector's predecessor edge, or (ii) one invariant inter-event tag delta. The raw sign parity P still requires a separately defined absolute frame reference; the relational r does not. Whether such edge continuity is licensed in the full Cell/Link/Port TRIADIC_CLOSURE_E event is the remaining domain-specific question.


## Appendix B — V39 based-loop readout: why two stored frames lose one link bit

The prior fixed-port note constructs a specific V39 controller: three sequential source-driven packet choices, ABC for b_t=0 and ACB for b_t=1, where b_t=(y_t+1)/2. The frame increment for each 1 choice is the same 3-cycle g, so after the first, second and third packet

    h1=g^(b0),  h2=g^(b0+b1),  h3=g^(b0+b1+b2),

with all exponents understood modulo three. The previous parity receiver used **only h2,h3**, because h2 distinguishes the exact count b0+b1∈{0,1,2}, and h3-h2 recovers b2; thus the sum b0+b1+b2 and raw parity in a calibrated reference frame are known.

**Theorem B1 (sharp two-versus-three frame distinction).** For the invariant-link target r in Appendix A under a fixed V5 generator, the pair (h2,h3) has six possible outputs on the eight signed input words. Four outputs each determine one r; the other two outputs each contain **two different r states**. In contrast, the three frame observations (h1,h2,h3) distinguish all eight signed words and therefore recover the entire r exactly. This result holds for all three detector axes and all four fixed V5 twists.

Proof: h2 identifies n=b0+b1∈{0,1,2}; h3 then reveals b2∈{0,1}. When n=0, (b0,b1)=(0,0); when n=2, (b0,b1)=(1,1). Thus four output cells (two b2 choices for each of n=0,2) identify the full word. When n=1, (b0,b1) can be (0,1) or (1,0). These two alternatives have the same y0y1=-1 but *opposite* y1y2 and therefore different r_(j-2), proving the two ambiguous output cells. A first-frame snapshot gives b0=h1 exponent∈{0,1}. Then b1=n-b0 and b2=(exponent(h3)-n) mod3, so all three signs and the relation r are recovered. The proof does not assume a native self-triggering V39 event; it applies to the previously defined controlled packet interface.

**Receiver limitation:** the two-frame ambiguity is exact for this specific accumulated-C3 packet language and observer, not a bound on all possible V39 encoders, BRC source histories or multi-channel instruments. It shows that a readout proven sufficient for raw *three-sign product* need not preserve the finer four-state relative-link invariant.

The [V39 exact checker](check_v39_link.py) enumerates 3 detector axes × 4 fixed twists × 8 initial sign words. In each of twelve contexts it finds exactly 6 two-frame codewords (4 singletons and 2 doubletons) and 8 distinguishable three-frame codewords. Read the frame snapshots at **all three packet boundaries** to recover the two gauge-invariant link bits without a calibrated absolute sign frame when generator-edge continuity holds.

Taken together, Appendix A and B identify two distinct dependencies for a genuinely native, reference-independent triadic sensor: (i) edge-sign continuity or one inter-event invariant delta, and (ii) retaining enough V39 intermediate packet-state information to recover both independent link signs.
