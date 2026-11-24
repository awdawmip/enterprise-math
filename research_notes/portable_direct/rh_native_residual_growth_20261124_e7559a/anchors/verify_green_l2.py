#!/usr/bin/env python3
"""Exact checks for normalized Green decay and the closed skeleton 5/4 bound."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import json


def nodes(count):
    return [2**(j//2+1) if j%2==0 else 3*2**(j//2) for j in range(count)]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('green_l2_certificate.json'))
    args=parser.parse_args()
    kernel_checks=0
    for count in range(3,22):
        a=nodes(count);a0,aN=a[0],a[-1]
        for j in range(count):
            for k in range(1,count-1):
                G=F((min(a[j],a[k])-a0)*(aN-max(a[j],a[k])),aN-a0)
                assert G*G/F(a[j]*a[k])<=F(3,4)**abs(j-k)
                kernel_checks+=1
    vectors=integer_points=0
    for count in range(2,8):
        a=nodes(count)
        for q in product((-2,0,3),repeat=count):
            energy=F(0)
            for j in range(count-1):
                u,v=a[j],a[j+1]
                for n in range(u,v):
                    value=F((v-n)*q[j]+(n-u)*q[j+1],v-u)
                    energy+=max(value,F(0))**2/(n*n)
                    integer_points+=1
            energy+=F(max(q[-1],0)**2,a[-1]**2)
            integer_points+=1
            anchor=sum((F(max(qj,0)**2,aj) for aj,qj in zip(a,q)),F(0))
            assert energy<=F(5,4)*anchor
            vectors+=1
    result={'schema':'EM_GREEN_CHAIN_L2_CERTIFICATE_V1','status':'PASS',
            'arithmetic':'Exact fractions; no floating decisions',
            'normalized_green_decay_checks':kernel_checks,
            'green_domain':'Interlaced-chain prefixes of3..21 nodes; all row nodes and interior source columns',
            'closed_skeleton_vectors':vectors,'closed_integer_point_evaluations':integer_points,
            'skeleton_domain':'Interlaced-chain prefixes of2..7 nodes; all q in{−2,0,3}^count',
            'constants':{'lower_adjacent_ratio':'4/3','upper_adjacent_ratio':'3/2','green_l2_operator_upper':'7+4sqrt(3)','closed_skeleton_energy_upper':'5/4'},
            'scope':'Finite implementation coverage; all-parameter inequalities proved in GREEN_CHAIN_L2_TRANSFER.md.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))


if __name__=='__main__':main()
