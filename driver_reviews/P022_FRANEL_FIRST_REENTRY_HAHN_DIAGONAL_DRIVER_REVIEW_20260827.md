# Driver Review — P022 Franel First-Reentry Hahn-Diagonal Reduction

Status: `DRIVER_TERMINAL / ACCEPTED_EXACT_REDUCTION / ALL_PARAMETER_NONVANISHING_OPEN / RESULT_ONLY`

Date: `2026-08-27`

Driver-ID: `EM-DRIVER-01 / CONTROL_PLANE`

Task: `RS-P022-FRANEL-FIRST-REENTRY-KERNEL-NONVANISHING`

Publication: `TP2-18D80E295208AC91EB70`

Execution: `ER-2299B0A0C2E9CDA09AE3`

Result: `RR-EF198E9B037C152CD050`

Source evidence: Draft PR `#751`, frozen research head `6ba3e7de96a11026824a499b7242689a94ff3661`, return blob `06e4ede003aa697037f03b45c1a3252b75337ba1`.

## 1. Disposition

`DRIVER_DISPOSITION = ACCEPTED`.

`TASK_TERMINAL_BASIS = TASKBOOK_EXACT_REDUCTION_STOPPING_CLAUSE`.

`RESULT_CLASS = EXACT_HAHN_DIAGONAL_REDUCTION / RESULT_ONLY`.

`ALL_PARAMETER_NONVANISHING = NOT_PROVED`.

`ADMISSIBLE_ZERO_WITNESS = NOT_FOUND`.

`P022_Q_EQ_3R_MINUS_1_BOUNDARY = OPEN`.

`FOUNDATION_MUTATION = NONE`.

`WORKING_TRUTH_PROMOTION = NONE`.

`TOOLBOX_MUTATION = NONE`.

The result is accepted exactly at the strength it claims: the fixed first-reentry Franel residual has been reduced to one named moving-parameter Hahn-polynomial diagonal and reconnected to the Franel divisibility obstruction by a unit equivalence. This is terminal for this task because the taskbook explicitly permits stopping when the best exact route reaches a smaller established invariant whose required nonvanishing is independently open.

Acceptance does **not** mean that the all-parameter nonvanishing theorem has been proved, and it does **not** close the P022 `q=3r-1` arithmetic boundary.

## 2. Independent mathematical audit

Write

\[
n=3m,\qquad p=6n-1=18m-1.
\]

The submitted fixed kernel is

\[
R_m(p)=\sum_{j=0}^{n}
\frac{(-1/6)_j^3}{(1/2)_j(-1/2)_j\,j!}\pmod p.
\]

Because `6n = 1 (mod p)`, the parameters reduce termwise to

\[
{}_3F_2(-n,-n,-n;1-3n,-3n;1).
\]

In the standard Hahn normalization

\[
Q_k(x;\alpha,\beta,N)
={}_3F_2(-k,k+\alpha+\beta+1,-x;\alpha+1,-N;1),
\]

the substitution

\[
k=x=n,\qquad \alpha=-3n,\qquad \beta=n-1,\qquad N=3n
\]

gives exactly

\[
\mathcal H_n=Q_n(n;-3n,n-1,3n).
\]

Thus `R_m(p) = H_n (mod p)` is a direct parameter identity, not an empirical identification.

The terminating-series reversal was also checked independently:

\[
{}_3F_2(-n,2n,2n+1;1,1;1)
=
(-1)^n\frac{(2n)_n(2n+1)_n}{(n!)^2}\,\mathcal H_n.
\]

Every factor in the prefactor is below `p=6n-1`, so the prefactor is a `p`-unit. Together with the accepted parent Franel bridge this yields the exact equivalence

\[
p\mid F_{2n}
\iff
Q_n(n;-3n,n-1,3n)\equiv0\pmod p.
\]

For `n=3m`, this is exactly

\[
q\mid F_{6m}
\iff
Q_{3m}(3m;-9m,3m-1,9m)\equiv0\pmod q,
\qquad q=18m-1.
\]

The specialized Hahn difference equation is consistent with the standard second-order Hahn operator. With

\[
A(x)=(x-3n+1)(x-3n),\qquad C(x)=x(x-4n),
\]

the diagonal point satisfies

\[
2(2n-1)Q(n+1)+2Q(n)-3nQ(n-1)=0.
\]

The ordinary positive-weight Hahn orthogonality/zero-interlacing theorems do not supply the desired conclusion here: the specialization has `alpha=-N=-3n`, while `beta=n-1`, outside the standard positive-orthogonality parameter regime. No illicit zero-free inference from classical orthogonality is therefore accepted.

As supplemental Driver checking, the exact terminating reversal was independently replayed for small `n`, and the submitted finite regression was independently reproduced: among all prime boundaries `p=6n-1<50000`, the only unrestricted Hahn zeros are `(n,p)=(1,5)` and `(25,149)`; among the `90` admissible P022 twin-boundary cases there are no zeros. This remains finite regression only.

## 3. Scope and provenance boundary

The accepted authority is `RR-EF198E9B037C152CD050`, bound to `ER-2299B0A0C2E9CDA09AE3` and `TP2-18D80E295208AC91EB70`.

The research return disclosed that Draft PR `#741` was inspected only after the registered CLAIM and was not used to derive the Hahn identity or the Franel-to-Hahn unit equivalence. The present acceptance therefore treats the Hahn reduction as a disclosed nonblind result, not as an independent replication of the parallel conductor-18 route.

Method harvest is `RESULT_ONLY`: identifying this residual with a classical Hahn diagonal and its standard difference operator is useful structure, but no new general project-wide method family is being promoted from this execution.

## 4. Successor gate

There is a genuine remaining gap:

\[
Q_n(n;-3n,n-1,3n)\not\equiv0\pmod{6n-1}
\]

under

\[
3\mid n,\qquad 6n-1,\ 4n-1,\ 4n+1\ \text{prime}.
\]

However, an immediate new typed successor is **not** published in this review. The existing live execution for `RS-P022-OBSERVATION-HISTORY` (Draft PR `#741`, registered claim `chatgpt-p022obs-20260827-1645`) is already attacking the same unresolved arithmetic boundary through an independently derived double-horizon / conductor-18 kernel.

Opening another claimable task now would duplicate an active frontier rather than add portfolio diversity. The correct control-plane action is therefore:

1. preserve `RR-EF198E9B037C152CD050` as the accepted exact Hahn reduction;
2. allow the already-live observation-history execution to reach its terminal handoff or lease boundary;
3. if that lane does not close the arithmetic residue, publish a Hahn-specific successor centered on finite-field / Cartier-Frobenius / discrete-operator nonvanishing, using this accepted result as frozen input;
4. do not substitute a larger finite census for proof.

This is a scheduling decision only. It does not demote the accepted Hahn reduction and does not grant authority to any unreviewed statement in PR `#741`.

## 5. Final control state

`RR-EF198E9B037C152CD050 = ACCEPTED / TERMINAL_EXACT_REDUCTION`.

`TP2-18D80E295208AC91EB70 = TERMINAL_BY_AUTHORIZED_EXACT_REDUCTION_STOPPING_CLAUSE`.

`HAHN_DIAGONAL_IDENTIFICATION = ACCEPTED`.

`FRANEL_TO_HAHN_P_UNIT_EQUIVALENCE = ACCEPTED`.

`ALL_PARAMETER_HAHN_NONVANISHING = OPEN`.

`P022_Q_EQ_3R_MINUS_1_BOUNDARY = OPEN`.

`IMMEDIATE_SUCCESSOR_PUBLICATION = WITHHELD_DUE_TO_ACTIVE_OVERLAPPING_P022_EXECUTION`.

`NEXT_CONTROL_PLANE_ACTION = REVIEW_NEXT_TERMINAL_HANDOFF; REASSESS HAHN-SPECIFIC SUCCESSOR AFTER PR #741 HANDOFF OR LEASE EXPIRY`.
