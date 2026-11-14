# R139B — Exact presence and final disappearance of the extremal two-one Sturmian word

Date: 2026-11-14 Asia/Shanghai. Status: AUTHOR-SIDE PROOF / NOT_REVIEWED.
Scientific scope: one-parameter external tied-phase S23 auxiliary observer only, **not a native X6 operation**. Frozen source pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessors: R137B exact Farey-gap correspondence; R138 modular criterion; R139.1 exact last failure per gap, in this research directory. All remain author-side mathematical results pending independent review.

## Definitions and theorem

For integers `m>=4, K>=2, L=K-1`, and `0<theta<1`, consider
```text
S_i^(K)(theta) = floor((L+i+1)*theta)-floor((L+i)*theta), 0<=i<m.
```
Let `w_m=10^(m-2)1` denote a length-m binary word with 1 in its first and last positions, and 0 in all intervening positions.

**R139B.1 (one division and remainder determine exact presence).** Write
`L=m*q+r`, `q=floor(L/m)`, `0<=r<m`. Then
```text
w_m in V(K,m)    <=>    2*q+r >= m-2.                (1)
```
In particular, w_m is absent exactly when `2*q+r<=m-3`. The same condition holds for the bitwise complementary word `0 1^(m-2) 0` using the complement symmetry already established in R136 (or the irrational theta -> 1-theta argument below). Membership is decidable by one integer quotient/remainder and one inequality, even for arbitrary-length K.

**R139B.2 (exact eventual coefficient of the extremal word).**
The largest integer `K>=2` for which w_m is absent is
```text
K_bad(m)=(m-2)*floor((m-1)/2).                        (2)
```
Thus the first coefficient from which w_m, and its complementary word, is permanently present equals
```text
K_ext(m)=(m-2)*floor((m-1)/2)+1.                     (3)
```
As both words belong to the full finite Sturmian language, the exact *complete-language* eventual threshold satisfies the unconditional lower bound
```text
K_eventual(m) >= (m-2)*floor((m-1)/2)+1, m>=4.       (4)
```
R136–R139 exact finite calculations show equality in (4) for every m=4,...,22. Whether equality holds for every m>=4 remains an **open conjecture**, not a theorem of this note.

## Proof of R139B.1

Take an open mechanical-word representation with slope alpha in (0,1) and intercept rho in (0,1). To obtain exactly w_m, the first step must cross 1, the next m-2 steps must not cross an integer, and the last step must cross 2. The strict interiors of these conditions are
```text
max(1-alpha, 2-m*alpha) < rho < min(1, 2-(m-1)*alpha).
```
A nonempty interval requires exactly `1/m<alpha<1/(m-2)`. For m>=4 these slopes comprise precisely **two** adjacent order-m Farey intervals separated by `1/(m-1)`:
```text
A:  1/m       < alpha < 1/(m-1),
    2-m*alpha < rho   < 1.
B:  1/(m-1)   < alpha < 1/(m-2),
    1-alpha   < rho   < 2-(m-1)*alpha.
```
The case of equality at a rational parameter contributes no new binary word because the original floor differences are right-continuous and locally constant immediately to the right of each boundary; this is also R137B's strict-gap completeness.

For tied-phase rho={L alpha}, apply R138's exact modular feasibility predicate to A and B.

For A, `(a,b,c,d,p,j,q_upper,k,D)=(1,m,1,m-1,2,m,1,0,m)`, hence `h=L mod m=r` and
```text
A infeasible  <=>  L+m <= (m-1)*(m-r).
```
Substitute `L=m*q+r`; this inequality is exactly
```text
q+r <= m-2.                                            (5)
```

For B, `(a,b,c,d,p,j,q_upper,k,D)=(1,m-1,1,m-2,1,1,2,m-1,m-1)`. Assume A infeasible, so q+r<=m-2. Then
```text
L=m*q+r=(m-1)*q+(q+r),
L mod(m-1) = q+r.
```
The B infeasibility criterion is therefore
```text
L+(m-1) <= (m-2)*((m-1)-(q+r)),
```
which simplifies to
```text
2*q+r <= m-3.                                          (6)
```
As (6) implies (5), **both** A and B are infeasible iff (6). Every w_m representation comes from A or B, so (1) follows. QED.

For complement symmetry, if theta is irrational then for every positive integer n, `floor(n*(1-theta))=n-1-floor(n*theta)`. Thus corresponding mechanical step words obey `S_i^(K)(1-theta)=1-S_i^(K)(theta)`. Each attainable word can be represented at an irrational theta because the word is constant on some open interval after removing its finitely many rational breakpoints. Hence w_m and its complement have the same presence status for all K.

## Proof of R139B.2

A missing coefficient must have `L=m*q+r>=1`, `q>=0`, `0<=r<m`, and `2q+r<=m-3`. For each permissible q, the largest r is `m-3-2q`, so the largest L at that q is
```text
L_max(q)=m*q+(m-3-2*q)=(m-2)*q+m-3.
```
Since m>=4, this increases with q. Its largest permissible q is `q0=floor((m-3)/2)`. Consequently
```text
K_bad = L_max(q0)+1
      = (m-2)*(floor((m-3)/2)+1)
      = (m-2)*floor((m-1)/2).
```
The corresponding q0,r0 meet all bounds, so the last bad coefficient is actually attained; no later L can satisfy (6). This proves (2)–(3). The full language contains w_m, so (4) follows. QED.

## Exact finite validation and scope

Companion `check_r139b.py` tests the single-quotient criterion against R138's two Farey-gap modular predicates for every m=4..40 and every K from 2 through `(m-1)^2+3`, plus two K values exceeding `10^80`: 20,683 exact comparisons. It also cross-checks w_m and its complement against an *independently enumerated chronological rational-atom scan* of the original strict fractional-part formula for m=4..8, K=2..39: 380 exact comparisons. Both suites passed; arithmetic uses only Python integers and `Fraction`. The infinite theorem is established by the symbolic proof above, not the finite tests.

Current open questions: (i) does w_m always control full-language eventual saturation `K_eventual(m)`, i.e. equality in (4)? (ii) classify which other words can last disappear at or beyond K_ext and identify a no-scan proof. Preserve source/observer typing and the current native task owner boundaries.
