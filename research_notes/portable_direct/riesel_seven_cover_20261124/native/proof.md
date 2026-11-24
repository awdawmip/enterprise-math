# Native BRC execution of the complete seven-cover minimum and ternary minimum

Status: actual author native execution in Research Activity `RA-D2EC212845B63844081F9A14`, Researcher `EM-DIRECT-970E1C`. The execution is shared-context implementation evidence. It is not independent project Review, formal mathematical acceptance or Foundation promotion.

## 1. Exact source and full integer state

The script reuses the portable native harness pattern from commit `f57dd6fd49d5b3f0a12abb3703c76edd6dbd37b5`, path `research_notes/portable_direct/riesel_finite_observers_20261124/native/verify_native.py`. It executes two new roots. It does not repeat the preceding binary or crossing-root trajectories.

Before any native import, the script checks the published base certificate Git blob `c1909a5e2e209b0f6bd5f613d0f758dde45caee9` and all four frozen modules from native commit `b1efc6c805661ed7b476e6e730107da6043176ee`:

| Module | Verified Git blob |
|---|---|
| `brc_transport.py` | `be1debe367263931bd5e93fd750be3ed54624fe1` |
| `brc_histogram.py` | `9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1` |
| `brc_rational_holonomy.py` | `2591640fe348da9cd7f293a957bea9ae92c82943` |
| `brc_weighted_recurrent.py` | `4e6b3132580e3cd70a20a0d8bd4d28792b961afb` |

These common identities are checked once for this execution. The old dictionary P, its exact base-two orders, the old root and its hole predicate are retained prior inputs. Their use and observed certificate identity are recorded in the output.

The native state is the full typed integer register

\[
x_n=a^2 2^n-1,
\]

starting from \(x_0=a^2-1\). The script constructs

```python
step = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
twice = step.then(step)
```

It checks the exact singleton entries: positive weight one, multiplicity one, affine action \(x\mapsto2x+1\); the native composed action is \(x\mapsto4x+3\). Every subsequent integer is obtained by calling `step.evaluate` on the entire preceding integer. Every even index also receives a separate evaluation of `twice` on the previous even-index state. The returned `WeightHistogram` is checked for the same positive singleton weight and multiplicity each time.

Each native integer is compared both with the separately advanced scalar integer recurrence and with the closed formula. The closed formula is a comparison target; it is not substituted for native state advancement.

The fixed X6 anchor is unchanged. The exponent is an arithmetic update index; prime readouts are observations, not new axes or extra BRC branches.

## 2. The two newly executed roots

The complete-classification minimum is

\[
a_{7,\min}=
168515727251568031139784117408423468924151126118048106286760549300706338389494633573.
\]

It has 84 decimal digits and uses the modulo-five completion. The minimum in the newly identified ternary family is

\[
a_{7,3}=
1046533155647696956851681902279650889819246480725727047415947079817885251912744029965820233.
\]

It has 91 decimal digits. The companion all-prime classification and exact CRT comparison establish these respective minimum scopes; native execution checks the displayed parameters and their resulting trajectories.

Both roots satisfy

\[
a\equiv a_*\pmod{6M},\qquad
a\equiv602924359709868072943
\pmod{1354510679787418425415},
\]

including the fixed R2 coordinates \(a\bmod433=0\) and \(a\bmod38737=38733\). Their difference is divisible by \(6ML_2\). All these conditions are checked before execution.

The selected supplementary rows are as follows. Here \(u=n/2\), and an indicated row has zeros at \(u=c_q\pmod{\operatorname{ord}_q4}\).

| Root | Ordered primes | Ordered u phases |
|---|---|---|
| \(a_{7,\min}\) | 5, 13, 19, 73, 631, 23311, 181 | 1, 0, 4, 1, 16, 25, 34 |
| \(a_{7,3}\) | 5, 13, 19, 73, 262657, 87211, 246241 | 1, 0, 4, 1, 16, 7, 52 |

For the first root, the three tail phases occupy w=0,3,1 modulo five. For the second, they occupy w=0,1,2 modulo three. The table follows from \(u=16+18w\), with each phase reduced modulo the applicable even-index order.

The fixed R2 observer has 31 primes. Each new trajectory adds its three free tail primes, giving **34 simultaneously observed prime channels**. Neither dictionary uses the fixed active prime 38737 to complete its tail, although its residue value remains one of the 31 fixed observations.

## 3. Complete periods actually executed

The old prime dictionary has exact base-two order least common multiple

\[
\operatorname{lcm}_{q\in P}\operatorname{ord}_q2=6720.
\]

Adding the seven selected primes gives the sufficient complete residue-value periods 20,160 and 60,480. Including all 31 fixed observations does not enlarge either period. The script verifies every relevant exact multiplicative order and calculates both least common multiples directly.

The old-hole predicate itself has the smaller proved exponent period 210. Consequently the complete coverage predicates have periods 1,260 and 3,780, respectively. The native run executes each larger residue-value period, which contains sixteen complete coverage periods:

| Trajectory | Complete coverage period | Executed complete residue-value period | Coverage periods executed |
|---|---:|---:|---:|
| 84-digit minimum | 1,260 | 20,160 | 16 |
| 91-digit ternary minimum | 3,780 | 60,480 | 16 |

These period statements concern specified readout or coverage predicates. The full integer state and its cofactors do not repeat at those periods.

Every native state supplies the actual prime hits. Counting the remaining old holes after successive selected primes gives:

| Trajectory | Counts over one coverage period | Counts over the full native execution |
|---|---|---|
| 84-digit minimum | 216, 108, 39, 26, 13, 8, 3, 0 | 3456, 1728, 624, 416, 208, 128, 48, 0 |
| 91-digit ternary minimum | 648, 324, 117, 78, 39, 26, 13, 0 | 10368, 5184, 1872, 1248, 624, 416, 208, 0 |

The full-period terminal zero proves complete coverage when combined with the verified periodic predicates. Every observed zero has a proper prime divisor: \(1<q<x_n\), and the first positive-index term already exceeds all observed primes. A private old-hole witness for every selected prime is retained with its full state and exact cofactor. Such private witnesses prove irredundancy of the selected dictionary; global supplementary minimality uses the companion six-budget lower bound.

The full seven-cover classification and its minimum comparison are separate proofs. These trajectories do not infer an all-prime theorem from finite sampling. They verify the concrete behavior predicted by that theorem. Likewise, they imply \(\tau(a^2)\le27\), without a new equality claim for the total minimum.

## 4. Native joint cofactor readouts retain the state

At every state, the script first calls the frozen native

```python
euclidean_digits(x, (q,))
```

for each of the 34 observed primes. It retains the cofactor and residue together and checks

\[
x=qQ_q+r_q,\qquad 0\le r_q<q,
\]

against scalar integer division and the exact residue formula.

It then makes a separate **native joint readout** using the entire ordered 34-prime tuple as radices. If these radices are \(q_1,\ldots,q_{34}\), the frozen function returns one cofactor J and the joint quotient-chain digits \(d_1,\ldots,d_{34}\). The retained relation is

\[
x=J\prod_{i=1}^{34}q_i
  +\sum_{i=1}^{34}d_i\prod_{j<i}q_j,
\qquad 0\le d_i<q_i.
\]

These digits are mixed-radix digits, not the independent residues \(x\bmod q_i\). The script checks both kinds of readout against the same full integer. It calls the native `recompose` on the joint cofactor/digit tuple and requires exact recovery of x at every step; scalar division by the product of the radices supplies a second check.

The certificate retains the complete final integer, the complete final joint cofactor and digits, and all 34 complete final prime cofactors. Large integers use hexadecimal strings to avoid decimal conversion limits. It also retains separate SHA256 stream digests for the full native states, the joint cofactor/digit tuples, and the individual prime residues. The private witnesses retain their full integer and cofactor as well. These records preserve the cofactor relations instead of replacing the integer state by a residue vector.

## 5. Actual operation counts

The two trajectories use the following operations:

| Operation | 84-digit minimum | 91-digit ternary minimum | Total |
|---|---:|---:|---:|
| Native one-step BRC updates | 20,160 | 60,480 | 80,640 |
| Native composed two-step evaluations | 10,080 | 30,240 | 40,320 |
| Total native effect evaluations | 30,240 | 90,720 | 120,960 |
| Native individual prime readouts | 685,440 | 2,056,320 | 2,741,760 |
| Native joint 34-radix readouts | 20,160 | 60,480 | 80,640 |
| Native joint recompositions | 20,160 | 60,480 | 80,640 |
| Scalar full-integer comparisons | 20,160 | 60,480 | 80,640 |
| Closed-form full-integer comparisons | 20,160 | 60,480 | 80,640 |

Thus the run makes **2,822,400 native `euclidean_digits` calls** in total. Each individual prime readout is also compared with scalar division and the closed residue formula; each joint readout is compared with scalar division by its full joint modulus.

The old P-coordinate comparisons total 1,612,800. Comparisons with the eleven additional fixed R2 coordinates total 887,040. The script also makes **624,960 direct coordinate comparisons** between the two executed roots: all 31 fixed channels at each index 1 through 20,160. Beyond those actual comparisons, the common root congruence proves equality of all 31 residue-value trajectories for every future arithmetic index.

The all-future argument is the elementary identity

\[
a\equiv a'\pmod q
\quad\Longrightarrow\quad
a^2 2^n-1\equiv(a')^2 2^n-1\pmod q
\qquad(n\ge0).
\]

Neither finite equality of observations nor this infinite congruence equality identifies the two full integers. The integer states and joint cofactors remain distinct and explicitly retained.

## 6. Reproduction and scientific scope

Run from the retained workspace or repository layout:

```sh
python verify_native.py --source-dir /path/to/pinned_source
```

The source directory contains `enterprise_math/` with the four pinned modules. Matching `src/` or `vendor_src/` is detected automatically. The two original roots, their phase rows and expected counts are explicit in the script. The prior base and old-hole certificates remain at their established repository paths.

The generated `native_certificate.json` records exact source identities, the two complete executed periods, all operation counts, the full terminal states and joint readouts, private witnesses and stream digests. It is actual native execution evidence for these two representatives. Classification, all-prime necessity, minimum scope and the interpretation within the fixed-X6 integer register remain tied to their respective analytic arguments and stated evidence boundaries.
