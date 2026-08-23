# Native Enterprise maximal five-prime flower：prime-valued self-localization

Status: `FREE_RESEARCH_EXACT_PRIME_SPECIFIC_MULTI_CELL_READOUT / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_SEVEN_CELL_STAR_POISSON_SELF_LOCALIZATION_20260823.md`

## 1. Question and corrected priority

The 13-state loop code uses only prime/composite Boolean bits. This note studies a stronger multi-Cell packet that uses actual prime values and recovers native shell information from a maximal local flower.

Later audit identified a smaller prime-valued localizer: one ordered fully-prime triple-cell incidence already recovers `(r,t,sigma)` from its three prime values. Therefore this five-prime flower is **not** the first/minimal non-Boolean prime-valued readout. Its distinct role is stronger presentation robustness after sorting, maximal local prime occupancy, and propagation into constant-`h` filaments.

## 2. At most four prime neighbors

For a center Cell label `n>3` prime, reduce the six neighbor formulas modulo 6. Since every prime greater than 3 is `+1` or `-1 mod 6`, a neighbor is prime-eligible only if its residue is in `{1,5}`.

Complete enumeration of

- `sigma in {0,1,2}`;
- `r mod 6`;
- `n mod 6 in {1,5}`

shows that at most four of the six neighbors are prime-eligible.

Equality occurs exactly in the current oriented presentation when `sigma=1` and

- `r` even with `n == 5 mod 6`, eligibility word `011110`;
- `r` odd with `n == 1 mod 6`, eligibility word `110011`.

Therefore a center prime can have at most four prime nearest neighbors. A local prime star has at most five prime Cells including its center.

The two corresponding bright-incidence loop signatures are `011100` and `100011`, the two weight-three states of the 13-state loop code.

## 3. Maximal five-prime flower

Call a center plus four prime neighbors a **maximal five-prime flower**.

Let its five prime labels, sorted numerically, be

`p1 < p2 < p3 < p4 < p5`.

For every maximal flower, the center is exactly

`p3=n`.

### Even shell

For even `r`, the five values are

`n-6r+6`,

`n-3r+2`,

`n`,

`n+3r+2`,

`n+6r+6`.

Hence the gap word is

`(3r-4, 3r-2, 3r+2, 3r+4)`.

### Odd shell

For odd `r`, the five values are

`n-6r+6`,

`n-3r+1`,

`n`,

`n+3r+1`,

`n+6r+6`.

Hence the gap word is

`(3r-5, 3r-1, 3r+1, 3r+5)`.

## 4. Prime-only recovery of shell scale

In both parity classes,

`p5-p1 = 12r`.

Therefore the native shell index is recovered from the five prime values alone:

`r=(p5-p1)/12`.

No composite-neighbor labels, shell table or pre-attached coordinate tag is required.

This is strictly richer than the Boolean loop signature: the same weight-three brightness type occurs at many shells, while the actual prime quintuplet recovers the shell scale exactly.

## 5. Nested prime curvature code

The outer symmetric second difference is universal:

`p1 - 2*p3 + p5 = 12`.

The inner symmetric second difference is

`p2 - 2*p3 + p4 = 4` for even `r`,

`p2 - 2*p3 + p4 = 2` for odd `r`.

Thus

`p2 - 2*p3 + p4 = 3 + (-1)^r`.

So the same five primes recover both

1. shell magnitude `r` from the outer diameter;
2. shell parity from the inner curvature.

This gives the exact prime-valued local readout

`FIVE PRIME VALUES -> (SHELL SCALE, SHELL PARITY)`.

## 6. Finite census

Under the frozen forward allocation:

- through `r<=1500`: 74 maximal flowers;
  - 42 even-shell / inner-curvature 4;
  - 32 odd-shell / inner-curvature 2;
- through `r<=3000`: 186 maximal flowers;
  - 106 even;
  - 80 odd;
- through `r<=5000`: 400 maximal flowers;
  - 219 even;
  - 181 odd.

Every event satisfies the exact gap and curvature formulas above.

## 7. Presentation ablation

A global reversal of the within-sector side traversal changes which physical cells receive which labels and swaps the raw loop-bit presentation, but the sorted maximal-flower identities survive:

- `p5-p1=12r`;
- outer curvature `12`;
- inner curvature `4` for even `r`, `2` for odd `r`;
- the parity-dependent gap words above.

Hence the prime-valued self-localization is stronger under orientation ablation than the raw six-bit loop signature.

The absolute sector slot in which maximal eligibility appears remains presentation-dependent and is not promoted as an invariant.

## 8. Interpretation

The five-prime flower is a **nonminimal but stronger composite packet** in the prime-valued hierarchy.

The five prime values themselves carry a native geometric coordinate:

`MAXIMAL PRIME FLOWER VALUES -> NATIVE SHELL INDEX`.

Compared with the smaller triple-prime incidence localizer, it additionally supplies maximal local occupancy, a sorted orientation-robust shell diameter, parity curvature, and the seed for constant-`h` rolling filaments.

It is still an exact consequence of the frozen integer allocation and local incidence formulas; no claim is made that it constitutes a new theorem about the classical primes independent of this coordinate system.

Current verdict:

`MAXIMAL_FIVE_PRIME_FLOWER_SELF_LOCALIZATION = MAXIMAL LOCAL PRIME PACKET + FILAMENT SEED; MINIMAL PRIME-VALUED LOCALIZER IS THE TRIPLE-PRIME INCIDENCE`.
