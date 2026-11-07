#!/usr/bin/env python3
"""EC49EXL exact finite native-X6 BRC key/rank collision classifier."""
import itertools,collections,json
from fractions import Fraction
OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
HIST=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')
T2=(1836425,1866380)
T4=(1836687,1867942,1872656,1873981)
HS=tuple(range(2,9))
def sig(word):
    st=tuple(x for op in word for x in OPS[op]);n=0;f=1
    for ev,p in HIST:
        for x in st:
            if p==1 and x==2:
                if ev=='N':ev='A'
                elif ev=='B':ev='BA'
            if p==2 and x==1:
                if ev=='N':ev='B'
                elif ev=='A':ev='AB'
            p=x
        n+=BUCKETS.index(ev)*f;f*=5
    return n
def rank(sigs):
    rows=[[Fraction(int((s//(5**i))%5==b)) for s in sorted(sigs) for b in range(5)]for i in range(9)]
    r=0
    for col in range(len(rows[0])):
        p=next((k for k in range(r,9) if rows[k][col]),None)
        if p is None:continue
        rows[r],rows[p]=rows[p],rows[r]
        v=rows[r][col];rows[r]=[x/v for x in rows[r]]
        for k in range(r+1,9):
            if rows[k][col]:
                c=rows[k][col];rows[k]=[x-c*y for x,y in zip(rows[k],rows[r])]
        r+=1
        if r==9:break
    return r
def words(h):
    # Return endpoint X6=(2,0,...,0) iff #b=0 and #e=#a+1.
    for a in range((h-1)//2+1):
        e=a+1
        for r in range(h-2*a):
            for c in range(r+1):
                d=r-c
                for f in range(h-2*a-r):
                    g=h-2*a-1-r-f
                    k=(r+2*e+f,r+g,e,0,0,0)
                    multiset='a'*a+'c'*c+'d'*d+'e'*e+'f'*f+'g'*g
                    for p in set(itertools.permutations(multiset)):
                        yield ''.join(p),k
def partitions():
    def rec(seq,n):
        if len(seq)==7:
            if n==5:yield tuple(seq)
            return
        for x in range(min(n+1,5)):
            yield from rec(seq+[x],max(n,x+1))
    return list(rec([0],1))
def options(part,eligible):
    g=collections.defaultdict(list)
    for h,c in zip(HS,part):g[c].append(h)
    return g,{c:set.intersection(*(eligible[h] for h in ss)) for c,ss in g.items()}
def matching(opts):
    if any(not v for v in opts.values()):return False
    assigned={}
    def dfs(c,seen):
        for k in sorted(opts[c]):
            if k in seen:continue
            seen.add(k)
            if k not in assigned or dfs(assigned[k],seen):
                assigned[k]=c;return True
        return False
    return all(dfs(c,set()) for c in sorted(opts,key=lambda c:len(opts[c])))
def run():
    sets={};counts={};total=0
    for h in HS:
        keys=collections.defaultdict(set);n=0
        for w,k in words(h):
            n+=1;keys[k].add(sig(w))
        total+=n
        T2keys=set();T4keys=set();full=set()
        for key,sigs in keys.items():
            u,v,w=key[:3];r=u+v-h-1;a=w-1;f=h+1-v-2*w;g=h+1-u
            assert min(r,a,f,g)>=0
            is2=(r==0 and f>=1 and g>=1)
            is4=(r>=1)
            assert (rank(sigs)==9)==(is2 or is4),(h,key)
            if is2:
                assert set(T2)<=sigs and rank(T2)==9
                T2keys.add(key)
            if is4:
                assert set(T4)<=sigs and rank(T4)==9
                T4keys.add(key)
            if is2 or is4:full.add(key)
        sets[h]={'ANY':full,'T2':T2keys,'T4':T4keys}
        counts[h]={'returning_words':n,'legal_keys':len(keys),'rank9_keys':len(full),'T2_keys':len(T2keys),'T4_keys':len(T4keys)}
    assert total==411368
    assert [counts[h]['rank9_keys'] for h in HS]==[1,4,9,17,28,43,62]
    ps=partitions();assert len(ps)==140
    feasible=[]
    for p in ps:
        groups,opts=options(p,{h:sets[h]['ANY'] for h in HS})
        if matching(opts):
            feasible.append({'partition':list(p),'collisions':[x for x in groups.values() if len(x)>1]})
    triple=sum(any(len(x)==3 for x in p['collisions']) for p in feasible)
    assert len(feasible)==40 and triple==8
    profiles=[];excluded=[]
    for typ in itertools.product(('T2','T4'),repeat=6):
        typ=('T4',)+typ
        eligible={h:sets[h][t] for h,t in zip(HS,typ)}
        num=sum(matching(options(p,eligible)[1]) for p in ps)
        (profiles if num else excluded).append({'types':list(typ),'feasible_partitions':num})
    assert len(profiles)==60 and len(excluded)==4
    report={'status':'PASS','returning_words_checked':total,'by_horizon':counts,
            'partitions':{'all':140,'feasible':40,'excluded':100,'two_pairs':32,'one_triple':8},
            'signature_profiles':{'all':64,'feasible':60,'excluded':4,'excluded_types':excluded},
            'feasible_skeletons':feasible,
            'scope':'finite h=2..8 / exact native signed X6 / BRC keys / Q-rank 9; no E optimum inferred'}
    print(json.dumps(report,indent=2,ensure_ascii=False))
if __name__=='__main__':run()
