# Native Enterprise maximal-prime filaments：constant transverse coordinate and mod-6 channel

Status: `FREE_RESEARCH_EXACT_MULTI_CELL_FILAMENT / FINITE_CHAIN_CENSUS / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_MAXIMAL_FIVE_PRIME_FLOWER_SELF_LOCALIZATION_20260823.md`

## 1. Rolling overlap of maximal flowers

In the frozen oriented presentation, every maximal five-prime flower center lies in slot `sigma=1`.

If a maximal flower at `(r,t,1)` is followed by a neighboring maximal flower one shell outward, the next center is the inner-right prime neighbor. Exact coordinate inversion gives

- `t_{r+1}=t_r+1` when `r` is even;
- `t_{r+1}=t_r` when `r` is odd.

Therefore define

`h=t-ceil(r/2)`.

Then identically

`h_{r+1}=h_r`.

So every consecutive chain of overlapping maximal flowers lies on one constant-`h` zigzag filament through the native Cell graph.

## 2. Exact transverse residue selection

For slot `sigma=1`, the center label is

`n=B_r+r+t`.

Write `t=h+ceil(r/2)`.

### Even shell `r=2m`

Then

`n = 6m^2+h+1`,

so `n == h+1 mod 6`.

Maximal four-neighbor eligibility requires `n==5 mod 6`, hence

`h==4 mod 6`.

### Odd shell `r=2m+1`

Then

`n = 6m(m+1)+h+3`,

so `n == h+3 mod 6`.

Maximal four-neighbor eligibility requires `n==1 mod 6`, again giving

`h==4 mod 6`.

Thus for every maximal five-prime flower,

`h == 4 mod 6`.

The other five transverse residue classes are exactly forbidden.

## 3. Prime-value recovery of the filament coordinate

A maximal flower's five prime values recover

`r=(p5-p1)/12`

and its center is `p3`.

In the frozen presentation maximality already determines `sigma=1`, so

`t=p3-B_r-r`,

hence

`h=t-ceil(r/2)`.

Therefore the five prime values recover not only shell scale but the transverse filament coordinate as well.

## 4. Orientation-reversal ablation

Under global within-sector reversal, use the reversed side coordinate

`t_rev=r-1-t`.

Define

`h_rev=t_rev-ceil(r/2)`.

Independent finite checks show every reversed-allocation maximal flower again satisfies

`h_rev==4 mod 6`.

Thus the numeric value of a physical cell's side coordinate changes with presentation, but the rule "maximal flower lies in transverse class 4 modulo 6 relative to the active traversal" is presentation-equivariant.

## 5. Rolling prime sequence

A chain of `L` consecutive maximal flowers uses only `L+4` distinct primes because successive five-prime windows overlap in four values.

Let the first shell be `r`. The gap appended at shell `s` is

`d(s)=3s-4` for even `s`,

`d(s)=3s-5` for odd `s`.

Equivalently

`2d(s)=6s-9+(-1)^s`.

So a length-`L` filament produces `L+4` primes with consecutive gaps

`d(r), d(r+1), ..., d(r+L+2)`.

Every five-consecutive-prime window in this sequence is exactly one maximal flower.

## 6. Finite chain census to r<=10000

A complete sigma=1 census through `r<=10000` found

- maximal flowers: `1157`;
- every flower has `h mod 6 = 4`;
- maximal-flower chains by length:
  - length 1: `822`;
  - length 2: `132`;
  - length 3: `17`;
  - length 4: `5`;
- no length >=5 chain in this range.

This is a finite observation, not a global bound on filament length.

## 7. Geometric interpretation

The native prime distribution now has an exact two-coordinate description for this strongest local event:

`radial coordinate = shell r`,

`transverse coordinate = h=t-ceil(r/2)`.

Maximal five-prime flowers are confined to one of the six transverse residue channels:

`h=4 mod 6`,

and consecutive flowers propagate at constant `h`.

Thus the strongest observed local prime cluster does not wander freely in the 2D sector. It propagates on discrete arithmetic filaments selected jointly by native adjacency and prime residues.

## 8. Boundary

Prime k-tuples and congruence obstructions are classical. No infinitude or novelty claim is made for the underlying prime constellations.

The research-specific object is the derivation of a constant native transverse coordinate from overlapping triple-cell incidence flowers and the exact confinement of maximal flowers to one mod-6 filament class.
