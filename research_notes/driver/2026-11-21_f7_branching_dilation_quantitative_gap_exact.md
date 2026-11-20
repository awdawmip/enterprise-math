# F7 quantitative continuation: a sharp branching lower bound for fixed old-axis separation

Date: 2026-11-21 (+08:00). Original RESEARCH_DRIVER logical line `EM-DVR-DEBB5E`. Mathematical contribution: exact Driver-side general lemma and its F7 free-axis specialization. Native Review, Result admission, Task completion and parent closure are **not** asserted.

## Source and question

The original F7 A2 ablation source belongs to `EM-CBRCF7-83A1D4`, preserved at `research_checks/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_CHECK_20260903.py` in owner commit `c9bf0811f8cc17af1fa116af75911ed70b1f26b9`. Its exact unimodular old-axis matrix is `B=[[2,3],[3,4]]`.

The Driver's new quantitative family, `research_notes/driver/2026-11-21_f7_quantitative_no_gap_from_exact_a2_ablation.md@aa6cd7341bc424672dd8d89798709910a6197e7b` (blob `b4684756cc2270a96a40ade5088d4246c463880e`), established exact marked balance with arbitrary small global defect `delta` while its uniform old-positive separation constant also decreases to `delta`. This raises the stronger **fixed-separation** question: Is there nevertheless a positive defect gap when the old free axis is split into two nonzero dilations and separation has a specified positive lower bound?

## Theorem 1 (sharp r-branching dilation gap)

Let `r>=2` be an integer, and let `a_1,...,a_r∈Z\{0}` be fixed nonzero integer multipliers. Let `H:Z→[0,∞)` be finite-valued, `H(0)=0`, with a fixed uniform separation
```
inf_{t∈Z\{0}} H(t) >= c > 0.                           (S)
```
Suppose for some `epsilon>=0`,
```
|sum_{i=1}^r H(a_i t)-H(t)| <= epsilon     for every t∈Z. (E)
```
Then necessarily
```
                      epsilon >= (r-1)c.                (G)
```
This constant is best possible for every list of nonzero integer multipliers, attained by `H(t)=c·1_{t!=0}`.

**Proof (works with noncommensurate multiplicative paths, with duplicates).** Fix `t_0!=0`. For a word `w=(i_1,...,i_j)∈{1,...,r}^j` put `a_w=a_{i_1}...a_{i_j}`, and define
```
S_j = sum_{w∈{1,...,r}^j} H(a_w t_0),    S_0=H(t_0).
```
Every term has a nonzero argument. By (S), `S_j>=r^j c`. The upper inequality from (E), applied at each `a_w t_0` and summed **with word multiplicity**, gives `S_{j+1}<=S_j+r^j epsilon`. Iterating,
```
r^j c <= S_j <= H(t_0)+epsilon·(r^j-1)/(r-1).
```
Divide by `r^j` and let `j→∞`: `c<=epsilon/(r-1)`, yielding (G). Duplicated products are purposely counted with their full word multiplicity, so integer commutativity and path collisions do not invalidate the argument. For `H(t)=c` at `t!=0`, the defect is exactly `(r-1)c` on every nonzero input, and zero at zero. QED.

## Corollary 2 (the original F7 A2 old-axis automorphism has a fixed-c gap)

Let `f:Z^2→[0,∞)` satisfy `f(0,0)=0` and **fixed** `f(t,0)>=c>0` for every `t!=0`. Let the original integer two-slot map be
```
A(n,m,p,l)=(2n+3p,m,3n+4p,l)∈GL_4(Z), det A=-1.
```
If its global additive-energy defect obeys
```
|f(2n+3p,m)+f(3n+4p,l)-f(n,m)-f(p,l)|<=epsilon
```
for every integer input, then `epsilon>=c`.

**Proof.** Specialize `m=l=p=0` and `n=t` to get
```
|f(2t,0)+f(3t,0)-f(t,0)|<=epsilon
```
for every integer `t`. Apply Theorem 1 with `r=2`, `H(t)=f(t,0)`, `a_1=2,a_2=3`. QED.

**Exact saturation with F7 marked balance.** For any `0<c<=1/2`, the previously verified family
```
f_c(n,m) = [1_{2∤n}+1_{3∤n}]/2 + c·1_{n∈6Z,n!=0}
```
has `inf_{n!=0,m}f_c(n,m)=c`, retains `f_c(1,0)=1` and `f_c(2,0)=f_c(3,0)=1/2`, and has global defect exactly `epsilon=c` for this same map `A`. The preceding source proved the exact modulo 2/3 and modulo 6 identities for all integers. Hence **the lower-bound constant one is attained even after imposing exact marked balance and J-evenness** in this fixed-matrix family.

## Scope, provenance and next precise question

- Theorem 1 applies to any nonzero integer multiplicative branching and has an exact universal proof, no finite enumeration.
- Corollary 2 applies to the original **specific** free-axis-splitting `A`, and any `f` with a fixed old-axis lower bound. It does not yet prove a uniform gap for an arbitrary A0-compatible `GL_4(Z)` map, whose elementary images need not remain collinear with the old input axis under iteration.
- This reconciles the earlier **no universal gap with shrinking `c`** with the **sharp fixed-`c` gap for this axis-preserving family**; neither reverses the original exact F7 no-go.
- A useful follow-up is whether an invariant finite directed cone of primitive old-input rays for a general A0 map can replace the single-axis multiplicative tree; a proof requires a certified cone/closure and quantitative positive separation on each reachable ray, not just A0 on the first column.
- Keep original Result `RR-AA38973D56330E59D315`, frozen manifest SHA256 mismatch and original Native first-Review error `NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED` (Issue #2874) as separate provenance/control issues. Do not replay the failed write.

**Layered status:** new mathematical proof subunit 1; Native Review accepted 0; Native Result accepted 0; formal Task DONE 0; parent Objective CLOSED 0.
