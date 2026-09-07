# BRC Cell-Collapse Phase Diagram and Finite-Group Phase Boundary

Status: `RESEARCH FRONTIER / EXACT COMPLEXITY TRADEOFF + MODULAR-PHASE REDUCTION + CAPABILITY GAP / NO SPEEDUP CLAIM`
Date: `2026-09-08`
Parents:
- `research_notes/BRC_COPPERSMITH_CELL_BENCHMARK_20260908.md`
- `research_notes/BRC_GCD_DIVISOR_LATTICE_QUOTIENT_FRONTIER_20260908.md`
- `research_notes/BRC_MULTIPLIER_COLLISION_ENERGY_TRACE_20260908.md`
Current source snapshot before write: `main@1e338a83e19d45557de1d3e0026b606017d224fc`
BRC capability audit:
- positive Weighted-BRC / rational holonomy available;
- finite multiplicative-group phase carrier not identified in current tool inventory;
- positive-rational holonomy must not be substituted for finite-group phase.

## 0. Purpose

The collision/activation line has reduced the hidden factor search to two possible sources of asymptotic gain:

1. an N-only preconditioner that shrinks the real factor-location interval;
2. a collective constructor that evaluates many one-factor search cells faster than visiting them individually.

The Harvey-Hittmeir interval theorem supplies a natural external cell scale `N^(1/4)` near balanced factors. This note derives the exact exponent tradeoff between preconditioning and collective collapse, then compares that positive/Boolean BRC route with the finite-group phase mechanism used in modern deterministic `N^(1/5)` factorisation.

The result is a clean capability boundary: the current positive/divisor BRC carrier is sufficient to state the one-factor OR problem but does not contain the multiplicative-group phase coordinate that drives the known exponential improvement.

---

## 1. Cell-count exponent after N-only localization

Let `N=pq` with `p<q` and balanced factor scale `p=Theta(N^(1/2))`.

Suppose an N-only preconditioner, construction-family theorem, or other valid observer restricts the least factor to an interval of width

`H = N^(1/2-gamma+o(1))`,

for some localization exponent `gamma>=0`.

Near `sqrt(N)`, Harvey-Hittmeir's interval algorithm gives a polynomial-time cell width of order

`N^(1/4+o(1))`.

Therefore the number of unresolved Coppersmith-scale cells is

`C = H/N^(1/4) = N^(1/4-gamma+o(1))`

when `gamma<1/4`; for `gamma>=1/4` the search is already polynomial-time under the interval theorem.

This is the correct population size for any BRC collective-cell observer in the balanced one-factor zone.

---

## 2. Collective-collapse exponent

Assume a collective constructor can evaluate the one-factor cell OR / proper-gcd state for `C` cells in

`C^(beta+o(1)) * polylog(N)`

work, with `0<=beta<=1` as the effective cell-collapse exponent.

Because the entire population lies below `q`, Boolean OR is operation-safe: a positive aggregate may return `p` directly through gcd, so no cell label is required.

Ignoring the separately accounted cost of the preconditioner, the search exponent is

`e(gamma,beta)=beta*(1/4-gamma)`

for `0<=gamma<1/4`.

Hence to beat an exponent-one-fifth deterministic benchmark one needs

`beta*(1/4-gamma) < 1/5`.

This is the main phase boundary.

### Pure collective-collapse route

If no growing localization is obtained (`gamma=0`), then

`e=beta/4`.

Beating `1/5` requires

`beta<4/5`.

Thus a genuinely new Boolean/cell BRC constructor would need to collapse the approximately `N^(1/4)` cells in strictly sub-`C^(4/5)` work.

### Pure localization route

If the cell evaluator remains linear (`beta=1`), then beating `1/5` requires

`gamma>1/20`.

Equivalently the factor interval must be narrower than

`N^(9/20-o(1))`.

For an `n`-bit modulus, `gamma=1/20` corresponds to roughly `n/20` bits of growing magnitude localization. For RSA-270 (`n=895`) this is about 45 bits.

### Mixed route

Every pair `(gamma,beta)` below the line

`beta=1/(5*(1/4-gamma))`

in the admissible square gives an exponent below one fifth, again before charging the preconditioner.

This supplies a quantitative score for future BRC ideas: a partial magnitude leak and a partial collective-collapse gain may compose even when neither is individually sufficient.

---

## 3. Why fixed local residues remain asymptotically negligible

The concrete collision-local work for RSA-270 reached

`S^2 mod 2880`

and related fixed congruence refinements. These remove only a constant number of candidate classes, so asymptotically they correspond to

`gamma=0`.

Likewise a fixed binary construction prefix narrows the real interval by a constant factor and therefore still has `gamma=0`.

To move horizontally in the phase diagram, the information budget must grow with `log N`: for example a real interval width `N^(1/2-gamma)` or a growing modular/coset restriction with a proved backend giving comparable candidate-density reduction.

A fixed congruence must never be counted as a positive `gamma`.

---

## 4. Finite-group phase identity for the factor sum

The modern deterministic factorisation literature uses a different information carrier.

For `N=pq` and

`S=p+q`,

we have the elementary identity

`N+1-S = (p-1)(q-1)`.

Therefore for every unit

`alpha in (Z/NZ)^*`,

Euler's theorem on both prime components gives

`alpha^(N+1) = alpha^S (mod N)`.

This is the exact Pollard/Hittmeir phase relation highlighted in modern deterministic factoring work.

If `alpha` has multiplicative order `M`, then equality of powers implies

`S == N+1 (mod M)`

inside the cyclic subgroup generated by `alpha`; more precisely any solution exponent `x` to

`alpha^x=alpha^(N+1)`

is congruent to `S mod M`.

Thus large multiplicative order supplies a **growing-modulus phase coordinate of S**.

This is qualitatively different from the fixed local congruence shadows of the collision-energy route: the order `M` itself may grow as a power of `N`.

---

## 5. Candidate-space effect of an order-M phase

Assume for the moment that an exact residue

`S == s0 (mod M)`

is available and that a fixed RSA-type ratio prior restricts `S` to an interval of width `Theta(sqrt(N))`.

Then the number of ordinary integer candidates for `S` is

`O(sqrt(N)/M + 1)`.

Each candidate may be checked by testing whether

`Delta=S^2-4N`

is a non-negative square.

Therefore an order

`M=N^(mu)`

would, if its S residue were already materialised at negligible cost, reduce naive candidate enumeration to

`N^(1/2-mu+o(1))`.

In particular:

- `mu>=3/10` makes naive S-candidate enumeration no worse than `N^(1/5)`;
- `mu>=1/2` determines S up to O(1) candidates in a balanced constant-ratio band.

This is only an information-effect calculation. Computing or exploiting the phase is the hard part, and modern algorithms use BSGS and stronger structured searches rather than simply enumerating S candidates.

---

## 6. External one-fifth mechanism is phase-rich, not Boolean-support-only

Harvey's exponent-one-fifth deterministic algorithm explicitly reviews the relation

`alpha^(p+q) == alpha^(N+1) (mod N)`

and the use of baby-step/giant-step searches in `(Z/NZ)^*`. Its exponential improvement over the old `N^(1/4+o(1))` framework comes from applying BSGS much more globally to factor-sum / Lehman-combination candidate spaces, together with large-order elements and fast algebraic evaluation.

Harvey-Hittmeir's 2026 work identifies deterministic construction of sufficiently large multiplicative-order elements as an essential subroutine in the fastest recent deterministic factoring algorithms and removes earlier lower-bound restrictions on the target order `D`.

So the known record-level route introduces a carrier with:

- finite-group values;
- multiplicative phase/equality under powers;
- large-order injectivity range;
- collision structure exploitable by BSGS.

A Boolean `UNIT/nonunit` or divisor-support state does not retain this phase coordinate.

---

## 7. Current BRC capability audit

The project currently contains `brc_rational_holonomy.py`, whose explicit semantics are **positive rational** edge weights, rational gauge normal forms and prime-valuation coordinates.

That carrier is useful for positive-rational multiplicative holonomy, but it is not the finite unit group `(Z/NZ)^*` and does not carry cyclic phase modulo an unknown/order-dependent group period.

The account-wide BRC policy also freezes

`POSITIVE_WEIGHTED_BRC != SIGNED_OR_PHASE_CANCELLATION`.

Therefore it would be semantically invalid to claim that the existing positive-rational holonomy tool already implements the phase used by deterministic factoring.

Current resolution:

`CAPABILITY_GAP_CONFIRMED`.

The missing typed carrier is a finite-group / group-valued phase branch state, or another exact interface with equivalent power-collision semantics. Introducing such a carrier would be a domain extension, not an automatic Foundation promotion and not a proof of a new factoring algorithm.

---

## 8. BRC interpretation of the gap

The Boolean activation program asks only:

`does some branch contain p?`

and can quotient all positive branches to one OR state in a one-factor zone.

The group-phase program retains much richer information:

`which exponent class maps to this group value?`

Its recoalescence is not positive-mass union. It is equality/collision in a finite multiplicative group, and the collision position carries an exponent difference.

This explains the repeated pattern observed in the collision research:

- positive support can often be compressed to tiny state;
- that compression does not automatically reduce constructor complexity;
- the known exponential speedup arrives only after retaining a phase coordinate that the positive quotient deliberately erased.

Freeze:

`SMALL_POSITIVE_CARRIER != FAST_CONSTRUCTOR`.

`GROUP_PHASE_RECOALESCENCE != BOOLEAN_SUPPORT_RECOALESCENCE`.

---

## 9. Revised attack trichotomy

The RSA-270 BRC line now has three mathematically clean possible successors.

### A. Positive-cell breakthrough

Stay entirely in Boolean/divisor BRC and construct the one-factor OR over `C` Coppersmith cells in `C^(beta)` work with `beta<4/5` when `gamma=0`, or satisfy the mixed inequality

`beta*(1/4-gamma)<1/5`

with a separately costed preconditioner.

### B. Growing preconditioner

Produce a genuine N-only magnitude/coset restriction with `gamma>1/20` if cell evaluation remains linear, or enough localization to cross the mixed phase boundary with a weaker collective improvement.

### C. Typed finite-group phase extension

Introduce an explicit finite-group phase carrier and ask whether BRC branch/provenance tools can reorganize the existing power-collision search more efficiently than current large-order/BSGS methods.

This route must compare directly with Harvey/Hittmeir-class algorithms. Merely restating

`alpha^(N+1)=alpha^S`

or ordinary BSGS as BRC is prior-art semantics, not new progress.

---

## 10. Kill conditions

Kill a future claim if:

- it uses fixed local residues but assigns a positive localization exponent `gamma`;
- it collapses positive cells to Boolean support and then assumes the constructor becomes equally small;
- it silently treats positive-rational holonomy as finite cyclic phase;
- it invokes ordinary large-order search / discrete log / BSGS and labels the result a new BRC factoring algorithm;
- it reports an exponent below one fifth without charging the preconditioner or phase-construction cost.

Retain only work that either crosses the quantitative `(gamma,beta)` phase boundary with a new constructor/preconditioner, or builds a typed phase interface that yields a demonstrable algorithmic improvement over the current deterministic factoring baseline.

No Foundation promotion, Working Truth promotion, or factorization-speedup claim is made.