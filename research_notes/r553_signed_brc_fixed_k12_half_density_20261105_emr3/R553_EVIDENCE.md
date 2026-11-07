# R553 verification evidence (2026-11-05, author-side)

Scientific source: frozen R462 `18783e01e3646c72b7aab3b16d3f565e83e6446f`. Target fixed `k=12` and `m≥0`.

Executed locally in Python 3 with SymPy, using the algorithms shipped in the accompanying scripts. The original exploratory `R553_VERIFY.py` generated candidate rational centers from SymPy `nroots` and checked every Rouché predicate with exact `Fraction` arithmetic; the published `R553_VERIFY.py` freezes those 23 rational centers so numerical root exploration is not needed for reproducing the proof checks.

```text
R553_RAW_COEFFICIENT_PASS identities=24 Catalan=208012 p2=17550 degree=23
R553_RATIONAL_ROUCHE_PASS roots=23 pairs=253 eps=1/10000 max_ratio_below=3/500
R553_RECURRENCE_PASS m=0..1024 plus_minus_zero_changes=(514,511,0,302)
R553_MOD_INTERPOLATION_PASS deg=506 time=0.12
R553_MOD_CYCLOTOMIC_PASS p=65537 deg_R=506 q_bound=512072 count=991 max_q=2310 time=21.74
R553_INDEPENDENT_BERKOWITZ_PASS m=1..16, raw polynomial convolution, recursive integer D; signs=[1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,1]
```

Scope: 24 exact raw coefficient equalities; 23 disjoint rational root circles and 253 strict pairwise separations; exact modular resultant interpolation of degree 529, exact division by (u-1)^23, 991 candidate q checks covering all q≤512072 with φ(q)≤506; two independent out-of-grid finite-field resultant values; 1025 exact rational recurrence terms; 16 independent exact raw Toeplitz determinants.

The asymptotic half-density theorem is a mathematical deduction from the exact root/phase certificate and Weyl equidistribution. The zero-finiteness corollary uses the classical Skolem–Mahler–Lech theorem for nondegenerate characteristic-zero linear recurrences. Neither a finite sample nor a GitHub commit alone constitutes independent mathematical admission.

Reproduce: `python R553_VERIFY.py`, `python R553_MODULAR.py`, `python R553_INDEPENDENT.py` from this one directory. Each script is executable separately; modular script imports the first as a local module. No credentials or external database required.

Native TASK CLAIM/Result and independent Driver review remain unconfirmed.
