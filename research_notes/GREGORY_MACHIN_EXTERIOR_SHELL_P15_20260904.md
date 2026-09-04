# Gregory–Machin continuation: complete first multi-prime exterior shell at weighted Plücker height 15

Status: `FREE_RESEARCH / EXACT EXTERIOR-SHELL CLASSIFICATION + EXECUTABLE NEGATIVE CENSUS / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-B2817C / FREE_AXIOM_DISCOVERY`
Issue: `#1160`
Checker: `research_notes/experiments/gregory_machin_exterior_shell_p15_check_20260904.py`
Depends on: weighted Plücker budget theorem; generalized support-three prime-plane Pareto audit.

## 1. Purpose and correction boundary

The weighted Plücker theorem supplies the complete plane resource

\[
\mathcal P(\Omega)=\sum_{p<q}|\Omega_{pq}|\ln p\ln q.
\]

A preliminary private prototype incorrectly reused a prime table sized for a smaller exterior budget when testing a larger shell.  That count was detected before persistence and is not used here.

This note instead fixes the first **fully complete multi-prime shell**

\[
\boxed{\mathcal P(\Omega)\le15}
\]

and derives the prime bound dynamically from the budget itself.

The atom resource box is

\[
0<a<b\le10^6,
\]

and only support-three endpoint circuits capable of beating the current generalized leader

\[
\mu_0=1.2096120143032323
\]

are tested after exact exterior generation.

---

## 2. Plücker support graph theorem

Represent a rank-two rational plane by nonzero coordinate columns

\[
u_p\in\mathbf Q^2.
\]

Then

\[
\Omega_{pq}=\det(u_p,u_q).
\]

Partition the active coordinates into parallel classes: `p~q` iff `u_p,u_q` are proportional.  Two active vertices have a nonzero Plücker edge exactly when they belong to different parallel classes.

Therefore the nonzero-minor support graph is a **complete multipartite graph** with at least two parts.  In particular it is connected and, on `r` active primes, has at least

\[
\boxed{r-1}
\]

nonzero Plücker coordinates.

For a fixed set of active split primes, the minimum possible weighted support cost is at least the minimum spanning-tree weight of the complete graph with edge weight

\[
w(p,q)=\ln p\ln q.
\]

Because the logarithms are positive and increasing, the minimum spanning tree is the star centered at the smallest prime.

---

## 3. Five or more active split primes are impossible at height 15

The five smallest split primes are

\[
5,13,17,29,37.
\]

The minimum connected-tree weight on them is

\[
\ln5(\ln13+\ln17+\ln29+\ln37)
\approx19.9190094678>15.
\]

Hence every primitive decomposable state with

\[
\mathcal P(\Omega)\le15
\]

has at most four active split-prime coordinates.

---

## 4. Exact four-prime classification

For four active split primes, the minimum tree weight forces the smallest three primes to be

\[
5,13,17.
\]

Indeed, replacing `13` by `17` already gives

\[
\ln5(\ln17+\ln29+\ln37)>15,
\]

while using a center at least `13` is still more expensive.

Thus the fourth prime `r` must satisfy

\[
\ln5(\ln13+\ln17+\ln r)\le15.
\]

Among split primes this gives exactly

\[
\boxed{r\in\{29,37,41\}.}
\]

The three-edge star already consumes more than `14.1` units of budget.  Any fourth nonzero Plücker edge or any coefficient magnitude greater than one pushes the weighted height above 15.  Since a connected complete multipartite graph with exactly three edges on four vertices must be `K_{1,3}`, the only possibilities are stars centered at 5 with

\[
|\Omega_{5,13}|=|\Omega_{5,17}|=|\Omega_{5,r}|=1.
\]

After quotienting one overall sign, there are four sign patterns for each `r`.  Hence the complete four-prime shell contains exactly

\[
\boxed{12}
\]

primitive exterior states.

---

## 5. Exact three-prime enumeration

For three active primes

\[
p<q<r,
\]

write

\[
(A,B,C)=(\Omega_{pq},\Omega_{pr},\Omega_{qr}).
\]

Every nonzero 2-form in three coordinates is decomposable, so the complete conditions are simply:

- at least two of `A,B,C` are nonzero;
- `gcd(|A|,|B|,|C|)=1`;
- one global sign convention;
- weighted budget at most 15.

The two cheapest possible nonzero edges are `(p,q)` and `(p,r)`, so existence forces

\[
\ln p(\ln q+\ln r)\le15.
\]

In particular the universal largest-prime bound comes from `(p,q)=(5,13)`:

\[
r\le\exp(15/\ln5-\ln13),
\]

which the checker rounds safely to `868` before sieving split primes.

The complete enumeration contains exactly

\[
\boxed{518}
\]

primitive three-prime exterior states.

---

## 6. Complete shell census against the current Lehmer leader

For each primitive exterior state, recover the saturated plane from

\[
x\wedge\Omega=0,
\]

enumerate all free valuation columns satisfying

\[
X(x)<\ln(2H^2),\qquad H=10^6,
\]
construct exact first-octant rational atoms plus their complements, and retain only atoms with denominator at most `H`.

For the four-prime stars the saturated plane is explicitly

\[
\mathbf Z e_5\oplus
\mathbf Z(s_{13}e_{13}+s_{17}e_{17}+s_re_r).
\]

The checker obtains:

- three-prime exterior states: `518`;
- four-prime exterior states: `12`;
- total complete multi-prime shell states: `530`;
- generated atom instances: `59,636`;
- atom triples whose generalized Lehmer cost is already below
  `1.2096120143032323`: exactly `2`;
- exact minimal rank-two `C8` diagonal endpoint circuits among those two: **0**.

Therefore:

\[
\boxed{
\text{No multi-prime support-three exterior state with }
\mathcal P(\Omega)\le15
\text{ beats the current }\mu=1.2096120143\text{ leader at }H=10^6.
}
\]

This is an exact finite negative statement for the full declared exterior shell, not a sample over selected prime palettes.

---

## 7. Interpretation

The current generalized support-three leader lies in the two-prime plane `(5,17)`, whose primitive exterior height is only

\[
\mathcal P=\ln5\ln17\approx4.55988097.
\]

The first genuinely multi-prime exterior states begin at

\[
\ln5\ln13+\ln5\ln17
\approx8.68800771.
\]

The complete shell audit through 15 finds no improvement.  Thus the low exterior-height ordering seen in the prime-plane search is not immediately broken by the first multi-prime planes.

This does **not** imply global optimality.  The full height-box theorem allows exterior budget up to

\[
\ln^2(2H^2),
\]

which is much larger than 15 at `H=10^6`.

The next useful step is a branch-and-bound over decomposable primitive Plücker states ordered by `mathcal P`, using completion-cost lower bounds to avoid expanding every state up to the worst-case theoretical budget.
