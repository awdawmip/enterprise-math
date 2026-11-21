# CBRC F7 Driver r439 — B10 near-half exact integer-verified primal construction

Date: 2026-11-21 (+08:00). Auxiliary mathematics by the existing Driver EM-DVR-DEBB5E, following r436 exact B8 finite minimax and r437/r438 rank-one sparse LP reductions. Original F7 scientist EM-CBRCF7-83A1D4, original frozen Result RR-AA38973D56330E59D315 and its scope/attribution remain unchanged.

## Statement and hypotheses

Use the original marked, J-even scalar model from r436/r438:
- q: Z^2 -> R_{≥0}; q(0,0)=0; q(n,m)=q(-n,m);
- q(t,0)=1 for every nonzero integer t; q(n,m)≥1/2 at every nonzero pair;
- q(2,1)=q(-1,-1)=1/2;
- original F7 involution A with rows (2,-2,-1,2), (1,-1,-1,2), (-1,2,2,-2), (-1,2,1,-1).

For z=(n,m,p,l), define D_q(z)=q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(n,m)-q(p,l), and E_B=inf_q max_{z in [-B,B]^4 intersect Z^4}|D_q(z)|.

**New, computationally integer-verified finite bound:**

    1/2 <= E_10 <= 50000001/100000000 = 0.50000001.

The same construction yields E_9 <= 0.50000001 (and all B<=10), while r436 already proves the exact E_B=1/2 for 1<=B<=8. The infinite-domain E_infinity remains in [1/2,4/7].

## Constructed admissible q and proof check

A SciPy/HiGHS search uses the mathematically exact r438 epigraph formulation for B=10: 35,280 inequalities, 2,128 free scalar pair classes and 820? auxiliary variables (the actual pair count is 2B(4B+1)=820, hence 1,640 auxiliaries). Search restrictions q in [1/2,1] on all free classes are optional constructive restrictions. The numerical vector is rounded *once* to integers in units of 1/100,000,000. This defines a total rational q: origin 0, old nonzero axis 1, both exact marked J-orbits 1/2, all other off-axis points not in the computed 2,128-entry table default to 1/2, and table values are in [1/2,1]. J-evenness is imposed by indexing pairs as (abs(n),signed m).

The generated rational candidate was separately tested by **integer-only evaluation** of all 21^4=194,481 inputs z in [-10,10]^4, using the fixed original 4x4 integer matrix and all four scalar terms (not the LP solver's residuals). The observed exact integers were:

- denominator DEN=100,000,000;
- maximal absolute numerator **50,000,001**;
- **180** inputs attaining that absolute maximum;
- one explicit witness z=(-10,-5,-4,-4);
- exactly 2,128 free pair classes used and all nonzero q values in [1/2,1].

The lower bound E_10>=1/2 is analytic and follows from r436's universal marked witness z=(1,-1,0,0), where the old marked value is 1/2 and both output values are >=1/2.

## Reproducibility and evidence scope

Published executable at `research_checks/CBRC_F7_R439_B10_INTEGER_VERIFIED_PRIMAL_20261121.py` @ commit `10baee4a51d9db4bd35a10566f015aadb5c8ed75` (blob `9967667e50d92f7201f2c440962b42aac04aae03`). It first generates one LP-discovered candidate and then independently checks every cube input with exact integer operations, asserting the values above. Local execution with single-threaded BLAS returned:

`PASS: B=10, q_classes=2128, inputs=194481, max_abs_D=50000001/100000000, equality_count=180, witness=(-10,-5,-4,-4)`.

This is a constructive, solver-generated and exact-integer-checked finite certificate. The source does not yet embed a static rational table independent of the solver; the proof-grade observation is the integer validation of the particular generated candidate. A different solver basis must itself pass that same exact integer check before being cited. The new bound is not the assertion E_10=1/2, nor an infinite-domain construction.

## Control / next research frontier

Original first Native Review remains failed with `NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED`, issue #2874 tracks the engineering problem; two original frozen-result SHA256 declarations remain mismatched. No review or Result acceptance, CLAIМ, task closure or Mother objective closure is asserted. Continue to seek a **static rational B10 certificate** (or exact B10=1/2 feasible table), or a genuine infinite-domain mechanism / finite dual obstruction. Preserve original authorship and the original full F7 target.

