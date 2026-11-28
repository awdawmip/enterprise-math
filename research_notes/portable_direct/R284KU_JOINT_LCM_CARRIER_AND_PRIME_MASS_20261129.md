# R284KU — joint LCM carrier, necessary large-prime mass, and exact integer exclusion to d=3300

2026-11-29. Author proof and local exact Python computation; NOT_REVIEWED. Auxiliary arithmetic of R284, not native spatial transfer. Own open session metadata recovered (r1-20261129-0100-recover-own), EM-DIRECT-0C386E / TASK_RESEARCH / RA-B82240E8488EF5A1DA5186C4, no formal RUN. Owner request r1-20261129-0100-leased-inventory last observed WAITING_RESOURCE, EVENT_READ_CONTROL_BUSY; no shared Task acquisition or mutation, no inference of empty inventory. Global canonical main d150ab52ca21af5f73e1781e06065739d42a8cb2, both entry blobs verified; P000 V4, Source V5 foundation projection, ACTIVE worldview, current portable and research method consulted. Frozen inputs KT 60fc4edf0a39e5972485b0eaf370096f5c5f4637:research_notes/portable_direct/R284KT_UNIFORM_EVALUATED_HEIGHT_AND_FACTORIAL_CARRIER_20261129.md; KO 0c99ee610045cd1d36e9da996f257ae4afabc0be:research_notes/portable_direct/R284KO_FIXED_SUPPORT_FAMILY_AND_EVEN_DECIC_20261128.md; KS 57423d472d6d65475583b7239efc51154c183d65; JR 88211c0912397b00536b6c4d6427cab29d4499f2:research_notes/portable_direct/R284JR_GLOBAL_BUDGET_POLYNOMIAL_AND_INTEGER_ROOT_EXCLUSION_20261127.md; KD 544d7a97fa075fe62848ae1cf27acdb9bdc7df19:research_notes/portable_direct/R284KD_FINITE_BRIDGE_AND_MODULAR_FALLBACK_20261128.md; KR pin inherited from KS. Root interval code frozen KL 87cbd27a2836e45f8d64523271eb5a1db4afa43b:research_notes/portable_direct/R284KL/root.py, changed range only for that subroutine.

## 1. Exact smaller simultaneous reverse-ratio carrier

Retain KT's wedge d>=8(s+4), d+s odd, t=s+1, a_j=3d+s+4-2j and b_j=d-s-2-2j for 0<=j<t. Both progressions consist of positive odd integers. Let rho_i=(-1)^i prod_{j<i} a_j/b_j, and L_s=lcm(b_0,...,b_{t-1}). Then

L_s rho_i is an integer for every 0<=i<=t.

Proof: for each odd prime p and power p^e, two length-i progressions of step -2 contain numbers divisible by p^e in counts differing by at most one: both counts are floor(i/p^e) or ceil(i/p^e). If the denominator count exceeds the numerator count, p^e divides some b_j. Thus the positive net denominator valuation across all e is at most max_j v_p(b_j)=v_p(L_s). At p=2 all terms are units. This proves exact simultaneous clearing, including negative signs. The argument retains the full ordered support; it does not remove a composite observer.

Moreover L_s divides KT's A_s=ell_t B_s/oddpart(t!), where B_s=prod b_j and ell_t=oddpart(lcm(1,...,t)). For p^e<=t, denominator count for the full progression is at least floor(t/p^e); the contribution to v_p(A_s) is at least one at every such e (the ell term adds one). For p^e>t the floor is zero, and the contribution is one whenever any b_j is divisible by p^e. Summing shows v_p(A_s)>=v_p(L_s). Exact minimal denominator is lcm_i den(rho_i), which divides L_s; it may be smaller. This is a reduction in the integer carrier, not a proof of minimality of L_s.

For T_s=binom(2s+2,s), J_s=(d+s)(d+s+1), L=4s+2, replace A_s in KT by L_s and define H_s=8 J_s L L_s T_s. The exact KT observer arithmetic carries over unchanged: H_s times V/r,Q/r,A_obs/r,E/r,W/r,Z/r are integers, and U_s=2 H_s^2 C(q0,d)/r^2 is an integer. The weight denominator divides 4J_s, the endpoint denominator divides 4(d+s+1)L, and H_s A_obs/r is even. All retained quantities are reconstructible from their scaled values and H_s. Since H_s has no prime factor >d+s+2, v_p(U_s)=v_p(P_d(q0)) there, including the zero convention.

## 2. Single denominator for the entire support vector

Let S satisfy d>=8(S+4), and use all admissible s<=S. Write M(n)=lcm(1,...,n), and D*=lcm of all odd b_j from these supports (empty lcm=1). Define

H*=8 D* M(d+S+1) M(4S+2) M(2S+2).

For every admissible s, H_s divides H*. Indeed L_s|D*, J_s|M(d+S+1) because its two adjacent factors are coprime, L|M(4S+2), and T_s|M(2S+2) by the binomial valuation floor bound v_p(T_s)<=floor(log_p(2s+2)). Also D*|M(d). Hence one common integer scale H* simultaneously represents all normalized joint observations and all endpoint contributions. KT's elementary M(n)<=8^n implies log H*=O(d+S)=O(d). This is a bound on the denominator of the whole vector, not on total numerator storage or total computational work. For p>d+S+2 all factors of H* are units, so the original large-prime valuation is preserved at every coordinate. For smaller primes eligible at a particular s (d+s+2<p<=d+S+2), the individual U_s still gives exact valuation; the common numerator U_s*=(H*/H_s)^2 U_s requires subtracting 2v_p(H*/H_s) (for nonzero values). Never treat a prime introduced by the common scale as an actual exceptional prime.

## 3. Linear interval forces large-prime mass (necessary, not yet sufficient)

Fix 0<c<alpha (KR), e.g. c=1/10, S=floor(cd), d large enough for the wedge. Let I be the admissible supports 0<=s<=S, d+s odd, M=|I|=cd/2+O(1). Let integer q be in [4d^2/5,4d^2/3]; define h_s=2q+d-s, Y=d+S+2. All h_s are positive odd integers, log h_s=2 log d+O(1) uniformly. Let h_s^(>Y)=prod_{p>Y}p^{v_p(h_s)}.

Then sum_s log h_s^(>Y) >= M log d-O_c(d).

Proof: h_s form an arithmetic progression of step -2. For odd p, at each power p^e the number of coordinates divisible by p^e is <=M/p^e+1. Put Hmax=max h_s=O(d^2). Thus the total log-mass from p<=Y is at most
M sum_{p<=Y} log p/(p-1) + pi(Y) log Hmax.
For completeness, KT's M(n)<=8^n gives psi(Y)=sum_{p^e<=Y}log p=O(Y). The factorial identity log(floor(Y)!)=sum_{p^e<=Y}floor(Y/p^e)log p implies sum_{p^e<=Y}log p/p^e<=log Y+O(1) by bounding each rounding error by log p, and the tail p<=Y,p^e>Y contributes <=2 theta(Y)/Y=O(1). Also pi(Y)<=sqrt(Y)+2psi(Y)/log Y=O(Y/log Y). Hence small-prime log-mass <=M log Y+O_c(d)=M log d+O_c(d), while total log-mass is 2M log d+O_c(d). Subtraction proves the claim.

Since a single h_s contributes at most 2 log d+O(1), at least M/2-O_c(d/log d) distinct coordinates have a prime >Y. Such primes cannot divide two different h_s because their difference has absolute value <=S<Y. The same lower bound holds for the number of distinct large primes over the family. This provides a deterministic necessary burden for any hypothetical root: the complete product of large parts must divide the product of |U_s| over I (all U_s nonzero for sufficiently large d by KR/KQ), with p>s+d+2 at every selected coordinate; in particular at least M/2-O_c(d/log d) mutually distinct exceptional primes are needed, assigned to specific coordinates, not merely a union of supports. It does not contradict KT's separate height bounds; a joint numerator divisibility or correlation estimate remains open. No unproved smooth-number distribution assumption is used.

## 4. Exact finite extension and joint arithmetic witness measurement

KD proves unique real zero on the whole legal interval for each d>=81. For every d=3201..3300 the KL fixed-point procedure located consecutive integers q_l,q_l+1 with exact positive and negative signs respectively. All intermediate multipliers and quantities used in the interval propagation are nonnegative in this legal region, hence endpoint multiplication is monotone. The final interval is in units of T^-4, T=2^96, and exact subtraction yields signed bounds; the approximate bisection is only a proposal, the strict endpoint signs and uniqueness prove the result independently of bisection error. Combined with previous d<=3200 coverage, all legal integer q for 3<=d<=3300 have C!=0 and thus qK!=32/3. No upper q bound is imposed.

As an independent arithmetic witness for both neighboring integers of each new d, search the complete h_s coordinates in increasing s (admissible parity) with s<=floor(d/10), factor h_s by trial division, and for each p>d+s+2 dividing h_s evaluate 2C(q0,d)/r^2 in F_p via KO's exact finite-support observer, retaining endpoint. All divisions are p-units by KO. Nonzero residual excludes an exact integer zero by JR polynomial congruence. This is an additional measurement of joint coordinate power, not needed for the real-root bracket theorem. Result: all 200 candidate integers have such a witness; first coordinate alone 162, second 33, third 3, fourth 1, fifth 1; maximum s=9; none missing. No inference that this finite fraction holds uniformly. The arithmetic witness search is distinct from exact sign certification.

Local executed Python script and complete compact certificate follow (raw exact-bound stdout SHA-256 bc100f54a050b6cf4cf6223f8429bbbb226ca98e7031a8ce87e628ea7f9990e5; local source SHA-256 268985aa8716b7b76618d65db699e8b791eb8cd0a1887c80a76346a1eb34b8bf). The compact certificate records d,q_l and both first witness triples (s,p,residue); q_h=q_l+1, h=2q+d-s. Exact signed bounds reproduced by script, not rounded data.

## 5. Executed reproduction

```python
from math import gcd,lcm,isqrt
from fractions import Fraction
import json

def carriers(d,s,check=True):
    B=O=ell=L=1
    for j in range(s+1):
        b=d-s-2-2*j; B*=b; L=lcm(L,b)
        z=j+1; z//=z&-z; O*=z; ell=lcm(ell,z)
    assert B%O==0
    A=B//O*ell; assert A%L==0
    if check:
        R=L; rho=Fraction(1); minimal=1
        for j in range(s+1):
            a=3*d+s+4-2*j;b=d-s-2-2*j
            assert (R*a)%b==0; R=-R*a//b
            rho*=Fraction(-a,b);minimal=lcm(minimal,rho.denominator)
            assert R==L*rho
        assert L%minimal==0
    else: minimal=None
    return A,L,minimal
count=strict=optimal=0
for d in range(32,201):
    for s in range(d//8-3):
        if (d+s)%2:
            a,l,m=carriers(d,s);count+=1;strict+=l<a;optimal+=l==m
samples=[]
for d,s in [(1000,99),(4000,399),(16000,1599),(16000,1713),(64000,6399)]:
    a,l,m=carriers(d,s,False);samples.append([d,s,a.bit_length(),l.bit_length()])
print(json.dumps(dict(count=count,strict=strict,optimal=optimal,samples=samples)))
T=1<<96
def scale(x,a,b=1):return (x[0]*a//b,-(-x[1]*a//b))
def mul(x,y):return(x[0]*y[0],x[1]*y[1])
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def obs(q,d,exact):
    u=q+d;n=2*q+d;J=2*u*(2*u+1);L=4*n+2
    if exact:
        def pref(v):
            r=[(T,T)]
            for i in range(d):r.append(scale(r[-1],v-i,v+i+3))
            return r
        U,N=pref(u),pref(n);V=Q=A=(0,0)
        for k in range(d+1):
            l=d-k;a=scale(mul(U[k],N[l]),(k+1)*(l+1));b=scale(mul(U[k],N[l-1]),(k+1)*l) if l else (0,0)
            V=add(V,a);Q=add(Q,b);A=add(A,scale(add(a,b),(u-k)*(u+k+2),J))
        E=scale(U[d],T*q*(2*d+3)*(n+2),2*(2*u+1)*L);W=add(A,E);Z=add(scale(A,q),add(V,Q))
        P=scale(mul(W,Q),3*q*(4*q+3*d+1)**2);M=scale(mul(Z,Z),32*(3*q+d+1))
        return P[0]-M[1],P[1]-M[0]
    def pref(v):
        r=[1.]
        for i in range(d):r.append(r[-1]*(v-i)/(v+i+3))
        return r
    U,N=pref(u),pref(n);V=Q=A=0.
    for k in range(d+1):
        l=d-k;a=(k+1)*(l+1)*U[k]*N[l];b=(k+1)*l*U[k]*N[l-1] if l else 0.
        V+=a;Q+=b;A+=(u-k)*(u+k+2)*(a+b)/J
    E=U[d]*q*(2*d+3)*(n+2)/(2*(2*u+1)*L);Z=q*A+Q+V
    return 3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*Z*Z

def large_factors(n,Y):
    f=[];a=2
    while a*a<=n:
        if n%a==0:
            if a>Y:f.append(a)
            while n%a==0:n//=a
        a+=1 if a==2 else 2
    if n>Y:f.append(n)
    return f

def residue(d,s,p):
    J=(d+s)*(d+s+1);L=4*s+2
    V=Q=A=0;r=rho=1;prev=0
    for i in range(s+2):
        if i:
            r=r*(s-i+1)*pow(s+i+2,-1,p)%p
            rho=rho*(3*d+s+6-2*i)*pow(s-d+2*i,-1,p)%p
        a=(d-i+1)*(i+1)*rho*r;b=(d-i+1)*i*rho*prev
        V=(V+a)%p;Q=(Q+b)%p;A=(A+(s-d+2*i)*(3*d+s-2*i+4)*(a+b))%p;prev=r
    A=A*pow(4*J,-1,p)%p
    E=(s-d)*(2*d+3)*(s+2)*pow(4*(d+s+1)*L,-1,p)%p
    W=(A+E)%p;Z=((s-d)*pow(2,-1,p)*A+Q+V)%p
    return (3*(s-d)*(2*s+d+1)**2*W*Q-32*(3*s-d+2)*Z*Z)%p

def witness(d,q):
    for s in range(1-d%2,d//10+1,2):
        assert d>=8*(s+4)
        h=2*q+d-s
        for p in large_factors(h,d+s+2):
            r=residue(d,s,p)
            if r:return [s,h,p,r]
    return None
hist={};missing=0;mx=0
for d in range(3201,3301):
    lo=4*d*d//5;hi=(4*d*d+2)//3
    while hi-lo>1:
        mid=(lo+hi)//2
        if obs(mid,d,False)>0:lo=mid
        else:hi=mid
    x=obs(lo,d,True);y=obs(hi,d,True)
    assert hi==lo+1 and lo>=64 and d*d<=4*lo and x[0]>0 and y[1]<0,(d,lo,hi,x,y)
    w=[witness(d,lo),witness(d,hi)]
    for v in w:
        if v is None:missing+=1;continue
        i=(v[0]-(1-d%2))//2;hist[i]=hist.get(i,0)+1;mx=max(mx,v[0])
    print(json.dumps([d,lo,hi,str(x[0]),str(y[1]),w],separators=(',',':')))
print(json.dumps(dict(brackets=100,missing=missing,max_s=mx,first_coordinate=hist)))
```

Local exact output summary:
```
{"count": 935, "strict": 501, "optimal": 124, "samples": [[1000, 99, 666, 612], [4000, 399, 2733, 2497], [16000, 1599, 10988, 9942], [16000, 1713, 11565, 10478], [64000, 6399, 44075, 40050]]}
{"brackets": 100, "missing": 0, "max_s": 9, "first_coordinate": {"0": 162, "2": 3, "1": 33, "3": 1, "4": 1}}
```
Here count is the number of all admissible d<=200 support pairs, strict counts L_s<A_s, optimal counts L_s equal to the exact least common denominator of all reverse ratios. Large samples only verify the exact A_s/L_s division and compare bit lengths, not the minimal carrier or entire joint vector. The proof is separate from finite checks.

Complete compact certificate:
```
3201 10919093 0 370193 69952 0 2426821 69403
3202 10925920 1 1681157 737557 1 3122149 1210046
3203 10932750 4 950813 221557 0 4523 1428
3204 10939582 1 1683259 1055005 1 87881 79751
3205 10946416 0 128047 62929 0 180959 39970
3206 10953253 1 8831 4108 1 447137 162557
3207 10960091 0 21923389 15813668 0 35999 3092
3208 10966932 1 10613 5278 1 327419 25745
3209 10973775 0 4093 669 0 37781 21168
3210 10980619 1 18757 7611 1 7129 5380
3211 10987466 0 68897 24788 0 627947 617861
3212 10994315 1 9467 2352 1 21991843 3357127
3213 11001167 0 6197 2099 0 106307 56410
3214 11008020 1 7339751 563280 3 7339751 3541619
3215 11014876 0 2002997 1058298 0 61717 1516
3216 11021733 1 361421 132679 1 22046683 9291155
3217 11028593 0 22060403 1027567 0 4412081 2907493
3218 11035455 1 22074127 4580124 3 22074127 18648007
3219 11042319 0 669329 405507 2 669329 579718
3220 11049185 1 9377 6632 1 7367197 808284
3221 11056054 0 22115329 18256491 0 351037 350202
3222 11062924 1 115859 86093 3 115859 79540
3223 11069797 2 5381 700 0 55219 20180
3224 11076671 3 51647 20031 5 51647 22955
3225 11083548 2 303703 168186 4 303703 85786
3226 11090427 1 7394693 299989 1 22184081 12008731
3227 11097308 0 2466427 926546 0 4439569 2258856
3228 11104192 1 419087 21766 1 2467957 2228337
3229 11111077 0 5651 2621 0 48847 2793
3230 11117965 1 7413053 7154178 1 29147 28
3231 11124854 0 22252939 14773262 0 824183 182838
3232 11131746 1 26227 22744 3 26227 22524
3233 11138640 0 22280513 12939246 0 66509 56673
3234 11145536 1 15013 5406 1 3184901 1818618
3235 11152434 0 22308103 5885569 0 51283 36890
3236 11159335 1 1488127 1033796 1 197539 30560
3237 11166237 0 7445237 423685 2 7445237 1254428
3238 11173142 1 22349521 3530234 1 1064263 437377
3239 11180048 0 496963 308398 0 972319 24743
3240 11186957 1 11821 9691 3 11821 1206
3241 11193868 0 1066237 268713 0 132491 65464
3242 11200781 1 22404803 15142142 1 4480961 1711386
3243 11207697 0 15601 7736 0 8179 3878
3244 11214614 1 9049 514 1 3457 2357
3245 11221534 0 7333 6544 2 7333 3616
3246 11228455 1 16699 6599 1 3323 3137
3247 11235379 0 13259 13228 0 22474007 13158060
3248 11242305 1 3212551 1102568 1 108637 29167
3249 11249233 2 576967 253475 0 3214531 1658844
3250 11256163 1 900623 278974 1 3216511 2930918
3251 11263096 0 979541 889538 0 25457 24591
3252 11270030 1 1073491 357737 1 1734101 1565766
3253 11276967 2 644491 197257 0 7519063 4841478
3254 11283906 1 410383 89898 1 7523689 3877196
3255 11290847 0 4547 2797 0 6451 3864
3256 11297790 3 22598833 14838790 1 4019 3604
3257 11304735 0 9241 4158 0 12073 8437
3258 11311682 1 9011 3155 1 22626623 18916635
3259 11318631 0 101527 15805 0 7546841 4852089
3260 11325583 7 42187 971 9 42187 3864
3261 11332537 0 96461 33032 2 96461 7437
3262 11339492 1 4536449 602097 3 4536449 4498340
3263 11346450 0 4099 27 0 5827 5779
3264 11353411 1 197479 39438 1 2523343 92708
3265 11360373 0 23117 14429 2 23117 3925
3266 11367337 1 5441 4938 1 4111 1952
3267 11374304 2 1197467 621190 0 91373 64713
3268 11381272 1 734381 622069 1 69197 37458
3269 11388243 0 25171 6574 2 25171 21173
3270 11395216 1 36587 583 1 7597901 1650364
3271 11402191 2 26801 595 0 350887 281198
3272 11409168 1 3307 2134 1 7607203 4549469
3273 11416147 2 12377 7299 0 22835569 6059552
3274 11423129 1 60289 40141 3 60289 53412
3275 11430112 0 10729 5662 0 2540389 1990221
3276 11437098 1 73561 51526 3 73561 58274
3277 11444086 0 7219 7198 0 8291 2585
3278 11451076 3 275969 14247 1 1205549 730468
3279 11458068 2 2083583 551519 0 4253 697
3280 11465062 3 7644467 1378539 1 9697 6599
3281 11472059 0 6521 3988 2 6521 5132
3282 11479057 1 42131 19863 1 7653799 3868837
3283 11486058 0 22975399 8561239 0 7658467 2901293
3284 11493061 1 1532627 275788 1 3284201 2733154
3285 11500065 2 23003413 168351 0 23003417 9576802
3286 11507072 1 15907 1041 1 42863 33525
3287 11514082 2 3290207 3269975 0 7677151 703710
3288 11521093 1 20743 16445 1 307273 74587
3289 11528106 0 16993 3863 0 2562167 784025
3290 11535122 1 89087 41846 1 11863 5988
3291 11542140 0 4519 468 0 23087573 10096129
3292 11549160 1 3547 1255 1 23101613 1685386
3293 11556182 0 7705219 2314623 0 3302237 2823029
3294 11563206 1 6833 2324 3 6833 6406
3295 11570232 0 625507 385554 2 625507 473631
3296 11577260 1 36469 19073 1 166603 143037
3297 11584291 2 2574653 302326 0 83653 22844
3298 11591323 1 123989 8021 1 4637189 2096579
3299 11598358 0 4640003 1055558 0 38861 6201
3300 11605395 3 66137 37520 1 53861 52846
```

## 6. Next

Seek a joint exceptional-prime **numerator** constraint, as sharing a denominator does not bound the union of unrelated numerators by O(d). Use the necessary linear large-prime assignment from section 3 as the target. Investigate primes appearing in adjacent support observers through exact modular finite-support recurrence, and develop a single correlated valuation certificate instead of adding heights. The remaining original global target is d>=3301. KS second-order thin-strip constants remain open. No mathematical acceptance, formal Result, or Foundation promotion.
