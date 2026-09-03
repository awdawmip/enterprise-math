# Finite Cayley half-turn certificates and a target-free two-sided period squeeze

Status: `FREE_RESEARCH / EXACT FINITE BRIDGE + STANDARD CONTINUOUS LIMIT / NOT FOUNDATION`  
Date: `2026-09-03`  
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`  
Author/program signature: `YUAN X / Enterprise Math`

## 1. Setup

Let the chirality-selected rotation algebra be

\[
A_J=\mathbf R[J]/(J^2+1).
\]

Let the forward dyadic root tower satisfy

\[
U_1=J,
\qquad
U_{n+1}^2=U_n,
\]

and write

\[
U_n=c_n+s_nJ,
\qquad
c_n^2+s_n^2=1,
\qquad
s_n>0.
\]

The normalized-bisector construction gives

\[
c_{n+1}=\sqrt{\frac{1+c_n}{2}}
\]

and

\[
s_n=2c_{n+1}s_{n+1}.
\]

All finite values are generated without inserting the numerical value of classical `pi`.

## 2. Exact Cayley coordinate of each root

Define

\[
\tau_n=\frac{s_n}{1+c_n}.
\]

The unit relation implies the exact cross-multiplied identity

\[
\bigl((1+c_n)-s_nJ\bigr)U_n
=(1+c_n)+s_nJ.
\]

Consequently

\[
\boxed{
U_n=\frac{1+J\tau_n}{1-J\tau_n}
=:\mathcal C(\tau_n).
}
\]

Thus every dyadic root state is simultaneously an exact Cayley state.

Since

\[
U_n^{2^n}=-1,
\]

we obtain a finite Euler endpoint certificate at every depth:

\[
\boxed{
\left(\frac{1+J\tau_n}{1-J\tau_n}\right)^{2^n}=-1.
}
\]

No limiting exponential is needed for this identity.

## 3. Exact half-step law in Cayley coordinates

The Cayley composition law is

\[
\mathcal C(u)^2
=
\mathcal C\!\left(\frac{2u}{1-u^2}\right).
\]

Because `U_(n+1)^2=U_n`, the forward positive coordinates satisfy

\[
\boxed{
\tau_n=\frac{2\tau_{n+1}}{1-\tau_{n+1}^2}.
}
\]

In particular,

\[
0<\tau_{n+1}<\frac{\tau_n}{2}.
\]

The first values are

\[
\tau_1=1,
\qquad
\tau_2=\sqrt2-1,
\]

followed by the usual nested half-phase defects. These are produced by the finite root law, not selected by inverse trigonometry.

## 4. A target-free two-sided completion interval

Define the lower and upper period readouts

\[
P_n=2^n s_n,
\]

\[
Q_n=2^{n+1}\tau_n
=\frac{2P_n}{1+c_n}.
\]

### Lower monotonicity

Using `s_n=2c_(n+1)s_(n+1)`,

\[
\frac{P_{n+1}}{P_n}
=\frac1{c_{n+1}}>1.
\]

Therefore

\[
P_1<P_2<P_3<\cdots.
\]

### Upper monotonicity

Using the Cayley half-step law,

\[
\frac{Q_{n+1}}{Q_n}
=1-\tau_{n+1}^2<1.
\]

Therefore

\[
Q_1>Q_2>Q_3>\cdots.
\]

### Pointwise squeeze

Since `c_n<1`,

\[
\frac{Q_n}{P_n}=rac2{1+c_n}>1.
\]

Thus

\[
\boxed{P_n<Q_n.}
\]

Moreover `c_n -> 1`, so

\[
\frac{Q_n}{P_n}\longrightarrow1.
\]

It follows that both sequences converge to the same finite positive constant:

\[
\boxed{
L=\lim_{n\to\infty}P_n
=\lim_{n\to\infty}Q_n.
}
\]

This is a target-free definition of the completed half-period scale.

The initial upper value is exact:

\[
Q_1=4.
\]

Hence

\[
\boxed{2<L<4.}
\]

## 5. Exact finite interval width

The difference between the Cayley upper readout and the antisymmetric lower readout is

\[
\begin{aligned}
Q_n-P_n
&=P_n\left(\frac2{1+c_n}-1\right)\\
&=P_n\frac{1-c_n}{1+c_n}\\
&=P_n\tau_n^2.
\end{aligned}
\]

Therefore

\[
\boxed{
0<L-P_n<Q_n-P_n=P_n\tau_n^2.
}
\]

Because `tau_(n+1)<tau_n/2` and `Q_1=4`, this immediately gives a geometric finite certificate; for example,

\[
Q_n-P_n<\frac{16}{4^n}.
\]

Thus every finite root depth supplies a completely target-free interval

\[
\boxed{P_n<L<Q_n}
\]

whose width decays at least quadratically under one dyadic refinement.

## 6. The finite-to-exponential bridge

Put

\[
L_n=Q_n=2^{n+1}\tau_n.
\]

Then the finite half-turn certificate can be rewritten as

\[
\boxed{
\left(
\frac{1+J L_n/2^{n+1}}
     {1-J L_n/2^{n+1}}
\right)^{2^n}
=-1.
}
\]

Since `L_n -> L`, this is an exact sequence of norm-one rational/Cayley compositions whose step size tends to zero while the accumulated endpoint remains reversal.

The standard Cayley-to-exponential limit is

\[
\lim_{N\to\infty}
\left(
\frac{1+Jx/(2N)}{1-Jx/(2N)}
\right)^N
=e^{Jx}.
\]

Taking `N=2^n` and `x=L_n`, continuity of this standard limit gives

\[
\boxed{e^{JL}=-1.}
\]

Thus the exponential endpoint is not postulated. It is the continuous completion of the finite exact half-turn certificates.

## 7. Identification with classical pi

The finite construction defines `L` before any classical trigonometric decoder. Under the standard identification of `J` with the usual complex unit and of `exp(Jx)` with the unit-speed complex exponential, the least positive half-period is classical `pi`.

The forward short-root tower selects the first winding, and the target-free squeeze already gives `0<L<4`. Therefore

\[
\boxed{L=\pi.}
\]

Equivalently,

\[
P_n<\pi<Q_n,
\]

where both bounds were generated without using `pi` as input.

## 8. Geometric reading

The completed chain is now

```text
C3 native right-turn representation
  -> G=I+R, six oriented directions and reversal
  -> H=(I+G)/sqrt(3), six directions interleaved with six gates
  -> J=H^3, Cell-radius-normalized chirality with J^2=-I
  -> native component segment as a spinor of its rotation character
  -> repeated normalized adjacency bisectors U_(n+1)^2=U_n
  -> exact Cayley coordinates tau_n
  -> finite identities C(tau_n)^(2^n)=-1
  -> target-free squeeze P_n < L < Q_n
  -> continuous Cayley composition exp(JL)=-1
  -> standard identification L=pi.
```

The role of `e` is therefore precise:

\[
\boxed{
 e\text{ denotes the continuous completion of repeated infinitesimal multiplicative transport.}
}
\]

It is not a spatial direction or an extra geometric axis.

## 9. Boundary

- The finite Cayley, root, squeeze, and endpoint identities are exact.
- The Cayley-to-exponential passage uses standard real/complex analysis.
- The character plane remains a derived rotation representation, not the primitive native metric plane.
- Only the first Cell/gate refinement has a one-step physical realization; deeper states are transition-history refinements unless separately realized.
- The result does not identify the spinor, tetrahedral residual, and paired-Pell `C2` classes as one object without a further intertwiner.

Freeze candidate:

`AC-EM-FREE-F6D046-EULER-FINITE-CAYLEY-SQUEEZE-V1`:

> The forward dyadic rotation roots admit exact Cayley coordinates whose finite powers equal endpoint reversal. Their antisymmetric and Cayley-scaled readouts form monotone lower and upper sequences with a common target-free limit. The continuous Cayley composition is the Euler exponential, and its internally selected first half-period is classical pi.
