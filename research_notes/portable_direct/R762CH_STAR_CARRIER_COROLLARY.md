# R762CH-S — K4 four-STAR readout: exact 12+3 pair-area split

**Parent:** R762CH pair-area carrier, same Draft PR #2575. **Frozen input:** X6 Cell torsor and established FCC/K4 four STAR carrier subatlas at P000 `a72226e2430ffa4786321ac86e7f0c599d5f0389`. This is an exact *combinatorial diagnostic observer* theorem, not a claim about an independently licensed Port-change event. Independent review: NOT_REVIEWED.

## Frame chart and theorem

Identify the six X6 axis **labels for this K4 chart** with the six edges of a tetrahedral K4:
`01,02,03,12,13,23`. The four STAR triple selections (one per vertex) are
`S0={01,02,03}`,
`S1={01,12,13}`,
`S2={02,12,23}`,
`S3={03,13,23}`.

For each selected STAR, allow the diagnostic readout of its three cyclic pair-area residues, with the signed orientation convention of R762CH. The **union** of pair probes over all four STAR triples consists exactly of the **12 unordered pairs of K4 edges that share a vertex**. The three unobserved pair coordinates are precisely the opposite-edge pairs
`(01,23)`, `(02,13)`, `(03,12)`.
This 12+3 partition is invariant under the full K4 vertex permutation group S4. Any choice of signs or cyclic roots on a STAR only changes order/sign of three of these same 12 components.

For integer q>=2, restrict to the R762CH common coarse fibre built from q labeled B/L square slots for each of the 15 edge-pairs, giving 2^(15q) positive N-BRC source histories and the *same* final full X6 Cell, elapsed time and 12-direction signed-step histogram. Let O_STAR read the four STAR triples' pair-area residues modulo q. Then:

1. Its exact observer quotient has **q^12** classes; unrestricted fixed-length class encoding requires `ceil(log2(q^12))` bits.
2. Every observed STAR class has **q^3** distinct full all-pair provenance phases, carried by the three disjoint-edge residues. If later pair probes can access all three, the minimum *conditional repair* after STAR observation is `ceil(log2(q^3))` bits.
3. The mass in any STAR residue class `a` equals
`2^(3q) product_(e in E_STAR) f_q(a_e)`,
where `f_q(0)=2` and `f_q(t)=binom(q,t)` for `1<=t<q`. The dormant three residues have their own product weights before aggregation; no mass is lost.
4. For q=3, the STAR observation has `3^12=531441` classes requiring **20 bits**, versus `3^15=14348907` classes requiring **24 bits** in a *jointly optimal* full encoding. After the STAR code has already been fixed, separately repairing its 27-element hidden fibre needs **5 bits**. The 4-bit difference between optimal independent-from-scratch code lengths is *not* the conditional repair cost.

## Proof

A pair of distinct K4 edges either shares exactly one vertex or is disjoint. Exactly `4*binom(3,2)=12` pairs share a vertex, and each is counted once because two distinct graph edges cannot share two vertices. Of the `binom(6,2)=15` total pairs, the remaining 3 are the displayed perfect-matching opposite-edge pairs. Vertex permutations preserve incidence and the partition. By R762CH Theorem 3, independent pair-area squares realize all q^15 phase tuples on a common coarse fibre; projecting to the 12 incident-edge coordinates gives q^12 classes and leaves q^3 dormant phases per observed class. R762CH's single-coordinate phase probes separate every permitted visible phase, and all-pair probes separate all dormant phases when they are added to the interface. The BRC coefficient product from R762CH Theorem 4 gives the displayed mass by summing the three dormant factors, each of whose total is 2^q. The q=3 bit calculations are exact integer ceilings. QED.

## Verification and decision boundary

`R762CH_STAR_VERIFY.py` exhausts all 24 S4 label permutations, computes the four stars, 12 visible / 3 dormant edge-pairs, and checks the exact q=2..10 count/mass identities. `R762CH_STAR_EVIDENCE.json` contains the finite results. General validity rests on the combinatorial proof and parent R762CH.

The Source X6 definition establishes *four STAR coordinate/carrier-readout selections* within the FCC/K4 atlas. It does not, by that fact alone, authorize arbitrary signed pair-area event queries. This corollary supplies a crisp next discriminator for `TRIADIC_CLOSURE_E` / V17/V29/V39: identify whether legal triadic updates can reveal any opposite-edge residue. If none are legally observable in the declared future scope, the 12-pair STAR quotient is safe for that scope; if a licensed suffix reveals even one of the three hidden coordinates, retain its BRC source class.
