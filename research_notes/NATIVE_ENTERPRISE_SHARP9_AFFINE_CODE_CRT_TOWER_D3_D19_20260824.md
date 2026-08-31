# Native Enterprise sharp-nine affine-code CRT tower: collapse dimensions 3 through 19

Status: `FREE_RESEARCH_EXACT_HIGH_DIMENSIONAL_CODE_TOWER / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_PRIME_INCIDENCE_CONNECTIVITY_TOWER_D2_D19_20260823.md`;
- `NATIVE_ENTERPRISE_FILAMENT_CURVATURE_FLATTENED_AFFINE_MDS_CODE_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_P_ADIC_EXCEPTION_DESINGULARIZATION_20260824.md`.

## 1. Dimension convention

Let

`p_1=2,p_2=3,p_3=5,...`

be the increasing primes.

The d=2 channels 2 and3 already select the long native sigma-1 filament family and its alternating curvature chirality.

For each `d>=3`, add the independent local divisibility channels

`p_3,...,p_d`.

This is an arithmetic collapse-channel dimension, not a Euclidean spatial dimension.

## 2. Local sharp-nine survivor basins

For a prime q and chirality `chi`, let

`N_9(q,chi)`

be the number of parameter pairs `(r,c) in F_q^2` for which all nine entries of the curvature-flattened sharp-nine affine code are nonzero modulo q.

The first local counts are:

- q=5: `1 / 1` for `chi=+/-`;
- q=7: `13 / 13`;
- q=11: `51 / 51`;
- q=13: `84 / 85`;
- q=17: `172 / 172`;
- q=19: `226 / 226`;
- q=23: `354 / 353`.

For every later prime through 67 the two chirality counts agree. Beyond the finite exceptional support they are given by

`q^2-9q+36`.

## 3. CRT product state space

Conditioned on the d=2 long-filament channel, define

`B_d^chi = product_{i=3}^d S_{p_i}^chi`,

where `S_q^chi` is the local sharp-nine survivor set of size `N_9(q,chi)`.

By CRT this is exactly the residue-state basin modulo

`M_d=product_{i=3}^d p_i`.

Hence

`|B_d^chi|=product_{i=3}^d N_9(p_i,chi)`.

The downward map

`B_d^chi -> B_{d-1}^chi`

forgets the last prime channel and has constant fiber size

`N_9(p_d,chi)`.

Thus the high-dimensional object is one exact product/collapse tower, not a collection of independently fitted plots.

## 4. The q=5 singleton collapse

At d=3 the prime-5 channel leaves exactly one sharp-nine residue state for each chirality:

`|B_3^+|=|B_3^-|=1`.

This is the code-space form of the mod-5 dual tangency theorem. The same channel that destroys every unbounded native filament also collapses the maximal-window local parameter basin to a singleton.

The next channel q=7 expands each chirality basin from one state to13 states, after which later dimensions branch by exact CRT products.

## 5. Chirality injection and freeze

The first chirality asymmetry appears at d=6 when q=13 is added:

`|B_6^+|/|B_6^-|=84/85`.

The q=17 and q=19 channels are chirality-blind, so this ratio persists through d=8.

At d=9, q=23 changes the ratio to

`(84*354)/(85*353)=29736/30005`

`~=0.9910348275287452`.

Every later channel through d=19 has equal local counts in the two chiralities. Therefore

`|B_d^+|/|B_d^-|=29736/30005`

for every

`9<=d<=19`.

In fact the same ratio remains frozen for all later prime channels because q=13 and q=23 are the only prime-level channels with unequal total survivor counts.

Thus the full high-dimensional chirality imbalance is injected at exactly two coordinates and then transported unchanged down the remaining tower.

## 6. Selected exact states

The cumulative basin sizes begin:

- d=3:
  `1 / 1`;
- d=4:
  `13 / 13`;
- d=5:
  `663 / 663`;
- d=6:
  `55692 / 56355`;
- d=9:
  `766360236096 / 773292940680`.

At d=19:

`|B_19^+|=`

`118499918922088701572595178462522612264206336`,

`|B_19^-|=`

`119571901643034419245551463874360740549754880`.

The parameter modulus is

`M_19=1309720258513377842646515`.

The corresponding basin densities inside the full parameter plane are approximately

`6.90813733596e-5`

and

`6.97063023828e-5`.

So the surviving basin becomes very thin while its absolute number of high-dimensional CRT states remains enormous.

## 7. Two different collapse phenomena at d=3

The connectivity tower and the affine-code tower meet at the same channel:

- graph level:
  q=5 changes unbounded 1D filaments into finite islands of size at most9;
- maximal-window code level:
  q=5 changes the local sharp-nine parameter plane into one residue state per chirality.

This double role is exact and is not shared by any later individual prime channel.

## 8. Interpretation

The current native high-dimensional picture is

`D2: LONG FILAMENT + C2 CHIRALITY`

`-> D3/q=5: CONNECTIVITY BREAK + SINGLETON SHARP9 BASIN`

`-> D4-D5: SYMMETRIC CRT BRANCHING`

`-> D6/q=13: FIRST CHIRALITY SPLIT`

`-> D9/q=23: FINAL CHIRALITY ADJUSTMENT`

`-> D9+: FROZEN RATIO + THINNING PRODUCT BASIN`.

This supplies a genuinely non-orthogonal 2-to-19-dimensional organization of the prime-incidence candidate space. It remains an exact coordinate/carrier theorem rather than evidence for a nonclassical prime-frequency law.
