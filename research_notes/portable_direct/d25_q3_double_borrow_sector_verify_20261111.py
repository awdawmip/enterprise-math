#!/usr/bin/env python3
"""Exact q³ double-borrow sector verification; depends on neighboring q² jet."""
from math import comb
import json
from d25_q2_lucas_carry_jet_verify_20261111 import binom_jet,prime

def check(q,m,e):
    Q=q**3; x=pow(2,-1,Q)
    directA=directB=jetA=jetB=count=0
    sample=[]
    for k in range(m+1):
        _,R1,c1=binom_jet(q,m,k)
        _,R2,c2=binom_jet(q,2*m+e,k)
        if not (c1 and c2): continue
        actual=comb(m,k)*comb(2*m+e,k)*pow(x,k,Q)%Q
        predicted=q*q*R1*R2*pow(x,k,Q)%Q
        assert actual==predicted,(q,m,e,k,actual,predicted)
        w=1-6*e+12*k
        directA=(directA+actual)%Q
        directB=(directB+w*actual)%Q
        jetA=(jetA+predicted)%Q
        jetB=(jetB+w*predicted)%Q
        count+=1
        if len(sample)<8:
            sample.append({"k":k,"R1":R1,"R2":R2,
                "A_contribution":actual,"B_contribution":w*actual%Q})
    assert (directA,directB)==(jetA,jetB)
    return {"count":count,"sector_mod_q3":[jetA,jetB],"sample":sample}

def verify():
    rows=borrowed=nonzero=0
    examples={}
    for q in range(5,998):
        if not prime(q):continue
        for r in range(1,12):
            N=q**r
            e=int(N%6==5); m=(N-1-4*e)//6
            if m>600:break
            v=check(q,m,e)
            rows+=1; borrowed+=v["count"]
            nonzero+=int(v["sector_mod_q3"]!=[0,0])
            if (q,r) in {(7,2),(7,3),(11,2),(13,2),(17,2),(29,2),(37,2)}:
                examples[f"{q}^{r}"]={"N":N,"m":m,"epsilon":e,**v}
    assert rows==188 and borrowed==1704 and nonzero==19
    assert examples["7^2"]["sector_mod_q3"]==[49,147]
    assert examples["13^2"]["sector_mod_q3"]==[1183,507]
    return {"bounded_pairs":rows,"double_borrow_terms":borrowed,
            "nonzero_joint_sector_pairs":nonzero,"all_exact_checks_passed":True,
            "named_examples":examples}

if __name__=="__main__":
    print(json.dumps(verify(),indent=2))
