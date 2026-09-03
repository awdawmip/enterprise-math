# Viète winding-memory depth -> certified scalar precision bits

Status: `FREE_RESEARCH / EXACT FINITE PRECISION-RESOURCE LAW / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`

## 1. Inputs already proved

The #1158 line has established two ingredients without using classical pi as the target value.

### Binary winding-resolution tower

At gate level

\[
G_m=C_{3\cdot2^m},
\]

the 2-primary coordinate records winding/process history modulo

\[
2^m.
\]

Thus level `m` carries `m` bits of binary winding-resolution state beyond the fixed coarse `C3` factor.

### Two-sided scalar completion interval

Using the target-free Viète recurrence, for radical depth `n>=1` define

\[
I_n=[\Pi_n^-,\Pi_n^+]
\]

with

\[
\Pi_n^-=2^{n+1}s_n,
\qquad
\Pi_n^+=\frac{2^{n+1}s_n}{c_n}.
\]

The intervals are nested, contain the intrinsic completion constant `Pi_rot`, and their widths

\[
W_n:=|I_n|
\]

satisfy

\[
\boxed{
\frac{W_{n+1}}{W_n}
=
\frac{c_n}{(1+c_n)(1+c_{n+1})}
<\frac14.
}
\]

The first nontrivial interval is

\[
I_1=[2\sqrt2,4],
\]

so

\[
W_1=4-2\sqrt2<2.
\]

## 2. Gate-depth indexing

The quarter-turn seed sits at gate level

\[
m=2\quad(C_{12}).
\]

The first nontrivial scalar interval `I_1` sits one refinement later at

\[
m=3\quad(C_{24}).
\]

Hence

\[
\boxed{n=m-2}
\]

for `m>=3`.

Write the gate-indexed interval as

\[
J_m:=I_{m-2}.
\]

## 3. Exact finite width bound

Iterating the strict one-quarter contraction from `W_1<2` gives, for `n>=1`,

\[
W_n
<
2\left(\frac14\right)^{n-1}.
\]

Therefore

\[
W_n<2^{-2n+3}.
\]

Substitute

\[
n=m-2.
\]

Then for every `m>=3`,

\[
\boxed{
|J_m|
<
2^{7-2m}.
}
\]

This is an intrinsic finite precision certificate generated entirely from the radical/gate state.

No classical pi value is used in the bound.

## 4. Certified binary scalar bits from m winding bits

Say an interval certifies `b` binary absolute precision bits when its width is strictly below

\[
2^{-b}.
\]

The gate-level bound gives

\[
|J_m|<2^{-(2m-7)}.
\]

Hence level `m` certifies at least

\[
\boxed{b_m=2m-7}
\]

binary absolute precision bits for `m>=4`.

More generally use `max(0,2m-7)` if a nonnegative count is desired at startup levels.

Thus the finite state-resource law is

\[
\boxed{
\text{m binary winding-resolution bits}
\Longrightarrow
\text{at least }2m-7\text{ certified scalar bits}.
}
\]

This is a statement about this special deterministic completion constant; it is not a claim that one arbitrary information bit encodes two arbitrary bits of data.

## 5. Required winding depth for a requested scalar precision

To guarantee interval width below

\[
2^{-b},
\]

it suffices that

\[
7-2m\le-b.
\]

Hence

\[
\boxed{
m\ge\left\lceil\frac{b+7}{2}\right\rceil.}
\]

Equivalently, in radical-depth indexing,

\[
\boxed{
n\ge\left\lceil\frac{b+3}{2}\right\rceil.}
\]

This matches the earlier nested-interval precision theorem.

## 6. Every extra winding bit buys more than two certified bits after startup

Because the exact interval-width ratio is strictly below `1/4`, every one-step binary gate refinement satisfies

\[
\boxed{
|J_{m+1}|<\frac14|J_m|.
}
\]

Therefore the number of certified binary absolute bits increases by **strictly more than two** whenever the current width itself is used as the certificate threshold.

As the refinement depth grows, the contraction ratio tends to

\[
\frac14,
\]

so the asymptotic gain tends to exactly two bits per added binary winding-resolution level.

## 7. State-count form

The number of finite gate states is

\[
M_m=3\cdot2^m.
\]

Since

\[
2^m=M_m/3,
\]

the crude finite bound becomes

\[
|J_m|
<
\frac{1152}{M_m^2}.
\]

The sharper asymptotic theorem already proves

\[
M_m^2(\Pi_{\rm rot}-\Pi_m)\to6\Pi_{\rm rot}^3
\]

and

\[
M_m^2|J_m|\to18\Pi_{\rm rot}^3.
\]

Thus the exact finite certificate and asymptotic law have the same quadratic state-count exponent.

## 8. Process-memory interpretation

The new feature is not the exponent `2` alone. It is what the finite-resolution resource means.

At level `m`, the native/process candidate does **not** store an `m`-bit binary approximation of a real angle. It stores winding history modulo

\[
2^m.
\]

The character/radical readout turns that relational resolution into a certified scalar interval.

Therefore the precision pipeline can be written

```text
m-bit winding/process memory
    -> C_{3*2^m} gate state
    -> finite character half-trace
    -> nested radical shell state
    -> target-free interval J_m
    -> >= 2m-7 certified scalar bits
```

This is a concrete realization of finite precision as endogenous state structure rather than an external decimal error bar.

## 9. Width versus algebraic-state complexity

A separate #1158 theorem proves that if the exact ideal gate direction at level `m` must instead be realized as a fixed stationary integer/rational linear projective attractor, the minimum state dimension is

\[
D_m=2^{m-3}=M_m/24.
\]

Hence two very different resource architectures coexist:

### Winding-address architecture

Store one gate/process state using a binary depth parameter `m`; the precision state space has `2^m` sheets but one state label uses only `O(m)` binary information.

### Exact stationary-linear slope architecture

Store the exact ideal algebraic direction as a projective attractor; the required relational **dimension** itself grows like

\[
2^m.
\]

This sharpens the distinction between native finite-state precision and algebraic exact-direction representation.

## 10. Boundary

The theorem assumes the winding-mod-`2^m` process augmentation and the already-proved G1 scalar interval mechanism.

It does not prove that current P000 requires actual Cell rotation to retain winding history modulo powers of two.

Thus the finite precision-resource law is exact conditional on that minimal process-memory architecture, while the native effectivity/selection of the architecture remains open.
