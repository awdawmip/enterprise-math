"""Fraction-free exact Q dynamic basis over every signed X6 path, no modular inference.
At fixed (z,q) all continuations act on the 3 BRC/count weights by the same diagonal map;
therefore retaining a Z-linear-independent sample basis spans all reachable weight triples over Q.
"""
import json, time
from pathlib import Path
from collections import defaultdict
from sympy import Matrix
from VERIFY_EC49CR import suffixes, row_rank_q, summary
from VERIFY_EC49CJ import advance, follow, label, displacement, weight, W, Z, reach_back


def det(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

def insert(b,vec,path):
    if not b: b.append((vec,path));return True
    a=b[0][0]
    if len(b)==1:
        if any(a[i]*vec[j]!=a[j]*vec[i] for i in range(3) for j in range(i+1,3)):
            b.append((vec,path));return True
        return False
    if len(b)==2:
        if det(a,b[1][0],vec):b.append((vec,path));return True
        return False
    return False

def gen(n,targets):
    state={(Z,0):[((1,1,1),())]}
    for t in range(n):
        nxt={}
        for (z,q),samples in state.items():
            for sign in (+1,-1):
                for i in range(6):
                    zz=list(z);zz[i]+=sign;zz=tuple(zz)
                    if not reach_back(zz,n-t-1,targets):continue
                    a=sign*(i+1);qq=advance(q,a);key=(zz,qq)
                    dst=nxt.setdefault(key,[])
                    for vec,path in samples:
                        ww=(vec[0]*(W[0][i] if sign>0 else 1),vec[1]*(W[1][i] if sign>0 else 1),vec[2])
                        insert(dst,ww,path+(a,))
        state=nxt
    return state

def rank(n,sufs):
    d=summary(sufs)
    groups=d['fibers'];targets=[tuple(f['target']) for f in groups];t0=time.monotonic()
    states=gen(n,targets);table=[]
    for f in groups:
        tar=tuple(f['target']); bases=[(s,vec) for q in range(9) for vec,s in states.get((tar,q),[])]
        rows=[]
        for suffix,labelno in f['basis_readouts']:
            s=sufs[suffix];ww=weight(s)
            for k in range(3):
                rows.append([v[k]*ww[k] if label(follow(follow(0,p),s))==labelno else 0 for p,v in bases])
        rr=Matrix(rows).rank() if rows and bases else 0
        table.append({'target':list(tar),'formal':3*f['rational_per_type_rank'],'actual_Q_rank':rr,'candidate_paths':len(bases)})
    return {'n':n,'formal_rank':d['three_channel_formal_rank'],
            'exact_rational_rank':sum(a['actual_Q_rank'] for a in table),
            'fibers':table,'runtime_s':round(time.monotonic()-t0,3),'final_typed_states':len(states)}

if __name__=='__main__':
    ss=suffixes(1,2);out=[]
    for n in (4,6,8,10,12):
        r=rank(n,ss);out.append(r)
        print(n,r['exact_rational_rank'],'/',r['formal_rank'],'seconds',r['runtime_s'],flush=True)
        if n>=10:print('missing',[(v['target'][:2],v['actual_Q_rank'],v['formal']) for v in r['fibers'] if v['formal']!=v['actual_Q_rank']],flush=True)
    (Path(__file__).parent/'RATIONAL_RANK_EC49CR.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
