# P025 Supplement 83 — Cyclotomic Divisor-Lattice Carrier and Exact Overlap Correction

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-cyclotomic-stage76`  
Depends on: P025 Supplements 79, 82  
Hard block: `NONE`

## 1. Stage 82 changes the state object

Stage 79 showed that for an odd prime exponent one nonlinear cyclotomic factor is enough to carry the future query:

> does threshold-one projective activation force repeated nonlinear support?

Stage 82 proves that this state is insufficient for composite exponents. At exponent four, the difference branch can activate while the top `Phi_4` factor remains squarefree.

The correct next object must retain the **sign-specific cyclotomic divisor lattice** rather than one chosen top factor.

## 2. P025-D26 — sign-specific cyclotomic index sets

For integer exponent

\[
n\ge2,
\]

define

\[
\boxed{
I_-(n):=\{d:d\mid n\},
}
\]

and

\[
\boxed{
I_+(n):=\{d:d\mid2n,\ d\nmid n\}.
}
\]

Then the standard homogeneous cyclotomic factorizations are

\[
\boxed{
p^n-q^n=\prod_{d\in I_-(n)}\Phi_d(p,q),}
\]

and

\[
\boxed{
p^n+q^n=\prod_{d\in I_+(n)}\Phi_d(p,q).}
\]

Examples:

\[
I_-(3)=\{1,3\},
\qquad
I_+(3)=\{2,6\},
\]

\[
I_-(4)=\{1,2,4\},
\qquad
I_+(4)=\{8\},
\]

and

\[
I_-(9)=\{1,3,9\},
\qquad
I_+(9)=\{2,6,18\}.
\]

These index sets are the combinatorial skeleton of the carrier state.

## 3. Layer values need not be coprime

Write

\[
F_d:=\Phi_d(p,q).
\]

A false simplification would be

\[
m\!\left(\prod_dF_d\right)
\stackrel{?}{=}
\prod_dm(F_d).
\]

This fails whenever a prime occurs in more than one cyclotomic layer.

The overlap is not a nuisance to ignore. It is an exact extra carrier.

For every prime `r` dividing at least one selected layer, let

\[
t_r:=\#\{d\in I_\pm(n):r\mid F_d\}.
\]

Define

\[
\boxed{
\Delta_\pm(n;p,q)
:=
\prod_r r^{t_r-1}.
}
\]

Equivalently,

\[
\boxed{
\Delta_\pm
=
\frac{\prod_{d\in I_\pm(n)}\operatorname{rad}(F_d)}
{\operatorname{rad}(p^n\pm q^n)}.
}
\]

This is the **cyclotomic overlap correction**.

## 4. P025-T172 — exact residual carrier decomposition

Since

\[
p^n\pm q^n=\prod_dF_d,
\]

we have

\[
\begin{aligned}
m(p^n\pm q^n)
&=
\frac{\prod_dF_d}{\operatorname{rad}(p^n\pm q^n)}\\
&=
\frac{\prod_d\operatorname{rad}(F_d)}
{\operatorname{rad}(p^n\pm q^n)}
\prod_d\frac{F_d}{\operatorname{rad}(F_d)}.
\end{aligned}
\]

Therefore

\[
\boxed{
m(p^n\pm q^n)
=
\Delta_\pm(n;p,q)
\prod_{d\in I_\pm(n)}m(F_d).
}
\]

This identity is completely exact and requires no pairwise-coprimality assumption.

For the equal-exponent projective atom,

\[
\boxed{
\rho_{n,\pm}
=
\frac{\Delta_\pm\prod_dm(F_d)}
{n(p+q)}.
}
\]

Thus projective pressure lives on two resources:

1. within-layer multiplicity `m(F_d)`;
2. cross-layer support reuse `Delta`.

## 5. Earlier formulas become special cases

### Odd prime exponent

For prime `ell`, the carrier has only two layers. The overlap correction is precisely the exceptional exponent-prime factor already seen in Stage 79.

For example, in the cube sum

\[
11^3+13^3,
\]

the layers are

\[
\Phi_2=24,
\qquad
\Phi_6=147=3\cdot7^2.
\]

Prime three occurs in both layers, so

\[
\Delta=3.
\]

Then

\[
m(11^3+13^3)
=3\,m(24)m(147)
=3\cdot4\cdot7
=84.
\]

### Fourth-power difference

For

\[
23^4<41^4,
\]

the layers are

\[
\Phi_1=18,
\qquad
\Phi_2=64,
\qquad
\Phi_4=2210.
\]

Prime two occurs in all three layers, so

\[
\boxed{\Delta=2^{3-1}=4.}
\]

The top layer is squarefree, but

\[
\Delta\,m(\Phi_1)m(\Phi_2)
=4\cdot3\cdot32
=384
\]

already exceeds the projective denominator

\[
4(41+23)=256.
\]

This is exactly why top forcing fails.

## 6. P025-D27 — selected carrier and outside carrier

Let

\[
U\subseteq I_\pm(n)
\]

be a nonempty set of cyclotomic layers whose repetition we want to test.

Define the selected residual product

\[
\boxed{
R_U:=\prod_{d\in U}m(F_d),
}
\]

and the outside carrier

\[
\boxed{
K_U:=
\Delta_\pm
\prod_{d\notin U}m(F_d).
}
\]

Then P025-T172 becomes

\[
\boxed{
m(p^n\pm q^n)=K_U R_U.}
\]

This is an exact two-block compression of the full divisor-lattice carrier.

## 7. P025-T173 — exact forcing-margin criterion

Fix a projective threshold

\[
T>0.
\]

Suppose

\[
\rho_{n,\pm}\ge T.
\]

Then

\[
K_U R_U
\ge
Tn(p+q).
\]

Therefore, if

\[
\boxed{
K_U<Tn(p+q),
}
\]

one necessarily has

\[
R_U>1.
\]

Equivalently,

\[
\boxed{
\rho_{n,\pm}\ge T
\quad\text{and}\quad
K_U<Tn(p+q)
\Longrightarrow
\exists d\in U:\ F_d\text{ nonsquarefree}.
}
\]

This is the exact **forcing-margin criterion**.

It does not claim that `K_U` is small. It tells us precisely what must be bounded in order to justify a future-safe collapse to the selected layers.

## 8. Prime exponent versus composite exponent

Choose `U` to be the maximal cyclotomic index.

For an odd prime exponent `ell`, Stage 79 proves universally that the outside carrier is too small to reach threshold one by itself. Therefore top repetition is forced.

For composite exponents, proper divisor layers may already carry enough pressure.

The distinction is structural:

\[
\boxed{
\text{prime exponent: shallow divisor carrier}
\qquad
\text{vs.}
\qquad
\text{composite exponent: inheritable lower-layer carrier}.
}
\]

## 9. P025-C25 — odd composite exponents also destroy top forcing

Exponent nine proves that the Stage-82 phenomenon is not an even-parity accident.

### Ninth-power difference

Take

\[
(q,p)=(23,71).
\]

Then

\[
I_-(9)=\{1,3,9\}.
\]

The layers are

\[
\Phi_1=48,
\]

\[
\Phi_3=3\cdot7^4,
\]

and

\[
\Phi_9
=3\cdot811\cdot54501859.
\]

The top `Phi_9` layer is squarefree.

Prime three occurs in all three layers, so

\[
\Delta=3^2.
\]

Nevertheless

\[
\boxed{
\rho_{9,-}=\frac{1372}{47}>1.
}
\]

All top residual is zero; the pressure is inherited from the proper-divisor layers `Phi_1,Phi_3` plus their overlap correction.

### Ninth-power sum

Likewise, with

\[
(q,p)=(11,13),
\]

\[
I_+(9)=\{2,6,18\},
\]

and

\[
\Phi_{18}
=3\cdot19\cdot73\cdot883
\]

is squarefree, while

\[
\boxed{
\rho_{9,+}=\frac76>1.
}
\]

Again the repeated pressure already lives in the lower cube layer `Phi_6`, with prime three shared across all three layers.

Therefore:

\[
\boxed{
\text{oddness does not rescue top forcing; primality of the exponent was the shallow case.}
}
\]

## 10. Precision interpretation

The carrier state now has three layers of precision:

\[
\boxed{
\text{index precision}
\to
\text{within-layer residual precision}
\to
\text{cross-layer overlap precision}.
}
\]

A top-factor-only quotient discards the last two whenever pressure can be inherited from proper divisor layers.

The forcing-margin criterion says exactly when such a collapse is safe for the future query "must this selected layer repeat?": it is safe only after the outside carrier has been proved below the threshold budget.

This is a much sharper instance of task-relative quotient safety than the original top-factor heuristic.

## 11. Prior-art / novelty discipline

Cyclotomic factorizations and radical identities are classical. The formula for `Delta` is an elementary exact re-accounting.

P025 does not claim those ingredients individually.

The project-side candidate is the use of the overlap-corrected divisor-lattice residual as the exact pressure carrier, the selected/outside carrier split, and its forcing-margin semantics for projective precision routing. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 12. Executable assets

Added:

- `src/enterprise_math/abc_cyclotomic_divisor_carrier.py`;
- `tests/test_abc_cyclotomic_divisor_carrier.py`.

The executable layer computes homogeneous cyclotomic values recursively, verifies the sign-specific factorization, derives `Delta` both from support counts and the radical quotient, checks the exact residual decomposition, and reproduces the prime-exponent, fourth-power, and ninth-power forcing/counterforcing fixtures.

## 13. Next frontier

No hard block exists. Continue with:

1. study the overlap correction `Delta` itself: determine how much of it is forced purely by the exponent divisor lattice rather than the prime values;
2. compress proper-divisor inheritance recursively — a composite-exponent hard state may be a lifted hard state from a proper exponent;
3. define a minimal carrier antichain: discard cyclotomic layers that provably cannot alter the chosen future query;
4. test whether `rho_{n,sign}` has exact inheritance laws along exponent divisibility `m|n`;
5. relay the forcing-margin semantics to P023/A2 only after the inheritance law is resolved.
