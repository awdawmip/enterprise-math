"""Direct integer three-state check of fourth-place crossover at k=8,9,10."""
import argparse
from fractions import Fraction as Q
from functools import lru_cache
from heapq import nsmallest
import json
from math import comb, lcm
from check_three_states import compositions
from edge_helpers import ordered_three, word_tv
from rank_four import front_pair, terminal_pair


@lru_cache(None)
def integer_weights(visible_stock, fives, p):
    # All three original Plackett-Luce probabilities share the remaining count
    # of this symbol. Clear the rate denominators by the same scalar for every state.
    K=visible_stock+1
    denominators=(4*K+fives,K+fives,K+4*fives)
    numerators=(1,1,4) if p==5 else (4,1,1)
    multiple=lcm(*denominators)
    return tuple(num*(multiple//den) for num,den in zip(numerators,denominators))


def observe(row,weights,p):
    a,b,c=(x*w for x,w in zip(row,weights))
    if p==2:
        return (0,a,b+c)
    if p==3:
        # Multiply through by 8, common to every state.
        return (7*(a+b+c)+a,b,c)
    return (a,b,c)


def direct_integer_tv(k,path):
    visible,fives=2*k,k+1
    h0=(1,0,0)
    h1=(0,1,0)
    for idx,m in enumerate(path):
        symbols=(5,)*m + ((2,3) if idx<k else ())
        for p in symbols:
            weights=integer_weights(visible,fives,p)
            h0=observe(h0,weights,p)
            h1=observe(h1,weights,p)
            if p==5:fives-=1
            else:visible-=1
    assert (visible,fives)==(0,2)
    t0,t1=sum(h0),sum(h1)
    return Q(sum(abs(x*t1-y*t0) for x,y in zip(h0,h1)),2*t0*t1)


def run():
    results=[]
    for k in (8,9,10):
        count=0
        def all_paths():
            nonlocal count
            for path in compositions(k-1,k+1):
                count+=1
                yield direct_integer_tv(k,path),path
        top=nsmallest(6,all_paths())
        assert count==comb(2*k-1,k)
        assert [p for _,p in top[:3]]==list(ordered_three(k))
        assert top[3][1]==(front_pair(k) if k<=9 else terminal_pair(k))
        assert top[4][1]==(terminal_pair(k) if k<=9 else front_pair(k))
        assert all(top[j][0]<top[j+1][0] for j in range(5))
        assert all(tv==word_tv(k,path) for tv,path in top)
        results.append({'k':k,'count':count,'first_six':
                        [{'path':path,'exact_tv':str(tv)} for tv,path in top]})
    return {'method':'direct integer three-state likelihoods, exhaustive enumeration, smallest six rechecked by independent scalar map',
            'checked_count':sum(x['count'] for x in results),'results':results}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',default='rank_four_direct.json')
    args=p.parse_args()
    data=run()
    with open(args.output,'w') as f:json.dump(data,f,indent=2)
    print('Verified',data['checked_count'],'direct three-state schedule distances for k=8,9,10.')
