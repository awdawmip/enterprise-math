#!/usr/bin/env python3
"""Exact rational implication checks for PREFIX-670, frozen BRC observer."""
from fractions import Fraction as F
import json

SCIENCE_PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'

def linear_penalty(q):
    q = F(q)
    assert 12 <= q <= 24
    return q*(F(76650,12) + F(76595,144)*(q-12))

def quadratic_penalty(q):
    q = F(q)
    return F(15000*q*q+221*q,2)

def check():
    n=0
    def ck(a):
        nonlocal n
        assert a
        n+=1
    ck(linear_penalty(12)==76650)
    ck(linear_penalty(24)==306490)
    ck(linear_penalty(18)==F(689685,4))
    ck(quadratic_penalty(12)==1081326)
    ck(quadratic_penalty(24)==4322652)
    ck(quadratic_penalty(18)==2431989)
    for q in range(12,25):
        L=F(24-q,12)*F(76650,12)+F(q-12,12)*F(306490,24)
        ck(linear_penalty(q)==q*L)
        ck(L>0)
        ck(quadratic_penalty(q)>7500*q*q)
    ck(F(76595,144)>0)
    return {
      'schema':'EM_PREFIX670_R6_SLOT_RESOLVED_STABILITY_V1',
      'science_pin':SCIENCE_PIN,
      'scope':{'p':['0','1/64'],'z':['607/4096','609/4096'],'q':['12','24']},
      'L_formula':'q*(76650/12+76595*(q-12)/144)',
      'C_formula':'(15000*q*q+221*q)/2',
      'z_term':'6400000*(z-z_star(q))^2',
      'examples':{str(q):{'L':str(linear_penalty(q)),
                          'C':str(quadratic_penalty(q))} for q in (12,18,24)},
      'checks_passed':n,'result':'ALL_CHECKS_PASS',
      'status':'AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED'
    }
if __name__=='__main__':
    o=check()
    print(json.dumps(o,indent=2))
    print('ALL_CHECKS_PASS',o['checks_passed'])
