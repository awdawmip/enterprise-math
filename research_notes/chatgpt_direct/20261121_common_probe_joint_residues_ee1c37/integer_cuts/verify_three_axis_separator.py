"""Exact three-coordinate parity separator for the first modular/star frame-2 point."""
from pathlib import Path
from fractions import Fraction
import argparse,json,hashlib
from parallel_family import POINTS
HERE=Path(__file__).resolve().parent

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--witness',type=Path,default=HERE/'star_joint_exact/cover_2.json')
    p.add_argument('--output',type=Path,default=HERE/'three_axis_separator.json');a=p.parse_args()
    data=a.witness.read_bytes();d=json.loads(data);free=int(d['free_mask'])
    U=sum(1<<i for i,(x,y,z) in enumerate(POINTS) if free>>i&1 and ((x==3)^(y==4)^(z==2)))
    assert U==36060501842677877893061286573469995140 and U.bit_count()==37
    lhs=sum((Fraction(r['numerator'],r['denominator']) for r in d['weights'] if (int(r['mask'])&U).bit_count()%2),Fraction())
    assert lhs==Fraction(171522011904914807150345818478833199184,172795823802562932703984005438262925839)<1
    out={'frame':2,'witness_sha256':hashlib.sha256(data).hexdigest(),
         'predicate':'free intersect ((x0=3) XOR (x1=4) XOR (x2=2))','subset_mask':str(U),'subset_size':37,
         'point_ids':[i for i in range(125) if U>>i&1],
         'point_coordinates':[p for i,p in enumerate(POINTS) if U>>i&1],
         'lhs':str(lhs),'rhs':1,'gap':str(1-lhs),'violated':True,
         'scope':'A particular exact point satisfying full stars and the declared one-/two-coordinate modular families is separated; this alone does not exclude its full frame.'}
    a.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['point_ids','point_coordinates']}))

if __name__=='__main__':main()
