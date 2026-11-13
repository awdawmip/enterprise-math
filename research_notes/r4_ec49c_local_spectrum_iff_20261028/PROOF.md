# EC49C — Sharp likelihood-ratio-spectrum criterion for one terminal continuation

Date: 2026-10-28 (Asia/Shanghai). Author-side TASK_RESEARCH continuation of EC49B (Draft PR #1620, immutable `fde05e28dfd8e8f74a67710139e1503359903005`). Status: `AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / UNREVIEWED / NOT_ADMITTED`. Research context is shared with EC48U–EC49B and is not an independent Driver review.

## Frozen scientific interpretation

This is a strictly positive, finite, two-source P/Q *auxiliary probabilistic BRC observation* model. The carrier consists of labeled branches and exact positive P and Q masses; the quotient erases a pre-terminal ancillary signal W while retaining the current exact P/Q likelihood ratio. The declared observer is `O=(P(accept), Q(accept), E_P T, E_Q T)`, with source-neutral behavioral randomization. The allowed next actions are `accept`, `reject` or `continue` at the penultimate decision, and `accept`/`reject` after exactly one informative terminal observation. Stopping time T counts these abstract decision stages. These are neither physical heartbeat steps nor signed/phase BRC amplitudes.

The project ontology remains P000: native discrete six-axis X6 Cell space and separately typed time. No X6 state, six-axis placement/update/readout or signed BRC correspondence has been constructed for this auxiliary model. Thus the result is a scoped observation/compression theorem, not a native X6 dynamical theorem.

## 1. Exact local theorem

Fix an earlier prefix policy, and a **reachable, isolated** penultimate coarse readout state z of positive Q mass q. Assume:

1. Its P mass is `lambda*q`, with `lambda>0`; at z, every fine history, including W, has the same exact pre-action likelihood ratio lambda.
2. W has finite support with `kappa(w)>0`, and `P(W=w|z)=Q(W=w|z)=kappa(w)` (source ancillarity).
3. If `continue` is selected, a final signal Y has strictly positive normalized conditional kernels `K_P^w(y), K_Q^w(y)`. At the final decision the coarse controller can read its **current complete LR** `lambda*R_w(y)`, where `R_w(y)=K_P^w(y)/K_Q^w(y)`; it need not retain W. No action follows the final accept/reject decision, and continuing takes exactly one additional decision-time unit.
4. Controllers use source-neutral real behavioral probabilities, no source selector or retained private random seed. Both coarse and W-refined controllers may stop/accept/reject or continue at z. Other prefix policies are held fixed for the local comparison.

Define the conditional **Q-law** of the terminal LR, including ratio collisions, by

`nu_w(r) = sum_{y: R_w(y)=r} K_Q^w(y)`.

Every `nu_w` is a finite positive probability distribution over positive ratios and satisfies `sum_r r*nu_w(r)=1`.

**Theorem (local exact iff).** For this fixed prefix/coarse state and the complete four-output raw observation region, W deletion is universally safe for all real source-neutral behavioral choices **if and only if** every reached `nu_w` is identical. The statement concerns the isolated state with its fixed prefix mass and controller language; it does not claim that global set equality after reoptimizing an unrelated earlier prefix implies the local condition.

**Sufficiency (raw, not convexified).** When `nu_w=nu`, take an arbitrary W-aware policy with penultimate action probabilities `pi_w(a)`. Replace its coarse penultimate policy by `mu(a)=sum_w kappa(w)pi_w(a)`. Because W is ancillary, the two source-specific immediate acceptance probabilities and continuation masses match. At final ratio r, set the coarse acceptance probability to the conditional Q-mass-weighted average of all W-aware accepting branches at r, divided by `mu(cont)*nu(r)`; if this is zero, the value is arbitrary. The numerator and denominator are computed from the *fixed* policy and may depend on z, not on the hidden actual source. All fine atoms in the ratio fiber have common P/Q ratio `lambda*r`, so the Q equality simultaneously implies P equality. The continuation masses match, giving equal `E_P T` and `E_Q T`. This constructs one legal coarse controller realizing **the same raw O**. The W-aware observer can ignore W for the converse inclusion. This strengthens neither the horizon nor the native BRC carrier relative to EC49B Theorem B.

**Necessity (explicit separating support direction).** For `t>=0` write

`C_w(t)=sum_r nu_w(r)*(r-t)_+`, `D_w(t)=C_w(t)-(1-t)_+ >= 0`, with `x_+=max(x,0)`.

The inequality is Jensen's inequality, using `sum r*nu_w(r)=1`. The positive-part threshold payoff is the best terminal acceptance contrast `P(accept)-lambda*t*Q(accept)` per unit conditional Q mass. The best stop-now contrast is `lambda*(1-t)_+`. The value `D_w(t)` is their additional benefit, normalized by lambda.

For any `c>=0`, use the *linear* four-vector support functional

`F_{t,c}(O) = alpha - lambda*t*beta - [lambda*c/(lambda+1)]*(E_P T+E_Q T)`.

The shared prefix contribution and the t-stage baseline are constants. Conditional on W, one extra continuation step has P/Q time-cost total `lambda*c*q*kappa(w)`. Therefore the **exact** W-observation advantage in the optimized local support is

`Gap_{z}(t,c) = lambda*q * ( sum_w kappa(w)*(D_w(t)-c)_+ - (sum_w kappa(w)*D_w(t)-c)_+ ) >= 0.`

This accounts for *all real randomized* behavioral policies: the support objective is affine in each action probability; at the terminal stage the LR threshold rule maximizes its contribution, and at the penultimate stage stop/continue compares the stated affine options. There is no hidden convexification of the raw region.

If two spectra differ, the finite call-payoff transforms `C_w(t)` differ at some nonnegative t. Indeed these functions are continuous piecewise affine with breakpoints at the union of positive LR support atoms, have common value 1 at t=0, and vanish beyond the largest ratio. Equality at every breakpoint implies equality everywhere; their one-sided slopes recover each tail mass and therefore the complete distribution. Their `D_w` then differ for some t. Choose any c strictly between the minimum and maximum `D_w(t)`. Since every `kappa(w)>0`, some terms `D_w-c` are positive and others negative, and the displayed Jensen-positive-part inequality is **strict**. Thus a linear functional separates the fine and coarse raw regions (indeed their convex hulls). If P/Q kernels and lambda are rational, choose t from the finite ratio breakpoints and c as the rational midpoint: this yields an exact rational strict separation certificate. QED.

### Corollary: finite exact certificate algorithm

Compute each reduced rational ratio `R_w(y)`, aggregate its conditional Q masses to obtain `nu_w`, and compare the transforms at the sorted union of support ratios. If they agree, output a constructive LR-fiber-averaging simulation. Otherwise take a knot t where `D_w(t)` differ and choose `c=(min_w D_w(t)+max_w D_w(t))/2`. The formula above is the exact rational separation certificate. No approximate optimization or generic real-closed-field solver is required for this local one-step decision language.

## 2. Minimal four-positive-leaf separating model

Let `W=0,1` have P=Q probability 1/2, and let final binary V obey:

| W | P(V=1|W) | Q(V=1|W) | conditional Q-law of R |
|---|---:|---:|---|
| 0 | 3/4 | 1/4 | `nu_0(1/3)=3/4, nu_0(3)=1/4` |
| 1 | 1/2 | 1/4 | `nu_1(2/3)=3/4, nu_1(2)=1/4` |

All four unconditional leaf masses are strictly positive:

| W,V | P | Q | P/Q |
|---|---:|---:|---:|
| 0,0 | 1/8 | 3/8 | 1/3 |
| 0,1 | 3/8 | 1/8 | 3 |
| 1,0 | 1/4 | 3/8 | 2/3 |
| 1,1 | 1/4 | 1/8 | 2 |

Both sources normalize to 1. At threshold t=1, `D_0=1/2`, `D_1=1/4`; select the rational one-step cost `c=3/8`. Here lambda=q=1. Writing the support functional up to an irrelevant common additive constant,

`F'(O)=alpha-beta-(3/16)*(E_P T+E_Q T-2)`, with `T=1` if stopped at W and `T=2` if continued.

The **coarse maximum equals 0**: stopping immediately has zero P-Q contrast, while continuing on any source-neutral probability x yields at most `x*(3/8)` terminal accept/reject contrast and incurs `x*(3/8)` extra time cost. The **W-refined maximum equals 1/16**: continue only when W=0, reject when W=1, then accept at the terminal step iff the current LR exceeds 1. This policy realizes the explicit raw four-vector

`O_fine=(3/8, 1/8, 3/2, 3/2)` and `F'(O_fine)=1/16`.

The exact separating gap is therefore `1/16>0`, so this raw point also lies outside the coarse **convex hull**. The finite verifier independently enumerates 48 coarse and 144 refined deterministic policies, including every terminal LR accept/reject bit assignment, and checks these exact optima.

## 3. Execution and verification scope

Run `python VERIFY.py`; its JSON stdout is `EXACT_REPORT.json`. Only Python standard-library `fractions.Fraction` is used. The code asserts positive P/Q leaf masses, source normalization, both LR spectra, exact gap and witness; it exhausts all 48+144 deterministic policies in the four-leaf model. Separately it tests 243 binary positive rational kernel pairs and W weights on the grid {1/4,1/2,3/4}, of which 63 have equal spectra and 180 unequal spectra. For each unequal pair it constructs an exact positive separation at one LR knot and a rational cost. These finite checks validate the construction, algorithm and counting; the stated all-real iff is established by the preceding proof.

**Scope boundaries:** Strictly positive finite auxiliary P/Q probabilities, one optional informative terminal step, fixed reachable z/prefix and current complete terminal LR. The local necessity implication cannot be applied without checking optional continuation, source ancillarity, full terminal threshold actions, fixed prefix, time-cost freedom and current-LR access. Nonlinear/richer future relations, two further decision steps, restricted cost objectives, simultaneous multiple z states, memory-transition constraints, signed/phase BRC and native X6 dynamics are separate problems.

The theorem is an exact, scoped finite statistical experiment/optimal stopping derivation in the Blackwell comparison tradition, not a claim that the general Blackwell theorem or call-payoff calculus was first discovered here. External prior art is listed in SOURCES.md.
