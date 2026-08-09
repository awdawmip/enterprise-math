# E002 — Precision-Locked Actuation, Supplement 02

Status: `ACTIVE ENGINEERING RESEARCH NOTE`  
Scope: centered precision quotient, actuation compatibility, gcd repair, delayed multi-level control, and adaptive precision  
Parent: `docs/E002_PRECISION_NATIVE_HYSTERESIS.en.md`  
Dependency: P018 finite-precision arithmetic and P023 composition-safe quotient theory

## 1. Why the second stage changes the question

Stage 1 established a strict negative boundary: the E002 relay at precision half-width `d` is black-box identical to an ordinary symmetric hysteresis relay with thresholds `-d,+d`, even when `d` varies in time.

Therefore a second-stage result does not count merely because it produces another hysteresis curve.

The falsifiable structural question is now:

> if precision is already a state coordinate of sensing/representation, when can physical actuation use the same coordinate without reading detail that the precision state has collapsed?

This turns E002 from a threshold-output comparison into a quotient-compatibility problem. P023 now owns the general theorem that a coarse state is future-safe for an operation family exactly when the relevant fibers form a congruence, and that failure should be repaired by the coarsest future-forced refinement. This supplement derives the exact arithmetic specialization for integer translation actuators.

## 2. The actual centered cell width

The Stage-1 target fiber is

\[
-d<e<d.
\]

It contains

\[
\boxed{w=2d-1}
\]

integer states.

This odd integer `w`, not merely the threshold radius `d`, is the natural width of the centered precision cell.

Set

\[
c_w=\frac{w-1}{2}=d-1.
\]

Define the centered quotient and detail

\[
\boxed{
Q_w^c(e)=\left\lfloor\frac{e+c_w}{w}\right\rfloor,
\qquad
R_w^c(e)=(e+c_w)\bmod w.
}
\]

Every signed integer error therefore has the unique exact decomposition

\[
\boxed{
e=wq+r-c_w,
\qquad
q=Q_w^c(e),
\qquad
0\le r<w.
}
\]

No hidden real value is used.

## 3. E002-T14 — The three-way relay observation is the sign of an exact quotient

The Stage-1 observation satisfies

\[
\boxed{
H_d(e)=
\begin{cases}
\mathrm{BELOW},&Q_w^c(e)<0,\\
\mathrm{COLLAPSED},&Q_w^c(e)=0,\\
\mathrm{ABOVE},&Q_w^c(e)>0.
\end{cases}
}
\]

### Proof

`Q_w^c(e)=0` exactly when

\[
0\le e+d-1<2d-1,
\]

which is equivalent over integers to

\[
-d<e<d.
\]

Likewise `Q_w^c(e)<0` iff `e<=-d`, and `Q_w^c(e)>0` iff `e>=d`. ∎

### Consequence

The Stage-1 three-valued observation was not the full precision state. It was a task-specific shadow:

\[
\boxed{
\text{integer error}
\to
\text{centered quotient }q
\to
\operatorname{sign}(q)
\to
\text{relay response}.
}
\]

This explains why `H_d(e)` can be sufficient for the immediate relay response yet fail to be sufficient after plant evolution: it has discarded both the within-cell detail `r` and the magnitude of the nonzero coarse quotient.

## 4. Translation actuators

Let one physical actuation step be the integer translation

\[
T_a(e)=e+a.
\]

Write the actuation increment in the same cell width:

\[
\boxed{
a=kw+s,
\qquad
0\le s<w.
}
\]

For the current state write

\[
e=wq+r-c_w,
\qquad0\le r<w.
\]

Then

\[
e+a
=w(q+k)+(r+s)-c_w.
\]

There is one exact carry

\[
\gamma_a(r)=
\begin{cases}
1,&r+s\ge w,\\
0,&r+s<w.
\end{cases}
\]

and therefore

\[
\boxed{
Q_w^c(e+a)=q+k+\gamma_a(r)
}
\]

and

\[
\boxed{
R_w^c(e+a)=(r+s)\bmod w.
}
\]

The carry is not numerical error. It is the exact event by which an actuation step reads enough within-cell phase to alter the next coarse cell.

## 5. E002-T15 — Exact actuation compatibility criterion

Translation by `a` descends to a deterministic map on the centered quotient `Q_w^c` if and only if

\[
\boxed{w\mid a.}
\]

When `a=kw`, the induced quotient operation is simply

\[
\boxed{q\mapsto q+k}
\]

and the detail is invariant:

\[
\boxed{r\mapsto r.}
\]

### Proof

If `w|a`, then `s=0`, so the carry is always zero and the displayed formulas give the result.

Conversely, suppose `0<s<w`. In one quotient fiber compare the two details

\[
r_0=0,
\qquad
r_1=w-s.
\]

They have the same coarse quotient before actuation. But

\[
\gamma_a(r_0)=0,
\qquad
\gamma_a(r_1)=1.
\]

Hence their next coarse quotients differ. The translation is not fiber-constant and cannot descend through `Q_w^c`. ∎

### P023 interpretation

This is an arithmetic specialization of the P023 fiber-constancy criterion, not a new general congruence theorem.

It gives E002 a clean engineering meaning:

> a sensor/representation precision cell and a physical actuator are exactly composable without hidden repair when the actuator step is locked to the cell width.

## 6. One-step misalignment repair

If `a=kw+s` with `0<s<w`, the one-bit coordinate

\[
\boxed{
\gamma_a(r)=\mathbf 1_{r\ge w-s}
}
\]

is sufficient to recover the next coarse quotient:

\[
Q_w^c(e+a)=q+k+\gamma_a(r).
\]

On every fiber both carry values occur, so one bit is also cardinality-minimal for this declared one-step future quotient.

This is the direct translation analogue of P023's canonical one-bit boundary repair. E002 does not need a separate repair theory.

## 7. Finite multi-level action families

Let

\[
A=\{a_1,\ldots,a_m\}\subset\mathbb Z
\]

be the set of physical increments available to a multi-level actuator.

Define

\[
\boxed{
g=\gcd(w,|a_1|,\ldots,|a_m|).}
\]

Because `w` is odd, `g` is a positive odd divisor of `w` even when some actions are zero.

The centered `g`-width quotient is

\[
Q_g^c(e)
=\left\lfloor\frac{e+(g-1)/2}{g}\right\rfloor.
\]

Since `g|a_j` for every action, every generator descends exactly through this refined quotient:

\[
\boxed{
Q_g^c(e+a_j)=Q_g^c(e)+\frac{a_j}{g}.
}
\]

## 8. E002-T16 — The gcd width is the coarsest all-future action repair

For the action family `A`, the centered width

\[
\boxed{g=\gcd(w,|a_1|,\ldots,|a_m|)}
\]

gives the coarsest refinement of the original `w`-cell partition that is compatible with every finite action word.

Equivalently, inside each original `w`-cell, exactly

\[
\boxed{\frac wg}
\]

future-distinguishable subcells are required.

### Sufficiency

Write

\[
w=gW.
\]

The `g`-width centered quotient refines every `w`-cell into `W` consecutive subcells. Because every action is a multiple of `g`, the exact formula above shows that every action generator, and hence every finite composition of generators, acts deterministically on `Q_g^c`.

P023-T10 through T14 then identify this as a common-compatible quotient candidate for the whole operation family.

### Coarsestness

Within one `w`-cell write details as

\[
r=gA+b,
\qquad
0\le A<W,
\qquad
0\le b<g.
\]

The residues modulo `w` generated by finite words in the actions form the cyclic subgroup

\[
\{0,g,2g,\ldots,w-g\}.
\]

Take two states with subcell indices `A<A'`. The residue

\[
s=w-gA'
\]

is generated by some finite action word modulo `w`. Adding a representative of that word makes every state in subcell `A'` cross the next `w` boundary, while every state in subcell `A` remains below it:

\[
gA'+s\ge w,
\]

but

\[
gA+g-1+s<w.
\]

Therefore the two subcells have different future `Q_w^c` observations under some finite action word. Any quotient compatible with the full operation language must separate them.

Thus no coarser refinement than the `g`-width centered partition can support every future action word. ∎

### Three regimes

The theorem exposes three exact engineering regimes:

1. `g=w`: no refinement is needed; sensing precision and actuation are fully locked;
2. `1<g<w`: only partial within-cell detail is dynamically relevant;
3. `g=1`: the action family eventually forces integer-resolution state for exact arbitrary-horizon prediction.

This is a much sharper statement than saying that an actuator is merely "well aligned" or "poorly aligned" with a quantizer.

## 9. E002-T17 — The actuator-induced precision spectrum

For a nontrivial action family define its physical grain

\[
\boxed{
G=\gcd(|a_1|,\ldots,|a_m|)>0.
}
\]

A centered E002 cell width `u` is already exact for every action, with no repair, if and only if

\[
\boxed{u\mid G.}
\]

Since centered E002 widths are positive odd integers, the exact admissible precision widths are precisely

\[
\boxed{
\{u:u\mid G,\ u\text{ odd}\}.
}
\]

The corresponding E002 half-widths are

\[
\boxed{d_u=\frac{u+1}{2}.}
\]

### Consequence

A physical multi-level actuator therefore induces a finite **precision divisor lattice** rather than an arbitrary tuning continuum.

The all-zero action family is the degenerate exception: every centered width is compatible because the plant never moves, so there is no finite maximum admissible width.

## 10. E002-T18 — Exact projection between nested centered precisions

Let `u|v` be positive odd centered widths and write

\[
v=mu.
\]

The ratio `m` is automatically odd. Let `Q_u^c` and `Q_v^c` be the two centered quotients. Then

\[
\boxed{
Q_v^c(e)
=
\left\lfloor
\frac{Q_u^c(e)+(m-1)/2}{m}
\right\rfloor.
}
\]

Thus the coarser centered precision factors exactly through the finer one whenever their odd cell widths are comparable by divisibility.

### Proof

Write

\[
e=uq+r-\frac{u-1}{2},
\qquad0\le r<u.
\]

Since

\[
\frac{v-1}{2}
=m\frac{u-1}{2}+\frac{m-1}{2},
\]

we obtain

\[
e+\frac{v-1}{2}
=u\left(q+\frac{m-1}{2}\right)+r.
\]

Division by `v=mu` gives the claimed floor quotient. The residual term `r/(mu)` is too small to cross the next `1/m` boundary. ∎

### A nested adaptive ladder

For any odd base `b>=3`, choose widths

\[
1,b,b^2,b^3,\ldots
\]

and therefore E002 half-widths

\[
\boxed{
d_\ell=\frac{b^\ell+1}{2}.}
\]

For `b=3` the first levels are

\[
1,2,5,14,41,\ldots
\]

with widths

\[
1,3,9,27,81,\ldots.
\]

Every coarsening along this ladder is an exact quotient projection. This does not prove that such a ladder is physically preferred; it is an exact engineering candidate for adaptive precision without arbitrary nonnested cell boundaries.

## 11. E002-T19 — The lcm cost of supporting several precision levels with one actuator

Suppose a controller may operate at finitely many centered widths

\[
u_1,\ldots,u_k.
\]

A single physical increment `a` is exact at every one of those precisions if and only if

\[
\boxed{
\operatorname{lcm}(u_1,\ldots,u_k)\mid a.
}
\]

Hence the smallest positive shared exact actuation magnitude is

\[
\boxed{
L=\operatorname{lcm}(u_1,\ldots,u_k).
}
\]

For an action family of grain `G`, all actions are exact at all requested levels if and only if

\[
\boxed{L\mid G.}
\]

### Example

The three E002 half-widths

\[
d=(2,3,4)
\]

have centered widths

\[
(3,5,7).
\]

Therefore

\[
L=\operatorname{lcm}(3,5,7)=105.
\]

An actuator whose physical increments are arbitrary multiples of `105` supports all three levels without repair. An increment of `15` supports widths `3` and `5` but not width `7`.

### Negative boundary

Adaptive precision is therefore not free when one insists that a fixed physical actuator remain exactly closed at every level. Adding mutually incommensurate centered widths can rapidly increase the common actuation unit.

This is a finite arithmetic tradeoff, not a floating-point conditioning statement.

## 12. Delayed multi-level actuation

Let a delay line contain a finite queue of future physical increments, all chosen from an action family whose stable width is `g`.

If the queue itself is retained as an explicit finite state coordinate, then applying its head action gives

\[
\boxed{
q_{t+1}=q_t+\frac{a_{\mathrm{head}}}{g}
}
\]

on the `g`-width centered quotient, while

\[
\boxed{r_{t+1}=r_t.}
\]

The queue then shifts and the new command is appended.

Therefore finite command delay introduces a **memory obligation**, but it does not introduce a finer **spatial precision obligation** once the quotient has already been repaired to the gcd-compatible width.

If the controller's command policy depends only on this quotient plus explicitly retained controller/queue memory, the entire delayed closed loop factors exactly through

\[
\boxed{
(q,\text{controller memory},\text{pending action queue}).
}
\]

No hidden within-cell remainder is needed.

## 13. Misaligned delayed actuation still exposes hidden phase

Take `d=3`, so

\[
w=5.
\]

The errors

\[
e_1=-2,
\qquad
e_2=-1
\]

belong to the same centered quotient cell `q=0`.

Apply the same increment

\[
a=4.
\]

Then

\[
e_1+a=2
\]

remains in `q=0`, while

\[
e_2+a=3
\]

enters `q=1`.

Thus even before a delayed controller makes a second decision, the same coarse state plus the same physical command branches into different coarse futures. The problem is not delay itself. The problem is actuation/precision incompatibility.

## 14. What this adds beyond Stage 1

Stage 1 could be reproduced exactly by a conventional variable-hysteresis relay. Stage 2 still does not claim that a classical digital controller could not reproduce the same input/output sequence.

The stronger structural content is instead:

1. the relay band is the zero cell of an exact centered Euclidean quotient;
2. the same cell width gives a necessary-and-sufficient arithmetic compatibility condition for physical actuation;
3. a whole multi-level action family selects its coarsest all-future safe precision by one gcd;
4. the no-repair precision spectrum is the odd-divisor lattice of the actuator grain;
5. several requested precisions impose an exact lcm cost on a shared physical actuator;
6. finite delay adds state memory but does not force finer precision once the action family is quotient-compatible.

This is where E002 first tests whether one precision coordinate can be reused across sensing, representation, actuation, and future-state prediction rather than being introduced only as a tuned deadband.

## 15. Relation to P018 and P023

The ownership boundary is important.

### P018 supplies

- Euclidean quotient/remainder as exact finite precision coordinates;
- carry as exact information crossing a precision boundary;
- divisibility-based scale transport.

### P023 supplies

- fiber constancy as the criterion for a future operation to descend;
- minimal future-forced repair;
- operation-family closure and arbitrary finite operation-word semantics.

### E002 contributes

- the target-centered odd-width chart induced by the Stage-1 threshold fiber;
- the translation-specific compatibility theorem `w|a`;
- the explicit gcd closed-form for the stable repair of a multi-level translation family;
- the actuator-induced odd-divisor precision spectrum;
- the delayed-control and adaptive-precision engineering interpretations.

The generic congruence machinery is not duplicated or claimed as E002-owned mathematics.

## 16. Executable audit

Reference implementation:

- `src/enterprise_math/precision_locked_actuation.py`

Tests:

- `tests/test_precision_locked_actuation.py`

Deterministic probe:

- `experiments/e002_precision_locked_actuation_probe.py`

Independent reconstruction outside repository CI checked:

- T14 centered-chart reconstruction and threshold equivalence for `d<20` and hundreds of signed errors per precision;
- T15 translation transport and the divisibility criterion across bounded signed increments and fibers;
- T16 gcd-family closure plus coarsestness against all reachable modulo-`w` action residues over multiple small action families;
- T18 centered projection across many odd divisible width pairs.

These bounded checks support the proofs but do not replace repository CI.

## 17. Current falsification boundaries

E002 Stage 2 must be rejected or narrowed if any of the following occurs:

1. the centered quotient fails to reproduce the Stage-1 threshold partition;
2. a non-multiple of `w` acts fiber-constantly on all `w` cells;
3. an action family has a strictly coarser all-word compatible refinement than the proved gcd width;
4. a claimed nested centered projection fails for odd divisible widths;
5. the delayed coarse model diverges from the integer physical model despite every applied increment being a multiple of the retained cell width and the queue being explicit;
6. the project begins treating ordinary congruence, gcd/lcm arithmetic, quantized control, or partition refinement as historically novel.

The historical novelty of the integrated interpretation remains `NOVELTY_UNVERIFIED`.

## 18. Next pressure tests

The highest-value next questions are now concrete:

1. characterize the minimal repair for mixed action families when only a restricted controller language, rather than every action word, matters;
2. measure when the gcd repair saves state relative to full integer resolution in realistic actuator alphabets;
3. introduce actuator saturation and determine whether clipping creates a new boundary-dependent repair beyond gcd alignment;
4. introduce asymmetric positive/negative actuation grains and test whether one scalar centered width remains sufficient;
5. test dynamically changing precision only along the centered divisibility lattice and distinguish scale-change memory from plant-state memory;
6. compare event-triggered and delayed policies without allowing control-policy complexity to be mistaken for a precision theorem.
