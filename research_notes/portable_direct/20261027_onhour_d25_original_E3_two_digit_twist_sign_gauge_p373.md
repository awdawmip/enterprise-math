# D25 original E3: the sign-root gauge and exact two-digit p=373 comparison

Date: 2026-10-27. Research logical lane: chatgpt-research-onhour-enterprise-math-20260923, distinct from CONTROL_PLANE_MAINTENANCE. Mother Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).

**AUTHOR-SIDE EXACT ALGEBRA / EXECUTED FINITE CERTIFICATE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NOT_NATIVE_H0B0 / NOT_SOURCE_CHECKPOINT / NOT_LIFT_PROOF.**

## Precise question and consumed prior work

The previous original-family 3-isogeny comparison to Babei–Roy–Swisher–Tobin–Tu, arXiv:2408.08844v3 (2025), Appendix Proposition 7.1, found target maps differing by negation when the *same* square root u of -3 was fixed. That result did not yet identify the simultaneous choice of u and target sign as a gauge equivalence, nor supply the original signed matrices modulo 373 squared. Resolve those two otherwise ambiguous native comparison inputs now, without replacing the original H0/B0 object.

Consume, do not recredit or recompute as newly discovered: research_notes/portable_direct/20261027_onhour_d25_2025_E3_isogeny_published_sign_alignment.md, immutable project commit ddeacffead4c17e5677e012cd275a0b409514eec. Work on the unmodified original E_t: y²+xy+(t/27)y=x³, t=(2-s)/4, s²=2. The established Vélu quotient uses coordinates U,V and published translated coordinate X=U+1/3, target x^sigma=-X/3. The source differential basis is (omega,eta=x omega), with dU/(2V)=omega and U omega cohomologous to 3 eta.

## New exact sign-root gauge theorem

Let 3 be invertible, let u²=-3, and let epsilon in {+1,-1} denote the selected target twist coordinate

    v^sigma = epsilon V/(3u).

Define the actual observable sign-root parameter alpha=epsilon*u. Since 1/u=-u/3,

    v^sigma=-alpha V/9, alpha²=-3.

Consequently the two labeled choices (u,epsilon) and (-u,-epsilon) induce exactly the SAME rational target map and the SAME full de Rham transport. The four apparent (square-root,label) combinations represent only two maps distinguished by alpha in {u,-u}. Explicitly,

    M3(alpha)=[[-alpha,alpha/9],[0,alpha]],
    det M3(alpha)=3, M3(alpha)^2=-3 I.

Here columns are the pullbacks of (omega^sigma,eta^sigma) in the original ordered basis (omega,eta). Keeping u fixed, epsilon->-epsilon DOES give the distinct negation map; allowing u to flip at the same time does not. Thus labels 'paper positive' and 'author negative' are only comparative once a COMMON root orientation is fixed; they are not independent intrinsic binary identifiers. This is a provenance/observer correction, not a claim that the 2025 article is wrong.

Consuming the already-established original degree-2 isogeny (do not newly claim it), its signed composite CM matrix can be written without epsilon:

    Mtheta(alpha)=[[s*alpha,alpha*(1-2s)/18],[0,-s*alpha]],
    Mtheta(alpha)^2=-6 I.

The map alpha->-alpha negates BOTH full matrices, hence changes signed eigenvalue labels but not their squared operators or eigenspaces. A quotient retaining only alpha², determinant, norm, or Frobenius square is NOT sufficient for a future signed first-column/second-column comparison. The smallest adequate observer here is the actual alpha (plus source/target coordinate provenance), not a free epsilon label.

## Exact p=373, modulo 139129 certificate

Let p=373, q=p²=139129 and R=(Z/qZ)[T]/(T²-2), with sigma(T)=-T. The residue u0=177 obeys u0²=-3 mod p. Its unique Hensel lift congruent to 177 is

    (177²+3)/373=84,
    k=-84*(2*177)^(-1) mod373=240,
    u=177+373*k=89697 mod139129,
    u²+3=0 mod139129.

The opposite root is -u=49432. In the alpha=89697 branch,

    M3=[[49432,102719],[0,89697]],
    Mtheta=[[89697*T,120924+36410*T],[0,49432*T]]  (mod139129).

In the alpha=49432 branch,

    M3=[[89697,36410],[0,49432]],
    Mtheta=[[49432*T,18205+102719*T],[0,89697*T]] (mod139129).

All four displayed matrices satisfy the exact degree/square checks; M3²=139126 I (-3), Mtheta²=139123 I (-6). The target-coordinate coefficient -alpha/9 equals 36410 for alpha=89697 and 102719 for alpha=49432. In particular

    (epsilon=+1,u=89697) = (epsilon=-1,u=49432)

as the ENTIRE 3-isogeny map, not merely its squared or norm observer. Reducing the two M3 branches modulo p recovers the earlier (paper-fixed-root,author-fixed-root) matrices [[196,144],[0,177]] and [[177,229],[0,196]], respectively.

## Reproducible exact standard-library checker

~~~python
p=373; q=p*p; u0=177
inv=lambda x: pow(x,-1,q)
assert (u0*u0+3)%p==0
k=(-((u0*u0+3)//p)*pow(2*u0,-1,p))%p
u=(u0+p*k)%q
assert k==240 and u==89697 and (u*u+3)%q==0
def mat3(alpha):
    return ((-alpha)%q,(alpha*inv(9))%q,0,alpha%q)
def v_twist(eps,r):
    return eps*inv(3*r)%q
assert v_twist(+1,u)==v_twist(-1,(-u)%q)==36410
assert v_twist(-1,u)==v_twist(+1,(-u)%q)==102719
pairmul=lambda x,y: ((x[0]*y[0]+2*x[1]*y[1])%q,
                      (x[0]*y[1]+x[1]*y[0])%q)
def theta(alpha):
    return ((0,alpha%q),
            (alpha*inv(18)%q,(-alpha*inv(9))%q),
            (0,(-alpha)%q))
for alpha,expectedM3,expectedTheta in [
  (89697,(49432,102719,0,89697),((0,89697),(120924,36410),(0,49432))),
  (49432,(89697,36410,0,49432),((0,49432),(18205,102719),(0,89697))) ]:
    m=mat3(alpha); a,b,_,d=m
    assert m==expectedM3
    assert a*d%q==3 and a*a%q==q-3 and d*d%q==q-3
    assert (a*b+b*d)%q==0
    t=theta(alpha)
    assert t==expectedTheta
    assert pairmul(t[0],t[0])==(q-6,0)
    assert tuple((x+y)%q for x,y in zip(pairmul(t[0],t[1]),pairmul(t[1],t[2])))==(0,0)
    assert pairmul(t[2],t[2])==(q-6,0)
assert mat3(u)==mat3((-(q-u))%q)
print("D25_E3_SIGN_ROOT_GAUGE_TWO_DIGIT_PASS",p,q,k,u)
~~~

Executed exact Python integer checks: **PASS** (both alpha branches, matrix products and coefficient ring). No floating-point or untested native code is involved. Full rational-family comparison and char-0 cohomological reduction are consumed from the prior evidence, not separately certified by this small modulo-q script.

## Research meaning, source separation, next exact action

BRC usage: COMPOSE_APPLIED to the (root u, target sign epsilon, original source/target coordinates, omega/eta columns) carrier. Exact fiber constancy under simultaneous (u,epsilon)->(-u,-epsilon) licenses compressing to alpha; the coarser alpha² fiber is NOT constant for signed M3 or Mtheta. The operation and observer are stated, unlike an unjustified sign erasure. This is algebra on an external original elliptic curve, not an automatic native X6 or H0/B0 bridge.

The mother D25/JT2 remains OPEN and the same-original-class native divided-power benchmark remains NOT_EXECUTED / PENDING_OWNER at #1559. Actual native [X]U mod139129, rank, eta/Frobenius direction and normalization, odd signed Green/Hesse and original kappa/Delta-R are NOT supplied here. The native owner must pin an actual alpha in Z/139129 together with the rational comparison map and both de Rham columns **only if** its H0/B0-to-E3 comparison is proven, then execute and return original raw data. Native H0/B0 cannot be inferred from these M3 matrices. Published arXiv 2408.08844 equation (6.8) retains only conjectural p³ strength; LIFT is not proved.

Research recovery evidence: own #6575 recovery reported no valid claim/run, #6576 dispatch FAILED/TimeoutExpired; latest Site gateway current source continuation read returned CONTROL_QUOTA, and the gateway's read-only Site identity reports no native Researcher write authority. These are control/source-access facts, not a scientific failure. Do not reissue those mutations or use the maintenance conversation identity. This GitHub note is AUTHOR-SIDE only; pending native publication, review and registration must remain separate. Current Source authority/head, frozen scientific pin and existing schedule must not be modified.