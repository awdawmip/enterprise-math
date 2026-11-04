# D25: four exact signed shell certificates and an explicit half-truncation falsifier

2026-11-05. TASK_RESEARCH author-side, UNREVIEWED / NOT_ADMITTED. Immutable research input c47e13e4aba0e006366f989d6334d443f6333ae3; task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. This is a direct finite arithmetic continuation of the all-prime signed shell theorem at research_notes/portable_direct/20261105_onhour_d25_weighted_shell_literature_reduction.md.

Define W_half and V_half using original 216 and 2304 coefficients and their (6k+1)/(8k+1) weights, k<= (p-1)/2. Let T_A be the explicit signed factorial upper-shell sum in the theorem. Exact integer modular recurrence calculation yields:

| p | p^3 | W_half mod p^3 | V_half mod p^3 | (W_half-V_half)/p^2 mod p | T_A mod p | sum of two signed digits |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 2197 | 520 | 13 | 3 | 10 | 13 |
| 19 | 6859 | 3629 | 19 | 10 | 9 | 19 |
| 139 | 2685619 | 2434585 | 139 | 126 | 13 | 139 |
| 373 | 51895117 | 14887176 | 373 | 107 | 266 | 373 |

All table entries are exact integer residues, not floating-point output; the lower difference numerator is exactly divisible by p^2 for each witness. Hence p^2*(lower signed digit + T_A) is divisible by p^3 in each row, while both source-labelled coordinates are nonzero. This produces four complete finite witnesses for W_p-V_p=0 mod p^3.

**Scoped falsifier:** At the smallest frozen target p=13, W_half-V_half=507=3*13^2 (mod 13^3), so the *uncorrected* claim W_half=V_half mod p^3 is false for the actual original coefficient families. The high shell supplies +10*13^2, exactly repairing the missing signed 13-adic digit. The same information loss occurs in the 19,139,373 rows.

The all-prime 2304 cancellation is an independent *published* Guo–Zudilin 2019 theorem consumed in the previous note; the equality W_p=V_p on all target primes is not promoted from four tests. A correct terminating proof should establish W_half=p-p^2*T_A (mod p^3) on p=13,19 mod24, not eliminate the 216 upper shell.

Original native p=373 H0/B0 divided-power [X]U mod139129, module rank, semilinear Frobenius and independent replication remain Issue #1559 NOT_EXECUTED. No Research CLAIM, Source checkpoint, Result or review admission is asserted by this author-side GitHub evidence.
