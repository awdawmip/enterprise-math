# Odd-sector shell allocator: central-filament arithmetic phase theorem

Status: `FREE_RESEARCH_EXACT_COMBINATORIAL_GENERALIZATION / POST_AUDIT_V2_NARROWED / NOT_CANONICAL_ENTERPRISE_GEOMETRY / EXTERNAL_NOVELTY_UNRESOLVED`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Post-audit authority: `NATIVE_FILAMENT_COUPLED_SELECTION_POST_AUDIT_V2_STATEMENT_FREEZE_20260825.md`.

Only the specialization `s=3` is the current Enterprise tri-sector model. Other odd `s` are controlled shell-allocation deformations, not canonical Enterprise geometry.

## 1. Abstract odd-sector shell allocator

Fix an odd positive integer `s`.

At shell `r>=1`, take `s` cyclic half-open blocks, each with `r` positions `t=0,...,r-1`, and allocate consecutive integers shell-by-shell and block-by-block.

The first label on shell `r` is

`B_r^(s)=1+s*r*(r-1)/2`,

and

`N_s(r,t,sigma)=B_r^(s)+sigma*r+t`.

For odd `s`, the unique central block is

`sigma_*=(s-1)/2`.

Take

`t=h+ceil(r/2)`

on the inherited admissible side-position domain. Then

`N_s(r)=h+1+(s*r^2+eps(r))/2`.

Therefore the odd-curvature coefficient is exactly

`B=s`.

## 2. Even-sector control

For even sector count, central symmetry lands on a seam. The reflected central-seam labels are

`s*r^2/2-h`

and

`s*r^2/2+1+h`,

so their difference is

`2h+1`.

Hence two nonexceptional odd primes cannot occupy the reflected seam pair simultaneously. The central parity-curvature filament mechanism therefore intrinsically selects odd sector count.

## 3. First-breaker classification

For the odd-sector central filament, with `B=s`:

- `2` is a universal breaker iff `s=1 mod4`;
- `3` is a universal breaker iff `3∤s`;
- `5` is a universal breaker iff `Legendre(s/5)=-1`;
- no prime `q>=7` is a universal breaker.

Thus the first-breaker phase is determined by `s mod60`.

Among odd residue classes modulo60:

- first breaker `2`:
  `{1,5,9,13,17,21,25,29,33,37,41,45,49,53,57}`;
- first breaker `3`:
  `{7,11,19,23,31,35,43,47,55,59}`;
- first breaker `5`:
  `{3,27}`;
- no finite universal breaker:
  `{15,39,51}`.

## 4. Exact breaker-coprime run capacities

For the three breaking phases, the exact maximal consecutive runs avoiding divisibility by the first breaker are

- breaker `2` -> `1`;
- breaker `3` -> `5`;
- breaker `5` -> `9`.

These are **breaker-coprime / divisibility capacities**, not unrestricted prime-run caps for the abstract integer family.

The blind independent audit explicitly verified this scope and warned against promoting E4 to an unrestricted prime-run theorem.

## 5. Why `s=3` is extremal

For the current Enterprise model,

`s=3`.

It avoids breaker `2` because `3=3 mod4`, avoids breaker `3` because `3|s`, and breaks at `5` because `(3/5)=-1`.

No finite universal breaker can occur after `5`, since every `q>=7` has a transparent transverse class.

Therefore among positive odd sector counts with a finite universal breaker,

`3`

is the smallest sector count attaining the latest possible finite first breaker `5`.

This gives the exact selection chain

`THREE SECTORS`

`-> CURVATURE COEFFICIENT 3`

`-> ESCAPE 2 AND 3`

`-> BREAK AT 5`

`-> BREAKER-COPRIME CAPACITY 9`.

## 6. Relation to the actual native plane

Only `s=3` inherits the native three-axis/three-sector incidence complex and seam analysis.

For `s!=3`, no `s`-sector Enterprise metric or canonical higher-sector geometry is claimed.

For `s=3`, the parent native research branch separately proves

`MAX GLOBAL TYPED-CELL PRIME-INCIDENCE ISLAND SIZE = 9`.

That actual-prime theorem is compatible with the breaker-coprime capacity `9`, but it uses additional native incidence/seam/domain structure and is not deduced solely from the one-dimensional breaker theorem.

## 7. Prior-art boundary

Shell counting, quadratic residues, Legendre symbols, CRT and periodic residue-run calculations are classical.

The external novelty candidate is only the exact geometry-selected coupling from sector count to curvature coefficient and then to the breaker phase. External novelty remains unresolved pending independent literature review.
