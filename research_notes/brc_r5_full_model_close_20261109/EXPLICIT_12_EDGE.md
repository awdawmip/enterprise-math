# R5 — Exact explicit 12-edge Blackwell matrix for a nonzero-residual source

2026-11-09 Asia/Shanghai. This is a **finite exact construction** in the frozen seven-node P/Q-BRC terminal-observer model. It complements the all-real existential triangular theorem in RESEARCH.md.

Choose
\[
(t,p,q,\theta,\kappa)=(1/10,3/4,1/4,1,0).
\]
The lawful FULL_HIST source is
\[
x=(1,1/10,1,27/800,1/100,27/400,1/100),
\]
with strictly nonzero seedless-defect
\[
9bz-4a(v-z)=9/100.
\]
The constructive interpolation in VERIFY_PGEQ.py produces the lawful seedless target
\[
y=(4673/6400,1311/6400,4673/6400,38759/512000,
47301/256000,103999/512000,1311/64000).
\]
Both \(T_P\) and \(T_Q\) are exactly equal between \(x,y\).

For \(r=(1/10,1/2,3/4,1,5/4,3/2,19/10)\), the following **12 nonzero entries** of a \(7\times7\) matrix \(E\), with target LR row \(i\) and source LR column \(j\), constitute a fully exact martingale Blackwell certificate (all omitted entries are zero):

| i | j | \(E_{ij}\) |
|---:|---:|---:|
|0|0|16109/720000|
|0|1|9/2080|
|0|2|273874223/2995200000|
|2|1|9/1300|
|2|2|21277/83200|
|3|2|2442943/38400000|
|3|3|98191/360000|
|3|5|9/100|
|5|2|1/256|
|6|2|8134171/230400000|
|6|5|9/80|
|6|6|29609/720000|

All entries are nonnegative, the smallest positive entry is \(1/256\). With \(M_i\) the frozen mass map, the verifier checks exactly:
\[
\sum_j E_{ij}=M_i(y),\quad
\sum_i E_{ij}=M_j(x),\quad
\sum_i r_iE_{ij}=r_jM_j(x)
\]
for **all seven rows and columns**, plus seedless constraint, physical capacities and two time equalities.

**Discovery vs verification:** scipy HiGHS floating LP suggested an edge support; a rational linear solve reconstructed the displayed exact coefficients. The published VERIFY_EXPLICIT_MATRIX.py uses only the standard library and the sibling VERIFY_PGEQ.py, validates exact Fraction arithmetic and is independent of LP/SymPy at reproduction time.

Executed in the local sandbox (exit code zero):
~~~text
PASS_R5_EXACT_12_EDGE_BLACKWELL_CERTIFICATE
SOURCE_RESIDUAL_9_OVER_100_TARGET_RESIDUAL_ZERO
MARTINGALE_ROW_COLUMN_AND_WEIGHTED_COLUMN_IDENTITIES_PASS
STOP_TIMES_AND_SEEDLESS_PHYSICAL_BOUNDARIES_PASS
~~~

**Next:** generalize the sparse-support selection to a certified rational martingale coupling algorithm for arbitrary lawful inputs. Analyze bit cost and worst-case sparsity, rather than extrapolating algorithmic complexity from this single explicit example. Separate author-side checking from independent project mathematical acceptance.
