# RH rooted factorial resolvent and exact critical-depth tail

Status: `RESEARCH FRONTIER / EXACT FACTORIAL OPERATOR BOUND + DISCRETE CRITICAL-DEPTH LAW / NOT A PROOF OF RH`
Date: `2026-09-07`
Project: `Enterprise Math / 进取数论`
Researcher: `EM-RHHR-20260907`
Scope: `RH / rooted Volterra resolvent / Factor-BRC / factorial path suppression / critical depth`
Parents:

- `RH_ROOTED_VOLTERRA_SOURCE_RESOLVENT_20260907.md`
- `RH_BOUNDARY_PROFILE_CRITICAL_DEPTH_LAW_20260907.md`

## 0. Purpose and correction

The parent Volterra note obtained the coarse row-mass estimate

\[
\|\mathcal K\|_\infty\le\Lambda_X
\]

and hence a geometric-series contraction only when `t Lambda_X<1`.
That estimate ignores the most important BRC constraint: every successive
operator step must use a strictly larger prime label. Therefore an `r`-step
path is an unordered/distinct prime set after canonical ordering, and its
total mass has a factorial denominator.

This note proves the sharper bound

\[
\|\mathcal K^r\|_\infty
\le\frac{\Lambda_X^r}{r!},
\]

which removes the artificial `tau=1` barrier and extends the critical-depth
law from the limiting profile to the exact discrete Volterra resolvent.

The earlier geometric bound remains true but is nonsharp. Its apparent
`tau=1` threshold is a limitation of that certificate, not of the operator.

P000 remains unchanged. Operator power is composite Factor-BRC path depth,
not spatial dimension.

---

## 1. Exact path formula

For

\[
(\mathcal KF)(N,y)
=
\sum_{y<q\le N}
\frac{\lfloor N/q\rfloor}{N}
F(\lfloor N/q\rfloor,q),
\]

the parent note proved

\[
\begin{aligned}
(\mathcal K^rF)(N,y)
={}&
\sum_{\substack{y<q_1<\cdots<q_r\\q_1\cdots q_r\le N}}
\frac{\lfloor N/(q_1\cdots q_r)\rfloor}{N}
\\
&\times
F\!\left(
\left\lfloor\frac{N}{q_1\cdots q_r}\right\rfloor,q_r
\right).
\end{aligned}
\]

Every path has distinct, strictly increasing prime provenance. In particular,
there are no repeated-label words and no `r!` order multiplicity hidden in
the state.

---

## 2. Factorial operator bound

Let

\[
\Lambda_X(y)=\sum_{y<q\le X}\frac1q,
\qquad
\Lambda_X=\Lambda_X(1).
\]

Since

\[
\frac{\lfloor N/(q_1\cdots q_r)\rfloor}{N}
\le\frac1{q_1\cdots q_r},
\]

the path formula gives

\[
\begin{aligned}
|(\mathcal K^rF)(N,y)|
&\le\|F\|_\infty
\sum_{y<q_1<\cdots<q_r\le X}
\frac1{q_1\cdots q_r}.
\end{aligned}
\]

The sum is the `r`th elementary symmetric polynomial in the positive numbers
`1/q`. Expanding the `r`th power of their sum counts every distinct set
exactly `r!` times and adds repeated-label tuples. Therefore

\[
\sum_{q_1<\cdots<q_r}
\frac1{q_1\cdots q_r}
\le
\frac1{r!}\left(\sum_q\frac1q\right)^r.
\]

Hence

\[
\boxed{
\|\mathcal K^r\|_{\infty\to\infty}
\le\frac{\Lambda_X^r}{r!}.
}
\]

A local version with `Lambda_X(y)` also holds for paths starting at cutoff
`y`.

This is exactly the BRC gain lost by treating every stage as an arbitrary
future branch:

```text
STRICTLY_INCREASING_PRIME_PROVENANCE
-> ELEMENTARY_SYMMETRIC_MASS
-> FACTORIAL_SUPPRESSION.
```

---

## 3. Entire resolvent bound

The exact discrepancy equation is

\[
(I+t\mathcal K)E=-tQ.
\]

Because `K` is nilpotent, its inverse is a finite polynomial. Applying the
factorial bound gives, for every complex `t`,

\[
\begin{aligned}
\|(I+t\mathcal K)^{-1}\|_
{\infty\to\infty}
&\le
\sum_{r\ge0}
|t|^r\frac{\Lambda_X^r}{r!}
\\
&=e^{|t|\Lambda_X}.
\end{aligned}
\]

Therefore

\[
\boxed{
\|E\|_\infty
\le |t|e^{|t|\Lambda_X}\|Q\|_\infty.
}
\]

At the boundary scale

\[
t=\frac{\tau}{L_X},
\qquad
L_X=\log\frac{\log X}{\log Y},
\qquad
Y=(\log X)^2,
\]

we have `Lambda_X/L_X=1+o(1)`, so for every fixed bounded complex `tau`,

\[
\boxed{
\|E\|_\infty
\le
\frac{|\tau|e^{|\tau|+o(1)}}{L_X}
\|Q\|_\infty.
}
\]

There is no intrinsic resolvent threshold at `tau=1`.

Freeze:

```text
TAU_EQ_1_SUP_NORM_GEOMETRIC_BARRIER = SUPERSEDED_BY_FACTORIAL_PATH_BOUND
BOUNDED_TAU -> ENTIRE_FACTORIAL_RESOLVENT
```

This still controls only propagation of `Q`; it does not prove that the final
signed source functional is small.

---

## 4. Exact finite truncation tail

Let

\[
E^{(R)}
=-t\sum_{r=0}^{R}(-t\mathcal K)^rQ
\]

be the exact resolvent truncated after rooted face depth `R`. Then

\[
\boxed{
\|E-E^{(R)}\|_\infty
\le
|t|\|Q\|_\infty
\sum_{r>R}
\frac{(|t|\Lambda_X)^r}{r!}.
}
\]

This is a genuine finite discrete estimate. It does not pass through the
limiting `e^{-tau}` profile and does not assume moment convergence at growing
order.

For real or complex bounded `tau` and `t=tau/L_X`, the Poisson/factorial tail
is eventually comparable, on the logarithmic scale, to its first omitted
term:

\[
\sum_{r>R}
\frac{(|t|\Lambda_X)^r}{r!}
=
\frac{(|\tau|+o(1))^{R+1}}{(R+1)!}
\exp(O_\tau(1/R)).
\]

---

## 5. Exact discrete critical-depth exponent

Take

\[
R_X
=\alpha\frac{\log X}{\log\log X}
+o\!\left(\frac{\log X}{\log\log X}\right),
\qquad
\alpha>0.
\]

Stirling's formula gives

\[
\sum_{r>R_X}
\frac{(|t|\Lambda_X)^r}{r!}
=X^{-\alpha+o(1)}
\]

for every fixed nonzero bounded `tau`.

The one-step source is at most subpolynomial in the crude supremum norm:
for real `0<=t<=1`, both the discrete and continuum one-step masses are at
most `Lambda_X+O(1)`, so

\[
\|Q\|_\infty=X^{o(1)}.
\]

Also `|t|=X^{o(1)}`. Hence

\[
\boxed{
\|E-E^{(R_X)}\|_\infty
\le X^{-\alpha+o(1)}.
}
\]

In particular, absolute control of the unresolved exact discrete Volterra
tail at the square-root scale requires

\[
\boxed{
R_X\ge
\left(\frac12-o(1)\right)
\frac{\log X}{\log\log X}.
}
\]

This reproduces the critical depth from the earlier universal-profile
argument, now as a bound on the actual finite discrete operator tail.

---

## 6. Triple appearance of the same depth

The scale

\[
K_X\sim\frac12\frac{\log X}{\log\log X}
\]

now has three independent derivations inside the current route:

1. **Hildebrand/Kubilius cutoff depth:**
   `Y=(log X)^2` gives `log X/log Y` of this size;
2. **Factor-BRC state completeness:**
   arity above `K_X` has only square-root-scale population capacity;
3. **exact resolvent precision:**
   factorial path tail beyond `K_X` is at most
   `X^{-1/2+o(1)}`.

Thus `K_X` is simultaneously a population, provenance and numerical
precision threshold.

This is the strongest current reason to treat the critical depth as
structural rather than an arbitrary truncation parameter.

---

## 7. Geometric consequence for primes and composites

The factorial improvement depends on the exact geometry:

- a prime source is the zero-arm root;
- a semiprime contribution is one operator step;
- a three-prime contribution is two strictly ordered steps;
- an `r+1`-prime squarefree contribution is an `r`-step rooted simplex;
- path labels cannot repeat, so a rooted simplex appears once rather than in
  all `r!` orders.

Prime powers live in the exponent fiber and do not alter this distinct-label
factorial bound.

Hence the geometry of multifactor composites is not merely “more paths”.
Canonical prime ordering removes permutation redundancy and creates the
factorial decay that makes the full resolvent entire on bounded boundary
scales.

---

## 8. No-go boundary

The theorem closes the **high-arity propagation tail** by an absolute bound
once depth `K_X` is retained. It does not bound the first `K_X` layers or the
one-prime source pairing.

Therefore none of the following follows:

- `E` itself is `X^{-1/2}`;
- the centered square-root root-label functional is small;
- the prime-incidence discrepancy has RH strength;
- low layers cancel merely because high layers have factorial capacity;
- X6 fixed width alone proves the result.

Freeze:

```text
FACTORIAL_HIGH_DEPTH_TAIL_CONTROL
!=
LOW_DEPTH_SIGNED_SOURCE_CANCELLATION
```

The hard problem has now been localized to a finite but growing front block
of depths `0,...,K_X`.

---

## 9. Exact checker

Task-local checker:

`experiments/rh_rooted_factorial_resolvent_check.py`

It verifies with exact rational arithmetic on a finite state system:

- `||K^r||_infinity <= Lambda^r/r!`;
- nilpotence of the increasing-prime operator;
- the exact Neumann remainder is bounded by the factorial tail for an
  arbitrary rational source.

The checker is an algebraic regression certificate, not evidence for the
asymptotic depth law or RH.

---

## 10. New smallest unresolved unit

The full problem is now decomposed as

\[
\boxed{
\text{one-prime signed source}
\xrightarrow{\text{first }K_X\text{ rooted faces}}
\text{critical front block}
+
O(X^{-1/2+o(1)})\text{ high-depth tail}.
}
\]

The next admissible target is a fixed power saving for the **front block**
under the final square-root root-label observer.

Because the high-depth tail is already controlled, a successful theorem no
longer needs to handle infinitely many or all possible factor arities at
once. It must control a growing but explicit triangular block of size

\[
K_X\times\pi(Y)=X^{o(1)}
\]

while retaining quotient populations and prime labels.

A viable route may use the ordered-prime edge carrier or a weighted Hilbert
norm on this front block. Taking absolute values across its depth coordinate
would forfeit the remaining Möbius cancellation.

No RH proof is claimed.
