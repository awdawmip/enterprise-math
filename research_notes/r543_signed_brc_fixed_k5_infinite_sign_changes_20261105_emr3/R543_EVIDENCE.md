# R543 exact evidence and status

Observation: 2026-11-05, Asia/Shanghai. Frozen scientific input R462 commit 18783e01e3646c72b7aab3b16d3f565e83e6446f. Author-side research, formal independent Driver admission pending.

Execute with Python 3 and SymPy: python R543_VERIFY.py && python R543_CROSSCHECK.py.

Exact script output from completed local execution:

~~~text
R543_EXACT_CERT_PASS
degree 9 disks 9 max_rouche_ratio 0.0055500
dominant_modulus_lower 1926336411/1000000 remainder_modulus_upper 1904177/1000
Ck 42 coefficients 1,-7007,23005125,-133928680600/3,53961853874500,-294568712804437500/7,21185555100608559375,-140256221267917777343750/21,1203398378478734529609375,-286809946870765062890234375/3
witness m42/43/44 + - +
signchanges to128 24
R543_INDEPENDENT_RAW_PASS H/B=10, raw matrices=9 (incl m43), negative43=True
~~~

The displayed Rouché ratio is a float for reporting only. All proof assertions employ arbitrary-precision rational/integer comparisons. Nine disjoint disks certify all simple roots; the top conjugate pair has modulus >1926, all other roots modulus <1905. Simple-root residues are nonzero and the main oscillatory term dominates asymptotically. Cesàro proof supplies an actual infinitely-often sign result independent of finite recurrence checks.

Distinct validation route: R543_CROSSCHECK.py directly extracts original signed H coefficients and uses SymPy Berkowitz on the nine raw Toeplitz matrices including 43×43. These are author-controlled implementations, not an independent Driver review. P000/ACTIVE worldview and frozen R462 were not modified.
