# D25/LIFT GH-86–GH-87 — Frobenius resonance and a signed-jet polynomial certificate

2026-10-29, TASK_RESEARCH (author portable evidence). Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Parent D25/LIFT/JT2 OPEN. Frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Logical lane chatgpt-research-hourly-enterprise-math-20260923; no native claim, session or checkpoint asserted.

## Typed source and hypotheses

Take a prime p=4d+3>=7, k=F_p and theta=z d/dz. Reuse the original GH-84/GH-85 distinct sources S_d=sum_{j=0}^d c_j z^j and U_d=sum_{j=0}^d h_j z^j, where c_0=h_0=1 and

c_(j+1)/c_j=(4j+1)^3/[(4j+2)(4j+3)(4j+4)],
h_(j+1)/h_j=(4j+3)^3/[(4j+4)(4j+5)(4j+6)].

All denominators in these ranges are units and c_d h_d != 0. The true GH-3 sum is T_(p,z)=(8theta+1)S_d; the reflected Laurent obstruction is (8theta+5)U_d. They must not be identified.

Use L_- = theta(theta-1/2)(theta-1/4)-z(theta+1/4)^3 and L_+ = theta(theta+1/4)(theta+1/2)-z(theta+3/4)^3. GH-84 established L_-S_d=(c_d/8) z^(d+1) and L_+U_d=0.

## GH-86 — exact gauge and complete formal solution modules at the singular chart z=0

Set s=(p-1)/2=2d+1, u=(p+1)/2=2d+2, t=(3p-1)/4=3d+2. Since s=-1/2 and u=1/2 in k, theta(z^r f)=z^r(theta+r)f yields exact operator identities

L_-(z^u f)=z^u L_+f, and L_+(z^s f)=z^s L_-f.

Therefore V_d=z^u U_d solves L_-V_d=0, deg V_d=t<p, whereas W_d=z^s S_d has the nonzero terminal obstruction

L_+W_d=(c_d/8)z^t != 0.

The complete formal solution modules are

ker(L_+ : k[[z]] -> k[[z]]) = U_d k[[z^p]],
ker(L_- : k[[z]] -> k[[z]]) = z^u U_d k[[z^p]].

Proof: For Y=sum a_n z^n the recurrences are P_±(n)a_n=Q_±(n-1)a_(n-1), with P_+=n(n+1/4)(n+1/2), Q_+=(n+3/4)^3, P_-=n(n-1/2)(n-1/4), Q_-=(n+1/4)^3. For L_+ the only free residue positions n mod p are 0,s,t. The zero branch is precisely U_d; Q_+(d)=0 makes it terminate at d. The s branch has a nonzero obstruction at t because P_+(t)=0 while Q_+(t-1)=(-1/2)^3 !=0. The t branch has a nonzero obstruction at p because P_+(p)=0 while Q_+(p-1)=(-1/4)^3 !=0. For L_- the potential positions are 0,d+1,u. The 0 branch is killed at d+1 by Q_-(d)=(-1/2)^3 !=0; the d+1 branch is killed at u by Q_-(u-1)=(-1/4)^3 !=0. The u branch is V_d and ends at t because Q_-(t)=0. Each surviving branch has degree <p-1, so no carry obstruction to the next p-block; the coefficient recursion repeats modulo p in every block. Arbitrary block scalars are exactly multiplication by k[[z^p]]. All claimed generators solve the equations, proving equality.

This theorem concerns regular power series at the singular point z=0 only. It does NOT assert the dimension of all ordinary-point solutions at z=9. In particular, the nonzero forced term for W_d cannot be discarded when seeking a second adjoint companion.

## GH-87 — exact quadratic signed-jet identity

Use the signed GH-84 concomitant

B(S,U)=(1-z)[U theta²S-(theta U)(theta S)+(theta²U)S] +(z-3)U theta S/4 +(3-5z)(theta U)S/4 +(2-7z)US/16,

with theta B(S,U)=U L_-S+S L_+U. Substituting S=V_d=z^uU_d gives theta B(V_d,U_d)=0. Direct expansion yields B(V_d,U_d)=z^u R_d with

R_d=(1-z)[2U_d theta²U_d-(theta U_d)^2]+(1-3z)U_d theta U_d/2-(9z/16)U_d².

One cannot infer B is constant from theta B=0 in characteristic p without excluding z^p terms. The z^(2d+1) coefficient of R_d is exactly -(d+3/4)^2 h_d²=0. Hence deg B<=u+2d=p-1. The only polynomial of degree <p killed by theta is constant; B(0)=0 and u>0. Thus B=0 and, since k[z] has no zero divisors,

R_d(z)=0 identically in F_p[z], for every p=4d+3>=7.

This is a lossless signed-jet identity with no division by U_d. If a!=0,1 and U_d(a)=0, it implies U'_d(a)=0. The pre-existing GH-79 ordinary-point no-triple-root bound then gives exact double roots; the latter is a reused consequence, not a newly credited theorem. For U_d(a)!=0, R_d reconstructs theta²U_d from U_d and theta U_d. The GH-84 inhomogeneous pairing B(S_d,U_d) remains nonzero, and T_(p,9) is not determined by R_d alone.

## Author-side exact checks

A separate standalone Python-standard-library verifier constructed both original coefficient arrays and compared complete operator polynomial coefficients, checked all resonance pivots, the full quadratic R_d, and performed independent finite-field matrix nullity checks at p=7,11,19,23,31,43.

PASS_GH86_FROBENIUS_GAUGE: 154 primes p<2000, 282710 exact polynomial coefficient entries.
PASS_GH86_RESONANCE_BLOCKS: all 154, plus 12 independent small-prime kernel-dimension checks.
PASS_GH87_SIGNED_JET_QUADRATIC_CERTIFICATE: all 154, 70716 exact coefficients.

Witness p=23,d=5: S=[1,1,4,2,12,11], U=[1,10,7,21,19,11], u=12,s=11,t=17, L_+(z^11 S)=10 z^17, and L_-(z^12 U)=0. These are finite author checks, not formal checker evidence or independent review.

## BRC, status and continuation

COMPOSE_APPLIED with exact carrier (prime, residue class n mod p, Frobenius block, ordered S/U source labels, signed theta-jets). A coarse support-only quotient loses the nonzero terminal forcing and is invalid. These are auxiliary finite-field scalar charts, NOT a Heartbeat World native X6 proof/transfer. P000 ACTIVE remains unchanged.

Next exact action: return to the *ordinary* observation point z=9. Use the GH-84 inhomogeneous dual sum and the GH-85 exact special-fiber formula, preserving S_d and theta²S_d, and seek an independent CM/WZ arithmetic evaluation or second **local** companion capable of recovering the original T_(p,9) together with the GH-83 Laurent first-order B_0 L correction. Do not mistake the singular-chart kernel or R_d=0 for GH-3. Independent GH-74/75 audit, GH-20/21, W/S, Hasse ports and R23/R36 retain their own obligations.

Native gateway 0.6.11 at this run: research_authority_granted=false, executor_binding_configured=false, source_sync.control.state=CODE_REVIEW_REQUIRED, active_jobs=5/5. Recovery-status contract was advertised but not exposed as a callable native operation in the connection. No native session/claim/open/checkpoint, review, Source acceptance, session transfer or mutation was performed. Existing issue #1558 is the control owner. These author proofs need independent review and canonical admission.