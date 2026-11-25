# R284IE — Rational-level inverse threshold and integer resonance

2026-11-26. Author proof and exact symbolic certificates, NOT_REVIEWED. Auxiliary binary-tag safe-word total-count observer K only; no native physical attribution. Frozen ID @ 000fb8cf43bf42509bcb2b90e65fdbb5edc95ca8:research_notes/portable_direct/R284ID_TAIL_BLOCK_FINITE_COMPLEMENT_CLOSURE_20261126.md (assembled all-integer monotonicity); HW @ 8c3bad026fc69c3a685218fc4677433a48310256:research_notes/portable_direct/R284HW_UNIFORM_WEDGE_RESIDUAL_PAYMENT_20261125.md (baseline and explicit residual); HH @ f9b8351559e49b13fbe70faad67d87e1b84fa9b9 and HE @ 0e4f8d4318f145100959ca9ec3f41c0e219090d5 (prior level-1 classification), GT @ c751b59823c79aac4b071d7b4b69e13ca830a7a (labeled cycle ratio K^2). IB and HY frozen analytic dependencies of ID were read; not a complete independent review. Current canonical global entries at dd16450e316d67e5d91fa0fc4d98b40002460418 matched actual blobs; P000 V5, ACTIVE worldview, joint preservation, Heartbeat and current portable/method/BRC/residual instructions read. Own RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E: recovery_status r1-20261126-0458-own-recovery verified open own session and registration receipt r1-20261124-0256-r284gd-session-v1 SUCCEEDED, no run; metadata only. Current LEASED inventory r1-20261126-0457-owner-read SUCCEEDED, as_of 2026-11-25T20:58:12.461046Z, Source 6ef4949f9a48d3349766b474b5cef8105a6aafd4, zero returned tasks. No shared CLAIM, no formal Result or Review write.

## Theorem
For every fixed positive rational level c, put
P_c(q)=c q^2/36+(8c/27+17/6)q+(128c^2-1431c-45360)/(162c),
T_c=2(68c^2+6991c+81180)/(3c^2)>0.
For all sufficiently large integer q (onset depending on c),
K(q,floor(P_c(q)))<c<K(q,floor(P_c(q))+1).
Consequently, **conditional on ID's assembled author theorem**, the minimum integer reading budget u>q giving K(q,u)>c is floor(P_c(q))+1, with no equality at that level for any valid u at these q. The adjacent bracket itself only needs HW. This is new for arbitrary rational levels, not a reproof of HH at c=1. The rational baseline's local real root is P_c(q)+T_c/q+O_c(q^-2). No continuous extension of the original combinatorial count is asserted. In the original labeled-cycle observer the corresponding ratio threshold is c^2.

For c=9/2, P=q^2/8+25q/6-135/2 and T=101348/27. P is integral exactly at q=6,18 mod 24. The integer formula above is valid for every q>=100000, using the explicit coefficient certificate below. This includes resonance, where the positive T correction, not rounding a leading approximation, determines the correct integer. No universal finite onset for arbitrary c or sharp onset for 9/2 asserted.

## Proof
Use HW's same signed baseline:
S=4u+2q+4; j=u+2q+1; d=u-q;
f(S,g)=[4(g+2)^2-S]/[S(S-1)];
Q0=f(S,d-1), V0=j/(S-j+1) f(S,d),
A0=[j(j-1)f(S-2,d)+j(S-j)f(S-2,d-1)]/[S(S-1)].
K0=A0 Q0 (3u+q+1)^2/[(Q0+V0+q A0)^2(u+2q+1)].
HW gives, for u>=640,u>=2q+10, (1+delta)^-2<=K/K0<=(1+2delta)(1+delta), delta=200 exp(-(u-1)/36). Thus K0 remains a paid observer; E and all signed omitted mass are not declared zero.

Let K0=N/D in the exact factored form computed in the replay (D is a polynomial square, positive on the wedge since the signed normalized Q0,V0,A0 are positive). N has total degree 9 and D degree 10; F=N-cD has weighted degree 18 for weight(u)=2,weight(q)=1. Substitute u=c q^2/36+a q+b+t/q. Coefficient of q^18 vanishes. Coefficient of q^17 is c^8(54a-16c-153)/117546246144, so a=8c/27+17/6. Coefficient of q^16 after this choice is c^8(b-b_c)/2176782336, b_c=(128c^2-1431c-45360)/(162c). Coefficient of q^15 after both choices is c^8(t-T_c)/2176782336. These identities follow by multinomial expansion, exact symbolic replay below. D's highest weighted term is 36u^8 q^2, hence the leading coefficient on the substituted curve is c^8/36^7>0.

In particular at u=P_c+s with bounded s,
K0-c=36s/q^2+O_c(q^-3);
at s=0, K0-c=-36T_c/q^3+O_c(q^-4).
For fixed c and bounded t, at u=P_c+t/q the difference is 36(t-T_c)/q^3+O_c(q^-4). The local real-root expansion follows by the implicit function theorem after scaling u/q^2, since the rescaled limiting K0 is 36u/q^2 and has nonzero derivative; equivalently solve the analytic rational equation in 1/q near u/q^2=c/36. All estimates uniform on bounded s or t. At these points u~c q^2/36 so HW's residual is smaller than every inverse power of q.

Because c is rational, the coefficients of P_c have a fixed common integer denominator H_c. At floor(P_c), s is either zero or <=-1/H_c. At floor(P_c)+1, s>=1/H_c. For nonzero s, the q^-2 term dominates the q^-3 error; at s=0 the strictly positive T_c makes the q^-3 term negative. Transfer the strict signs using HW's paid bound, which is exponentially smaller even at resonance. This proves the bracket. Invoke ID only to extend the two signs to all earlier/later budgets at the same q. For c=1 the polynomial P agrees with the inverse of HE's eventual floor transition; no claim of a new sharp level-1 onset.

## Explicit effective certificate at c=9/2
For q modulo 24, s=floor(P)-P belongs to {-5/6,-19/24,-2/3,-1/2,-11/24,-1/3,-1/6,-1/8,0}. For each of these nine s, put A=N(P+s,q), B=D(P+s,q), and for the upper endpoint use P+s+1. Check the polynomials sign*q^3*(A-cB)-B at the lower endpoint (sign=-1) and upper endpoint (sign=+1), substituting q=100000+x. All 359 coefficients (including the constant terms) are nonnegative and each constant is strictly positive; exact replay below. Thus each signed baseline gap exceeds 1/q^3, including the two integral residue classes.

Both endpoint budgets U>=q^2/8 for q>=100000 and U>=2q+10. Therefore (U-1)/36>=q^2/300. Using exp(x)>=x^3/6 gives delta<=1200*300^3/q^6<1/(1000q^3). Then (1+2delta)(1+delta)<=1+4delta, (1+delta)^2<=1+3delta, and c*4delta<1/q^3. The strict sign of the true K at each endpoint follows from the HW sandwich. Together with the author monotonicity this proves the exact inverse threshold at level 9/2 for every integer q>=100000.

## Exact replay
Python/SymPy and Fraction. The coefficient-extraction function computes the actual Laurent coefficient without expanding all low-order terms. This compact replay expresses the calculations executed in /tmp/level.py and /tmp/reson.py; no full exact count at the huge budgets is claimed. For the paid numerical samples use a conservative common delta=2^-200 valid for U>=8000 because 200*2^-floor((U-1)/36)<2^-200. A first check at q=10^6 for c=1/16 did not establish the predicted upper sign: this is outside the unspecified eventual range, and is not counted as success. Increasing q to 10^10 yielded all asserted paid signs.

```python
import sympy as s
from fractions import Fraction as R
from math import lcm,isqrt
u,q,c,a,b,t=s.symbols('u q c a b t')
S=4*u+2*q+4;j=u+2*q+1;d=u-q
f=lambda S,g:(4*(g+2)**2-S)/(S*(S-1))
Q=f(S,d-1);V=j/(S-j+1)*f(S,d)
A=j*(j-1)/(S*(S-1))*f(S-2,d)+j*(S-j)/(S*(S-1))*f(S-2,d-1)
N,D=s.fraction(s.factor(A*Q*(3*u+q+1)**2/((Q+V+q*A)**2*(u+2*q+1))))
P=s.Poly(N-c*D,u,q)
def coef(deg):
    z=0
    for (i,j),v in P.terms():
        need=2*i+j-deg
        if need<0:continue
        for ib in range(min(i,need//2)+1):
            for it in range(min(i-ib,need//3)+1):
                ia=need-2*ib-3*it;ic=i-ia-ib-it
                if ia<0 or ic<0:continue
                z+=v*s.factorial(i)/s.prod(s.factorial(k) for k in [ia,ib,it,ic])*(c/36)**ic*a**ia*b**ib*t**it
    return s.factor(z)
assert coef(18)==0
ar=s.solve(coef(17),a)[0]
br=s.factor(s.solve(coef(16).subs(a,ar),b)[0])
tr=s.factor(s.solve(coef(15).subs({a:ar,b:br}),t)[0])
print(ar,br,tr)
p=lambda c,q:c*q*q/36+(8*c/27+R(17,6))*q+(128*c*c-1431*c-45360)/(162*c)
kn=s.lambdify((u,q),N,'math');kd=s.lambdify((u,q),D,'math')
checks=reson=0
for C in map(R,['1/16','1/4','1/2','1','2','3','4','9/2','9','16','36']):
    den=lcm((C/36).denominator,(8*C/27+R(17,6)).denominator,((128*C*C-1431*C-45360)/(162*C)).denominator)
    res=[k for k in range(den) if p(C,k).denominator==1]
    qs={10**10,10**10+1}
    qs.update(10**10-10**10%den+k for k in res[:2])
    for qq in sorted(qs):
        pp=p(C,qq);U=pp.numerator//pp.denominator;reson+=pp.denominator==1
        for Uu,sign in [(U,-1),(U+1,1)]:
            assert Uu>=8000 and Uu>=2*qq+10
            k=R(kn(Uu,qq),kd(Uu,qq));delta=R(1,2**200)
            assert k*(1+2*delta)*(1+delta)<C if sign<0 else k/(1+delta)**2>C
            checks+=1
print('paid signs',checks,'resonance rows',reson)
cc=s.Rational(9,2);p9=q*q/8+25*q/6-s.Rational(135,2)
ss=sorted({-(p9.subs(q,i)%1) for i in range(24)})
print('offsets',ss)
polys=[]
for z in ss:
    for offset,sign in [(z,-1),(z+1,1)]:
        A=s.Poly(N.subs(u,p9+offset),q);B=s.Poly(D.subs(u,p9+offset),q)
        poly=s.Poly(sign*q**3*(A-cc*B)-B,q)
        assert poly.LC()>0
        polys.append(poly.shift(100000))
assert all(all(v>=0 for v in poly.all_coeffs()) and poly.TC()>0 for poly in polys)
print('coefficients',sum(len(v.all_coeffs()) for v in polys))
print('ID coverage counts',[sum(min((u+9)//2,isqrt(441*u-1))-256 for u in range(L,U+1)) for L,U in [(1201,2400),(2401,3600),(3601,4800),(4801,6000),(6001,7299)]])
```

Actual executed outputs (equivalent split scripts):
- a=8*c/27+17/6; b=(128*c**2-1431*c-45360)/(162*c); t=2*(68*c**2+6991*c+81180)/(3*c**2).
- paid signs 48, resonance rows 2, all passed; 11 rational levels as listed.
- c=9/2 denominator 24, integral residues [6,18]; 9 offsets; q shift 100000, bad 0, count 359.
- ID independent coverage recount [721785,1070254,1324037,1543142,1890444], matches ID; coverage arithmetic alone, not rerunning its interval certificate or reviewing all analytic proofs.

## Next
Develop a uniform effective bound in the numerator and denominator of c using the coefficient/residue certificate, or sharpen the level-9/2 onset. The ID author proof's independent review remains an outstanding separate task. No native dynamical implication or canonical acceptance asserted.
