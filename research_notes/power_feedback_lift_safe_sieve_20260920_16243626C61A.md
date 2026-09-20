# POWER feedback research: lift-safe residue sieve

Research-Activity-ID: `RA-POWER-REVIEW-16243626C61A`  
Researcher-ID: `EM-DIRECT-16243626C61A`  
Status: `PROVED_FINITE_ARITHMETIC_DERIVATION + EXECUTED_REGRESSION_CHECKS / NOT_DRIVER_ACCEPTED / NOT_FOUNDATION`  
Source stimulus: `awdawmip/power@6d784d3990afae602a03745173c3f2a16a076b0c` and prior note `research_notes/power_reuse_review_20260920_16243626C61A.md`.

## Selected question

How should a residue/wheel filter act on a factor-search fiber

\[
p=r+Mx
\]

without deleting a true factor merely because the coarse prefix `r` fails a filter?

This is the first feedback unit because the POWER audit produced a concrete false-negative witness, so correctness must be repaired before performance claims are optimized.

## Existing Enterprise interfaces reused

### T5 Integer Precision / Refinement Calculus — `REUSE_APPLIED`

The coarse prefix `r` is not the full state. The quotient coordinate `x` is the explicit detail needed to reconstruct `p=r+Mx`. The relevant T5 discipline is: projection may discard a detail coordinate only if the intended observer does not need it.

### T6 Operation-Safe Quotient / Predictive Refinement — `REUSE_APPLIED`

Population: integer lifts `x`.  
Coarse state: fixed prefix `r` modulo stride `M`.  
Observed output: divisibility of `r+Mx` by a filter modulus `ell`, or the vector of such outputs for a wheel.  
Allowed future operation: lift reconstruction `x -> r+Mx`, followed by divisibility/coprimality observation.

T6 says whole-fiber pruning is valid only when the observed output is constant on the coarse fiber. When it is not, refine the state by the smallest coordinate that restores constancy.

Reuse verdict: **COMPOSE_APPLIED (T5 + T6)**. No new top-level tool family is claimed.

## Exact lift theorem

Solve

\[
M x \equiv -r \pmod \ell.
\]

Let `d=gcd(M,ell)`.

1. If `d ∤ r`, there is no solution: no lift in the fiber is divisible by `ell`.
2. If `d | r`, divide by `d`. Since `gcd(M/d, ell/d)=1`, there is exactly one solution class

\[
x \equiv -\frac r d\left(\frac M d\right)^{-1}\pmod{\ell/d}.
\]

3. If `ell/d=1`, every quotient is a solution.

Therefore the exact repair coordinate for this observer is `x mod (ell/d)`. For several wheel primes, the joint observer is preserved by keeping `x` modulo the least common multiple of their active repair periods.

### Global descent criterion

The predicate `ell | p` descends through the quotient `p -> p mod M` for **every** prefix iff

\[
\ell\mid M.
\]

For a prime wheel factor `ell` not dividing `M`, the observer is generally nonconstant on the full lift fiber; whole-fiber rejection from the prefix alone is invalid.

## POWER counterexample repaired

For the audited Round-14 stride:

```text
M = 16,796,160,000
r = 7
x = 2
p = 33,592,320,007
```

`gcd(r,30030)=7`, but `gcd(p,30030)=1`.

For `ell=7`, `gcd(M,7)=1` and the theorem gives:

```text
x ≡ 0 (mod 7)
```

as the bad quotient class. Hence `x=2` survives.

## Executable specialization

Candidate source published with this research unit:

- `src/enterprise_math/lift_safe_residue_sieve.py`
- `tests/test_lift_safe_residue_sieve.py`

The module returns exact certificates with status:

```text
NEVER      no quotient hits the filter modulus
ALL        every quotient hits it
ONE_CLASS  one residue class modulo period hits it
```

It also compiles a joint repair period and filters a finite quotient window while preserving the boundary where the candidate itself equals the filter prime.

### Local validation before publication

- `pytest`: 5/5 passed.
- random linear-congruence comparisons: 1,000 parameter triples inside the pytest suite.
- additional exhaustive comparison: **1,702,074** `(prefix,stride,modulus,x)` checks; every certificate matched direct modular arithmetic.
- the POWER `r=7,x=2` witness is a permanent regression test.
- finite-window wheel survivors match direct `gcd(candidate,30030)` over 200 randomized configurations.

These are implementation checks for a finite elementary theorem, not factorization-performance evidence.

## BRC information audit

Before repair, the branch representation kept prefix-level Boolean support and erased quotient identity. That erased information is material because the divisibility observer varies inside the fiber.

After repair:

- retained: prefix `r`, stride `M`, quotient congruence class `x mod period`, filter-prime provenance;
- erased safely: quotient distinctions inside the same joint repair class, because all supplied wheel divisibility outputs agree there;
- not claimed: that the repair period is optimal for later operations beyond the declared wheel observer;
- finite-window failure remains `NOT_FOUND_WITHIN_BUDGET`, never `PROVED_EMPTY` outside the declared window.

This is a direct specialization of current BRC observer/fiber discipline.

## Other POWER ideas retained for further research, without overpromotion

### Witness-preserving Smith normal form

POWER's useful idea is to return `U,V` alongside invariant factors. Enterprise Math already has cokernel/reduced-Laplacian and chain-reduction surfaces, but the current tool inventory does not expose a generic Smith certificate interface. The next gate is to determine whether this extends T10/T11, with mandatory unimodularity verification, rather than creating a new family.

Status: `CAPABILITY_GAP_NOT_YET_PROMOTED`.

### Group-ring collision mass

The exact positive-integer observer `K_Q` is useful, but POWER materializes subgroup support and therefore does not establish an efficient classical Shor analogue. The next mathematical question is to characterize the coarsest future-observer quotient that preserves the identity coefficient under the remaining group-ring multipliers, and prove when any compression is genuinely smaller than the subgroup.

Status: `T4/T6 REUSE TARGET IDENTIFIED`; no asymptotic breakthrough claimed.

### Exact-root backend

The POWER failure shows that integer-only arithmetic is insufficient if budget exhaustion is silently mapped to empty output. Enterprise Math should keep explicit `UNKNOWN/BUDGET_EXHAUSTED` typing whenever exact refinement is incomplete.

Status: method-design feedback, not a new theorem in this unit.

## Smallest unresolved unit

For the lift-safe sieve, the mathematics is closed at the stated wheel-observer scope. A later performance study may compare unsafe prefix deletion, direct per-candidate wheel testing, and compiled quotient-class skipping on the same candidate population, measuring false negatives, modular operations, surviving classes, and wall time. No performance advantage is assumed here.
