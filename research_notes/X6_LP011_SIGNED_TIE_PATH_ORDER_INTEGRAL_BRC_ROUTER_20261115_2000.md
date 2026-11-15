# X6 LP011 — integral provenance-safe path-order routing at signed dominant-axis ties

Date: 2026-11-15 20:00 Asia/Hong_Kong. Parent: \`RS-X6-LEGACY-PLANE-RECONCILIATION\`; publication \`TP2-B4A441B23DA3159232C2\`. Author: X6 on-hour TASK_RESEARCH lane (continuing prior author-side LP011 #38). Status: **AUTHOR-PROVED / EXACT FINITE TEST / NONBLIND / UNREVIEWED / NOT_ADMITTED**. No native benchmark, formal Result, independent Driver review, or historical wrong-caller attribution is claimed.

## Pinned type and question

Preserve frozen signed-X6 P000 V5 at \`awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:p000_reality_foundation.json\`. For \`z=(z_1,...,z_6) in Z^6\` nonzero, let \`L=sum |z_i|\` and \`B(z)=L! / product |z_i|!\` count free shortest ordered native signed-axis words. Let \`M=max |z_i|>0\`, and let \`T(z)={(i,sign(z_i)):|z_i|=M}\` be the **named signed dominant tie set**, of size \`m\`. The earlier exact LP011 N=2500 census gives 102539052 endpoints and tie sizes 1..4, with 3338160 endpoints having ties. Counting each tied label as a separate Cell introduces duplicate Cell and path mass. Find a deterministic **word-level**, integral, symmetry-respecting route without inventing a singleton function of the endpoint alone.

## New theorem: all first-appearance tie orders are equipotent

For each shortest native signed word \`w\` realizing \`z\`, scan from left to right and record the *first occurrence* of each symbol in \`T(z)\`. This yields a permutation \`ord_T(w)\` of all m named signed labels. For every ordering \`pi\` of these labels,

\[
 \#\{w:\operatorname{ord}_{T(z)}(w)=\pi\}=\boxed{B(z)/m!}\in\mathbb Z .
\]

**Proof.** Every tied signed symbol occurs exactly M>0 times in any shortest word. The abstract permutation group \`S_m\` acts on shortest words by relabeling the tied signed symbols and leaving every non-tied symbol and every position fixed. Equal counts M ensure the resulting word has the same endpoint z, even for mixed positive/negative tied labels (the relabeling acts on signed *step symbols*, not the physical Cell coordinates). The action is free: an invariant word contains every tied symbol, so its pointwise symbol relabeling fixes all tied labels. It transports any specified first-appearance ordering to any other, hence is transitive on the m! ordering classes and defines bijections between them. Their disjoint union has B(z) elements. QED.

The first tied step therefore gives a canonical, **integer** allocation of \`B(z)/m\` words to each named dominant label. The full first-appearance order gives an m!-way provenance-preserving partition with \`B(z)/m!\` words per order. This is a mathematical partition of **paths**, not an S_m-equivariant endpoint-only selection of one dominant axis.

An endpoint-only equivariant singleton dominant selector is impossible on any nontrivial tie whose symmetry exchanges tied labels: the endpoint is fixed under such label exchanges, while no individual tied label is fixed. The word-level routing resolves the information need using already legitimate native path order, without arbitrary tie breaking or fractional path multiplicities. These are combinatorial symbol-renaming statements; no Enterprise physical rotation theorem is presumed.

## Exact N=2500 certificate and separate small-word enumeration

A pure Python stdlib exact checker exhausts all **3356 nonincreasing absolute square decompositions** of 2500 into six entries, counting all signed labeled endpoints by multiset permutations/sign choices. For each tuple it computes exact multinomial B and verifies \`B % factorial(m) == 0\`. Orbit-weighted counts and BRC masses independently reproduce the prior N2500 census:

| m | Signed endpoints | Exact free-shortest BRC mass |
|---:|---:|---:|
| 1 | 99200892 | 35475223480934449276968789614961077811398352519117351449193109599974530182415341882442005421332 |
| 2 | 3275520 | 8110893186798064638027688698967289983674264472806249147897587041553729333322631577221695358080 |
| 3 | 61440 | 2677814761198139674727581468527950118702144444354117740270567960348335461723017382023533363200 |
| 4 | 1200 | 1180206073344738821666738381471760663663866636929863218899499116432258805760 |

Total exact BRC mass:
\`46263931428930653590904265855801056735441499817749479001025131238806458196360489958119492948372\`.

All six signed primitive axis labels have equal **allocated** BRC mass under first-occurrence routing by coordinate permutation and sign reversal bijection of the entire N=2500 shell, namely
\`3855327619077554465908688821316754727953458318145789916752094269900538183030040829843291079031\` per signed label (total / 12). This is different from the prior #38 *membership* mass, which double-counts ties.

The independent small-word generator enumerated all shortest words and checked exact equipartition across tie orders for signed examples \`(1,1,0,0,0,0)\`: B=2, 2 orders, 1 each; \`(-2,2,1,0,0,0)\`: B=30, 2 orders, 15 each; \`(1,1,1,0,0,0)\`: B=6, 6 orders, 1 each; \`(2,-2,2,1,0,0)\`: B=630, 6 orders, 105 each. Full checker locally executed with **PASS / exit code 0**, using exact integer arithmetic; no floating-point approximation.

## Consumer contract, provenance and remaining parent work

For a true current LP011 consumer needing an exclusive dominant-axis **path attribution**, offer \`first_tied_step(word)\` or \`first_appearance_tie_order(word)\` with exact integer fiber sizes. For a pure endpoint readout, preserve the full \`T(z)\` set; a singleton choice changes symmetry/observation semantics. Verify the actual caller's input type and output before making a code patch.

Already-read true current consumers \`research_checks/X6_LP011_SIGNED_DOMINANT_FIBRE_CHAMBER_20261112.py\` (blob \`1ee09fdd...\`), \`research_checks/X6_LP011_TYPED_DOMINANT_CONSUMER_20261112.py\` (blob \`cf2c11...\`), and native \`signed_brc.py\` (blob \`300a96e3...\`) retain correct signed tie/path type. Inspected frozen \`experiments/x6_native_coordinate_completion_v7_20260905/x6_coordinate.py\` (blob \`ef66285d...\`) and \`experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py\` (blob \`ac32f6d...\`) implement explicitly derived min-zero quotient versus signed Cell semantics, not the alleged LP011 native bad singleton selector. Actual specific historical wrong caller remains **UNRESOLVED_PROVENANCE**. A true erroneous positive natural N-BRC signed-cancellation caller LP019 likewise remains unlocated.

The original R063 unchanged 17-gate and full r=1..512 native replay still needs an authorized same-object runner [execution-support #2416](https://github.com/awdawmip/enterprise-math/issues/2416); this finite combinatorial theorem does not execute that experiment. The 28-LP active downstream dependency closure and independent Driver REQUEST_REVISION remain open.

Highest Native Source checkpoint before this new note: units **#1–#38 SOURCE_CHECKPOINT_PUBLISHED**, original request \`onhour-20261115-1936-x6-units37-38-semantic-source-progress-v1\` verified SUCCEEDED, source \`d2abe977942b39693219535bde40d6265e1a2744\`. Preserve original Research SID \`MCP-082892eb480e45dea6d4b9fcc0491034\`, CLAIM \`MCP-30a8f5fd123215e08bd4a7cf\`, RUN \`RUN-3356cbe3c2b4916d79399941\`. The read-only continuation \`x6-read-continuation-20261115-1958-v1\` succeeded with \`execution_authorized=false\`; publication of a new native semantic unit requires original-holder fresh authorization. This is author-side, not an assertion of the live run being writable from this transport.
