# BRC N=4 / S23 / stopping-time-only: ten labels lift from 64 signatures to ALL 2048 deterministic policies

Date: 2026-10-31. Author-side analytic proof plus independently executable exact integer exhaustive check. **UNREVIEWED / NOT_ADMITTED**. All results concern the frozen positive-mass finite external model, not native P000 X6 dynamics.

## Input and quantifiers

Frozen source: six latent cells (AU0, AU1, AV, BU0, BU1, BV), six prepared rows
\[
M=\tfrac1{20}\begin{pmatrix}
10&10&0&0&0&0\\
9&11&0&0&0&0\\
0&0&20&0&0&0\\
0&0&0&10&10&0\\
0&0&0&2&18&0\\
0&0&0&0&0&20
\end{pmatrix}.
\]
Full deterministic S23 stopping policies: two first-stage bits (A/B), three second-stage bits (AU=BU / AV / BV), and six third-stage cell bits, giving 4·8·64=2048 legal tables. Observation T takes values 1,2,3,4 only. A common stochastic encoder with k outputs is selected before policy H; at most m policy labels can be communicated prior to realized source/outcome; the decoder depends only on label and encoded state. Let R^{det}_{k,m}(T) denote the maximum-six-input TV minimax restricted to these **2048 deterministic S23 policies**. This is NOT the minimax over behavioral-randomized S23 policies.

## Theorem (new scope closure)

For EVERY integer k>=4 and 10<=m<=63:
\[
\boxed{R^{\rm S23,det}_{k,m}(T)=1/2.}
\]
The ten-label upper bound applies to the complete deterministic grammar, not just the 64 point-mass subclass. The result is exactly finite, with no numerical approximation and no dependence on BU sensor noise.

### General half-majority lifting lemma

Suppose a finite latent-source experiment partitions its cells into provenance groups j, each prepared row lives in one group, and each group has a designated latent cell c_j whose conditional mass in **every** row of that group is at least 1/2. Suppose each deterministic admissible policy H has a designated-cell time signature h(H) which belongs to a set S covered by m coordinate-wise two-element time boxes B_l. Then a common encoder retaining only the provenance group, and for label l a decoder uniform on its pair B_{l,j}, produce worst total-variation error at most 1/2 on **all deterministic H**.

Proof: select box B_l containing h(H), permissible because its label is chosen from the policy before execution. Each input row i in group j assigns at least 1/2 probability to its designated cell's stopping time h_j. The reconstructed row from that group is uniform on B_{l,j}, hence assigns exactly 1/2 to h_j. Therefore the overlap coefficient \(\sum_t \min(p_i(t),q_{l,i}(t))\) is >=1/2, and TV=1-overlap <=1/2. This uses positive probabilities and preserved provenance; it does not extend to signed/phase amplitudes.

### Applying the lemma to S23

Use four provenance groups AU, AV, BU, BV and choose designated cells AU1, AV, BU1, BV respectively. The corresponding row weights are:
- AU Q: AU1=10/20, AU P: AU1=11/20;
- AV: AV=20/20;
- BU Q: BU1=10/20, BU P: BU1=18/20;
- BV: BV=20/20.

All meet the 1/2 hypothesis. A four-state deterministic encoder records AU/AV/BU/BV. For policy H, write \(h(H)=(T_{AU1},T_{AV},T_{BU1},T_{BV})\). This signature lies in the previously established 64-point set S64: retain H's two first-stage and three second-stage decisions, and assign the AU0 third-stage choice to equal AU1's choice, and BU0's choice to equal BU1's. Earlier stop decisions are shared within each of AU and BU, so this operation is a legal S23 table and its resulting four group times equal h(H). Crucially the third-stage six bits are independent in S23; no illicit earlier latent observation has been introduced.

The *same* explicitly certified ten boxes from the predecessor 64-signature set-cover are:
\`\`\`text
AU AV BU BV (two choices in each coordinate)
34 24 34 24
34 23 34 34
34 34 34 23
24 24 12 12
12 12 24 34
12 13 23 24
23 34 12 13
24 34 12 14
13 12 13 13
12 12 14 12
\`\`\`
Here 34={3,4}. For each deterministic policy select a box covering h(H), and decode group j uniformly over its two time choices. The lemma gives TV<=1/2 for all six prepared inputs, for all 2048 policies, with one common four-state encoder and ten fixed label kernels. States k>4 and labels m>10 can duplicate unused states/labels.

### Lower bound for 10<=m<=63

The prior S64 proof constructed 64 genuinely legal S23 deterministic policies with four distinct source-group point-mass stopping-time signatures. Under an arbitrary stochastic encoder and any fixed label decoder, if maximal error were strictly less than 1/2, each of four chosen prepared rows would require reconstructed probability >1/2 at its signature's stopping time. A probability distribution cannot have two distinct atoms each of mass >1/2. Thus a label can serve at most one of the 64 signatures, requiring at least 64 labels. In particular, m<=63 forces risk >=1/2 for **any k**, even a randomized encoder. The explicit four-state construction achieves 1/2. This closes the equality in the stated scope.

## Why randomization is still open (new exact counter-witness against this fixed construction)

Take H0 with first-stage A-continue/B-stop, second-stage AU/AV-continue, and third-stage AU0/AV-stop-at-3, AU1-continue-to-4: latent stop vector \((3,4,3,1,1,1)\). Take H1 that stops everything at time 1. A lawful policy can implement \(H_{\rm mix}=(2/3)H0+(1/3)H1\) by flipping a Bernoulli 2/3 continuation coin at the A first-stage decision; B always stops at 1; after continuing, stage-two and stage-three actions are H0's. This introduces **no need for a correlated hidden coin across later information sets**.

For this mixed behavioral policy, when tested against the **particular ten frozen uniform-pair kernels above**, the ten exact maximum-six-row TV risks, with common denominator 240, are
\[
(240,240,240,240,240,240,168,160,160,160)/240.
\]
The best label therefore incurs \(\boxed{2/3}\), not 1/2. This is a counterexample to naively extending the *specific 10-box uniform-pair construction* from deterministic to all randomized policies; it is NOT a lower bound on arbitrary alternative 10-label encoders/decoders. Convexifying policies after selecting a policy-dependent label changes the quantifier structure: a union of convex decoder-error balls need not be convex.

Consequently, for the full behaviorally randomized S23 class at 10<=m<=63, currently the rigorously justified bound is **1/2 <= R^{S23,beh}_{k,m}(T) <= 2/3** when k>=4 (upper by the previously proved four-label heavy-time construction). Exact behavioral R_{k,10} is not established here.

## Executed validation and scope

The saved VERIFY.js uses integer M counts with exact denominators 20,40,80,120,240, enumerates exactly 4*8*64=2048 deterministic policies, checks all six prepared rows and all ten labels (2048*10*6 exact TV evaluations), independently confirms 64 legal point-mass signatures and all 64 heavy signatures covered, and checks the two-policy lawful behavioral witness against all ten labels. No floating-point comparisons, optimizer tolerance or random sampling are used. The explicit program output is in RUN_EVIDENCE.txt. Analytic majority lifting establishes the universal upper for the finite deterministic grammar; the exact loops provide a separate complete finite check.

P000 remains an internal project axiom (X6 spatial Cell plus separately typed time). This finite positive BRC observer model has no established native six-axis Cell/time fidelity bridge, no proof for signed/complex BRC, and no lawful S2 transfer claim. Independent mathematical review is pending.
