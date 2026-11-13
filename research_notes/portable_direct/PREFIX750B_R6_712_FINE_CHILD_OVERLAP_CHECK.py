#!/usr/bin/env python3
"""PREFIX-750B-R6: independently replay the inherited PREFIX712
old-witness *fine-cell* sufficient certificate on all 197 distinct
published sibling upper /384 closed rectangles, each with four /768
fine children. Python 3 stdlib only; exact Fractions, no floats.
Usage: python PREFIX750B_R6_712_FINE_CHILD_OVERLAP_CHECK.py [first last_exclusive]
A split run asserts its exact expected local accepted fine children.
Full run across 197 rectangles may exceed a short interactive timeout.
"""
import json,sys
from pathlib import Path
from PREFIX741_R6_INNER_STRIP_194 import endpoint_lower, oldmu, oldW

EXPECTED = [[40,94,2253597],[41,94,5318721],[41,95,452325],[43,96,1926330],[46,98,2345829],[47,98,5537828],[47,99,1221214],[48,100,247976],[49,100,3480312],[51,102,2014029],[53,104,1117278],[54,104,4430149],[54,105,875174],[55,104,7752598],[55,105,4202284],[56,104,11081648],[56,105,7538956],[57,104,14414255],[57,105,10882228],[58,104,17747314],[58,105,14229070],[59,104,21077662],[59,105,17576393],[60,104,24402087],[60,105,20921050],[61,104,27717332],[61,105,24259841]]
def microfloor(q):
    v=q*1000000
    return v.numerator//v.denominator

def main():
    source=json.loads(Path(__file__).with_name("PREFIX_R6_GAMMA_SIBLING_UNION_746_749_RESULTS.json").read_text(encoding="utf-8"))
    originals=[tuple(x) for x in source["all_unique_upper_pairs"]]
    assert len(originals)==197 and len(set(originals))==197
    assert all(0<=i<j<192 for i,j in originals)
    if len(sys.argv)==3:
        first,last=map(int,sys.argv[1:])
    elif len(sys.argv)==1:
        first,last=0,len(originals)
    else:
        raise SystemExit("usage: ...py [first last_exclusive]")
    assert 0<=first<last<=len(originals)
    positive=[];coarse_floors=[]
    for i,j in originals[first:last]:
        coarse=endpoint_lower(i,j,1,0,0,oldmu,oldW)
        assert coarse<0,(i,j,"not excluded from 711 coarse")
        coarse_floors.append(microfloor(coarse))
        for di in range(2):
            for dj in range(2):
                g=endpoint_lower(i,j,2,di,dj,oldmu,oldW)
                if g>0:
                    positive.append([2*i+di,2*j+dj,microfloor(g)])
    own_macro=set(originals[first:last])
    expected=[x for x in EXPECTED if (x[0]//2,x[1]//2) in own_macro]
    assert positive==expected, (len(positive),len(expected),"PREFIX712 fine child list mismatch")
    print("PASS macro",first,last,"coarse G1 all negative",len(coarse_floors))
    print("PASS finer old positive upper",len(positive),
          "reflected",2*len(positive),flush=True)
    if first==0 and last==197:
        assert len(positive)==27
        assert 1576-2*len(positive)==1522
        assert max(coarse_floors)==-102756816
        print("ALL_CHECKS_PASS PREFIX750B-R6 old-prefix712 fine overlap 54; unique-relative-712 1522")
if __name__=="__main__":main()
