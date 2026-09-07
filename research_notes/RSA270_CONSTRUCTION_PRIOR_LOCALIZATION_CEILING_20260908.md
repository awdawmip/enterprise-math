# RSA-270 Construction-Prior Localization Ceiling

Status: `RESEARCH FRONTIER / CURRENT EXTERNAL-PROVENANCE AUDIT + CONDITIONAL LOCALIZATION CALCULATION + GROWING-PRECISION NO-GO / NO FACTORING CLAIM`
Date: `2026-09-08`
Parent: `research_notes/BRC_CELL_COLLAPSE_PHASE_CARRIER_BOUNDARY_20260908.md`
Project source snapshot before write: `main@5bdadbf93e1255243897d28f3e3729e272ccfbe1`

## 0. Purpose

The BRC cell-collapse phase diagram showed that, if the best known interval-divisor backend is kept unchanged, a pure N-only magnitude preconditioner would need a growing localization exponent `gamma>1/20` to beat the exponent-one-fifth deterministic benchmark. For 895-bit RSA-270 this corresponds to roughly 45 bits of genuine factor-location information.

This note audits the actual public construction information for the original decimal-labelled RSA Challenge family and separates:

1. documented hard metadata;
2. current solved-family statistical evidence;
3. conditional transfer of that family evidence to still-unfactored RSA-270.

The conclusion is that all currently defensible construction priors remain constant-information constraints. They are useful for finite ordering and validation but cannot supply the required growing localization exponent.

---

## 1. Documented original-list metadata

The archived 1994 RSA Challenge list states that every listed number was produced from

- two randomly chosen primes of approximately the same length;
- both primes congruent to `2 mod 3`, so public exponent `e=3` would be valid;
- probabilistic primality testing;
- factor values discarded after the product was formed.

For RSA-270, which belongs to this original decimal-labelled list, the congruence

`p == q == 2 (mod 3)`

is therefore documented family metadata rather than a post-hoc inference.

The phrase “approximately the same length” is qualitative. It does not by itself provide an exact factor-bit pair or a growing number of known high bits.

---

## 2. 2026 solved-family high-bit study

A 2026-08-31 study of 22 solved formal RSA Challenge moduli (44 factors), with the original decimal-labelled and later bit-labelled populations controlled separately, reports that all 44 retained factors begin with binary prefix

`11`.

The paper interprets this as family-level evidence for high-bit conditioning or an observationally equivalent selection rule. It explicitly does **not** claim unique implementation attribution, weak-key status, or reduced factorisation resistance.

For the original-list population it also exactly recovers the documented

`p == q == 2 (mod 3)`

rule.

Importantly, after controlling for high-bit conditioning, size/label constraints and the documented residue rule, the study does not establish an additional adjacent-bit factor-balance signature. Thus the observed continuous `q/p` clustering in solved cases is not justified as an independent hard prior for RSA-270.

---

## 3. New RSA-260 factorisation is an out-of-data-freeze check

RSA-260 was publicly factored on 2026-09-03, after the 2026 high-bit paper's stated data freeze.

The published factors are

- both 431-bit primes;
- binary prefixes beginning `110...` and `111...`, so both satisfy the `11` condition;
- both congruent to `2 mod 3`;
- ratio approximately `1.1435795688`.

Thus RSA-260 is a useful time-out-of-sample consistency check for the two retained original-family features:

`prefix 11` and `2 mod 3`.

It does not create a new RSA-270 hard constraint. The high-bit property remains a construction-family inference for the unsolved member, not authenticated factor data.

---

## 4. Conditional RSA-270 bracket under the strongest simple family transfer

For a finite upper-bound diagnostic only, assume all of the following transfer to RSA-270:

1. the two factors have adjacent bit lengths `447` and `448` (consistent with an 895-bit product under balanced bit allocation plus high-bit conditioning);
2. both factors begin with prefix `11`;
3. `p<q`;
4. the documented `2 mod 3` rule holds.

Then the high-bit ranges are

`3*2^445 <= p < 2^447`,

`3*2^446 <= q < 2^448`.

Using the exact public product `N` and `q=N/p` narrows p further to the intersection

`max(3*2^445, ceil(N/(2^448-1)))`

through

`min(2^447-1, floor(N/(3*2^446)))`.

For the published RSA-270 modulus, this product-consistency intersection is only about `2.13` times narrower than the raw prefix-`11` 447-bit p interval.

Relative to an unrestricted 447-bit prime interval:

- prefix `11` supplies about one binary bit of interval shrinkage;
- exact product consistency under the assumed q-prefix contributes only about `log2(2.13)≈1.09` additional interval bits;
- the fixed class `p==2 mod3` reduces candidate density by only a constant factor 3 (about `log2 3≈1.585` bits), not the real interval width.

Even multiplying these constant reductions gives only a few bits of effective finite candidate pruning, not a quantity growing with `log N`.

This calculation is deliberately conditional and must not be presented as a proved RSA-270 factor range.

---

## 5. Comparison with the BRC phase-diagram target

The strongest external interval-search benchmark derived in the parent work needs roughly

`gamma>1/20`

for a pure localization improvement to beat exponent one fifth with linear cell evaluation. At 895 bits this is roughly 45 bits of growing magnitude localization.

Current construction information is qualitatively different:

- modulo-3 restriction: fixed modulus;
- prefix `11`: fixed number of high bits;
- approximate equal length: fixed-ratio/bit-allocation family condition;
- RSA-270 fixed collision residue `S^2 mod2880`: fixed modulus.

All of these correspond asymptotically to

`gamma=0`.

No combination of a fixed number of such conditions can cross a positive power-law localization threshold.

Freeze:

`CURRENT_RSA270_CONSTRUCTION_PRIORS -> CONSTANT_INFORMATION_ONLY`.

`CONSTANT_INFORMATION_ONLY -> gamma=0`.

---

## 6. Claim correction relative to earlier research language

Earlier RSA-270 research checkpoints occasionally referred to “fixed leading-bit patterns” or used a construction-family ratio band for finite benchmarking. Those are valid **conditional experiment priors** only to the extent stated by the relevant source/model.

The current provenance audit requires the following hierarchy:

- hard documented original-family rule: `p,q == 2 mod3` and approximately equal length;
- supported but non-hard family inference from solved moduli: high-bit prefix `11`;
- unsupported as an independent signature: tighter residual factor-balance beyond the documented/high-bit model;
- not justified from the currently audited evidence: assigning RSA-270 a long fixed binary prefix or dozens of known magnitude bits.

Future complexity claims must use this hierarchy rather than silently upgrading family evidence to exact hidden-factor data.

---

## 7. Route B decision

The pure construction-prior/magnitude-preconditioner route is closed at the current public frontier.

Reopen only if new authenticated information supplies one of:

- a factor prefix/coset whose size grows with the RSA modulus length;
- generator-specific state/seed leakage with a proved candidate-space reduction;
- a new N-only mathematical observer giving `H=N^(1/2-gamma)` for some fixed `gamma>0` at subdominant cost.

A new solved Challenge example that merely repeats the fixed `11` and `2 mod3` family signatures strengthens provenance inference but does not change the asymptotic localization exponent.

No factor of RSA-270 was recovered and no factoring speedup is claimed.