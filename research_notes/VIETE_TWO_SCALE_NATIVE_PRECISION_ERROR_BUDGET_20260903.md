# Viète two-scale native precision budget: dyadic truncation plus integer-trace rationalization

Status: `FREE_RESEARCH / EXACT ERROR DECOMPOSITION + CONVERGENT-SUBSEQUENCE PRECISION LAW / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Parents:
- `research_notes/VIETE_SEGMENT_BISECTOR_ROTATION_PRECISION_20260903.md`
- `research_notes/VIETE_ENTERPRISE_J_TRACE_PELL_PRECISION_20260903.md`
- `research_notes/VIETE_STATIONARY_INTEGER_PRECISION_MINIMAL_DIMENSION_20260903.md`

## 1. Two distinct finite-resolution errors

The ideal algebraic Viète tower at depth `n` gives

\[
\Pi_n=2^{n+1}s_n,
\]

with positive transverse component `s_n`, and the classical completion bound already proved in the predecessor is

\[
0<\pi-\Pi_n
\le
\frac{\pi^3}{6\,4^{n+1}}.
\]

But for `n>=2`, the ideal direction generally has irrational slope and is not exactly one finite integer component trace.

Therefore a genuinely native finite-resolution implementation has a second error source: rationalizing the ideal orientation by an integer trace direction.

Freeze:

`DYADIC_TRUNCATION_ERROR != NATIVE_TRACE_RATIONALIZATION_ERROR`.

## 2. Native trace approximation of one ideal direction

Let the ideal positive slope at depth `n` be

\[
\tau_n=\frac{s_n}{c_n}>0.
\]

Choose a positive rational approximation

\[
x=\frac pq
\]

with `p,q` positive integers, interpreted as the native component trace

\[
T_{q,p}.
\]

Its normalized transverse readout is

\[
\widetilde s(x)=\frac{x}{\sqrt{1+x^2}}
=\frac{p}{\sqrt{p^2+q^2}}.
\]

Define the finite trace-based precision readout at ideal depth `n` by

\[
\boxed{
\widetilde\Pi_{n;p,q}
=2^{n+1}\frac{p}{\sqrt{p^2+q^2}}.
}
\]

This uses only the native integer trace components and their frozen sector-local Pythagorean length at the final readout.

## 3. Lipschitz transfer from slope error to pi-readout error

Let

\[
f(x)=\frac{x}{\sqrt{1+x^2}}.
\]

Then

\[
f'(x)=\frac1{(1+x^2)^{3/2}}
\]

so on `x>=0`,

\[
0<f'(x)\le1.
\]

Therefore

\[
|f(x)-f(\tau_n)|\le|x-\tau_n|.
\]

Hence

\[
\boxed{
|\widetilde\Pi_{n;p,q}-\Pi_n|
\le
2^{n+1}\left|\frac pq-\tau_n\right|.
}
\]

This isolates native direction quantization from the ideal dyadic truncation.

## 4. Continued-fraction convergent bound

For every irrational `tau_n`, its ordinary continued-fraction convergents contain infinitely many rational traces `p/q` satisfying the standard bound

\[
\left|\tau_n-\frac pq\right|<\frac1{q^2}.
\]

No claim is made that every denominator budget admits such a trace; `q` below denotes an actual convergent denominator.

For those native trace scales,

\[
\boxed{
|\widetilde\Pi_{n;p,q}-\Pi_n|
<\frac{2^{n+1}}{q^2}.
}
\]

Combining with ideal Viète truncation gives the exact two-source upper envelope

\[
\boxed{
|\pi-\widetilde\Pi_{n;p,q}|
<
\frac{\pi^3}{6\,4^{n+1}}
+
\frac{2^{n+1}}{q^2}.
}
\]

The two terms have opposite dependence on dyadic depth: ideal truncation falls like `4^(-n)`, while a fixed trace denominator becomes more costly after multiplication by `2^(n+1)` in the scalar readout.

## 5. Balanced depth for one available convergent scale

Write

\[
m=n+1,
\qquad
A=\frac{\pi^3}{6}.
\]

The error envelope is

\[
E(m,q)=A2^{-2m}+\frac{2^m}{q^2}.
\]

Treat `m` temporarily as continuous and set

\[
y=2^m.
\]

Then

\[
E(y,q)=\frac{A}{y^2}+\frac{y}{q^2}.
\]

Differentiating gives the balancing scale

\[
-\frac{2A}{y^3}+\frac1{q^2}=0,
\]

so

\[
\boxed{
y^3=2Aq^2.}
\]

Equivalently,

\[
\boxed{
2^{n+1}\asymp q^{2/3}.
}
\]

Thus the dyadic depth that best uses a given good native trace denominator grows only logarithmically with that denominator:

\[
n+1
\sim
\frac23\log_2 q
\]

up to an additive constant from `A`.

## 6. q^(-4/3) balanced error law

At the continuous balance point

\[
y=(2A)^{1/3}q^{2/3},
\]

one gets

\[
E_{\mathrm{bal}}(q)
=
\frac{3A^{1/3}}{2^{2/3}}q^{-4/3}.
\]

Using `A=pi^3/6`,

\[
\boxed{
E_{\mathrm{bal}}(q)
=
\frac{3\pi}{24^{1/3}}\,q^{-4/3}
}
\]

for the continuous envelope.

Because actual dyadic depth is integral and good `q` values occur on a convergent subsequence, the robust asymptotic statement is

\[
\boxed{
E_{\mathrm{balanced}}(q)=O(q^{-4/3})
}
\]

along available convergent scales after choosing the nearest dyadic depth to the balance point.

This is an error **upper-envelope law**, not a claim of universal lower-bound optimality over every conceivable native approximation algorithm.

## 7. Equivalent target-epsilon resource scaling

To achieve total error of order `epsilon` under the balanced two-source architecture, the ideal dyadic term requires roughly

\[
4^{-(n+1)}\asymp\epsilon,
\]

so

\[
2^{n+1}\asymp\epsilon^{-1/2}.
\]

Balancing the trace term then requires

\[
q\asymp\epsilon^{-3/4}
\]

along a good convergent scale.

Therefore the low-state native trace architecture has the indicative resource law

\[
\boxed{
\text{dyadic state order scale}\sim\epsilon^{-1/2},
\qquad
\text{trace denominator scale}\sim\epsilon^{-3/4}.
}
\]

The denominator exponent `3/4` is the joint consequence of quadratic Viète truncation in angular resolution and quadratic Diophantine convergence in trace slope.

## 8. Width-versus-magnitude tradeoff

The stationary exact-direction architecture from the sibling note has exact minimal state dimension

\[
D_n=2^{n-1}.
\]

At the balanced scalar-error depth,

\[
2^n\asymp\epsilon^{-1/2},
\]

so exact stationary projective direction representation uses state **width** of order

\[
D_n\asymp\epsilon^{-1/2}.
\]

By contrast the native trace approximation architecture keeps only a two-component trace but pays in integer **magnitude**, with good denominator scale

\[
q\asymp\epsilon^{-3/4}.
\]

These are different resource currencies and should not be compared as though one scalar “precision” measured both.

The meaningful tradeoff is:

- `GROWING_STATE`: exact ideal direction as a stationary integer projective attractor;
- `GROWING_MAGNITUDE`: low-dimensional native traces approximating the ideal direction;
- `ALGEBRAIC_READOUT`: exact nested-radical direction retained at G1 without rationalizing it into an integer trace at every depth.

## 9. Special n=2 improvement from the explicit Pell family

At `n=2`, the predecessor gives an explicit native recurrence

\[
(a_{k+1},b_{k+1})=(2a_k+b_k,a_k)
\]

with exact defect

\[
a_k^2-2a_kb_k-b_k^2=\pm1
\]

and exact slope error

\[
\left|\frac{b_k}{a_k}-(\sqrt2-1)\right|
=
\frac{\sqrt2-1}{a_k(a_k+(\sqrt2-1)b_k)}.
\]

So at the first irrational Viète layer the `q^-2` trace-error behavior is not merely supplied by general continued fractions; it has a canonical-looking explicit Pell-type certificate family derived from the integer coefficient `2` of the prior equal-component native trace.

Whether similarly structured exact certificate families exist at higher algebraic degrees is open.

## 10. Interpretation for #1158

The finite precision picture is no longer one-dimensional.

At least three precision coordinates are now separated:

1. `DYADIC_DEPTH` — how many ideal half-angle refinements have been performed;
2. `TRACE_SCALE` — how finely an irrational ideal direction is approximated by a native integer trace;
3. `RELATIONAL_STATE_DIMENSION` — how much stationary integer linear state is required if the ideal direction itself must be an exact projective attractor.

Thus Viète's nested radicals encode an ideal algebraic rotation-refinement tower, while actual discrete Cell/trace realization introduces a second native quantization scale whose interaction with dyadic depth has an explicit error budget.

This is a concrete precision-aware reinterpretation of the product, not a decimal approximation attached after the fact.

## 11. Next frontier

The current error budget uses generic continued-fraction convergents at each ideal depth. A stronger native theorem would derive the trace-approximation rule from Cell/trace dynamics itself.

The next discriminating question is whether the Cell geometry produces:

- Pell/continued-fraction-like low-state nonstationary approximants;
- growing-dimensional stationary integer state;
- or no canonical rationalization at all, leaving exact orientation only as a G1 algebraic readout.
