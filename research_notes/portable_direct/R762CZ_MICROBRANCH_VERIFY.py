"""R762CZ: exact microbranch-ID versus directional-window observation checks."""
from math import gcd
from functools import reduce
from itertools import product
from collections import defaultdict
import json

def counts(p,q,h):
    v=(1,0,0); a=[v]
    for _ in range(h):
        w=[0]*3
        for i,n in enumerate(v):
            w[(i+1)%3]+=p*n; w[(i-1)%3]+=q*n
        v=tuple(w);a.append(v)
    return a

def cvg(v): return reduce(gcd,v,0)
def step(i,branch,p): return (i+1)%3 if branch < p else (i-1)%3

def window_edges(p,q,C,h,r):
    D=p+q;g=cvg(C[h-r]);M=D**h//g
    layers=[];assert M*g==D**h
    for t in range(h-r+1):
        e={}
        for i in range(3):
            for word in product(range(D),repeat=r):
                numerator=M*C[t][i];denominator=D**(t+r)
                assert numerator%denominator==0,(p,q,h,r,t,i,word)
                cnt=numerator//denominator
                if cnt:e[(i,)+word]=cnt
        assert sum(e.values())==M
        layers.append(e)
    return M,layers

def src(e,p): return e[:-1]
def dst(e,p): return (step(e[0],e[1],p),)+e[2:]

def check_flow(p,q,h,r,layers,decompose=False):
    for t in range(1,len(layers)):
        out=defaultdict(int);incoming=defaultdict(int)
        for e,n in layers[t].items():out[src(e,p)]+=n
        for e,n in layers[t-1].items():incoming[dst(e,p)]+=n
        assert incoming==out,(p,q,h,r,t)
    if decompose:
        ed=[dict(l) for l in layers];paths=defaultdict(int);M=sum(ed[0].values())
        while ed[0]:
            e=next(iter(ed[0])); initial=e[0];branchids=list(e[1:])
            ed[0][e]-=1
            if ed[0][e]==0:del ed[0][e]
            for t in range(1,len(ed)):
                state=initial
                for b in branchids[:t]:state=step(state,b,p)
                node=(state,)+tuple(branchids[t:t+r-1])
                choices=[w for w,n in ed[t].items() if n and src(w,p)==node]
                assert choices,(p,q,h,r,t,node)
                w=choices[0]
                branchids.append(w[-1])
                ed[t][w]-=1
                if ed[t][w]==0:del ed[t][w]
            paths[(initial,tuple(branchids))]+=1
        assert sum(paths.values())==M
        for t,layer in enumerate(layers):
            c=defaultdict(int)
            for (i,words),m in paths.items():
                state=i
                for b in words[:t]:state=step(state,b,p)
                key=(state,)+words[t:t+r]
                c[key]+=m
            assert c==layer,(p,q,h,r,t)

def run():
    s=dict(schema='R762CZ_MICROBRANCH_EVIDENCE_V1',domain={'p_q':'1..4, including non-coprime','h':'0..5','r':'0..h'},tests=dict(weight_pairs=0,window_cases=0,integral_event_assertions=0,flow_overlap_layers=0,explicit_path_decompositions=0,ratio_assertions=0),examples={})
    z=s['tests']
    for p in range(1,5):
        for q in range(1,5):
            z['weight_pairs']+=1;D=p+q;g=gcd(p,q);pn=p//g;qn=q//g;Cn=counts(pn,qn,5);C=counts(p,q,5)
            for h in range(6):
                for r in range(h+1):
                    z['window_cases']+=1
                    Mm=D**h//cvg(C[h-r]);Mc=(pn+qn)**h//cvg(Cn[h-r])
                    assert Mm==g**r*Mc
                    z['ratio_assertions']+=1
                    for t in range(h-r+1):
                        for i in range(3):
                            assert Mm*C[t][i]%(D**(t+r))==0
                            z['integral_event_assertions']+=1
                    if r>=1:
                        m,layers=window_edges(p,q,C,h,r)
                        assert m==Mm
                        check_flow(p,q,h,r,layers,decompose=(h<=3 and D<=6))
                        z['flow_overlap_layers']+=len(layers)-1
                        if h<=3 and D<=6:z['explicit_path_decompositions']+=1
    for p,q,h in [(2,4,5),(2,2,5),(1,2,5),(4,4,5)]:
        D=p+q;g=gcd(p,q);C=counts(p,q,h);Cp=counts(p//g,q//g,h)
        s['examples'][f'p={p},q={q},h={h}']={'coarse':[ ((D//g)**h)//cvg(Cp[h-r]) for r in range(h+1)],'micro':[ D**h//cvg(C[h-r]) for r in range(h+1)]}
    print(json.dumps(s,indent=2))
if __name__=='__main__':run()
