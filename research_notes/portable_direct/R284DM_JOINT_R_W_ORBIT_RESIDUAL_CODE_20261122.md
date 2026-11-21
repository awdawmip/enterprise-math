# R284DM — 冻结 Port 观察器的 r/w 联合四轨道保真码及两位直接更新

Date: 2026-11-22 (Asia/Shanghai)
Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**
Scope: frozen 34-bit Port auxiliary finite observer; independently developed portable TASK research. No native X6/BRC dynamics or formal Task/CLAIM/Result/Review is inferred.

## 1. Frozen scientific source

The immutable input is awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py (Git blob b46e0f682b58e47c27094b4bea6fa4e55119a3ee). Source states are the 65,536 lexicographically indexed upper-four/lower-twelve binary matrices; the pinned determinant gives residues modulo P=17,179,869,143, with ordered residue SHA-256 b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4. There are 64 original labeled circular integer arcs. Define f(i) as the maximum exact integer distance from the source residue g(i) to those arcs.

Let R(i)=i xor 1 flip the lower r variable; W(i)=i xor 64 flip the lower w variable. These commuting fixed-point-free involutions generate G={0,1,64,65} under XOR. Earlier R284DI/R284DK established that each two-read observer (f(i),f(Ri)) or (f(i),f(Wi)) separates all source states, and R284DL constructed a W-only one-bit orientation update.

Research question: one state-fidelitous observer jointly updateable under both R and W, with exact composition and no 65,536-state inverse lookup during updates.

## 2. Theorem A: four-orbit invariant and two-bit residual

For u in G let F_i(u)=f(i xor u). Define the **orbit key**

\[
H(i)=\operatorname{sort}\bigl(F_i(0),F_i(1),F_i(64),F_i(65)\bigr).
\]

**Exact finite classification on this pinned universe.** The G action has 16,384 four-state orbits. Every orbit has four **pairwise distinct** f-values. Their sorted four-read keys H are pairwise different across all 16,384 orbits.

Since the four values are distinct, let m(i) be the unique u in G at which F_i(u) is minimal. Then

\[
\boxed{C(i)=(H(i),m(i))\text{ is injective over all }65,536\text{ states}.}
\]

For every t in G,

\[
\boxed{H(i\mathbin{\mathrm{xor}}t)=H(i),\qquad m(i\mathbin{\mathrm{xor}}t)=m(i)\mathbin{\mathrm{xor}}t.}
\]

Thus R and W respectively toggle bits 0 and 6 of the two-bit orientation m. Both updates square to identity, commute exactly, and require no new determinant or arc distance. Conditional on fixing the complete orbit invariant H, two bits of varying orientation are **necessary and sufficient** because each H fiber has exactly four distinct source states.

**Proof.** The group identity F_(i xor t)(u)=F_i(u xor t) proves H invariance and the XOR rule for the unique minimizer. If two states have the same H, the verified finite lemma that 16,384 H keys separate 16,384 G-orbits implies they are of form j=i xor t. Equal m values then force t=0 and i=j. The fiber cardinality four gives the sharp orientation lower bound log2(4)=2. The complete finite lemma is proved by exhaustive exact integer enumeration, with algorithm and digest below. QED.

## 3. Theorem B: directly readable, four-register observer

Maintain the **ordered** four-register code U(i)=(F_i(0),F_i(1),F_i(64),F_i(65)). The source updates are pure register permutations:

\[
U(Ri)=(U_1,U_0,U_3,U_2),\qquad
U(Wi)=(U_2,U_3,U_0,U_1).
\]

Current f(i) is always U_0, and both permutations satisfy the group laws. U is injective because its (U_0,U_2) subpair is the earlier injective W-two-read observer. Initial preparation costs four f observations; every subsequent R/W word is updated by register permutations without source inversion.

**Restricted four-register optimality.** In the architecture whose only stored registers are a nonempty subset of the literal translates F_i(u), u in G, and in which both updates must be achieved solely by permutation of already stored registers (no synthesis, inversion or hidden-state access), the offset subset must be invariant under XOR by both 1 and 64. Their action on G is transitive, so the only nonempty closed subset is G itself. Hence **four translated registers are minimal in this exact permutation-only architecture**. This is not an unrestricted minimum number of observations: an injective two-read code already exists, but its second generator's direct update needs further computation.

## 4. Finite certificate and reproducibility

Published scientific files:
- R284DM_joint_orbit_code_checker.py: standalone Python standard-library exact checker, faithfully reproducing the frozen determinant/arc construction and verifying the frozen 65,536-word digest.
- R284DM_joint_orbit_code_certificate.json: exact finite results and canonical-key digest.

The checker performs 65,536 x 64 = 4,194,304 exact integer point-arc evaluations, confirms both earlier two-read injectivity results, exhaustively enumerates all 16,384 joint orbits, checks all four f-values distinct within every orbit, all H keys globally unique, and all 65,536 distinct (H,m) states with both generator updates. No floating-point arithmetic or sampling enters the exhaustive claims.

| Metric | Exact result |
|---|---:|
| Source states | 65,536 |
| Joint R/W orbits | 16,384 |
| Joint orbits with four distinct f-values | 16,384 |
| Distinct H keys | 16,384 |
| Distinct (H,m) codes | 65,536 |
| Offset m for orbit representative: 0 / 1 / 64 / 65 | 3,674 / 3,882 / 4,826 / 4,002 |
| Same / opposite W-pair ordering across the R flip | 13,225 / 3,159 orbits |

SHA-256 of the 16,384 sorted H records, iterated over representative base states i&65=0 in ascending order, serializing each four-component key as four 8-byte big-endian integers:

fcc398115115d8f91a5aec28b00a0952decc597c2cbbc9bc43149b6889c6aaae

A concrete reproducible witness: at source base i=0 the four ordered readings are (8360532145, 8419222558, 8366177878, 8407120005), hence m(0)=0, m(R0)=1, m(W0)=64. This theorem and calculation are author-controlled; independent mathematical review is NOT_REVIEWED.

## 5. Recovery, cost and limits

The sorted representation (H,m) preserves exact state identity and admits two-bit updates, but it need not expose the current f(i) from the *unordered* four-number key without additional readout logic. Use ordered U for constant-time f readout. Full preprocessing, precision, initial four observations and state recovery remain separate costs.

A table-free (65,536-entry inverse table not required) constructive inverse for C can be obtained by enumerating at most 12 ordered distinct pairs from H, invoking the existing valid W-two-read source decoder of R284DK on each pair, then retaining the candidate whose recomputed (H,m) agrees. The genuine pair occurs among the 12; all other candidates are ruled out by C injectivity. This inversion construction relies on the prior decoder's proved scope; **it has not been run end-to-end in this round**, and its cost may exceed direct four-register use.

The observed preservation law covers only the monoid of legal source flips generated by R and W and the associated Port f readouts. The finite Port auxiliary circle/determinant is not asserted to be the native X6 three-dimensional slice or a native BRC physical rotation.

## 6. Next question and control provenance

Use the pinned modular increment and 65-segment event envelope to seek a shorter initialization from the already sufficient W two-read code to the joint four-read permutation code. Compare preparation, bit precision, subsequent update count and readout/recovery cost against R284DG/R284DK. Compute the sharp joint four-read quantization/noise separation, distinguishing the raw four-register code from an unordered H code.

Provenance: independent TASK portable contribution following R284DL; historical EM-DIRECT-20B766 is earlier authorship, not a credential for this run. No new native Researcher/CLAIM/Result/Review has been asserted. Current-owner snapshot request r1-20261122-0100-owner-check-v1 failed with SOURCE_TREE_TRUNCATED; no shared task was claimed. Portable Activity linkage remains to be associated by the genuine authorized session and Source CAS.
