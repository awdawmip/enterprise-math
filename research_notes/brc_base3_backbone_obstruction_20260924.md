# BRC base-3 universal-backbone criterion and shared class-19 hyperedge obstruction

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / AUXILIARY_ONLY / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`.

Stable logical lane: `chatgpt-research-hourly-enterprise-math-20260923`.

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`.

This unit consumes the three-sector domination theorem. It isolates exactly when the `3|L` sector has a single universal pure backbone and exhibits the first observed finite-horizon obstruction mechanism. No D24/UR formal status is changed.

## 1. Exact 3-compatible rows

Fix `p == 13 (mod24)` and the finite 19-neutral LCM atom library. For every earlier class-13 prime q write

`ord_q(4)=2s_q`.

Let `V_3` denote all admissible atoms with `3|L`. Since `s_13=3`, these are exactly atoms carrying the base q=13 cancellation source.

Call an earlier class-13 row q **3-compatible** when

`lcm(3,s_q)`

is class-19-neutral below p. Let `U_3(p)` be the set of all such rows.

### Lemma 1.1 — exact cancellability criterion

An earlier row q is cancelled by some atom in `V_3` iff `q in U_3(p)`.

Proof. If a 3-sector atom L cancels q, then both 3 and `s_q` divide L. Hence `lcm(3,s_q)|L`; every divisor of a 19-neutral atom is 19-neutral, so q is 3-compatible.

Conversely, if `lcm(3,s_q)` is 19-neutral, then both generating steps are clean and their lcm is itself an admissible LCM atom in `V_3`, cancelling q. QED.

Thus `U_3(p)` is not a heuristic support union. It is the exact set of negative directions available anywhere in the entire 3-sector.

## 2. Canonical backbone candidate

Define

`C_3(p)=lcm { s_q : q in U_3(p) }`.

Every atom that could dominate the whole 3-sector must cancel every row in `U_3(p)`: for each such q, Lemma 1.1 gives a 3-sector atom whose q-coordinate is `-c_q`; a dominating signature cannot be nonnegative there. Therefore every universal 3-sector backbone must be divisible by `C_3(p)`.

Call an atom **pure** when every earlier class-13 coordinate is nonpositive; equivalently

`q|L and s_q does not divide L`

never occurs on an earlier tracked class-13 row.

### Theorem 2.1 — exact universal-backbone criterion

There exists one atom C whose signature dominates every atom in `V_3` iff the canonical candidate `C_3(p)` is

1. class-19-neutral below p, and
2. pure.

When these conditions hold, `C_3(p)` itself is a universal 3-sector backbone and is the least one under divisibility in the target-blind canonical quotient.

Proof, necessity. Suppose C dominates all `V_3`. By the argument above, `C_3(p)|C`. Since C is admissible, every divisor of C is class-19-neutral, proving condition 1.

Also the atom `3` belongs to `V_3`. If C does not cancel an earlier row q, domination of the signature of 3 forces

`v_q(C)<=v_q(3)=0`.

Hence C has no positive denominator spill on an uncancelled row: C is pure. If `C_3(p)` had a positive denominator factor q without cancelling q, then q divides C as well. Purity of C would force C to cancel q, so some 3-sector atom cancels q; Lemma 1.1 would put q in `U_3(p)`, and then `s_q` would already divide `C_3(p)`, contradiction. Thus the canonical candidate itself is pure.

Proof, sufficiency. Assume `C_3(p)` is neutral and pure. It is an admissible atom because it is the lcm of clean generating steps. If a 3-sector atom L cancels q, Lemma 1.1 gives `q in U_3(p)`, so `C_3(p)` also cancels q and both signatures equal `-c_q`. If L does not cancel q, the backbone either cancels q, giving a negative coordinate no larger than L's nonnegative one, or does not cancel q, in which case purity gives backbone coordinate 0 while L has `v_q(L)>=0`. Hence `a(C_3)<=a(L)` coordinatewise for every `L in V_3`. QED.

This theorem replaces full sector enumeration by two exact arithmetic checks on one canonical lcm.

## 3. Shared-hyperedge obstruction

The criterion also identifies a failure mechanism which is invisible in pairwise row checks.

At target

`p=2221`,

the rows q=61 and q=853 are individually 3-compatible:

`s_61=15=3*5`,

`s_853=213=3*71`,

and each of 15 and 213 is class-19-neutral below 2221.

But their shared lcm is

`lcm(15,213)=1065=3*5*71`.

Now

`2131` is an earlier prime with `2131 == 19 (mod24)`, and

`(2131-1)/2=1065`.

Therefore 1065 is a forbidden class-19 endpoint divisor. Since both q=61 and q=853 belong to `U_3(2221)`, the canonical candidate `C_3(2221)` must be divisible by 1065, hence is not 19-neutral.

By Theorem 2.1:

**No single admissible atom can dominate the complete 3-sector at p=2221.**

This is a genuine shared hyperedge obstruction. Neither q=61 nor q=853 is individually dirty relative to the base-3 carrier. The obstruction appears only after their required cancellation sources are combined. Thus pairwise compatibility of every requested row with the base carrier does not imply global backbone existence.

## 4. Relation to the p=1117 compensated-star unit

At p=1117 the canonical candidate is

`C_3=4947619432543905`

and is both 19-neutral and pure, so the previous unit's backbone C is not an empirical choice: it is exactly the canonical universal 3-sector backbone supplied by Theorem 2.1.

The p=1117 q=1093 obstruction belonged to the complementary `3∤L` sector: q=1093 cannot be made pure there, but its q=13 debt is compensated by C.

At p=2221 a qualitatively later obstruction occurs: the base-3 sector itself no longer admits one universal atom because its support union crosses a class-19 forbidden endpoint. Any further two-generator theorem must therefore either refine the sector partition or permit several backbone atoms; merely extending the earlier `{A,C}` pattern cannot be justified unchanged.

## 5. Independent falsification/regression

Paired checker:

`research_checks/check_brc_base3_backbone_obstruction_20260924.py`.

It reconstructs exact multiplicative orders and class-19 forbidden divisors. At p=397,733,1021,1117 it also reconstructs the full finite atom libraries and verifies that the canonical `C_3` dominates every 3-sector atom. Across these moderate horizons it checks 1072 3-sector atoms.

For p=2221 it verifies directly:

- `s_61=15`, `s_853=213`;
- both are individually 19-neutral;
- `2131` is prime and `19 mod24`;
- its endpoint is 1065;
- `lcm(15,213)=1065`;
- both rows lie in `U_3(2221)`;
- `C_3(2221)` is divisible by 1065 and therefore not neutral.

A deterministic finite census through p=2221 finds this criterion passing at the earlier class-13 target horizons and failing at p=2221. That census is regression only; the no-backbone statement at p=2221 follows from the exact hyperedge argument and Theorem 2.1.

## 6. BRC interpretation / next

The minimal sufficient state for backbone existence is not the list of pairwise-compatible rows. It must retain the lcm interaction of their cancellation sources against class-19 forbidden endpoint divisors. The obstruction is therefore naturally a hypergraph constraint:

- vertices: required cancellation-source factors;
- admissible row edges: individual `lcm(3,s_q)` constraints;
- forbidden hyperedges: earlier class-19 denominators/endpoints;
- universal backbone exists exactly when the total support lcm remains admissible and denominator-closed.

Do not infer that failure of the one-backbone criterion means the full repair cone is infeasible; it only kills a single universal 3-sector generator.

If D24 succession remains blocked, the next nonredundant unit is to replace the failed single-backbone sector by a minimum admissible cover of `U_3(p)` under these forbidden hyperedges and determine how its cover number interacts with the semigroup domination basis. If the canonical lossless staging/session-rollover operation becomes live, stop auxiliary work and return to D24 immediately.
