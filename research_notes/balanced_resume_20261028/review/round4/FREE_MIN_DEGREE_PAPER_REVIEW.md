# Independent paper review: finite native-neighbour support

Reviewer: EM-REVIEW-58D6A2.
Activity: RA-BALANCE-REVIEW-20261028-58D6A2.
Finding: LOCAL_NONAUTHOR_PAPER_CHECK_NO_MUSTFIX_FOUND.
The lower bound, complete equality classification and finite-support
obstruction follow under the precise stated hypotheses. No supplementary
definition or proof repair is required by this review.

## Exact reviewed object and exposure

The complete frozen paper is
`free_round4/phase_a/phase_a_candidate.md`, candidate
`CAND-FREE-R4-FINITE-NEIGHBOR-SUPPORT-20261028-870C7C4C`.
SHA256: `cbcf739c20cc5bf30a472ef81fb5761d7bb05b88bcf15277f85777784f3eb3e8`.
The immutable Source commit is
`2033a243d6e393457c49d1c2660dc1c6bf2e02d8`, repository path
`research_notes/balanced_resume_20261028/free_round4/phase_a/phase_a_candidate.md`.

I read the complete text directly from the actual owner-provided response
`free_round4/freeze_readback_0.json`. Its content SHA256, Git blob SHA1,
immutable URL and requested path/ref agree. This was verification of an
existing actual readback, not a new remote request by this reviewer.

I did not participate in the candidate's construction, supply its question,
or provide any repair before or after this freeze. Shared control and prior
research exposure are disclosed; this is a nonauthor NONBLIND paper review,
not a clean-blind or discovery-firewall attestation. The author's
ANCHOR_EXPOSED status is retained. Phase B prior-art and tool-coverage
classification are outside my assignment and were not imported as proof.

## 1. The obstruction and endpoint cases

Finiteness and nonemptiness guarantee a maximizer of the integer sum of
the six raw coordinates. None of its six positive unit neighbours belongs
to S. Only the six negative neighbours remain possible, so some vertex
has internal degree at most six. This directly excludes every integer
threshold k>=7; it does not confuse the ambient degree twelve with a
minimum internal degree achievable by a finite set.

The stipulated parameter is an integer k>=0. At k=0, nonemptiness gives
the sharp lower bound one, and exactly the singleton sets realize it.
At k>=1, a singleton cannot satisfy the degree hypothesis, so some raw
coordinate genuinely varies. Thus the proof's nontrivial cut exists.
No connectedness of S is assumed or needed.

## 2. The lower-bound induction

Choose an integer t with min{x_j:x in S}<=t<max{x_j:x in S} in a varying
coordinate j. Integrality makes the sides x_j<=t and x_j>=t+1 a complete
disjoint partition, with no omitted intermediate coordinate values.

For a vertex on either side, only a unit step along axis j toward the
other side can cross the cut. Consequently it loses at most one of its
original internal neighbours. Its degree within its own side is at least
k-1. Each side is a finite nonempty subset of the same six-dimensional
coordinate graph, so the induction hypothesis applies to both, without
changing the ambient carrier. Their cardinalities add to at least 2^k.

The proof does not require the cut to contain any crossing edge in advance.
If a gap makes all crossing edges absent, the inherited lower bound is
still valid; the later equality argument correctly excludes such a gap
from an extremizer.

## 3. Rigidity when equality holds

If |S|=2^k, each side must have exactly 2^(k-1) vertices. Simultaneous
induction therefore identifies each side as a translated unit box on
k-1 distinct native axes. Every vertex of either such box has exactly
k-1 internal neighbours, not merely at least that many.

The original minimum-degree condition then forces every vertex to have
the one possible cross-cut neighbour. For an A vertex that neighbour is
x+e_j, so x_j=t. For a B vertex it is x-e_j, so x_j=t+1. Thus every vertex
on each side lies on its respective cut face. Axis j cannot be one of the
varying axes of A. Moreover the required map x -> x+e_j sends every A
vertex into B injectively; equal side sizes make B exactly A+e_j.

This proves alignment and identical cross-sections, rather than merely
two unrelated boxes of equal size. Their union is the claimed k-axis
unit box. At k=1 this argument simply matches two adjacent singletons,
so it has no missing first induction step. At k=6 it forces all six
axes to vary. Necessity of the entire equality classification is paid.

Conversely, in the stated box, each selected axis supplies exactly one
internal neighbour at every vertex. The opposite step exits that axis's
two-element coordinate set; every unselected-axis step exits the fixed
coordinate slice. Distinct axis choices give distinct neighbours. Thus
the degree is exactly k and the size exactly 2^k. Such boxes exist for
all k=0,...,6. Together with the obstruction, this proves all three
theorem clauses, including existence if and only if k<=6.

## 4. Native-state and interpretation boundaries

An anchor change translates the six coordinate values by constants and
does not alter adjacency or the partition argument. The sum witness then
changes by a constant, preserving its maximizing set. Signed-axis reversal
changes a unit-box representation by a corresponding base-Cell shift;
it does not produce additional extremizer types.

The ambient object remains the full signed Z6 Cell torsor throughout.
For k<6, unselected coordinates are fixed values of a restricted finite
set, not deleted coordinates or a recovered native plane. The exact A/B
partition retains all Cells and neighbour tests; it is not a compressed
state or a future-predictive quotient. The auxiliary scalar selects a
vertex but is never asserted sufficient to represent a Cell.

The resulting size 64 for k=6 is a static adjacency threshold. It says
nothing about force balance, physical persistence, dynamical accessibility,
probability or amplitudes. Replacing minimum degree by average degree,
changing unit-axis adjacency, or allowing infinite support changes the
problem. The paper states these exclusions explicitly, and the proof
does not cross them.

## Evidence grade and disposition

Validation was complete paper reasoning plus exact byte/source binding.
No scientific checker, mirrored enumeration, symbolic solver or proof kernel
was run. The induction and equality proof are sufficient without adding
sample evidence. I found no unresolved mathematical defect and contributed
no correction, new bridge, new hypothesis or second result.

This finding establishes the stated derivation in its fixed model, not
external novelty, a new axiom, a new tool family or canonical acceptance.
The author's separate Phase B may identify a known equivalent theorem;
that would affect reuse classification without invalidating this proof.
No formal Driver verdict, Task claim, Working Truth, Foundation promotion
or closure of the balanced research goal is supplied.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH
