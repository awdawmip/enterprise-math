# R5 — Quantitative BRC support-gap stability under source/history-sensitive terminal errors

**Research date:** 2026-10-31 Asia/Shanghai.
**Scope/status:** New author-side *conditional analytic theorem* and exact rational checks. `AUTHOR_DERIVED_CONDITIONAL_ON_R5_BASELINE / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING`. The preexisting R5 Bellman support formula is a cited premise, not independently reconstructed here. No X6-native correspondence or physical-law inference.

## Frozen sources and inherited result

- Global account knowledge: `awdawmip/chatgpt-global-knowledge main@dcf0d53b5d5a749b42de27537f733acd7f201b84`. Read bootstrap, manual, ACTIVE worldview and math/BRC/code/research rules.
- Enterprise Math: canonical `main@cb59f2d182fa47f65cbb1e9de7e9c89b01239c48`. Read P000, joint-relation preservation, X6/Heartbeat contract and portable research protocol.
- Scientific predecessor, unreviewed author-side commit `e7916482f44a925e11ece98e406309f4655fb1f1`: `research_notes/brc_r5_positive_two_merger_rigidity_20261031_t1340/README.md` and its evidence archive. The baseline support identity below is inherited as an explicitly conditional input.

The finite positive two-law STOP/CONTINUE model has source `i=0,1`, Q origin mass `1/2` each, and conditional Q stage-2 probabilities `(alpha_i,1-2alpha_i,alpha_i)`, with `0<alpha_i<1/2`, for LR classes `(1/2,1,3/2)`. The corresponding P probabilities are `(alpha_i/2,1-2alpha_i,3alpha_i/2)`. Both outer stage-2 routes optionally reach the shared stage-3 LR=1 decision gate. Terminal errors are expected indicators under each law; the other observables are the respective expected stopping times. FULL may distinguish origins and histories; seedless LR behavior cannot.

Let `s=(alpha_0+alpha_1)/2`, `d=|alpha_0-alpha_1|`, and `c=3/4+1/(2s)>0`. The predecessor's author-side Bellman calculation gives the support gap in direction `H=c e_Q - T_Q`:

```text
Delta_H^0 := max_FULL H(O^0) - max_LR H(O^0) = d/(4s). (R5-input)
```

The original proof is an unreviewed research input. Conditional use of that identity is kept explicit throughout this result.

## New lemma — observer support is Lipschitz in terminal labels

Fix **all** natural P/Q path weights, decision topology and feasible strategy sets. Replace terminal Q-error label `r^0(h,a)` by any legal label `r^1(h,a) in [0,1]`, with `|r^1-r^0|<=epsilon` on a declared cylinder `C` of complete branch/decision histories; labels outside C remain unchanged. The replacement may independently depend on hidden source, route, full retained history and terminal action. P-error labels can be modified arbitrarily, independently.

Suppose Q-probability of reaching C is bounded `Q_pi(C)<=m` for every FULL and LR real behavioral policy. Because only terminal Q-errors change,

```text
|e_Q^1(pi)-e_Q^0(pi)|
= |sum_(h in C) Q_pi(h)*(r^1(h,a_pi)-r^0(h,a_pi))|
<= epsilon*Q_pi(C) <= m*epsilon.                          (1)
```

The positive Q branch mass is summed **only** for this declared absolute perturbation bound. Origin and route labels remain in the underlying BRC carrier and in the full strategy/error observer. No permanent quotient or native X6 state elimination follows.

Stopping times are unchanged, so each strategy obeys `|H(O^1_pi)-H(O^0_pi)| <= c*m*epsilon`. Apply `|sup f-sup g|<=sup|f-g|` separately to FULL and LR to obtain the new all-real theorem

```text
Delta_H^1 >= Delta_H^0 - 2*c*m*epsilon.                  (2)
```

This lemma does **not** depend on (R5-input). Since H ignores e_P, arbitrary legal changes to P-error labels leave this exact support gap identically unchanged.

## Corollary A — arbitrary terminal Q-error changes

For changes anywhere in the terminal law, `m=1`. Combining (2) with the inherited support identity,

```text
Delta_H^1 >= [d-(6*s+4)*epsilon]/(4*s).                  (3)
```

For `d>0`, strict four-observer convex-hull separation persists for every legal kernel with `0<=epsilon<d/(6*s+4)`. Thus `d/(6*s+4)` is a **necessary minimum amplitude** for possible terminal-error-only hull repair, not a sufficient condition.

## Corollary B — source/history-sensitive post-merger responses only

Let C consist of complete terminal histories that pass through the shared stage-3 merger. Before optional STOP choices, the Q source-labelled outer-route weights are exactly

```text
(alpha_0/2, alpha_0/2, alpha_1/2, alpha_1/2).
sum = alpha_0 + alpha_1 = 2*s.
```

Any earlier STOP decreases the mass reaching the merger, hence uniformly `Q_pi(C)<=2s`. Substituting `m=2s` into (2) gives

```text
Delta_H^1 >= d/(4*s) - (3*s+2)*epsilon
          = [d-4*s*(3*s+2)*epsilon]/(4*s).              (4)
```

Consequently, for unequal origins (`d>0`), equal four-dimensional FULL/LR observation convex hulls under post-merger-error-only calibration **require**

```text
epsilon >= d/[4*s*(3*s+2)].                            (5)
```

This rigorously excludes every source-/route-/history-/action-sensitive legal Q-error kernel in a full continuous neighborhood around the baseline. P-error response may vary arbitrarily without affecting this separator. The exclusion retains the fixed natural transition law and decision incidence; it makes no claim for changed natural transitions or topology.

The BRC source residual remains `(alpha_0-alpha_1,-2(alpha_0-alpha_1),alpha_0-alpha_1)`, with conditional total-variation `2*d`. The summation to `2s` is certified only for this one-shot bounded Q-error readout at the finite horizon, not for future path-sensitive operations. No native X6 correspondence is claimed.

## Exact benchmark and stronger convex-hull distance

At `(alpha_0,alpha_1)=(1/4,1/8)`,

```text
s=3/16, d=1/8, c=41/12, Q(C)<=3/8.
J=12*H=41*e_Q-12*T_Q,  ||J||_1=53.
baseline support gap Delta_J^0=2.
Delta_J^1 >= 2-(123/4)*epsilon.                         (6)
```

Hence every legal post-merger Q-error modification of amplitude `epsilon<8/123` preserves strict convex-hull separation. At `epsilon=1/16` the exact residual gap is at least `5/64>0`.

Finite-horizon compactness gives a FULL policy `x^1` maximizing new J. For every point `y` of the **entire new LR convex hull**, `J(x^1-y)>=Delta_J^1`. By the L1/Linfinity dual inequality,

```text
dist_inf(x^1, conv(O_LR^1))
   >= [2-(123/4)*epsilon]/53.                          (7)
```

At `epsilon=1/16`, this is `5/3392`. This is an **existence certificate** for a possibly new FULL optimizer; it does not assume the previous witness remains optimal after label changes. For arbitrary all-terminal Q-error perturbations instead, the benchmark threshold is `epsilon<1/41`.

## Verification, boundaries and next discriminating unit

`VERIFY.py` uses standard-library exact `Fraction` arithmetic. For five rational alpha pairs it checks strict P/Q normalization, four retained Q outer-route masses, algebraic constants, and exhausts 81 rational reach combinations times 16 signed error changes per pair, verifying the sharp local one-policy mass envelope. It does **not** rerun the predecessor's Bellman support optimization or a native X6 experiment. The full real-parameter claim is established by the written inequality proof conditional on the R5-input, not by extrapolating this finite test.

The new quantitative exclusion eliminates the small-amplitude terminal-response search region for the strictly positive two-merger stochastic model. Next: at `alpha_0=1/4`, `alpha_1=1/8`, test exact rational Q-error changes with `epsilon>=8/123`, seeking a four-hull equality certificate (every FULL vertex as an exact nonnegative combination of at most five LR vertices) or another explicit Farkas separator. Only if full hull equality and rank four hold, test nonmembership in the *real behavioral* LR image. The original mother target, formal Source CLAIM/Result, independent Driver review and X6 bridge remain open.
