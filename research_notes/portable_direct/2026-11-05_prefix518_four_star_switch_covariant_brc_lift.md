# PREFIX-518 — Four-STAR gluing: an S4-covariant native-X6 / BRC phase-path lift

Date: 2026-11-05 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Task: `RS-X6-NATIVE-ROTATION-DYNAMICS`. Researcher-ID: `EM-X6-FE5602`; Activity-ID: `RA-BA8544AD6DED0FDF5D892BCB`.
Frozen scientific pin: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Prior frontier: PREFIX-515 through PREFIX-517 at their published immutable source commits.

## Precise question and declared continuation relation

Can the frozen four FCC/K4 STARs be glued into a common-pivot, frame-covariant phase/path automaton which retains exact signed-X6 BRC provenance and intermediate Cell queries?

Use one **chosen native pivot Cell** P; all positions below are relative to P in the ambient six-axis X6 torsor. The four frozen STAR axis triples are
`S_A={L1,L3,L6}`, `S_B={L1,L4,L5}`, `S_C={L2,L3,L5}`, `S_D={L2,L4,L6}`.
Every pair of distinct STARs meets in exactly one line family, and every line belongs to exactly two STARs. On each triple `{i,j,k}`, use the local signed six-cycle
`(+i,-k,+j,-i,+k,-j)`, with both sweep orientations allowed. Equivalently, the neighbors of `+i` are `-j,-k` and the neighbors of `-i` are `+j,+k`. This is a valid choice of the frozen local C6 chirality convention; the adjacency graph is independent of the order of i,j,k.

Define a **candidate one-pivot switch relation**, rather than presupposing an established physical STAR-switch law: a directed state is `(S,prev,current)` with the last two phases adjacent in S. At current phase `a`, either (a) stay in S and take its unique next neighbor other than prev; or (b) switch to the other STAR S' containing the unsigned axis of a, and take either of its two neighboring phases. Each chosen macroedge `a→b` is resolved into both frozen shortest signed native microtraces
`I=(-a,b)` and `O=(b,-a)`, retaining the ordered branch label `beta=0/1`. The next directed state is `(newSTAR,a,b)`.
This defines a fully explicit typed discrete relation to test cross-STAR path compatibility. It is not an assertion that nature selects these switches.

## Theorem 1: exact one-switch branching and minimum choice information

There are exactly `4×6×2=48` directed incoming phase states (four frames; six current phases; two possible incoming neighbors).
For every state the nonbacktracking stay move is unique. The other STAR meets the old STAR only in the current axis, hence its two exit phases differ from the stay successor and from each other. There are exactly **three** admissible next phases under the declared relation.

For each such next phase b, the two native words I/O reach the same new shell Cell `P+b` from `P+a` by two signed primitive steps; their intermediate Cells are respectively `P` and `P+a+b`. Because a,b have distinct axis supports, `a+b≠0`; the six pairs `(next phase, intermediate Cell)` are all distinct. Thus each directed state has exactly **six labeled primitive microtrace continuations**.

To encode the exact outcome of an arbitrary one-step next-phase/intermediate-Cell query, any fixed-length binary choice code needs at least `ceil(log2(6))=3` bits; a ternary phase choice plus one branch bit achieves six distinct labels. This bound is for this declared per-step choice interface, not an additional lower bound on a representation already storing the entire phase itinerary.

## Theorem 2: associative full-X6 BRC / signed-area / visit-set composition

For any complete microtrace word w, let `y(w)∈Z^6` be its net signed displacement, and `p_i(w)=(N_i(w)-|y_i(w)|)/2`, where `N_i` is the total number of signed primitive steps on axis i. Retain the **full six-component** BRC cancellation vector p. For any concatenated words u,v,
`kappa_i(u,v)=(|y_i(u)|+|y_i(v)|-|y_i(u)+y_i(v)|)/2`,
`p_i(uv)=p_i(u)+p_i(v)+kappa_i(u,v)`.
This follows by adding step counts and re-evaluating the signed net displacement. It is an exact six-axis generalization of the cancellation law used in PREFIX-515.

Let `A(w)=sum_{r<t} s_r wedge s_t∈Λ²(Z^6)`, and let U(w) be the set of intermediate native Cell **offsets relative to the initial Cell of w**. Then
`A(uv)=A(u)+A(v)+y(u) wedge y(v)`,
`U(uv)=U(u) union (y(u)+U(v))`.
The latter requires a boundary-consistent concatenation of complete macroedge words. Each law is associative because it comes from actual path concatenation. Retaining the signed phase itinerary, frame itinerary and the ordered I/O bit string reproduces every primitive signed word and indexed intermediate Cell. For a fixed phase itinerary of N macroedges, the `2^N` distinct branch histories require N bits of information for exact recovery of every indexed midpoint; the bit string attains it.

For any continuation of N macroedges, every microtrace contributes displacement `b-a`; telescoping gives `y=a_N-a_0` independently of switches and branch labels. This is an exact common-pivot endpoint invariant.

## Theorem 3: tetrahedral S4 covariance and a useful observer warning

Identify the six axis labels with the six unordered edges of the abstract K4 whose four vertices are STAR A/B/C/D:
`L1=AB,L2=CD,L3=AC,L4=BD,L5=BC,L6=AD`.
Every permutation of the four STAR vertices induces a permutation F of all six native axis labels and maps STAR triples and the **unoriented** local C6 adjacency graph onto themselves. Since the directed state includes prev/current, the induced action also transports the stay/switch continuation relation. The inner/outer microtrace words, their intermediate Cells and their branch bits transport exactly. This supplies an `S4`-equivariant gluing of the declared candidate relation, with all 24 chart automorphisms.

Under F, `y↦Fy`, `p↦Fp`, `A↦Λ²F(A)`, `U↦F(U)`, and the exact concatenation formulas commute with F. The induced permutation acts as a **change of native axis labeling**; the proof does not identify it with a generated physical rotation.

The prior color-fixed five-axis BRC observer `(V,W)=(p_b+2p_d+p_e,p_c+p_e)` is not itself invariant under every such atlas automorphism. Indeed the word `(+L1,-L1)` has `p_1=1`, all other p_i zero and `(V,W)=(0,0)`; the K4 vertex permutation `(A,B,C,D)↦(C,D,A,B)` sends line L1=AB to L2=CD, giving `p_2=1` and `(V,W)=(1,0)`. Retaining the six-component p vector and the chart-color map is sufficient to recompute V,W in a transported frame. A KMP transducer based on fixed axis-color names also needs an explicit chart/color transport or the original signed word; this is the discriminating question for PREFIX-519.

## Finite independent implementation checks

Run `node research_notes/portable_direct/prefix518_four_star_switch_certificate.js`; it uses exact integer arithmetic on signed six-component arrays. It exhaustively checks:
* all 48 directed local incoming states and their 288 labeled shortest one-step microtraces;
* all 24 K4 vertex automorphisms against all 288 one-step choices, i.e. 6,912 covariance checks;
* all `48×6^3=10,368` three-macroedge labeled histories for endpoints, indexed pivot/outer Cell recovery, six-axis BRC cross-boundary counts, 15-coordinate area composition and translated set union;
* a concrete color-observer noninvariance witness.

Executed result: `ALL_CHECKS_PASS`. The arbitrary-length and S4 assertions follow from the proofs above; the bounded enumeration checks implementation and local combinatorics.

## Sources and next unit

Frozen input: `research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md` at `f42f2906d77f24085c123f3ccfe9667d41caa96d`, specifically §§3–4 and 9–11; P000 and `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json` at the task's frozen scientific pin. Previous exact controls: PREFIX-515 (cross-cancellation), PREFIX-516 (area), PREFIX-517 (indexed Cell provenance). Current normative context read through `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context` and `docs/PORTABLE_RESEARCH_PROTOCOL.md`.

PREFIX-519 should derive the minimal **frame/color-sensitive KMP–BRC transducer** under the 24 atlas automorphisms, testing whether storing the six-axis BRC p plus a finite orbit of KMP transition functions admits exact composition without full path replay. Distinguish that finite-state observer from the N-bit indexed historical Cell query and from a physical STAR-switch selection law.
