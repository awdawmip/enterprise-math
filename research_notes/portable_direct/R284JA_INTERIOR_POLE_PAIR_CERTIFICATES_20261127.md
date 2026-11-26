# R284JA — Two interior-pole certificates and coupled exterior double pole
2026-11-27. Author proof and executed exact finite checks; NOT_REVIEWED. Auxiliary binary-tag joint-count observer only. Frozen predecessor R284IZ at c9d5457abea78a3b69ecae364ca71e9a6a80cd57:research_notes/portable_direct/R284IZ_JOINT_DENOMINATOR_CARRY_COMPRESSION_20261127.md (blob 8d33e4d9f86e1c766eacccc76d60518fcde6f112). Own existing RA-B82240E8488EF5A1DA5186C4, own session recovery metadata verified. Owner inventory r1-20261127-0257-owner still RUNNING at preparation; independent portable continuation, no shared claim or owner mutation. P000 V5, ACTIVE worldview, joint observer preservation and current portable rules consulted.

## 1. Setting
Integers q>=64, 2<=d<=2sqrt(q). u=q+d, m=2q+d, l=d-k. R_n(j)=product_{i=0}^{j-1}(n-i)/(n+i+3). w0=(k+1)(l+1)R_u(k)R_m(l); w1=(k+1)l R_u(k)R_m(l-1) for l>=1, zero otherwise. v=(u-k)(u+k+2)/(2u(2u+1)).
V=sum w0, Q=sum w1, A=sum v(w0+w1),
E=R_u(d)(u-d)[(d+1)(u+d+2)+(d+2)(u-1-d)](m+2)/[2u(2u+1)(4m+2)].
W=A+E, Z=qA+Q+V, Y=q(4q+3d+1)^2 WQ/[(3q+d+1)Z^2], F=Y-32/3. All four observers and exterior factors retained. Positivity of the actual real Z follows from IZ.

## 2. Second-branch penultimate denominator: exact double-pole theorem
Set N=2q+2d+1=m+d+1=2u+1. If prime p|N and p>4d+3, t=v_p(N), then
v_p(A)=v_p(W)=v_p(Z)=-2t, v_p(Q)=-t, v_p(Y)=t, v_p(F)=0.
Proof: at the formal residue N=0, q=-(2d+1)/2, u=-1/2, m=-d-1. Among all raw R denominators the unique possible p-divisible factor is m+d+1 at i=d-2; all numerators are p-units (multiply half-integers by 2 to inspect them). All other relevant factors have nonzero residue with absolute numerator at most 4d+3, including the prefactors q, 4q+3d+1, 3q+d+1, 2u, 4m+2. Let T=R_m(d-1), with v_p(T)=-t. Only k=0,1 in the full fiber and k=0 in the shifted fiber have this pole. The exterior factor 2u+1=N creates an additional pole in v; E has at most one pole since R_u(d) is a unit. Ratios of the pole branch factors to T are units and regular at N=0. R_m(d)/T=-2d, R_u(1)=-1/5 at this coordinate. Thus the two full weights divided by T reduce to -2d(d+1) and -2d/5, while the shifted weight reduces to d. All other weights divided by T vanish modulo p. Nv at k=0,1 reduces respectively to 3/4 and 15/4. Consequently
NA/T = (3/4)[-2d(d+1)+d]+(15/4)(-2d/5) = -3d(2d+3)/4 mod p,
NZ/T = 3d(2d+3)(2d+1)/8 mod p.
Both are units under p>4d+3. Also Q/T=d mod p, NE/T=0 mod p. This proves the stated valuations; inserting them in the full Y ratio gives -2t-t+4t=t. Since 32/3 is a p-unit, v_p(F)=0. The two poles are jointly coupled by the exact identity N=m+d+1=2u+1. Retaining just the maximum unweighted product exponent would miss the extra exterior pole.

## 3. First-branch penultimate denominator: explicit polynomial criterion, including cancellation
Set M=q+2d+1=u+d+1. Suppose prime p|M and p>12d+14, t=v_p(M). At M=0 we have q=-2d-1,u=-d-1,m=-3d-2. All raw factors except u+d+1 are units (inspect these residues; the largest exterior magnitude is 12d+6). Set T=R_u(d-1), v_p(T)=-t. Only k=d-1,d in the full fiber and k=d-1 in the shifted fiber have the pole. At the formal residue R_u(d)/T=-2d, R_m(1)=(3d+2)/(3d-1), v(d-1)=0, v(d)=-1/[2(d+1)]. Substituting the actual E formula as well gives the following regular ratios modulo p:
V/T=-2d(3d^2-d-3)/(3d-1), Q/T=d, A/T=d,
E/T=-d^2(2d+3)/[2(2d+1)],
W/T=-d(2d^2-d-2)/[2(2d+1)],
Z/T=-2d(6d^2-2d-3)/(3d-1).
These expressions mean reduction of the ratios, not replacement of the true observers away from M=0.
Define the integer cross-multiplied residual before common-denominator clearing,
C=3q(4q+3d+1)^2 WQ-32(3q+d+1)Z^2 (a rational number).
Direct expansion of the regular residue gives
C/T^2 = d^2 P(d)/[2(3d-1)^2] mod p,
P(d)=1350d^6+46125d^5-14442d^4-53890d^3-454d^2+17781d+4554.
Hence if p does not divide P(d), C is nonzero and F is nonzero, even if Z/T vanishes. Conversely p|P(d) is necessary for equality under this coordinate; it is not sufficient. The polynomial is strictly positive for d>=2: coefficients in x=d-2 are 1350,62325,527808,1891574,3343598,2856341,938508 in descending order. Consequently at most O(1) distinct p>12d+14 can divide P(d), by P(d)=O(d^6). When Z/T vanishes and W/T does not, the real rational Y has negative p-valuation (exactly -2 v_p(Z/T)), providing another certificate. Do not assume a nonzero Z residue when using C. This is a genuine two-pole-fiber cancellation test, rather than separate product maxima.

## 4. Density of the two new certificate events
Let d(q) be an integer eventually nondecreasing with d(q)=s sqrt(q)+O(1), fixed 0<s<2. The event P^+(N)>4d(q)+3 has natural density log 2 in q; the event that there exists p|M, p>12d(q)+14 with p not dividing P(d(q)) also has density log 2. Here P^+ is the largest prime factor, and the events refer to certificates, not actual equality frequencies.
Proof: the strictly increasing maps q -> q+d(q) and q -> q+2d(q)+1 omit at most O(sqrt X) integer indices up to their respective endpoints X+O(sqrt X). Therefore the first event transfers to odd integers N up to 2X+O(sqrt X), the second to ordinary integers M up to X+O(sqrt X). On q in [epsilon X,X] either threshold lies between positive constants times sqrt X. For ordinary integers up to cX, the count with largest prime factor >C sqrt X is cX log 2+o(X) for any fixed c,C>0: primes >sqrt(cX) cannot occur twice as factors of a given integer, so sum floor(cX/p), with total rounding error O(pi(cX))=o(X) and reciprocal-prime sum log 2+o(1) by Mertens' prime reciprocal theorem. Replacing sqrt(cX) by C sqrt X changes at most sum floor(cX/p) over a constant-factor sqrt X interval, which is o(X) by the same theorem. On odd integers the corresponding count is cX log 2/2+o(X), by counting odd multiples of each odd prime instead (error O(1) per prime). Apply the threshold squeeze, discard q<epsilon X, then let epsilon tend to zero. For the second certificate discard the exceptional p|P(d): for fixed d there are O(1) eligible primes, and all q having this d lie in an interval of length O(d) by inversion of |d-s sqrt q|<=constant. Each such prime >12d+14 divides M=q+2d+1 at most O(1) times within the interval. Summing over d=O(sqrt X) gives O(sqrt X) discarded q. No independence of the five coordinate events is asserted. Both new families thus give unbounded positive-density certificate resources, but a union density improvement requires additional correlation information.

## 5. Executed exact checks
Python Fraction, all integers 2<=d<=30; primes p<700. Second-branch test p>4d+3, N in {p,3p,p^2}; first-branch test p>12d+14, M in {p,2p,p^2}; retain q>=64,d^2<=4q. 8255 second-branch cases (5171 with t=1,3084 with t=2), 6950 first-branch cases. All residue and valuation assertions passed. First-branch P-divisibility exceptions: seven (d,p) pairs (2,197),(2,397),(4,379),(7,223),(13,373),(22,647),(29,541); 21 actual q cases, all F nonzero in these finite tests, with v_p(F)=1 except (d,p,q)=(13,373,719), v_p(F)=2. Z-leading cancellation pairs (5,137),(7,277),(10,577),(13,197),(14,229),(15,439),(30,593); 21 actual cases, v_p(Y)=-2 for all. These are observations, not a universal higher-order classification.
Reproduction script (executed):
```python
from fractions import Fraction as F
from math import isqrt
from sympy import primerange

def obs(q,d):
    u,m=q+d,2*q+d
    def rr(n):
        r=[F(1)]
        for i in range(d): r.append(r[-1]*F(n-i,n+i+3))
        return r
    r,s=rr(u),rr(m)
    V=Q=A=F(0)
    for k in range(d+1):
        l=d-k
        a=(k+1)*(l+1)*r[k]*s[l]
        b=(k+1)*l*r[k]*s[l-1] if l else F(0)
        v=F((u-k)*(u+k+2),2*u*(2*u+1))
        V+=a;Q+=b;A+=v*(a+b)
    E=r[d]*F((u-d)*((d+1)*(u+d+2)+(d+2)*(u-1-d))*(m+2),2*u*(2*u+1)*(4*m+2))
    Z=q*A+Q+V
    Y=q*(4*q+3*d+1)**2*(A+E)*Q/((3*q+d+1)*Z**2)
    return V,Q,A,E,Z,Y,r[d-1],s[d-1]
def vp(x,p):
    if not x:return float('inf')
    a,b=x.numerator,x.denominator;z=0
    while a%p==0:a//=p;z+=1
    while b%p==0:b//=p;z-=1
    return z
def mod(x,p):
    x=F(x);return x.numerator*pow(x.denominator,-1,p)%p
def poly(d):return 1350*d**6+46125*d**5-14442*d**4-53890*d**3-454*d**2+17781*d+4554

def check():
    counts=[0,0]; exceptions=[];zexception=[]; ts={}
    for d in range(2,31):
        for p in primerange(4*d+4,700):
            for N in (p,3*p,p*p):
                q=(N-2*d-1)//2
                if q<64 or d*d>4*q:continue
                V,Q,A,E,Z,Y,ru,T=obs(q,d);t=vp(F(N),p)
                assert vp(T,p)==-t and vp(V,p)>=-t and vp(Q,p)==-t and vp(E,p)>=-t
                assert mod(N*A/T,p)==mod(F(-3*d*(2*d+3),4),p)
                assert mod(N*Z/T,p)==mod(F(3*d*(2*d+3)*(2*d+1),8),p)
                assert vp(A,p)==vp(Z,p)==vp(A+E,p)==-2*t
                assert vp(Y,p)==t and vp(Y-F(32,3),p)==0
                counts[0]+=1;ts[t]=ts.get(t,0)+1
            if p<=12*d+14:continue
            for N in (p,2*p,p*p):
                q=N-2*d-1
                if q<64 or d*d>4*q:continue
                V,Q,A,E,Z,Y,T,rm=obs(q,d);t=vp(F(N),p)
                assert vp(T,p)==-t
                v=F(-2*d*(3*d*d-d-3),3*d-1);w=F(-d*(2*d*d-d-2),2*(2*d+1));z=F(-2*d*(6*d*d-2*d-3),3*d-1)
                assert [mod(a/T,p) for a in (V,Q,A,A+E,Z)]==[mod(a,p) for a in (v,d,d,w,z)]
                c=3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*Z*Z
                assert (mod(c/(T*T),p)==0)==(poly(d)%p==0)
                if poly(d)%p:assert Y!=F(32,3)
                else:exceptions.append((d,p,q,vp(Y-F(32,3),p)))
                if z.numerator%p==0:zexception.append((d,p,q,vp(Y,p)))
                counts[1]+=1
    print('counts',counts,'second t',ts,'P exceptions',exceptions,'Z exceptions',zexception)
if __name__=='__main__':check()
```

Next: extend the two-fiber calculation to a general interior pole offset r=d-j, keeping the exterior factor and the full C/T^2 residue. Classify when the polynomial exceptions lift to higher orders, and combine with IZ carry witnesses. The first-order calculation has constant-size algebra for these two fixed offsets; discovery of a suitable prime/factorization is not claimed polynomial-time. Full equality exclusion, joint coverage beyond log 2, real inverse-polynomial separation, and general aggregate valuation remain open. No independent review or formal task completion asserted.
