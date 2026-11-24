# Native BRC verification of the cost-eight root in the fixed 43-channel fiber

Date: 2026-11-24. This note records actual author-level native execution of the new compact root. The existing research identity and Activity are retained by the integrating research session. The calculation is collaborative implementation evidence, not independent project Review or formal acceptance.

## 1. Executed object and frozen implementation

The root is

```text
125881617004399660936368886076947194311916726055055408371127347321463572549463017011507634869211696849333543777014426253559019210427608296334538652533279482688323
```

It has 162 decimal digits. The construction certificate identifies it as the smallest positive root of its eight explicitly constructed CRT progressions. Exact supplementary cost eight follows from that construction and the complete seven-prime classification on R2. For this compact root, the total-cover conclusion is \(\tau(a^2)\le28\).

The full native state is

\[
x_0=a^2-1,\qquad x_n=a^2 2^n-1.
\]

The script constructs a native positive singleton effect

```python
step = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
twice = step.then(step)
```

and checks the weight and multiplicity are both one. Each new integer is produced by `step.evaluate` on the preceding full integer. At every even index, `twice.evaluate` on the previous even-index state separately checks the native composed action \(4x+3\). Both results are compared with the scalar recurrence and the closed formula. Formula evaluation is a check, not the source of native state advancement.

The unchanged X6 anchor carries this typed integer register. Exponent indices and prime channels remain arithmetic indices and readouts of the state; no new spatial axis or BRC branch is introduced.

The implementation is frozen at Enterprise Math commit
`b1efc6c805661ed7b476e6e730107da6043176ee`.
Before import, the four module bytes were verified once against these Git blobs:

| Module | Git blob |
|---|---|
| `brc_transport.py` | `be1debe367263931bd5e93fd750be3ed54624fe1` |
| `brc_histogram.py` | `9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1` |
| `brc_rational_holonomy.py` | `2591640fe348da9cd7f293a957bea9ae92c82943` |
| `brc_weighted_recurrent.py` | `4e6b3132580e3cd70a20a0d8bd4d28792b961afb` |

The execution adapts the established seven-cover native harness. The old P dictionary, its exact orders, and its period-210 hole predicate are inherited scientific inputs; the script independently checks the orders and all actual states used here.

## 2. Eight selected channels and the executed coverage period

Writing \(n=2u\), the supplementary rows are:

| Prime | Base-two order | u phase |
|---:|---:|---:|
| 5 | 4 | 1 |
| 13 | 12 | 0 |
| 19 | 18 | 4 |
| 73 | 9 | 1 |
| 38737 | 72 | 34 |
| 246241 | 108 | 34 |
| 33975937 | 216 | 16 |
| 138991501037953 | 216 | 52 |

Here a u phase is interpreted modulo \(\operatorname{ord}_q4\). On the final residual coordinate \(u=16+18w\), the last four rows occupy \(w=1\bmod2\), \(w=1\bmod3\), \(w=0\bmod6\), and \(w=2\bmod6\), respectively.

The old-P hole predicate has exponent period 210. Combining it with the exact selected zero-phase periods gives

\[
L_{\mathrm{cover}}=\operatorname{lcm}(210,4,12,18,9,72,108,216)=7560.
\]

**The native execution advances every index from 1 through 7,560.** It completes one full period of the covering predicate. The separate sufficient complete prime-residue-value period, computed from all observed prime orders, is 60,480; this native execution does not run that larger interval. Indeed, the final observed residue vector at index 7,560 differs from its initial value.

For every actual state, the native prime readouts determine which primes hit. The uncovered counts after adding successive rows are:

| Supplementary budget along this route | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Uncovered indices among 1,...,7,560 | 1,296 | 648 | 234 | 156 | 78 | 39 | 26 | 13 | 0 |

These are this specified nested route's counts; no optimal-density claim at each intermediate budget is needed. Every observed zero is a proper prime divisor, and the first positive-index integer already exceeds every observed prime.

The execution found and retained a private old-hole witness for each of the eight supplementary primes at indices

\[
(6,12,152,20,140,392,32,320)
\]

in the displayed prime order. It also retained private witnesses for all 28 primes of the selected full dictionary. Each witness includes its complete integer and prime cofactor in hexadecimal. These witnesses establish irredundancy of the displayed dictionary; global supplementary minimality comes from the all-seven-cover theorem.

## 3. Forty-five prime observations and lossless joint readout

The root belongs to the previously fixed R3 fiber. Its 43 fixed coordinates consist of the 31 R2 primes and the twelve primes of the exact seven-budget observer. Adding the two new order-216 primes gives 45 observed primes.

At each index, the native routine `euclidean_digits(x, (q,))` supplies the cofactor and independent residue for each q. The script checks

\[
x=qQ_q+r_q,
\qquad 0\le r_q<q,
\]

against scalar division and the exact residue formula. All 43 fixed-coordinate residues are also directly compared with the separately advanced scalar trajectory of the fixed R3 base

```text
191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
```

The difference between this base and the new root is divisible by the full R3 progression modulus. This congruence proves equality of all 43 observed future trajectories; the execution checks 325,080 coordinate equalities over the actually executed interval.

A separate native 45-radix call returns a joint cofactor J and mixed-radix digits \(d_i\). For the ordered observed primes \(q_i\), the script verifies

\[
x=J\prod_{i=1}^{45}q_i+
\sum_{i=1}^{45}d_i\prod_{j<i}q_j,
\qquad 0\le d_i<q_i.
\]

The native `recompose` function recovers x exactly at every index. These quotient-chain digits are distinguished from the independent residues \(x\bmod q_i\); both readouts retain the same complete integer.

## 4. Actual operation counts and retained certificate

| Operation | Executed count |
|---|---:|
| Native one-step BRC updates | 7,560 |
| Native composed two-step evaluations | 3,780 |
| Native effect evaluations in total | 11,340 |
| Native individual prime quotient/remainder readouts | 340,200 |
| Native joint 45-radix readouts | 7,560 |
| Native joint recompositions | 7,560 |
| Native `euclidean_digits` calls in total | 347,760 |
| Scalar full-integer comparisons | 7,560 |
| Closed-form full-integer comparisons | 7,560 |
| Direct fixed-43-coordinate reference comparisons | 325,080 |

Every individual readout additionally has a scalar division and a closed residue-formula comparison. Every joint readout has a scalar division comparison by the product of its 45 radices.

The complete final integer has **8,631 bits**. `native_cost8_certificate.json` retains that full integer, the final scalar reference integer, all 45 final prime cofactors and residues, the full final joint cofactor and digit vector, all private witnesses, and three stream digests for the native integers, joint quotient-chain readouts and individual prime residues.

The native integer-stream SHA256 is

```text
f0a0613ff13fcd28c9b55ee9c79f170e71e0dd60ed4c82d98f9d0180aa798ba5
```

The script finished with `PASS`. The terminal zero uncovered count, together with the proved periodic predicate, verifies complete coverage of this concrete root. The cost-eight existence proof and the separate coprimalized total-cost-28 construction remain their respective mathematical arguments; the large coprimalized root was not rerun through this native trajectory.

## 5. Reproduction

```sh
python verify_native_cost8.py --source-dir /path/to/frozen/source
```

The source directory contains the pinned `enterprise_math/` package. In a complete repository layout, a matching ancestor `src/` or `vendor_src/` is detected automatically. The calculator embeds the exact mathematical constants and orders, so it does not depend on an old workspace's absolute file paths. It produces `native_cost8_certificate.json`, or the path supplied by `--output`.

The four native modules must match the declared frozen scientific identities. The new-prime primality and exact construction data are reused from the companion cost-eight proof and its deterministic arithmetic certificate.
