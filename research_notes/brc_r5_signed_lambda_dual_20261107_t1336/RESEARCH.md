# R5 — Two sharp signed-error support directions on a real stopping-time interval

Date: 2026-11-07 (Asia/Shanghai). Author-side status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Provenance and mother question

Frozen scientific inputs unchanged: Global a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Direct predecessor: enterprise-math commit 5f7708b9152857a8b74fec3cff374bb006a8c59d, research_notes/brc_r5_signed_low_key_support_20261107_t1240/RESEARCH.md. Current behavioral context: docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context plus project/global ACTIVE rules. The model is the frozen four-stage P/Q-BRC probabilistic observer, not native X6 spatial dynamics.

The R5 mother question remains equality or strict separation of complete four-observer FULL_HIST and seedless LR images W=(eP,eQ,TP,TQ). This unit solves two perturbed support directions under all seven declaration keys and a continuous symmetric-time interval.

## Exact frozen model

Let (g,a,b,u,v,w,z) be any real flow with 0<=a,b<=g<=1; C0=13a/40+b/80, C1=a/10+9b/40, C2=3a/40+21b/80; 0<=u<=C0, 0<=v<=C1, 0<=w<=C2, 0<=z<=a/10, 0<=v-z<=9b/40.

TP=1+g+(3a+5b)/8+u/2+v+3w/2; TQ=1+g+(a+b)/2+u+v+w.

The ordered likelihood-ratio keys are r=(1/10,1/2,3/4,1,5/4,3/2,19/10). Stopped Q masses are:

~~~
M0 = 509u/900+47z/180+67(v-z)/162+w/100
M1 = C0-u
M2 = (g-a)/2
M3 = 1-g+C1-v+191(u+w)/450+43z/90+14(v-z)/81
M4 = (g-b)/2
M5 = C2-w
M6 = u/100+47z/180+67(v-z)/162+509w/900.
~~~

Choose independent declarations 0<=Ej<=Mj, giving eQ=sum Ej and 1-eP=sum rj Ej. Seedless LR additionally obeys 9*b*z=4*a*(v-z), with legal degenerate branches interpreted directly.

Define U_lambda=eQ-(1+lambda)*(1-eP). At each fixed FULL_HIST timing flow, its maximum over all declarations is obtained by setting Ej=Mj at positive coefficients 1-(1+lambda)rj, and Ej=0 at negative coefficients. Consequently:

~~~
S_plus  = (89/100)M0+(9/20)M1+(7/40)M2                (lambda=+1/10)
S_minus = (91/100)M0+(11/20)M1+(13/40)M2+(1/10)M3    (lambda=-1/10).
~~~

## THEOREM — all-real sharp symmetric-time optima

For each real t in the closed interval 1<=t<=133/40, both unrestricted FULL_HIST and unrestricted seedless LR have the SAME exact maxima

~~~
max{U_(+1/10): TP=TQ=t} = (3869/34875)*(t-1)
max{U_(-1/10): TP=TQ=t} = 1/10+(3041/34875)*(t-1).
~~~

The maxima quantify over all legal real timing and terminal declaration probabilities, including irrational points and endpoints.

### Proof of global upper bounds: exact affine nonnegative certificates

Set t0=31/10 and L=(g-b,u,C1-v,w,9b/40-v+z). Every component of L is nonnegative on the complete FULL_HIST legal flow polytope. Direct exact expansion gives, identically for all seven arbitrary real flow coordinates:

~~~
27083/116250 + (-43037/348750)*(TP-t0) +(81727/348750)*(TQ-t0) - S_plus
 = (13079/558000)*(g-b)
 +(332837/2790000)*u
 +(67769/558000)*(C1-v)
 +(112541/2790000)*w
 +(21983/162000)*(9b/40-v+z).

16456/58125 + (21007/348750)*(TP-t0) +(9403/348750)*(TQ-t0) - S_minus
 = (13781/558000)*(g-b)
 +(46481/930000)*u
 +(54791/558000)*(C1-v)
 +(183499/2790000)*w
 +(17537/162000)*(9b/40-v+z).
~~~

All ten residual coefficients are strictly positive. Both equalities are affine functions of (g,a,b,u,v,w,z); VERIFY.py checks each on the origin and seven coordinate basis vectors, an exact coefficient-level certificate valid over arbitrary real values. Hence U_lambda<=S_lambda and both support inequalities hold for all FULL_HIST strategies. At TP=TQ=t, the sum of time coefficients simplifies to 3869/34875 for lambda plus, and 3041/34875 for lambda minus; evaluating at t=1 yields the constants 0 and 1/10 respectively. This proves the proposed upper bounds.

### Exact seedless LR construction attaining every real point

For any real t in [1,133/40], let q=40*(t-1)/93, so q belongs to [0,1]. Set

~~~
(g,a,b,u,v,w,z)=(q,q,q,0,13q/40,0,q/10).
~~~

All original legality constraints hold; both central histories continue with the same probability; the seedless relation 9*b*z=4*a*(v-z) holds, including q=0 by direct zero-capacity interpretation. We get TP=TQ=1+93q/40=t. The exact stopped mass vector is

~~~
(M0,M1,M2,M3,M4,M5,M6)
=(143q/1200,27q/80,0,1-137q/150,0,27q/80,143q/1200).
~~~

All seven masses are nonnegative, sum to one and have likelihood-ratio first moment one for every real q in [0,1].

For lambda=+1/10, declare only at keys 0 and 1, giving eQ=137q/300, eP=1-271q/1500, U_plus=3869q/15000=(3869/34875)(t-1).

For lambda=-1/10, declare at keys 0,1,3, giving eQ=1-137q/300, eP=1099q/1500, U_minus=1/10+3041q/15000=1/10+(3041/34875)(t-1). The construction proves sharpness for all real times in the claimed interval, not merely rationals.

At t=31/10, q=28/31, the common optimal timing flow yields stopped masses (1001/9300,189/620,0,407/2325,0,189/620,1001/9300). Optimal observer points differ because optimal declaration sets differ:

~~~
lambda +1/10: W=(9728/11625,959/2325,31/10,31/10), U=27083/116250.
lambda -1/10: W=(7693/11625,1366/2325,31/10,31/10), U=16456/58125.
~~~

### Rigidity

Equality in either support certificate forces g=b, u=w=0, v=C1, z=v-9b/40=a/10. Setting TP=TQ then forces a=b, and therefore g=a=b=q=40(t-1)/93. Thus the extremizing timing flow is unique for each fixed real symmetric time t. Terminal declarations at strictly signed coefficients are forced; any zero-coefficient declaration remains free within its own stopped mass.

## Verification and open question

The exact executable Fraction verifier checks the two affine identities on 16 basis evaluations; 94 rational flows (including endpoints and t=31/10) for seedless legality, masses, moments and attainment; and 29 additional asymmetric legal FULL_HIST samples. EXACT_OUTPUT.txt holds actual execution stdout. The all-real theorem follows analytically from the displayed exact identities and formulas; the finite tests validate the arithmetic and implementation.

This proves FULL_HIST and seedless LR have identical support maxima for two new nonparallel directions on the entire stated symmetric-time interval. The complete four-dimensional image equality/separation mother problem remains open. Next: determine exact lambda breakpoints on [-1/10,1/10], compare the competing flow faces, then test asymmetric stop-time slices (NEXT_UNIT.md).

GitHub connected actor awdawmip has repository push/admin permission; native control status returned BACKEND_IDENTITY_OR_VERSION_MISMATCH and operation_sent=false. The Site gateway reports research_authority_granted=false. Active native Owner and formal CLAIM remain unconfirmed. This author-side research publication does not assert native Result/Review or mathematical admission.
