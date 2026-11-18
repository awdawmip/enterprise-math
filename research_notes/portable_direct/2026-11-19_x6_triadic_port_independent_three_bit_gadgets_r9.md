# X6 observer X (R9): fixed-source Port-quotient minimality and exact three-bit-per-block history residual

Date: 2026-11-19 (Asia/Shanghai). Status: author-side exact **conditional** finite event model theorem; independent review NOT_REVIEWED, no native physical admission or Foundation promotion. Task line: RS-X6-NATIVE-TIME-DYNAMICS / TP2-91D4A7C2F63805BE21A3. Scientific input remains frozen at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389; current operating rules were read separately.

## Exact predecessor and model

R8 source: [one-shot guarded triadic target conflicts, future-safe quotient, and 1-bit Port residual](2026-11-19_x6_triadic_one_shot_target_conflict_future_quotient_r8.md), introduced at commit 1035fb48b57069bf3b783f269170caa85346edff; its exact Boolean-BRC program and result are present at commit 202c8b0087cbbb62d528fa95d4e748a5cf5bad19. R8 proved sufficiency of the (R,X) future-safe quotient for labelled original-source/Port one-shot events. This R9 settles necessity **within a fixed remaining-original-source set** and constructs arbitrarily many independent Port-history bits inside six fixed signed spatial coordinates.

Retain exactly R8's narrowly declared model. Relative raw Cell positions form a Z^6 affine torsor chart about a *chosen* Cell anchor, not a distinguished global origin. An ordered frame F=(i_0,i_1,i_2) consists of three distinct native axis indices. Each original occupied source Cell contains its own ordered source-labelled triple of three nonzero positive signed-axis primitive tokens. The conditional model **declares** TRIADIC_CLOSURE_E(F) admissible; it has not established that this arbitrary token triple satisfies the actual native force-closure law. A labelled event (s,r), where r is an original Port in {0,1,2}, moves the entire source triad once from occupied original Cell c_s to vacant target c_s + E_(i_r). The event remembers source, Port, branch and order. All moved triads remain occupied but frozen for the rest of the one-shot episode; only still-unmoved original sources may emit another event. One native-axis step, not a diagonal, is the primitive operation. No silent event, numeric force cancellation or physical clock is postulated.

The coarse observer sees the exact per-original-source departure counts (and therefore any local phases determined only by those counts); the required output is the complete set of all finite legal **decorated (source,Port) future words**, including the empty word. The underlying typed Boolean-BRC carrier retains signed six-coordinate Cell occupancy, distinct source-labelled triads and ordered branches until observer-specific future preservation is proved. Positive Boolean branch support is not substituted for signed amplitudes.

## Theorem 1: necessity and sufficiency of (R,X) at a fixed remaining-source set

For each reachable state u, define:
    
    R(u) = {original sources that have not departed}
    T_R  = union_{s in R, r in {0,1,2}} {c_s + E_(i_r)}
    X(u) = (occupied relocated-triad Cells) intersect T_R

Fix static source geometry, frame and a particular set R. Two reachable states with this **same** remaining-original-source set R have equal full decorated future languages **if and only if** their X sets agree. If the X sets disagree, their one-step labelled languages already disagree.

Proof. If X agrees, R8's actual future-quotient theorem applies: an event (s,r) is enabled exactly if s belongs to R and target y=c_s+E_(i_r) lies neither at any remaining original source Cell nor in X. After a legal event:

    R' = R minus {s}
    X' = (X union {y}) intersect T_(R')

All future suffixes are preserved by induction because T_(R') is contained in T_R.

Conversely choose y in the symmetric difference X(u) △ X(v). It belongs to T_R, so it is the target y=c_s+E_(i_r) of at least one remaining original s. In one state it is occupied by a relocated triad and blocks (s,r). No remaining original source Cell can equal y: those originals are still occupied and the model enforces exclusive occupancy. In the other state y is absent from X, so no relocated triad occupies it (y lies in T_R); no remaining original source occupies it either. Thus the same labelled event (s,r) is enabled in exactly one of the two states. Their one-step languages differ, proving necessity. QED.

Let 𝓧_R be the finite set of actually reachable X values when precisely R originals remain. For the fixed-count/fixed-R coarse observer, the exact number of distinct full future languages is |𝓧_R|, and the minimal worst-case fixed-length recovery code uses

    b_R = ceil(log2 |𝓧_R|) bits.

This is a fixed-R claim: across different R, blocked/dead source labels may admit further language-equivalent merges. It is not a quotient for observers measuring complete numeric occupancy or later relocation.

## Theorem 2: 8^n exact languages and 3n necessary bits for any n in six dimensions

Let n be any positive integer and F=(i_0,i_1,i_2) any ordered frame of distinct axes. Choose one unused axis h not in F, and put σ(j)=(j+1) mod 3. Define n groups of four distinct original sources by:

    b_g       = 10*g E_h,                           g=0,...,n-1
    c_(B_g)   = b_g
    c_(A_gj)  = b_g + E_(i_j) - E_(i_σ(j)),          j=0,1,2.

Each source occupies an independent labelled ordered triad. The relative source Cell displacement between b_g and c_(A_gj) is a coordinate relation, NOT one primitive off-axis segment. Only original-to-target unit-axis relocation is primitive.

For each independent bit β_(g,j) ∈ {0,1}, let A_gj execute exactly once:

    β_(g,j)=1: take Port σ(j) -> b_g + E_(i_j)                     (shared target)
    β_(g,j)=0: take Port j    -> b_g + 2 E_(i_j) - E_(i_σ(j))      (safe target).

All 3n chosen A events are legal in any fixed prescribed ordering. To check this directly: every original A position has one +1 and one -1 on different frame axes; every shared target has exactly one +1; every safe target has +2 and -1. Consequently none of these occupied destinations equals an original source position, and the shared and safe destinations for different indices are pairwise distinct. Different groups lie on disjoint h-coordinate levels 10g and each move preserves h.

After these events every A_gj has departure count 1 and every B_g count 0, regardless of the bit vector β. Thus all 2^(3n) histories are indistinguishable under the full original-source count observer (and all count-derived phases). Source B_g remains at b_g. The target of its Port j, namely b_g+E_(i_j), is occupied **if and only if** β_(g,j)=1. Hence

    Allowed(B_g) = {j in {0,1,2} : β_(g,j)=0}.

Changing any bit changes the actual enabled decorated one-step event label (B_g,j). So the 2^(3n) constructed histories represent 8^n pairwise distinct full future languages.

They also exhaust all possible language *classes* within the coarse-observed fiber at the cut where every A has departed and no B has departed. Any history there, including histories selecting the third unused A Port, can influence remaining B futures only through whether each of their 3n Port targets is occupied. No groups' candidate B targets meet, and departed A are frozen. Hence there are at most 2^(3n)=8^n enabled-Port patterns and, by Theorem 1/R8, at most that many languages. All 8^n patterns were realized above.

Therefore the exact worst-case extra state for these labelled futures is

    M(n) = 8^n,       b_all(n) = ceil(log2 M(n)) = 3n bits.

The residual scales linearly with source population while remaining within six spatial dimensions. Its source is joint occupancy/Port history, not a seventh spatial coordinate, physical time calibration, signed force amplitude or BRC representation error. This establishes the conditional one-shot model's **ability** to produce extensive history-dependent future language, not that native X6 physics actually implements this model. QED.

## Theorem 3: productive quota completion and exact word counting

If the acceptance target additionally requires a final departure of **each** of the n remaining B_g sources, productivity holds iff each B_g has at least one allowed Port. Each B has seven nonempty Port subsets out of eight. Because groups' footprints are disjoint, all such choices admit a complete labelled future. Thus the complete-future productive-language classes number exactly

    M_productive(n) = 7^n,
    b_productive(n) = ceil(log2(7^n)).

For example n=6 gives 7^6=117649 and b_productive=17 bits, whereas the unrestricted finite-future-language observer requires 18 bits.

Put a_g = |Allowed(B_g)|. The number C_l of *ordered decorated legal future words* of length l (with 0<=l<=n) is

    C_l = l! [z^l] PRODUCT_(g=0)^(n-1) (1 + a_g z);
    C_n = n! PRODUCT_g a_g.

Proof: select l distinct remaining named sources, choose one of their a_g enabled Port labels independently, and order the selected sources arbitrarily. No selected B departure modifies any other B Port target; thus this counts every word exactly once. But the numeric generating polynomial does NOT by itself preserve the decorated future language: at n=1, enabled sets {0,1} and {0,2} yield identical 1+2z yet different one-letter labels. The (R,X) target relation is a genuine extra observer direction beyond cardinality. QED.

## Exact reproducible Boolean-BRC verification

Program: [x6_triadic_port_multibit_brc_verify.py](x6_triadic_port_multibit_brc_verify.py), local tested SHA256 25c900c50528de1ed655cf1c3aa7b7a3062e803cb9cc0c93d96d7e026591f86d. Result: [x6_triadic_port_multibit_brc_results.json](x6_triadic_port_multibit_brc_results.json), local tested SHA256 bcb48544fd93593543208d0049450beb536bb581e78be12aa399d3811a3663a5.

    python3 x6_triadic_port_multibit_brc_verify.py > x6_triadic_port_multibit_brc_results.json

PASS: all 120 ordered frames, all 8^n bit histories per frame for n=1 and n=2, plus all 8^n histories at F=(0,1,2) for n=3 and n=4. Total 13,248 exact branch-history cases; 13,248 exhaustive decorated finite-future language enumerations, at every suffix length; 51,360 B labelled quotient-successor checks. Each computed complete/prefix word cardinality matches Theorem 3; each projected B target bit matches the original guarded occupancy and continues to do so after enabled B moves. The checker carries the source ID, ordered positive signed-axis triad tokens, current six signed-coordinate Cell occupancy, moved-source ledger, branch order and labelled future word. There is no π or classical trig computation. The arbitrary-n theorem comes from the exact combinatorial/Cell-separation proof, not from finite extrapolation. It has not been independently peer-reviewed or physically validated.

## Open native boundary and continuation

1. Derive real native TRIADIC_CLOSURE_E and joint-force/Port admissibility for a proposed triad from the P000-compatible native relational contract. Here closure is a **declared candidate assumption**, never an established native law.
2. Investigate repeated relocation from already-moved targets and changing environmental resources. R8/R9's target projection may then lose future-relevant occupancy; establish a new typed BRC descent certificate or retain full branch provenance.
3. For any claim about a specific native three-dimensional research slice, supply its actual embedding and third-coordinate meaning/readout, then prove updates stay in that slice. The present construction is in the full six-dimensional torsor and does not silently promote a two-coordinate notation into a native slice.

Source and authorization note: GitHub scientific work is independently saved under the portable protocol. Native control checks in this execution returned BACKEND_IDENTITY_CHECK_UNAVAILABLE with operation_sent=false; no present Researcher-ID, Activity or live formal CLAIM could be authenticated. Historical EM-X6-214D9C or other predecessor authors must not be borrowed. This publication does not write formal native PROGRESS, Result or Review.
