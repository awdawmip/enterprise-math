#!/usr/bin/env python3
"""EC49FAS: exact native-X6 all-horizon H2-root safe-suffix checks (stdlib)."""
import itertools, json, math
from collections import defaultdict
from fractions import Fraction

OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
     'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
ROOTS=('de','ed','ce','ec')
START=(('N',0),('N',1),('N',2),('A',0),('A',2),
       ('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')

def signed_net(word):
    vector=[0]*6
    for op in word:
        for step in OPS[op]: vector[abs(step)-1]+=1 if step>0 else -1
    return tuple(vector)

def cache_key(word):
    key=[0]*6
    for op in word:
        for step in OPS[op]:
            if step>0: key[step-1]+=1
    return tuple(key)

def obs(word):
    answer=[]
    for state,prev in START:
        for op in word:
            for step in OPS[op]:
                if prev==1 and step==2:
                    if state=='N': state='A'
                    elif state=='B': state='BA'
                if prev==2 and step==1:
                    if state=='N': state='B'
                    elif state=='A': state='AB'
                prev=step
        answer.append(BUCKETS.index(state))
    return tuple(answer)

def rational_rank(rows):
    a=[[Fraction(x) for x in row] for row in rows]
    rank=0
    for col in range(9):
        pivot=next((j for j in range(rank,len(a)) if a[j][col]),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        base=a[rank][col]
        for k in range(col,9): a[rank][k]/=base
        for j in range(rank+1,len(a)):
            factor=a[j][col]
            if factor:
                for k in range(col,9): a[j][k]-=factor*a[rank][k]
        rank+=1
    return rank

def closed_count(n):
    return sum(math.factorial(n)//(math.factorial(k)**2*math.factorial(n-2*k))*3**(n-2*k)
               for k in range(n//2+1))

def key_census(h):
    by_key={}
    for z in range(1,(h+1)//2+1):
        rem=h-(2*z-1)
        for r in range(1,rem+1):
            for f in range(rem-r+1):
                g=rem-r-f
                key=(2*z+r+f,r+g,z,0,0,0)
                n=math.factorial(h-2)//(math.factorial(z-1)**2*math.factorial(r-1)
                                        *math.factorial(f)*math.factorial(g))
                assert n>0 and key not in by_key
                by_key[key]=n
    return by_key

def exhaustive(h):
    by_key=defaultdict(lambda:[0]*4)
    positive=0
    for suffix in itertools.product('acdefg',repeat=h-2):
        if suffix.count('a')!=suffix.count('e'): continue
        w=''.join(suffix)
        for index,root in enumerate(ROOTS):
            word=root+w
            assert signed_net(word)==(2,0,0,0,0,0)
            allowed=obs(word)==obs(root)
            criterion=('c' not in w) if index<2 else ('d' not in w)
            assert allowed==criterion,(h,root,w)
            if allowed:
                positive+=1
                by_key[cache_key(word)][index]+=1
    return positive,dict(by_key)

def run():
    sig={root:obs(root) for root in ROOTS}
    assert sig=={
      'de':(2,3,2,3,3,2,4,3,4),'ed':(2,2,2,3,3,2,2,3,4),
      'ce':(1,1,4,1,3,4,4,3,4),'ec':(1,1,1,1,1,4,4,3,4)}
    rows=[[int(s[j]==b) for j in range(9)] for s in sig.values() for b in range(5)]
    rank=rational_rank(rows)
    assert rank==9
    report=[]
    for h in range(2,11):
        by_key=key_census(h)
        predicted=4*sum(by_key.values())
        assert predicted==4*closed_count(h-2)
        assert len(by_key)==sum(math.comb(h-2*k,2) for k in range((h-2)//2+1))
        if h<=7:
            brute,observed=exhaustive(h)
            assert brute==predicted
            assert set(observed)==set(by_key)
            for key,count in by_key.items():
                assert observed[key]==[count]*4,(key,observed[key],count)
        report.append({'h':h,'keys':len(by_key),'safe_words_per_root':closed_count(h-2),
                       'safe_words_all_roots':predicted,'brute_verified':h<=7})
    for n in range(1,15):
        assert (n+1)*closed_count(n+1)==(6*n+3)*closed_count(n)-5*n*closed_count(n-1)
    return {'status':'PASS','scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
            'model':'signed_native_X6_7_ops_nine_start_five_bucket_six_signatures',
            'roots':list(ROOTS),
            'safe_suffix_alphabet':{'de':['a','d','e','f','g'],
               'ed':['a','d','e','f','g'],'ce':['a','c','e','f','g'],
               'ec':['a','c','e','f','g']},
            'root_signatures':{k:list(v) for k,v in sig.items()},
            'rank_four_root_signatures_over_Q':rank,
            'exhaustive_native_observer_and_cache_key_check':'all balanced suffixes, h=2..7',
            'horizon_counts':report,'recurrence_checked':'n=1..14',
            'readback_scope_note':'Analytic statements all horizons. Exhaustive native observer checks h<=7.'}

if __name__=='__main__':
    print(json.dumps(run(),indent=2,ensure_ascii=False,sort_keys=True))
