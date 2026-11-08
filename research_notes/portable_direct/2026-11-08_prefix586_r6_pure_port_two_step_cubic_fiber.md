# PREFIX-586-R6 — Native two-step pure-port fiber contrast in cubic BRC coupling

Date: 2026-11-08 Asia/Shanghai.
Status: EXACT_FINITE_EXHAUSTIVE_AUTHOR_PROOF / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Native formal Owner/Researcher session: unconfirmed (backend database unavailable).

## Question and inherited interfaces

PREFIX-582-R6 proved, under the UNIFORM random initial port law on all 96 native four-STAR X6-BRC ports and six equiprobable actions at every depth,
`cum(Y_n,P_i(n),P_j(n))=q_n M_ij`
where
```
P_0=R_1+R_2, P_1=R_3+R_4, P_2=R_5+R_6,
Y_n=K_n-(5R_1-R_2+5R_3-R_4-4R_5-4R_6)/192,
M=[[0,1,-1],[1,-1,0],[-1,0,1]].
```
At n=2 the uniform-law matrix is `-M/864`. Does this one-scalar form survive when the initial port is deterministic rather than uniform? Retain native action labels and port identities to test this (no premature observer collapse).

## Theorem — every pure port produces a DIFFERENT rank-one two-step form

For each of the **96 deterministic initial native ports**, let `C_i^(2)` denote the 3x3 matrix of cubic cumulants `cum(Y_2,P_a(2),P_b(2))` under the 36 equiprobable ordered native length-two action paths.

1. On the six first actions out of each initial port the pair-mass vector is deterministic (a fixed unit vector).
2. On the second step there are exactly TWO supported pair-mass unit vectors, call them u_i,v_i.
3. For each port i, the exact matrix is
```
C_i^(2) = gamma_i (u_i-v_i)(u_i-v_i)^T,
gamma_i = cum(Y_2, X_i, X_i),
X_i = 1{second step pair mass equals u_i}.
```
All 96 values gamma_i are NONZERO; hence every local C_i^(2) has rank exactly 1. There are exactly **15 distinct** numerical matrices across the 96 pure start ports.
4. Since M has zero diagonal and rank 2, NO C_i^(2) is proportional to M. Thus the uniform-start single-scalar full-length theorem has a sharp initial-law boundary already at depth two.

The first two facts and the nonzero exhaustive classification are verified by the exact published native edge function `PREFIX565_positive_marginal_certificate.edge` applied to all 96 x 6 x 6 = 3456 native labeled ordered paths. The rank-one factorization in (3) is an algebraic theorem: the first-step pair mass is constant; the second-step pair mass equals v_i+X_i(u_i-v_i); mixed cumulants of order >=2 vanish when an argument is constant and are multilinear. Since all exact gamma_i are nonzero and the differences u_i-v_i are nonzero, rank=1. Therefore (4) follows from the explicit shape of M.

## Independent hand-checkable port-0 counterexample

Take original initial port `0`, zero root, and six equiprobable actions twice. The 36 length-two native paths aggregate into exactly two atoms, in the integer H=192Y_2 and *second-step* pair readout:

| second-step pair | H | number of paths |
|---|---:|---:|
| P_2 | -1 | 24 |
| P_1 | -4 | 12 |

The first-step pair is always P_0, so `P(2)=e_0+e_2+X(e_1-e_2)`, with `P(X=1)=1/3`. Also `Y_2=-1/192-X/64`. Using the exact Bernoulli third cumulant `cum_3(X)=p(1-p)(1-2p)=2/27`,
```
gamma_0 = cum(Y_2,X,X) = -1/64 * 2/27 = -1/864,
C_0^(2) = (-1/864) * [[0,0,0],[0,1,-1],[0,-1,1]].
```
The uniform-initial matrix is `-M/864`; for example its (0,1) entry is -1/864, whereas the port-0 (0,1) entry is 0. The difference is an exact falsifying witness for extending the uniform-start theorem to arbitrary start laws.

## What the native observer retains

At depth one, every deterministic start port has a fixed pair P, so its local cubic pair matrix is zero; yet averaging over the 96 starting ports produces the nonzero uniform-start first-depth matrix `M/576` (PREFIX-581-R6). At depth two every pure-start matrix is rank one, whereas the uniform-start matrix has rank two. Since third cumulants of mixtures contain cross-fiber mean/covariance terms, averaging cumulant matrices is not the same as taking the cumulant after mixing. This gives a concrete native BRC provenance-loss witness: the starting-port fiber matters to the cubic observable.

## Exact reproducibility and next unit

The standalone standard-library checker `PREFIX586_R6_pure_port_two_step_certificate.py` imports the SOURCE native frozen edge implementation (same science pin), enumerates all 3456 native ordered two-step paths, evaluates exact Fraction cumulants for 96 pure starts, verifies pair supports, nonzero rank-one factors, failure of proportionality, exact port-0 atom counts, and 15 distinct exact matrices. Local execution: `ALL_CHECKS_PASS`; output file `PREFIX586_R6_PURE_PORT_RESULTS.json`. This is a complete proof for the stated finite domain, not a finite-depth extrapolation.

Next discriminating task: derive the 15 local shapes from a small native port automorphism/branch classification, then compare for other eight frozen roots. For arbitrary initial-port mixtures, seek a closed observer retaining the initial-fiber mean and covariance cross terms. No native formal CLAIM/Result/Review or Working Truth promotion is asserted.
