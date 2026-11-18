#!/usr/bin/env python3
"""Independently verify each concrete PREFIX-920 row witness (Python 3).

python3 PREFIX920_R6_WITNESS_AUDIT.py PREFIX920_R6_COMPLETE_ROW_WITNESS_OUTPUT.txt
"""
import hashlib
import json
import sys
from collections import Counter
from math import gcd

N=1<<32
B=440665
FIRST=(1<<18)+1
LAST=(1<<19)-1

def audit(path):
    counts=Counter()
    digest=hashlib.sha256()
    expected=FIRST
    headline=None
    target=None
    with open(path,'rb') as f:
        for raw in f:
            digest.update(raw)
            line=raw.decode('ascii').rstrip('\n')
            if line.startswith('W '):
                vals=[int(v) for v in line[2:].split(',')]
                assert len(vals)==7,(expected, vals)
                a,b,t,x,y,i,j=vals
                assert a==expected and b==B and t in (1,2,3)
                expected+=2
                assert 0<=x<y<N
                assert (i==-1 or 0<=i<32) and (j==-1 or 0<=j<32)
                if t==1: assert i==j==-1
                elif t==2: assert i>=0 and j==-1
                else: assert i>=0 and j>=0
                u=x if i==-1 else x^(1<<i)
                v=y if j==-1 else y^(1<<j)
                assert 0<=u<N and 0<=v<N
                assert (x-y)%a==0 and (u-v)%b==0
                if t==2: assert gcd(a,b)==1
                if a==262151:
                    target={'a':a,'b':b,'type':t,'x':x,'y':y,'i':i,'j':j,
                            'end_u':u,'end_v':v,'start_multiplier':(y-x)//a,
                            'end_multiplier':(v-u)//b}
                counts[t]+=1
            elif line.startswith('TARGET '):
                continue
            elif line.startswith('TOTAL '):
                headline=line
            else:
                raise AssertionError(f'Unknown line: {line!r}')
    assert expected==LAST+2
    assert sum(counts.values())==(1<<17)
    assert (counts[1],counts[2],counts[3])==(1405,61884,67783)
    assert target and target['type']==3
    return {
        'schema':'PREFIX920_ROW_WITNESS_INDEPENDENT_AUDIT_V1',
        'observed_ascii_sha256':digest.hexdigest(),
        'fully_checked_named_witnesses':sum(counts.values()),
        'zero_zero':counts[1],
        'zero_flip':counts[2],
        'flip_flip_only':counts[3],
        'zero_witness_deficits':0,
        'target':target,
        'generator_summary':headline,
        'audit':'Python integer verification, independently rechecks both observed modular equalities for every printed named pair'
    }

if __name__=='__main__':
    if len(sys.argv)!=2:
        raise SystemExit('Usage: audit.py generator_output.txt')
    print(json.dumps(audit(sys.argv[1]),indent=2))
