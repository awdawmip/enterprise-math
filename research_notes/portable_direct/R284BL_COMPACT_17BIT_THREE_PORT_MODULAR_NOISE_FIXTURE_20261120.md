# R284BL-FX1 — 17-bit modular star-Port scalar with certified ±3 noise correction (3×3 binary case)

Date: 2026-11-20 (Asia/Shanghai). Mode: independent portable TASK_RESEARCH, same declared auxiliary star-Port observer as R284BJ/R284BK. Mathematical status: EXACT_FINITE_CERTIFICATE_PASSED / NOT_REVIEWED. This file does not assert a live formal CLAIM or Result.

## Frozen lineage and exact statement

Scientific source: R284BJ proof pinned at `ba9ac42ee03c61e34a057ede0d57561d0c418f6b:research_notes/portable_direct/R284BJ_FINITE_FIELD_INFORMATION_OPTIMAL_PORT_SCALAR_20261120.md`, with its declared n=3,H=2,δ=3 fixture p=13,604,881. P000 and native X6/BRC assertions are unchanged; this is an auxiliary finite arithmetic observer.

**Distinct subseries ID R284BL-FX1 (separate from the existing R284BL extension-field Las Vegas theorem).** The latter changes read count/alphabet; this certificate improves the fixed three-dimensional one-base-field-symbol example.

**Finite certified result.** For every C in `{1,2}^{3×3}`, take the field F_100003 and fixed controls

    (d0,d1,d2,z1,z2)=(25614,64524,70267,34320,67846).

Define `P_C = det(diag(d0,d1,d2)-C-z1 E_01-z2 E_02) (mod 100003)`. The 512 residues are pairwise distinct and their **minimum circular gap is exactly 8**, attained by the centers 19023 and 19031.

Therefore, for every C and every adversarial integer e with |e|≤3, one observed residue `r=P_C+e (mod 100003)` uniquely determines C by cyclic nearest-center decoding. The same fixed setting tolerates adversarial real circular noise |e|<4 (closed arcs of radius ρ<4 are disjoint). This is a fixed-size constructive certificate, not a uniform asymptotic polynomial-time decoding theorem.

## Proof and verification method

1. Enumerate the 512 matrices lexicographically by their nine entries (each 1 or 2). For every matrix form the above 3×3 matrix and evaluate its determinant by the explicit six-term Leibniz formula over integers, then reduce mod 100003. Independently compare to a standard 3×3 determinant expansion on every input.
2. Trial-division primality check verifies 100003 is prime. The sorted 512 residues are stored in the JSON companion. The full deterministic calculation verifies there are 512 distinct residues and the minimum of all 512 adjacent cyclic gaps (including the wraparound gap) equals 8. The `sorted_residue_csv_sha256` commitment identifies the exact sorted list.
3. For all 512 centers and all seven integer errors in {-3,...,3}, the checker matches the observed residue to exactly the originating center. Total 3,584 noisy observations. Abstractly, the gap > 2δ establishes all integer-error cases once injectivity and gaps are certified.

These steps form an exhaustive finite computer-assisted proof. The companion standard-library checker is the executable specification, and the JSON carries both candidate-order and sorted 512-residue lists for independent cross-checks. The randomized search used to discover the tuple is not needed for verification; a fixed tuple and exhaustive verification suffice.

## Resource comparison and boundaries

| Quantity | This exact fixture | Earlier R284BJ example |
|---|---:|---:|
| Prime modulus | 100,003 | 13,604,881 |
| Transmitted symbol bits | 17 | 24 |
| Candidate matrices | 512 | 512 |
| Guaranteed integer error magnitude | 3 | 3 |
| Minimum cyclic spacing | 8 | 10 |

Information-theoretic packing gives `p ≥ 512(2·3+1)=3584` for this model. The present 100003 modulus is about 27.9 times that bound and about 136 times smaller than the previous example prime. The discovery search is **not** a proof of minimality, nor is the fixed fixture an asymptotic improvement of BJ1. Each control is a field element and thus a 17-bit value; the native modulo source-side instrument and candidate-table cost remain separate resources.

## Reproduction and remaining question

Run Python 3 `R284BL_compact_modular_port_checker.py` without dependencies. It exhaustively verifies every matrix, a second determinant expansion, every integer error case, and outputs full sorted/candidate-order residues. Compare its output to `R284BL_compact_modular_port_verification.json`.

Next: exact search/symmetry reduction for smaller primes (ideally closer to the 3,584 packing bound), derive a structure-backed family for general n,H with reduced leading communication exponent, and cost native modular determinants and candidate decoding independently. Author-side computational certificate only; independent mathematical review pending.