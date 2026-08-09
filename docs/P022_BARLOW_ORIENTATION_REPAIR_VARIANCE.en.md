# P022 — Exact Second Moment of Orientation-Type Repair

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE SECOND MOMENT / ANALYTIC ASYMPTOTIC`  
Owner: `program/p022-geometry-v2`  
Depends on: excursion orientation repair; typed repair mechanism polynomial; Weyl-wall quotient interpretation  
Cross-route relevance: P018/P023/P024 uncertainty of event-driven repair budgets

## 1. Why a mean is not enough

The microscopic-average repair theorem proves

\[
\overline r_N=\Theta(\sqrt N).
\]

A first-moment tail bound then shows that linear repair has counting density zero.

That does **not** imply that repair is sharply concentrated around one deterministic multiple of `sqrt(N)`.

The Weyl-wall interpretation separates the total repair into two typed components:

- `E_N`: orientation bits released by zero-coordinate wall departures;
- `B_N`: side-label bits released by diagonal splits.

The orientation component already has an exact nonvanishing square-root-scale fluctuation.  This note derives it completely.

---

## 2. One-sided orientation repair is zero local time

For one labelled signed prefix walk

\[
S_t=\sigma_1+\cdots+\sigma_t,
\qquad\sigma_i\in\{-1,+1\},
\]

an orientation repair bit is born exactly when the absolute process leaves zero.

Through horizon `N`, this means the one-sided orientation count is

\[
\boxed{
L_N
=\sum_{j=0}^{m}
\mathbf1_{\{S_{2j}=0\}},
\qquad
m=\left\lfloor\frac{N-1}{2}\right\rfloor.
}
\]

The event at `j=0` is the initial departure from the origin.

Let

\[
p_j
=\Pr(S_{2j}=0)
=\frac{\binom{2j}{j}}{4^j}.
\]

The finite-counting interpretation is primary: `p_j` is simply the ratio of zero-return prefixes to all `2^(2j)` prefixes.

---

## 3. P022-OV01 — exact mean

The mean is

\[
\mathbb E L_N
=\sum_{j=0}^{m}p_j.
\]

Using the classical central-binomial partial-sum identity,

\[
\boxed{
A_N:=\mathbb E L_N
=(2m+1)rac{\binom{2m}{m}}{4^m}.
}
\]

This is the one-sided term already used in the repair-complexity theorem.

---

## 4. P022-OV02 — exact second moment

Write

\[
I_j=\mathbf1_{\{S_{2j}=0\}}.
\]

Then

\[
L_N^2
=\sum_iI_i
+2\sum_{i<j}I_iI_j.
\]

For `i<j`, the Markov decomposition of a walk that is zero at both times gives

\[
\Pr(I_i=1,I_j=1)
=p_i p_{j-i}.
\]

Therefore

\[
\mathbb E L_N^2
=A_N
+2\sum_{0\le i<j\le m}p_i p_{j-i}.
\]

Now use the generating function

\[
\sum_{j\ge0}p_jz^j
=(1-z)^{-1/2}.
\]

Squaring gives

\[
\left(\sum_{j\ge0}p_jz^j\right)^2
=(1-z)^{-1},
\]

so for every `s>=0`,

\[
\boxed{
\sum_{i=0}^{s}p_i p_{s-i}=1.
}
\]

Hence the triangular convolution sum satisfies

\[
\sum_{i=0}^{m}p_i\sum_{k=0}^{m-i}p_k
=m+1.
\]

Removing the diagonal contribution produces

\[
\boxed{
\mathbb E L_N^2
=2(m+1)-A_N.
}
\]

This is an exact rational identity.

---

## 5. P022-OV03 — exact variance

Subtract the square of the mean:

\[
\boxed{
\operatorname{Var}(L_N)
=2(m+1)-A_N-A_N^2.
}
\]

The two labelled Barlow sides are independent before the coordination quotient, so the total orientation repair

\[
E_N=L_N^{(1)}+L_N^{(2)}
\]

has

\[
\boxed{
\mathbb E E_N=2A_N,
}
\]

and

\[
\boxed{
\operatorname{Var}(E_N)
=2\left(2(m+1)-A_N-A_N^2\right).
}
\]

No approximation is used in these formulas.

---

## 6. P022-OV04 — orientation repair has horizon-linear variance

The standard central-binomial estimate gives

\[
A_N
=\sqrt{\frac{2N}{\pi}}+O(N^{-1/2}).
\]

Substituting into the exact variance gives

\[
\operatorname{Var}(L_N)
=\left(1-\frac2\pi\right)N+O(\sqrt N),
\]

and therefore

\[
\boxed{
\operatorname{Var}(E_N)
=2\left(1-\frac2\pi\right)N+O(\sqrt N).
}
\]

Thus

\[
\boxed{
\operatorname{sd}(E_N)=\Theta(\sqrt N).
}
\]

The orientation-repair standard deviation is the **same order** as its mean.

---

## 7. P022-OV05 — relative fluctuations do not vanish

The mean has leading term

\[
\mathbb E E_N
=2\sqrt{\frac{2N}{\pi}}+o(\sqrt N).
\]

Hence the coefficient of variation satisfies

\[
\frac{\sqrt{\operatorname{Var}(E_N)}}{\mathbb E E_N}
\longrightarrow
\boxed{
\frac{\sqrt{\pi-2}}{2}
}.
\]

Equivalently,

\[
\frac{\operatorname{Var}(E_N)}{(\mathbb E E_N)^2}
\longrightarrow
\boxed{
\frac{\pi-2}{4}
}.
\]

This limit is strictly positive.

Therefore even the orientation component alone does not become sharply concentrated relative to its own square-root mean scale.

---

## 8. What this does and does not prove about total repair

Since

\[
r_N=E_N+B_N,
\]

the orientation variance theorem proves that one typed component has nontrivial `sqrt(N)` fluctuations.

It does **not** by itself prove a closed variance formula or limiting law for the scalar total `r_N`, because the covariance between orientation events and diagonal-split events must be controlled separately.

So the current hierarchy is:

- exact total mean: proved;
- exact orientation variance: proved;
- exact total second moment: computable from the repair polynomial by derivatives;
- sharp total-variance asymptotic: still open.

This preserves the correct evidence boundary.

---

## 9. Precision consequence

The event-driven architecture should not replace a worst-case linear budget by one deterministic square-root budget and call the problem solved.

Even within one repair type,

\[
\boxed{
\text{mean}=\Theta(\sqrt N),
\qquad
\text{standard deviation}=\Theta(\sqrt N).
}
\]

So state provisioning must distinguish at least:

- mean repair load;
- repair distribution/tail;
- worst repair;
- repair mechanism type.

This is another concrete reason that precision is a structured future-state requirement, not one universal scalar.

---

## 10. Prior-art boundary

Simple random-walk return probabilities, central binomial coefficients, local times, Markov decompositions and their generating functions are established mathematics.

P022 does not claim those ingredients.

The project-specific result is their exact identification with the orientation component of the Barlow event-repair state and its placement inside the typed finite-precision architecture.

---

## 11. Executable assets

Added:

- `src/enterprise_math/p022_barlow_orientation_variance.py`;
- `tests/test_p022_barlow_orientation_variance.py`.

The tests verify the return-probability convolution identity, compare exact mean/second moment/variance against direct microscopic word enumeration on short horizons, and preserve the asymptotic limit as a derived analytic statement rather than a floating primitive.
