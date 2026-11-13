#!/usr/bin/env python3
"""R749SMO: exact-rational single-node TV identity and depth-two coupling bound."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from R749SMN_REPEATED_PORT_OBSERVER_EXACT_CHECK import observer, chi

def tv(p,q):
    return sum(abs(a-b) for a,b in zip(p,q))/2
def column(rows,x):
    return [row[x] for row in rows]
def mixed(rows):
    n=len(rows[0]); return [sum(row)/n for row in rows]
def reach(name,x,masks,biases):
    if name=='': return F(1)
    bit=1 if name=='1' else -1
    return (1+bit*biases['']*chi(masks[''],x))/2

def main():
    vals=(F(-1),F(-1,2),F(0),F(1,2),F(1))
    old_profiles=[{'':F(1,2),'0':F(-1,2),'1':F(1,2)},
                  {'':F(1),'0':F(1),'1':F(1)},
                  {'':F(-1),'0':F(-1),'1':F(-1)}]
    tests=0
    for aa,bb,cc in product(range(4),repeat=3):
        masks={'':aa,'0':bb,'1':cc}
        for old in old_profiles:
            K=observer(2,2,masks,old)
            for node in ('','0','1'):
                for new_lam in vals:
                    new=dict(old);new[node]=new_lam
                    L=observer(2,2,masks,new)
                    delta=abs(new_lam-old[node])/2
                    for x in range(4):
                        expected=reach(node,x,masks,old)*delta
                        assert tv(column(K,x),column(L,x))==expected
                    mixed_bound=delta*sum(reach(node,x,masks,old) for x in range(4))/4
                    assert tv(mixed(K),mixed(L))<=mixed_bound
                    tests+=1
    multi=0
    for t in range(500):
        masks={'':(t+1)%4,'0':(3*t+1)%4,'1':(7*t+3)%4}
        old={n:vals[(t+4*i+i*i)%5] for i,n in enumerate(('','0','1'))}
        new={n:vals[(2*t+i+2*i*i+1)%5] for i,n in enumerate(('','0','1'))}
        K=observer(2,2,masks,old); L=observer(2,2,masks,new)
        q0=abs(old['']-new[''])/2
        q1=max(abs(old[n]-new[n]) for n in ('0','1'))/2
        cap=1-(1-q0)*(1-q1)
        assert tv(mixed(K),mixed(L))<=cap
        assert all(tv(column(K,x),column(L,x))<=cap for x in range(4))
        multi+=1
    masks={'':0,'0':0,'1':0}
    old={'':F(1),'0':F(1),'1':F(1)}
    new={'':F(1,3),'0':F(1),'1':F(1,2)}
    actual=tv(column(observer(2,1,masks,old),0),column(observer(2,1,masks,new),0))
    sharp=1-(1-F(1,3))*(1-F(1,4))
    assert actual==sharp==F(1,2)
    result={
        'schema':'ENTERPRISE_MATH_R749SMO_TV_ERASURE_EXACT_V1',
        'status':'PASS',
        'arithmetic':'Python Fraction exact',
        'single_node_profiles':tests,
        'single_node_source_columns':4*tests,
        'multinode_depth_two_profiles':multi,
        'sharp_witness_tv':'1/2',
        'model':'Abstract public binary Walsh feedback tree, arbitrary repeated masks',
        'scientific_input':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389'}
    with Path(__file__).with_name('R749SMO_ADAPTIVE_ERASURE_TV_RESULTS.json').open('w') as f:
        json.dump(result,f,indent=2);f.write('\n')
    print('PASS',tests,'single-node profiles',multi,'multi-node profiles; sharp TV=',actual)
if __name__=='__main__':main()
