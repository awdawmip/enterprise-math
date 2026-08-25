# Odd-sector minimum gate 105 and tri-sector dual-optimal selection theorem

Status: `FREE_RESEARCH_EXACT_SELECTION_THEOREM / NOT_CANONICAL_ENTERPRISE_GEOMETRY`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- odd-sector central-fiber saturation-gate theorem;
- odd-sector first-breaker phase theorem.

Only `s=3` is the native Enterprise geometry. Other odd `s` are controlled shell-allocation comparators.

## 1. Gate notation

Let `G_s` be the complete modular saturation gate of the central s-slot even-shell packet

`P_(s,j)(m)=2s*m^2+2j*m+1`,

with `j=-(s-1)/2,...,(s-1)/2`.

Thus `G_s` is the product of every odd prime channel that kills some packet lane for every nonzero `m` residue class.

## 2. Universal lower bound for every nontrivial odd sector count

For every odd `s>=7`, the automatic primorial core contains

`3*5*7=105`,

so

`G_s>=105`.

The remaining small cases are exact:

### s=3

The automatic core is `3`.

The large-prime profile additionally saturates `5` and `7`.

Hence

`G_3=105`.

### s=5

The automatic core is `3*5=15`.

The extra channel `7` saturates.

Hence

`G_5=105`.

### s=7

The automatic core already is

`3*5*7=105`.

No extra prime in `(7,15]` saturates.

Hence

`G_7=105`.

Therefore for every odd `s>=3`:

`G_s>=105`.

## 3. Equality classification

For `s>=11`, the automatic core already contains

`3*5*7*11=1155>105`.

For `s=9`, direct Legendre-profile evaluation gives extra saturation at `11` and `13`, so

`G_9=3*5*7*11*13=15015>105`.

Therefore

`G_s=105`

iff

`s in {3,5,7}`.

Freeze:

`105 IS THE MINIMUM NONTRIVIAL ODD-SECTOR CENTRAL-FIBER GATE`.

## 4. Gate migration across s=3,5,7

The same minimum gate is assembled differently in the three equality cases:

### s=3

- automatic core: `{3}`;
- arithmetic extras: `{5,7}`.

### s=5

- automatic core: `{3,5}`;
- arithmetic extra: `{7}`.

### s=7

- automatic core: `{3,5,7}`;
- arithmetic extras: none.

So as sector count increases, the factors `5` and then `7` migrate from quadratic root-profile effects into pure lane-count coverage.

The native `s=3` case is therefore the equality case in which the largest fraction of the gate is genuinely produced by the quadratic geometry rather than automatic lane multiplicity.

## 5. Longitudinal first-breaker comparison

The audited first-breaker rules give:

### s=3

- survives channel2;
- survives channel3 by coefficient degeneration;
- first breaker is5.

### s=5

`5=1 mod4`, so first breaker is2.

### s=7

`7=3 mod4` but `3` does not divide `7`, so first breaker is3.

Thus among the three minimum-gate models:

`first_breaker(3)=5`,

`first_breaker(5)=2`,

`first_breaker(7)=3`.

## 6. Dual-optimal tri-sector selection

Every finite first breaker in the odd-curvature family is at most `5`.

Therefore `5` is the latest possible finite breaker.

Combining this with the gate minimum:

- `s=3,5,7` are exactly the odd-sector models with minimum central-fiber gate `105`;
- among them, only `s=3` attains the latest possible finite breaker `5`.

Hence:

`TRI-SECTOR s=3 IS THE UNIQUE MODEL THAT SIMULTANEOUSLY`

`(A) ATTAINS THE MINIMUM NONTRIVIAL CENTRAL-FIBER GATE 105`

`AND`

`(B) ATTAINS THE LATEST POSSIBLE FINITE LONGITUDINAL BREAKER 5`.

This is an exact two-objective selection theorem inside the controlled odd-sector family.

## 7. Relation to sector complexity

The same `s=3` is also the smallest nontrivial odd sector count.

Thus three independent optimization statements meet at the native value:

1. minimal nontrivial sector count;
2. minimal central-fiber modular gate;
3. maximal delay among models with a finite universal breaker, within the minimum-gate class.

This does not prove that three sectors are uniquely preferred under every conceivable objective. It proves a specific exact Pareto/selection statement for the two frozen arithmetic observables above.

## 8. Prior-art boundary

Primorial products, quadratic roots and residue classes are classical.

The research-specific candidate is the exact dual-objective selection induced by the odd-sector shell allocator and its longitudinal/transverse arithmetic readouts.