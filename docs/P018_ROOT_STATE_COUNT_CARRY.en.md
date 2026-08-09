# P018 — Exact Ternary Quotient-Root State-Count Carry

Status: `DISCOVERY / NONCANONICAL`  
Scope: exact cardinality of the positive quotient-root observation states for one fixed integer state  
Depends on: P018 exact denominator fibers, graded coalescence horizon, integer roots  
Discipline: integer-only. Classical floor-quotient block decomposition and Bernoulli inequalities are prior art; no priority claim is made for those ingredients.

## 1. Setup

Fix

\[
n\ge1,\qquad r\ge1,
\]

and consider the observation

\[
\phi_{n,r}(d)=R_r\!\left(\left\lfloor\frac nd\right\rfloor\right),
\qquad 1\le d\le n.
\]

Let \(N_r(n)\) be the number of distinct **positive** values taken by \(\phi_{n,r}\).

The earlier P018 root-state atlas defines

\[
H=H_r(n)=R_{r+1}(rn-1),
\qquad
D=\left\lfloor\frac{n}{(H+1)^r}\right\rfloor.
\]

The denominator axis has two exact charts:

- \(1\le d\le D\): roots are \(>H\) and pairwise distinct;
- \(d>D\): roots are \(\le H\); every \(1,\ldots,H-1\) occurs, while \(H\) contributes one optional boundary bit.

Hence, for \(H\ge1\),

\[
N_r(n)=D+H-1+\kappa,
\qquad \kappa\in\{0,1\}.
\]

The present note compresses the remaining pair \((D,\kappa)\) into one exact three-valued carry.

## 2. Three-point denominator band

Put

\[
q=\left\lfloor\frac Hr\right\rfloor.
\]

Then

\[
\boxed{\max(0,q-1)\le D\le q+1.}
\]

### Upper bound

The definition of \(H\) gives

\[
rn-1<(H+1)^{r+1}.
\]

Since both sides are integers,

\[
rn\le(H+1)^{r+1}.
\]

Because \(D(H+1)^r\le n\),

\[
rD(H+1)^r\le rn\le(H+1)^{r+1},
\]

and cancellation of the positive factor \((H+1)^r\) gives

\[
rD\le H+1.
\]

Therefore

\[
D\le\left\lfloor\frac{H+1}{r}\right\rfloor\le q+1.
\]

### Lower bound

If \(q=0\), the lower bound is automatic. Assume \(q\ge1\), so \(H\ge r\).

The discrete tangent/Bernoulli bound

\[
(H+1)^r-H^r\le r(H+1)^{r-1}
\]

implies

\[
\begin{aligned}
H^{r+1}-(H-r)(H+1)^r
&=r(H+1)^r-H\bigl((H+1)^r-H^r\bigr)\\
&\ge r(H+1)^r-rH(H+1)^{r-1}\\
&=r(H+1)^{r-1}>0.
\end{aligned}
\]

Hence

\[
(H-r)(H+1)^r<H^{r+1}\le rn-1<rn.
\]

Since \(rq\le H\),

\[
r(q-1)\le H-r,
\]

so

\[
r(q-1)(H+1)^r<rn.
\]

The quantities are integral, hence

\[
(q-1)(H+1)^r\le n,
\]

and therefore \(D\ge q-1\).

Thus the coarse denominator threshold has only three possible adjacent values.

## 3. The lower exceptional band forces the horizon bit

If \(q>0\) and

\[
D=q-1,
\]

then the horizon root necessarily occurs.

Indeed \(rq\le H\), so

\[
rqH^r\le H^{r+1}\le rn-1<rn.
\]

Therefore

\[
qH^r<n,
\]

which implies

\[
\left\lfloor\frac n{H^r}\right\rfloor\ge q=D+1.
\]

Thus \(\kappa=1\). This dependency is exactly what prevents the binary horizon carry and the three-point \(D\)-band from creating six independent cases.

## 4. Exact ternary carry

Define

\[
A=\max\left\{q(H+1)^r,(q+1)H^r\right\},
\]

and

\[
B=(q+1)(H+1)^r.
\]

Then define

\[
\tau_r(n)=
\begin{cases}
0,&n<A,\\
1,&A\le n<B,\\
2,&n\ge B.
\end{cases}
\]

The exact state count is

\[
\boxed{
N_r(n)=H+q-1+\tau_r(n).
}
\]

### Proof by the three possible values of \(D\)

Because

\[
D=\left\lfloor\frac n{(H+1)^r}\right\rfloor,
\]

we have:

1. \(D=q-1\) exactly in the lower part before \(q(H+1)^r\); the previous section forces \(\kappa=1\), so \(N=H+q-1\).
2. \(D=q\) between the two adjacent denominator thresholds. In this middle band, \(\kappa=1\) exactly when \(n\ge(q+1)H^r\). Thus the transition to \(N=H+q\) occurs at the larger of \(q(H+1)^r\) and \((q+1)H^r\), namely \(A\).
3. \(D=q+1\) begins at \(B=(q+1)(H+1)^r\). At that point the state count becomes \(H+q+1\). The horizon bit is automatically present in the realized cases, but the formula needs only the already established exact atlas.

The exceptional \(H=0\) case is \(r=n=1\); then \(q=0\), \(A=0\), \(B=1\), \(\tau=2\), and the same formula gives \(N_1(1)=1\).

## 5. One-root cardinality band

Since \(\tau\in\{0,1,2\}\),

\[
\boxed{
N_r(n)\in
\left\{
H+\left\lfloor\frac Hr\right\rfloor-1,
H+\left\lfloor\frac Hr\right\rfloor,
H+\left\lfloor\frac Hr\right\rfloor+1
\right\}.
}
\]

Thus one \((r+1)\)-st integer root determines the exact cardinality up to one ternary boundary decision.

For fixed \(r\), because

\[
H=(rn)^{1/(r+1)}+O(1),
\]

we obtain the sharper asymptotic

\[
\boxed{
N_r(n)
=(r+1)r^{-r/(r+1)}n^{1/(r+1)}+O(1).
}
\]

This improves the earlier \(\Theta(n^{1/(r+1)})\) statement to a bounded additive error around the exact leading term.

For \(r=1\), this specializes to the familiar square-root-scale distinct floor-quotient decomposition. The P018 contribution under investigation is the integer-root compressed all-\(r\) packaging, its coalescence interpretation, and its relation to finite-precision state counts; historical novelty remains unverified.

## 6. Executable validation

`src/enterprise_math/p018_root_state_carry.py` implements both:

- the earlier binary horizon carry \(\kappa\);
- the new exact ternary count carry \(\tau\).

`tests/test_p018_root_state_carry.py` compares the ternary formula against the exact two-chart count over dense bounded grids, checks monotonicity within each horizon shell, and includes explicit witnesses for all three carry values.

## 7. Next formal target

The strongest economical Lean target is not the full cardinality theorem first. Formalize in this order:

1. the three-point band \(\max(0,q-1)\le D\le q+1\);
2. `D=q-1 -> horizon fiber present`;
3. the threshold characterization of \(\tau\);
4. the exact cardinality identity once a finite-set/cardinality owner interface is chosen.

This keeps arithmetic separate from finite-enumeration infrastructure and avoids duplicating the general carry cocycle machinery in `Precision/Carry.lean`.