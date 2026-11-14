"""EC49FEG finite theorem; Python standard library only.
Frozen pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Run: python EC49FEG_CERTIFY.py
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product, combinations
import json

OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
     'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
ORDER='acdefg'
TRANS=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
       (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
       (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
SIGNATURES={4:(16,32),5:(1,2,4,8),6:(16,32),
            7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
A=(3,2,1)
B_FAMILY=((3,4,1),(4,3,1),(5,2,1),(5,2,2),(6,1,1),(6,1,2))
C_FAMILY=((4,6,1),(5,5,1),(6,4,1),(6,4,2),(7,3,1),
          (7,3,2),(8,2,1),(8,2,2),(8,2,3))

def native(w): return bytes(v+7 for s in w for v in OPS[s])
def pref(w):
    q=native(w);return {q[:i] for i in range(1,len(q)+1)}
def sig(w):
    q=0
    for ch in w:q=TRANS[q][ORDER.index(ch)]
    return SIG[q]
def key(w):
    z=Counter(t for ch in w for t in OPS[ch] if t>0)
    return z[1],z[2],z[3]
def end(w):
    z=Counter(t for ch in w for t in OPS[ch])
    return tuple(z[i]-z[-i] for i in range(1,7))

@lru_cache(None)
def pool(h,k):
    x,y,z=k
    a=z-1;r=x+y-h-1;f=h+1-y-2*z;g=h+1-x
    if min(a,r,f,g)<0:return ()
    cs={'a':a,'c':0,'d':0,'e':z,'f':f,'g':g}
    out=[]
    def rec(left,q,w):
        if not left:
            if SIG[q]:
                wd=''.join(w)
                assert key(wd)==k and end(wd)==(2,0,0,0,0,0)
                out.append((wd,SIG[q]))
            return
        for j,s in enumerate(ORDER):
            if cs[s]:
                cs[s]-=1;w.append(s);rec(left-1,TRANS[q][j],w)
                w.pop();cs[s]+=1
    for nc in range(r+1):
        cs['c']=nc;cs['d']=r-nc;rec(h,0,[])
    return tuple(out)

def early28():
    good={}
    for h in (2,3):
        words=[''.join(v) for v in product(ORDER,repeat=h)]
        good[h]=[w for w in words if sig(w) and end(w)==(2,0,0,0,0,0)]
    h2=[xs for xs in combinations(good[2],4)
        if all(any(sig(w)&mask for w in xs) for mask in (18,20,33,40))]
    h3=[xs for xs in combinations(good[3],2)
        if all(any(sig(w)&mask for w in xs) for mask in (18,20,33,40))]
    out=[]
    for x,y in product(h2,h3):
        if len({key(w) for w in x+y})<=2:out.append((x,y))
    assert len(out)==28,len(out)
    return out

@lru_cache(None)
def min_cover(masks,n):
    """Exact minimum unit-cost cover of n groups using integer bitmasks."""
    raw=set(m for m in masks if m)
    maximal=tuple(m for m in raw if not any(m!=v and m&v==m for v in raw))
    by_bit=tuple(tuple(m for m in maximal if m>>j&1) for j in range(n))
    @lru_cache(None)
    def opt(need):
        if not need:return 0
        j=min((j for j in range(n) if need>>j&1),key=lambda t:len(by_bit[t]))
        assert by_bit[j]
        return 1+min(opt(need&~m) for m in by_bit[j])
    return opt((1<<n)-1)

def case_bound(B,C,free):
    groups=[]
    for h,ss in SIGNATURES.items():
        ks=(A,) if h==4 else (B,C) if h==5 else (B,) if h==6 else (C,)
        p=tuple(z for k in ks for z in pool(h,k))
        for s in ss:
            words={native(w) for w,t in p if t==s}
            assert words,(h,s,B,C)
            groups.append(words)
    depths=max(max(len(w) for w in ws) for ws in groups)
    bound=35;covers=[]
    for depth in range(1,depths+1):
        # Retain only groups whose EVERY alternative reaches this depth.
        active=[ws for ws in groups if min(map(len,ws))>=depth]
        masks=defaultdict(int)
        for i,ws in enumerate(active):
            for w in ws:masks[w[:depth]]|=1<<i
        free_mask=0
        for p,m in masks.items():
            if p in free:free_mask|=m
        uncovered=((1<<len(active))-1)&~free_mask
        if not uncovered:cnt=0
        else:
            bits=[i for i in range(len(active)) if uncovered>>i&1]
            choices=frozenset(sum(1<<j for j,i in enumerate(bits) if m>>i&1)
                              for p,m in masks.items() if p not in free)
            cnt=min_cover(tuple(sorted(choices)),len(bits))
        covers.append(cnt);bound+=cnt
    return bound,covers

def audit_witness(W):
    sizes={2:4,3:2,4:2,5:4,6:2,7:4,8:4,9:2}
    assert set(map(int,W))==set(sizes)
    pre=set();ks=set()
    for hs,words in W.items():
        h=int(hs);assert len(words)==sizes[h] and len(set(words))==len(words)
        assert all(any(sig(w)&mask for w in words) for mask in (18,20,33,40))
        for w in words:
            assert len(w)==h and end(w)==(2,0,0,0,0,0)
            pre.update(pref(w));ks.add(key(w))
    assert len(ks)==5
    return len(pre), sorted(ks)

WITNESS={'2':['ce','ed','ge','ec'],'3':['feg','gef'],
'4':['fegg','gefg'],'5':['gefgd','feggd','feggc','gefgc'],
'6':['feggfg','gefgfg'],
'7':['gefgdfd','feggddf','feggcfc','gefgccf'],
'8':['gefgdfgf','feggfgfd','feggcffg','gefgfgfc'],
'9':['feggfgfgf','gefgfgffg']}

def run():
    early=early28()
    costs=[len(set().union(*(pref(w) for group in e for w in group))) for e in early]
    assert min(costs)==35
    union=set().union(*(pref(w) for e in early for group in e for w in group))
    assert len(union)==70
    trans=str.maketrans({'c':'d','d':'c','f':'g','g':'f'})
    assert {tuple(sorted((tuple(sorted(g)) for g in e))) for e in early} == \
           {tuple(sorted((tuple(sorted(w.translate(trans) for w in g)) for g in e))) for e in early}
    out=[]
    for b in B_FAMILY:
        for c in C_FAMILY:
            lb,numbers=case_bound(b,c,union)
            out.append({'A':A,'B':b,'C':c,'lower_bound':lb,'depth_cover':numbers})
    assert len(out)==54 and min(x['lower_bound'] for x in out)==109
    cost,ks=audit_witness(WITNESS)
    assert cost==109
    return {'frozen_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
            'early_28':len(early),'minimum_early_cost':min(costs),
            'early_union_prefixes':len(union),'orbit_representatives':len(out),
            'min_lower_bound':min(x['lower_bound'] for x in out),
            'max_lower_bound':max(x['lower_bound'] for x in out),
            'all_108_ge_109':all(x['lower_bound']>=109 for x in out),
            'full_witness_cost':cost,'witness_keys':ks,
            'scope':'108 three-late-key assignments, 28 early pairs, H5 allowed B or C; native signed X6 and exact 9-state signatures',
            'cases':out}
if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2))
