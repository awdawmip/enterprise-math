# R284IT — Critical-gap distribution, equality certificate and adaptive precision law
2026-11-26. Author analytic proof and executed exact-rational checks, NOT_REVIEWED. Existing directed R284 research, own RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E; original registration recovered SUCCEEDED; no shared run. Current owner query r1-20261126-2004-owner-inventory last observed RUNNING before publication; no shared Task claimed or mutated. Account entries verified at main@00dda2d5410c114bdcc4b515d56fd65a371e4397, P000 V4 projection matched canonical blob, Source foundation projection and ACTIVE worldview consulted. Auxiliary binary-tag joint-count observer only; no native physical attribution.

Frozen sources: IS@d235b53a819dc0fd6b4aa3ca3e349de911f5d96a (exact joint counts and polynomial fiber oracle); IJ@75426bd0581d1826bfde31ac82cb5a632f53cc51 (uniform profile, inversion and derivative certificates); IK@edf8d2a631c536cc4f7e9f4c94ed3fa77306c3bd (equidistribution); IM@0b2b7b16e08ca9516a4fa64d75d6aec2f60f70fc (quantitative discrepancy); IO@b6d9d4c99b9fcba85c5fca2e9eb83fe763d276cf (root enclosure and rational evaluator). All are the exact R284 portable_direct notes. ID author-level monotonicity through IJ is needed only for minimum-budget interpretation, not the local gap law or rational equality test.

## 1. Two-scale critical-gap law

Write F(q,d)=qK(q,d)-32/3, h=q^(-1/2), s=s0, C=C0, Z=Z0, a=Phi'(s0)>0, and T(q)=s sqrt(q)+C+Z/sqrt(q). Define G(q)=min{|F(q,d)|: integer d, |d-T(q)|<=3, 0<=d<=2 sqrt(q)} for sufficiently large q (finite small q irrelevant). IJ's uniform expansion yields, for x=d-T(q), |x|<=3,
q F(q,d)=a x+O(h|x|+h^2).
Indeed IJ has error O(h|x|+h|x|^2+h^2) after multiplication by q, and x is bounded. In particular qG(q)=a dist(T(q),Zintegers)+O(h). Constants uniform in the local candidates. For a small margin epsilon, the sharper sandwich uses
(a-O(h))|x|-O(h^2) <= q|F| <= (a+O(h))|x|+O(h^2).

For integer X and X<=q<2X, uniformly in epsilon>=0,
# {q: qG(q)<=epsilon} = X min(1,2 epsilon/a)+O(sqrt(X)).
Proof: the O(h) sandwich changes the fractional-distance window length by O(X^-1/2), including clipping at 0 and 1/2. T is strictly increasing on the block, T' asymptotic to s/(2sqrt(q)), T''=O(X^-3/2); its inverse has derivative O(sqrt(X)) and second derivative O(1). On each complete unit interval of T, the preimage length of a fractional subinterval J differs from |J| times the full preimage length by O(1), by the bounded variation of the inverse derivative on that unit. Integer counting differs from length by O(1) per interval. There are O(sqrt(X)) complete cells and at most two boundary cells of length O(sqrt(X)). Sum; the error is uniform in J and in epsilon. Distance-to-integer uses at most two intervals. This elementary first-scale law needs no Diophantine estimate.

The second scale is finer. For each fixed t>=0 define B_t(X)=#{q<=X: q^(3/2)G(q)<=t}, with finite initial terms omitted. Let Q_n=((n-C)/s)^2, W=2Z/s, and U_n=Q_n-W. For every fixed upper bound t_max, uniformly for 0<=t<=t_max,
B_t(X) = (4t/a) sqrt(X) + O_{t_max,epsilon}(sqrt(X) L_X^(-1/2+epsilon)),
where L_X=log X/log log X and epsilon>0. In particular B_t(X)/sqrt(X) -> 4t/a; for t=0 this counts exact local equalities, not merely ambiguous signs.

Proof: if q^(3/2)|F(q,n)|<=t, the sharper sandwich forces |n-T(q)|=O(h). Consequently q=U_n+O(1). Conversely in any fixed bounded neighborhood of U_n, direct expansion yields
sqrt(q)(n-T(q))=(s/2)(U_n-q)+O(q^-1/2)
and hence
q^(3/2) F(q,n)=(as/2)(U_n-q)+O(q^-1/2).
Here the first identity follows from the exact difference of square roots; its error is in fact O(q^-1) in a bounded neighborhood. The second retains IJ's genuine remainder O(h^4) in F, which becomes O(q^-1/2) after rescaling. Thus actual q are sandwiched between integer intervals centered at U_n of radii max(0,2t/(as)-K/n) (empty if the untruncated radius is negative) and 2t/(as)+K/n. Distinct large-n intervals are disjoint. Complete n below X number s sqrt(X)+O(1); partial last interval contributes O(1). On a dyadic n block [M,2M), changing radii by O(1/M) changes expected counts by O(1). For a fixed bounded radius R the lattice-count function of {U_n} is a bounded step function with finitely many jumps, average 2R, and variation uniformly bounded for bounded R; even closed endpoints and R=0 are controlled by discrepancy via arbitrarily small neighborhoods. IM's prefix discrepancy bound controls block counts by O(M D_{2M}+M D_M+1), also for the two perturbed radii. If lower radius is negative use empty lower bound with expected length error O(1/M). Sum dyadically (small n contribute a bounded or negligible term), giving the stated error. The same proof with IK alone gives o(sqrt(X)). Exact equality or shrinking t is retained. This is distinct from the rounding-exception count: the new observation is the magnitude of the true signed joint-count residual.

For alpha>1/2, the same upper sandwich on each dyadic q block gives
#{q<=X: G(q)<=q^(-1-alpha)} = O_epsilon(sqrt(X) L_X^(-1/2+epsilon)).
Indeed the radius is O(X^(1/2-alpha)+X^-1/2), the expected block count O(X^(1-alpha)+1), dominated asymptotically by the displayed discrepancy error. The first-scale bound also holds for small positive epsilon and equality.

## 2. Exact equality by a rational-height certificate

IS gives a polynomial-bit-complexity interval oracle of width O(2^-p) for every integer q>=64, 0<=d<=2 sqrt(q), and p above an absolute constant. Here we remove the need for a full rational enumeration fallback to distinguish exact equality. Use its exact notation u=q+d, m=u+q, V,Q,A,E, and define the integer common denominator
D = [prod_{i=0}^{d-1}(u+i+3)(m+i+3)] [prod_{l=0}^d(m-l+1)] 2u(2u+1)(d+1)(u+d+2)(4m+2).
Each of D V,D Q,D A,D E is an integer (the (l+1) in the Q observer cancels before forming the denominator, while the exact endpoint retains its separate denominator). Set v=D V,b=D Q,c=D A,e=D E. The original exact rational law becomes
qK = q(3u+q+1)^2(c+e)b / [(u+2q+1)(qc+b+v)^2].
All factors in D are <=8q, and there are 3d+6 of them. IS gives V<=Zsum, Q<=4Zsum, A<=5Zsum, with Zsum=(d+1)(d+2)(d+3)/6 <=(8q)^3. Hence qc+b+v <=5(q+1) Zsum D <=(8q)^(3d+10). Since u+2q+1<=8q, the displayed positive denominator is <=(8q)^(6d+21). Subtracting 32/3 proves the exact alternative
F(q,d)=0 or |F(q,d)| >= (8q)^(-6d-22).
No integer product D has to be materialized in the decision algorithm. Use the bound, or the smaller bound 2^[-(6d+22) ceil(log2(8q))], and increase interval precision until either the target is strictly outside or the enclosure containing it has width strictly less than that bound. In the second case F=0 exactly. Termination precision O((d+1) log q) holds by IS. The full oracle remains polynomial in precision plus input length, but this cap is not polynomial in log q at d~sqrt(q). It is an equality-capable compressed algorithm rather than a claim of polylogarithmic worst-case complexity. For d=0 the identity Q=0 also directly settles the sign.

## 3. Adaptive precision distribution (including exact equality)

For large q, use a constant-size candidate set containing all integers within distance 2 of T(q) and contained within distance 3. An approximation to T within 1/4 suffices (take all integers within 5/2 of it). For example approximate s to O(q^-1/2) using IO's simple-root rational Taylor/bisection evaluator, approximate C to fixed error smaller than 1/16, and omit Z/sqrt(q) once negligible; rational sqrt brackets can be obtained by integer bisection. The source's simple-root derivative bound and analytic uniform Taylor tails imply polynomial(log q) candidate construction; finitely many initial q can be handled exactly. IJ strict local brackets + frozen ID monotonicity allow the minimum budget for either >= or > to be read from certified signs in this set. No nonzero-gap assumption needed.

Use IS precision p0(q)=ceil(log2 q)+c0 (fixed c0 to exceed the uniform oracle startup bound) and increase in single-bit steps. At each precision, either strict sign is certified or the height test certifies equality. Let J(q) be the largest additional bits required among the constant-size candidates. If J(q)>j then G(q)<=C_* 2^-j/q by uniform interval width. Therefore uniformly on X<=q<2X,
#{q: J(q)>j} = O(X 2^-j+sqrt(X)).
For j>=ceil(log2 X) the second-scale estimate (upper shrinking interval) strengthens this to O_epsilon(sqrt(X) L_X^(-1/2+epsilon)). The equality cap gives J(q)=O(sqrt(X) log X). Summing tail probabilities (integer layer cake) up to ceil(log2 X) costs O(X+sqrt(X) log X); summing the rest costs O_epsilon(X log X L_X^(-1/2+epsilon)). Thus for 0<epsilon<1/2,
(1/X) sum_{X<=q<2X} J(q) = O_epsilon(1+log X L_X^(-1/2+epsilon)) = o(log X).
The average final precision over a dyadic block is consequently log2 X+o(log X), even with exact equality included. A truncated strategy at extra (1/2) log2 X+O(1) bits leaves O(sqrt(X)) difficult budgets; the mean truncated extra bits is O(1), by the first-scale tail sum. These statements concern precision and number of incremental precision rounds, not mean bit runtime of a high-degree polynomial oracle; high moments and actual implementation costs remain separate. This uses the entire joint residual and does not erase E or infer gap from a rounded budget.

## 4. Executed checks
Python standard-library exact integer/Fraction arithmetic. Ideal centered interval counts over n=100..20099; frozen outward enclosures from IJ/IO:
t, lower count, upper count, ambiguous cluster count, predicted mean count
1,2429,2431,2,2442.4650681246535
4,9847,9848,1,9769.860272498614
16,39105,39105,0,39079.441089994456
32,78180,78181,1,78158.88217998891
These are IDEAL bands only, not true-K enumeration.
Actual IS full joint count intervals at four consecutive q near each of six centers; Y/N means strictly inside/outside q^(3/2)|F(q,n)|<t at t=1,4,16,32, with comparison by exact squaring:
n,q,p,decisions
100,10216,68,NNNY
100,10217,68,NNYY
100,10218,68,NNYY
100,10219,68,NNNY
500,264541,78,NNNY
500,264542,78,NNYY
500,264543,78,NNYY
500,264544,78,NNNY
1000,1062610,82,NNNY
1000,1062611,82,NNYY
1000,1062612,82,NNYY
1000,1062613,82,NNNY
3000,9590031,88,NNNY
3000,9590032,88,NNYY
3000,9590033,88,NNYY
3000,9590034,88,NNNY
10000,106658819,94,NNNY
10000,106658820,94,NNYY
10000,106658821,94,NYYY
10000,106658822,94,NNNY
20000,426723414,98,NNNY
20000,426723415,98,YYYY
20000,426723416,98,NNYY
20000,426723417,98,NNNN
All 96 threshold decisions strict and certified. For q=64..149, all 1808 allowed d (0<=d<=floor(2sqrt q)) were independently enumerated exactly to check common denominator, height and separation; no equality in this finite domain. The unbounded equality alternative is analytic; this finite evidence does not exclude equality elsewhere.

## Reproduction
Reuse the frozen IS functions below (unchanged oracle; imports and comments may be condensed), then run the additional exact tests. All threshold decisions use rational comparisons, decimal output is presentation only.
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


sl,sh=F('0.968081516889'),F('0.968081516890')
cl,ch=F('2.0640021544'),F('2.0640021551')
wl,wh=F('17.0792896715'),F('17.0792897012')
al,ah=F('33.8337158292'),F('33.8337158341')
zl,zh=F('0.93718182334228629862467342690845'),F('0.93718182334228629862467342690846')
def center(n):return (F(n)-ch)**2/zh-wh,(F(n)-cl)**2/zl-wl
def floor(x):return x.numerator//x.denominator
def ceil(x):return -floor(-x)
def count(l,r):return max(0,floor(r)-ceil(l)+1)
for t in [1,4,16,32]:
    rl,rh=2*t/(sh*ah),2*t/(sl*al)
    low=high=amb=0
    for n in range(100,20100):
        l,u=center(n);a=count(u-rl,l+rl);b=count(l-rh,u+rh)
        assert a<=b
        low+=a;high+=b;amb+=a!=b
    print('ideal',t,low,high,amb,'predicted',float((rl+rh)*20000))
for n in [100,500,1000,3000,10000,20000]:
    l,u=center(n);k=floor((l+u)/2)
    for q in [k-1,k,k+1,k+2]:
        p=2*q.bit_length()+40
        a,b,*_=certify(q,n,p);a-=F(32,3);b-=F(32,3)
        lo=F(0) if a<=0<=b else min(abs(a),abs(b));hi=max(abs(a),abs(b))
        decisions=['Y' if q**3*hi**2<t*t else 'N' if q**3*lo**2>t*t else '?' for t in [1,4,16,32]]
        assert '?' not in decisions
        print('actual',n,q,p,''.join(decisions))
def exact_height(q,d):
    u=q+d;m=u+q
    def weights(n):
        a=[F(1)]
        for i in range(d):a.append(a[-1]*F(n-i,n+i+3))
        return a
    P,R=weights(u),weights(m);V=Q=A=E=F(0)
    for k in range(d+1):
        l=d-k;w=(k+1)*(l+1)*P[k]*R[l]
        t=F(l*(m+l+2),(l+1)*(m-l+1));v=F((u-k)*(u+k+2),2*u*(2*u+1))
        V+=w;Q+=w*t;A+=w*v*(1+t)
        if l==0:E=w*v*(1+F((d+2)*(u-1-d),(d+1)*(u+d+2)))*F(m+2,4*m+2)
    D=1
    for i in range(d):D*=(u+i+3)*(m+i+3)
    for l in range(d+1):D*=m-l+1
    D*=2*u*(2*u+1)*(d+1)*(u+d+2)*(4*m+2)
    v,b,a,e=[z*D for z in (V,Q,A,E)]
    assert all(z.denominator==1 for z in (v,b,a,e))
    den=(u+2*q+1)*(q*a+b+v)**2
    assert den.denominator==1 and den<=(8*q)**(6*d+21)
    g=F(q*(3*u+q+1)**2)*(a+e)*b/den-F(32,3)
    if g:assert abs(g)>=F(1,(8*q)**(6*d+22))
    return bool(g)
from math import isqrt
n=zeros=0
for q in range(64,150):
    for d in range(isqrt(4*q)+1):
        zeros+=not exact_height(q,d);n+=1
print('height checks',n,'equality',zeros)
```

## Next
Implement and benchmark the full adaptive equality-capable search (the proof above specifies the algorithm, but a full search benchmark was not executed this turn). Tighten rational height with shared denominators and p-adic valuations; seek a poly(log q) nonzero-gap bound or exact equality exclusion on useful unbounded families. Preserve the full signed residual, the finite actual K certificates and the IM discrepancy dependency. Independent review remains open; do not promote or close the shared mother question.
