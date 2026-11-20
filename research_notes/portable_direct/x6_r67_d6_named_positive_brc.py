#!/usr/bin/env python3
"""X6 R67: exact conditional named-positive BRC repeated-A star observer.

Every AB trial retains its positive branch weight and both named source Ports;
all B choices are independent resets. This is not a native P000 triad simulator.
"""
from fractions import Fraction
from itertools import product
import json

U=Fraction(2,3)
V=Fraction(3,5)
W=U*V
WITNESSES={
    "baseline_p6":(6,(1,0,0,0,0)),
    "threshold_p21":(21,(-1,-14,14,-6,1)),
    "threshold_p41":(41,(-29,-6,13,-6,1)),
    "threshold_p57":(57,(-35,35,-21,7,-1)),
}
OSC={"baseline_p6":62,"threshold_p21":60,"threshold_p41":48,"threshold_p57":2}

def histograms(p,a):
    left,right=[0]*7,[0]*7
    for d,x in enumerate(a,2):
        left[d]=max(x,0)
        right[d]=max(-x,0)
    left[0]=p-sum(left);right[0]=p-sum(right)
    assert min(left+right)>=0
    return left,right

def named_positive_branches(hist,t):
    degrees=[d for d,c in enumerate(hist) for _ in range(c)]
    count=0
    first=last=None
    for a_port,degree in enumerate(degrees):
        for b_ports in product(range(degree),repeat=t):
            identity=(a_port,b_ports)
            if first is None:first=identity
            last=identity
            count+=1
    return count,W**t*count,first,last

def run():
    output={"schema":"X6_R67_NAMED_POSITIVE_BRC_CHECK_V1",
            "source_weights":{"A":"2/3","B":"3/5"},
            "model":"ordered named AB branches, fixed A Port, independently reset B",
            "witnesses":{}}
    for name,(p,a) in WITNESSES.items():
        c,cp=histograms(p,a)
        delta=[]; counts=[]
        for t in range(1,7):
            n,m,_,_=named_positive_branches(c,t)
            np,mp,_,_=named_positive_branches(cp,t)
            assert n==sum(c[d]*d**t for d in range(7))
            assert np==sum(cp[d]*d**t for d in range(7))
            assert m-mp==W**t*sum(a[d-2]*d**t for d in range(2,7))
            counts.append([n,np]);delta.append(n-np)
        assert max(delta)-min(delta)==OSC[name]
        output["witnesses"][name]={"p":p,"a":list(a),"left_hist":c,
            "right_hist":cp,"moment_differences":delta,
            "oscillation":OSC[name],"count_pairs":counts,"result":"PASS"}
    output["scientific_scope"]="exact typed positive named BRC branch enumeration; no native event/heartbeat, independent review or physical amplitude claim"
    print(json.dumps(output,ensure_ascii=False,indent=2))
if __name__=="__main__":run()
