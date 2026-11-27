from fractions import Fraction as F
from math import gcd,ceil,floor
from itertools import product
import json,hashlib
from pathlib import Path
G=10**85; E=400000
raw=Path('root_8800_result.json').read_bytes(); assert hashlib.sha256(raw).hexdigest()=='367ed5c982ef92405623cfe6633aa29ce1449bfa2e1cb2e355fd8692d84355a9'
new=Path('root_9200_only.json').read_bytes(); assert hashlib.sha256(new).hexdigest()=='b17b098179d915eabbdefc8f6050a8d401e06731a59e7f130350ce6aaab1948f'
D=json.loads(raw); R=tuple(F(int(v),G) for v in json.loads(new)['rho']); C,T=[tuple(F(int(v),G) for v in D[k]) for k in ('c','d')]
V=((13241695572016246280452795405,-614903515325433031059117378,-586453816401334287434546),(1182616791650392258028253444,-74796824988556406807726418,4246778208283374384362279),(-7752265403315380654172299023,382363756442351370763912993,-4494886358260478563501531))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
W=tuple(zip(cross(V[1],V[2]),cross(V[2],V[0]),cross(V[0],V[1])))
assert tuple(tuple(dot(v,w) for w in zip(*W)) for v in V)==((1,0,0),(0,1,0),(0,0,1))
q0=544447235321021556325566186117974922693
q1=25525828069781181809194072375836326527854111431881463
K=T[1]+F(2*E,q0); H=2*T[1]+F(4*E,q0)
assert q0>16*E/T[0]
# Pair identities with e=f-j: delta=d/(ab)+(e_b-e_a)/(b-a), gamma=-d(1/a+1/b)+(be_a-ae_b)/(b-a).
# |gamma error| <= E*(a+b)/(L^2*(b-a)) <4E/(q L). Signed for q>=q0.
def scan(L,Q=q1,local=False):
    k=T[0]/4-F(2*E,q0); h=T[0]-F(4*E,q0)
    assert k>0 and h>0
    r=(R[0]-K/L**2,R[1]-(k/L**2 if local else 0)); c=(C[0]+(h/L if local else 0),C[1]+H/L)
    ineq=[((1,0,0),Q),((-1,0,0),-q0),((r[0],-1,0),0),((-r[1],1,0),0),((c[0],0,-1),0),((-c[1],0,1),0)]
    ranges=[]
    for a,b,c0 in V:
        vals=[q*(a+b*rr+c0*cc) for q,rr,cc in product((q0,Q),r,c)]
        ranges.append((ceil(min(vals)),floor(max(vals))))
    # permute coordinates to enumerate smallest two ranges
    idx=sorted(range(3),key=lambda i:ranges[i][1]-ranges[i][0]); X,Y,Z=idx
    lin=[(tuple(dot(v,w) for w in zip(*W)),F(z)) for v,z in ineq]
    ans=[]; loops=0
    for i in range(ranges[X][0],ranges[X][1]+1):
      for j in range(ranges[Y][0],ranges[Y][1]+1):
        loops+=1; lo,hi=ranges[Z]
        for abc,z in lin:
            t=z-abc[X]*i-abc[Y]*j; a=abc[Z]
            if a>0:hi=min(hi,floor(t/a))
            elif a<0:lo=max(lo,ceil(t/a))
            elif t<0:lo,hi=1,0;break
            if lo>hi:break
        for k in range(lo,hi+1):
            n=[0]*3;n[X]=i;n[Y]=j;n[Z]=k
            v=tuple(dot(w,n) for w in W)
            assert all(dot(a,v)<=b for a,b in ineq)
            if gcd(v[0],v[1])==1:ans.append(v)
    return sorted(ans),ranges,loops
def witness(L,line):
    q,p,h=line; d=sum(T)/2; r=F(p,q); c=F(h,q)
    res=(-h*pow(p,-1,q))%q
    a0=L+(res-L)%q; last=2*L-q-1
    lo,hi=0,(last-a0)//q
    if hi<0:return None
    def at(n):
        a=a0+n*q; b=a+q
        return a,b,r+d/(a*b),c-d*(F(1,a)+F(1,b))
    # Both c>=C_l and rho<=R_u are monotone in a.
    while lo<hi:
        mid=(lo+hi)//2; a,b,rho,cc=at(mid)
        if rho<=R[1] and cc>=C[0]:hi=mid
        else:lo=mid+1
    a,b,rho,cc=at(lo)
    if not (R[0]<=rho<=R[1] and C[0]<=cc<=C[1]):return None
    assert L<=a<b<2*L and b-a==q
    for m in (a,b):
        assert (p*m+h)%q==0
        assert rho*m+cc+d/m==F(p*m+h,q)
    return dict(a=a,b=b,rho=str(rho),c=str(cc),d=str(d))
if __name__=='__main__':
    M=16225927682921336339157801028812800000000
    # independently verify inherited all-future small-q exclusion on the smaller box
    P=72486411641368782354423090020719211170157; Qw=3380890274893182433251695995418378677023
    assert gcd(P,Qw)==1 and Qw>q0-1
    eta=max(abs(r-F(P,Qw)) for r in R)
    margin=F(1,Qw)-(q0-1)*eta-(T[1]*(q0-1)+2*E)/M**2
    assert margin>0
    L0=10**8
    while L0<4*10**76:L0*=2
    ans,rs,loops=scan(L0); assert len(ans)==1 and ans[0][0]==q1
    line=ans[0]; assert R[0]<F(line[1],q1)<R[1] and C[0]<F(line[2],q1)<C[1]
    print('tail minimum',L0,line,rs,loops,'small q margin',float(margin),flush=True)
    results=[]
    for i in range(5):
        L=L0*2**i
        a,rs,n=scan(L,10**53,True)
        w=witness(L,a[0]) if a else None
        print('local',i,float(L),len(a),a[0][0] if a else None,bool(w),rs,n,flush=True)
        results.append(dict(L=L,Q=10**53,count=len(a),minimum=a[0] if a else None,ranges=rs,loops=n,witness=w))
    Ltail=L0*16; q,p,h=line; d=sum(T)/2
    # For each integer L>=Ltail choose greatest a congruent to res with a+q<2L.
    # Then a>=2L-2q, so c' and rho' in frozen box for every such L.
    A=2*Ltail-2*q
    assert A>=Ltail and A>0
    assert F(p,q)+d/A**2<R[1] and F(h,q)-2*d/A>C[0]
    for row in results[:-1]:
        assert not row['minimum'] or row['minimum'][0]>q1
    assert all(row['witness'] for row in results)
    assert results[-1]['minimum']==line
    assert q0*q0>L0
    first=10**8
    while first<q1*q1:first*=2
    assert first>=Ltail and first//2<q1*q1<=first
    wfirst=witness(first,line);assert wfirst
    second=F(first**3)/(9*T[1]/8)**2
    print('sqrt-pair first',first,'second distinct lower (exact rational in JSON)',flush=True)
    out=dict(source_hashes=[hashlib.sha256(raw).hexdigest(),hashlib.sha256(new).hexdigest()],q0=q0,small_q_margin=str(margin),L0=L0,tail_minimum=line,tail_ranges=scan(L0)[1],tail_loops=scan(L0)[2],local=results,Ltail=Ltail,first_sqrt_pair=first,first_sqrt_pair_witness=wfirst,second_distinct_lower=str(second),witness_rho_margin=str(R[1]-F(p,q)-d/A**2),witness_c_margin=str(F(h,q)-2*d/A-C[0]))
    Path('pair_result.json').write_text(json.dumps(out,indent=2)+'\n')
