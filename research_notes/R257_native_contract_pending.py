#!/usr/bin/env python3
"""R257 Source-native integration probe. NOT EXECUTED against original EM package in R257.
Run inside a matching checkout of awdawmip/enterprise-math@9a1659352c5c5959e82c87924c4c2939c77c0b1b
with its original enterprise_math Python package importable. This tests exact Source
ControlPacket.from_edges, then, Affine and EffectHistogram, not legal P000 dynamics.
"""
from fractions import Fraction
from enterprise_math.brc_transport import Affine
from enterprise_math.brc_control_port import ControlPacket

DFA=((1,0),(2,0),(2,2))
I=Affine.identity(6)

def packet(source_labels, start):
    # Product control R={0,1,2}; one physical control q=0.
    edges=[(r,DFA[r][label],Fraction(1),I,1)
           for r in range(3) for label in source_labels]
    return ControlPacket.from_edges(3,start,1,edges)

def two_step_count(source_labels):
    first=packet(source_labels,0)
    joined=first.then(packet(source_labels,1))
    by_monitor={r:0 for r in range(3)}
    for source,target,hist in joined.blocks:
        if source!=0:continue
        for weight,action,multiplicity in hist.entries:
            assert weight==1 and action==I
            by_monitor[target]+=multiplicity
    return by_monitor

def main():
    # Raw-edge identities are distinct even if source labels coincide.
    A=ControlPacket.from_edges(1,0,1,[(0,0,1,I,1),(0,0,1,I,1)])
    B=ControlPacket.from_edges(1,0,1,[(0,0,1,I,1),(0,0,1,I,1)])
    assert A==B and A.then(A.at(1))==B.then(B.at(1))
    assert A.blocks[0][2].entries==((Fraction(1),I,2),)
    x=two_step_count((0,1))
    y=two_step_count((0,0))
    assert sum(x.values())==sum(y.values())==4
    assert x[2]==1 and y[2]==4
    print('PASS: exact original Source ControlPacket/EffectHistogram two-step provenance lift')

if __name__=='__main__':main()
