# R757 — Source-defined V39 bow-tie three-packet closure with non-Abelian orientation residual

**Status:** exact group theorem, source-backed V36/V37/V38/V39 based-loop macro construction, finite S3 verifier PASS; author research, not primitive `TRIADIC_CLOSURE_E` admission or independent Driver approval.
**Task:** `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`.
**Researcher:** `EM-X6-D25F40`; original activity `RA-CAA90D5BD12F505657A65DC6`; run `RUN-c99655fb22237769554480ab`, resumed generation 2 by request `research3-20261113-0120-resume-r756`.
**Frozen P000/science:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` (not repinned).
**Comparison input (not repinning science):** `awdawmip/enterprise-math@deb8bbbf9d844c0ceb777631e576763a634eed99`, `research_notes/X6_ACTIVE_LOOP_TO_DIRECTED_RING_REALIZATION_V36_20260906.md`, `X6_NONABELIAN_HOLONOMY_OVER_ABELIAN_CYCLE_CURRENT_V37_20260906.md`, `X6_ZERO_CURRENT_NONABELIAN_COMMUTATOR_MEMORY_V38_20260906.md`, `X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md`, `X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md`.
**Earlier author results:** R754 PR #2184, R755 PR #2185, R756 PR #2190.

## 1. Positive construction in the actual V39 based-loop language

The V37/V38 bow-tie network has one common Cell x0, based active support 012, and two *completed* directed triangular loop packets:

- A: 012 -> 013 -> 023 -> 012, with `j(A)=c_A=(1,0)` and `h(A)=a=(0,2,1)`;
- B: 012 -> 023 -> 123 -> 012, with `j(B)=c_B=(0,1)` and `h(B)=b=(1,0,2)`.

Their physical rings and return of active supports are sourced in V36/V37. V38 explicitly uses the based inverses A^{-1}, B^{-1}, with negative net currents and inverse holonomies. In V39's *declared* based-loop future language, finite compositions of admitted based packets remain composable at the shared base. Define the third **macro-packet**

`C := B^{-1} ; A^{-1}`.

Then C is a *composite* completed based packet, has `j(C)=(-1,-1)`, and transports the base frame by `h(C)=h(A^{-1}) ∘ h(B^{-1})=a^{-1} ∘ b^{-1}=(2,0,1)`. Here `h(P;Q)=h(Q) ∘ h(P)` is exactly V39's composition convention, not the opposite convention chosen silently.

Every block A, B or C separately returns the declared active support to base. Thus **all six permutations of these three completed macro-packets** are admitted continuations inside V39's based-loop language and the V36/V37/V38 bow-tie realization assumptions; this is an actual legal packet triple at this *macro* level. No identification of C as one primitive force quantum or of a block with one V29 PASS is made.

## 2. General theorem: balanced three-packet macro and reverse-order obstruction

Let L be a based-loop group of reversible packets (or its actual reversible sublanguage), with homomorphism j into an abelian current group and compositional frame transport h into a group G. For arbitrary admitted A,B with admitted inverses, put C=B^{-1};A^{-1}. Then for every permutation sigma of the three named blocks, `j(sigma(A,B,C))=0`. The three forward cyclic block orders A;B;C, B;C;A and C;A;B have `h=e`. The other three permutations all have nonidentity final h **if and only if** h(A) and h(B) fail to commute.

**Proof.** Abelian additivity gives j(C)=-j(B)-j(A). By inverse and associativity, A;B;C=A;B;B^{-1};A^{-1}=identity packet; its two cyclic rotations are conjugates of identity, hence carry h=e. Writing the path-order transport product `x★y:=y∘x`, we have `c=(a★b)^{-1}`. One reversed product equals `a★c★b`; it is identity exactly when `a★b=b★a`, by multiplying by the appropriate inverses. The two other reversed products are conjugate to this one (cyclic rotation). Therefore either all three reverse products are identity (commuting pair) or all three are nonidentity (noncommuting pair). This argument is exact for every group G. QED.

This theorem produces an *explicit macro-level three-packet closure*, rather than merely classifying hypothetical S3 labels, and supplies a direction-sensitive residual despite exact zero current.

## 3. Concrete S3 classification and full V29 occurrence equality

For V37's actual transposition maps, our exact V39 convention gives:

| macro block order | final j in (c_A,c_B) | exact final frame |
|---|---|---|
| ABC | (0,0) | (0,1,2) |
| ACB | (0,0) | (2,0,1) |
| BAC | (0,0) | (1,2,0) |
| BCA | (0,0) | (0,1,2) |
| CAB | (0,0) | (0,1,2) |
| CBA | (0,0) | (1,2,0) |

Because C expands to B^{-1};A^{-1}, every schedule has exactly the same four directed physical ring traversal occurrences `{A+,A-,B+,B-}`. Within V29's matched-TRANSFER grammar, this implies identical final **nonnegative directed TRANSFER count histograms** (each directed edge of each circuit occurs once in each direction), identical net current and zero scalar accumulation, even though their V39 frame results differ. This is a sourced COUNT/FRAME construction, not an assertion about three local PASS events.

The exact endpoint-frame fiber sizes are 3, 2 and 1. A fixed-length outcome repair for the declared final `(j,h)` observation needs `ceil(log2 3)=2` additional bits beyond the common full directional histogram; the narrower yes/no final frame closure `h=e` needs 1 bit. If six block orders are additionally sampled uniformly, their final-frame probabilities are (1/2, 1/3, 1/6) and the exact entropy is

`H=(1/2)log2(2)+(1/3)log2(3)+(1/6)log2(6)=1.4591479170272448... bits.`

Uniform scheduling is only an auxiliary ensemble; the deterministic group and counting statements do not use it.

## 4. Finite verification and relation to mother objective

`R757_V39_BOWTIE_PACKET_VERIFY_20261113.py` enumerates all six macro schedules, checks the exact S3 maps, ring-current and four-direction occurrence histogram, and checks the general closure-versus-commutation claim for all `6^2=36` pairs in S3 (each six schedules). The independent algebraic proof covers every group; finite enumeration checks the concrete X6 source-labelled witness.

**Solved local frontier:** a triple of actually composable V39 based-loop **macro** packets with exact Cell-network realization, V29 matched-TRANSFER count trace and V39 frame transport. The family has three orientation-sensitive nontrivial reverse outcomes and demonstrates exact provenance loss under count-only compression.

**Remaining hard target:** a primitive typed `TRIADIC_CLOSURE_E` needs an admitted *three-force* incidence predicate, the Cell/Link/Port force-to-V29 PASS/TRANSFER trigger, and any V39 active-frame update specified by that event. Here C is two inverse loops (not one force), and based-loop composition is not a proof of primitive triadic force balance. A useful next discriminating test is to locate a source-defined force-incidence event and see whether it can assign these packet macros as a declared readout, or whether it requires a new genuine event bridge; keep the R757 V39 macro witness as a legal sublanguage example in either case.

No P000, ACTIVE worldview, frozen science, task publication, previous formal Result or Driver status is changed.
