# E002 Supplement 01 — Scale Tradeoff and Black-Box Equivalence

Status: `ACTIVE ENGINEERING RESEARCH`  
Program: `E002`  
Depends on: `E002-T01..T10`  
Novelty: `NOVELTY_UNVERIFIED`

## 1. Why this supplement exists

The first E002 note proves that a target-centered precision fiber plus state persistence is exactly a symmetric hysteretic relay. That already blocks a weak novelty claim. The next question is sharper:

> Can the precision-native interpretation produce any relay-level input/output behavior that a conventional hysteresis controller cannot reproduce?

For the current E002 response law, the answer is no. This supplement records that no-go result and then derives the exact engineering tradeoff created by increasing the precision half-width `d`: coarse precision suppresses disturbance-driven switching, but the same coarsening can also suppress a corrective switch caused by a genuine target error.

## 2. E002-T11 — Black-box equivalence under arbitrary precision schedules

Status: `PROVED BY STEPWISE IDENTITY`.

Let

\[
(e_t)_{t\ge0}
\]

be any finite or infinite integer error sequence, and let

\[
(d_t)_{t\ge0},\qquad d_t\in\mathbb N_{>0},
\]

be any externally declared precision schedule.

The E002 update is

\[
u_{t+1}=R_{d_t}(e_t,u_t),
\]

where

\[
R_d(e,u)=
\begin{cases}
\mathrm{ON}, & e\le-d,\\
u, & |e|<d,\\
\mathrm{OFF}, & e\ge d.
\end{cases}
\]

Now define a conventional variable-hysteresis relay whose lower and upper thresholds at time `t` are exactly

\[
-d_t\quad\text{and}\quad+d_t,
\]

with the same state-persistence rule between them.

For every input triple `(e_t,u_t,d_t)`, the two next-state maps are identical. Induction on `t` therefore gives

\[
\boxed{
u_t^{\mathrm{E002}}=u_t^{\mathrm{variable\ hysteresis}}\quad\text{for all }t.}
\]

This holds for arbitrary time-varying precision schedules and arbitrary input sequences; no regularity or monotonicity assumption is needed.

### Consequence

No black-box experiment that observes only

```text
error input -> relay output
```

can distinguish the current E002 controller from a conventional hysteresis controller whose thresholds are coupled to the same `d_t` schedule.

Therefore the precision-native claim is not a new relay function class. Its falsifiable content must live in the **origin and coupling of `d_t`**:

- is `d_t` independently fixed by sensing, representation, actuation, or another world-engine resolution constraint?
- does changing that independently justified precision automatically move the control thresholds without a second deadband parameter?
- do multiple operations consume the same precision coordinate consistently?

If `d_t` is tuned only to obtain the desired switching behavior, E002 collapses to ordinary variable hysteresis with renamed parameters.

## 3. E002-T12 — Immediate switch extinction under coarsening

Status: `PROVED`.

Fix a nonzero measured error `e` and a relay state that conflicts with the sign of that error:

- `u=OFF` with `e<0`, or
- `u=ON` with `e>0`.

Write

\[
m=|e|>0.
\]

At precision `d`, the corrective switch is forced exactly when the signed error lies outside the target fiber. Hence

\[
\boxed{
R_d(e,u)\ne u
\iff
d\le m.
}
\]

Equivalently,

\[
\boxed{
R_d(e,u)=u
\iff
d\ge m+1.
}
\]

Thus the smallest integer coarsening that extinguishes the immediate corrective switch is

\[
\boxed{d_{\mathrm{extinct}}=|e|+1.}
\]

### Monotonicity at one decision

For fixed `(e,u)`, increasing `d` can only retract a forced switch into persistence. It cannot create a new immediate switch that was absent at a finer precision.

Conversely, refinement can expose a sign-separated state and create a corrective switch that was previously collapsed, but it cannot hide a switch that was already forced at a coarser threshold small enough to resolve the error.

This is the control-side cost of coarse precision. E002-T03 showed that coarsening beyond the disturbance radius can eliminate target chatter; E002-T12 shows that the same operation can also preserve an outdated actuator state when a real excursion is still smaller than the coarse target fiber.

The theorem is deliberately one-step. Across a full trajectory, prior precision choices may have changed the relay state, so trajectory-level monotonicity does not follow automatically.

## 4. E002-T13 — Exact robust-immunity / robust-detection feasibility window

Status: `PROVED`.

Assume bounded additive integer measurement disturbance

\[
|\eta|\le N,
\qquad N\in\mathbb N.
\]

We ask for one fixed integer precision `d` that satisfies both requirements:

1. **target immunity:** at true error zero, every admissible disturbance preserves the current relay state;
2. **robust correction:** at a genuine error of magnitude `E>0` opposing the current state, every admissible disturbance forces the corrective switch.

From E002-T03, target immunity is equivalent to

\[
d>N,
\]

or, over integers,

\[
d\ge N+1.
\]

For a negative excursion `x=-E` while the relay is `OFF`, E002-T06 says MUST `ON` requires

\[
-E\le-d-N,
\]

which is equivalent to

\[
d\le E-N.
\]

The positive-excursion/`ON` case is symmetric and gives the same bound.

Therefore the exact feasible precision set is

\[
\boxed{
N+1\le d\le E-N.
}
\]

This set is nonempty if and only if

\[
N+1\le E-N,
\]

that is,

\[
\boxed{E\ge2N+1.}
\]

So the smallest integer true-excursion magnitude for which **complete target-noise immunity and worst-case guaranteed corrective detection can coexist** is

\[
\boxed{E_{\min}=2N+1.}
\]

When the condition holds, the number of admissible integer precision choices is

\[
\boxed{E-2N.}
\]

### Interpretation

This is not a claim that hysteresis removes a fundamental control tradeoff. It proves the opposite. Once bounded disturbance and guaranteed detection are both demanded, the precision coordinate is trapped in an exact finite interval. Making `d` larger improves immunity only until it begins to erase genuine excursions; making `d` smaller improves sensitivity only until bounded disturbance can force unwanted switches.

The same algebra exists for conventional symmetric hysteresis. The E002-specific research question remains whether `d` is independently supplied by the finite representation rather than independently tuned as a controller deadband.

## 5. Relation to E001 and the common scale principle

E001 and E002 now show that coarsening does **not** have a universal dynamical meaning.

- In E001, coarsening can collapse a positive spatial gap into coarse contact and thereby **create** a collision response.
- In E002, coarsening expands the target-equivalence fiber and can thereby **extinguish** a corrective relay switch.

The shared invariant is not “coarse precision always creates interaction” or “coarse precision always suppresses interaction.” The shared invariant is only:

\[
\boxed{
\text{precision changes the represented relation first;}
\quad
\text{the declared response law determines the dynamical consequence.}
}
\]

This strengthens the four-stage architecture already emerging across the engineering lanes:

```text
finite precision collapse/refinement
-> scale-level observable relation
-> declared response law
-> finite next state
```

Any general theory that attempts to infer dynamics directly from the direction of precision change, without naming the observable relation and response law, is therefore too strong.

## 6. Validation target

The accompanying regression test exhaustively checks bounded integer boxes for:

- E002 trajectory equality with an independently written variable-hysteresis comparator under changing precision schedules;
- exact switch-extinction threshold `|e|+1` for both sign/state orientations;
- exact robust precision window `[N+1,E-N]` and feasibility condition `E>=2N+1` using the finite MAY/MUST disturbance relation itself.

These are mathematical regression checks, not historical novelty evidence.
