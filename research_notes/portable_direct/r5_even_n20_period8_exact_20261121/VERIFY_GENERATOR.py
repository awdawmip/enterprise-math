from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json

S0=(214,215,216,217,218)
S1=(214,216,217,218,219,220,221)
S2=(215,216,217,218,219,220,221)
E0=tuple(range(219,315))
E1=(215,)+tuple(range(222,315))
E2=(214,)+tuple(range(222,315))
Eh=tuple(range(222,315))
N=96
J=4
ZERO=(Q(0),Q(0))
ONE=(Q(1),Q(0))

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def neg(a): return (-a[0],-a[1])
def div(a,b): return mul(a,(b[0]/(b[0]*b[0]+b[1]*b[1]),-b[1]/(b[0]*b[0]+b[1]*b[1])))
def scale(a,k): return (a[0]*k,a[1]*k)
def ii(e): return (ONE,(Q(0),Q(1)),(Q(-1),Q(0)),(Q(0),Q(-1)))[e%4]

def choose_int(n,r):
    import math
    p=1
    for j in range(r): p*=n-j
    return p//math.factorial(r)

def qjet(e): return tuple(scale(ii(e),(-1)**r*choose_int(e,r)) for r in range(J))
J0=(ZERO,)*J
J1=(ONE,)+(ZERO,)*(J-1)

def jadd(a,b): return tuple(add(x,y) for x,y in zip(a,b))
def jsub(a,b): return tuple(sub(x,y) for x,y in zip(a,b))
def sumgauss(xs):
    ans=ZERO
    for x in xs: ans=add(ans,x)
    return ans
def jmul(a,b):
    return tuple(sumgauss([mul(a[k],b[r-k]) for k in range(r+1)]) for r in range(J))
def jinv(a):
    out=[div(ONE,a[0])]
    for r in range(1,J):
        out.append(neg(div(sumgauss([mul(a[k],out[r-k]) for k in range(1,r+1)]),a[0])))
    return tuple(out)

def base(): return [J1]+[J0]*N
def invfac(arr,d,e):
    q=qjet(e)
    out=list(arr)
    for k in range(d,N+1): out[k]=jadd(out[k],jmul(q,out[k-d]))
    return out
def mulfac(arr,d,e):
    q=qjet(e)
    out=list(arr)
    for k in range(d,N+1): out[k]=jsub(arr[k],jmul(q,arr[k-d]))
    return out
def pm(arr,terms):
    for d,e,v in terms: arr=invfac(arr,d,e) if v==1 else mulfac(arr,d,e)
    return arr
def conmul(arr,c): return [jmul(x,c) for x in arr]
def sumarr(terms):
    ans=[J0]*(N+1)
    for a in terms: ans=[jadd(x,y) for x,y in zip(ans,a)]
    return ans
def minusarr(a,b): return [jsub(x,y) for x,y in zip(a,b)]
def zshare(a): return [J0]+a[:-1]
def jH(s): return zshare(pm(base(),[(1,0,1)]+[(1,p,1) for p in s]))
def M(a,b): return pm(base(),[(1,a,1),(1,b,1),(1,a+b,1),(2,a+b,-1)])
def V(a,b,c): return pm(base(),[(2,a+b+c,1),(1,a,1),(1,b,1),(1,c,1),(3,a+b+c,-1)])
def S(a,b,c):
    return minusarr(sumarr([invfac(M(b,c),1,a),invfac(M(a,c),1,b),invfac(M(a,b),1,c)]),V(a,b,c))
def Hh():
    vals=[]
    for r in (219,220,221):
        zc=J1
        for t in (219,220,221):
            if t!=r: zc=jmul(zc,jinv(jsub(J1,qjet(t-r))))
        vals.append(conmul(S(214,215,r),zc))
    return zshare(pm(sumarr(vals),[(1,0,1)]+[(1,p,1) for p in range(216,219)]))

def bc_free(E):
    b,c=ZERO,ZERO
    for p in E:
        if p%4==0:
            u=(Q(p-1,2),Q(0))
            v=add(mul(u,u),(-Q((p-1)*(p-2),6),Q(0)))
        else:
            w=ii(p)
            ratio=div(w,sub(ONE,w))
            u=scale(ratio,-p)
            v=add(mul(u,u),scale(ratio,Q(p*(p-1),2)))
        c=add(c,add(v,mul(b,u)))
        b=add(b,u)
    return b,c

hs=[jH(S0),jH(S1),jH(S2),Hh()]
bs=[bc_free(e) for e in (E0,E1,E2,Eh)]
lams=[(Q(1),Q(0)),(Q(220),Q(-220)),(Q(220),Q(0)),(Q(-440),Q(0))]
vals=[]
for m in range(N+1):
    h=[x[m] for x in hs]
    v=[ZERO]*4
    for hh,(b,c),lam,order in zip(h,bs,lams,[24,23,23,23]):
        for r in range(4):
            value=hh[r]
            if r>=1: value=add(value,mul(b,hh[r-1]))
            if r>=2: value=add(value,mul(c,hh[r-2]))
            if order-r>=21: v[24-order+r]=add(v[24-order+r],mul(lam,value))
    D,L,Ms=v[1:4]
    vals.append(add(add(Ms,scale(L,11)),scale(D,Q(391,6))))

regression={
 2:(48482836880,-353679803),4:(62305047576,26697661156),
 6:(139491897968,-937930390),8:(161213561320,62200887820),
 10:(250809507200,-1708202337),12:(275603223472,93146912664),
 14:(364816103520,-2614103020),16:(388967996240,110700698600),
 18:(468491838960,-3564664775),20:(489385674440,110556536860),
 22:(553414980560,-4458507778),24:(569545763896,92936448916)}
for m,z in regression.items(): assert vals[m]==(Q(z[0]),Q(z[1])),(m,vals[m],z)
assert vals[0]==ZERO
v=[vals[2*k] for k in range(N//2+1)]

def boosted(k,L=11):
    ans=ZERO
    for j in range(L+1):
        if k-4*j>=0: ans=add(ans,scale(v[k-4*j],(-1)**j*comb(L,j)))
    return ans
num=[boosted(k) for k in range(44)]
assert all(boosted(k)==ZERO for k in range(44,len(v)))

P_coeff=[
 (0,0),(48482836880,-353679803),(61597687970,-70268012604),
 (-98009801000,-123425946724),(-210955786886,107859493748),
 (-1474163328,299237536078),(241786872358,44049730764),
 (80918962488,-184532034052),(-92380070722,-90839040004),
 (-20860776480,-123703595)]
import sympy as sy
t=sy.Symbol('t')
I=sy.I
q=lambda g: sy.Rational(g[0].numerator,g[0].denominator)+I*sy.Rational(g[1].numerator,g[1].denominator)
Ppoly=sum((a+I*b)*t**k for k,(a,b) in enumerate(P_coeff))
factor=(1-t*t)**6*(1-I*t)**9*(1+I*t)**11
expected=sy.Poly(sy.expand(Ppoly*factor),t,extension=I)
assert all(sy.simplify(expected.nth(k)-q(num[k]))==0 for k in range(44))
assert expected.degree()==41
R=sy.cancel(Ppoly/(1-t*t)**5)
C=sy.simplify(R.subs(t,-I))
B=sy.simplify(I*sy.diff(R,t).subs(t,-I))
assert C==-71390 and B==1442320-49940*I

out={
 'schema':'R5_QI_N20_EVEN_T_GENERATOR_EXACT_V1',
 'source_pin_sha256':'50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b',
 'jet_order_in_s':3,'z_max':N,
 'generator':{'numerator_ascending':[{'re':a,'im':b} for a,b in P_coeff],
              'denominator':'(1-t^2)^5*(1-i*t)^2','t':'t=z^2, m=2k'},
 'primitive_pole':{'location':'t=-i','double':-71390,'simple':{'re':1442320,'im':-49940}},
 'regressions':list(regression),'regression':'PASS',
 'rational_bound':'Denominator divides (1-t^4)^11; proper generating function',
 'coefficients_checked':len(v),'determining_coefficients':44,
 'new_samples':{'m26':{'re':int(v[13][0]),'im':int(v[13][1])},
                'm28':{'re':int(v[14][0]),'im':int(v[14][1])}},
 'status':'AUTHOR_SYMBOLIC_DERIVATION_EXACT_RATIONAL_CHECKED_NOT_REVIEWED'}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS: 12 prior DP regressions, 44 exact rational coefficients, 5 holdouts, primitive double-pole certificate')
