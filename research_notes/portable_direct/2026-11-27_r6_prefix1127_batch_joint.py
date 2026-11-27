# Reuse candidate observer definitions; do not recompute anchor.
from pathlib import Path
exec(Path('candidate_joint.py').read_text().split('tc=rootbox')[0])
import pair as scanmod
import sympy as sy
scanmod.V=tuple(map(tuple,pair['V'])); V=sy.Matrix(scanmod.V);assert abs(V.det())==1
scanmod.W=tuple(tuple(map(int,row)) for row in V.inv().tolist());scanmod.R=(R.a,R.b);scanmod.C=(C.a,C.b)
c0=(C.a+C.b)/2
x=F(floor((T.a+T.b)*G/2),G)
_,_,f,gg,cols=observe(I(x),c0)
# Compress point columns and centers with directed error payments for quick exact comparisons.
rf=rg=F(0);nc=[]
for u,v in cols:
    a=F(floor(u*G),G);b=F(floor(v*G),G);rf+=abs(a-u);rg+=abs(b-v);nc.append((a,b))
a=F(floor(f*G),G);b=F(floor(gg*G),G);rf+=abs(a-f);rg+=abs(b-gg);f,gg=a,b
cols=nc+[(F(ceil(rf*G),G),F(0)),(F(0),F(ceil(rg*G),G))]
D=198/T**2+216/(4-T**2)+216/(16-T**2);Dp=-396/T**3+432*T/(4-T**2)**2+432*T/(16-T**2)**2
alpha=36/T**2-2+(1-T**2/36)*D/2;beta=9/T-T/4
ap=-72/T**3-T*D/36+(1-T**2/36)*Dp/2;bp=-9/T**2-F(1,4)
gp=beta*f3+(bp+alpha-c0)*f2+ap*slope
# Fixed reference projection strips. For any s, at the root G=G-sF.
ss=list(dict.fromkeys([cols[0][1]/cols[0][0],F(0)]+[v/u for u,v in cols if u]))
strips=[]
for s in ss:
    v=gg-s*f;w=sum(abs(b-s*a) for a,b in cols);z=gp-s*slope
    strips.append((s,I(v-w,v+w),z))
# First normal is the dominant shared anchor; exact comparisons only.
def check(line):
    q,p,h=line;rl=max(R.a,F(p,q));ru=min(R.b,F(p,q)+K/L**2);cl=max(C.a,F(h,q)-H/L);cu=min(C.b,F(h,q))
    if rl>ru or cl>cu:return 'marginal',None
    t=rootbox(rl,ru); tl=max(T.a,t.a);tu=min(T.b,t.b)
    if tl>tu:return 'rootbox',None
    dx=I(tl-x,tu-x);target=I(cl-c0,cu-c0)*slope
    ftest=I(f-sum(abs(a) for a,b in cols),f+sum(abs(a) for a,b in cols))+dx*slope
    if ftest.a>0 or ftest.b<0:return 'F',str(min(abs(ftest.a),abs(ftest.b)))
    for i,(s,ab,z) in enumerate(strips):
        out=ab+dx*z
        if out.b<target.a:return f'strip_{i}_below',str(target.a-out.b)
        if out.a>target.b:return f'strip_{i}_above',str(out.a-target.b)
    return 'remaining',None
Q=2*10**59
ans,rs,loops=scanmod.scan(L,Q)
from collections import Counter
counts=Counter();records=[];remaining=[]
for line in ans:
    kind,margin=check(line);counts[kind]+=1;records.append([list(map(str,line)),kind,margin])
    if kind=='remaining':remaining.append(line)
print('scan',len(ans),rs,loops,'classification',counts,flush=True)
print('first remaining',remaining[0] if remaining else None,flush=True)
assert records[0][1]!='remaining'
qnew=remaining[0][0] if remaining else Q+1
first=10**8
while first<=d.a*qnew*qnew/(4*E):first*=2
firstp=10**8
while firstp<qnew*qnew:firstp*=2
print('q lower',qnew,'triple',float(first),'sqrt pair',float(firstp),flush=True)
res=dict(Q=str(Q),L=str(L),V=pair['V'],ranges=rs,loops=loops,counts=dict(counts),q_lower=str(qnew),first_triple=str(first),first_sqrt_pair=str(firstp),x=str(x),c0=str(c0),center=[str(f),str(gg)],cols=[[str(u),str(v)] for u,v in cols],slope=[str(slope.a),str(slope.b)],gp=[str(gp.a),str(gp.b)],strips=[[str(s),str(ab.a),str(ab.b),str(z.a),str(z.b)] for s,ab,z in strips],records=records)
Path('batch_joint_result.json').write_text(json.dumps(res,indent=2)+'\n')
