# D25 / SECOND-DIGIT-LIFT — original E3 second-kind coefficient, exact closed sum and normalization negative control

Date: 2026-10-27. Logical lane: chatgpt-research-onhour-enterprise-math-20260923 (TASK_RESEARCH; not maintenance).
Mother task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen SCIENTIFIC Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).
Class: AUTHOR-SIDE exact algebraic proof + executed finite calculations; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. Native fixed H0/B0 divided-power benchmark remains NOT_EXECUTED / PENDING_OWNER. This is NOT a native [X]U computation, a Source-native checkpoint, Frobenius normalization, a LIFT all-prime proof, or an independent review.

## New exact original-coordinate formula (not a substitute model)

For the **original** family E_c: y²+xy+cy=x³, set c=(2-T)/108 with T²=2, and take its genuine local coordinate xi=-x/y. The invariant differential and the algebraic de Rham second-kind representative are

    omega = dx/(2y+x+c),     eta = x omega.

Let f(xi) be the unique formal x-coordinate satisfying

    x = c*xi + xi*x + xi²*x²,   x(0)=0.

Put D(xi)=(1-xi)²-4c*xi³ with square root of constant term +1. Solving the quadratic and differentiating exactly gives

    x(xi)=((1-xi)-sqrt(D(xi)))/(2xi²),
    omega = - dxi / sqrt(D(xi)).

The final identity follows directly: differentiating xi²x²-(1-xi)x+cxi=0 and using
c+x-2x/xi=-(x/xi+xi*x²) gives dx/dxi divided by 2y+x+c equal to -1/sqrt(D).
This is an identity of original-curve formal differentials, with no Hesse substitution and no Frobenius assumptions.

Define **sign-aligned coefficients** a_n = -[xi^n](omega/dxi), b_n = -[xi^n](eta/dxi), so b is the formal coefficient of x/sqrt(D), NOT the authenticated normalized Proposition-16 / Gauss-Manin companion. Set z=c*xi³/(1-xi)². Since (1-4z)^(-1/2)=sum_j binom(2j,j)z^j, for every n>=0 the following two exact identities hold over characteristic-zero Q(c), and integrally when the denominators of c are units:

    a_n = sum_{j=0}^{floor(n/3)}
                 binom(2j,j)*binom(n-j,2j)*c^j.                    (A)

    b_n = (1/2) sum_{j=1}^{floor((n+2)/3)}
                 binom(2j,j)*binom(n-j+1,2j-1)*c^j.              (B)

Proof of (B), retaining the unnormalized second-kind observer:

    x/sqrt(D) = (1/(2xi²)) * [ (1-4z)^(-1/2) - 1 ].

Extracting coefficient xi^n gives (B). The integer binomial coefficient binom(2j,j) is even for j>=1, so the apparent factor 1/2 creates no new rational denominator in the coefficient. (A) follows similarly from 1/sqrt(D)=(1-xi)^(-1)(1-4z)^(-1/2). These are exact identities, not extrapolations from primes. Prior source notes already calculated a_n by a hypergeometric expression; the new narrow deliverable here is **the companion b_n for the actual unmodified second-kind representative**, with a validated original-coordinate sign and a native comparison discriminator. No originality beyond this task-specific derivation is claimed.

## Exact p=373 certificate

In R=(Z/373³ Z)[T]/(T²-2), 373³=51,895,117, the formulas give:

    a_372 = 46,042,747 + 33,130,606 T = 373*(123,439+88,822T);
    b_372 = 40,642,453 + 16,308,355 T            (mod 51,895,117).

The value a_372/373 modulo 373² independently agrees with previously saved original-source formal E3 coefficient calculation (the prior certificate is not recredited). Reducing a_372/373 and b_372 modulo 373 gives

    A=349+48T,  B_plain=49T,  A*B_plain=228+316T (mod 373).

This product agrees *numerically* with the **already independently derived** original de Rham CM-eigenbasis mixing coefficient beta=(4-T)/72, for which beta mod373 = 228+316T (see immutable original isogeny note d2d534fdd3c02cbccd02f831b2989e03e6e9ae68). At eight tested target primes the same equality A*B_plain=beta modulo p occurs; **this is a finite observation, NOT a proved all-prime identity or an independent confirmation of native normalization**.

Under the *conditional* Proposition-16 supersingular Frobenius normalization b2=p, the desired normalized coefficient instead must satisfy A*B_required=-1, hence B_required=242+111T mod373; indeed A*(242+111T)=372 in F_373. Therefore

    B_plain = 49T != 242+111T = B_required (mod 373).

This is a concrete original-model negative-control witness. Even the genuine **source algebraic de Rham basis representative eta=x omega** cannot be silently treated as the normalized companion. A nontrivial exact-basis transport/normalization, including principal-part and Frobenius convention, must be proved first. It is a type/observer mismatch, NOT an exact counterexample to LIFT, and does not authenticate the true H0/B0 rank or [X]U coefficient.

## Executed standard-library verification

The following reproduction uses exact modular pair arithmetic in T²=2 and checks (A), (B) for p=13,19,37,43,61,67,211,373, retaining complete p³ precision at 373. It additionally independently constructs x via its quadratic recursive equation and then the original differential via dx/dxi/(c+x-2x/xi), and checks BOTH basis columns coefficient-for-coefficient for the selected target indices. All assertions passed in this research turn. Finite tests are not universal proofs and do not execute H0/B0.

~~~python
from math import comb

def check(p):
    Q = p**3 if p == 373 else p**2
    zero, one = (0, 0), (1, 0)

    def add(x,y):
        return ((x[0]+y[0])%Q, (x[1]+y[1])%Q)
    def neg(x):
        return ((-x[0])%Q, (-x[1])%Q)
    def scale(k,x):
        return ((k*x[0])%Q, (k*x[1])%Q)
    def mul(x,y):
        return ((x[0]*y[0]+2*x[1]*y[1])%Q,
                (x[0]*y[1]+x[1]*y[0])%Q)
    def inv(x):
        norm = (x[0]**2-2*x[1]**2)%Q
        return scale(pow(norm,-1,Q),(x[0],-x[1]))

    c = scale(pow(108,-1,Q),(2,-1))
    n = p-1
    powers = [one]
    for j in range(1,(n+2)//3+1):
        powers.append(mul(powers[-1],c))
    a,b = zero,zero
    for j in range(n//3+1):
        a=add(a,scale(comb(2*j,j)*comb(n-j,2*j),powers[j]))
    for j in range(1,(n+2)//3+1):
        b=add(b,scale(comb(2*j,j)*comb(n-j+1,2*j-1)*pow(2,-1,Q),powers[j]))

    # Independent original-curve formal recurrence, not reuse of (A)/(B).
    x = [zero for _ in range(n+2)]
    x[1]=c
    for k in range(2,n+2):
        v=x[k-1]
        for i in range(1,k-2):
            v=add(v,mul(x[i],x[k-2-i]))
        x[k]=v
    D=[neg(c)]  # constant term of c + x - 2x/xi
    for k in range(1,n+1):
        D.append(add(x[k],neg(scale(2,x[k+1]))))
    w=[]
    for k in range(n+1):
        v=scale(k+1,x[k+1])
        for j in range(1,k+1):
            v=add(v,neg(mul(D[j],w[k-j])))
        w.append(mul(inv(neg(c)),v))
    a_rec=neg(w[n])
    b_rec=zero
    for i in range(1,n+1):
        b_rec=add(b_rec,mul(x[i],w[n-i]))
    b_rec=neg(b_rec)
    assert (a,b)==(a_rec,b_rec)

    assert a[0]%p == a[1]%p == 0
    A=(a[0]//p%p,a[1]//p%p)
    B=(b[0]%p,b[1]%p)
    AB=((A[0]*B[0]+2*A[1]*B[1])%p,
        (A[0]*B[1]+A[1]*B[0])%p)
    beta=(4*pow(72,-1,p)%p,-pow(72,-1,p)%p)
    assert AB==beta  # tested samples only; conjectural globally
    if p==373:
        assert a==(46042747,33130606)
        assert b==(40642453,16308355)
        assert A==(349,48) and B==(0,49)
        assert AB==(228,316)
    return p,A,B,AB

for p in (13,19,37,43,61,67,211,373):
    print(check(p))
~~~

Observed (p,A,B,AB):
~~~
(13, (2, 9), (0, 12), (8, 11))
(19, (11, 16), (0, 16), (18, 5))
(37, (14, 9), (0, 4), (35, 19))
(43, (12, 19), (0, 32), (12, 40))
(61, (37, 48), (0, 58), (17, 11))
(67, (6, 55), (0, 29), (41, 40))
(211, (18, 175), (0, 7), (129, 126))
(373, (349, 48), (0, 49), (228, 316))
~~~

## Observer/BRC provenance and continuity

Declared object: the **original** E3 curve, xi=-x/y, formal invariant omega, and original second-kind representative x omega. Typed field/branch: T²=2; at target p the Frobenius sends T to -T; signs of both de Rham columns and the normalization condition are NOT discarded by taking norms. Formal-coefficient and divided-power cohomology objects are different observers; the present exact lift keeps two columns and p³ coefficients but does not build the latter's quotient or its canonical normalized Frobenius map.

Consumed and do-not-repeat: accepted D24 UR/JT0, source original a coefficient check; earlier independent degree-2/3 isogeny and beta eigenbasis result; prior fixed-z derivative and basefield no-go; prior finite W scans and Wilson companion tail. The arithmetic equality for A*B_plain at finite p is a cross-observation only.

Highest unfinished scientific obligation: authorized original-class fixed H0/B0 divided-power evaluator, actual [X]U mod 139129 at p=373, rank, semilinear Frobenius direction, full two-digit eta/basis normalization, signed Green/Hesse observer, and original kappa/Delta-R. Existing responsible intake: https://github.com/awdawmip/enterprise-math/issues/1559 ; PENDING_OWNER / NOT_EXECUTED. The next exact native action is to authenticate and run that original representation, document raw reproducer/source pin and compare its operator to (A)/(B) **only after a proven correspondence**. A candidate identification that equates b_plain with normalized b is directly ruled out at p373 under the stated supersingular normalization.

Control handoff: prior own recovery request research-onhour-20261027-0501-recovery-r13 (https://github.com/awdawmip/kimi-query-bridge/issues/6575) showed local ACTIVE but source_authority_verified=false, no legitimate own claim/open. Original canonical dispatch request research-onhour-20261027-0507-dispatch-r13 (https://github.com/awdawmip/kimi-query-bridge/issues/6576) ended FAILED/TimeoutExpired; it was not replayed. The attempted new read-only exact continuation during this turn returned CONTROL_QUOTA, not an authenticated Source packet. The neutral original staging disposition SD-d7c23e7984c2ddaac60a remains independent. Own authenticated Source session/CLAIM/run: NOT VERIFIED. No fresh dispatch/claim/open, Source-native checkpoint, accepted Result, review or native experiment is asserted. Same Research logical lane identity maintained and unrelated CONTROL_PLANE_MAINTENANCE lane untouched.

Next Research turn: reconcile only actual unresolved original request IDs, read canonical Source continuation when available and verify legal ownership before new claim; hand native target and this concrete sign/basis negative control to the existing authorized owner. Portable mathematics can proceed within actual authorization but must not be reported as H0/B0 completion. No scheduler, Actions, native source pin, P000, or notification settings were changed.
