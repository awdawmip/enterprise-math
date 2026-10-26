# D25/LIFT R27 — Exact finite-field W/S Picard–Fuchs source intertwiner and resonant boundary transfer

Date: 2026-10-27, Asia/Hong_Kong. Actual scheduled TASK_RESEARCH logical lane: chatgpt-research-hourly-enterprise-math-20260923; do not use maintenance chatgpt-hourly-enterprise-math-20260921. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Parent D25/LIFT/JT2 remains OPEN.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** Not a native authorized run, Source checkpoint, original-class H0/B0/Frobenius experiment, Result, independent review, or LIFT proof.

## Consumed mathematical inputs; exact new question

Consume without recredit R23 (a88573ebcb030a8ddedc6a3d8020805ec88cb1d7), R24 (73a9246ec47de455e7c21c97135ca6e60ffc5a71), R25 (cd33744aa6ab958e6d1b1db2bab31116c645a24a), and R26 (41eadf654f5c0b97cdc207b9534aa6ab58d0f3ee). R24 identifies distinct finite-field differential operators and individually nonzero truncation sources; R25 finds the exact invertible Hadamard kernel h_r; R26 retains a lost original S port at the fourth p-adic digit. The new question is whether the entire *inhomogeneous residual operators*, INCLUDING their cutoff coefficient X^m, admit an exact information-preserving intertwiner. A coefficientwise equality of just two truncated solutions does not by itself answer this question.

Fix a prime p=6m+1>=7, work over F_p, and write theta=X*d/dX. Define the original R24 operators

~~~
L_W = theta*(theta+1/6)*(theta+1/3) - X*(theta+2/3)^3,
L_S = theta*(theta-1/12)*(theta+1/6)*(theta+5/12)
      - X*(theta+1)*(theta+2/3)^3.
~~~

For every 0<=r<m set

~~~
h_r=(4/3)_r*r! / ((11/12)_r*(17/12)_r), h_0=1,
(r-1/12)*(r+5/12)*h_r = r*(r+1/3)*h_(r-1) (1<=r<m).
~~~

Every denominator here is a unit on the strict range; the r=m singularity belongs to the a/b recurrences and is NOT traversed. Define two F_p-linear, explicitly SOURCE-BOUND operators:

~~~
H_m [sum_(r=0..m-1) f_r X^r] =
       sum_(r=0..m-1) h_r f_r X^r,

K_m [sum_(r=1..m) g_r X^r] =
       sum_(r=1..m) r h_(r-1) g_r X^r.
~~~

## Theorem A — exact residual intertwining including the resonant endpoint

For every f in F_p[X] of degree <m,

~~~
                   L_S ( H_m f ) = K_m ( L_W f )          (1)
~~~

as FULL polynomials in F_p[X] of degree <=m, not merely modulo X^m. Moreover K_m is an automorphism of the positive-degree residual space X*F_p[X]_(<=m), since every r h_(r-1) is a unit for 1<=r<=m.

**Proof.** Set f_m=0 and u_r=h_r f_r for r<m, u_m=0. The coefficient of X^r (1<=r<=m) in L_W f is

~~~
W_r= r*(r+1/6)*(r+1/3)*f_r - (r-1/3)^3*f_(r-1).
~~~

That in L_S H_m f is

~~~
S_r= r*(r-1/12)*(r+1/6)*(r+5/12)*h_r*f_r
     - r*(r-1/3)^3*h_(r-1)*f_(r-1).
~~~

For 1<=r<m, R25's exact h recurrence makes S_r=r*h_(r-1)*W_r. For r=m the f_m term vanishes on BOTH sides by truncation, and the same equality follows from the remaining lower-index coefficient without defining h_m. At r=0 both operators have zero constant coefficient. This proves (1) at EVERY coefficient, INCLUDING the source X^m. Unit invertibility follows from 1<=r<=m<p and nonzero h_(r-1). QED.

## Theorem B — normalized diagonal source transport is unique

Suppose diagonal coefficient transports H(f)_r=alpha_r*f_r (0<=r<m, alpha_0=1) and K(g)_r=k_r*g_r (1<=r<=m) satisfy L_S H=K L_W for ALL f of degree <m. Then necessarily

~~~
k_r=r*alpha_(r-1),                    1<=r<=m,
alpha_r/alpha_(r-1) =
     r*(r+1/3)/((r-1/12)*(r+5/12)), 1<=r<m.
~~~

Hence alpha_r=h_r and k_r=r h_(r-1); (H_m,K_m) is the UNIQUE normalized diagonal operator pair on the stated source-labelled spaces. This uniqueness does not claim no non-diagonal WZ or gauge transform exists.

**Proof.** For 1<=r<m compare separately the coefficients of free independent inputs f_(r-1) and f_r in L_S H f=K L_W f. The former forces k_r=r alpha_(r-1) because (r-1/3) is nonzero, and the latter forces the displayed recursion after cancelling the p-units r, r+1/6, r+1/3. At r=m only f_(m-1) occurs, forcing k_m=m alpha_(m-1). The recurrence and alpha_0=1 determine all remaining coefficients uniquely. QED.

## Corollary — the two nonzero PF endpoint forcings are the SAME transferred residual datum

Let F_W=sum_(r<m) a_r X^r, F_S=sum_(r<m) b_r X^r with the *actual* R24/R25 Pochhammer coefficients and b_r=h_r a_r. As R24 proved,

~~~
L_W F_W= (a_(m-1)/8)*X^m !=0,
L_S F_S=-(b_(m-1)/48)*X^m !=0.
~~~

Equation (1) now gives the precise, nonzero transfer:

~~~
    [X^m]L_S F_S / [X^m]L_W F_W
             = m*h_(m-1) = -h_(m-1)/6   in F_p^x.   (2)
~~~

Thus the two cutoff forcings are not independent *at this specified exact Hadamard source interface*: one determines the other by a unit multiplier. Neither forcing can be deleted, and an observation that drops X^m would erase BOTH. This strengthens R24's two separately computed nonzero endpoint certificates; it does not overturn their result.

Example checks (p, m, h_(m-1), K_m endpoint unit, W endpoint, S endpoint), all modulo p:

~~~
(13,2,2,4,9,10)
(19,3,4,12,16,2)
(181,30,87,76,62,6)
(373,62,68,113,251,15)
(733,122,449,536,729,55)
~~~

The identity concerns coefficientwise PF source transport. The genuine SOURCE-WEIGHTED outputs still read

~~~
U_p = C_m * [(1+2*theta)F_W](2),
M_p = D_m * [(13/3+8*theta)F_S](9)        (mod p).
~~~

H_m does not equate these TWO distinct evaluations, and the lost S-weight coordinate at p=13(mod24) remains as in R25/R26. No all-prime W_p=S_p mod p^3 bridge follows, and original z=2 Clausen six-channel ports, finite faces, infinity/high-high sources remain separately typed.

## Executed exact author check, reuse resolution and next action

Checker: research_notes/portable_direct/20261027_hourly_d25_pf_source_intertwiner_r27_check.py. Executed in local Python 3 standard library: PASS for all 148 primes p<2000 with p=1(mod6). At all 22,952 positive-degree residual indices, checked (1) for three distinct polynomial inputs each (68,856 coefficient comparisons); independently checked 148 pairs of nonzero endpoint values plus Pochhammer recursion. Finite evidence is author checking, not the basis of the all-prime proof or independent review.

**BRC COMPOSE_APPLIED**: input carrier has W and S labelled factorial provenance, strict index cutoff r<m, finite-field coefficient arrays, independent internal residuals, endpoint X^m and source-weighted observers U/M. Future operations include theta derivatives, the PF equations, and the H_m/K_m transfer. K_m is exact, label-sensitive, invertible on residuals; quotienting by X^m destroys a source and cannot be silently treated as a safe congruence for all future operations. These are external finite-field indices, not Enterprise X6 native directions or a change to P000, ACTIVE worldview or accepted Foundation.

**Actual source status.** Last read-only Research-lane recovery #6571 and complete canonical continuation #6572/#6573/#6574 verify durable native checkpoint bytes but report NO_LIVE_CLAIM, NEEDS_DISPATCH, execution_authorized=false and a mismatch between previous checkpoint claim and latest claim. The current direct continuation attempt request_id researchhourly-20261027-0721-continuation-r27 returned CONTROL_QUOTA; the original request ID returned CONTROL_REQUEST_NOT_FOUND on readback. No own fresh claim/open authorization or Source publication was obtained. No service session_close/claim mutation, neutral staging disposal, maintenance-lane identity use, or scheduler modification. Existing support owner: enterprise-math Issue #1558. Registration of this R27 semantic increment is REGISTER_PENDING/SYNC_DEBT absent a verified activity-registration event.

**NEXT unfinished portable unit after (1).** Seek a *source- and evaluation-preserving* adjoint/WZ certificate that carries the distinct output functionals (1+2theta) at 2 and (13/3+8theta) at 9, including the p=13(mod24) missing original S port and exact low-half p^2-divided defect. An operator intertwiner on the entire residual space is a useful transport lemma, NOT the required scalar equality. Separately original-class H0/B0, [X]U modp^2, eta/kappa and p373 native execution remain NOT_DONE; independent Driver review remains pending. Preserve parent task OPEN and source pin unchanged.
