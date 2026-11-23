# R284FZ — An all-q explicit first-edge obstruction on the p3/p5-heavy three-pattern carrier

Date: 2026-11-23 (Asia/Shanghai). Research mode: informed portable TASK_RESEARCH, unshared scientific note.
Status: AUTHOR_ANALYTIC_PROOF / EXPLICIT_INTEGER_WITNESS_CHECKED / NOT_INDEPENDENTLY_REVIEWED.
Scientific lineage (unchanged frozen premise): R284CO -> R284FM/R284FT -> R284FW/R284FX -> R284FY. This is a finite binary observer lemma within Enterprise Math, not an amendment of P000 or the ACTIVE Heartbeat X6 ontology.

## New theorem

Let q>=5, u=1, and consider the exact four-phase reset-free omission/noisy-read model of R284FM and R284FT. Normalize c0=0 and restrict to three nonconstant column patterns:
- p3=(0,1,1,0), multiplicity a=2q+s;
- p5=(0,1,0,1), multiplicity b=2q+t;
- p6=(0,0,1,1), multiplicity c;
with integers s,t>=3, c>=0 and s+t+c<=9. Other column types have multiplicity zero.

**Theorem (uniform first-edge exclusion).** Every ordering of attempted writes on publication edge 0->1 has a prefix whose radius-one observation ball intersects a *stable* radius-one observation ball of phase 2 or 3. This holds with **zero misses on the currently attempted edge**, and with at most q misses per earlier relevant publication edge. Thus no member of this entire infinite-parameter family admits a correct non-atomic four-phase publication protocol.

**Corollary for R284FY.** All its a-dominant stable-admissible three-pattern families at widths n=4q+8 and n=4q+9 fail on the very first publication edge, for every q>=5: respectively 3 and 7 histogram families (10 total). This supplies an analytic first-edge obstruction for these templates; R284FY's other 15 stable-admissible templates and the unrestricted seven-pattern problem remain separate.

## Explicit adversarial prefix barriers

On edge 0->1 only types p3 and p5 change; p6 remains zero. Let i and j count attempted/successful writes of p3 and p5 at a prefix. Select an omission-free current edge (a legal adversary choice), so the written p3 and p5 bits are exactly one.

Define the safe-corridor strict inequalities

    i <= s-3,       j <= t+i-3.                       (1)

There are two types of boundary node:

**Boundary A:** i<=s-3 and j=t+i-2, crossed when a p5 write increases j. An actual prefix state and a legal stable phase-3 state can be selected at Hamming distance exactly 2.

**Boundary B:** i=s-2 and 0<=j<=t+s-6, crossed when a p3 write increases i from s-3 before Boundary A. An actual prefix state and a legal stable phase-2 state can be selected at Hamming distance exactly 2.

Every monotone count path from (0,0) to (a,b) crosses A or B: starting at (0,0) satisfies (1), while reaching i=s-2 violates its first inequality; if the second inequality is violated earlier the crossing is A. At B the previous safe node has i=s-3 and j<=t+s-6. All thresholds are positive, at most the available bit multiplicities.

Since two binary words at Hamming distance 2 possess a common word at Hamming distance 1 from each, the radius-one readout balls intersect at each such boundary. Correct stable decoding of phase 2/3 forces the prohibited third-phase observation during the 0->1 publication.

## Constructive omission witnesses and exact budgets

All omissions below are on **last nominal change edges** of their respective column types, as in R284FM; error histories on the compared phase-prefix state and the stable state may be chosen separately. Distinct edge budgets must not be merged.

**At Boundary A (third phase 3):** The prefix has i newly written p3 bits equal to 1 and j newly written p5 bits equal to 1. Choose the preceding phase-0 state by omitting the 3->0 change on q *unattempted* p5 bits; those remain 1. In a stable phase-3 state, omit the 2->3 changes on the i written p3 bits (so they are 1) and on q-i distinct unwritten p5 bits (so they are 0). This spends exactly q omissions on the phase-3 edge 2. Omit the 1->2 changes of all c p6 bits in the phase-3 history (the p6 last-change edge 1), so they remain 0. The resulting p3 and p6 bits match exactly. Among p5 bits, the prefix and phase-3 state match on j+q+(q-i) bits, leaving

    b-j-q-(q-i) = (2q+t)-(t+i-2)-2q+i = 2

mismatches. Source edge-3 misses=q; target edge-2 misses=q; target edge-1 misses=c<=3<=q. Also i<=s-3<=3<=q, so all allocations exist.

**At Boundary B (third phase 2):** Omit the 2->3 changes on q unattempted p3 bits in the preceding phase-0 history; they retain value 1 across 3->0. In a stable phase-2 history, omit the 0->1 changes on q *different* unwritten p3 bits, leaving those 0. On all j newly written p5 bits, omit the 1->2 changes so stable phase-2 bits retain value 1. On all c p6 bits, also omit the 1->2 changes so stable phase-2 bits retain value 0. The p5 and p6 bits match exactly, and of the a-i remaining p3 bits exactly

    a-i-2q = (2q+s)-(s-2)-2q = 2

differ. Source last-change edge 2 misses=q; target edge 0 misses=q; target edge 1 misses=j+c<=t+s-6+c<=3<=q. These are separate legal per-edge budgets.

The word choices on each side are reachable under arbitrarily old retained omission residues: an anomaly in a column persists until its next successful nominal change. Both witness pairs consist of allowed physical states, rather than a relaxed distance surrogate. No current-edge write needs to fail.

## Parameter scope, verification, and next question

The argument only needs s,t>=3, c>=0, s+t+c<=9 and q>=5; hence it covers a larger 16-template (k=8,9) carrier family than the 10 stable-admissible a-dominant histograms of R284FY. The proof is valid for arbitrary q in its domain, not extrapolated from finite enumeration.

Independent local exact integer/bit-word checker: `R284FZ_explicit_prefix_witness_checker.py`. It constructs both witness words, asserts exactly two differing bits, checks each last-edge omission budget, and covers every boundary node of all 16 templates at each q in {5,6,7,13,32,64}. Observed 16 templates and 74 boundary witness pairs per q, with no failed assertions. This is arithmetic corroboration of the symbolic construction, not an external independent mathematical Review.

The complete scientific scope remains the four-phase binary observer, with its prior frozen input and provenance preserved. The result neither classifies the remaining {3,5,6} three-pattern templates (c-dominant and dual-dominant) nor eliminates extra column types {1,2,4,7}. Next: construct uniform first-edge barriers or safe-first-edge structural conditions for the remaining 15 three-pattern templates; then analyze the 48 additional stable seven-pattern patterns observed at n=4q+9. The conjectured unrestricted n_min(q,1)=4q+10 for all q>=2 remains open.
