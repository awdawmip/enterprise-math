"""Executed exact EC49CD condensed reproduction, Python 3.11+ standard library.
Native signed-X6 BRC source is the unchanged EC49CA_CRT/native_signed_brc.py.
"""
import json,sys
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str((P/'EC49CA_CRT') if (P/'EC49CA_CRT').exists() else (P.parent/'EC49CA_CRT')))
from native_signed_brc import endpoint_weight,endpoint_multiplicity
S=(1,2,3,4,5,6,-6,-5,-4,-3,-2,-1)
WP=((2,3,3,2,1,1),(3,2,3,2,1,1))
Z=(0,)*6

def step(q,a):
    if q==2 or (q==1 and a==2):return 2
    return int(a==1)
def sw(a):return ((2 if abs(a)==1 else 1)* (1 if a>0 else -1)) if abs(a) in (1,2) else a
T=tuple(tuple(3*step(q//3,a)+step(q%3,sw(a)) for a in S) for q in range(9))
AQ=tuple((q%3)*3+q//3 for q in range(9))
A=tuple(2*(q//3==2)+(q%3==2) for q in range(9))
W=tuple((WP[0][a-1],WP[1][a-1],1) if a>0 else (1,1,1) for a in S)

def act(key,s,t):
    z,q=key
    if s:z=(z[1],z[0],z[2],z[3],z[4],z[5]);q=AQ[q]
    if t:z=(z[0],z[1],z[2],z[3],z[5],z[4])
    return z,q

def canon(key):
    z,q=key
    return z[4]<=z[5] and (z[0]<z[1] or (z[0]==z[1] and q<=AQ[q]))

def orbit(key,v):
    out={}
    for s,t in ((0,0),(1,0),(0,1),(1,1)):
        y=act(key,s,t);value=(v[1],v[0],v[2]) if s else v
        assert y not in out or out[y]==value
        out[y]=value
    return out

def advance(states,remain,compressed):
    out={}
    for key,v in states.items():
        for (z,q),value in (orbit(key,v).items() if compressed else ((key,v),)):
            for j,a in enumerate(S):
                i=abs(a)-1;zz=z[:i]+(z[i]+(1 if a>0 else -1),)+z[i+1:]
                if sum(map(abs,zz))>remain:continue
                y=(zz,T[q][j])
                if compressed and not canon(y):continue
                old=out.get(y,(0,0,0));w=W[j]
                out[y]=(old[0]+w[0]*value[0],old[1]+w[1]*value[1],old[2]+value[2])
    return out

def atoms(states):
    out=[[0,0,0] for _ in range(4)]
    for (z,q),v in states.items():
        assert z==Z
        for k in range(3):out[A[q]][k]+=v[k]
    return out

def measure(states):
    return sum(sum(max(1,x.bit_length()) for x in v) for v in states.values())

result=[]
for n in (0,2,4,6,8,10,12):
    f={(Z,0):(1,1,1)};c=dict(f);sizes_f=[1];sizes_c=[1];bits_f=[3];bits_c=[3]
    for t in range(n+1):
        lifted={}
        for x,v in c.items():
            assert canon(x)
            for y,w in orbit(x,v).items():
                assert y not in lifted
                lifted[y]=w
        assert lifted==f,('intermediate fiber mismatch',n,t)
        fix=[sum(act(x,*g)==x for x in f) for g in ((1,0),(0,1),(1,1))]
        assert len(f)+sum(fix)==4*len(c),('Burnside mismatch',n,t)
        if t==n:break
        f=advance(f,n-t-1,False);c=advance(c,n-t-1,True)
        sizes_f.append(len(f));sizes_c.append(len(c));bits_f.append(measure(f));bits_c.append(measure(c))
    af=atoms(f);ac=atoms(lifted);assert af==ac
    native_w=int(endpoint_weight(n,Z,WP[0],(1,)*6))
    native_c=endpoint_multiplicity(n,Z)
    assert [sum(row[k] for row in af) for k in range(3)]==[native_w,native_w,native_c]
    result.append(dict(n=n,native_weight=native_w,native_count=native_c,
                       peak_full=max(sizes_f),peak_orbit=max(sizes_c),
                       peak_full_bits=max(bits_f),peak_orbit_bits=max(bits_c),atoms=af))
print('PASS_EC49CD_MIN',len(result))
(P/'EXACT_REPORT_EC49CD_MIN.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
