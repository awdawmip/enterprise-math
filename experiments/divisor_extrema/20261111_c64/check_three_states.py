"""Independent C62 three-state likelihood enumeration and comparison to scalar TV."""
import argparse
import json
from fractions import Fraction as Q
from math import comb
from edge_helpers import ordered_three, word_tv


def direct_tv(k, path):
    # Each row starts immediately after the corresponding fixed preparation history.
    # Retain natural observation likelihoods by keeping each row unnormalized.
    rows = [[Q(1),Q(0),Q(0)], [Q(0),Q(1),Q(0)]]
    stock = {2:k,3:k,5:k+1,7:1}
    rates = (Q(1,4),Q(1),Q(4))
    observed = []
    for i,m in enumerate(path):
        observed.extend([5]*m)
        if i < k:
            observed.extend((2,3))
    for prime in observed:
        factors = []
        for z in rates:
            total = stock[2]+stock[3]+stock[7]+z*stock[5]
            numerator = stock[prime]*(z if prime==5 else 1)
            factors.append(numerator/total)
        for i,row in enumerate(rows):
            mass = [value*p for value,p in zip(row,factors)]
            if prime==2:
                rows[i] = [Q(0),mass[0],mass[1]+mass[2]]
            elif prime==3:
                rows[i] = [sum(mass)*Q(7,8)+mass[0]/8,mass[1]/8,mass[2]/8]
            else:
                rows[i] = mass
        stock[prime] -= 1
    assert stock=={2:0,3:0,5:2,7:1}
    first,second=([x/sum(row) for x in row] for row in rows)
    return sum(abs(x-y) for x,y in zip(first,second))/2


def compositions(total,length):
    if length==1:
        yield (total,)
        return
    for first in range(total+1):
        for tail in compositions(total-first,length-1):
            yield (first,)+tail


def check(max_k):
    records=[]
    for k in range(2,max_k+1):
        ranked=[]
        for path in compositions(k-1,k+1):
            distance=direct_tv(k,path)
            assert distance==word_tv(k,path)
            ranked.append((distance,path))
        ranked.sort()
        assert len(ranked)==comb(2*k-1,k)
        assert tuple(p for _,p in ranked[:3])==ordered_three(k)
        assert all(ranked[i][0]<ranked[i+1][0] for i in range(min(3,len(ranked)-1)))
        records.append({'k':k,'count':len(ranked),'exact_top_three':
                        [{'path':p,'tv':str(v)} for v,p in ranked[:3]]})
    return {'tests':'direct three-state normalized endpoint versus scalar TV for every schedule; strict ranks',
            'checked':sum(row['count'] for row in records),'rows':records}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--max-k',type=int,default=7)
    p.add_argument('--output',default='three_state7.json')
    args=p.parse_args()
    result=check(args.max_k)
    with open(args.output,'w') as file:json.dump(result,file,indent=2)
    print('Verified',result['checked'],'exact three-state versus scalar TV comparisons.')
