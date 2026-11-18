"""EC49CE portable exact check; native signed BRC, no physical dynamics.
Python 3.11+ standard library; run from EC49CE_STABILIZER_TRANSFER directory.
"""
import json,sys
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P if (P/'native_signed_brc.py').exists() else P.parent/'EC49CA_CRT'))
from native_signed_brc import endpoint_weight,endpoint_multiplicity
S=(1,2,3,4,5,6,-6,-5,-4,-3,-2,-1)
W0=(2,3,3,2,1,1);W1=(3,2,3,2,1,1);Z=(0,)*6
G=((0,0),(1,0),(0,1),(1,1))
def mul(g,h):return(g[0]^h[0],g[1]^h[1])
def move(a,g):
    i=abs(a);v=1 if a>0 else -1
    if g[0] and i in (1,2):i=3-i
    if g[1] and i in (5,6):i=11-i
    return v*i
def dfa(q,a):
    return 2 if q==2 or (q==1 and a==2) else int(a==1)
SW=tuple((q%3)*3+q//3 for q in range(9))
ATOM=tuple(2*(q//3==2)+(q%3==2) for q in range(9))
D=tuple(tuple(3*dfa(q//3,a)+dfa(q%3,move(a,(1,0))) for a in S) for q in range(9))
WEIGHTS={a:((W0[a-1],W1[a-1],1) if a>0 else (1,1,1)) for a in S}
def act(k,g):
    z,q=k
    if g[0]:z=(z[1],z[0],z[2],z[3],z[4],z[5]);q=SW[q]
    if g[1]:z=z[:4]+(z[5],z[4])
    return z,q
def canon(k):return min(act(k,g) for g in G)
def step(k,a):
    z,q=k;i=abs(a)-1
    return z[:i]+(z[i]+(1 if a>0 else -1),)+z[i+1:],D[q][S.index(a)]
def norm(k):return sum(map(abs,k[0]))
def lift(k,v):
    out={}
    for g in G:
        y=act(k,g);w=(v[1],v[0],v[2]) if g[0] else v
        assert y not in out or out[y]==w
        out[y]=w
    return out
def add(out,k,v):
    x=out.get(k,(0,0,0));out[k]=(x[0]+v[0],x[1]+v[1],x[2]+v[2])
def full(src,rem):
    out={}
    for k,v in src.items():
        for a in S:
            y=step(k,a)
            if norm(y)>rem:continue
            w=WEIGHTS[a];add(out,y,(w[0]*v[0],w[1]*v[1],v[2]))
    return out
def compile_from(r):
    assert canon(r)==r
    Hr={g for g in G if act(r,g)==r}
    seen=set();out={}
    for a in S:
        if a in seen:continue
        seen.update(move(a,h) for h in Hr)
        y=step(r,a);d=canon(y)
        k=next(g for g in G if act(y,g)==d)
        Hd={h for h in G if act(d,h)==d}
        E={h for h in Hr if move(a,h)==a}
        assert E<=Hd
        visited=set();m=out.setdefault(d,[0,0,0,0,0]);w=WEIGHTS[a]
        for h in sorted(Hd):
            if h in visited:continue
            visited.update(mul(h,e) for e in E)
            g=mul(h,k)
            if g[0]:m[1]+=w[1];m[2]+=w[0]
            else:m[0]+=w[0];m[3]+=w[1]
            m[4]+=1
        assert visited==Hd
    return tuple((d,tuple(m)) for d,m in out.items())
def compiled(src,rem):
    out={}
    for r,v in src.items():
        for d,m in compile_from(r):
            if norm(d)>rem:continue
            add(out,d,(m[0]*v[0]+m[1]*v[1],m[2]*v[0]+m[3]*v[1],m[4]*v[2]))
    return out
def terminal(states):
    rows=[[0,0,0] for _ in range(4)]
    for (z,q),v in states.items():
        assert z==Z
        for i in range(3):rows[ATOM[q]][i]+=v[i]
    return rows
rows=[]
for n in (0,2,4,6,8,10,12,14):
    f={(Z,0):(1,1,1)};c=dict(f)
    for j in range(n+1):
        rebuilt={}
        for k,v in c.items():
            for y,w in lift(k,v).items():
                assert y not in rebuilt
                rebuilt[y]=w
        assert rebuilt==f,(n,j)
        if j==n:break
        f=full(f,n-j-1);c=compiled(c,n-j-1)
    w=int(endpoint_weight(n,Z,W0,(1,)*6));m=endpoint_multiplicity(n,Z)
    t=terminal(f)
    assert [sum(row[i] for row in t) for i in range(3)]==[w,w,m]
    rows.append({'n':n,'native_weight':w,'native_closed_count':m,
                 'final_atom_channels':t,'all_layers_exact':True})
print('PASS_EC49CE_PORTABLE',len(rows))
(P/'EXACT_REPORT_EC49CE_PORTABLE.json').write_text(json.dumps(rows,indent=2,sort_keys=True)+'\n')
