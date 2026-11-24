# A finite-pool total-cost check on the eight saved zero-W examples

2026-11-24, Researcher `EM-DIRECT-970E1C`, Activity
`RA-D2EC212845B63844081F9A14`. Author computation with shared-context
collaboration; no independent project Review or new native BRC execution.

The complete zero-W theorem has eight geometric types. Its saved certificate
contains one ordinary exact-cost-nine CRT root from each type. This note
records a limited total-cost exploration on those eight roots, without
promoting the chosen candidate pool to a universal bound on unrestricted tau.

## Exact observation

For each of the eight roots, the originally displayed P20 plus nine-prime
supplement is inclusion-minimal even when the twenty old primes may be
deleted: all twenty-nine selected primes have private positions over their
complete common residue period.

The pool was then expanded to 86 primes: P20, the seven fixed active R3
supplements `{5,13,19,73,38737,246241,487824887233}`, and all 59 free prime
coordinates occurring in the complete ninth-budget observer. Every prime
and its exact base-two order is checked by deterministic arithmetic.

The numbers of active primes on the eight roots are 35,35,35,34,35,35,35,36.
For all eight roots, every old P prime still has a private index even
relative to this entire active pool. The exact minimum covering subset
of the specified 86-prime pool has cardinality **29 in all eight cases**.
The selected minimum need not be the original dictionary: the first
root admits a replacement using the fixed W channels, but this still
uses twenty old primes and nine supplements.

## Reproducible finite proof

For each active prime, the program finds its unique zero phase modulo
its exact order. It checks every position of the common period of all
active pool primes. Inactive primes have no zero phase and cannot help.
All listed primes are smaller than each root's first sequence term, so
each divisibility hit is a proper factor.

At each period position form the set of active primes that hit it. Covering
the whole period is exactly the finite hitting-set problem on those sets.
Duplicate constraints and supersets of another constraint can be removed.
For a remaining constraint C, every covering set contains some q in C.
The dynamic program branches on every such q and solves the constraints
not already met by it. This recursion is exhaustive and returns a minimum
cardinality. The certificate stores the full reduced constraints, a
minimum dictionary, and private indices. The state counts are small;
the calculation does not use a heuristic solution as a lower bound.

Run `python verify_selected_pool.py`. The adjacent `source_input.json`
contains the eight original roots, their source-certificate SHA-256, the
explicit prime pool and deterministic primality certificates. The checker
writes `selected_pool_certificate.json`.

## Scope

These observations give tau<=29 for the same eight roots and show that
this particular enlarged pool cannot improve that upper bound. They do
**not** give tau>=29 among all prime dictionaries, do not exclude other
roots with tau<=27, and do not conflict with the separately proved
one-W example having delta_P=9 and tau=28. No new unrestricted total-cost
equality follows from this finite-pool calculation.
