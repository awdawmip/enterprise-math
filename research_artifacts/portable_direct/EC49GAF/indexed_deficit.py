"""GAE exact dominance via inverted bitsets; benchmark on original frozen cases."""
from pathlib import Path
from collections import Counter
from random import Random
from time import perf_counter_ns
import json
import sys
from multi_target import model, physical


def bits(x):
    while x:
        b = x & -x
        yield b.bit_length() - 1
        x ^= b


def indexed(out, k, n):
    keep = {}
    postings = [0] * (k + n)
    alive = 0
    universe = (1 << (k + n)) - 1
    for (m, c), loss in sorted(out.items(), key=lambda a: (a[1], a[0][0].bit_count()+a[0][1].bit_count(), a[0])):
        key = m | (c << k)
        candidates = alive
        for j in bits(universe ^ key):
            candidates &= ~postings[j]
            if not candidates:
                break
        if candidates:
            continue
        bit = 1 << len(keep)
        keep[m, c] = loss
        alive |= bit
        for j in bits(key):
            postings[j] |= bit
    return keep


def make_solver(check=False):
    src = Path('deficit_slots.py').read_text().split('def main():')[0]
    start = src.index('            keep={}')
    end = src.index('        stats[where', start)
    replacement = '            keep=indexed(out,k,n)\n'
    if check:
        replacement += '            assert keep==quadratic(out)\n'
    replacement += '            out=keep\n'
    ns = {'indexed': indexed, 'quadratic': quadratic}
    exec(compile(src[:start]+replacement+src[end:], 'indexed_parent', 'exec'), ns)
    return ns['solve']


def quadratic(out):
    keep = {}
    for (m,c),loss in sorted(out.items(), key=lambda a:(a[1],a[0][0].bit_count()+a[0][1].bit_count(),a[0])):
        if not any(u&m==u and r&c==r for u,r in keep):
            keep[m,c]=loss
    return keep


def main():
    from deficit_slots import solve as baseline
    old = json.load(open('deficit_slots.out'))
    nodes = []
    for line in open('ga_nodes.txt'):
        k,n,*p=map(int,line.split()); st=list(zip(p[::2],p[1::2])); _,qs,*_=model(n,physical(st,10,25))
        blocks=[sum(1<<j for j,(u,h) in enumerate(st) if u==b) for b in sorted({u for u,h in st})]
        nodes.append((n,qs,blocks,k))
    fast=make_solver(); checked=make_solver(True)
    checks=Counter(); timings=Counter(); rows=[]
    for row in old['rows'][int(sys.argv[1]) if len(sys.argv)>1 else 0:int(sys.argv[2]) if len(sys.argv)>2 else None]:
        i,j=row['index'],row['test']; args=(*nodes[i],tuple(row['weights']))
        expected=row['pruned']; assert checked(*args)==expected
        runs=[('index',fast,True),('quadratic',baseline,True),('unpruned',baseline,False)]
        if (i+j)%2: runs.reverse()
        times={}
        for name,fn,prune in runs:
            t=perf_counter_ns(); a=fn(*args,prune); dt=perf_counter_ns()-t
            assert a==(row['unpruned'] if not prune else expected)
            timings[name]+=dt; times[name]=dt
        checks['frozen']+=1; rows.append({'index':i,'test':j,'times_ns':times,'value':expected['value'],'final':expected['final']})
    rng=Random(43169)
    for _ in range(500):
        k=rng.randrange(0,7); n=rng.randrange(1,17); out={}
        for j in range(rng.randrange(1,250)):
            key=(rng.randrange(1<<k),rng.randrange(1<<n)); loss=rng.randrange(20)
            out[key]=min(loss,out.get(key,loss))
        assert indexed(out,k,n)==quadratic(out); checks['synthetic_profiles']+=1
    print(json.dumps({'checks':checks,'times_ns':timings,'rows':rows},sort_keys=True))

if __name__=='__main__': main()
