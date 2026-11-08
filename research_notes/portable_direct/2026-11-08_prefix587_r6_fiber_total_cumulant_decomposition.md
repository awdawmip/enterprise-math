# PREFIX-587-R6 — Exact law-of-total-cumulance repair for native BRC start-port mixing

Date: 2026-11-08, Asia/Shanghai.
Status: AUTHOR_PROVED / EXACT_EXHAUSTIVE_FINITE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.
Frozen science: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d` (96 original native ports, 576 labeled actions, zero root).
Research identity/active owner via Source-native session: unconfirmed because live status database is unavailable; this independent source note is not a formal CLAIM, Result or Review.

## Native question

PREFIX-582/583-R6 proved for a uniform native initial-port distribution at every length n:
```
P0=R1+R2, P1=R3+R4, P2=R5+R6;
Y=K-(5R1-R2+5R3-R4-4R5-4R6)/192;
C^(n)_ab=cum(Y_n,P_a(n),P_b(n))=q_n*M_ab;
M=[[0,1,-1],[1,-1,0],[-1,0,1]].
```
At n=2, q_2=-1/864. PREFIX-586-R6 exhaustively established that for each of 96 deterministic start ports i, the native two-step local tensor C_i^(2) has rank 1, is nonzero, and is not proportional to M. There are exactly 15 local matrices. The exact issue is to explain how their uniform mixture produces the rank-2 M, without discarding initial-port provenance or assuming third cumulants commute with a mixture.

## Lemma — law of total third cumulance with initial-port fiber

Let I be the initial native port. For any triple (A,B,C) with all third moments, define conditional means mu_A(I)=E[A|I], similarly for B,C. Direct expansion of the central mixed third moment gives
```
cum(A,B,C)
 = E[cum(A,B,C|I)]
 + cum(mu_A,mu_B,mu_C)
 + Cov(mu_A, Cov(B,C|I))
 + Cov(mu_B, Cov(A,C|I))
 + Cov(mu_C, Cov(A,B|I)).
```
Proof: Write A=mu_A(I)+a where E[a|I]=0, and analogously B,C. Expand E[(A-E A)(B-E B)(C-E C)] and condition on I. Terms containing a single conditional-centered factor vanish. The all-centered, three-mean and three mixed one-mean/two-centered terms are precisely those displayed. This is an exact identity without an independence assumption between the observed variables.

## Theorem — all four exact between-fiber contributions at native depth two

Take I uniform on all 96 frozen native ports and, conditional on I, independently choose each of the six native action labels with probability 1/6 at both steps. Set A=Y_2, B=P_a(2), C=P_b(2). Define the symmetric 3x3 matrices corresponding to the five lemma terms (grouping the two symmetric last terms into one).

Full exact Fraction enumeration of all 96*6*6=3456 labeled paths proves:
```
E_I[ cum(Y,P_a,P_b | I)]                            = 0*M_ab
cum_I(mu_Y,mu_Pa,mu_Pb)                              = (1/7776)*M_ab
Cov_I(mu_Y, Cov(P_a,P_b | I))                        = (-1/1296)*M_ab
Cov_I(mu_Pa,Cov(Y,P_b|I)) + Cov_I(mu_Pb,Cov(Y,P_a|I))= (-1/1944)*M_ab
-----------------------------------------------------------------------
cum(Y_2,P_a(2),P_b(2))                                = (-1/864)*M_ab.
```
The scalar cancellation is exact because
```
(1/7776) -(1/1296) -(1/1944)
=(1-6-4)/7776 = -9/7776 = -1/864.
```
An independent direct exact third-cumulant calculation over the pooled 3456 paths agrees entrywise with the decomposition and with PREFIX-582/583's uniform-start scalar q_2.

**Consequence.** Every pure-port local cubic tensor is individually nonzero (PREFIX-586), yet its uniform average over ports is exactly the zero matrix. Therefore the entire uniform-start depth-two cubic signal `-M/864` comes from between-initial-port variation of conditional means and covariances. This is an explicit BRC observer-fiber reconstruction certificate: the start-port fiber is a necessary repair coordinate for conditional-to-pooled cumulant reconstruction, even when the averaged local third tensor vanishes. This exact statement concerns the declared third-cumulant observer and two-step horizon; the native labeled path data remain intact.

## Verification and coverage

Run published `PREFIX587_R6_mixture_cumulant_certificate.py` beside source `PREFIX565_positive_marginal_certificate.py`. The checker reads the original frozen `edge(initial, action, ZERO_ROOT)` and checks `SCIENCE_PIN`, all 96 x 6 x 6 edge sequences, all five 3x3 exact rational decomposition terms and a separate pooled calculation with exact Fraction arithmetic. Its local result was `ALL_CHECKS_PASS`; the source result is `PREFIX587_R6_MIXTURE_RESULTS.json`.

This is a complete finite theorem for exactly two native steps and the specified frozen zero-root action law. It is a new local construction, separate from all-length coefficient results of PREFIX-585-R6.

## Next discriminating question

For each initial-port mixture distribution pi (not necessarily uniform), derive the minimal per-fiber sufficient stored observations that allow exact reconstruction of the pooled third cumulant under a declared finite-horizon action semigroup. Seek an exact representation that preserves enough branch provenance while compressing the 96-port conditional moment arrays, and classify the effect of changing the nine frozen native roots. Test for small native automorphism orbits underlying the 15 pure-port local cubic matrices. Maintain distinct observer scope and project proof/admission status.
