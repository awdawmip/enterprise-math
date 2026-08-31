# ADVERSARIAL_REVIEW

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`

## Verifier A — Complex Analysis

### Candidate B

Failure target: Lemma 10.

- `g` is declared entire.
- Its Taylor coefficient radius is therefore infinite.
- A nonzero fixed-base exponential asymptotic for those coefficients gives finite radius.
- Contradiction is independent of numerical zero data.

Verdict: **FAIL**.

### Candidate C

Failure target: Hadamard product for `xi(1/2+iz)`.

- functional equation gives evenness, not real zeros;
- off-line zeta zeros map to non-real zeros in the `z` coordinate;
- pairing the divisor as `±gamma_k` assumes RH.

Verdict: **FAIL / CIRCULARITY**.

## Verifier B — Infinite Operations

### Candidate A

- Hilbert–Schmidt convergence for `sigma>1/2`: reproduced.
- bounded perturbation cannot change leading eigenvalue growth: safe.
- zero diagonal does not by itself justify every notion of regularized trace neutrality; source appropriately labels the diagonal-trace statement formal.
- determinant identity is not generated automatically from trace neutrality.

Verdict: **DIRECT SPECTRAL ROUTE CLOSED; DETERMINANT BRIDGE OPEN**.

### Candidate B

Finite computational regions:
- finite `d,n,r` interval certificates remain finite facts;
- finite verification of `C_s` or `D_r(n)` cannot close `for all r,n`;
- an asymptotic ratio below a chosen `q<1` does not by itself prove a uniform geometric envelope for every unverified intermediate index.

Verdict: **NUMERIC_TO_EXACT_GAP** in addition to Lemma 10.

### Candidate C

Distributional or weak convergence of spectral measures does not automatically provide locally uniform convergence of a quotient of entire functions across moving zero sets. Any such upgrade needs uniform normal-family bounds plus divisor control that is not itself circular.

Verdict: **CONVERGENCE / DIVISOR CONTROL NOT CLOSED**.

## Verifier C — RH Circularity

Detected:

1. Candidate C real-zero Hadamard factorization = hidden RH.
2. Candidate B use of critical-line ordinates as the exhaustive reciprocal-pole spectrum is RH-level unless omitted complex poles are independently excluded.
3. Negative control bridge equation = tautology under the functional equation.

Not detected as circular:

- Candidate A's determinant identity **as a target**. It is a legitimate open theorem target; proving it independently would be substantive.

## Verifier D — Counterexample / Finite Stress

### Stress D1 — Lemma 10 coefficient inference

Take
\[
g(z)=(1-z/2)(1-z/3).
\]

Hadamard product is exact, but its Taylor coefficients terminate. They are not a nontrivial sum of the form
\(R_1 2^{-m}+R_2 3^{-m}\) for all large \(m\).

This separates:
- zero-product information,
from
- reciprocal-function residue expansions.

### Stress D2 — Candidate A finite matrices

For representative `sigma=1`, bounded coupling, diagonal `n^4-0.15n^2`,
the independently computed largest-eigenvalue ratios were:

| N | lambda_max / N^4 |
|---:|---:|
| 20 | 0.9996250000 |
| 40 | 0.9999062500 |
| 80 | 0.9999765625 |
| 120 | 0.9999895833 |

`EVIDENCE_ONLY`: this numerically illustrates, but does not prove, the already proved bounded-perturbation asymptotic.

### Stress D3 — target counting

Using the leading Riemann–von Mangoldt term in the squared spectral variable:

| Lambda | Lambda^(1/4) | RvM(sqrt Lambda) approx | ratio |
|---:|---:|---:|---:|
| 1e4 | 10 | 29.0 | 2.9 |
| 1e8 | 100 | 10,143 | 101 |
| 1e12 | 1,000 | 1,747,146 | 1,747 |
| 1e16 | 10,000 | 248,008,024 | 24,801 |

Again this is illustrative; the asymptotic exponents already decide the issue.

### Stress D4 — negative control

CIPHER's publicly failed bridge is classified as tautological by the same checker.

Verifier calibration: **PASS**.

## Hostile-verifier conclusion

No candidate passes all four verifier perspectives.

The strongest exact failure object in the full-claim-with-Claude-assistance route is:

`Gershon Lemma 10 — spectral-gap factorisation / Taylor-coefficient expansion`

with failure type:

`FALSE_LEMMA`.

An earlier dependency, Lemma 8, remains `UNPROVED_LEMMA`, but Lemma 10 is the first load-bearing node for which this rerun has a direct mathematical contradiction.
