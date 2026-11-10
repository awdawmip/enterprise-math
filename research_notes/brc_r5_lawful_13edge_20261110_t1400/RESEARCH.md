# R5: an exact lawful 13-edge Blackwell transfer, with a sharp lower-support certificate

Date: 2026-11-10, Asia/Shanghai. Status: **author-side mathematically explicit rational counterexample / exact verified construction**, pending independent mathematical review and formal Result acceptance. Parent scientific context and frozen inputs unchanged: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Immediate parents: Draft PR #1954 at `6f01b6424cc5563db7976fa8131ef687c15091ca`, and 4-dimensional transfer-face Draft PR #1958 at `6b3a582d4cfbc85494ac3d7c3693958a8acf5900`; underlying capacity and Blackwell model is retained from PR #1950. The ten exact forced-arc duals are from PR #1939.

## Theorem: the legal physical model realizes a minimum of 13 positive transfer arcs

In the frozen seven-likelihood-ratio P/Q–BRC Blackwell model with 30 allowed arcs `D` and the full 21-row condition matrix `C_full`, there exists an explicitly rational lawful pair of physical policies satisfying the original (g=b), seedless-F, two stopping-time equalities and all 26 capacity nonnegativity constraints, for which the exact minimum positive-mass Blackwell transfer support is **13**, i.e.

[
\boxed{\min_{E\ge0,\;C_{\rm full}E=b_{\rm full}(p)} |\operatorname{supp}(E)|=13.}
]

No new physical model, observer restriction or change in admissible transfer arcs is used.

### Explicit construction

Use the predecessor's immutable family `p(z)=p+P*(tstar+z)` and the interior fourteen-arc contact

[
R=\frac{49948501046391}{3920403670319950000},
\qquad z_c=R(-1,1,1,-1,-1,-1,-1,1).
]

At that contact the target component `mu_1` is strictly positive:

[
u=\mu_1(z_c)=\frac{16932541854726549}{313632293625596000000}>0.
]

Take the **new** exact perturbation

[
h=\left(0,\frac{937899}{293725}u,0,0,u,0,0,0\right),
\qquad z_{13}=z_c+h.
]

Let the previous interior 14-arc wall's primitive integral normal be

[
n=(34101,-293725,-85599,42525,937899,293725,85599,-3287440).
]

Direct rational multiplication gives `n·h=0`, so the new point lies on the exact 14-arc support wall. In addition, `mu_1(z_13)=mu_1(z_c)-u=0`: on that wall the old common arc `(1,5)` shrinks exactly to zero, leaving the following **thirteen** strictly positive arcs:

```text
((0,0),(0,1),(0,2),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6),
 (2,1),(3,2),(0,3))
```

The exact coefficient vector is provided by the rational linear solve in `VERIFY_13.py`, and all thirteen explicit rational masses are printed in `EXACT_OUTPUT.txt`. The smallest is

[
\min_{E_e>0}E_e
 =\frac{131977087948072769}{313632293625596000000}>0.
]

The original five physical affine equalities hold exactly, all 26 original capacity slacks are nonnegative, and the smallest strictly positive physical slack is

[
\frac{3836062555208901}{156816146812798000000}.
]

All 21 original Blackwell equations are satisfied. Hence the minimum support is at most 13.

### Proof that 12 arcs or fewer are impossible

Let `F` be the ten previously proved mandatory transfer arcs:

```text
F=((0,0),(0,1),(0,2),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6)).
```

For each `e in F`, the source PR #1939 supplied a rational 21-coordinate linear functional `y_e` satisfying, for **every** allowed arc `f in D`,

[
y_e^T C_{\rm full}[:,f] \le \mathbf 1_{f=e}.
]

The new `VERIFY_13.py` includes these ten exact sparse vectors and checks all 300 inequalities for the frozen 30-arc model. At `z_13`, the ten exact margins

[
\beta_e=y_e^T b_{\rm full}(p(z_{13}))
]

are all strictly positive; their values are recorded in the executable's output. Consequently, for **every** legal transfer `E`,

[
0<\beta_e
 =\sum_{f\in D} y_e^T C_f E_f \le E_e;
]

all ten arcs `F` must appear.

The ten chosen reduced columns of the exact rank-15 transport system have rank 10. Choose a five-row left annihilator `L`; project the remaining 20 columns into five-dimensional quotient vectors `V=L*C_other`, and let `q=L*b_reduced(z_13)`. Any realization using at most twelve total arcs would require `q` to lie in a span of at most two of those 20 quotient columns. The program examines **all**

[
\binom{20}{2}=190
]

pair subsets and verifies with **exact rational matrix rank**, for every pair `S`,

[
\operatorname{rank}[V_S\mid q]>
\operatorname{rank}(V_S).
]

This exhausts every support with at most two non-forced arcs (a single arc is contained in at least one such pair), proving that no twelve-or-fewer-arc transfer is possible. Together with the explicit thirteen-positive-arc solution, the exact minimum is 13.

### Mathematical interpretation and scope

This is the first **exact lawful 13-positive-arc instance in this local continuation**. It connects the preceding 14-edge interior wall to a genuine additional support-deletion boundary where the physical target component `mu_1` reaches zero. The 4D first-contact transport face of PR #1958 supplies the branch family; the final certificate retains the full branch identities and 21-row observer, so it does not mistake a coarse scalar support count for a physical law.

The theorem is **existential and exactly model-scoped**: it establishes the minimum at the stated rational point, not a universal thirteen-arc implementation for every legal physical strategy pair, nor an entire thirteen-edge stratum. Its source proof remains author-side, and the shared R5 runtime does not have a current immutable `R5` publication (native query returned `NO_CURRENT_IMMUTABLE_PUBLICATION`); this research has not taken another task's CLAIM.

### Validation provenance

An independent local SymPy-rational transcription was actually executed: the exact complete output, including the ten positive dual margins, thirteen arc masses and 190 exhaustive rank exclusions, is retained as `EXACT_OUTPUT.txt`. The repository `VERIFY_13.py` is a separately composed reproducible wrapper that consumes the pinned parent `VERIFY_SHEET.py` model and then checks the same rational predicates and ten dual witnesses. Do not present the independent transcription output as byte-for-byte stdout of this wrapper until the wrapper itself is executed. All finite logical implications used in the proof are explicitly stated.

## Next smallest scientific unit

Classify the local `mu_1=0` contact where the thirteen-arc solution persists, measure its dimension within the real physical feasibility region, and determine the neighboring positive/negative perturbation chambers under actual capacity constraints. In parallel, extract the five-dimensional quotient rank exclusion as a reusable BRC support/minimum algorithm, with full input transformation/bit-complexity accounted for before performance claims. Priority to independently re-execute `VERIFY_13.py` and review the dual certificate source and all 190 rank checks before formal result admission.
