# R284IS — Polynomial fiber summation for certified critical-sign evaluation
2026-11-26. Author analytic proof and executed exact rational computation; NOT_REVIEWED. Directed continuation of R284 on own Activity RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E. Own original session registration recovered SUCCEEDED, no shared run. Current owner inventory r1-20261126-1856-owner-inventory last observed RUNNING; no shared task claim or mutation. Account main entry snapshot a0d14a8795c0574f20c85d85393232a12fd76190. P000 V4 projection blob verified against canonical; Source V5 foundation and ACTIVE worldview consulted. Auxiliary binary-tag safe-word counting observer; no native spatial attribution.
Frozen science: II@c7be4488d3caa0ff3fa0a2febac189f084982516 and IJ@75426bd0581d1826bfde31ac82cb5a632f53cc51 (exact branch law and ID monotonicity dependency), IR@586bdd64a16a0ac082c9c16eb3895a18f4c14d6c (current frontier), IO@b6d9d4c99b9fcba85c5fca2e9eb83fe763d276cf (root enclosure used only to propose candidate integers). No repeat of earlier full historical enumerations.

## Result
For integer q>=64, 0<=d<=2 sqrt(q), and integer p>=1, the full original qK (including E) can be enclosed in an exact rational interval of width O(2^-p), uniformly in q,d, for all p above a fixed absolute constant, by a number of bit operations polynomial in p+log q. This is an alternative to explicit asymptotic-remainder certification: no estimate for the omitted IJ fourth-order coefficient is needed to certify a strict sign. For a nonzero threshold gap |qK-32/3|>=q^-C, fixed C, the sign is thus decidable in polynomial(log q) bit complexity. No uniform gap bound or equality decision in polynomial time is asserted. For arbitrary gap use increasing precision and a finite full exact rational fallback if required.
Minimum-budget interpretation still depends on frozen ID author-level monotonicity; a strict two-point bracket itself is an independently exact statement for the original K.

## Proof: preserve the joint fiber, compress only the polynomial sum
Let u=q+d, m=u+q, l=d-k, and R_n(j)=prod_{i=0}^{j-1}(n-i)/(n+i+3). Denote w_k=R_u(k)R_m(l), v=(u-k)(u+k+2)/(2u(2u+1)), g=l(m+l+2)/(m-l+1). After removing the common positive H0 from II, V=sum w(k+1)(l+1), Q=sum w(k+1)g, A=sum w v(k+1)(l+1+g). E=(d+1)R_u(d)v(d)(1+r_b)gamma_m with r_b and gamma_m exactly as in II. Thus qK=(L/q)(A+E)Q/[A+(Q+V)/q]^2 with L=(3u+q+1)^2/(u+2q+1).
The positive branch w and exact endpoint E are retained; the signed operation is only polynomial summation, not positive mass cancellation. In particular no independent pointwise approximation of Q/V is imposed.

Write rho=(d+2)/u<1/2 and Lb=d(d+2)/(u(1-rho))<=9. For J>=1 let
P_n(j)=sum_{a=1}^J [-S_a(j)+(-1)^a(S_a(j+3)-S_a(3))]/(a n^a),
where S_a(j)=sum_{i=0}^{j-1} i^a. P(k)=P_u(k)+P_m(d-k) is a rational polynomial of degree at most J+1. Truncated log(1-x) is nonpositive and truncated log(1+y) nonnegative for 0<=x,y<=rho. Both have magnitudes bounded by x/(1-rho), y/(1-rho), respectively. Summing these bounds uses k(k+2)+l(l+2)<=d(d+2), hence -Lb<=P<=0. Taylor tails for both logarithms give
|log w_k-P(k)|<=4d rho^(J+1).
For even T define W(k)=sum_{i=0}^T P(k)^i/i!, a polynomial of degree <=(J+1)T. Taylor's real remainder on the nonpositive segment gives W>=exp(P)>0 and
|W-w|<=e0:=4d rho^(J+1)+Lb^(T+1)/(T+1)!.
The exponential is 1-Lipschitz on negative real inputs. These are exact error bounds, including k=0,d.

Approximate only the denominator of g by its positive geometric sum:
g0=l(m+l+2)/(m+1) sum_{j=0}^J (l/(m+1))^j.
Then 0<=g0<=g<=4l and 0<=g-g0<=4l rho^(J+1).
Put Z=sum (k+1)(l+1)=(d+1)(d+2)(d+3)/6. Use polynomial sums normalized by Z to approximate V,Q,A with W,g0, retaining v exactly. Since 0<v<=1, w<=1, the respective absolute errors are bounded by e0, 4(e0+rho^(J+1)), 5e0+4rho^(J+1). The exact E prefactor divided by Z is ef; approximate E by ef W(d), error <=ef e0. All four intervals can be intersected with nonnegative reals, then propagated by positive rational interval arithmetic through the exact qK formula. The lower endpoint of its denominator must be positive before division.
The normalized true V>=exp(-9)>2^-14, A>=V/8 (u-k>=4u/5 and denominator <=6u²); all normalized quantities are bounded by fixed constants (V<=1,Q<=4,A<=5,E<=3). Also L/q<=9. Consequently the positive rational expression has a uniform finite Lipschitz constant on an enlarged compact neighborhood with A bounded away from zero. Choosing J,T so each contribution to e0 is <=2^(-p-1) gives interval width O(2^-p) uniformly. For d=0 use exact Q=0, and the displayed code also handles it; rho^(J+1) need not be small there because g=0 exactly. For d>=1, rho^(J+1)<=2^(-p-1)/(4d); for d=0 set gerr=0. The proof of width includes this zero boundary.

## Exact summation and bit complexity
The four approximating carriers are polynomials (E is an endpoint evaluation); maximal degree D=(J+1)T+J+5, including v and g0. For any polynomial f of degree <=D,
sum_{k=0}^d f(k)=sum_{j=0}^D binom(d+1,j+1) Delta^j f(0).
This follows from Newton's binomial basis and the hockey-stick identity. Use min(d,D)+1 samples, summing directly when d<=D. No O(d) branch enumeration is required in the large-window case.
Use exact integer common denominators: log denominator J!(um)^J; W denominator den^T T!; g0 denominator (m+1)^(J+1); v denominator 2u(2u+1). Sample numerators, all finite differences, binomial weights and final rational interval operations are exact; cancellation in the polynomial basis is never evaluated by float arithmetic. Power sums follow S_0(k)=k and S_a(k)=[k^(a+1)-sum_{i<a} binom(a+1,i)S_i(k)]/(a+1), so no hidden O(d) cost. Since rho<=1/2 and Lb<=9, J=O(p+log q), T=O(p+1) and D polynomial in p+log q. All integer sizes are polynomial in these parameters (sample arguments <=d, denominators have O(J(log q+log J)) bits, powers and binomial weights multiply by polynomial degrees). Schoolbook arithmetic and finite differences therefore suffice for polynomial bit complexity; this includes normalization and output recovery. Precision doubling reaches any fixed inverse-polynomial gap with p=O(log q); exact full rational fallback guarantees termination for equality, with no polynomial guarantee in that case. Candidate generation can use ordinary search/monotonicity where available; no unproved rounding constant is used for the certificate.

## Executed evidence
Local Python integer/Fraction arithmetic. 24 exact inclusion checks against full rational branch enumeration for q=64,81,100,121,256,1024 and d in {0,1,sqrt(q),2sqrt(q)}. Six old strict brackets were independently verified by the compressed method at p=56:
q,d_lo,J,T,D,upper_lo_gap,lower_hi_gap
10234,100,9,20,214,-0.00025176452756131665,0.00290352624112174
264559,500,7,18,156,-1.9883146896127537e-06,0.00012469384386954924
1062628,1000,6,18,137,-2.444355465745728e-07,3.144457440030561e-05
9590049,3000,6,18,137,-9.027370027178893e-09,3.5133949453535065e-06
106658837,10000,5,18,118,-2.3981862739960353e-10,3.16823882563153e-07
400000000,19363,5,18,118,-5.875344770306687e-08,2.5813219128903914e-08
Five new budgets (decimal candidate generation only; strict signs certified with rational intervals):
q,d_lo,p,J,T,D,upper_lo_gap,lower_hi_gap,elapsed_seconds_for_pair
10^12,968083,74,4,22,119,-1.965390919800487e-11,1.417966152778515e-11,0.178
10^24,968081516891,114,3,30,128,-5.29524698299338e-24,2.853846882694241e-23,0.142
10^36,968081516889092507,154,3,38,160,-3.0560166302337925e-35,3.273549525063728e-36,0.434
10^48,968081516889092505839245,194,3,46,192,-2.8578393818595457e-47,5.2553220128891347e-48,1.079
10^60,968081516889092505839243780671,234,3,52,216,-3.216373503441562e-59,1.6699807890278032e-60,2.205
For the largest case, 217 polynomial samples for lower d, instead of approximately 9.68*10^29 terms; timing is observed for this implementation only, not a speedup ratio. Decimal displays of margins are not used for decisions. Both signs for every pair were asserted exactly against Fraction(32,3).
The original executed routine below had gerr=rho**(J+1) also at d=0; this is safe but its width does not shrink with p if J fixed at 1. The single zero-case correction gerr=0 if d==0 (g is identically zero) is given below; it does not change any d>0 result. Recheck zero case and rerun full evidence if using the corrected routine.

## Reproduction (Python stdlib)
```python
from fractions import Fraction as F
from math import comb, factorial
from time import perf_counter

def power_sums(k,J):
    v=[k]
    for j in range(1,J+1):
        x=k**(j+1)-sum(comb(j+1,i)*v[i] for i in range(j))
        y,r=divmod(x,j+1); assert r==0
        v.append(y)
    return v

def sum_poly(vals,d):
    if len(vals)==d+1: return sum(vals)
    ans=0
    for j in range(len(vals)):
        ans+=comb(d+1,j+1)*vals[0]
        vals=[b-a for a,b in zip(vals,vals[1:])]
    return ans

def certify(q,d,p=48):
    assert q>=64 and 0<=d and d*d<=4*q
    u=q+d;m=u+q; rho=F(d+2,u); assert rho<F(1,2)
    eps=F(1,2**(p+1)); J=1
    while 4*d*rho**(J+1)>eps: J+=1
    L=F(d*(d+2),u)/(1-rho); T=0
    while L**(T+1)/factorial(T+1)>eps:T+=2
    err=4*d*rho**(J+1)+L**(T+1)/factorial(T+1)
    gerr=rho**(J+1) if d else F(0)
    den=factorial(J)*(u*m)**J
    U=[den//(j*u**j) for j in range(1,J+1)]
    M=[den//(j*m**j) for j in range(1,J+1)]
    assert all(den%(j*n**j)==0 for n in (u,m) for j in range(1,J+1))
    S3=power_sums(3,J)
    def log_num(k,coeff):
        S=power_sums(k,J); Sp=power_sums(k+3,J)
        return sum(coeff[j-1]*(-S[j]+(-1)**j*(Sp[j]-S3[j])) for j in range(1,J+1))
    Wden=den**T*factorial(T)
    co=[den**(T-i)*(factorial(T)//factorial(i)) for i in range(T+1)]
    def Wnum(k):
        z=log_num(k,U)+log_num(d-k,M)
        assert -L*den<=z<=0
        v=co[-1]
        for c in reversed(co[:-1]):v=v*z+c
        assert v>=0
        return v
    Gden=(m+1)**(J+1); Vden=2*u*(2*u+1)
    D=(J+1)*T+J+5
    vs=[]; qs=[]; aa=[]
    for k in range(min(d,D)+1):
        l=d-k; w=Wnum(k)
        g=l*(m+l+2)*sum(l**j*(m+1)**(J-j) for j in range(J+1))
        v=(k+1)*(l+1); qq=(k+1)*g; vn=(u-k)*(u+k+2)
        vs.append(w*v);qs.append(w*qq);aa.append(w*vn*(v*Gden+qq))
    Z=(d+1)*(d+2)*(d+3)//6
    v=F(sum_poly(vs,d),Wden*Z)
    Q=F(sum_poly(qs,d),Wden*Gden*Z)
    a=F(sum_poly(aa,d),Wden*Gden*Vden*Z)
    ef=F((d+1)*(u-d)*(u+d+2),Vden)*(1+F((d+2)*(u-1-d),(d+1)*(u+d+2)))*F(m+2,4*m+2)/Z
    e=F(Wnum(d),Wden)*ef
    def iv(x,r):return max(F(0),x-r),x+r
    vl,vh=iv(v,err);ql,qh=iv(Q,4*(err+gerr));al,ah=iv(a,5*err+4*gerr);el,eh=iv(e,ef*err)
    factor=F((3*u+q+1)**2,q*(u+2*q+1))
    tl=al+(ql+vl)/q;th=ah+(qh+vh)/q
    if tl==0:return None,None,J,T,D
    return factor*(al+el)*ql/th**2,factor*(ah+eh)*qh/tl**2,J,T,D

def exact(q,d):
    u=q+d;m=u+q
    def weights(n):
        a=[F(1)]
        for i in range(d):a.append(a[-1]*F(n-i,n+i+3))
        return a
    P,R=weights(u),weights(m);V=Q=A=E=F(0)
    for k in range(d+1):
        l=d-k;w=(k+1)*(l+1)*P[k]*R[l];t=F(l*(m+l+2),(l+1)*(m-l+1));v=F((u-k)*(u+k+2),2*u*(2*u+1))
        V+=w;Q+=w*t;A+=w*v*(1+t)
        if l==0:E=w*v*(1+F((d+2)*(u-1-d),(d+1)*(u+d+2)))*F(m+2,4*m+2)
    return F((3*u+q+1)**2,q*(u+2*q+1))*(A+E)*Q/(A+(Q+V)/q)**2

if __name__=='__main__':
    n=0
    for q in [64,81,100,121,256,1024]:
        for d in sorted({0,1,int(q**.5),int(2*q**.5)}):
            a,b,*_=certify(q,d,24); v=exact(q,d); assert a<=v<=b; n+=1
    print('exact Fraction inclusion cases',n,flush=True)
    for q,d in [(10234,100),(264559,500),(1062628,1000),(9590049,3000),(106658837,10000),(400000000,19363)]:
        st=perf_counter(); a,b,j,t,D=certify(q,d,56); c,e,*_=certify(q,d+1,56)
        assert b<F(32,3)<c
        print(q,d,'J,T,D',j,t,D,'samples',min(d,D)+1,'upper lower margins',float(b-F(32,3)),float(c-F(32,3)), 'sec',round(perf_counter()-st,3),flush=True)
    from decimal import Decimal,getcontext
    getcontext().prec=60
    s=Decimal('0.937181823342286298624673426908455').sqrt()
    for k in [12,24,36,48,60]:
        q=10**k
        d=int(s*Decimal(q).sqrt()+Decimal('2.064002154731')+Decimal('8.26707233348')/Decimal(q).sqrt())
        p=int(k*3.322)+35
        st=perf_counter(); a,b,j,t,D=certify(q,d,p); c,e,*_=certify(q,d+1,p)
        assert b<F(32,3)<c
        print(k,d,p,j,t,D,float(b-F(32,3)),float(c-F(32,3)),round(perf_counter()-st,3))

```

## Next
1. Integrate exact sign oracle with local monotonicity/bracketing search; analyze typical and worst-case precision cost without assuming a uniform Diophantine gap. The explicit IJ fourth-order remainder is useful for candidate screening and counting but no longer a prerequisite for individual sign certification.
2. The all-scale discrepancy power bound, E-function value separation at larger primitive denominators, and independent review remain open. Preserve IR and prior asymptotic results; no formal Result or foundation promotion.
