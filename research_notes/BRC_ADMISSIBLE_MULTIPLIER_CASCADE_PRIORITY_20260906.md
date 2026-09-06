# BRC Admissible Multiplier Cascade and Priority Audit — Round 6

Status: `PROVED SAFE PRUNING / PROVED m->m+2 TRANSPORT / STATIC STRONG SQUARE FILTER / EXPERIMENTAL PRIORITY HEURISTIC / NO ASYMPTOTIC FACTORIZATION CLAIM`
Date: `2026-09-06`
Parent tools: `t0.brc_multiplier_basin`, `t0.brc_multiplier_transition`, `t0.brc_square_gap_prefilter`

## 1. Question

After replacing repeated `sqrt(mN)` evaluations by BRC root/remainder transport, can the `m=1..100` multiplier scan be reduced further without discarding any immediate difference-of-squares witness?

Two distinct layers were tested:

1. **safe deterministic pruning/filtering** — theorem/certificate level;
2. **multiplier priority** — experimental ordering only.

The factoring surface remains classical multiplier-Fermat / Lawrence-Lehman-Hart difference-of-squares mathematics. The BRC-specific contribution is exact retained-state transport and typed composition with the classical filters.

## 2. Safe parity deletion: 100 multipliers -> 75

For odd `N`, if `m == 2 (mod 4)` then `mN == 2 (mod 4)`. Integer squares are only `0` or `1 mod 4`, hence a difference of two squares is only `0,1,3 mod 4`.

Therefore `m == 2 (mod 4) -> NO x,y with x^2-y^2=mN`.

Exactly 25 multipliers in `1..100` are deleted with zero loss. The admissible path is `1,3,4,5,7,8,9,11,...,99,100`.

The previous consecutive BRC recurrence still handles one-step moves. The only new transport needed is `m->m+2` for source `m=1,5,9,...,97`.

## 3. Exact m->m+2 BRC transport

Write `mN = J^2 + R`, `0<=R<=2J`.

For a safe skip set `beta=sqrt((m+2)/m)`, `gamma=beta-1`, `C=floor(2^B gamma)`, `d0=floor(CJ/2^B)`, with the same precision rule as the existing consecutive theorem.

Since `J/2^B<1/2`, `d0 <= gamma J < d0+3/2`.

Also `beta<=sqrt(3)` on the maximal jump `1->3`. Writing `sqrt(mN)=J+delta`, `0<=delta<1`, `sqrt((m+2)N)=J+gamma J+beta delta` lies below `J+d0+3.232...`.

Thus `J_(m+2)-(J+d0) in {0,1,2,3}`.

The provisional exact remainder is `G0 = R + 2N - d0(2J+d0)`. Subtract successive odd basin widths `2a+1` until the remainder is in its basin. At most three corrections occur. No new `N`-dependent square root is used.

The static fast path adds only 25 high-precision constants (6425 raw bytes) for the skip transitions. Ordinary one-step transitions reuse the existing 99-entry table.

## 4. Strong two-table square filter

The previous strong single table was `M=20160`, with 576 square-residue classes. A second coprime modulus was selected: `46189 = 11*13*17*19`. It has exactly 3780 quadratic-residue classes and a packed payload of 5774 bytes.

A true integer square must pass both tables, so the cascade has zero false negatives. For uniformly distributed residues the exact pass fraction is

`(576/20160)*(3780/46189) = 108/46189 = 0.002338219...`.

Thus the uniform rejection rate is about `99.766178%`.

This does **not** mean a structured factor-search population always rejects 99.77%: true square gaps are deliberately overrepresented in a hit-rich benchmark and must pass.

### Structured semiprime benchmark

Population: every distinct prime pair `101<=p<q<=997`; 10,153 semiprimes; 100 multipliers each; 1,015,300 candidate gaps.

Observed:

- actual square gaps: `29,798`;
- actual square gaps at excluded `m == 2 mod 4`: `0`;
- mod-20160 survivors: `46,372`;
- two-table survivors: `29,804`;
- two-table false negatives: `0`;
- nonsquare false positives after the cascade: only `6`.

So on this deliberately hit-rich population the cascade reduces exact square tests from 46,372 to 29,804, essentially the irreducible 29,798 true hits.

## 5. Whole-pipeline timing

Compared:

1. `direct`: fresh `isqrt(mN)` and fresh gap `isqrt` for all `m=1..100`;
2. `current`: Round-5 all-100 BRC transition + mod-4032 filter;
3. `new`: 75-state admissible BRC path + mod-20160/mod-46189 cascade.

Current-environment finite medians:

| N bits | new/direct | new/current |
|---:|---:|---:|
| 128 | 1.33x | 1.26x |
| 256 | 1.61x | 1.08x |
| 512 | 2.26x | 1.27x |
| 1024 | 2.36x | 1.20x |
| 2048 | 2.46x | 1.29x |
| 4096 | 2.32x | 1.34x |

These are Python implementation timings only. They are not asymptotic complexity claims.

## 6. Multiplier-priority heuristic

For a divisor split `uv=m`, the classical immediate-hit identity can be oriented so `u/v` approximates `q/p`. The immediate ceiling condition is equivalent to `(uq-vp)^2 < 4(uq+vp-1)`.

Near the balance center, the admissible ratio interval has an `m^(-1/4)` scaling up to the unknown-ratio factor. Define

`nu(m) = # {(u,v): uv=m, u>v>0, u==v (mod 2)}`.

Use the exact ranking proxy `score(m)=nu(m)^4/m`, order-equivalent to `nu(m)/m^(1/4)`. Force `m=1` first because the near-equal factor case is qualitatively important.

For `m<=100` the order begins `1,96,45,48,63,72,75,15,80,99,21,24,27,32,33,...`.

For semiprimes that actually have at least one immediate hit in the admissible set:

| prime range | sample | hittable | ascending mean/median rank | heuristic mean/median rank |
|---|---:|---:|---:|---:|
| 101..997 | all 10,153 | 9,696 | 16.91 / 12 | 7.48 / 5 |
| 1009..9999 | 20,000 | 10,949 | 31.39 / 29 | 13.49 / 10 |
| 10007..99999 | 20,000 | 3,510 | 32.02 / 30 | 13.51 / 10 |
| 100003..999999 | 20,000 | 1,095 | 32.23 / 30 | 12.96 / 9 |

Mean first-hit rank improves by `2.26x..2.49x` on those hittable subsets.

### Kill boundary

The fraction of semiprimes immediately hittable at all falls rapidly as factor scale grows in these finite samples: `95.5% -> 54.7% -> 17.6% -> 5.5%`.

A separate 1000-sample probe with random 32-bit prime factors produced only two `m<=100` immediate hits; a 200-sample probe with random 64-bit prime factors produced zero.

Therefore the priority rule is **not** a general RSA shortcut. It only reorders the classical multiplier-Fermat surface when such a hit already exists. The project should not infer asymptotic factorization progress from the rank improvement.

## 7. Prior-art boundary

Lehman's 1974 algorithm systematically chooses small rational factor ratios in a Lawrence/Fermat difference-of-squares framework. Hart's 2012 one-line factoring algorithm is another multiplier-Fermat variant and explicitly discusses modular square tests/table lookups and practical multiplier choices.

Accordingly: parity pruning is classical; quadratic-residue cascade is classical; divisor-ratio priority rationale is a classical-search-derived heuristic; `m->m+2` retained `(J,R)` transport is the new BRC application/result in this round.

No novelty claim is made for the factoring principle or the multiplier-ratio idea.

## 8. Next frontier

The immediate-ceiling surface is now highly optimized but is too sparse at large factor scales. The next meaningful attack is therefore **not** another ordering tweak.

Open the second coordinate `x = ceil(sqrt(mN)) + t`, `t>=0`, with exact update `D_(t+1)=D_t+2x+1`.

This creates a two-dimensional `(m,t)` BRC lattice. The next question is whether the existing multiplier transport and square-residue cascade can implement a Lehman-style search rectangle with lower constant cost or a new typed pruning invariant. Any complexity claim must be compared directly with classical Lehman/Hart bounds.
