# EC49FTR verification log (2026-11-19)

Command executed locally using the Python standard library:

```shell
python EC49FTR_MIXED_TP2_ATOM_VERIFY.py
```

Exit code: **0**. The program emitted the full JSON content of `EC49FTR_MIXED_TP2_ATOM_CERT.json`.

Exact checks: 99 rational interior m-samples checked against expanded closed forms for A(m), B(m), B(m)/A(m), its derivative and positivity. At each m, 4 exact TP2 cross determinants on a second later m-slice were strictly positive (396 checks). The code algebraically differentiated the rational atom ratio using rational polynomial operations; the quadratic discriminant is `-26785873329330290364`, strictly negative. Exact conditional CDF difference at p=23, q=93/4, threshold=719/960 equals `20716724056922624/76239764025565563>0`.

This is a finite reproducibility check complementing the analytic proof, not an exhaustive proof of a continuum or independent review. The inherited 228-observer native Bellman result was not recalculated. Scientific freeze `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` unchanged; new scientific argument is external price-prior postprocessing. Status: `AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED`.
