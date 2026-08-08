# P019 — Integer Focusing, Supplement 05: Finite Focusing, Relative Expansion, and a Branch-Clock Candidate

Status: `ACTIVE RESEARCH NOTE / EXTERNAL-COMPARISON GATE OPEN`  
Depends on: P011 collision spectrum, P019 Directed Expansion Supplement 03  
Scope: derive a pure-integer finite-focusing theorem and fraction-free relative-expansion ordering from `Xi=B-C`  
Discipline: this is not a proof of a discrete Raychaudhuri equation; it constructs integer theorems suitable for structural comparison with it.

## 1. Starting point

For a nonempty cross-section `A` of a finite directed primitive graph, P019-D proved

\[
\Xi(A)=|F(A)|-|A|=B(A)-C(A),
\]

where:

- `B(A)` is outgoing branching surplus;
- `C(A)` is the collision/focusing excess produced when multiple outgoing incidences merge into the same future target.

Define the **focusing margin**

\[
\boxed{M(A)=C(A)-B(A)=-\Xi(A).}
\]

Hence

\[
M<0 \iff \Xi>0,
\qquad
M=0 \iff \Xi=0,
\qquad
M>0 \iff \Xi<0.
\]

## 2. P019-F-T01 — Strict collision domination is exactly bounded section contraction

Status: `PROVED`

For every positive integer `q`,

\[
\boxed{C(A)\ge B(A)+q}
\]

if and only if

\[
\boxed{\Xi(A)\le-q.}
\]

Therefore

\[
\boxed{|F(A)|\le |A|-q.}
\]

This is an immediate integer consequence of `Xi=B-C`, but it upgrades a sign statement into an exact cardinality contraction bound.

## 3. P019-F-T02 — Finite focusing theorem

Status: `PROVED`

Let

\[
A_{t+1}=F(A_t)
\]

and suppose that whenever `A_t` is nonempty there is a fixed positive integer `q` satisfying

\[
C(A_t)\ge B(A_t)+q.
\]

By T01,

\[
|A_{t+1}|\le|A_t|-q.
\]

Iteration gives

\[
|A_t|\le|A_0|-tq.
\]

Because cardinality cannot be negative, the future section must become empty no later than

\[
\boxed{
T_*
\le
\left\lceil\frac{|A_0|}{q}\right\rceil.
}
\]

The internal form needs no rational ceiling:

\[
\boxed{
T_*
\le
(|A_0|+q-1)//q.
}
\]

In particular, if

\[
C(A_t)\ge B(A_t)+1
\]

persists at every nonempty step, then

\[
\boxed{T_*\le|A_0|.}
\]

This is a genuine finite focusing theorem: persistent collision domination forces finite-step extinction rather than merely asymptotic convergence.

It is a finite combinatorial theorem and requires no affine parameter, differential equation, or continuum limit.

## 4. Boundary of the comparison with external focusing theorems

In classical GR the Raychaudhuri equation governs the evolution of geodesic-congruence expansion and, under appropriate conditions, supports finite-affine/proper-time focusing results.

P019-F-T02 is similar only in **logical shape**:

`persistent negative expansion/focusing condition -> finite focusing`.

It does not derive:

- the continuum expansion scalar;
- shear or vorticity;
- the Ricci tensor;
- an energy condition;
- conjugate points;
- Einstein dynamics.

The current result may therefore be called an **integer finite-focusing theorem**, but not a completed discrete Raychaudhuri theorem.

## 5. P019-F-T03 — Fraction-free relative-expansion change numerator

Status: `PROVED`

Let

\[
N_t=|A_t|>0,
\qquad
\Xi_t=N_{t+1}-N_t.
\]

At the external comparison layer one might write normalized expansion as

\[
\theta_t=\Xi_t/N_t.
\]

Enterprise Math need not store this rational number. Define instead the pure-integer cross-multiplied numerator

\[
\boxed{
\mathcal R_t
=
N_t\Xi_{t+1}-N_{t+1}\Xi_t.
}
\]

Since

\[
\theta_{t+1}-\theta_t
=
\frac{\mathcal R_t}{N_tN_{t+1}},
\]

with strictly positive denominator,

\[
\boxed{
\operatorname{sgn}(\mathcal R_t)
=
\operatorname{sgn}(\theta_{t+1}-\theta_t).
}
\]

Thus:

- `R_t<0`: relative expansion strictly decreases;
- `R_t=0`: relative expansion is unchanged;
- `R_t>0`: relative expansion increases.

The internal decision uses only integer multiplication, subtraction, and order.

This follows the P007/P018 pattern of comparing ratios by cross multiplication rather than making a hidden fraction primitive.

## 6. P019-F-T04 — Branching/collision decomposition of relative-expansion change

Status: `PROVED`

Substitute

\[
\Xi_t=B_t-C_t
\]

into T03:

\[
\mathcal R_t
=
N_t(B_{t+1}-C_{t+1})
-N_{t+1}(B_t-C_t).
\]

Define

\[
\boxed{
\mathcal R^B_t
=N_tB_{t+1}-N_{t+1}B_t,
}
\]

\[
\boxed{
\mathcal R^C_t
=N_tC_{t+1}-N_{t+1}C_t.
}
\]

Then

\[
\boxed{
\mathcal R_t
=
\mathcal R^B_t-\mathcal R^C_t.
}
\]

A fully integer sufficient focusing condition is therefore

\[
\mathcal R^B_t\le0
\quad\text{and}\quad
\mathcal R^C_t\ge0.
\]

Under these conditions

\[
\boxed{\mathcal R_t\le0.}
\]

Semantically:

- branching pressure relative to section size does not increase;
- collision/focusing pressure relative to section size does not decrease;

so relative expansion cannot increase.

This is closer to the question asked by continuum focusing dynamics than merely testing whether `Xi<0` at one instant: it asks whether expansion itself continues to move toward more negative values.

## 7. P019-F-T05 — An intrinsic branch-clock candidate can be defined from the causal graph in the reverse direction

Status: `DEFINITION + EXACT IDENTITY / PHYSICAL INTERPRETATION OPEN`

Correction 04 proved that using an external Schwarzschild clock label to generate causal graph structure is underdetermined.

A more robust research direction is to reverse the arrow: derive a candidate intrinsic causal-rate quantity from the primitive causal graph first.

If every state in a cross-section `A` has at least one future successor, define

\[
\boxed{
K_{\rm branch}(A)
=
\sum_{v\in A}(\deg^+(v)-1).
}
\]

This is exactly the branching surplus:

\[
\boxed{K_{\rm branch}(A)=B(A).}
\]

The central identity becomes

\[
\boxed{
\Xi(A)
=K_{\rm branch}(A)-C(A).
}
\]

The formula itself is an exact integer identity.

However, there is currently **no proof** that `K_branch` is physical proper-time rate, gravitational clock rate, or the earlier Schwarzschild `K_sigma`.

It is therefore only an **intrinsic causal branching-clock candidate**.

Its value is methodological: the research arrow becomes

\[
\text{primitive causal graph}
\to
(K_{branch},C,\Xi),
\]

followed by the question of whether external clock rate is a finite observation of `K_branch`, instead of assuming

\[
\text{clock}\to\text{graph}.
\]

## 8. P019-F-C01 — Zero branch-clock budget still does not by itself define a horizon

Status: `COUNTEREXAMPLE / NECESSITY RESULT`

If

\[
K_{branch}=B=0,
\]

then

\[
\Xi=-C\le0.
\]

But there are two distinct cases.

### No collision

If the successor map is injective on `A`,

\[
C=0,
\qquad
\Xi=0,
\]

so the section is marginal.

### Collision

If two current states merge into one future state,

\[
C>0,
\qquad
\Xi<0,
\]

so the section contracts.

Thus even after defining an intrinsic causal clock as branching budget,

\[
\boxed{
K_{branch}=0
\not\Rightarrow
\Xi=0.
}
\]

The collision/focusing channel remains essential.

This again supports the common-structure model: time/branch capacity and spatial convergence cannot be completely described by one scalar variable.

## 9. An integer research template closer to Raychaudhuri

At this stage the next problem can be compressed into

\[
\boxed{
N_t,
\quad B_t,
\quad C_t,
\quad \Xi_t=B_t-C_t,
\quad
\mathcal R_t=N_t\Xi_{t+1}-N_{t+1}\Xi_t.
}
\]

The external Raychaudhuri comparison concerns the derivative of congruence expansion and source terms such as shear and curvature.

The integer questions are now:

1. which local combinatorial structures control `R^B_t`;
2. which local collision-spectrum or curvature-like structures control `R^C_t`;
3. whether an integer energy/focusing condition can force

\[
\mathcal R^B_t\le0,
\qquad
\mathcal R^C_t\ge0;
\]

4. whether the full P011 `J_k^out` contains enough structure beyond the coarse `C` to distinguish shear-like from Ricci-like focusing;
5. which causal-set or discrete-Ricci tools are useful comparison mathematics without making probability or real-valued transport distance primitive in Enterprise Math.

## 10. Initial external prior-art scan

Two comparison directions are especially important:

1. causal set theory takes locally finite causal order as a fundamental discrete structure and, in continuum approximation, uses cardinality as the analog of spacetime volume. This is methodologically adjacent to P019's causal-relation plus finite-cardinality route, but causal-set theory has its own established definitions, random sprinkling, covariance, and dynamics literature and must be cited explicitly;
2. the 2026 work *Ollivier-Ricci Curvature for Causal Sets* constructs a mesoscopic Ricci-curvature notion from Lorentzian optimal transport and probability measures on causal diamonds. It demonstrates direct prior art for extracting curvature-like information from order-theoretic discrete data, while using probabilistic/optimal-transport primitives different from the current Enterprise Math integer-only core.

Novelty claims must therefore remain narrow. Any potentially new contribution would have to lie in the **specific integer branch/collision calculus and its integration with Enterprise Math precision/fiber machinery**, not in a claim to be the first discrete causal or curvature treatment of black holes.

## 11. Stage ledger

- `P019-F-T01`: collision domination iff bounded integer contraction — `PROVED`
- `P019-F-T02`: finite focusing under persistent positive margin — `PROVED`
- `P019-F-T03`: cross-multiplied relative-expansion change numerator — `PROVED`
- `P019-F-T04`: branching/collision decomposition of relative-expansion change — `PROVED`
- `P019-F-T05`: no-sink intrinsic branch-clock candidate equals branching surplus — `DEFINITION + EXACT IDENTITY`
- `P019-F-C01`: zero branch-clock budget does not by itself imply marginality — `COUNTEREXAMPLE / NECESSITY`

Executable checks:

- `src/enterprise_math/focusing.py`
- `tests/test_focusing.py`

## 12. Next stage

Two directions have priority:

1. **local source decomposition**: try to decompose `C` or `R^C` into pure-integer local terms comparable to shear-like and curvature-like effects;
2. **clock-calibration no-go / bridge**: determine whether Schwarzschild/RN finite clock observations can be legitimate P018 observations of `K_branch`. If not, formally demote “clock” from a primitive variable to a derived observable.

Until those are resolved, do not move on to black-hole entropy coefficients, Hawking radiation, or detailed Kerr calculations.
