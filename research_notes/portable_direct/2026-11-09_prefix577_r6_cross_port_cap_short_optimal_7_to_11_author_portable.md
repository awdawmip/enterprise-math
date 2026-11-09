# BRC-X6: exact cross-source cap lemma and compact full-positive 7–11 minimal decompositions

Date: 2026-11-09. Status: `AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED`.
Frozen science: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Native observation: 96 ports, 6 labeled actions each, 9 frozen roots, the complete signed joint atom `(next_port, R1..R6, K)`. Four source ports `(6,7,28,29)` with signs `(+,-,-,+)`. The 38 admissible deterministic controls are the lexicographically ordered four-tuples preserving the signed atoms on every frozen root.

## Cross-source maximum-mass residual theorem

For any convex mixture of deterministic six-action policies (x=∑_{i=1}^{m} w_i v_i) with (w_i>0), and for two distinct source ports p and q, assume each of the six action masses at q is positive. Define

```text
M_p = max_{a=0..5} x[p,a]
h_pq = #{ a in {0,...,5} : x[q,a] > M_p }.
```

Then **the exact minimum number of deterministic policies is at least `6+h_pq`**. Proof: each coefficient w_i is contained in exactly one positive cell at p, so w_i <= M_p. Each q-action cell heavier than M_p requires at least two coefficients. Every other strictly positive q-cell requires at least one; the pure-policy index sets contributing to different q-cells are disjoint. Thus m >= 2h_pq+(6-h_pq) = 6+h_pq.

This is a source-labeled BRC mass-residual lower bound. It uses the complete marginal action rows to establish a combinatorial obstruction; the exact signed native joint observer is retained and separately checked for the upper-bound constructions.

## Complete exact witnesses

Each displayed 4x6 integer table below has common denominator D. Row order is (6,7,28,29); action labels are original zero-based 0..5. All 24 cells are strictly positive. The positive integer coefficients of the exact convex mixture are listed by canonical 38-policy index; division by D yields weights. The index-to-native-four-action-tuple map appears below.

| Exact minimal m | D | Port p | Port q | max_a D*x[p,a] | # heavy cells q |
|---:|---:|---:|---:|---:|---:|
| 7 | 8 | 6 | 7 | 2 | 1 |
| 8 | 10 | 6 | 7 | 2 | 2 |
| 9 | 12 | 6 | 29 | 2 | 3 |
| 10 | 18 | 6 | 29 | 3 | 4 |
| 11 | 36 | 6 | 29 | 6 | 5 |

### m=7, denominator D=8

```text
 1  1  1  1  2  2
 3  1  1  1  1  1
 2  2  1  1  1  1
 1  1  3  1  1  1
```

Explicit native vertex weights: `6:1, 8:1, 15:1, 21:1, 23:1, 29:1, 30:2` (divide by 8).

### m=8, denominator D=10

```text
 2  2  1  1  2  2
 3  3  1  1  1  1
 2  2  2  2  1  1
 1  1  3  3  1  1
```

Explicit native vertex weights: `5:2, 8:1, 10:1, 15:1, 21:1, 23:1, 29:1, 30:2` (divide by 10).

### m=9, denominator D=12

```text
 2  2  2  2  2  2
 3  1  2  2  3  1
 2  4  2  2  1  1
 3  3  3  1  1  1
```

Explicit native vertex weights: `6:2, 8:1, 10:1, 13:2, 20:1, 21:1, 23:1, 29:1, 30:2` (divide by 12).

### m=10, denominator D=18

```text
 3  3  3  3  3  3
 5  4  3  3  2  1
 5  6  2  3  1  1
 4  4  4  4  1  1
```

Explicit native vertex weights: `4:1, 5:2, 8:1, 10:2, 13:3, 17:2, 20:1, 23:2, 29:1, 30:3` (divide by 18).

### m=11, denominator D=36

```text
 6  6  6  6  6  6
 7  7  6  6  7  3
 6 10  6  6  7  1
 7  7  7  7  7  1
```

Explicit native vertex weights: `5:4, 6:2, 8:1, 10:5, 13:4, 15:2, 20:5, 21:1, 23:3, 29:3, 30:6` (divide by 36).

### Native four-action tuples for all used vertex indices

```text
 4 : (0,0,5,5)
 5 : (0,1,2,3)
 6 : (0,4,2,0)
 8 : (1,0,3,2)
10 : (1,4,3,0)
13 : (2,2,1,1)
15 : (2,2,4,4)
17 : (3,3,0,0)
20 : (3,3,4,4)
21 : (3,3,5,5)
23 : (4,1,0,3)
29 : (4,5,0,1)
30 : (5,0,1,2)
```

All five mixtures have exactly m distinct positive admissible policies. The lower-bound observer has h=m-6, so `minSupport=m` exactly in every case. The original native frozen edge function verifies every listed policy against all 9 roots and every whole mixture against the 7-variable signed joint observation. No scalar quotient was substituted for the original validation.

## Integer-denominator threshold within this certificate method

For full-positive 6-cell rows with common integer denominator D, the integer numerator of M_p is at least ceil(D/6). To have h q-cells above M_p, integer positivity requires

```text
D >= h*(ceil(D/6)+1) + (6-h).
```

For h=1,2,3,4,5 the smallest integer denominators satisfying this necessary inequality are respectively **8, 10, 12, 18, 36**. The five native witnesses above attain these bounds. Hence these witnesses have denominator-optimal *cross-port cap certificates*. The statement does not claim a global minimum denominator across all different potential lower-bound arguments.

Compared with prior author portable evidence, the 9-term full-positive instance improves denominator 24 to 12, the 10-term instance replaces a 127-bit base-14 denominator by 18, and the 11-term instance replaces a 141-bit denominator by 36. Prior exact 12/13-term witnesses remain valid.

## Exact reproducibility, provenance and follow-up

Portable archive: `BRC_X6_CROSS_PORT_CAP_7_TO_11_AUTHOR_PORTABLE_20261109.zip`; SHA-256 `83a56cc76e40518bf47a07528c441ad5658774f3022e0a31abc576b133bf616e`. The archive contains: original frozen `frozen_native_kernel_prefix577.py`, `verify_cross_port_cap.py`, `CROSS_PORT_CAP_CERTIFICATE.json`, full local theorem and manifest. Certificate SHA-256 `d24295ed5a1ac79a9c5dda82dfdca9faa1ab8535c1e749b2fe03fb825c53a7cd`. Re-extracted stdlib exact verification `EXACT_PASS` and bytewise certificate match.

Proof boundary: the theorem holds for the declared deterministic-mixture carrier; the numeric results hold on the frozen 9-root signed-native kernel. Original D25 H0/B0, Frobenius and CM Source frontier remains untouched. The original read-only D25 continuation request `h40-r11-d25-exact-continuation-20261109t0137-read-v1` previously returned SUCCEEDED but `execution_authorized=false`; this author-side publication has no Source CLAIM, native Task checkpoint, Result or Driver admission. UR original four-file V2 package remains sought by exact 94,687-byte size and SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`, with no match in the checked local files.

Next scientific unit: formulate and test an exact two-/three-port joint-incidence residual for short 12/13-term witnesses, preserving the native signed observer and the frozen source pin. Existing 7..11 certificates are retained as the do-not-repeat baseline.
