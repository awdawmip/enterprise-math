"""Exact three-coordinate mod-three separation of the joint4 survivor."""
from fractions import Fraction
from hashlib import sha256
from itertools import product
from pathlib import Path
import argparse
import json

TYPES=((9,557),(10,744),(11,936),(11,944))
COUNTS=(2,5,2,1)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--old-witness',type=Path,required=True)
    p.add_argument('--new-witness',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    data=a.old_witness.read_bytes();old=json.loads(data)
    assert sha256(data).hexdigest()=='688cc132b50d235d4781b58d0b86c6485e21f03dcd4f08f44c38ac40b87f8e68'
    newer=a.new_witness.read_bytes();new=json.loads(newer)
    assert old['free_mask']==new['free_mask']
    free=int(old['free_mask']);pts=list(product(range(5),repeat=3))
    lam=[(int(x==0)+int(y==0)+min(z,5-z))%3 for x,y,z in pts]
    aa=(0,2,2,0)
    rhs=(sum(lam[p] for p in range(125) if free>>p&1)+sum(x*y for x,y in zip(aa,COUNTS)))%3
    assert rhs==2
    def lhs(doc):
        ans=Fraction()
        for r in doc['weights']:
            mask=int(r['mask']);typ=TYPES.index((r['size'],r['cost']))
            coeff=(sum(lam[p] for p in range(125) if mask>>p&1)+aa[typ])%3
            ans+=coeff*Fraction(r['numerator'],r['denominator'])
        return ans
    old_value,new_value=lhs(old),lhs(new)
    assert old_value==Fraction(640653671197550772695391122065144819577,
                               327044389539142404231032919160124124202)<2
    assert new_value>=2
    result={'old_witness_sha256':sha256(data).hexdigest(),
       'new_witness_sha256':sha256(newer).hexdigest(),'modulus':3,
       'point_formula':'lambda(x) = [x0=0] + [x1=0] + min(x2,5-x2) (mod 3)',
       'type_coefficients':aa,'rhs':rhs,'old_lhs':str(old_value),'old_gap':str(2-old_value),
       'new_lhs':str(new_value),'old_point_separated':True,
       'validity':'In an integer partition the sum of nonnegative residues is congruent to 2 modulo 3, hence at least 2.',
       'arithmetic':'exact integer and Fraction','review_status':'NOT_REVIEWED'}
    a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))


if __name__=='__main__':main()
