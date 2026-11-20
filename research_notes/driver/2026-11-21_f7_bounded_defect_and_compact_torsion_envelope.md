# F7 continuation: bounded-defect torsion envelopes and compact-fiber positivity

Date: 2026-11-21 (Asia/Shanghai). Logical contribution: original RESEARCH_DRIVER line `EM-DVR-DEBB5E`, SID `MCP-9b4714dc46b948afa4875a86c89c713c`. This is an author-side new scoped mathematical lemma and extension, not an independent Native Review or Result admission. Preserve the F7 original theorem-repair authorship `EM-CBRCF7-83A1D4`.

## Exact prior sources and question

Prior Driver theorem: `research_notes/driver/2026-11-21_f7_torsion_envelope_transfer_and_infimum_boundary.md` at `2d7998407bcd27efdc225907406393544d714625`, blob `041198977a6364ea70834d039e84c737bffbfd9a`. It proved exact descent of separable conservation across any torsion group, and required fiber-uniform old-coordinate positivity for infinite torsion.

Original F7 revised theorem: `research_returns/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_20260903.md`, original author commit `c9bf0811f8cc17af1fa116af75911ed70b1f26b9`, Git blob `69265a0fadfd9fcd0be9354ff74f33e5e825fe84`. Frozen Result `RR-AA38973D56330E59D315`, verified record SHA256 `2a89647a31de47e4ddef17ae61a843ea9a271fe602f8ab60adcca81699022c9b`.

This unit asks (i) whether bounded rather than exact conservation defects amplify when passing to the torsion-fiber envelope, and (ii) when the positivity hypothesis required for the F7 free obstruction follows automatically for an infinite torsion group.

## Theorem A: an infimum-envelope contraction with optimal constant one

Let `L=Z^d`, `K` any torsion abelian group, `C=L⊕K`, and `s>=1` finite. Let `Phi∈Aut(C^s)` be an additive automorphism. Its induced quotient automorphism is `A∈GL_{ds}(Z)`. For any finite-valued nonnegative `q:C→[0,∞)`, set
```
Q(z_1,...,z_s)=sum_i q(z_i);
f(x)=inf_{k∈K} q(x,k);
F(x_1,...,x_s)=sum_i f(x_i).
```
If for some `epsilon>=0`
```
|Q(Phi(z))-Q(z)| <= epsilon       for every z∈C^s,              (A1)
```
then
```
|F(Ax)-F(x)| <= epsilon           for every x∈L^s.              (A2)
```
Thus the exact-defect case `epsilon=0` recovers the prior transfer theorem. There is no multiplicative loss from the number of slots, torsion-cardinality or torsion exponent.

**Proof.** The torsion subgroup of `C^s` is `K^s`, characteristic under every automorphism. Hence for a fixed free vector `x`, `Phi` maps the entire input fiber `{x}×K^s` bijectively onto `{Ax}×K^s`. Bound (A1) holds at every point on this fiber, so its infima satisfy
```
|inf_{k∈K^s} Q(Phi(x,k)) - inf_{k∈K^s} Q(x,k)| <= epsilon.
```
The bijection identifies the first infimum with `F(Ax)`. For the second, independent minimization across finitely many slots gives `inf_{k∈K^s}sum_i q(x_i,k_i)=sum_i inf_{k_i∈K}q(x_i,k_i)=F(x)`: choose each coordinate within `eta/s` of its infimum and let `eta→0`. This proves (A2), with no continuity or attainment hypothesis. QED.

**Sharpness.** For `K={0}`, `s=1`, `L=Z^2`, take `Phi(n,m)=(m,n)` and `q(n,m)=epsilon·1_{n!=0}` with `epsilon>0`. Then the maximal defect is exactly `epsilon`, attained at `(n,m)=(1,0)`, and the quotient defect is also `epsilon`. Evenness under `n↦-n` and `q(0)=0` hold. Thus no universal factor smaller than one is possible.

## Theorem B: infinite compact torsion fibers can retain strict positivity

Let `K` additionally be a **compact Hausdorff topological torsion abelian group** (possibly infinite). Take `L=Z^2` with `x=(n,m)`. Suppose for each `x`, the function `k↦q(x,k)` is lower semicontinuous on `K`; `q((n,m),k)>0` for every `n!=0` and every `m,k`; and `q((0,0),0)=0`.

Then `f(0,0)=0`, and `f(n,m)>0` for every `n!=0`. In particular, if `q` is invariant under a fiber-bijective old-coordinate involution covering `J(n,m)=(-n,m)`, then `f(-n,m)=f(n,m)`.

**Proof.** A finite-valued lower-semicontinuous function on a compact space attains its infimum. At every fiber with `n!=0`, every value is strictly positive; the attained minimum is therefore strictly positive. Nonnegativity and `q((0,0),0)=0` give `f(0,0)=0`. The involution assertion follows from the induced bijection of the two fibers and equality of `q` on paired points. QED.

**Conditional F7 consequence.** Under exact conservation `epsilon=0`, the stated involution, A0 on the free quotient (`Pe` and `Re` both have nonzero old-coordinate projections for `e=(1,0)`), and the original *free* A0/J-aware no-go proposition, a compact Hausdorff torsion summand with fiberwise l.s.c. `q` is excluded exactly as a finite torsion summand is. This expands the earlier conditional reduction to infinite compact torsion groups. It does not itself independently establish the original free no-go theorem. For `epsilon>0` the conclusion is the quantitative inherited defect (A2), not a no-go without an additional quantitative free obstruction.

## Witness: compactness without lower semicontinuity is insufficient

Let `K=prod_{j>=1}(Z/2Z)` with its product topology, an infinite compact Hausdorff torsion group of exponent two. Let `k_j` be the coordinate unit vector, so `k_j→0`. Define `h:K→(0,1]` by `h(k_j)=1/(j+1)` and `h(k)=1` at every other point (including zero). Set
```
q((n,m),k)=0               if n=0,
            h(k)            if n!=0.
```
The original pointwise old-coordinate positivity, nonnegativity, `q(0)=0`, and `J`-evenness all hold. Nevertheless `inf_{k}q((n,m),k)=0` for every `n!=0`. Here `h` is not lower semicontinuous at zero, precisely because `h(0)=1>liminf_j h(k_j)=0`. Thus infinite torsion **plus compactness alone** does not justify transferring strict positivity. This is a witness about the *envelope premise*, not a counterexample satisfying F7's A0 and conservation simultaneously.

## Audit, information scope and next question

- Exact theorem proof uses characteristic torsion fibers and infimum inequalities; no numerical test or external axioms.
- The envelope forgets torsion labels only for the declared *quotient observable* `F` and the displayed conservation defect; original branch/torsion provenance is retained in `q` and the original frozen sources. No observer-safe equivalence for arbitrary future torsion-sensitive operations is asserted.
- The ordinary F7 carrier `Z^2⊕Z/3` remains the original scientific input. Compact infinite torsion is a **clearly marked extension**, not a replacement of the frozen F7 Task.
- Native Driver first-review original `dvr-20261121-0214-f7-first-review-source-integrity-request-revision-v1` remains terminal `FAILED/NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED` (Issue #2874). Independently, original frozen Result has two misdeclared manifest SHA256 entries; preserve both facts without rewriting frozen artifacts.
- Next independent mathematical question: obtain a *quantitative free A0/J obstruction* under a precisely normalized nonzero conservation defect, or construct small-defect families showing that an unrestricted positive stability gap cannot be inferred. Only the bounded defect descent is proved here.

**Unit status:** New exact mathematical subunit A + compact-fiber corollary B + sharp boundary witness. Formal Native Review=0, Native Result accepted=0, Task DONE=0, parent Objective closure=0.
