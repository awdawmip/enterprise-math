# R542 evidence | exact rational root disks and residues

Observed 2026-11-05 Asia/Shanghai. Frozen input R462 @ `18783e01e3646c72b7aab3b16d3f565e83e6446f`; R541 fixed-k generating-function frontier `75900e4750a4399df572b9e327ab168c03d4cf70`.

## Exact certificate

The executable `R542_VERIFY.py` tests its main mathematical obligations using Python `fractions.Fraction`, integer arithmetic, and `math.isqrt`: polynomial coefficients from ballot–Catalan H/B; d rational complex root disks; exact Rouche inequalities; pairwise separation; unique dominant real positive root; all non-dominant root modulus bounds; and strict positive residue domination.

The following abbreviated decimal displays are *only presentation of exact rational comparisons*, not inputs or floating-point justification. The complete exact comparisons are assertions in the code.

| k | degree | disk count | max Rouche left/right (presentation) | dominant A lower (presentation) | sum of other | separation |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | 5 | 5 | <0.00694 | >3.05252 | <2.19738 | alpha>237, others<144 |
| 4 | 7 | 7 | <0.00621 | >4.52792 | <3.68556 | alpha>755, others<600 |

Coarse rational bounds actually asserted by the script: `k=3: A0>305/100>220/100>sumother`, `k=4: A0>452/100>369/100>sumother`. The disk-by-disk inequalities assert `100*left<right` in exact rational arithmetic. All circular disks radius 1/10, with centers enumerated in R542_PROOF.zh-CN.md and source.

Local exact implementation output:
```
k=3 degree=5: 5/5 Rouche disks PASS; dominant lower 3.0525237807653816; total other upper 2.197370183649016; initial coefficients 0..1000 positive
k=4 degree=7: 7/7 Rouche disks PASS; dominant lower 4.527921963831225; total other upper 3.6855557175460625; initial coefficients 0..1000 positive
R542_EXACT_ROUCHE_RESIDUE_PASS
```

Independently checked original coefficient extraction `H` vs ballot formula for all t from 2 through r: k=3 six comparisons, k=4 eight; original signed Toeplitz matrices m=1..8: eight SymPy Berkowitz determinants per k. Output:
```
k 3 H/B 6 raw Bareiss/Berkowitz determinant 8 PASS
k 4 H/B 8 raw Bareiss/Berkowitz determinant 8 PASS
R542_INDEPENDENT_RAW_DET_PASS
```

The proof of positivity for **every** m≥0 is from the rational Rouche/residue certificate and a standard complex partial fraction identity. The 1000-order recurrence and 16 direct matrices are checks, not the quantified proof.

## Status and next

Author-checked exact proof. Independent Driver review / formal Result not registered by this document. BRC reuse=R462 signed H/B plus R540/R541. Next: fixed k=5 dominant complex pair and rigorous oscillation certificate; independently m=63 all-k parameter classification. Preserve original R462 pin and P000.
