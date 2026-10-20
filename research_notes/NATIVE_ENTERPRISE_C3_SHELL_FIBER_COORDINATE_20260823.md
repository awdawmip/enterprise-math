# Native Enterprise C3 shell-fiber coordinate for integer/prime allocation

Status: `FREE_RESEARCH_EXACT_COORDINATE_CANDIDATE / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_C3_SHELL_AP_RECOALESCENCE_RESONANCE_20260823.md`

## 1. Half-open sector convention

For every nonzero canonical Enterprise address `(a,b,c)` with `min(a,b,c)=0`, use the oriented half-open sector convention:

- slot `sigma=0`: `c=0` and `a>0`;
- slot `sigma=1`: `a=0` and `b>0`;
- slot `sigma=2`: `b=0` and `c>0`.

This assigns the three positive axes uniquely:

- `E1=(r,0,0)` to slot 0;
- `E2=(0,r,0)` to slot 1;
- `E3=(0,0,r)` to slot 2.

No nonzero canonical address is duplicated.

## 2. Shell-fiber coordinate

Define

`r=a+b+c`.

Then define the side coordinate `t` by

- slot 0: `t=b`;
- slot 1: `t=c`;
- slot 2: `t=a`.

Every nonzero address therefore has a unique coordinate

`(r,t,sigma)`

with

`r>=1`, `0<=t<r`, `sigma in {0,1,2}`.

The inverse is exact:

- `sigma=0`: `(a,b,c)=(r-t,t,0)`;
- `sigma=1`: `(a,b,c)=(0,r-t,t)`;
- `sigma=2`: `(a,b,c)=(t,0,r-t)`.

Thus

`A_E \ {0} <-> {(r,t,sigma): r>=1, 0<=t<r, sigma in C3}`

as a discrete address bijection under the chosen oriented presentation.

## 3. Integer label

Let

`B_r=3r(r-1)/2+1`.

Under the tri-sector shell allocation, the positive integer at `(r,t,sigma)` is

`N(r,t,sigma)=B_r+t+sigma*r`.

Hence cyclic sector rotation is arithmetic translation by one shell index:

`N(r,t,sigma+1)-N(r,t,sigma)=r`.

For fixed `(r,t)`, the C3 fiber is exactly

`{B_r+t, B_r+t+r, B_r+t+2r}`.

## 4. Inverse integer-to-coordinate map

Shell `r` contains the consecutive integer block

`B_r <= n <= 3r(r+1)/2`.

Therefore every positive integer `n` has a unique shell `r`, found as the least positive integer satisfying

`n <= 3r(r+1)/2`.

Set

`j=n-B_r`.

Then

`sigma=floor(j/r)`,

`t=j mod r`.

The formulas in section 2 recover the unique Enterprise address.

So the allocation is not merely a picture: it is a reversible integer-coordinate transform.

## 5. C3 fold as a native collapse

Define

`Fold_C3(r,t,sigma)=(r,t)`.

This forgets only the cyclic sector slot. Every non-origin fiber has exactly three states. The collapse readout preserves shell and side position and identifies the three cyclic alternatives.

Define prime-fiber brightness

`b(r,t)=sum_{sigma=0}^2 1_prime(N(r,t,sigma))`.

Thus

`b(r,t) in {0,1,2,3}`.

A fully bright C3 fiber has `b=3`.

Define whole-shell C3 prime resonance

`T(r)=#{t in [0,r-1]: b(r,t)=3}`.

The exact results already obtained become statements directly in these coordinates:

- `b(r,t)=3` with all values >3 implies `6|r`;
- the reflection-fixed midpoint `t=r/2` can have `b=3` only when `210|r`;
- at such a midpoint all three pre-collapse labels are `1 mod 210`;
- `T(r)` is enhanced when the native shell index carries additional small prime factors.

## 6. Presentation status

The full slot label `sigma` depends on the chosen cyclic start-axis/orientation presentation. Cyclic relabeling only translates `sigma` and leaves the folded coordinate `(r,t)` unchanged under the same orientation. Orientation reversal can change the side parameterization; the midpoint `t=r/2` is fixed and is therefore especially presentation-stable.

Hence:

- `(r,t,sigma)` is a convenient exact presentation coordinate;
- `(r,t)` is the C3-fold coordinate;
- the equal-coordinate midpoint fiber is the strongest current presentation-stable prime-pattern candidate.

This coordinate is a research candidate derived from the native tri-sector allocation. It is not promoted here to canonical Enterprise foundation.
