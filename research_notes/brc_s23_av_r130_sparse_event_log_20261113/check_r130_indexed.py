#!/usr/bin/env python3
"""R130.2 persistent exact point query on sparse event log."""
from fractions import Fraction as F
from bisect import bisect_left
from random import Random
from pathlib import Path
import json
from check_r130 import sparse_sweep, word

def build(bits,a,b):
    if b-a==1: return bits[a]
    c=(a+b)//2
    return (build(bits,a,c),build(bits,c,b))

def replace(root,a,b,i,val):
    if b-a==1:return val
    c=(a+b)//2
    if i<c:return (replace(root[0],a,c,i,val),root[1])
    return (root[0],replace(root[1],c,b,i,val))

def bit(root,a,b,i):
    if b-a==1:return root
    c=(a+b)//2
    if i<c:return bit(root[0],a,c,i)
    return bit(root[1],c,b,i)

def index_log(log):
    m=len(log['initial_word'])
    root=build(log['initial_word'],0,m)
    first=root
    cuts=[]; at=[]; after=[]; changes=0
    for ev in log['events']:
        left=root
        cut=left
        for i,value in ev['cut_delta']:
            cut=replace(cut,0,m,i,value);changes+=1
        right=left
        for i,value in ev['right_delta']:
            right=replace(right,0,m,i,value);changes+=1
        cuts.append(F(ev['theta']))
        at.append(cut);after.append(right)
        root=right
    return first,cuts,at,after,changes

def query(index,theta,i,m):
    first,cuts,at,after,_=index
    pos=bisect_left(cuts,theta)
    if pos<len(cuts) and cuts[pos]==theta:
        return bit(at[pos],0,m,i)
    root=first if pos==0 else after[pos-1]
    return bit(root,0,m,i)

def validate(x,A,d,E,m,l,h,rng):
    log=sparse_sweep(x,A,d,E,m,l,h)
    indexed=index_log(log)
    cuts=indexed[1]
    probe=[(l+cuts[0])/2] if cuts else [(l+h)/2]
    for j,c in enumerate(cuts):
        probe.append(c)
        probe.append((c+(cuts[j+1] if j+1<len(cuts) else h))/2)
    for _ in range(25):
        probe.append(l+F(rng.randrange(1,1000),1001)*(h-l))
    count=0
    for t in probe:
        expected=word(x,A,d,E,m,t)
        for i in range(m):
            assert query(indexed,t,i,m)==expected[i],(x,A,d,E,m,l,h,t,i)
            count+=1
    return {'cuts':len(cuts),'point_queries':count,'persistent_updates':indexed[4],
            'delta_count':log['total_saved_deltas']}

def main():
    rng=Random(130220261113)
    results=[]
    edges=[(F(0),0,1,1,64,F(0),F(1)),(F(1,7),-5,5,10,6,F(-2),F(-3,2)),
           (F(0),0,0,0,20,F(-1),F(1)),(F(1,2),0,0,1,12,F(-1),F(1))]
    for v in edges:results.append(validate(*v,rng))
    for _ in range(100):
        x=F(rng.randint(-7,7),rng.randint(1,8))
        A,d,E=(rng.randint(-6,6) for j in range(3))
        m=rng.randint(1,10)
        l=F(rng.randint(-7,3),rng.randint(1,5))
        h=l+F(rng.randint(1,6),rng.randint(1,5))
        results.append(validate(x,A,d,E,m,l,h,rng))
    summary={'status':'R130_PERSISTENT_INDEX_PASS','cases':len(results),
             'total_queries':sum(z['point_queries'] for z in results),
             'total_updates':sum(z['persistent_updates'] for z in results),
             'total_deltas':sum(z['delta_count'] for z in results),
             'total_cuts':sum(z['cuts'] for z in results),
             'm64_case':results[0]}
    print(json.dumps(summary,indent=2,sort_keys=True))
    Path(__file__).with_name('verification_r130_index.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()
