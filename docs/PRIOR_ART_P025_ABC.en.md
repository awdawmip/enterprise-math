# P025 ABC Radical-Support / Witness-Space Prior-Art Boundary

Status: `ACTIVE PRIOR-ART MAP / NONCANONICAL`  
Verified: 2026-08-09

## 1. Mason–Stothers and the Wronskian route

Baek and Lee's Lean 4 formalization exposes the classical short proof of Mason–Stothers particularly clearly: `f/rad(f)` divides the derivative; `a+b+c=0` makes the three Wronskians a common witness; the product of the three multiplicity residuals therefore divides that witness; and a Wronskian degree-capacity bound yields control by radical degree [SRC-BAEK-LEE-2024-MASON-LEAN].

P025 may reinterpret this chain as

`residual -> common witness -> witness capacity -> support bound`,

but derivatives, radicals, Wronskians, Mason–Stothers, and their formalizations are not Enterprise Math discoveries.

## 2. Pasten: relation-conditioned arithmetic derivatives on integers

Pasten directly studies the integer derivative bridge: arithmetic derivations satisfy a Leibniz rule and are constrained for a selected relation `a+b=c`; Geometry of Numbers supplies controlled-size derivations, and sufficiently small derivations are linked precisely to the abc conjecture [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES].

P025 therefore cannot claim as novel that:

- abc should admit an integer derivative analogue;
- a derivative should simultaneously interact with multiplication and a selected `a+b=c` relation;
- an integer Wronskian can absorb `n/rad(n)`-type multiplicity residual;
- abc can be reframed as the search for sufficiently small arithmetic derivatives.

The current P025 question is architectural: treat the set of relation-adapted derivations as a `relation-conditioned witness family`, then compare witness cost/precision with the cost of P023 future-safe refinement.

## 3. Exceptional-set route

Bernert, Browning, Lichtman, and Teräväinen obtain a power-saving count for abc-exceptional triples satisfying `rad(abc)<c^(1-epsilon)` [SRC-BERNERT-BROWNING-LICHTMAN-TERAVAINEN-2024-ABC-EXCEPTIONAL]. Runbo Li subsequently obtains the stronger exponent `O(X^(56/85+epsilon))` [SRC-LI-2025-ABC-EXCEPTIONAL].

Thus the fact that bad states can be quantitatively sparse is prior number theory. P025's possible contribution is only the quotient/collapse reinterpretation: whether scale-dependent exceptional incidence should become a reusable semantic level between exact safety and unrestricted failure.

## 4. Derivation generalization has broad prior art

Kikteva studies an ABC-type generalization for locally nilpotent derivations [SRC-KIKTEVA-2023-ABC-DERIVATION]. Merely replacing the ordinary derivative in Mason–Stothers by a more abstract derivation is therefore not a valid P025 novelty boundary.

## 5. Restricted successive minima already own the forbidden-sublattice minimum

Henk and Thiel study **restricted successive minima**: shortest lattice points in a symmetric convex body subject to the requirement that the realizing points avoid one or more forbidden sublattices [SRC-HENK-THIEL-2014-RESTRICTED-MINIMA]. Their framework explicitly includes shortest-vector questions outside proper sublattices and belongs to the Geometry-of-Numbers / Siegel-lemma-avoidance literature.

For the P025 witness flag, let

- `K=[-1,1]^S` in the real span of the prime-coordinate witness lattice;
- `Lambda=T=ker_Z(alpha)`;
- forbidden sublattice `Lambda_1=T^circ=T intersect ker_Z(beta)`.

Then P025's exact witness precision is precisely the corresponding restricted first minimum:

`mu = lambda_1(K, T \ T^circ)`.

The ordinary additive radius `rho` is the unrestricted first minimum `lambda_1(K,T)`.

Therefore P025 cannot claim as new:

- the invariant “shortest witness outside a forbidden sublattice”;
- general Geometry-of-Numbers bounds for that invariant;
- avoidance/Siegel-lemma methods for producing small non-degenerate lattice points.

The project-specific question is narrower: the `abc` relation itself generates `T^circ subset T`, arithmetic multiplicity demand supplies an independent lower certificate, and the same restricted minimum is then routed into exact proof-budget / future-precision semantics.

## 6. Current project-specific candidate

Within the present search, P025 provisionally marks only the following **combined architecture** as `NOVELTY_UNVERIFIED`:

1. express quotient-forgotten information as an explicit finite/integer residual;
2. derive a relation-conditioned witness/forbidden-sublattice flag from the arithmetic task itself;
3. connect arithmetic demand, the restricted first minimum, compact generator certificates, and exact proof-loss shells;
4. compare `refine state until exact descent` with `keep coarse state + attach bounded witness`;
5. add scale-dependent exceptional incidence to obtain an exact / bounded-witness / sparse-exception hierarchy.

A dedicated priority search for an equivalent general theory has not yet been completed. No “first”, “original”, or similar priority claim is permitted.
