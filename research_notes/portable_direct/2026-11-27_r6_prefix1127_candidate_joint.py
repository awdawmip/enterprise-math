# Uses exact frozen reconstruction from PREFIX-1126 without anchor rebuilding.
from pathlib import Path
exec(Path('root_joint_compact.py').read_text().split('# Point enclosure')[0])
from itertools import combinations
from math import isqrt
E=400000
old=json.load(open('root_8800_result.json')); D0=10**85
slope=I(*[F(int(v),D0) for v in old['F_jets'][1]])
f2=I(*[F(int(v),D0) for v in old['F_jets'][2]])
f3=I(*[F(int(v),D0) for v in old['F_jets'][3]])
assert slope.b<0
root=json.load(open('root_compact.json'));joint=json.load(open('joint_compact.json'));pair=json.load(open('pair_9600_result.json'))
T=I(*[F(int(v),10**95) for v in root['t']]);R=I(*[F(int(v),10**95) for v in root['rho']]);C=I(*[F(int(v),10**95) for v in joint['c']]);d=I(*[F(int(v),D0) for v in old['d']])
q,p,h=pair['minimum'];q0=544447235321021556325566186117974922693
K=d.b+F(2*E,q0);H=2*d.b+F(4*E,q0)
k=d.a/4-F(2*E,q0);g=d.a-F(4*E,q0);assert k>0 and g>0
# L >= 10^90; use valid enclosing limits for the whole tail.
L=10**90
rl0=F(p,q);ru0=rl0+K/L**2
cl0=F(h,q)-H/L;cu0=F(h,q)
assert R.a<rl0<=ru0<R.b and C.a<cl0<=cu0<C.b
# Interval sqrt enclosure at a much finer grid than root compact.
def rootbox(rl,ru):
    a,b=36/(1+ru),36/(1+rl)
    lo=isqrt(floor(a*G*G));hi=isqrt(floor(b*G*G))+1
    out=I(F(lo,G),F(hi,G));assert out.a**2<=a<=b<=out.b**2;return out
# Exact observer geometry at a specified t interval, c reference.
def observe(t,c0):
    x=F(floor((t.a+t.b)*G/2),G);r=max(x-t.a,t.b-x);xi=I(x)
    D=198/xi**2+216/(4-xi**2)+216/(16-xi**2)
    alpha=36/xi**2-2+(1-xi**2/36)*D/2;beta=9/xi-xi/4
    fval=[horner(p,xi) for p in pp];gval=[beta*horner(dp(p,2),xi)+(alpha-c0)*horner(dp(p,1),xi) for p in pp]
    def tt(j):return sum((abs(a)+rr)*sum(comb(j,k)*rowbound[k]*tr[j-k] for k in range(j+1)) for a,rr,tr in zip(cc,rad,tails))
    fm=[(v.a+v.b)/2 for v in fval];gm=[(v.a+v.b)/2 for v in gval]
    ferr=tt(0)+sum((abs(a)+rr)*(v.b-v.a)/2 for a,rr,v in zip(cc,rad,fval));gerr=beta.mag()*tt(2)+(alpha-c0).mag()*tt(1)+sum((abs(a)+rr)*(v.b-v.a)/2 for a,rr,v in zip(cc,rad,gval))
    cols=[(sum(fm[i]*inv[i][j] for i in range(6)),sum(gm[i]*inv[i][j] for i in range(6))) for j in range(6)]+[(fm[i]*dr[i],gm[i]*dr[i]) for i in range(6)]
    # Propagation rectangle for G'(t), derived on the candidate t interval.
    D=198/t**2+216/(4-t**2)+216/(16-t**2);Dp=-396/t**3+432*t/(4-t**2)**2+432*t/(16-t**2)**2
    alpha=36/t**2-2+(1-t**2/36)*D/2;beta=9/t-t/4
    ap=-72/t**3-t*D/36+(1-t**2/36)*Dp/2;bp=-9/t**2-F(1,4)
    gp=beta*f3+(bp+alpha-c0)*f2+ap*slope
    # Common displacement Taylor transfer: shared mean derivative segment and two axis errors.
    m1=(slope.a+slope.b)/2;m2=(gp.a+gp.b)/2
    cols.append((r*m1,r*m2));ferr+=r*(slope.b-slope.a)/2;gerr+=r*(gp.b-gp.a)/2
    cols += [(ferr,F(0)),(F(0),gerr)]
    f=sum(a*b for a,b in zip(cc,fm));gg=sum(a*b for a,b in zip(cc,gm))
    return x,r,f,gg,cols
# 2D zonotope support test: complete facet normals, exact feasibility of target interval at F=0.
def bound(f,g,cols):
    ss={F(0)}|{v/u for u,v in cols if u}
    def u(s,sg):return sg*(g-s*f)+sum(abs(v-s*u) for u,v in cols)
    assert abs(f)<=sum(abs(u) for u,v in cols), 'F slice empty'
    sh=min(ss,key=lambda s:u(s,1));sl=min(ss,key=lambda s:u(s,-1));return -u(sl,-1),u(sh,1),sl,sh

tc=rootbox(rl0,ru0);assert T.a<=tc.a<=tc.b<=T.b
x,r,f,gg,cols=observe(tc,F(h,q))
lo,hi,sl,sh=bound(f,gg,cols)
# candidate G=(c-h/q)*F' in [0, (-H/L)*slope.a]
needlo=F(0);needhi=-H/L*slope.a
print('candidate conditioned G lo/hi',float(lo),float(hi),'target',float(needlo),float(needhi),flush=True)
# Need not claim exclusion if overlap.
exclude=hi<needlo or lo>needhi
print('excluded',exclude,'slope',float(sl),float(sh),flush=True)
res=dict(q=str(q),p=str(p),h=str(h),L=str(L),rho=[str(rl0),str(ru0)],c=[str(cl0),str(cu0)],t=[str(tc.a),str(tc.b)],x=str(x),r=str(r),f=str(f),g=str(gg),cols=[[str(u),str(v)] for u,v in cols],G_bounds=[str(lo),str(hi)],required_G=[str(needlo),str(needhi)],s=[str(sl),str(sh)],excluded=exclude)
Path('candidate_joint_result.json').write_text(json.dumps(res,indent=2)+'\n')
