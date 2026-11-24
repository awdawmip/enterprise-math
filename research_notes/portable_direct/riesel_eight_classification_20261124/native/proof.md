# Native execution of the globally smallest cost-eight R3 root

Date: 2026-11-24, Asia/Hong_Kong. This note records actual execution in the continuing author research Activity `RA-D2EC212845B63844081F9A14`, Researcher `EM-DIRECT-970E1C`.

## 1. Native object and scientific source

The root is the 146-digit global minimum proved in `../minimum/proof.md`:

```text
25391491002591320391732108159477707323814206756039394016382357924666368039179689189103105696777816709091120408108658618711788120139363377072408503
```

The fixed Heartbeat X6 anchor carries the full typed integer register x_0=a^2-1. A positive singleton BRC has weight and multiplicity one and advances x to 2x+1. The native composed effect advances x to 4x+3. Each native result is checked against the full scalar recurrence and the closed form a^2 2^n-1.

The implementation remains frozen at Enterprise Math commit `b1efc6c805661ed7b476e6e730107da6043176ee`. Before import the calculator checks these exact Git objects:

| Module | Blob |
|---|---|
| brc_transport.py | be1debe367263931bd5e93fd750be3ed54624fe1 |
| brc_histogram.py | 9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1 |
| brc_rational_holonomy.py | 2591640fe348da9cd7f293a957bea9ae92c82943 |
| brc_weighted_recurrent.py | 4e6b3132580e3cd70a20a0d8bd4d28792b961afb |

The harness is adapted from the preceding verified cost-eight native execution. The root, its two new channels, their exact orders and the selected phases are changed explicitly; the full-state and cofactor semantics are retained.

## 2. Selected route and its complete covering period

Writing n=2u, the supplementary rows are:

| Prime | Base-two order | u phase |
|---:|---:|---:|
| 5 | 4 | 1 |
| 13 | 12 | 0 |
| 19 | 18 | 4 |
| 73 | 9 | 1 |
| 38737 | 72 | 34 |
| 487824887233 | 144 | 52 |
| 1153 | 288 | 16 |
| 193 | 96 | 88 |

The u phases are interpreted modulo ord_q(4). On the final coordinate n=32+36w, the last four rows cover w odd, w=2 modulo four, and w=0,4 modulo eight. The old-P hole predicate has exponent period 210. Consequently a complete common covering-predicate period is

\[
L=\operatorname{lcm}(210,4,12,18,9,72,144,288,96)=10080.
\]

The calculator executed every n from 1 through 10,080. The uncovered counts after adding zero through eight of the displayed supplementary rows were

\[
(1728,864,312,208,104,52,26,13,0).
\]

These are counts along this specified route. The full residue-value period across all 45 observed primes is 60,480, calculated from their exact orders; this new native run executed the complete covering period of 10,080.

## 3. Actual execution counts and retained evidence

The 43 fixed R3 channels are augmented by 1153 and 193. At every state the native quotient/remainder routine reads all 45 prime coordinates and retains their cofactors. A native joint mixed-radix readout is recomposed to the original integer at every step. All 43 fixed coordinates are compared directly with the separately advanced scalar trajectory of A3.

| Operation | Actual count |
|---|---:|
| Native one-step BRC updates | 10,080 |
| Native composed two-step evaluations | 5,040 |
| Individual prime cofactor/remainder readouts | 453,600 |
| Joint 45-radix readouts | 10,080 |
| Native joint recompositions | 10,080 |
| Fixed 43-coordinate comparisons | 433,440 |

Every actual zero hit is a proper prime divisor. All eight supplementary primes and all twenty old primes have retained private witnesses. The supplementary private exponents, in displayed dictionary order, are 6,12,152,20,140,392,32,1040. Each witness contains its full integer and prime cofactor in hexadecimal.

The final complete integer has 11,047 bits. Its full value, all 45 final prime cofactors and residues, the joint cofactor and digits, and the fixed-root reference state are saved in `native_minimum_certificate.json`. Digests of the full execution streams supplement these explicit values.

The run verifies the explicit cover and lossless native readouts. Exact delta_P=8 uses the seven-cover obstruction, and global root minimality uses the separate complete classification and exhaustive smaller-root exclusion. For this compact root tau(a^2)<=28; private witnesses alone are not a proof of unrestricted total-cost equality.

## 4. Reproduction

Run `python verify_native_minimum.py --source-dir /path/to/pinned_source`, where that directory contains the frozen `enterprise_math` package. In an unpacked reproduction bundle, `--source-dir src` selects the included modules. The script uses only the standard library and those four frozen scientific modules.
