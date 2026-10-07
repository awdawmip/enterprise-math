# CM(-24) UR: finite proof-translation checker

This is a new finite falsification check of the **import and translation interfaces** for first-digit unit reciprocity. It is not an all-prime proof, an independent Driver review, or a repetition of the predecessor's 77-prime experiment. It does not test or claim LIFT, the second p-adic digit, or a mod-p^3 supercongruence.

## Reproduce

Use Python 3.10+ and its standard library, from this directory:

```sh
python -I check_cm24_translation.py --output RUN.json
```

The publication bundle is flat and portable: seven unmodified original source files sit beside the checker. A private Python namespace created in memory allows their original relative imports without importing the entire repository initializer or modifying any source bytes. `REUSED_SOURCE_MANIFEST.json` lists original paths, flat bundle names, source commit, SHA-256, and Git blob hashes. The checker validates all seven original files before importing them. No network, nonstandard dependency, package installation, or repository checkout is required.

Actual runs on 2026-10-07 UTC succeeded under ordinary Python and isolated `python -I`. After flat packaging, a copied bundle in a separate temporary directory also passed under isolated Python. Their eight scientific records and exact trace hashes match. Repeated execution verifies packaging reproducibility, not additional prime coverage. Runtime differences are not scientific output. Neither predecessor `main()` was called.

## Declared finite population

The fixed primes are `13,19,37,43,61,67,109,139`: four in each target residue class `13,19 mod 24`. They are a small discrimination set, not a completeness horizon. Each case retains exact rational arrays with branch labels `(p,k)`, `0<=k<p`. The product carrier retains ordered `(p,i,j)` labels before the coefficient observer `n=i+j`.

The inherited series is

`B_k=(1/6)_k(1/3)_k/((k!)^2 2^k)`, `g=sum B_k`, and `h=sum(12k+1)B_k`.

The imported theorem uses

`A_k=(1/2)_k(1/3)_k(2/3)_k/((k!)^3 2^k)` and `W=sum(6k+1)A_k`.

The checker uses the original parent's `direct_Bs`, `frac_mod`, and `primes_below`, and the original differentiated-Legendre checker's `q_value_and_derivative`. The new A-coefficient recurrence directly instantiates the imported parameters `d=3`, `a=6`, and `lambda=1/2`; the coefficient `A_1=1/18` is checked explicitly.

## What is tested

For each fixed prime:

1. Exact parameter displacements `1/6=-m+p/6`, `1/3=-2m+p/3`, and the two relevant quadratic-character signs.
2. Every low coefficient of the finite Clausen convolution, over exact rationals.
3. The exact weighted identity `g*h=W+tail`, including the derivative-weight conversion `12` to `6` by ordered-pair symmetry.
4. Every ordered high-degree pair's valuation is at least two, plus exact modular verification that its accumulated tail vanishes modulo `p^2`.
5. The finite imported-theorem instance `W=p mod p^2`, and its translation to `g*h=p mod p^2`.
6. The frozen CM0/SIMPLE interface and `h=-6 Q'_m(1/2) mod p`.
7. Reduction of `g` modulo `p^2` before dividing by `p`, equality with the exact rational `g/p mod p`, and the resulting UR product.
8. Actual existing BRC CWM positive-family aggregation of g and h, followed by serial composition giving `p^2` labeled positive product branches and total `g*h`.

The exact trace contains all B and A fractions, valuation vectors, g, h, W, and tail. Its explicit ordered-pair domain and weight rule reconstruct the complete product carrier from the retained arrays. This is a factorized lossless record of the finite arithmetic carrier; it does not identify arbitrary historical paths or erase signed derivative information. Signed derivative and modular-unit readouts remain separate from positive CWM.

`EXACT_TRACE.json.gz` uses gzip `mtime=0`. The checker records compressed and uncompressed SHA-256 hashes. The trace need not be uploaded: it is exactly regenerated from the fixed input list and these published source files. Local compressed and base64 copies are retained.

## Fault discrimination

Each prime detects five deliberately wrong translations, for 40 detected nonzero defects total:

- use weight `12k+1` on the imported 3F2;
- use weight `6k+1` on the inherited 2F1 factor h;
- use the ordinary sign instead of the supersingular sign;
- reverse the sign of the Q derivative factor;
- reduce g modulo p before dividing by p.

## Limits and method reuse

The elliptic model's CM identification, good reduction, and all-prime applicability of the cited theorem remain obligations of the accompanying mathematical proof. Numeric quadratic characters at eight primes do not prove those obligations. A passing finite congruence is not a proof of UR.

`REUSE_EXECUTED` applies to the named frozen script and BRC functions actually called. The small scalar `rational_valuation(value,p)` helper is a task-local observer; it is not a new general-purpose tool or family. The existing rational-holonomy tool factors all numerator/denominator primes and cannot retain the signed modular unit, so its full factorization interface is unnecessary here. The scalar valuation test preserves the exact rational carrier and does not replace it with a valuation-only state.

Authorship: generated within root researcher EM-DIRECT-49ADE6's authorized CM24 run, with inherited context. `NOT_INDEPENDENT / NONBLIND_DISCLOSED`. No remote upload, task claim, Result freeze, Driver acceptance, or Foundation change is performed by this checker.
