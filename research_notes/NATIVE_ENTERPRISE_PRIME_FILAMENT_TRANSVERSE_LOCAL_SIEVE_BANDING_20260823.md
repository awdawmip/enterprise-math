# Native Enterprise maximal-prime filaments：transverse local-sieve banding

Status: `FREE_RESEARCH_EXACT_LOCAL_CAPACITY + FINITE_NULL_COMPARISON / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_MAXIMAL_PRIME_FILAMENT_TRANSVERSE_CLASS_20260823.md`

## 1. Starting channel

Every maximal five-prime flower lies on

`h=t-ceil(r/2) == 4 mod 6`.

This leaves one transverse class modulo 6. Refine it by the next local sieve primes 5 and 7.

## 2. Mod-210 corridor decomposition

There are exactly 35 residues `h mod 210` satisfying `h==4 mod 6`.

For each such h, enumerate `r mod 70` and count how many residue classes make all five rolling flower values nonzero modulo both 5 and 7.

Define this exact count as the local corridor capacity `C_35(h)`.

The capacities range from 1 to 35. The two maximum-capacity transverse corridors are

`h==124 mod 210`,

`h==166 mod 210`,

with

`C_35=35` out of 70 shell residues.

Thus the native filament plane naturally decomposes into bright and dark transverse corridors before any large-prime test.

## 3. Mod-30 first split

Already modulo 30, the five allowed h-classes have very different exact mod-5 capacities:

- `h mod 5 = 1 or 4`: 5 surviving `r mod 10` classes;
- `h mod 5 = 2`: 3 surviving classes;
- `h mod 5 = 0 or 3`: 1 surviving class.

Under `h==4 mod 6`, these correspond to the visible classes

`h mod 30 in {4,16,22,28,10}`.

In the exact `r<=10000` census, their maximal-flower counts are

- `h==16 mod30`: 384;
- `h==4 mod30`: 376;
- `h==22 mod30`: 241;
- `h==10 mod30`: 91;
- `h==28 mod30`: 65.

The ordering and approximate ratios follow the mod-5 local capacities.

## 4. Full mod-210 finite comparison

For every one of the 35 transverse corridors, aggregate the observed maximal-flower rate through `r<=10000`.

Comparing observed rate with the exact 5-and-7 corridor capacity gives Pearson correlation

`0.9656381441718418`.

Thus most of the visually strong transverse banding is already explained by the first two post-6 local sieve channels.

## 5. Extended finite local-null predictor

For each individual `h`, form a finite local-factor product using primes

`5<=q<=251`

and the exact number of `r mod 2q` classes on which the five flower values avoid q.

Multiply this local factor by a finite opportunity weight using the five logarithmic sizes over all valid shells through `r<=10000`.

On h-values with at least 1000 geometric opportunities:

- correlation between predicted and observed maximal-flower counts: about `0.77928`;
- after one global scale fit, standardized residual population standard deviation: about `1.0693`.

This is close to ordinary finite rare-event counting noise and does not expose a strong second transverse bias at the tested scale.

This is a diagnostic, not an asymptotic proof.

## 6. Sharp length-five corridor refinement

For a sharp length-five filament, imposing the same mod-5/7 conditions reduces the 35 h-corridors to only 9 nonempty classes modulo 210.

Their capacities over `r mod70` are:

- `h=124,166`: 7;
- `h=16`: 3;
- `h=46,64,184`: 2;
- `h=4,106,154`: 1.

The two explicit sharp filaments found so far occur in `h mod210 = 46` and `64`.

## 7. Verdict

The transverse banding is real and very clean in native coordinates, but the current evidence says it is overwhelmingly a geometric presentation of ordinary local prime-sieve structure.

Freeze:

`TRANSVERSE_BRIGHT/DARK_CORRIDORS = REAL NATIVE COORDINATE PATTERN`.

`RESIDUAL BEYOND LOCAL SIEVE = NOT DETECTED AT CURRENT SCALE`.

Therefore future work should not post-select the brightest corridor as a new prime law. The next useful target is a structural transition/readout between self-localizing prime packets that is not predicted merely by their individual local sieve capacities.
