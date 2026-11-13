# R121-LIT — Exact cubic floor-lift vocabulary via finite Sturmian words

Date: 2026-11-13. This is a *literature-linked strengthening* of R121-AP, not a novel claim to the published finite-word enumeration theorem. Original theorem and its independent S23 two-integer reduction are in `PROOF.md` (research commit `a6681741f3d1e2658ad1ffa6a6bf48d1595ce66f`).

## Exact cardinality

For `m>=1`, let

`P_m = { (floor(alpha+i*beta))_{i=0}^{m-1} : 0<=alpha,beta<1 }`.

Then its **exact** size, sharpening R121's direct arrangement bound, is

`|P_m| = 1 + sum_{r=1}^{m-1} (m-r) * phi(r)`,

where `phi` is Euler's totient function. In particular `|P_m| = (m-1)^3/pi^2 + O(m^2 log m)` by the classical totient summatory estimate; more conservatively `|P_m| = Theta(m^3)`.

**Precise reduction to published combinatorics.** Set `n=m-1` and let `w_i=q_{i+1}-q_i` for `i=0,...,n-1`, where `q in P_m`. Since `0<=beta<1`, each `w_i` is 0 or 1. The formula for `q_i` gives

`w_i = floor(alpha+(i+1)*beta)-floor(alpha+i*beta)`.

Thus `w` is a finite lower mechanical (Sturmian/balanced) word of length `n`. The standard mechanical characterization establishes the converse: every finite Sturmian/balanced binary word is realized by some `alpha,beta in [0,1)`; rational-slope and exact-boundary cases are covered by finite perturbation to a nearby irrational slope with the same finite word. Also `q_0=0`, and `q_i=sum_{r<i}w_r`, so `q <-> w` is bijective.

The established finite Sturmian-word enumeration formula is

`S(n) = 1 + sum_{r=1}^{n} (n-r+1)*phi(r)`.

Therefore `|P_m|=S(m-1)` exactly. The result is documented by OEIS A005598, including attribution to F. Mignosi (1991) and a geometric proof by J. Berstel and M. Pocchiola (1993), along with the cubic asymptotic. This part of R121 is **existing external mathematical knowledge**, now linked to the project's exact floor-lift theorem.

## Consequence for R121 S23 oracle

For a prescribed m-bit S23 joint eligibility vector on a fixed old parameter atom, the reduction in `PROOF.md` now needs no more than

`2^m [1+sum_{r=1}^{m-1}(m-r)*phi(r)] = O(2^m m^3)`

2-integer linear feasibility calls. To enumerate all 2^m possible eligibility vectors, the bound is `O(4^m m^3)` calls. Coefficient formation, exact arrangement generation, and the 2D ILP solver each contribute their separately accounted polynomial-in-m-and-input-bit-length cost. These bounds count oracle calls; they do not pretend that the accompanying bounded enumeration program is a polynomial ILP solver.

An exact finite checker extended the R121 rational line-arrangement enumerator to `m=2,...,13`. Its resulting counts

`2,4,8,14,24,36,54,76,104,136,178,224`

match the totient formula in all twelve cases. This is a finite implementation cross-check, not an independent proof of Mignosi's theorem.

## Sources and attribution

- OEIS A005598, *Number of possible interleaving orders / finite Sturmian words*: https://oeis.org/A005598 (formula, initial values, proof references and asymptotic).
- F. Mignosi, *On the Number of Factors of Sturmian Words*, Theoretical Computer Science 82(1):71–84 (1991). Original enumeration.
- J. Berstel and M. Pocchiola, *A Geometric Proof of the Enumeration Formula for Sturmian Words*, International Journal of Algebra and Computation 3(3):349–355 (1993), https://doi.org/10.1142/S0218196793000238 .
- Project original R121-AP proof, source check and original 72-case verification: `PROOF.md`, `check_r121.py`, `verification_r121.json` at `a6681741f3d1e2658ad1ffa6a6bf48d1595ce66f`.

## Next

A constructive implementation of exact 2D ILP with rational witness and no numeric approximation is still the algorithmic priority. Separately, evaluate whether the tighter cubic vocabulary can be enumerated directly from Farey fractions in near-output-linear operations rather than with the current generic line arrangement sweep. Preserve arithmetic-progression time-set hypotheses and exact signed source provenance when coupling to older rankings.
