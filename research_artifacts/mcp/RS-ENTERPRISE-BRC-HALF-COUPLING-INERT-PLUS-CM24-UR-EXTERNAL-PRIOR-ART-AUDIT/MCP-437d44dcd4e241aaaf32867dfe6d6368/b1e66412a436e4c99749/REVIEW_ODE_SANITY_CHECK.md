# Bounded sanity check of the frozen quadratic proof, §§2–3

**BOUNDARY_PASS: no defect found in the operator identity or the stated finite mod-$p^2$ truncation argument.** This is a directed, shared-context, nonformal read-only check of §§2–3 only. It is not mathematical acceptance of the Task, UR, LIFT, a period-normal identification, or the remaining proof sections.

The complete frozen input was read and its bytes pinned: **CM24_QUADRATIC_MOD_P2_TASK_LIFT_PROOF.md**, 12379 bytes, SHA-256 **dbe74c73a06875332cf12e7d550eedbcacf9f9a46367c447e875347490ce5632**. The author's file was not edited. No provider query, remote write, registration, claim, native mutation, or new research unit was opened.

## Operator check

Set $q=4x(1-x)$, $q'=4(1-2x)$, and $q''=-8$. Independently applying the chain rule to the stated Hesse operator, the coefficients of $F''(q)$, $F'(q)$ and $F(q)$ are respectively

$$
x(1-x)(q')^2,\qquad
x(1-x)q''+(1-2x)q',\qquad
-\frac{2}{9}.
$$

Their differences from the coefficients of $4(\mathcal D_G F)(q)$ are all identically zero:

$$
x(1-x)(q')^2=4q(1-q),\qquad
x(1-x)q''+(1-2x)q'=4-6q,\qquad
-\frac29=4\left(-\frac1{18}\right).
$$

The zero coefficient term matters: the displayed identity holds as an operator pullback for an arbitrary formal $F$, before imposing its Gauss equation. The independent symbolic check records three exact zero residuals.

The Hesse coefficient recurrence follows from the coefficient of $x^n$:

$$
(n+1)^2c_{n+1}
 =\left(n^2+n+\frac29\right)c_n
 =\left(n+\frac13\right)\left(n+\frac23\right)c_n.
$$

Over $\mathbf Q$, this determines a formal solution uniquely from $c_0=1$. Since $q(0)=0$, $F(q)$ has that constant term, so the characteristic-zero identity follows. This uniqueness step is performed in characteristic zero, not by dividing by $(n+1)^2$ after reducing modulo $p$.

## Valuation and finite cutoff check

Assume $p$ is prime and $p=6m+1$, so $m\ge1$ and $p\ge7$. For $0\le n<p$, all factorial denominators and the constants 3 and 6 are $p$-units.

For $0\le j<n<p$, the numerator progression $6j+1$ is below $6p$. If it equals $rp$, then $r\equiv1\pmod6$, so the only possible positive $r<6$ is $r=1$: the factor is $p$ at $j=m$. Similarly, $3j+1<3p$ only permits the multiple $p$ at $j=2m$, and $3j+2<3p$ only permits $2p$ at $j=4m$. Each displayed factor has valuation exactly one. The index enters the rising factorial only when $n>j$, not at $n=j$.

Consequently the stated formulas are correct:

$$
v_p(a_n)=\mathbf1_{n>m}+\mathbf1_{n>2m},\qquad
v_p(b_n)=\mathbf1_{n>2m}+\mathbf1_{n>4m}.
$$

Modulo $p^2$, the effective degrees are therefore at most $2m$ for the Gauss polynomial and $4m$ for the Hesse polynomial. After composing the former with the degree-2 $q$, its effective degree is at most $4m<p$ as well.

For each $k<p$, the characteristic-zero coefficient of $x^k$ in $F(q(x))$ only depends on Gauss indices $n\le k$, because $q$ has order one at zero. Both finite polynomials through index $p-1$ retain every term needed for this coefficient. These coefficients are exactly equal over $\mathbf Q$, and their finite inputs belong to $\mathbf Z_{(p)}$.

For $k\ge p$, both effective polynomials have zero coefficient modulo $p^2$, since $k>4m$. This covers the entire degree range up to $2p-2$. No integrality statement about an infinite hypergeometric tail with $n\ge p$, and no exchange between an infinite tail and reduction, is needed.

## Scope boundaries

The check depends on the prime and residue-class hypothesis, the finite index range $n<p$, the exact parameters stated in §§1–3, and the stated precision $p^2$. It does not certify a uniform polynomial identity modulo $p^3$, evaluate a Task lift, verify the later division/derivative/period claims, or validate native authority metadata.

Machine-readable frozen-input pin and exact symbolic residuals are saved in **ODE_SANITY_CHECK.json**. This bounded check is ready for handoff; the author files and current research scope remain unchanged.
