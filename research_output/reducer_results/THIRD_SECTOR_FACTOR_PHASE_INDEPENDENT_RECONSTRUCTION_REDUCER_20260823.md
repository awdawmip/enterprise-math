# Reducer Result — Third-Sector Factor Phase Independent Reconstruction

Status: `FROZEN_REDUCER_RESULT`

Task-ID: `RS-THIRD-SECTOR-FACTOR-PHASE-INDEPENDENT-RECONSTRUCTION`

Researcher-ID: `EM-TSFPR-D14474`

## Terminal result

`FULL_BIDIRECTIONAL_BRIDGE_INDEPENDENTLY_RECONSTRUCTED`

No retained formula has a finite counterexample in the declared checks. The infinite claims are retained because of the Gaussian-factorization proofs in the full report, not because the mismatch lists are empty.

## Minimal normal form

For admissible

`n=h^2 2^epsilon C`,

where `epsilon in {0,1}` and `C` contains exactly the `1 mod 4` prime powers:

1. parameter space: `Div(C)`;
2. only quotient: `d~C/d` after unit quotient;
3. forward representative:
   `Z_d=h(1+i)^epsilon product pi_p^{v_p(d)} conjugate(pi_p)^{e_p-v_p(d)}`;
4. normalized cell: `sort_desc(|Re Z_d|,|Im Z_d|)`;
5. count: `(tau(C)+1_{C square})/2`;
6. common scale: `h gcd(d,C/d)`;
7. generator: recurse through divisor exponents, retain `d<=C/d`;
8. primitive reverse normalization: `t=gcd(n,2)`, `m=n/t`;
9. reverse factors:
   `A=gcd(m,|ac+bd|/t)=gcd(m,|ad-bc|/t)` and
   `B=gcd(m,|ac-bd|/t)=gcd(m,|ad+bc|/t)`.

For distinct primitive quotient cells, `AB=m`, `gcd(A,B)=1`, and `A,B>1`.

## Reduction decisions

### Full `M(n)` -> split-core `M(C)`

The full divisor fiber of `n` overcounts shape choices because powers of `2` and even inert-prime powers contribute forced scale/axis-diagonal parity, not independent Gaussian split choices. The exact factor phase is the divisor fiber of `C`, with the removed information retained in `h` and `epsilon`.

### Four apparent spatial quotients -> one residual involution

After quotienting by units, swap and every global reflection are conjugation up to a unit. They all induce the single simultaneous complement action `d->C/d`. No primewise partial reflection is quotiented.

### Representation enumeration -> divisor recursion

The generator needs no scan over `(a,b)`. It enumerates exponent choices in `Div(C)`, constructs Gaussian products, and selects one complement representative. Direct enumeration exists only in the independent comparison module.

### Reverse factorization -> four gcd observables

The reverse algorithm has no integer-factorization call. Two primitive orientations divide the complete split prime-power support into equal-orientation and opposite-orientation blocks. The real and imaginary coordinates of `z conjugate(w)` expose one block, and those of `z w` expose the other.

## Smallest exact controls and failures

| Claim attacked | Smallest retained control | Exact outcome |
|---|---:|---|
| admit odd inert exponent | `n=3` | flawed generator emits `(1,0)` of norm `1`; direct set is empty |
| omit reverse `2`-adic normalization | `n=130` | cells `(9,7),(11,3)`; correct core `65` gives `{5,13}`, flawed rule gives `{10,26}` against `130` |
| treat swap as a distinct primitive state | `n=65` | `(8,1)` and ordered swap `(1,8)` yield only trivial `{1,65}` |
| apply primitive theorem to unequal scales | `n=25` | `(5,0)` and `(4,3)` make all raw gcds `5`; recovered factors are not coprime |
| apply primitive theorem before removing equal scale | `n=260` | `(16,2),(14,8)` give contaminated `{20,52}`; dividing scale `2` first recovers `{5,13}` at norm `65` |

No valid distinct primitive pair violated the retained reverse rule.

## Frozen executable result

- forward range: `0..4096`;
- direct/factor normalized hash:
  `2f918b91795a79dd7b4d3fa3951e262917a36bf5cef3c63920c27f33ec4d42f1`;
- forward/count/scale/injectivity/fixed-point mismatch counts: all `0`;
- reverse range: `1..20000`;
- primitive pairs checked: `2028`;
- reverse-result hash:
  `4d96fe911d42dd87fecaab057d1e1ab09dba64617a98578c59b05ef3abf44306`;
- reverse failure count: `0`;
- both required negative controls discriminated the flawed variants.

## Development normalization incident

The first run had `391` tuple-order mismatches: direct results were increasing in `b`, while factor results were lexicographically ordered. Counts, scales, injectivity, and fixed-point tests were already clean. Each module was changed to freeze its own lexicographic normalization before comparison; the retained run has identical set hashes. This was an output-normalization defect, not a mathematical counterexample.

## Kill-condition disposition

- forward noninjectivity: not found; excluded in general by Gaussian valuations;
- forward nonsurjectivity: not found; excluded in general by Gaussian UFD;
- reverse failure on a valid primitive pair: not found; excluded in general by the equal/opposite orientation partition proof;
- naive or out-of-scope variants: killed by the exact controls above.

The reducer therefore closes the precise normalized theorem and rejects every broader unnormalized reading.
