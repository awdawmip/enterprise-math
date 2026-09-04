# Gregory–Machin continuation: complete multi-prime exterior shell through weighted Plücker height 20

Status: `FREE_RESEARCH / EXACT EXTERIOR-SHELL CLASSIFICATION + EXECUTABLE NEGATIVE CENSUS / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-B2817C / FREE_AXIOM_DISCOVERY`
Issue: `#1160`
Checker: `research_notes/experiments/gregory_machin_exterior_shell_p20_check_20260904.py`
Depends on: weighted Plücker budget theorem; complete P<=15 shell; generalized support-three prime-plane Pareto audit.

## 1. Stronger exterior-shell question

The first complete multi-prime shell

\[
\mathcal P(\Omega)\le15
\]

contains no support-three endpoint circuit beating the current generalized leader

\[
\mu_0=1.2096120143032323.
\]

This note pushes the **complete**, not sampled, exterior search to

\[
\boxed{\mathcal P(\Omega)\le20}
\]

under the atom denominator box

\[
0<a<b\le10^6.
\]

The Plücker support-graph theorem from the predecessor note makes the entire shell classifiable before atom generation.

---

## 2. Six active primes are still impossible

A decomposable rank-two Plücker support graph on `r` active prime coordinates is complete multipartite, hence connected and has at least `r-1` nonzero edges.

The minimum weighted connected graph on a fixed prime set is the star centered at the smallest prime.  For the six smallest split primes

\[
5,13,17,29,37,41
\]

the minimum possible weighted support is

\[
\ln5(\ln13+\ln17+\ln29+\ln37+\ln41)
\approx25.8957731425>20.
\]

Thus the full `P<=20` shell has at most five active split primes.

---

## 3. Five active primes: exactly eight states

For five active primes, the minimum possible connected-tree cost is

\[
\ln5(\ln13+\ln17+\ln29+\ln37)
\approx19.9190094678<20.
\]

Replacing `37` by the next split prime `41` raises this above 20.  Therefore the active set is uniquely

\[
\boxed{\{5,13,17,29,37\}.}
\]

There is almost no budget beyond the four-edge minimum star.  Any extra nonzero Plücker edge or any primitive edge coefficient with magnitude greater than one exceeds the budget.

Hence the support graph is exactly `K_{1,4}` centered at `5`, all four nonzero minors have magnitude one, and after quotienting one overall sign there are

\[
\boxed{2^3=8}
\]

primitive five-prime exterior states.

---

## 4. Four active primes: complete star enumeration

The smallest possible non-star complete multipartite graph is `K_{2,2}`.  Its minimum weighted realization already exceeds 20; for example the least partition on the smallest four split primes gives a cost above 25.

Therefore every four-prime state under the current budget is a `K_{1,3}` star.

A star centered at `13` with the smallest available leaves `5,17,29` already has cost greater than 20, so the center is forced to

\[
\boxed{5}.
\]

Write the leaf primes as

\[
p<q<r
\]

and the primitive star minors, after fixing the first sign positive, as

\[
(a,b,c),\qquad a>0,\quad bc\ne0,\quad\gcd(a,|b|,|c|)=1.
\]

The complete budget condition is

\[
\boxed{
\ln5\left(a\ln p+|b|\ln q+|c|\ln r\right)\le20.
}
\]

This dynamically bounds the largest leaf prime by approximately 1130.  Exhaustive enumeration gives exactly

\[
\boxed{2336}
\]

primitive four-prime exterior states.

Each corresponding saturated plane is explicit:

\[
\mathbf Ze_5
\oplus
\mathbf Z(ae_p+be_q+ce_r).
\]

---

## 5. Three active primes: exact dynamic enumeration

For active split primes

\[
p<q<r
\]

write

\[
(A,B,C)=(\Omega_{pq},\Omega_{pr},\Omega_{qr}).
\]

All nonzero 2-forms in three coordinates are decomposable.  Complete enumeration therefore imposes only:

- at least two nonzero coordinates;
- primitive gcd one;
- one overall sign convention;
- weighted cost at most 20.

Because the two cheapest possible nonzero edges are `(p,q)` and `(p,r)`, existence forces

\[
\ln p(\ln q+\ln r)\le20.
\]

The universal largest-prime bound comes from `(p,q)=(5,13)`:

\[
r\le\exp(20/\ln5-\ln13),
\]

so the checker needs split primes only through `19184`.

The complete three-prime shell contains

\[
\boxed{13{,}374}
\]

primitive exterior states.

---

## 6. Complete P<=20 census

For every exterior state, the checker:

1. reconstructs its saturated integer plane;
2. enumerates all free valuation columns satisfying
   \[
   X(v)<\ln(2H^2),\qquad H=10^6;
   \]
3. constructs exact first-octant rational atoms plus complement branches;
4. retains denominator height at most `H`;
5. before endpoint work, keeps only three-atom combinations whose generalized Lehmer cost is already below
   \[
   \mu_0=1.2096120143032323;
   \]
6. applies exact minimal rank-two kernel and `C8` diagonal target certification.

Exact regression counts are:

| class | exterior states |
|---|---:|
| 3 active primes | 13,374 |
| 4 active primes | 2,336 |
| 5 active primes | 8 |
| **total** | **15,718** |

Across this complete shell:

- generated atom instances: `1,337,555`;
- atom triples below the current Lehmer leader: `172`;
- exact `C8` diagonal endpoint circuits among them:

\[
\boxed{0}.
\]

Therefore:

\[
\boxed{
\mathcal P(\Omega)\le20,\ b\le10^6,\ \text{multi-prime support-three}
\Longrightarrow
\mu\ge1.2096120143032323
}
\]

for every exact endpoint circuit in the declared shell.

The inequality is understood as the exhaustive negative census statement: no circuit with strictly smaller `mu` exists in this finite universe.

---

## 7. The next combinatorial phase boundary

The `P<=20` universe has a particularly simple topology because every four- and five-prime plane is still a star.

The first genuinely non-star four-prime support graph is `K_{2,2}`.  On the four smallest split primes, its least weighted partition is

\[
\{5,13\}\mid\{17,29\},
\]

with edge cost

\[
\ln5\ln17+
\ln5\ln29+
\ln13\ln17+
\ln13\ln29
\approx25.8838.
\]

Almost simultaneously, the minimum six-prime star enters at

\[
\approx25.8958.
\]

Thus the next exterior-search phase is not merely “a larger numerical cap”.  Near `P≈25.89` two new structural phenomena arrive together:

1. non-star `K_{2,2}` rank-two planes;
2. six-active-prime star planes.

That is the natural next shell boundary for a new enumeration algorithm.

---

## 8. Current interpretation

The support-three generalized leader remains the two-prime `(5,17)` circuit

\[
\mu\approx1.2096120143032323,
\]

while all genuinely multi-prime exterior states through weighted height 20 fail to improve it.

This does not prove global optimality inside the full atom-height box—the theoretical Plücker budget is much larger—but it converts “small prime planes seem best” into an exact low-exterior-height theorem.

The next method should enumerate decomposable primitive Plücker states across the structural transition around `P≈25.89`, rather than simply widening a literal prime-pair cutoff.
