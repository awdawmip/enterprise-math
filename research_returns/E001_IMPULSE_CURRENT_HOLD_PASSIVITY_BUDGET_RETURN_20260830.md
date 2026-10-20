# E001 Impulse Current-Hold Passivity Budget — Research Return

- Task: `RS-E001-IMPULSE-V2`
- Researcher-ID: `EM-E001-7C4A21`
- Claim: `chatgpt-e001imp-20260830-2140-7c4a21`
- Execution branch: `research/e001-impulse-current-hold-passivity-em-e001-7c4a21`
- Execution base: `cdfb6abd2c9ab15e6295a0c07125443c1d619f59`
- Consumed owner: PR #190, `engineering/e001-material-impulse-v2@9ebc903344f61cc0f1cb82d3612113362613160e`
- Verdict: **PASS**
- Owner-local target: **ACHIEVED — exact saved-state sampling defect identity, refinement order, worst/best schedule bounds, and universal passivity criterion**

## 1. Scope

PR #190 already separates static finite force-law work from the causal world policy that samples the force at the **current saved state**. It also gives the minimal elastic two-state warning that current-hold sampling can destroy cycle passivity. This return does not re-own that implementation and does not re-own contact-network quotient mathematics.

The remaining owner-local question addressed here is stronger and exact:

> For an irregular finite deformation grid and arbitrary legal saved-state jumps, what is the exact cost of current-state hold sampling relative to the static chord work, how does that cost change under saved-state refinement, and when is passivity guaranteed for every saved schedule?

The answer is elementary finite-sum algebra specialized to the E001 saved-state dynamics. No novelty claim is made for Riemann-sum identities or partition refinement.

## 2. Setup

Fix a peak depth `K >= 1`, strictly increasing deformation coordinates

`x_0 < x_1 < ... < x_K`, with `dx_i = x_i-x_{i-1} > 0`,

and loading/returning force samples `L_i, R_i`.

A loading saved schedule is

`S=(s_0,...,s_m)`, `0=s_0<...<s_m=K`.

A returning saved schedule is

`T=(t_0,...,t_n)`, `K=t_0>...>t_n=0`.

The PR #190 current-hold policy gives doubled work coordinates

`C_L(S) = 2 sum_j L_{s_j}(x_{s_{j+1}}-x_{s_j})`,

`C_R(T) = 2 sum_j R_{t_j}(x_{t_j}-x_{t_{j+1}})`.

The static chord coordinates are

`H_L = sum_{i=1}^K (L_{i-1}+L_i) dx_i`,

`H_R = sum_{i=1}^K (R_{i-1}+R_i) dx_i`,

with static loss `H = H_L-H_R` and current-hold loss `C(S,T)=C_L(S)-C_R(T)`.

Define the loading sampling deficit and returning sampling excess

`D_L(S)=H_L-C_L(S)`,

`D_R(T)=C_R(T)-H_R`.

## 3. Theorem A — exact passivity-budget identity

For every finite force table and every legal pair of saved schedules,

`C(S,T) = H - D_L(S) - D_R(T)`.

This is an exact identity, with no monotonicity assumption.

### Proof

Substitute the definitions:

`H-D_L-D_R = (H_L-H_R)-(H_L-C_L)-(C_R-H_R)=C_L-C_R`.

QED.

Thus static hysteresis loss is a finite budget. Current-state sampling spends that budget through a loading under-sampling term and a returning over-sampling term.

## 4. Theorem B — monotone branches make both defects nonnegative

Assume both force branches are nondecreasing with depth:

`L_0 <= ... <= L_K`, `R_0 <= ... <= R_K`.

Then for every legal schedule,

`D_L(S) >= 0`, `D_R(T) >= 0`,

hence

`C(S,T) <= H`.

Therefore static chord passivity `H>=0` is only necessary for current-hold passivity under this sampling rule; it is not sufficient. For a fixed schedule pair the exact condition is

`H >= D_L(S)+D_R(T)`.

### Proof

On a loading jump `a<b`, every chord sample over `[a,b]` is at least the held left force `L_a`, so its chord work is at least `2 L_a(x_b-x_a)`. Summing jumps gives `H_L>=C_L`.

On a returning jump `b>a`, every chord sample over `[a,b]` is at most the held high-depth force `R_b`, so its chord work is at most `2 R_b(x_b-x_a)`. Summing gives `C_R>=H_R`.

QED.

## 5. Theorem C — refinement order and exact schedule envelope

Under the same monotonicity hypothesis, inserting a saved depth into either schedule can only make the current-hold cycle **more** passive:

- loading refinement weakly increases `C_L`;
- returning refinement weakly decreases `C_R`;
- therefore either refinement weakly increases `C=C_L-C_R`.

For loading, splitting one jump `a<b` at `c` gives the exact gain

`2 (L_c-L_a)(x_b-x_c) >= 0`.

For returning, splitting `b>a` at `c` gives the exact change in returned work

`2 (R_c-R_b)(x_c-x_a) <= 0`.

Consequently, among **all** saved schedules with peak `K`:

### Worst (coarsest) current-hold loss

`C_min = 2 (L_0-R_K)(x_K-x_0)`.

It is attained by the two jumps `0->K` and `K->0`.

### Best (fully refined) current-hold loss

`C_max = 2 sum_{i=1}^K (L_{i-1}-R_i) dx_i`.

Moreover

`C_max = H - sum_{i=1}^K [(L_i-L_{i-1})+(R_i-R_{i-1})] dx_i`.

The last sum is the exact full-grid endpoint-sampling defect.

### Universal saved-schedule passivity criterion

Every legal saved schedule through peak `K` is current-hold passive **iff**

`L_0 >= R_K`.

Necessity follows from the coarsest schedule. Sufficiency follows because that coarsest schedule is the global minimum of `C`.

This criterion is deliberately strong. In the common E001 situation `L_0=0` and `R_K>0`, no nontrivial monotone force table can be called schedule-independent passive under arbitrary current-saved-state jumps. A passivity claim must therefore also constrain the sampling/saved-state language or change the force/work policy.

## 6. Minimal strong counterexample

Take the two-state grid `x=(0,1)` with

`L=(0,2)`, `R=(0,1)`.

This even satisfies the pointwise static sufficient condition `R_i<=L_i`.

Static chord work:

- loading `H_L=2`;
- returning `H_R=1`;
- static loss `H=+1` (passive).

Current-hold cycle `0->1->0`:

- loading holds `L_0=0`, so `C_L=0`;
- returning holds `R_1=1`, so `C_R=2`;
- current loss `C=-2` (active).

Thus neither static chord passivity nor pointwise `R<=L` is sufficient for the current-saved-state dynamical policy.

A refinement-repair witness is `x=(0,1,2)`, `L=(0,1,1)`, `R=(0,0,1)`: static loss is `+2`; the coarsest current cycle has loss `-4`; the fully refined current cycle has loss `0`. Saved-state refinement can therefore restore passivity without changing the material table.

## 7. Executable verification

`research_checks/E001_IMPULSE_CURRENT_HOLD_PASSIVITY_BUDGET_CHECK_20260830.py` independently enumerates:

- peak depths `K=1..4`;
- every nondecreasing loading and returning sequence over force alphabet `{0,1,2,3}`;
- every irregular grid with each cell width in `{1,2}`;
- every loading partition and every returning partition.

Totals:

- `61,776` force-law/grid cases;
- `3,374,664` saved-schedule pairs.

For every pair it verifies the budget identity and defect signs. For every force-law/grid case it verifies the exact coarsest minimum, fully refined maximum, full-grid defect formula, and the iff universal-passivity criterion. It also freezes the two explicit witnesses above.

Expected verdict: `PASS`, zero mismatches.

## 8. Research consequence

The E001 owner now has an exact separation of three notions that must not be conflated:

1. **material-table passivity** under the declared static chord work;
2. **sampling-policy passivity** for one chosen saved-state schedule;
3. **schedule-independent passivity** over all legal saved jumps.

For monotone branches, (3) is exactly `L_0>=R_K`, and (2) is exactly the static-loss budget inequality `H>=D_L+D_R`. Therefore the causal saved-state world cannot infer dynamical passivity from the material curve alone.

The clean next owner decision is architectural rather than another algebraic identity: choose whether legal dynamics should (a) restrict jump schedules, (b) use endpoint/chord-aware finite work, or (c) carry an explicit work/sampling-correction state. Hidden continuous path reconstruction remains disallowed.

## 9. Boundaries

- No continuum/contact-force model is asserted.
- No claim is made that arbitrary saved jumps are physically preferred; they are simply legal in the current owner semantics unless restricted.
- No contact-network or quotient theorem is re-owned.
- No external novelty claim is made; the value is the exact E001 finite-state classification and regression boundary.
