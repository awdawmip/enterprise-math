"""EC49CC: full-vector orbit equivariance of finite-field BRC spectral filter.
Inputs: native signed X6, positive (2,3,3,2,1,1), negative all one;
observer: whether ordered patterns (+1,+2) and (+2,+1) occur.
H=<swap 1 2>. Exact author-side finite audit; not physical dynamics.
"""
import itertools
import json
import time
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
SOURCE_OPTIONS=(HERE.parent/'EC49CA_CRT'/'native_signed_brc.py',
                HERE/'native_signed_brc.py', HERE/'EC49CB'/'native_signed_brc.py',
                HERE.parent/'EC49CB'/'native_signed_brc.py')
for f in SOURCE_OPTIONS:
    if f.exists():
        sys.path.insert(0,str(f.parent));break
else: raise FileNotFoundError('Pinned native_signed_brc.py required')
from native_signed_brc import endpoint_weight, endpoint_multiplicity

S=(1,2,3,4,5,6,-6,-5,-4,-3,-2,-1)
W=(2,3,3,2,1,1)
WC=(3,2,3,2,1,1)
Z=(0,)*6
LAB=('00','01','10','11')

def sw(a):
    if abs(a)==1:return 2 if a>0 else -2
    if abs(a)==2:return 1 if a>0 else -1
    return a

def nxt(q,a):
    if q==2:return 2
    if q==1 and a==2:return 2
    return 1 if a==1 else 0

TRANS=tuple(tuple(3*nxt(q//3,a)+nxt(q%3,sw(a)) for a in S) for q in range(9))
ATOM=tuple(2*(q//3==2)+(q%3==2) for q in range(9))
SWAPATOM=(0,2,1,3)
SWAPCHANNEL=(1,0,2)

def prime(p):
    return p>1 and all(p%d for d in range(2,int(p**.5)+1))

def spectral(n,L,p,group="K"):
    assert n%2==0 and L%2==1 and 2*L>n
    assert prime(p) and (p-1)%L==0 and p>int(endpoint_weight(n,Z,W,(1,)*6))
    w=next(pow(g,(p-1)//L,p) for g in range(2,200)
           if pow(g,(p-1)//L,p)!=1)
    assert pow(w,L,p)==1
    roots=tuple(pow(w,e,p) for e in range(L))
    invroots=tuple(roots[(-e)%L] for e in range(L))
    total=[[0,0,0] for _ in LAB]
    evals=0;fixed=0;pair=0
    def points():
        if group=="K":
            for e1 in range(L):
                for e2 in range(e1,L):
                    for e3,e4 in itertools.product(range(L),repeat=2):
                        for e5 in range(L):
                            for e6 in range(e5,L):
                                yield (e1,e2,e3,e4,e5,e6)
        elif group=="H":
            for e1 in range(L):
                for e2 in range(e1,L):
                    for suffix in itertools.product(range(L),repeat=4):
                        yield (e1,e2)+suffix
        elif group=="FULL":
            yield from itertools.product(range(L),repeat=6)
        else: raise ValueError("unknown group")
    t0=time.perf_counter()
    for es in points():
        x=[roots[e] for e in es]
        y=[invroots[e] for e in es]
        weight=[(W[j]*x[j]%p,WC[j]*x[j]%p,x[j]) for j in range(6)]
        weight += [(y[j],y[j],y[j]) for j in (5,4,3,2,1,0)]
        val=[[0,0,0] for _ in range(9)];val[0]=[1,1,1]
        for _ in range(n):
            new=[[0,0,0] for _ in range(9)]
            for q,(v0,v1,v2) in enumerate(val):
                if not (v0 or v1 or v2):continue
                for j,qt in enumerate(TRANS[q]):
                    d=new[qt];w0,w1,w2=weight[j]
                    d[0]=(d[0]+v0*w0)%p
                    d[1]=(d[1]+v1*w1)%p
                    d[2]=(d[2]+v2*w2)%p
            val=new
        atom=[[0,0,0] for _ in LAB]
        for q,v in enumerate(val):
            d=atom[ATOM[q]]
            for j in range(3):d[j]=(d[j]+v[j])%p
        # The 5<->6 swap fixes the entire output fiber and doubles a nonfixed orbit.
        factor=2 if group=="K" and es[4]!=es[5] else 1
        if group!="FULL" and es[0]!=es[1]:
            pair+=1
            for a in range(4):
                d=total[a];v=atom[a];s=atom[SWAPATOM[a]]
                for c in range(3):d[c]=(d[c]+factor*(v[c]+s[SWAPCHANNEL[c]]))%p
        else:
            if group!="FULL":fixed+=1
            for a in range(4):
                d=total[a];v=atom[a]
                for c in range(3):d[c]=(d[c]+factor*v[c])%p
            if group!="FULL" and es[0]==es[1]:
                for a in range(4):
                    for c in range(3):
                        assert atom[a][c]==atom[SWAPATOM[a]][SWAPCHANNEL[c]]
        evals+=1
    scale=pow(pow(L,6,p),-1,p)
    ans=[[v*scale%p for v in row] for row in total]
    return {'atoms':ans,'evaluations':evals,'fixed':fixed,'pairs':pair,
            'root_points':L**6,'prime':p,'omega':w,'group':group,
            'seconds':round(time.perf_counter()-t0,4)}

def exact_dp(n):
    t0=time.perf_counter()
    states={(Z,0):(1,1,1)}
    peak=1
    for t in range(n):
        out={}
        for (z,q),v in states.items():
            for j,a in enumerate(S):
                axis=abs(a)-1
                zz=z[:axis]+(z[axis]+(1 if a>0 else -1),)+z[axis+1:]
                if sum(map(abs,zz))>n-t-1:continue
                key=(zz,TRANS[q][j]);u=out.get(key,(0,0,0))
                weights=(W[axis],WC[axis],1) if a>0 else (1,1,1)
                out[key]=tuple(u[c]+v[c]*weights[c] for c in range(3))
        states=out;peak=max(peak,len(out))
    atom=[[0,0,0] for _ in LAB]
    for (z,q),v in states.items():
        if z!=Z:continue
        d=atom[ATOM[q]]
        for c in range(3):d[c]+=v[c]
    native=(int(endpoint_weight(n,Z,W,(1,)*6)),endpoint_multiplicity(n,Z))
    assert [sum(atom[a][c] for a in range(4)) for c in range(3)]==[native[0],native[0],native[1]]
    return {'atoms':atom,'peak_states':peak,'native_weight':native[0],
            'native_count':native[1],'seconds':round(time.perf_counter()-t0,4)}

def alias_witness():
    L=5;p=11;w=3
    assert pow(w,5,p)==1 and w!=1
    base=sum(W)+6
    x0=(base+(w-1)*W[0]+(pow(w,-1,p)-1))%p
    x1=(base+(w-1)*W[1]+(pow(w,-1,p)-1))%p
    assert (x0,x1,x0*x0%p,x1*x1%p)==(3,5,9,3)
    return {'p':p,'L':L,'root':w,'e':(1,0,0,0,0,0),
            'transformed_e':(0,1,0,0,0,0),'P_values':[x0,x1],
            'squared_unfiltered_integrands':[x0*x0%p,x1*x1%p]}

def verify():
    cases=[]
    for n,L,p in ((4,3,1000000000177),(8,5,1000000000211),
                  (10,7,1000000000189)):
        dp=exact_dp(n)
        f=spectral(n,L,p,group="K")
        assert f['atoms']==dp['atoms']
        assert f['evaluations']==L**4*(L+1)**2//4
        # A second independent orbit partition H=<swap(1,2)> checks K at n<=8.
        h=spectral(n,L,p,group="H") if n<=8 else None
        if h:
            assert h['atoms']==dp['atoms']
            assert h['evaluations']==(L**6+L**5)//2
        # Full-grid transfer without symmetry is cross-checked at n=4.
        full=spectral(n,L,p,group="FULL") if n==4 else None
        if full: assert full['atoms']==dp['atoms']
        cases.append({'n':n,'L':L,'prime':p,
                      'orbit_K':f,'orbit_H':h,'integer_dp':dp,
                      'full_grid_check':full})
    record={'schema':'EC49CC_ORBIT_SPECTRAL_EXACT_V1',
            'status':'AUTHOR_EXACT_FINITE_AUDIT / UNREVIEWED / NOT_ADMITTED',
            'scope':'ordered signed X6 closed paths; 9-state DFA of A=(+1,+2), B=(+2,+1); 3 BRC channels',
            'native_blob':'300a96e3dc24bf6fff73743037a0347a8bc83176',
            'group':'K=<swap(axes 1,2), swap(axes 5,6)>; first atom bits/channel 0,1 swap; second acts trivially',
            'theorem':'F(swap12-root)=T F(root); F(swap56-root)=F(root); entire 4x3 vector orbit-sums',
            'alias_example':alias_witness(),'cases':cases}
    (HERE/'EXACT_REPORT_EC49CC.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print('EC49CC_PASS',[(c['n'],c['orbit_K']['evaluations'],
                           c['orbit_K']['root_points'],
                           c['integer_dp']['native_weight']) for c in cases])
    return record

if __name__=='__main__':verify()
