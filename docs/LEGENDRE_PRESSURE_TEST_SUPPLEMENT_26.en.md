# Legendre Pressure Test — Supplement 26

Status: `PROVED RESEARCH NOTE`  
Scope: complete relative repair spectrum of least-prime precision refined by cofactor-root precision  
Depends on: P017 L064, P023-S11 relative repair spectrum, P018 exact root threshold  
Discipline: this is a finite square-basin representation theorem. It does not prove Legendre's conjecture.

## 1. From a one-bit bound to the full repair spectrum

L064 proves that every least-prime shell meets at most two cofactor-root classes.

S11 says that a finite precision refinement is not characterized only by its worst repair alphabet; it has a complete relative repair spectrum.

In the present P017 specialization, the L064 binary bound forces that entire spectrum to terminate after order two.

## 2. Split-shell count

Let

\[
N_P(k)=|X/P|
\]

be the number of nonempty realized least-prime shells in the square basin.

For each such prime `p`, let

\[
r_p
\in\{1,2\}
\]

be the number of actual cofactor-root values realized inside that shell.

Define

\[
\boxed{
S(k)=\#\{p:r_p=2\}.
}
\]

Thus `S(k)` counts precisely the least-prime shells that genuinely require the nontrivial root-repair bit.

## 3. L067-A — Exact joint class count

Status: `PROVED`.

The joint `(factor,root)` precision has

\[
\sum_p r_p
\]

classes. Since every `r_p` is either one or two,

\[
\boxed{
|X/(P\cap R)|
=N_P(k)+S(k).
}
\]

Each unsplit shell contributes one joint class; each split shell contributes one additional class.

This is the exact global class-count refinement of L064.

## 4. L067-B — The complete relative repair spectrum is quadratic

Status: `PROVED`.

Apply S11 to the canonical quotient projection

\[
X/(P\cap R)
\longrightarrow
X/P.
\]

Its fiber sizes are exactly the `r_p` values.

Therefore

\[
\mathcal R_1
=
\sum_p r_p
=N_P+S,
\]

and

\[
\mathcal R_2
=
\sum_p\binom{r_p}{2}
=S,
\]

while

\[
\boxed{
\mathcal R_j=0
\qquad(j\ge3).
}
\]

Hence

\[
\boxed{
\mathcal R(P\leftarrow P\cap R)
=(N_P+S,\ S).
}
\]

The entire higher-order repair structure is determined by one additional integer `S(k)` beyond the number of factor shells.

## 5. L067-C — Repair generating polynomial

Status: `PROVED`.

The S11 generating polynomial is

\[
K(t)
=
\sum_p\big((1+t)^{r_p}-1\big).
\]

There are `N_P-S` unsplit shells and `S` split shells, so

\[
\begin{aligned}
K(t)
&=(N_P-S)t+S(2t+t^2)\\
&=(N_P+S)t+St^2.
\end{aligned}
\]

Thus

\[
\boxed{
K_{P\leftarrow P\cap R}(t)
=(N_P(k)+S(k))t+S(k)t^2.
}
\]

The coefficient of `t^2` is not an abstract collision statistic here: it exactly counts factor shells that need a second root state.

## 6. L067-D — Exact threshold / p-rough occupancy criterion for a split shell

Status: `PROVED`.

Fix prime `p` and write

\[
j_p
=R_2\!\left(\left\lfloor\frac{k^2}{p}\right\rfloor\right).
\]

The P018 upper-root threshold is

\[
\boxed{
q=(j_p+1)^2.
}
\]

Let the open exact cofactor window be

\[
W_p(k)=[A_p,B_p].
\]

The lower root `j_p` is actually realized by the least-prime shell exactly when there exists a `p`-rough integer

\[
q\in[A_p,\min(B_p,(j_p+1)^2-1)].
\]

The upper root `j_p+1` is actually realized exactly when there exists a `p`-rough integer

\[
q\in[\max(A_p,(j_p+1)^2),B_p].
\]

Therefore

\[
\boxed{
r_p=2}
\]

if and only if **both** adjacent threshold subwindows contain a `p`-rough quotient.

This is the exact realizability-filtered version of the P018 raw two-basin split condition.

## 7. L067-E — Uniform binary product slots and unused-code count

Suppose `S(k)>0`, so the global factor-to-root repair alphabet must contain two symbols.

A uniform factor-first product code then allocates

\[
2N_P
\]

formal `(factor,bit)` slots.

The actual joint precision uses only

\[
N_P+S
\]

of them. Therefore

\[
\boxed{
2N_P-(N_P+S)
=N_P-S.
}
\]

So the number of unused uniform binary code slots is exactly the number of **unsplit** least-prime shells.

This gives S18's unrealized-support defect a shell-by-shell number-theoretic interpretation.

If `S(k)=0`, the task-minimal alphabet has one symbol and there are no unused slots.

## 8. Examples

### k=11

\[
N_P=5,
\qquad
S=1,
\qquad
|X/(P\cap R)|=6.
\]

Thus

\[
\boxed{
\mathcal R=(6,1).
}
\]

### k=18

The split shells are

\[
\boxed{p=2,7}.
\]

Hence

\[
N_P=5,
\qquad
S=2,
\qquad
|X/(P\cap R)|=7,
\]

and

\[
\boxed{
\mathcal R=(7,2).
}
\]

### k=1737

The actual basin has

\[
N_P=157,
\qquad
S=7,
\qquad
|X/(P\cap R)|=164.
\]

The uniform binary factor-first product has `314` formal slots, of which

\[
\boxed{150=157-7}
\]

are unused because their factor shells do not actually need the upper repair digit.

## 9. New interpretation of P011's second collision coordinate

P011's second spectrum coordinate usually counts pairs of fine classes merged by a coarse map.

Here the canonical precision-forgetting projection has only fibers of size one or two. Consequently

\[
\boxed{
J_2(\pi_{P\cap R,P})=S(k).
}
\]

Thus a P011 irreversibility-spectrum coordinate becomes an exact arithmetic observable of the P017 shell geometry.

This is a direct theorem-level bridge, not merely analogous notation.

## 10. Consequence for state design

A universal one-bit field attached to every factor shell is sufficient but wasteful.

The exact represented state may instead use:

- no extra root repair on unsplit shells;
- one binary branch only on the `S(k)` split shells.

If a fixed rectangular storage format is required, S18 may still pack the uniform product and then rank only realized support. But at theorem level, the local split profile is the more precise state description.

## 11. Executable specification

- `src/enterprise_math/p017_factor_root_spectrum.py`
- `tests/test_p017_factor_root_spectrum.py`

The executable layer verifies the p-rough threshold criterion against direct realized root sets, pins the examples above, checks quadratic spectrum truncation, and confirms that unused uniform binary codes equal unsplit shells.

## 12. Tool feedback

The abstraction loop is now

\[
\boxed{
\text{P011 collision spectrum}
\to
\text{P023 relative repair spectrum}
\to
\text{P017 exact split-shell observable}.
}
\]

This is precisely the intended research pattern: a general tool returns to number theory as a new exact integer statistic rather than as terminology alone.
