# D25 portable research: special-truncation reverse-fiber no-go

Status: AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT

Source boundary:
- GLOBAL_KNOWLEDGE_V1 canonical main: 12b0249e263af560f1f7ec7bc83dbfb1c42d844a
- Enterprise Math canonical main: cf8822a58936d46dac0795281224a79e99b8ce00
- P000 blob: 7334734bd1cff6d60bd6b73cd0c588fe01c88714
- AUTONOMOUS_RESEARCH_OPERATIONS blob: 83723848b8deb6d408e3af6d290088c58a6d88c6
- canonical D25_LOCAL_PROGRESS blob: 51dd15a8142f3dda0506a306f9c0693a036f5891
- predecessor portable head: e11351757017196785b31ab8aab6e9bd75ae770e
- recovery Issue #2621 remains read-only SUCCEEDED with session_state=ABSENT and execution_authorized=false.

This unit consumes the staged finite-connection reduction and tests the exact remaining loophole: whether the target truncation itself makes the two half-shift connection bands rationally reflect/telescope.

Let
T_j=p J(m+j) Q_j(m).
The forward universal band ratios are
R_B(r)=R_A(r-1/2), with

R_A(r)=
((4r+1)^2(4r+3)^2(12r+7)(12r+13) P_A(r+1))/
(18(r+1)(2r+3)(4r+5)^2(4r+7)^2 P_A(r)),
P_A(r)=144r^3+200r^2+97r+17,

and

R_B(r)=
((4r-1)^2(4r+1)^2(12r+1)(12r+7) P_B(r+1))/
(18(r+1)(2r+1)(4r+3)^2(4r+5)^2 P_B(r)),
P_B(r)=288r^3-32r^2+10r+1.

For p=12L+1 (class 13 mod 24), pair A_r with B_{L-r}, leaving B_0 as a boundary row. Since L=-1/12 mod p, the reversed-B ratio is

Rrev13(r)=
((3r+1)^2(6r-1)^2(12r+1)(12r+7)
 (1296r^3+4356r^2+4920r+1861))/
(288(r+1)(2r+1)(3r+4)^2(6r+5)^2
 (1296r^3+468r^2+96r+1)).

For p=12L+7 (class 19 mod 24), the equal-length pairing A_r with B_{L-r} has L=-7/12 mod p and

Rrev19(r)=
((3r+1)^2(6r+5)^2(12r+7)(12r+13)
 (324r^3+1575r^2+2562r+1393))/
(288(r+1)(2r+3)(3r+4)^2(6r+11)^2
 (324r^3+603r^2+384r+82)).

Exact Gosper normalization gives, for Rrev13,
A=(3r+1)^2(6r-1)^2(12r+1)(12r+7)/186624,
B(r-1)=r(2r-1)(3r+1)^2(6r-1)^2/648,
C=(1296r^3+468r^2+96r+1)/1296.

Degrees are (6,6,3), with leading coefficients 1/4 and 1; hence the candidate Gosper polynomial degree is d=3-6=-3. No rational antidifference exists.

For Rrev19,
A=(3r+1)^2(6r+5)^2(12r+7)(12r+13)/186624,
B(r-1)=r(2r+1)(3r+1)^2(6r+5)^2/648,
C=(324r^3+603r^2+384r+82)/324,

again giving degrees (6,6,3), leading coefficients 1/4 and 1, and d=-3. So the class-19 reversed fiber is also not rationally Gosper-summable.

A nonconstant rational reflection weight g(r) would satisfy
g(r+1)=[Rrev13/RA] g(r)
or
g(r+1)=[Rrev19/RA] g(r).
Exact Abramov rational-recurrence reduction returns only the zero rational solution in both cases. Thus A_r and the target-reversed B fiber are linearly independent over Q(r).

Consequently a rational two-fiber boundary ansatz
G(r)=u(r)A_r+v(r)B_{L-r}
for a nonzero scalar combination separates into two scalar rational antidifference equations. The A equation already has the forward d=-3 obstruction; the reversed-B equations have the d=-3 obstructions above. Therefore the existing rational weighted/reflection two-ended interface cannot eliminate the paired interior.

Actual target-prime witness: at p=19 the finite bands are B=(6,14), A=(10,12) mod 19, hence reversed B=(14,6). Constant reflection fails since
10*6-12*14=-108=6 mod 19 != 0.

Fresh exact-rational regression:
- all 45 target primes p<1000 with p=13 or 19 mod 24;
- includes p=811;
- forward A cross-multiplied recurrence: 45/45 pass;
- target-reversed B class-correct cross-multiplied recurrence: 45/45 pass;
- singular auxiliary ratio charts are retained cross-multiplied rather than divided through.

Proof-strength boundary:
This rules out a uniform rational weighted/reversed two-fiber endpoint certificate in the characteristic-zero Q(r) module, including the target-truncation reversal. It does not rule out p-dependent high-degree finite-field identities special to individual primes.

BRC:
population = two extended connection bands only;
observer = Lambda_p;
unsafe quotient = replace paired interior by old endpoint coordinates through rational reflection/telescoping;
separation = reverse-fiber Gosper d=-3 + Abramov rational independence + p=19 witness;
safe repair = retain Lambda_p;
reuse disposition = COMPOSE_APPLIED / TARGET_TRUNCATION_REVERSED_FIBERS / RATIONAL_WEIGHTED_REFLECTION_NO_GO / LAMBDA_RETAINED.

Local immutable evidence prepared in the execution conversation:
- d25_b_chart_special_truncation_reflection_no_go_20261001.md
  SHA256 369b4ca3c2f6b38451e222c6a40a980a4dfaae48f4c68faba8388525c6eccc03
- d25_special_truncation_reflection_checker.py
  SHA256 50b56f59c152e2f1242561b14d6c592f5c03f9b80c15efaee10710befe64c4f7
- D25_SPECIAL_TRUNCATION_REFLECTION_RESULT.json
  SHA256 573bd894c8cd76d3692c48e9ecab84217d809e2c4047503722ecfeaa0e16f4a8

Next exact unit:
Do not retry Gosper or restore rowwise Xi. Test genuinely p-dependent low-complexity finite-field dependence of Lambda_p on already-owned endpoint coordinates (delta_p, theta_p) and residue-class data. Either derive a finite-field law or produce a bounded-degree separation certificate showing that Lambda_p is a genuinely new arithmetic repair coordinate.
