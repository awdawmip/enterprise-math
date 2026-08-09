# P022 — Central-Binomial Triangular Pivots and the Remaining Franel Completion Problem

Status: `ACTIVE RESEARCH NOTE / STRUCTURAL PARTIAL EXPLANATION`  
Owner: `program/p022-geometry-v2`  
Depends on: low-order `J_1,J_2,J_3` identifiability certificate through segment length 150  
Prior-art boundary: prime divisibility of binomial coefficients and p-adic valuation tools are classical

## 1. The determinant growth is not entirely mysterious

The current finite certificate proves joint multiplicative independence of

\[
(A_\ell,F_\ell),
\qquad1\le\ell\le150,
\]

where

\[
A_\ell=\binom{2\ell}{\ell},
\qquad
F_\ell=\sum_j\binom{\ell}{j}^3,
\]

with the hidden-tail generator adjoined.

The rank extension alternates between `A`-valuation rows and `F_3`-valuation rows.  A large subset of the `A` pivots has an exact structural explanation.

---

## 2. P022-LI10 — prime `2n-1` gives an automatic new central-binomial pivot

Suppose

\[
p=2n-1
\]

is prime.

For every earlier segment length `m<n`,

\[
2m\le2n-2<p.
\]

Hence `p` cannot divide any factorial appearing in

\[
A_m=\frac{(2m)!}{m!^2},
\]

so

\[
\boxed{
v_p(A_m)=0\qquad(m<n).}
\]

At segment length `n`, we have

\[
n<p<2n.
\]

Therefore `p` occurs exactly once in `(2n)!` and not at all in `n!`, giving

\[
\boxed{
v_p(A_n)=1.}
\]

Thus the row

\[
\boxed{v_{2n-1}(A_\ell)}
\]

has zeros on every earlier segment column and a `1` in column `n`.

It is therefore an automatic triangular pivot for the new generator.

---

## 3. Infinitely many segment lengths are automatically separated

Every odd prime `p` can be written uniquely as

\[
p=2n-1
\]

with

\[
n=(p+1)/2.
\]

Since there are infinitely many primes, LI10 supplies infinitely many segment lengths at which the central-binomial moment alone contributes a fresh valuation direction.

Therefore any failure of global joint identifiability cannot come from a permanent exhaustion of new valuation information.

At infinitely many indices the `M_2` factor already provides a one-step triangular separator independently of the Franel factor.

---

## 4. Match with the finite certificate

Many `A` rows selected by the length-150 determinant are exactly of this form:

\[
\begin{array}{c|c}
 n & 2n-1\\
\hline
69&137\\
70&139\\
75&149\\
76&151\\
79&157\\
82&163\\
84&167\\
87&173\\
90&179\\
91&181\\
96&191\\
97&193\\
99&197\\
100&199\\
106&211\\
112&223\\
114&227\\
115&229\\
117&233\\
120&239\\
121&241\\
126&251\\
129&257\\
132&263\\
135&269\\
136&271\\
139&277\\
141&281\\
142&283\\
147&293
\end{array}
\]

Each corresponding prime is exactly `2n-1`, so the row is a literal new-column pivot before any interaction with later columns.

This explains a substantial part of the observed rank growth without numerical linear-algebra mystery.

---

## 5. The real unresolved structure is the composite `2n-1` defect set

If `2n-1` is composite, LI10 gives no new prime row of that triangular form.

Yet the finite certificate through 150 still gains rank at every such tested index, typically by a Franel valuation row and occasionally by another central-binomial row whose independence is global rather than strictly triangular.

So the global problem can be sharpened:

> **Franel defect-completion problem.**  Show that whenever the simple central-binomial triangular pivot is unavailable, the joint valuation surface still supplies a new direction; or characterize the first index where it does not.

This is more precise than the original undifferentiated multiplicative-independence question.

The certificate now has two conceptual layers:

\[
\boxed{
\text{automatic prime pivots from }A_n
+
\text{defect completion from joint }(A_n,F_n)\text{ valuations}.
}
\]

---

## 6. What would constitute a global proof

Several routes could complete the theorem:

1. prove an appropriate primitive/divisibility property for the Franel factors on the composite-`2n-1` defect set;
2. find a broader p-adic triangular rule not requiring a primitive prime;
3. prove directly that the infinite joint valuation columns are linearly independent;
4. derive a contradiction from the Franel recurrence or congruence structure for any hypothetical finite-support multiplicative relation.

The current targeted literature search found substantial work on Franel congruences and p-adic properties but no directly matching global theorem of the required form.  This is a search status, not a novelty claim.

---

## 7. Research consequence

Mechanical determinant extension above 150 remains useful as a pressure test, but the high-leverage frontier is now the composite-index completion mechanism.

Thus the current low-order program should proceed as

\[
\boxed{
\text{finite certificate}
\to
\text{identify automatic pivots}
\to
\text{isolate defect indices}
\to
\text{prove Franel/joint completion or find counterexample}.
}
\]

This turns the certificate from a large computation into a guide for the next number-theoretic theorem.
