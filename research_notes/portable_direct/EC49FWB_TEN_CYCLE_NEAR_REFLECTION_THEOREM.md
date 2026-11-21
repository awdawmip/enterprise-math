# EC49FWB — Universal near-reflection of ten-residue masks and signed correction spectrum

Research line: independent portable continuation of EC49FWA, immutable predecessor 44f3d0c2b34267dddac7816edc8706da1f00f1ee. Frozen scientific input: BRC16943, including the original Bernoulli-to-projective 11-adic certificate; no input pin has been replaced. Date: 2026-11-21.
Status: AUTHOR_PROVED / EXACT_FINITE_INTEGER_CHECK / PARENT_DEPENDENT / NOT_REVIEWED.

## Theorem 1 — arbitrary ten-position binary masks

Let A be any subset of the cyclic group Z/10Z. For each c in Z/10Z, set F_c(A)={c-x:x in A}, and define

  delta(A)=min_c |A symmetric_difference F_c(A)|.

Then **delta(A) is either 0 or 2**. Equivalently, each ten-position binary word is exactly reflection-symmetric or can be made reflection-symmetric by relocating just one occupied position. No assumption about the frozen projective predicate is needed in this theorem.

### Elementary proof

Since taking complements preserves each symmetric difference, assume k=|A|<=5. Each difference has even cardinality. We construct some reflection with at least k-1 elements in the intersection A ∩ F_c(A).

Use Z/10Z ≅ Z/2Z × F_5. Call the points in the two parity fibers E and O, each represented by its residue modulo 5. Even reflection centers act as x↦s-x in both F_5 fibers, with the same s. Odd centers swap the fibers, and pair even x and odd y whenever x+y equals the center.

* k=0,1,2: a reflection preserves A exactly; for two points, choose their sum as the center.
* k=3: a reflection about the sum of any two occupied points exchanges them. At least two points survive, so delta≤2.
* k=4 with at least three points in one fiber: every three- or four-element subset of F_5 is preserved by some reflection. Its complement has two or one points, respectively, and any one- or two-element subset is reflection-symmetric. Choose an even reflection preserving those at least three points; the remaining point changes at most two positions.
* k=4 with two points in each parity fiber: If two cross-fiber pairs have the same sum, they are necessarily disjoint and an odd reflection preserves all four points. Otherwise their four sums are distinct. Translate and multiply residues by a nonzero F_5 scalar to put E={0,1}. The O-pair difference is then neither 1 nor -1 (either would create repeated cross sums), so we may write O={r,r+2}, r in F_5. For r=0 choose even reflection center s=2: it exchanges O and fixes 1 in E. For r=4 choose s=0: it exchanges O and fixes 0 in E. For r=1 or r=3 choose s=1: it exchanges E and fixes 3 in O. For r=2 choose s=1: it exchanges both pairs. Thus some even reflection preserves at least three of the four points.
* k=5, all points in one fiber: this full parity fiber is reflection-invariant.
* k=5, partition 4+1: choose an even center fixing the singleton in the smaller fiber. The four occupied points of the other fiber overlap their reflected four-point subset in at least three positions because both omit only one of the five. At least four points survive.
* k=5, partition 3+2: six cross-fiber pairs have their sums among only five odd reflection centers. Two different pairs must have the same sum; by cancellation they are disjoint. The corresponding odd reflection preserves at least four occupied positions.

In all cases delta≤2. Being even, delta is 0 or 2. QED.

**Sharp boundary of this universal property:** For the 11-cycle, A={0,1,2,4,7} has defects, in center order 0,...,10, equal to [4,6,4,4,4,6,6,6,4,6,10]. Hence its minimum is 4. The universal ten-cycle phenomenon is not merely a generic consequence of cyclic symmetry at any modulus.

## Theorem 2 — application to BRC16943 rational-anchor denominator masks

EC49FWA defines the exact frozen C_11(h,n), its 44-cell mod-10 factor P_10, and the left/right denominator class sets R_-(a,b), R_+(a,b) over the period T=110b, for reduced 0<a<b. Its CRT reduction gives a ten-bit primitive affine-line word U_{a,b} and an 11-bit factor V_{a,b}, with

  D(a,b) = min_d |R_+(a,b) symmetric_difference (R_-(a,b)+d)|
         = F(a,b) delta(supp U_{a,b}),

where F(a,b)=11 if 11 divides a+b, and 10 otherwise.

Theorem 1 immediately implies D(a,b) belongs to {0,20,22} for **every** reduced rational anchor, without having to enumerate all 64 non-perfect primitive mod-10 directions. The separate exact zero-symmetry criterion proved and checked in EC49FVZ is

  delta(U_{a,b})=0 iff b is even AND (5 divides a OR 5 divides 2a-b).

Thus, combined with that inherited criterion, the exact quantitative EC49FWA formula follows. The new universal lemma explains why the nonzero defect is always just one swapped pair in the primitive ten-bit word; the zero-case identification and Bernoulli-to-projective bridge retain their original proof status.

## Theorem 3 — signed positions of the optimal two-site correction

For all 72 primitive directions (a,b) mod 10, rebuild U_{a,b} from the frozen 44-cell P_10. Each optimal reflection center of a non-symmetric word has exactly two mismatched positions, an occupied site u and an unoccupied site v. Preserve the **signed** displacement s=(v-u) mod 10 and the circular distance ell=min(s,10-s).

The complete finite classification has 8 perfectly symmetric primitive directions and 64 nonsymmetric ones. The nonsymmetric optimal-center multiplicities are: 24 directions with one optimal center, 24 with two, and 16 with four, totaling **136 signed two-site corrections**. The exact signed histogram is:

| s mod 10 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| number | 12 | 24 | 12 | 20 | 0 | 20 | 12 | 24 | 12 |

The corresponding circular distances ell=1,2,3,4,5 have frequencies 24,48,24,40,0. The absence of antipodal swaps at ell=5 is a **frozen P_10 specific finite result**, not an implication of Theorem 1. These histograms enumerate all primitive direction/optimal-center pairs, not a probability distribution on rational anchors. They retain direction and sign discarded by the scalar defect D.

## Verification

Companion standalone Node.js program EC49FWB_UNIVERSAL_TEN_CYCLE_VERIFY.js uses integer modular arithmetic and reconstructs P_10 from the same rational frozen constants 4822040484/8132285009, 141024/1653649, p=11, and 637. It checks:

1. All 1024 ten-bit masks: exactly 424 have optimal defect 0 and 600 have defect 2.
2. The explicit eleven-cycle counterexample.
3. All 12,100 original projective-row comparisons.
4. Exactly 44 frozen mod-10 cells and all 72 primitive affine directions.
5. Optimal-center multiplicities and all 136 signed shifts, including the zero count at displacement 5.

The attached captured executable output reports ALL PASS. Theorem 1 has the human proof above; Theorem 3 is an exhaustive finite mathematical certificate with supplied generator, not extrapolation from a sample.

## Source and worldview boundary

P000 and the ACTIVE Heartbeat World six-native-spatial-dimensions plus independent time axioms remain unchanged. The ten-residue and rational-anchor expressions are auxiliary algebraic observation coordinates, not a native two-dimensional plane or complete three-dimensional slice. The frozen BRC16943 bridge and its inherited proof obligations are unchanged. No new claim about native X6 dynamics, Bernoulli probabilities, or a global Farey-gap upper bound follows.

## Next question

Seek a non-enumerative explanation of the 136 signed correction centers and the absent antipodal displacement. Investigate whether those signed one-pair corrections supply a useful information-preserving representation for moving Farey anchors. The global gap conjecture lim_{H→∞} H G_max(H)=1 remains open.

Publication: portable author proof and reproducible exact calculation; independent mathematical review and native formal Task/Result linkage remain pending. Shared owners/CLAIMs and previous Activity events are unchanged.
