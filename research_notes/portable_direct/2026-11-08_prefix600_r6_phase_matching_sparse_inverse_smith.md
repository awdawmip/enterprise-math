# PREFIX-600-R6 — Native 48-phase matching, sparse inverse, and full-seven observation rank

Date: 2026-11-08 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_NATIVE_STRUCTURE_CHECKED_ON_SOURCE-FAITHFUL_TRANSCRIPTION / UNREVIEWED / NOT_ADMITTED.
Scientific input pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Research mode: direct TASK_RESEARCH, without a new formal CLAIM.
Original frozen input: `research_notes/portable_direct/PREFIX565_positive_marginal_certificate.py` (Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`).
Prior exact observation theorem: PREFIX-598 and PREFIX-599 (frozen model, nine allowed roots).
This note does not modify P000, scientific input pins, the native six-axis definition, or shared-task authority.

## Question and declared observer

PREFIX-599 proved by 18 rational row eliminations that the one-step native BRC observer retaining seven original reward components and the exact next original port has rank 49 (rank 50 when the original action label is retained) for each of nine roots. Find a **root-uniform native phase-graph proof**, and derive an explicit inverse and arithmetic structure of the 48-dimensional phase-background carrier.

An original port is `i=2p+b` with `0<=p<48`, `b∈{0,1}`. The six native actions are `(s,b')`, `s=0,1,2`, `b'=0,1`, with `NEXT[p][s]=q` and exact next port `2q+b'`. The original reward vector is `edge(i,(s,b'),r)[1]`. The phases, stars, signs, weights, roots and gate are **precisely** those of the pinned PREFIX-565 module. Phase matrices below are integer **action counts**, before dividing by six.

## Theorem 1 — permutation and 12 disjoint twin-pair swaps

Define `A∈Mat_48(Z)` and `S∈Mat_48(Z)` by
$$
A_{pq}=\#\{s\in\{0,1,2\}:\mathrm{NEXT}[p][s]=q\},\qquad
S_{pq}=\mathbf 1\{\mathrm{NEXT}[p][0]=q\}.
$$
Let `F` swap the two native phases with the same first two phase components `(a,p)` and different third signed component `c`. Set
$$
B=S^{\mathsf T}A-I.
$$
Then the following are **exact integer identities** in the frozen 48-phase model:
$$
S^{\mathsf T}S=SS^{\mathsf T}=I,\quad F^2=I,\quad
BF=FB=B,\quad B^2=2(I+F). \tag{1}
$$
The first-action permutation `S` consists of exactly eight disjoint 6-cycles, so `det S=+1`. The 24 `F`-twin pairs are carried by `B` to other twin pairs: each source phase has **one edge to each of the two phases in its target pair**, and both members of a source pair have the same target pair. The induced map `tau` on the 24 twin pairs is a fixed-point-free involution, hence **12 disjoint transpositions**.

A compact exact witness is the following list of `(source pair, target pair)` for these twelve transpositions; each pair lists original *phase indices* (not 96-port IDs):

```text
(0,9)<->(24,33)     (1,5)<->(37,41)
(2,11)<->(26,35)    (3,7)<->(39,43)
(4,8)<->(16,20)     (6,10)<->(18,22)
(12,21)<->(36,45)   (13,17)<->(25,29)
(14,23)<->(38,47)   (15,19)<->(27,31)
(28,32)<->(40,44)   (30,34)<->(42,46)
```

**Proof.** Enumerate the exactly 48 frozen `PHASES` and three `NEXT[p]` values per phase. Slot 0 visits each phase exactly once; its eight cycles have length 6. The phase construction has precisely two `c` values per fixed `(a,p)`. The other two slots, pulled back through `S^{T}`, connect each source twin pair to both phases in a single target twin pair, establishing `BF=FB=B`. Two such hops have exactly two paths to each member of the original twin pair, and no others, proving `B²=2(I+F)`. All these bounded integer equalities and the explicit twelve transpositions are independently checked by the accompanying certificate, which imports the original frozen native module. Since the resulting target-pair map squares to the identity and none of its targets is itself, it consists of 12 transpositions. QED.

## Theorem 2 — exact determinant, sparse inverse, and Smith form

Under a permutation of phase indices by the twelve paired orbits of Theorem 1, `B` is a direct sum of twelve identical 4-by-4 blocks
$$
H=\begin{pmatrix}
0&0&1&1\\
0&0&1&1\\
1&1&0&0\\
1&1&0&0
\end{pmatrix}.
$$
The eigenvalues of `H` are `2,-2,0,0`, so
$$
\boxed{\det A=\det S\prod_{j=1}^{12}\det(I_4+H)=(-3)^{12}=3^{12}=531441.}\tag{2}
$$
More constructively, (1) implies
$$
(I+B)(I+B-2F)=3I.
$$
and hence the **exact explicit inverse**
$$
\boxed{3A^{-1}=(I+B-2F)S^{\mathsf T}\in\mathrm{Mat}_{48}(\mathbb Z).}\tag{3}
$$
Each row of `3A^{-1}` has exactly **four** nonzero entries, one `-2` and three `+1`. Therefore an already-given 48-coordinate phase-background vector can be inverted using a constant-four-sparse rational readout (48 divisions by 3 and at most three additions per row, with no dense inversion). This is a claim about this specific finite phase-background step, not a blanket complexity speedup for full BRC input/output or full reward histories.

Since `3A^{-1}` is integral, every invariant factor of `A` divides 3; since `|det A|=3^{12}`, its exact integer Smith form is
$$
\boxed{\operatorname{SNF}(A)=\operatorname{diag}(1^{36},3^{12}).}\tag{4}
$$
In particular `rank_Q(A)=48`, `rank_F3(A)=36`, and `A` is invertible modulo every prime other than 3. QED.

## Theorem 3 — direct root-uniform 49/50 rank proof for the strong one-step BRC observer

Let `L_r` retain the full original **seven-component** BRC reward and exact next **96-port**, but forget the primitive action. Let `L_r^{act}` retain the action as well. Work on signed rational initial-port measures (stochastic probabilities are their nonnegative normalized subset). Consider the 48 even-port source rows `e_{2p}`. Project either one-step output to its next *phase* `q` only. Every projected row is `A[p,:]` divided by 3 (both new bits), so Theorem 2 proves these 48 input rows independent at every root.

Now let `d_p=e_{2p}-e_{2p+1}`. Away from native target predecessors `P={3,14,15}`, the gate never fires and `L_r(d_p)=L_r^{act}(d_p)=0`; the underlying six-axis edge rewards do not depend on the source bit. For the three predecessors, the only surviving term has destination exact port 9. All three have the same signed component `c=+1`, giving the same complete six-axis native reward for a fixed root. Hence `L_r(d_3)=L_r(d_{14})=L_r(d_{15})
e0`: a single new independent direction beyond the 48 background rows (it projects to zero under the next-phase marginal). With action retained, `d_3` survives only at action `(0,1)`, while `d_{14},d_{15}` survive only at `(1,1)`; these two nonzero disjoint-action contrasts are independent. Therefore for **each** of the nine frozen allowed roots,
$$
\boxed{\operatorname{rank}_{\mathbb Q}L_r=49,\quad
\operatorname{rank}_{\mathbb Q}L_r^{\mathrm{act}}=50.}\tag{5}
$$
Their kernel dimensions are `47` and `46`. The full bases are exactly those in PREFIX-599: all `d_p` outside `P`, plus `d_3-d_{14},d_{14}-d_{15}` when action hidden, or `d_{14}-d_{15}` when action retained. This proves the previous rank theorem by an explicit 48-phase integer identity and the gate-bit structure rather than an 18-matrix rational elimination.

**Observer scope.** The next original port and all seven reward coordinates are included. Dropping the next port, keeping history actions, changing the root family, or claiming a universal state quotient is not covered. Original X6 spatial, signed-axis, phase and provenance identities are preserved. The rational signed-kernel vectors are mathematical witnesses; no negative transition probability is introduced.

## Validation and remaining question

The companion Python script is a direct finite certificate importing the pinned frozen native `PHASES, NEXT, TARGET, ROOTS, ACTIONS, edge`: it checks the 48-phase permutation/twin identities, both products with the sparse inverse, 24-pair `tau` involution, its 12 swaps, and all nine-root gate-bit reward contrasts. **Local execution used a source-faithful transcription of the original frozen module and returned `ALL_CHECKS_PASS`; executing the published script against the GitHub original module in a second environment remains useful independent confirmation.** The analytic deductions (2)–(5) use exact finite identities, without numerical approximation.

Next independent questions: find a closed symbolic phase rule for the twelve transpositions `tau` that avoids even the 48-phase lookup; extend/compare the block decomposition when the native gate target and phase STAR carrier are varied; and quantify bit growth and full-observer reconstruction cost rather than inferring speedup from one sparse inverse.
