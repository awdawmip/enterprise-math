"""Exact local regularity checks needed by HIGH_HALF_REDUCTION.md.

This does not assert global C1 regularity. C86 proved that global assertion
false. Only joins crossed along r in [1/2,1], with s fixed, are checked here.
"""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).parent
SOURCE=ROOT.parent/'positions'/'mellin_chambers.json'


def clean(d):return {key:value for key,value in d.items()if value}


def terms(row):
    return [tuple(F(term[name])for name in ['a_r','b_s','c_rs','weight'])
            for term in row['terms']]


def ledger(rows,fixed_axis,fixed_value,derivative=False):
    out=defaultdict(F)
    for a,b,c,w in rows:
        if fixed_axis=='r':
            alpha,beta=a*fixed_value,b+c*fixed_value
            d0,d1=a,c
        else:
            alpha,beta=b*fixed_value,a+c*fixed_value
            d0,d1=a+c*fixed_value,F(0)
        sign=1
        if next((v for v in [alpha,beta]if v),0)<0:
            alpha,beta=-alpha,-beta;sign=-1
        if not(alpha or beta):continue
        if derivative:
            # Common factors p*sgn(alpha+beta*y)*|alpha+beta*y|^(p-1)
            # leave a rational affine coefficient sign*w*(d0+d1*y).
            out[alpha,beta,0]+=sign*w*d0
            out[alpha,beta,1]+=sign*w*d1
        else:out[alpha,beta,0]+=w
    return clean(out)


def run():
    data=json.loads(SOURCE.read_text())
    chamber={(row['r_index'],row['s_index']):terms(row)for row in data['chambers']}
    records=[]
    for left,right,axis,value,kind in [
        ((2,0),(3,0),'r',F(2,3),'interior vertical normal derivative'),
        ((2,1),(3,1),'r',F(2,3),'interior vertical normal derivative'),
        ((2,2),(3,2),'r',F(2,3),'identical high-high expression'),
        ((2,0),(2,1),'s',F(1,3),'fixed-s boundary tangent derivative'),
        ((3,0),(3,1),'s',F(1,3),'identical low-s expression'),
        ((2,1),(2,2),'s',F(1,2),'fixed-s boundary tangent derivative'),
        ((3,1),(3,2),'s',F(1,2),'fixed-s boundary tangent derivative')]:
        a,b=chamber[left],chamber[right]
        assert ledger(a,axis,value)==ledger(b,axis,value)
        assert ledger(a,axis,value,True)==ledger(b,axis,value,True)
        records.append({'left':left,'right':right,'fixed_axis':axis,
                        'fixed_value':str(value),'scope':kind,
                        'value_ledger_equal':True,'T_r_ledger_equal':True})
    def dictionary(rows):return {(a,b,c):w for a,b,c,w in rows}
    high=dictionary(chamber[2,2])
    assert high==dictionary(chamber[3,2])==dictionary(chamber[3,3])
    assert high=={(b,a,c):w for (a,b,c),w in high.items()}
    for si in range(4):assert not ledger(chamber[3,si],'r',F(1))
    result={'status':'PASS','arithmetic':'Fraction only',
            'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'local_join_records':records,
            'high_high_three_chambers_are_one_symmetric_expression':True,
            'r_one_boundary_zero_ledgers':4,
            'global_C1_claim':False,
            'concavity_sign_inequality_proved':False}
    (ROOT/'high_half_join_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    return result


if __name__=='__main__':print(json.dumps(run(),indent=2))
