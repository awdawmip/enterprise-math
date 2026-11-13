"""Stage477-B: exact positive-BRC type compression for two binary blocks in native X6."""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
from math import comb
import json, random

LETTERS = 'BC'
PAIRS = ('BB', 'BC', 'CB', 'CC')

def edges(word):
    hist = Counter(a+b for a, b in zip(word, word[1:]))
    return tuple(hist[z] for z in PAIRS)

def add(x, y):
    return tuple(a+b for a,b in zip(x,y))

def count_type(length, start, end, e):
    """Exact number of length-'length' binary words with endpoints and directed edges."""
    if length < 1 or any(x < 0 for x in e) or sum(e) != length-1:
        return 0
    bb,bc,cb,cc=e
    if bc-cb != (start=='B')-(end=='B'):
        return 0
    nb = bb+bc+(end=='B')
    nc = cc+cb+(end=='C')
    rb = cb+(start=='B')
    rc = bc+(start=='C')
    def ways(n,r):
        if n == 0:
            return int(r == 0)
        return comb(n-1,r-1) if 1 <= r <= n else 0
    return ways(nb,rb)*ways(nc,rc)

def compositions(total):
    for a in range(total+1):
        for b in range(total-a+1):
            for c in range(total-a-b+1):
                yield (a,b,c,total-a-b-c)

def observed_type(w,h):
    return (int(w[0]=='B')+int(h[0]=='B'),
            int(w[-1]=='B')+int(h[-1]=='B'),
            add(edges(w),edges(h)))

def hidden_mass(wfirst,wlast,we,typ,u):
    firstB = typ[0]-int(wfirst=='B')
    lastB = typ[1]-int(wlast=='B')
    if firstB not in (0,1) or lastB not in (0,1):
        return 0
    he=tuple(a-b for a,b in zip(typ[2],we))
    return count_type(u,'B' if firstB else 'C','B' if lastB else 'C',he)

def population(word,typ,u):
    return hidden_mass(word[0],word[-1],edges(word),typ,u)

def summarize(k,u,typ):
    classes=mass=types=0
    for we in compositions(k-1):
        for s in LETTERS:
            for t in LETTERS:
                nw=count_type(k,s,t,we)
                if nw:
                    nh=hidden_mass(s,t,we,typ,u)
                    if nh:
                        classes+=nw
                        mass+=nw*nh
                        types+=1
    return {'classes':classes,'population':mass,'supported_types':types}

def prefix_support(prefix,k,u,typ):
    if not prefix:
        return summarize(k,u,typ)['classes']
    rem=k-len(prefix)
    fixed=edges(prefix)
    count=0
    for extra in compositions(rem):
        all_edges=add(fixed,extra)
        for end in LETTERS:
            ways=count_type(rem+1,prefix[-1],end,extra)
            if ways and hidden_mass(prefix[0],end,all_edges,typ,u):
                count+=ways
    return count

def rank(word,k,u,typ):
    assert len(word)==k and population(word,typ,u)>0
    pre=''; r=0
    for char in word:
        if char=='C':
            r+=prefix_support(pre+'B',k,u,typ)
        pre+=char
    return r

def unrank(index,k,u,typ):
    total=summarize(k,u,typ)['classes']
    if not 0 <= index < total:
        raise ValueError('rank out of range')
    pre=''
    for _ in range(k):
        nb=prefix_support(pre+'B',k,u,typ)
        if index < nb:
            pre+='B'
        else:
            pre+='C'; index-=nb
    assert population(pre,typ,u)>0
    return pre

def brute(k,u):
    fibers=defaultdict(lambda: defaultdict(int))
    for w in map(''.join,product(LETTERS,repeat=k)):
        for h in map(''.join,product(LETTERS,repeat=u)):
            fibers[observed_type(w,h)][w]+=1
    checks=0
    for typ,groups in fibers.items():
        x=summarize(k,u,typ)
        assert x['classes']==len(groups)
        assert x['population']==sum(groups.values())
        for i,(w,nt) in enumerate(sorted(groups.items())):
            assert population(w,typ,u)==nt
            assert rank(w,k,u,typ)==i
            assert unrank(i,k,u,typ)==w
            checks+=1
    return len(fibers), checks

def test_type_formula():
    tested=0
    for length in range(1,10):
        words=defaultdict(int)
        for w in map(''.join,product(LETTERS,repeat=length)):
            words[(w[0],w[-1],edges(w))]+=1
        for (s,t,e),mass in words.items():
            assert count_type(length,s,t,e)==mass
            tested+=1
    return tested

def run():
    fmt=test_type_formula()
    fcount=word_checks=0
    for k in range(1,6):
        for u in range(1,6):
            f,c=brute(k,u)
            fcount+=f; word_checks+=c
    rng=random.Random(47720261106)
    k,u=40,31
    w=''.join(rng.choices(LETTERS,k=k))
    h=''.join(rng.choices(LETTERS,k=u))
    typ=observed_type(w,h)
    large=summarize(k,u,typ)
    assert large['population']>=1 and large['classes']>=1
    sample_ranks=sorted(set([0,large['classes']//2,large['classes']-1]))
    verified=[]
    for r in sample_ranks:
        candidate=unrank(r,k,u,typ)
        assert rank(candidate,k,u,typ)==r
        verified.append({'rank':r,'prefix':candidate[:12],'population':population(candidate,typ,u)})
    return {'model':'P=A^m; Q=A^m W A H A; W,H binary BC; Q POP=0; P POP/APPEND<=k; Q APPEND<=1',
            'type_formula_verified':fmt,'small_k_u_range':[1,5],
            'small_fibers_verified':fcount,'small_word_population_rank_checks':word_checks,
            'large':{'k':k,'u':u,'m':2*k+2,'n':2*k+2+k+u+2,
                     'observed_type':[typ[0],typ[1],list(typ[2])],
                     'w':w,'h':h,'classes':large['classes'],'population':large['population'],
                     'supported_types':large['supported_types'],'rank_spot_checks':verified},
            'status':'all assertions passed'}

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2))
