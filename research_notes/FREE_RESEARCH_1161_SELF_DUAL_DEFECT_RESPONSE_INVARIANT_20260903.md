# Free Research #1161 — self-dual defect/response conservation and a discrete completion bridge

Status: `FREE_RESEARCH_RESULT / NEW FINITE INVARIANT / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent issue: `#1161`

## 1. Generalized initial aspect ratio

Consider the same AGM recursion with

\[
a_0=1,\qquad b_0=x,\qquad 0<x\le1,
\]

\[
a_{n+1}=\frac{a_n+b_n}{2},
\qquad
b_{n+1}=\sqrt{a_nb_n},
\]

and the Gauss–Legendre budget variables

\[
A_0=1,
\qquad
P_0=1,
\]

\[
A_{n+1}=A_n-P_n(a_n-b_n)^2,
\qquad
P_{n+1}=2P_n.
\]

Define the finite accumulated response channel

\[
J_0=0,
\]

\[
\boxed{
J_{n+1}=J_n+4P_nb_n(a_n-b_n).
}
\]

No derivative or continuum object is present in this definition.

## 2. Finite defect/response invariant

Define

\[
\mathcal K_n
:=
A_n-J_n-2P_n(a_n^2-b_n^2).
\]

Then

\[
\boxed{\mathcal K_{n+1}=\mathcal K_n.}
\]

Proof: write `a=a_n`, `b=b_n`, `U=a-b`, `P=P_n`. The next squared pair difference is

\[
(a_{n+1})^2-(b_{n+1})^2
=
\frac{(a+b)^2}{4}-ab
=
\frac{U^2}{4}.
\]

Therefore

\[
2P_{n+1}\bigl((a_{n+1})^2-(b_{n+1})^2\bigr)
=P U^2.
\]

Using the updates for `A` and `J`,

\[
\begin{aligned}
\mathcal K_{n+1}
&=A-PU^2-J-4PbU-PU^2\\
&=A-J-2P(U^2+2bU)\\
&=A-J-2P(a^2-b^2)\\
&=\mathcal K_n.
\end{aligned}
\]

At `n=0`,

\[
\mathcal K_0
=1-2(1-x^2)
=2x^2-1.
\]

Hence the exact invariant is

\[
\boxed{
A_n-J_n-2P_n(a_n^2-b_n^2)=2x^2-1.
}
\]

This is independent of the earlier cone invariant and the retired-defect budget invariant.

## 3. The standard Gauss–Legendre seed is exactly self-dual

For #1161,

\[
x=1/\sqrt2,
\qquad x^2=1/2.
\]

Therefore the invariant constant vanishes:

\[
\boxed{
A_n-J_n=2P_n(a_n^2-b_n^2).
}
\]

The right-hand side is strictly positive for every finite step and tends to zero because the AGM gap contracts double-exponentially while `P_n=2^n` grows only exponentially.

Thus

\[
\boxed{J_n<A_n}
\]

for finite `n`, and

\[
\boxed{A_\infty=J_\infty}.
\]

Since every response increment is positive,

\[
J_n\uparrow A_\infty,
\]

while the original budget recursion gives

\[
A_n\downarrow A_\infty.
\]

The exact finite squeeze width is

\[
\boxed{
A_n-J_n=2^{n+1}(a_n^2-b_n^2).
}
\]

This supplies a second finite certificate for the limiting normalization.

## 4. Response-sum formula for the endogenous completion constant

At the self-dual seed,

\[
J_\infty
=
4\sum_{n=0}^\infty 2^n b_n(a_n-b_n).
\]

Since `H_inf=2M`, where `M` is the common AGM limit,

\[
\Pi_*=\frac{H_\infty^2}{A_\infty}
=\frac{4M^2}{J_\infty}.
\]

Hence

\[
\boxed{
\Pi_*
=
\frac{M^2}{\displaystyle\sum_{n=0}^\infty 2^n b_n(a_n-b_n)}.
}
\]

This expression uses only the finite AGM orbit and its positive response increments.

## 5. Internal `tau` bridge in response form

The independent #1159 finite-rotation program defines the internal boundary-completion constant `tau`.

Therefore

\[
\boxed{
\Pi_*=\tau
\iff
\tau\sum_{n=0}^\infty 2^n b_n(a_n-b_n)=M^2.
}
\]

This is the current sharpest purely project-internal form of the remaining global completion problem.

It asks for an equality between

- the #1159 rotation boundary-completion scale `tau`;
- the #1161 accumulated discrete AGM response;
- the squared limiting AGM scale.

This is structurally closer to a transfer/Green/Wronskian pairing than the raw formula `A_inf*tau=H_inf^2`.

## 6. Relation to a finite variational/Wronskian identity

There is an optional derived interpretation that is not required for the invariant above.

Treat `a_n,b_n` as functions of the initial ratio `x` and set

\[
W_n=a_nb_n'-b_na_n'.
\]

Direct differentiation of one AGM step gives

\[
W_{n+1}=\frac{a_n-b_n}{4\sqrt{a_nb_n}}W_n.
\]

Induction yields

\[
\boxed{
x(1-x^2)W_n
=2^n a_nb_n(a_n^2-b_n^2).
}
\]

Also

\[
\frac{a_{n+1}'}{a_{n+1}}-rac{a_n'}{a_n}
=
\frac{W_n}{a_n(a_n+b_n)}.
\]

Combining the two identities gives

\[
J_n
=
4x(1-x^2)\frac{a_n'}{a_n}.
\]

Hence the finite invariant can equivalently be written

\[
\boxed{
A_n
=2x^2-1
+4x(1-x^2)\frac{a_n'}{a_n}
+2^{n+1}(a_n^2-b_n^2).
}
\]

At `x=1/sqrt(2)`, the constant term vanishes. If the standard smooth limit `a_n -> M(x)` is used, then

\[
A_\infty=2x\frac{M'(x)}{M(x)}
\]

at the self-dual point, and therefore

\[
\boxed{
\Pi_*
=\frac{2M(x)^3}{xM'(x)},
\qquad x=1/\sqrt2.
}
\]

The derivative form is a derived response interpretation. The primary finite invariant and response sum do not depend on differentiating the limiting function.

## 7. Updated invariant hierarchy for #1161

At current free-research-result strength, the AGM reconstruction now has three distinct exact finite invariants/conservation laws:

1. cone invariant:
   `H^2-U^2-V^2=0`;
2. retired defect budget:
   `A_n + sum_{k<n} P_k U_k^2 = 1`;
3. generalized defect/response invariant:
   `A_n-J_n-2P_n(a_n^2-b_n^2)=2x^2-1`.

At the standard self-dual seed, invariant 3 becomes zero-defect balance and yields `A_inf=J_inf`.

## 8. Scope boundary

Freeze only at free-research-result strength:

`FINITE_DEFECT_RESPONSE_INVARIANT = PROVED`.

`SELF_DUAL_SEED x^2=1/2 -> A_INFINITY=J_INFINITY = PROVED`.

`PI_STAR_RESPONSE_SUM_FORMULA = PROVED`.

`PI_STAR_EQUALS_TAU = OPEN`.

`TAU * AGM_RESPONSE_SUM = M^2 = EXACT_REMAINING_INTERNAL_BRIDGE`.

`CLASSICAL_ELLIPTIC_LEGENDRE_RELATION = NOT_USED_AS_PREMISE`.
