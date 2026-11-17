# R254A — Exact 21-rational-parameter characteristic scaling pilot

Scientific date: 2026-11-18. Status: EXACT_FINITE_FAMILY / NOT_REVIEWED.
Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.

For every one of the 21 rational parameter anchors s=j/1000 with j=390,...,410, construct all 63 exact block characteristic polynomials c_m(x)=x^d+sum_{r=1}^d c_{m,d-r}x^(d-r). Define

T_min(s)=product_p p^{max_{m,1<=r<=d_m} ceil(v_p(den(c_{m,d_m-r}))/r)}.

This is **the least integer T>0 for which every T^d c_m(y/T) is integral**: the displayed p-adic exponent constraints are simultaneously necessary and sufficient, coefficient by coefficient. This is a finite-family exact theorem; it does not require unproved spectral assumptions.

The independent standard-library Fraction script R254A_grid_scaling.py checked all 21 parameters, all 63 masks and 249 coefficient positions per parameter (5229 coefficient positions). All T_min values divide L(s), where L(s) is the least common multiple of all 49 transition-entry denominators of the seven-state matrix.

- T_min(s) bit length: 19 to 35.
- L(s) bit length: 30 to 55.
- At s=0.390, T_min=272068200 and L=30669704049600.
- At s=0.400, T_min=299160 and L=552847680.
- At s=0.410, T_min=266419800 and L=29048283633600.

Exact 21-point factor vectors and bit lengths are saved in R254A_21_grid_summary.json. The full executable generates R254A_21_grid_scaling.json with exact L, T, J, each prime factorization, and per-parameter checks. Local full generated JSON SHA-256: 832c0398e3941da09da61fbba90c61a235cf744eb7f3289dfd74af95d0df99a5.

Mathematical interpretation: a p-adically minimal characteristic scaling can reduce the exact-denominator growth of an individual fixed-parameter rational recurrence relative to entrywise matrix clearing. R254 proved an **additional sharp labelled-output denominator equality** at s=2/5. The present R254A certificate proves the minimal characteristic scaling for the stated 21 points, leaving the sharp common-output formula at other parameters open.

Current task boundaries: positive scalar observer; labelled 63 masks retained; no native signed BRC port claims, P000 updates, CLAIM, Result, or independent review.

Next: seek a parameterwise invariant of the prime factors of T_min(s), and develop modular witnesses for exact common reduced denominators beyond s=2/5. Account for input rational height in bit complexity.
