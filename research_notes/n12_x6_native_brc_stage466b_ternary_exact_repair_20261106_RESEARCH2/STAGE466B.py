"""Stage466-B: exact BRC population/rank for a ternary native-X6 family.
Original A=+E1 B=+E2 C=+E3, future APPEND_Q uses all 12 directions.
Standard-library integers only. This family has hP=rP=0, sQ=1.
"""
from functools import lru_cache
from itertools import combinations
from math import comb
import json

A, B, C = 0, 2, 4  # native signed direction codes, +E1,+E2,+E3
DIRECTIONS = tuple(range(12))


def visible_count(n, k, hq):
    # P=A X1 A X2 ... Xk A, |P|=2k+1, Q=A^n (n>|P|).
    assert k >= 1 and n > 2*k+1 and 0 <= hq <= n
    return sum(2*i >= max(1, n-hq+1) for i in range(1, k+1))


def support_dp(k, b, v):
    assert 0 <= b <= k and 0 <= v <= k
    hidden = k-v
    @lru_cache(None)
    def f(left, needed):
        if needed < 0 or needed > left+hidden:
            return 0
        if left == 0:
            return int(needed <= hidden)
        return f(left-1, needed-1) + f(left-1, needed)
    return f


def unrank_visible(k, b, v, rank):
    f = support_dp(k,b,v)
    assert 0 <= rank < f(v,b)
    word=[]; remaining=b
    for left in range(v,0,-1):
        n_b = f(left-1,remaining-1)
        if rank < n_b:
            word.append(B); remaining-=1
        else:
            rank-=n_b; word.append(C)
    assert 0 <= remaining <= k-v
    return tuple(word)


def rank_visible(k,b,v,word):
    assert len(word)==v and all(z in (B,C) for z in word)
    f=support_dp(k,b,v)
    rank=0; remaining=b
    for left,z in zip(range(v,0,-1),word):
        if z==C:
            rank+=f(left-1,remaining-1)
        else:
            remaining-=1
    assert 0 <= remaining <= k-v and rank < f(v,b)
    return rank


def population(k,b,v,word):
    assert len(word)==v
    need=b-sum(x==B for x in word)
    return comb(k-v,need) if 0 <= need <= k-v else 0


def exact_summary(k,b,v):
    h=k-v; f=support_dp(k,b,v)
    classes=f(v,b)
    total=sum(comb(v,a)*comb(h,b-a)
              for a in range(max(0,b-h),min(v,b)+1))
    assert total==comb(k,b)
    spots=[]
    for i in sorted({0,classes//2,classes-1}):
        w=unrank_visible(k,b,v,i)
        spots.append({'rank':i,'decoded_word':''.join('B' if x==B else 'C' for x in w),
                      'population':population(k,b,v,w)})
    return {'k':k,'B_count':b,'visible_variables':v,'hidden_variables':h,
            'classes':classes,'original_population':total,'rank_unrank_spots':spots}


def observer(p,q):
    def vec(w):
        z=[0]*6
        for a in w:z[a//2]+=1 if a%2==0 else -1
        return tuple(z)
    def edges(w):
        z=[0]*144
        for x,y in zip(w,w[1:]):z[12*x+y]+=1
        return tuple(z)
    return (len(p),len(q),vec(p),vec(q),edges(p),edges(q),
            sum(x==y for x,y in zip(p,q)))


def pop_append_trace(p,n,hq):
    # Exhaust all Q-only futures with at most hq POPs and at most one APPEND;
    # after that APPEND, the only further Q move is POP, returning to a
    # previously represented original-prefix state. Record all 12 probes.
    out=[]
    for t in range(hq+1):
        q=(A,)*(n-t)
        out.append(observer(p,q))
        for u in DIRECTIONS:
            out.append(observer(p,q+(u,)))
    return tuple(out)


def brute_checks():
    stats={'families':0,'parameter_tests':0,'raw_history_pairs':0,
           'rank_roundtrips':0,'future_pair_checks':0,'full_append_directions':12}
    for k in range(1,6):
        m=2*k+1;n=m+3
        for b in range(k+1):
            words=[]
            for ix in combinations(range(k),b):
                xs=tuple(B if i in ix else C for i in range(k))
                p=tuple(z for x in xs for z in (A,x))+(A,)
                words.append((xs,p))
            # Source-distinct histories all in same complete initial fiber.
            assert len({observer(p,(A,)*n) for _,p in words})==1
            stats['families']+=1
            for hq in range(n+1):
                v=visible_count(n,k,hq)
                groups={}
                for xs,p in words:groups[xs[k-v:] if v else ()]=groups.get(xs[k-v:] if v else (),0)+1
                sorted_keys=sorted(groups)
                f=support_dp(k,b,v)
                assert len(groups)==f(v,b)
                assert sum(groups.values())==comb(k,b)
                for rank,word in enumerate(sorted_keys):
                    assert unrank_visible(k,b,v,rank)==word
                    assert rank_visible(k,b,v,word)==rank
                    assert population(k,b,v,word)==groups[word]
                    stats['rank_roundtrips']+=1
                stats['parameter_tests']+=1
                if k<=4 and hq in (0, n-m, n-m+1, n-m+2, n):
                    sig=[pop_append_trace(p,n,hq) for _,p in words]
                    for i in range(len(words)):
                        for j in range(i+1,len(words)):
                            x,y=words[i][0],words[j][0]
                            assert (sig[i]==sig[j]) == ((x[k-v:] if v else ())==(y[k-v:] if v else ()))
                            stats['future_pair_checks']+=1
    return stats


if __name__=='__main__':
    out={'stage':'466B','verification':'exact standard-library integers',
         'small_complete':brute_checks(),
         'large':exact_summary(30,14,18),
         'larger':exact_summary(50,23,34)}
    print(json.dumps(out,ensure_ascii=False,indent=2))
