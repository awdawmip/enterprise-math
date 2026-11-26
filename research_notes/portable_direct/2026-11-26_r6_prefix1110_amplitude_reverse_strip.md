# PREFIX-1110 — Reverse amplitude observation by adjacent normalized signed BRC values

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / DISPLAY_ENCLOSURE_CONDITIONAL / NOT_REVIEWED. Own R6 Activity RA-0ABD84561C86E53067DB0322, EM-DIRECT-780BBE / TASK_RESEARCH. Original registration r6-20261123-2358-session-start-own-v1 verified SUCCEEDED, execution_authorized=false. Current read-only owner query r6-20261126-2052-owner-read-v1 last RUNNING before this publication; no new claim, run or shared task mutation.

Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json and joint/time companions. Same Stage46 six-axis X6 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations Link {O,e1} blocked without renormalization, exactly two negative steps. Use only inherited signed radial BRC observer D_m(k)=L[x^m(1-x)^k]; no state collapse, native propagation, physical attribution or new classical comparison.

Sources:
- 60f5d76fb61beaefbd9c479a0e96c9429c379513:research_notes/portable_direct/2026-11-26_r6_prefix1100_centered_beta_dual.md (section 3 rounded display of normalized signed observations, refined anchor).
- 74b507708fa98cca4031924c9344e663f217ac0f:research_notes/portable_direct/2026-11-26_r6_prefix1100_centered_beta_dual.py (oracle returns exact center/radius; check prints list(map(float,...)); not rerun this round).
- 7e95625df3a8c21b6d370246065d51469afa6345:research_notes/portable_direct/2026-11-26_r6_prefix1107_signed_density_jet.md (effective normalized remainder; b in (.044,.045), g'(b)<0).
- 53d572769fe8745d7c60d93b92b28b182dabfa00:research_notes/portable_direct/2026-11-26_r6_prefix1097_effective_monotone_last_negative.md.
- f6cd6a43428786cbcc64f32baeba52eaf2e7be56:research_notes/portable_direct/2026-11-26_r6_prefix1109_reverse_edge_strip.md (coefficient boxes, 39 candidate pairs).

## New theorem
Let f(m)=rho*m+c+d/m, W(k)=D_m(k)/(K*Beta(m+1,k+1)), K>0 the common 1100 density normalization. Inherit the 1107 bound |D/(g'(b)B)+b^2 e/m| <= 1000|e|/m^2+620/m^3 for e=k-f(m), |e|<=2, m>=10^8. For adjacent observations k,k+1, assume both within this band and W(k)<0<W(k+1). Write x=f(m)-k, lambda=-g'(b)*b^2/(K*m)>0. Then W(k)=lambda*(-x+delta0), W(k+1)=lambda*(1-x+delta1), where |delta_i|<=epsilon=(2000/m+620/m^2)/(.044^2). In particular define r=-W(k)/(W(k+1)-W(k)); 0<r<1. Exact cancellation gives x=r+(1-r)*delta0+r*delta1, hence |x-r|<=epsilon. No evaluation of K, g'(b), or giant factorials; the common normalization cancels without discarding the residual. If -W(k) in [a_l,a_u], W(k+1) in [b_l,b_u] with strictly positive endpoints, monotonicity of a/(a+b) yields r in [a_l/(a_l+b_u),a_u/(a_u+b_l)]. Thus rho lies in [(k+r_l-epsilon-c_u-d_u/m)/m,(k+r_u+epsilon-c_l-d_l/m)/m]. This is a conditional analytic theorem with explicit inputs. For known exact K_last=k the previous reverse strip ensures x in [-E/m^2,1+E/m^2], so both offsets satisfy |e|<=2. It gives width <=(r_u-r_l+2epsilon+c_u-c_l+(d_u-d_l)/m)/m. With true normalized values known to relative adjacent-gap error eta, width scales O(eta/m+m^-2+width(c)/m+width(d)/m^2), not merely O(1/m). No unconditional uniform separation or independent validation.

## Actual computation and evidence limitation
Use the 1100 refined displayed V_k,V_(k+1) at m=10^21 and 10^22. They are rounded displays, NOT stored exact interval endpoints. Treat each displayed center as an enclosure with padding 10^-26 and each displayed radius 1.9127615888091676e-17 as bounded by 2e-17. These are deliberately much wider than ordinary binary64/decimal rounding of these reported values. The conditional numerical conclusion assumes the displayed values faithfully report the earlier exact computation to these tolerances. The parent code explicitly prints float(center),float(radius), which is consistent with this allowance; the raw Fraction endpoint values were not recovered or independently rerun in this round. Do not upgrade this new conditional certificate to raw exact BRC evidence until that replay is performed. This limitation is separate from the exact rational arithmetic performed here.

Actual Python Fraction execution: regenerated the prior 39 candidates with identical window counts/nodes, ordered compact-JSON SHA256 9634c13a9d74ff95ba43079d129687b9d7bb62abd3f7e7dac2b51253ed4b5f0e. Ratio intervals (rounded display only) for 10^21: [0.9315396464173455,0.931545259887596], epsilon<1.034e-15; for 10^22: [0.04630252504756364,0.046358659750067775], epsilon<1.034e-16. New intersected rho width 5.6134702504352114e-27, improvement 13020.574230663133 over 1109. Exact rho endpoints:
739434062350255201177721717793081996635402512715818087979520916942719907441004247795105248183/34488469958940427100000000000000000000000000000000000000000000000000000000000000000000000000
29577362494010208047108868719467279869317724401319927828721860465845893797071343936523767909/1379538798357617084000000000000000000000000000000000000000000000000000000000000000000000000
All 39 old candidates lie outside the new band, min gap 3.3799748502778165e-13. New exact midpoint rho=2144003672040464398327479053201547181/10^35, c,d unchanged old midpoints. Six new left-closed right-open dyadic windows beginning at M=1024,2048,4096,8192,16384,32768 times 10^9 return (nodes, candidate count)=(5,0),(5,0),(5,0),(87,1),(257,3),(765,9), totaling 1124 nodes and 13 candidates. First unresolved (10361329829227,222147292010950). New candidate list SHA256 37a7eae12d50510a319df882521a25ed9fa8854fc4f0fd107bf727e8e51cd391. Conditional on above enclosures and inherited results, all m in [10^8,65536*10^9) except these 13 have K_last=floor(rho_mid*m+c_mid+d_mid/m). All m<10361329829227 in this range are covered. Total 65535899999987 rows, conditional; previous 1109 certified rows retain original independent scope. No new expensive CT, no repeated raw propagation or anchor generation.

## Reproduction
The following combines the immutable 1109 reproduction and the new locally executed equivalent extension. The local execution used an equivalent standalone Fraction sieve and printed the exact endpoints, counts and hashes; this combined remote Markdown was not separately executed. The code below regenerates the original 1109 state first, then reproduces the conditional extension. The only unverified scientific input is the stated outward enclosure of the historical displayed values, in addition to inherited hypotheses. For exact-source upgrade run the 1100 oracle at the two adjacent rows and assert |V-V_display|<=10^-26 and radius<=2*10^-17 before using the extension.

```python
from fractions import Fraction as F
from math import lcm
import random,hashlib,json
D=10**30
R=[F(21440036720404643983243551290966,D),F(21440036720404643983306198520807,D)]
C=[F(99141010437680654620437916203756,D),F(99141010437680654628564001195910,D)]
T=[F(9690862659641548432988461360525,D),F(9690862659641549206936415331527,D)]
E=400000

def fs(n,m,a,b):
    q,a=divmod(a,m); ans=q*n*(n-1)//2
    q,b=divmod(b,m); ans+=q*n
    while True:
        if a>=m:
            q,a=divmod(a,m); ans+=q*n*(n-1)//2
        if b>=m:
            q,b=divmod(b,m); ans+=q*n
        y=a*n+b
        if y<m: return ans
        n,b=divmod(y,m); m,a=a,m

def sumfloor(l,h,a,b):
    w=lcm(a.denominator,b.denominator)
    return fs(h-l+1,w,int(a*w),int((a*l+b)*w))

def strip(l,h):
    x=F(l+h,2)
    al=R[0]-T[0]/x**2; bl=C[0]+2*T[0]/x-F(E,l*l)
    au=R[1]-T[1]/(l*h); bu=C[1]+T[1]*F(l+h,l*h)+F(E,l*l)
    return sumfloor(l,h,au,bu)+sumfloor(l,h,-al,-bl)+(h-l+1)

def isolate(l,h):
    stack=[(l,h)]; leaves=[]; points=[]; visited=0; initial=strip(l,h)
    while stack:
        a,b=stack.pop(); cnt=strip(a,b); visited+=1
        assert cnt>=0
        if cnt==0: leaves.append((a,b)); continue
        if a==b:
            low=R[0]*a+C[0]+T[0]/a-F(E,a*a)
            high=R[1]*a+C[1]+T[1]/a+F(E,a*a)
            jl=-((-low.numerator)//low.denominator); jh=high.numerator//high.denominator
            assert cnt==jh-jl+1
            points.extend((a,j) for j in range(jl,jh+1)); continue
        mid=(a+b)//2; stack.extend([(mid+1,b),(a,mid)])
    assert sum(b-a+1 for a,b in leaves)+len({a for a,j in points})==h-l+1
    return initial,visited,leaves,points


Rold=R[:]
rows=[(10**20,2144003672040464398426),(10**21,21440036720404643983373),(10**22,214400367204046439832847)]
for m,k in rows:
    R=[max(R[0],(k-C[1]-T[1]/m-F(E,m*m))/m),
       min(R[1],(k+1-C[0]-T[0]/m+F(E,m*m))/m)]
    assert R[0]<=R[1]
assert (Rold[1]-Rold[0])/(R[1]-R[0])>857
assert R[1]-R[0]<F(731,10**25)
print("rho width",float(R[1]-R[0]),"improvement",float((Rold[1]-Rold[0])/(R[1]-R[0])))
print("rho exact",*[str(r) for r in R])
Rnew=R[:]; R=Rold
windows=[(10**8,2*10**8-1),(2*10**8,10**9-1),(10**9,2*10**9-1),(2*10**9,4*10**9-1),(4*10**9,8*10**9-1),(8*10**9,16*10**9-1),(16*10**9,32*10**9-1),(32*10**9,64*10**9-1)]
old=[];vis=0
for l,h in windows:
    _,v,_,p=isolate(l,h); old+=p;vis+=v
assert len(old)==128 and vis==7554
assert hashlib.sha256(json.dumps(old,separators=(',',':')).encode()).hexdigest()=="c3169c9517f4722b6db3b848b76931ff5d6d3334966f0a790a226636e7d1e5d9"
R=Rnew
for m,j in old:
    lo=R[0]*m+C[0]+T[0]/m-F(E,m*m)
    hi=R[1]*m+C[1]+T[1]/m+F(E,m*m)
    assert hi-lo<1 and not lo<=j<=hi
    k=j if lo>j else j-1
    fhat=sum(Rold)*m/2+sum(C)/2+sum(T)/(2*m)
    assert k==fhat.numerator//fhat.denominator
    assert max(lo-j,j-hi)>F(1,10**12)
r_mid=F(21440036720404643983274822444259,D)
assert R[0]<=r_mid<=R[1]
allnew=[]
for l,h,n_expected,v_expected in [(64*10**9,128*10**9-1,0,1),(128*10**9,256*10**9-1,3,217),(256*10**9,512*10**9-1,8,565),(512*10**9,1024*10**9-1,28,1951)]:
    _,v,_,p=isolate(l,h)
    assert len(p)==n_expected and v==v_expected
    allnew+=p
    print("extension",l,h,v,len(p),p)
assert (R[1]-R[0])*1024*10**9+(C[1]-C[0])+(T[1]-T[0])/10**8+F(2*E,10**16)<F(1,8)
assert len(allnew)==39
print("certified",1024*10**9-10**8-len(allnew))


# 1110: reuse the old refined R and exact candidate list allnew.
Rold1110=R[:]
for m,k,a,b in [(10**21,21440036720404643983373,'-6.637907832856747e-12','4.878091008086301e-13'),(10**22,214400367204046439832847,'-3.301386868029895e-14','6.795578246862388e-13')]:
    rad=F('2e-17')+F('1e-26'); a=-F(a); b=F(b)
    assert a>rad and b>rad
    xl=(a-rad)/(a+b); xu=(a+rad)/(a+b)
    eps=(F(2000,m)+F(620,m*m))/F('0.044')**2
    R=[max(R[0],(k+xl-eps-C[1]-T[1]/m)/m),min(R[1],(k+xu+eps-C[0]-T[0]/m)/m)]
    assert R[0]<=R[1]
    print("ratio",m,float(xl),float(xu),"eps",float(eps),"rho width",float(R[1]-R[0]))
assert (Rold1110[1]-Rold1110[0])/(R[1]-R[0])>13020
assert R[1]-R[0]<F(562,10**29)
assert hashlib.sha256(json.dumps(allnew,separators=(',',':')).encode()).hexdigest()=="9634c13a9d74ff95ba43079d129687b9d7bb62abd3f7e7dac2b51253ed4b5f0e"
closed=[]
for m,j in allnew:
    lo=R[0]*m+C[0]+T[0]/m-F(E,m*m); hi=R[1]*m+C[1]+T[1]/m+F(E,m*m)
    assert not lo<=j<=hi
    closed.append(max(lo-j,j-hi))
assert min(closed)>F(337,10**15)
P=10**35; r=(sum(R)*P/2).__floor__()
assert r==2144003672040464398327479053201547181 and R[0]<=F(r,P)<=R[1]
new=[]
for lo,n,v in [(1024*10**9,0,5),(2048*10**9,0,5),(4096*10**9,0,5),(8192*10**9,1,87),(16384*10**9,3,257),(32768*10**9,9,765)]:
    assert (R[1]-R[0])*2*lo+C[1]-C[0]+(T[1]-T[0])/lo+F(2*E,lo*lo)<1
    _,w,_,pts=isolate(lo,2*lo-1); assert (len(pts),w)==(n,v)
    new+=pts; print("new",lo,w,len(pts),pts)
assert len(new)==13
assert hashlib.sha256(json.dumps(new,separators=(',',':')).encode()).hexdigest()=="37a7eae12d50510a319df882521a25ed9fa8854fc4f0fd107bf727e8e51cd391"
print("certified conditional",65536*10**9-10**8-len(new))

```

## Next
Recover actual raw 1100 normalized Fraction values (or run the pinned exact oracle and emit outward rational intervals); establish the display-enclosure premise before promoting the extended finite window certificate. Then consume the 13 remaining candidates using the same amplitude reverse method or a targeted certificate. Investigate joint correlated ratio error via shared anchor dual functional, which could reduce the ratio interval without increasing anchor order. Uniform arithmetic separation, exact zero, remaining spectrum zeros, c2=0 and mother B_fix,odd(32) remain open.
