# D25 — Coupled Gauss parameter jets and a universal Frobenius source charge

Date: 2026-11-07. TASK_RESEARCH author-side portable proof and executed exact regression; UNREVIEWED / NOT_ADMITTED. Logical Research lane: chatgpt-research-hourly-enterprise-math-20260923, separate from maintenance chatgpt-hourly-enterprise-math-20260921. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific input c47e13e4aba0e006366f989d6334d443f6333ae3. Mother problem: prove W_p ≡ p (mod p³) for every p≡13,19 (mod24), still OPEN.

## Theorem 1 — universal two-jet deformation of a truncated Gauss polynomial

Let p>3 be prime, 0<u<v<p-1, and c1,c2 be p-integral rationals. The formal parameter h is independent of p. Put

~~~text
G(h,z) = Σ_{n=0}^{p-1} [(-u+c1*h)_n (-v+c2*h)_n/(n!)²] z^n
       = Q(z) + h P(z) + h² S(z) + O(h³),
D = z*d/dz,       L0 = D²-z(D-u)(D-v),
K = c1(D-v)+c2(D-u).
~~~

S is the literal coefficient of h² (half the second derivative). All coefficient denominators are p-units for n<p. These are **exact polynomial identities over rational coefficients**:

~~~text
L0 Q = 0,
L0 P = z K Q,
L0 S = z K P + c1*c2*z*Q - b_p*z^p,                        (1)

b_p = c1*c2*(-1)^(u+v) u!v!(p-1-u)!(p-1-v)!/((p-1)!)².
~~~

Let R(z) retain only the degrees v+1,...,p-1 of S(z). Then

~~~text
[z^n]R = c1*c2*(-1)^(u+v) u!v!(n-u-1)!(n-v-1)!/(n!)²
         (v+1<=n<p),

L0 R = c1*c2*(-1)^(u+v)/binom(v,u)*z^(v+1) - b_p*z^p.    (2)
~~~

In F_p the factorial-reflection identity gives b_p≡c1*c2. Thus both models have the **same normalized top source -z^p**. The lower endpoint keeps model-specific u,v and binomial provenance.

**Proof.** Let L_h=L0-h*z*K-h²*c1*c2*z. Gauss coefficient recurrence annihilates G through degree p-1, leaving exactly

~~~text
L_h G=-(p-1-u+c1*h)(p-1-v+c2*h)*[z^(p-1)]G*z^p.
~~~

Two distinct Pochhammer factors in [z^(p-1)]G are c1*h and c2*h (indices u and v), so the boundary starts at h². Compare h^0,h^1,h² to obtain (1), with b_p given above by removing the two zero factors. For n>v, both products have a simple zero in h, giving the displayed R_n. Its recurrence is homogeneous in degrees v+2,...,p-1; the coefficient at v+1 is (v+1)² R_(v+1)=c1*c2*(-1)^(u+v)/binom(v,u), and at p it is -(p-1-u)(p-1-v)R_(p-1)=-b_p. This proves (2) over Q. Finally (p-1-u)!u!≡(-1)^(u+1) and similarly for v; Wilson yields b_p≡c1*c2 modp. QED.

## Theorem 2 — first-jet Wronskian/Green flux

The coupled first equation implies the following rational-function identity:

~~~text
d/dz [z*(Q P' - Q' P)/(1-z)^(u+v)]
 = Q*[(c1+c2)*z*Q'-(c1*v+c2*u)*Q]/(1-z)^(u+v+1).      (3)
~~~

Proof: subtract P*(L0 Q)=0 from Q*(L0 P)=z Q KQ; the resulting first-order Wronskian equation has integrating factor z/(1-z)^(u+v). This identity is also a polynomial equality after clearing the denominator.

At a simple Hasse zero x with Q(x)≡0 modp (x≠0,1), define q=Q(x)/p modp using the actual p-integral *lift* of Q at rational x, f=P(x) modp and J=(DQ)(x) modp. Specializing h=p yields the exact first-digit reconstruction

~~~text
G(p,x)/p ≡ q+f  (mod p).
~~~

Writing Phi=z*(Q P'-Q'P)/(1-z)^(u+v) gives Phi(x)=-J*f/(1-x)^(u+v). The outstanding normalized first-digit product c*J*(q+f)=1 is therefore equivalent to

~~~text
c*J*q - c*(1-x)^(u+v)*Phi(x) = 1 (mod p).               (4)
~~~

Equation (4) specifies the **next exact universal proof target**, not a completed universal unit theorem. It preserves the two source coordinates q and f rather than erasing them in their sum.

## Exact recovery of the separately proved D25 Frobenius boundaries

A/216: p=6m+1, u=m, v=2m, (c1,c2)=(1/6,1/3). Since c1*c2=1/18, (2) gives

~~~text
18 L0 R_A = (-1)^m/binom(2m,m) * z^(2m+1) - z^p  (mod p).
~~~

B/2304: u=k, v=3k+1 and (c1,c2)=(1/8,3/8) for both p=8k+3 and 8k+5 (swap hypergeometric order in B3; Euler parameters in B5). Since c1*c2=3/64 and u+v=4k+1, (2) gives

~~~text
(64/3) L0 R_B = -z^(3k+2)/binom(3k+1,k) - z^p   (mod p).
~~~

These are the two previously obtained endpoint laws (not claimed as a fresh discovery). **New connection:** their high second-order source is the tail of the *same* Gauss parameter deformation whose first-order source P controls the low Gauss Hasse lift. The hierarchy (1) and Wronskian (3) provide one source-preserving route from CM first digits to high Frobenius carry, without equating A and B ports.

BRC carrier: (Q,P,S_low,R,b_p), with branch labels A/B and, for B, Euler B3/B5; future operations are Hasse evaluation, D, Fricke pullback and p-adic second-digit extraction. The quotient G(p,x)/p discards the separate q/f origin, and is not a sufficient carrier for the next attribution operation.

## Executed mathematical checks

Companion executable: research_notes/portable_direct/d25_parametric_gauss_twojet_20261107.py. It uses pure integer arithmetic, independent coefficient-jet and Z/p² Gauss recurrences, independent factorial kernels, polynomial differential residuals including the z^p boundary, and (3) cleared of denominators on all target primes <=67. **PASS on all 94 target primes p<2500 for both streams (188 model instances)**. Equation (4) evaluated to 1 for all 188, an exact finite observation.

Examples in F_p as (q,f,J,G(p,x)/p,lower charge,top charge):

~~~text
p=13:  A=(7,4,7,11,10,5);          B=(3,8,12,11,4,3)
p=19:  A=(6,2,1,8,1,1);            B=(10,18,7,9,12,5)
p=373: A=(340,57,294,24,155,145); B=(326,33,41,359,17,134)
~~~

At p=13 the total Gauss quotient equals 11 in both streams but their (q,f) pairs differ; this is a concrete observer-fiber provenance loss. The p=373 run is a portable finite-ring check, separate from the native H0/B0/divided-power/Hesse-κ experiment and independent replication #1559.

## Highest frontier / next action / protected state

Reused without repetition: D25 p² Euler/Clausen fold, three-strata p³ A/B kernels, separate short overflows, the two-endpoint theorem, scalar second digit, and the parallel on-hour author-side CM/Hasse-zero proof at 923b2bc381b55c3289ba1d08d336bdf21d8ef00b. The mother target and p-adic unit proof remain open.

**Next discriminating action:** evaluate the finite-field rational Green flux Phi_A(1/2), Phi_B(1/9), with their different integer lift q_A,q_B. Search a Cartier/Fricke transfer proving (4) uniformly without assuming the desired weighted congruence. First test at p=13,19,43,67,373; then use (1)/(2) to transfer the second-digit charge through the existing four-port formula.

Actual Site local check 2026-11-07T15:17:06Z: CONFIGURED_NOT_LIVE_VERIFIED. Actual em_status({}) error: BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false. No authenticated native Researcher permission; no new native recovery, CLAIM, OPEN, checkpoint, Result or review. Preserve unresolved original requests em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13, old session/staging as UNKNOWN. Existing control owner/support: awdawmip/enterprise-math#1558. This GitHub artifact is author-side evidence / REGISTER_PENDING / SYNC_DEBT, not a native task checkpoint.
