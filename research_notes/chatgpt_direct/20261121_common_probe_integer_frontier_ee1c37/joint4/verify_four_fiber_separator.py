"""A 55-point odd-set separator, checked independently with Fraction."""
from fractions import Fraction
from hashlib import sha256
from itertools import product
from pathlib import Path
import argparse
import json


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--old-witness',type=Path,required=True)
    p.add_argument('--new-witness',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    data=a.old_witness.read_bytes();old=json.loads(data)
    assert sha256(data).hexdigest()=='f411ba7d7d45af6f4ca8531d36563bb712a9aca7e9561651e741a7b816396969'
    newdata=a.new_witness.read_bytes();new=json.loads(newdata)
    assert old['free_mask']==new['free_mask']
    free=int(old['free_mask']);pts=list(product(range(5),repeat=3))
    v=sum(1<<p for p,x in enumerate(pts) if (free>>p)&1
          and ((x[0]!=4)^(x[1]==4)^(x[2] in (1,4))))
    assert v==18051771192507465278461723409234964653 and v.bit_count()==55
    def lhs(doc):
        return sum((Fraction(r['numerator'],r['denominator']) for r in doc['weights']
                    if (int(r['mask'])&v).bit_count()%2),Fraction())
    old_value=lhs(old);new_value=lhs(new)
    assert old_value==Fraction(112938537080637033207601500431880235243,
                               146892661307821883249929206807463679241)<1
    assert new_value==1
    result={'old_witness_sha256':sha256(data).hexdigest(),
            'new_witness_sha256':sha256(newdata).hexdigest(),
            'predicate':'free intersect ((x0 != 4) XOR (x1 == 4) XOR (x2 in {1,4}))',
            'subset_mask':str(v),'subset_size':55,
            'rhs':1,'old_lhs':str(old_value),'old_gap':str(1-old_value),
            'new_lhs':str(new_value),'old_point_separated':True,
            'validity':'For every integer partition, occupation numbers of V sum to odd 55; at least one is odd.',
            'arithmetic':'exact integer and Fraction','review_status':'NOT_REVIEWED'}
    a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))


if __name__=='__main__':main()
