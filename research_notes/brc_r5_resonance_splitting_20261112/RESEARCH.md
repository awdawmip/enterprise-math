# R5 — exact splitting of the three one-coordinate resonances inside one Blackwell observer fiber

Date: 2026-11-12 (Asia/Shanghai). Status: **author-side exact finite proof and locally executed rational checker**. Subject: frozen, **external** P/Q–BRC Blackwell auxiliary transmission model; not native X6.

## Fixed scientific provenance and question

Preserve frozen scientific pins GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and EM `86149263e38c22292c9def1e0f69092efa1be77e`. Input objects (unchanged) are the strictly positive 28-mass rational state `X`, the 15 **labeled** elementary kernel moves `M_a`, and the ray direction `D=sum M_a` in immutable source `435e77af0d180eac32bd1f9c4c464bc4010b7551` (PR #2102). The immediately preceding result is `343ef84562909be87f520049893320d204fa9c4b` (PR #2108): all 1,144 interior *first-zero* phase values for that original state arise from target 0/source 3, while target 1/source 3 also first vanishes at three **coincident** resonance phases (ranks 607,715,1039). They correspond to the three-target resource increments `-12,-3,+15`.

This unit asks whether that one-coordinate completeness survives a **small observer-preserving change of the strictly positive initial state**, with all 15 labeled moves and the observer frozen.

## Exact perturbation and statement

Use target labels `i=0,...,6`, compensator source ports `j=1,2,5`, distinguished source `3`, and likelihood numerators `R=(2,10,15,20,25,30,38)`. Write `X_(i,j)` for the rational mass. Define a six-arc kernel move `H` by

- at source 3: `H_(1,3)=-23, H_(2,3)=+28, H_(6,3)=-5`;
- at source 1: the opposite changes `+23,-28,+5`;
- every other coordinate zero.

The mass and first-moment identities `-23+28-5=0` and `10(-23)+15(28)+38(-5)=0` prove `AH=0` for the complete frozen observer `A`.

Let
```text
x = X_(0,3) = X_(1,3) = 155682221/25142124560000000
eta = x/1000000 = 155682221/25142124560000000000000
X' = X + eta*H
epsilon_max = 9/115400000
```
The checker proves all 28 masses of `X'` strictly positive, `AX'=AX`, and `X'+epsilon_max D >= 0`. The old terminal-zero coordinate `(target=0,source=2)` is unchanged, so this is still the exact maximal nonnegative endpoint of the ray `X'+epsilon D`. Each of the 15 move vectors `M_a` and its labels remains frozen.

**Theorem (exact resonance split).** For this explicit rational `X'` and the same 15 labeled BRC moves, the set of distinct exact first-zero prefix thresholds on the closed maximal ray comprises **1,148** values: the original **1,144** interior target-0/source-3 thresholds, the unchanged endpoint, and exactly **three additional interior values**:

```text
t15 = 155678640308917/377131868400000000000000
t12 = 155678640308917/301705494720000000000000
t3  = 155678640308917/75426373680000000000000
```

All three new values are contributed by target 1/source 3, correspond respectively to signed prefix losses `-15,-12,-3`, and are **genuine decreases in the number of legal complete 15-atom permutations**. Thus the number of interior phase values rises from 1,144 to **1,147** under this observer-invisible initial-state change.

The unperturbed target-0/source-3 integer weights remain, in fixed labeled atom order:
```text
(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80).
```
Their subset-sum support continues to generate exactly 1,144 distinct interior target-0 thresholds. Consequently the previous single-coordinate **complete-spectrum equality** is a **resonant property of the particular initial-state fiber point**, rather than an invariant of the full observation fiber and labeled move list.

## Exact verification and complete coverage

The verifier reconstructs the original 28 rational entries and 15 moves from the immutable source, applies the displayed exact `H`, and proves all observer and endpoint invariants. It uses rational/integer arithmetic only. The key first-new-threshold witness is the prefix `S={(1,1),(2,1)}` (bitmask 33). At `t15`, its target 1/source 3 mass is exactly zero and **each of its other 27 masses strictly positive**. Before `t15` the following complete 15-atom schedule is legal; immediately after, this schedule is forbidden because the first two operations exhaust the target-1/source-3 capacity:
```text
(1,1),(2,1),(1,2),(1,3),(1,4),(1,5),
(2,2),(2,3),(2,4),(2,5),
(5,1),(5,2),(5,3),(5,4),(5,5).
```
Here the displayed schedule is verified at a rational point between the adjacent critical parameters; it does not claim legality on the whole ray.

For completeness, the checker enumerates **all 2^15 = 32,768 labeled prefix subsets**, finds every subset's first nonnegative-constraint zero using exact rational minima across all 28 coordinates, and collects the distinct thresholds `0<t<=epsilon_max`. The exhaustive list equals the union of the original 1D candidate set, the three listed split resonances and `epsilon_max`. It detects **no missing original target-0 phases** and no other new phase values.

For each new resonance, the checker counts complete legal permutations immediately before and immediately after by the exact Boolean-lattice recurrence `ways(S)=1_{X'+epsilon sum_{a in S}M_a >=0} * sum_{a in S} ways(S\\{a})` with `ways(empty)=1`:

| New phase | Immediately before | Immediately after | Lost orders |
|---|---:|---:|---:|
| `t15` | 851,207,682,192 | 471,427,082,208 | **379,780,599,984** |
| `t12` | 345,707,752,456 | 207,182,288,396 | **138,525,464,060** |
| `t3` | 24,238,509,972 | 11,322,118,044 | **12,916,391,928** |

The drops are individual cuts with all earlier constraints already active; they need not sum to the previous unperturbed resonant phase decrements.

## Structural interpretation and generalization

Because the original target-1 first-zero families are exact finite first-zero witnesses and their other coordinates have strict slack except explicitly audited ties, their target-1 thresholds depend continuously and nontrivially on the perturbed mass `X_(1,3)`. The target-0 threshold set remains fixed. For sufficiently small nonzero rational perturbations of this same signed direction avoiding finite coincidences, the three target-1 resource thresholds split off from their original target-0 resonance values, while observation and positivity are preserved. The displayed `eta` is a full exact finite witness and proves this instability constructively.

This is a statement about **sensitivity of threshold-value compression under invisible initial-state perturbations**; the complete 28-coordinate chain feasibility test remains valid throughout. The 15-atom minimum-distance result for the original endpoints and the open universal 15-legal-step question are not changed by this experiment.

## Reproduction, data and next unit

The lossless file `VERIFY_PERTURBED_RESONANCES.py.gz.b64` decodes to the locally executed Python-3 standard-library checker. To reconstruct and execute it:
```bash
base64 -d VERIFY_PERTURBED_RESONANCES.py.gz.b64 | gzip -d > VERIFY_PERTURBED_RESONANCES.py
python3 VERIFY_PERTURBED_RESONANCES.py
```
Expected decoded source SHA-256: `4076c869654e1d8c087a46de90d2b856c963b19494f6056197819fe953b02ed9`. `EXACT_OUTPUT.txt` is the captured executed result. The expanded 28-coordinate validator was run locally; independent remote-byte execution and independent mathematical review remain open.

**Next discrimination:** For a finite labeled BRC atom set and a current positive state, characterize (using each coordinate's subset-sum spectrum and exact coincidence constraints) the rational-affine chambers where a chosen coordinate generates the complete first-zero spectrum. Separate threshold *generation*, exact first-zero *activation*, and schedule-count jumps. Start with the one-parameter family `X+eta H`; compute its exact chamber boundaries, including the sign-dependent behavior of the three resource resonances. This retains the frozen source atoms and all observation equations.

No formal Task CLAIM, Source Result, reviewer authority, native X6 mapping or protected P000 change is asserted by this author-side proof.
