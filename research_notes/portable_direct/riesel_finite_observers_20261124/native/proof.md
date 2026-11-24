# Native BRC execution of the complete-six root and crossing R2 covers

Status: actual author native execution in the existing Researcher `EM-DIRECT-970E1C`, Activity `RA-D2EC212845B63844081F9A14`. This is shared-context implementation verification, not an independent project Review, formal mathematical acceptance, or Foundation promotion.

## 1. Exact native source and state

The calculation imports the four frozen native modules at commit
`b1efc6c805661ed7b476e6e730107da6043176ee`. Before importing, it verifies their Git blobs against the previously published base certificate, whose blob is `c1909a5e2e209b0f6bd5f613d0f758dde45caee9`:

| Module | Verified Git blob |
|---|---|
| `brc_transport.py` | `be1debe367263931bd5e93fd750be3ed54624fe1` |
| `brc_histogram.py` | `9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1` |
| `brc_rational_holonomy.py` | `2591640fe348da9cd7f293a957bea9ae92c82943` |
| `brc_weighted_recurrent.py` | `4e6b3132580e3cd70a20a0d8bd4d28792b961afb` |

The state is the established typed integer register

\[
x_n=F_n(a)=a^2 2^n-1.
\]

`EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])` constructs the positive singleton BRC update. Its entries are checked exactly, including weight one and multiplicity one. Native composition `step.then(step)` gives the affine effect \(x\mapsto4x+3\). Every executed one-step update and every executed two-step update retains the singleton positive weight and agrees with the exact integer formula.

The fixed X6 anchor is unchanged. The exponent is an arithmetic update index, and prime readouts are observations of the register, not extra axes or BRC branches. The full integer and its joint cofactor relations remain available.

## 2. Three actual roots

The first root is the previously computed 76-digit root, whose minimum scope is enlarged by the companion [complete-six theorem](../six/proof.md):

\[
a_6=1597463687996365290740241630260436015028835427889255944107518938773290244463.
\]

The second is the compact R2 binary-completion root from the [observer note](../observer/proof.md):

\[
a_{7,B}=142182133093029631521252488222753720130073171510309885943518183289197140261893115365205303.
\]

The third root supports both the binary and modulo-five routes in the [R2 sharp-budget analysis](../six/r2_proof.md):

\[
a_{7,\times}=5638859082119336258239285976823481197493104557616679794390344515886945665210917791971325889059624133.
\]

The old dictionary P, the base root and the established old-hole predicate are reused from their pinned prior scientific sources. All three roots have the fixed R1 residue

\[
a\equiv12926327728523\pmod{80754838636615},
\]

as well as the same old root congruence. The latter two roots additionally have

\[
a\equiv602924359709868072943\pmod{1354510679787418425415},
\qquad
(a\bmod433,a\bmod38737)=(0,38733).
\]

These conditions are checked before execution. Direct root-difference divisibility verifies equality in all 29 R1 coordinates and in all 31 R2 coordinates, respectively.

The first root and its six phase rows are unchanged from the ninth-continuation certificate at commit `b1de1acbdc97b5e51d486127abd1fadd24babd99`. Its inclusion in this new execution supplies the common-trajectory comparison with the two new roots; it is not a new minimum search or a new calculation of the eight CRT progression starts.

## 3. Full coverage periods and the crossing routes

Each row below gives the number of old holes left after each successive selected prime, starting with budget zero. All counts come from actual native integer states and native quotient/remainder readouts.

| Root and route | Ordered supplementary primes | Observed exponent period | Uncovered counts |
|---|---|---:|---|
| \(a_6\) | 5, 13, 19, 73, 433, 38737 | 2520 | 432, 216, 78, 52, 26, 13, 0 |
| \(a_{7,B}\), binary | 5, 13, 19, 73, 38737, 577, 487824887233 | 5040 | 864, 432, 156, 104, 52, 26, 13, 0 |
| \(a_{7,\times}\), modulo five | 5, 13, 19, 73, 181, 631, 23311 | 5040 | 864, 432, 156, 104, 52, 32, 12, 0 |
| \(a_{7,\times}\), binary | 5, 13, 19, 73, 38737, 577, 487824887233 | 5040 | 864, 432, 156, 104, 52, 26, 13, 0 |

At the same ordinary root \(a_{7,\times}\), the binary route leaves 26 holes after five primes, compared with 32 for the modulo-five route; after six primes the ordering reverses, leaving 13 versus 12. Both routes reach zero after seven primes. The analytic claim that these are the relevant sharp optima, and that every sharp six-prime dictionary must omit 38737, belongs to the companion all-prime proof. The native example exercises the resulting crossing without replacing that proof.

The old-hole predicate has the previously proved period 210 in n. For every selected prime, the calculator checks its exact base-2 order and the equivalence

\[
q\mid F_n(a)
\iff n\equiv2c_q\pmod{\operatorname{ord}_q(2)}.
\]

The least common multiple with 210 is 2520 for the first route, 5040 for the binary routes, and 1260 for the modulo-five route. Thus the last route is counted over four complete coverage periods in the common comparison interval. These facts, together with the zero terminal count, give full positive-index coverage for the displayed dictionaries. The residue values themselves need not have these smaller predicate periods.

Every observed zero has \(1<q<F_n(a)\), and the first term already exceeds every observed prime, so the assigned divisors remain proper. Each route also has a private old-hole index for every selected prime, recorded in the certificate. Such privacy proves irredundancy of that dictionary; it does not by itself prove the global total minimum. Exact supplementary costs use the companion lower bounds, and the compact roots here have the total-cost upper bounds 26 or 27 without a new equality claim.

## 4. Actual execution counts

The run completed successfully with:

| Operation or equality | Count |
|---|---:|
| Native one-step BRC updates | 12,600 |
| Native composed two-step evaluations | 6,300 |
| Total native effect evaluations | 18,900 |
| Native quotient/remainder readouts | 425,880 |
| Readouts equal to the exact closed formula | 425,880 |
| Equalities to the old P-coordinate formula | 252,000 |
| Equalities to the additional fixed-fiber formulas | 133,560 |
| Direct 29-coordinate comparisons with \(a_6\) | 146,160 |
| Direct 31-coordinate comparisons between the two R2 roots | 156,240 |

The 29-coordinate comparisons use indices 1 through 2520 for each new root against \(a_6\). The 31-coordinate comparisons use indices 1 through 5040 between the two R2 roots. These are counts of actually performed comparisons, not claims that a finite check alone proves all future equality.

The universal equality follows algebraically from the root congruence: if \(a\equiv a'\pmod N\), then

\[
a^2 2^n-1\equiv(a')^2 2^n-1\pmod N
\qquad(n\ge0).
\]

The root-congruence checks and this identity therefore bridge the finite execution to complete future residue-value agreement. Each final native integer is retained in the certificate by its bit length and SHA256 of its minimal unsigned big-endian encoding.

## 5. Reproduction and scope

Run from this directory, retaining the prior repository paths:

```sh
python verify_native.py --source-dir /path/to/pinned_source
```

The source directory must contain `enterprise_math/` with the four pinned modules. When run in the retained repository or scratch layout, the script also accepts the matching `src/` or `vendor_src/` automatically. The only retained external local data are the published base certificate and old-hole certificate; root values and new phase rows are explicit in the script.

`native_certificate.json` records the successful result, individual roots, all route rows, private witnesses, observed periods, source identities and operation counts. The universal finite-observer cost theorem and exponential-order bounds are written proofs in the companion notes. This finite execution neither establishes those theorems by extrapolation nor asserts a root of infinite covering cost.
