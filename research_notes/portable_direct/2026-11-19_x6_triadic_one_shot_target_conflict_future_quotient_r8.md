# X6 observer IX (R8): exact future-safe target-conflict quotient for one-shot guarded triadic transfers

Date: 2026-11-19 (Asia/Shanghai). Author-side **conditional** six-coordinate, source/port-labelled Boolean-BRC result; independent review NOT_REVIEWED. Research line RS-X6-NATIVE-TIME-DYNAMICS / TP2-91D4A7C2F63805BE21A3, frozen P000 pin awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.

## Relationship to verified frontier and exact transfer assumptions

The separately saved [guarded triadic resource-conflict result of 2026-11-18](https://github.com/awdawmip/enterprise-math/blob/f41c2690daba467ecbde99615a1337e67be46ffd/research_artifacts/mcp/RS-X6-NATIVE-TIME-DYNAMICS/MCP-456b8f22a648400585024ffbcc1c2c94/5a04daccb6795e494dbc/X6_TIME_GUARDED_TRIADIC_RESOURCE_CONFLICT_20261118.md) established three mutually exclusive ports at a single triad-bearing source and the disjoint-source configuration polynomial (1+3x)^m. The present note examines what *part* of the six-coordinate occupancy history remains required when two distinct sources have an overlapping candidate destination. It also tests the precise boundary of [R7 terminal-label reconstruction](2026-11-19_x6_penultimate_terminal_label_reconstruction_r7.md).

Let C be a Cell torsor with raw relative coordinates in Z^6, not a new lower-dimensional native plane. Choose an ordered frame F=(i_0,i_1,i_2) of three distinct axes from {0,...,5}. At each original source cell c_s is an occupied ordered token triple (s,(i_0,+,0),(i_1,+,1),(i_2,+,2)); it consists of three nonzero primitive signed-positive tokens. In this *candidate model* the predicate TRIADIC_CLOSURE_E(F) is declared true exactly as in the 2026-11-18 work; this does not independently establish physical admission or numerical signed-force cancellation.

A named one-shot event (s,r), r in {0,1,2}, moves the **whole triad** from original c_s to target c_s+E_{i_r}, iff s has not previously departed and this target is empty. The update vacates c_s, occupies its target with the same three ordered tokens, and records source/port/branch/order provenance. A source can execute at most one of its three original departures. Relocated triads are frozen for the remainder of this expressly bounded *one-shot episode*. Source cells are pairwise distinct and initially occupied; no silent event occurs. The future language is the set of possible ordered words over **decorated source/port labels (s,r)** under these guards. It does not include numeric location readouts or later relocation from a previously moved target.

## Theorem 1 — exact sufficient future-safe Port occupancy quotient

At a reachable state, let R be the set of original sources not yet departed, and let
```
T_R = union_{s in R} { c_s + E_{i_0}, c_s + E_{i_1}, c_s + E_{i_2} }
X   = (set of currently occupied relocated-triad target Cells) intersect T_R.
```
Then the pair **(R,X)** is a complete sufficient state for *all future ordered source/port event languages* in this one-shot episode, given the fixed original source geometry and ordered triadic frames. This gives an exact future-safe quotient of the provenance-labelled Boolean BRC branch carrier for this declared observer, although it does not reconstruct all six-coordinate relocated positions.

**Proof.** Every remaining source s in R still occupies its own original Cell c_s: a prior transfer could not land there while s remained, since destination occupancy is guarded. A proposed (s,r) is enabled iff s in R and its target y=c_s+E_{i_r} is absent both from the remaining original-source cells {c_z:z in R} and from X. All other occupied relocated cells lie outside T_R, and cannot equal the target of a remaining source. After a legal event (s,r),
```
R' = R \ {s},
X' = (X union {y}) intersect T_{R'}.
```
Indeed T_{R'} is a subset of T_R, so an earlier relocated target outside T_R cannot later become relevant; the newly relocated triad occupies y. Thus legality, label and successor quotient depend entirely on (R,X) and static source/frame data. Induction on |R| proves that the quotient preserves exactly all future labelled event words. QED.

When the complete original-source port footprints {c_s} union {c_s+E_{i_r}} are pairwise disjoint, X is always empty. The moved-source set alone determines all remaining source/port futures; past port alternatives are future-erasable for this observer. Overlapping destination footprints can make X necessary. The theorem asserts **sufficiency**, not a globally minimal quotient: further exact language-equivalent X values can be merged when justified.

## Theorem 2 — sharp six-coordinate two-source conflict and one-bit history residual

Take F=(0,1,2), source A at c_A=(0,0,0,0,0,0), and source B at c_B=(1,-1,0,0,0,0). All six coordinates are explicit signed relative displacements. Both sources initially carry separate ordered triads. Define t=(1,0,0,0,0,0).

The A-port-0 target and B-port-1 target coincide at t:
```
c_A + E_0 = t = c_B + E_1.
```
All other targets of B differ from A's three possible targets.

After the first event (A,0), t is occupied and the allowed one-step future language for original source B is exactly
```
L_after(A,0) = {(B,0), (B,2)}.
```
After first event (A,1) or (A,2), the corresponding language is
```
L_after(A,1) = L_after(A,2) = {(B,0),(B,1),(B,2)}.
```
All three histories have the identical exact *original-source departure count* (n_A,n_B)=(1,0), hence also identical local count phases for arbitrary declared periods. Yet their decorated Port-labelled future languages have exactly two classes. **One extra bit is necessary and sufficient** to recover that future language at this observer after A's first departure. A suitable bit is whether occupied moved-target t lies in X.

**Proof.** The whole A triad moves intact to c_A+E_r. B still occupies c_B. The only equality between an A target and a B target is c_A+E_0=c_B+E_1, found by comparing the six signed integer coordinates. B-port-1 is therefore blocked only in the r=0 history; B-ports-0 and 2 remain free for each r. No further original-A departure is allowed. There are exactly two distinct productive one-event future languages among the three first-A histories; an exact selector requires ceil(log2 2)=1 bit and the indicated occupancy bit attains it. QED.

**General pair family.** For every ordered F of three distinct axes and any r != s, take c_A=0 and c_B=E_{i_r}-E_{i_s}. Then c_A+E_{i_r}=c_B+E_{i_s}, and this is the unique cross-source target equality among their nine port-target pairs. The same two-language, one-bit witness holds. There are 6*5*4=120 ordered frames and 3*2=6 ordered off-diagonal (r,s) choices per frame.

## Theorem 3 — decorated-label quota bridge boundary

R7's exact penultimate terminal-source-label formula requires **one uniquely identified source letter per quota unit**. Here each terminal original-source quota unit has three possible *decorations* (the Port r), so several distinct future suffix words can share exactly the same source count vector and remaining source label. In the witness, the two states after A moves have the same n and the same length-zero productive prefix language {epsilon}, while the decorated one-step full languages differ.

Consequently, applying the R7 terminal-**source**-label decoder to a decorated source/Port alphabet without retaining the enabled Port subset is invalid: it would identify these two languages because the remaining source label is B for both. The correct conditional carrier either retains X as in Theorem 1, or retains an equivalent sufficient Port-observer/future-language signature. This is a counterexample to an *unproved decorated-alphabet extension* of R7, not a contradiction to R7's stated one-symbol-per-quota hypotheses.

## Exact typed Boolean BRC validation

Source `x6_triadic_one_shot_port_overlap_brc_verify.py`, SHA256 `1fa043903b10752ac04ec8732af6ffb6668d63204dae1d8f4efcdf1c5a5f8e48`. Output `x6_triadic_one_shot_port_overlap_brc_results.json`, SHA256 `bdd48a6dcbdaa6416947ff69dfef20dc6f0edeca27a717403b5683b47de2ca5a`.

Executed exact Python 3 integer/tuple program using a source/Port-labelled Boolean BRC branch carrier with full six signed Cell coordinates, ordered three-token frame, occupied-cell map and one-shot moved-source ledger. It checked all 120 ordered positive frames, all 720 shared-destination source-offset models and 2,160 first-A port histories, plus 120 far-disjoint controls. An independent operational quotient implementation compared enablement and projected successors across **18,720** reachable one-shot transitions; all equality/inequality assertions PASS. This includes two-source interleavings, not only the display example. Arbitrary-m theorem derives from the induction above; these are bounded tests.

Run `python3 x6_triadic_one_shot_port_overlap_brc_verify.py > x6_triadic_one_shot_port_overlap_brc_results.json`.

## Native boundary and next problem

The research uses P000's actual *types* (X6 Cell, three nonzero signed primitive force contributions, declared TRIADIC_CLOSURE_E predicate, separate ordered event time and source provenance) but the **inter-Cell transfer rule and frozen one-shot relocation** are specific *conditional candidate laws*. Therefore this verifies which residual is required *if* this guarded event family is adopted; it does not claim current native physical Port admission.

Next: obtain the authoritative native event-admission and repeated-relocation rules with source/target forces and environment, then test whether the same (R,X) projection commutes with those unrestricted updates. A permitted second departure from a relocated target can make discarded occupancy positions relevant, requiring an expanded typed BRC carrier. Check actual joint-force closure and preserve full three-dimensional slice embedding/readout when asserting a native-slice statement. No independent Driver review or Foundation promotion was performed.
