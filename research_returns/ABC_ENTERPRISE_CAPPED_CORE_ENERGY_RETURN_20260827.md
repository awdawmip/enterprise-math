# Research Return — ABC Enterprise Capped-Core Energy Bound

Task: `RS-ABC-ENTERPRISE-CAPPED-CORE-ENERGY`
Publication: `TP2-BFADCF4FE05B64A2BD24`
Researcher: `EM-ABC1-C0E119`
Execution: `ER-D7B0A54391369ACA084F`
Primary verdict: `EXACT_OBSTRUCTION`
Hard target: `ABC_CAPPED_CORE_BOUND_PROVED_OR_EXACT_OBSTRUCTION_FROZEN` — `MET_BY_EXACT_OBSTRUCTION`

## Executive result

The coefficient-2 capped-core route does not fail because the constant was numerically too loose. It fails because a naked upper bound on the capped core controls the wrong side of the exact abc budget.

Using an explicitly independent standard abc reconstruction for primitive `a+b=c`, define

`C=log c`, `R=log rad(abc)`, `H=log(abc/rad(abc))`, and `beta=log(c^2/(4ab))`.

Then

`3C = R + H + beta + log 4`.

For any decomposition `H=I+D`, one has the exact equivalence

`q=C/R <= 1+epsilon`

iff

`2R-I >= D + beta + log 4 - 3 epsilon R`.

Thus the nontrivial target is a **deficit lower bound** for `2R-I`. A theorem of the form `I<=2R` alone does not pay `D` or the boundary. Conversely, adopting the displayed deficit condition itself as the decisive lemma is merely the target abc quality inequality rewritten, so that route is killed by the taskbook anti-circularity rule.

## Natural cap-two test

Because the canonical conversation-frozen formula for `I_cap` is not durably present in the published task sources, this return does not pretend to recover it. For falsification, it defines the natural independent cap-two model

`I_2 = sum_p min(v_p(abc)-1,2) log p`,

`D_2 = sum_p max(v_p(abc)-3,0) log p`,

so `H=I_2+D_2`.

The raw coefficient-2 bound

`I_2 <= 2R`

is globally true term-by-term and therefore tautological; it does not use `a+b=c` after valuations are supplied.

Two exact counterexamples delimit the obvious strengthenings:

1. `1+8=9`: `rad=6`, `cap2=12`, `D_2=0`. The boundary-paid strengthening `I_2+beta+log4<=2R` exponentiates to `12*9^2 <= 6^2*1*8`, i.e. `972<=288`, false. The failure occurs with zero uncapped surplus.
2. `32+49=81`: `rad=42`, full height product `3024`, cap2 product `252`, surplus product `12`. Hence the full-height coefficient-2 claim fails exactly: `3024>42^2=1764`. Here `beta≈0.04505`, so this is not merely boundary escape.

## Bounded counterexample search

`python scripts/check_abc_enterprise_capped_core_energy.py --limit 5000`

checked `3,800,228` primitive unordered triples exactly.

Results:

- raw cap-two failures: `0` (and independently globally proved);
- first boundary-paid cap-two failure: `(1,8,9)`;
- first full-height coefficient-2 failure: `(32,49,81)`;
- exact integer regression: `PASS`.

Enumeration is used only as falsification/regression evidence, not as a global proof.

## Strength relative to abc

- `I_2<=2R`: strictly too weak / tautological radical-budget ceiling.
- `2R-I >= D+beta+log4-3epsilon R`: exactly equivalent to `q<=1+epsilon`, hence not an independent advance unless derived from another Enterprise invariant.
- Therefore the surviving research object is not a better constant near 2, but an **independent deficit generator**.

## Provenance and semantic guard

The task publication states `ABC_ENTERPRISE_PLANE_DECOMPOSITION_FROZEN_IN_CONVERSATION`, but the exact parent formulas defining canonical `I_cap` are absent from the durable task source set. This is recorded as a provenance blocker, not silently filled by guesswork.

All arithmetic quantities in this return remain derived arithmetic/readout objects. Native Enterprise point addresses, native line trace, and the separately typed derived displacement quotient remain semantically distinct as required by the pinned foundation sources.

## Surviving assumptions

1. Primitive positive `a+b=c`, `gcd(a,b)=1`.
2. The standard reconstructed log quantities above for the exact obstruction theorem.
3. For the abstract deficit equivalence, only a split `H=I+D` is required.
4. Identification of the natural `I_2` with the canonical conversation-frozen `I_cap` is **not** assumed.

## Smallest unresolved unit

`CANONICAL_I_CAP_DEFINITION_AND_AN_INDEPENDENT_DEFICIT_GENERATOR`

The useful next research question is:

Can a carry/local/Enterprise-derived observable prove a lower bound on `2R-I_cap` that pays the uncapped surplus and boundary terms, without importing an inequality algebraically equivalent to abc?

## Durable outputs

- `research_artifacts/ABC_ENTERPRISE_CAPPED_CORE_ENERGY/ABC_CAPPED_CORE_EXACT_OBSTRUCTION_20260827.md`
- `scripts/check_abc_enterprise_capped_core_energy.py`
- this return
- immutable execution/result provenance records

Return control to parent objective `ABC_ENTERPRISE_PLANE_RESEARCH_20260827`; ordinary result now awaits Driver review.
