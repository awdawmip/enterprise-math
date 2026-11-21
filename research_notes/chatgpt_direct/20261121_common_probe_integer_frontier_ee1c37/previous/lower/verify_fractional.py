"""Verify the relaxation obstruction using original menus and rational arithmetic."""
import argparse,json,sys
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
HERE=Path(__file__).resolve().parent

def pts(mask):
    while mask:
        bit=mask&-mask;yield bit.bit_length()-1;mask-=bit

def verify(previous):
    third=previous/'previous/previous/previous/previous'
    second=third/'previous'
    sys.path[:0]=[str(third/'low'),str(second/'bounds')]
    from cyclic11 import observations,class_cost
    from cores import orbits
    bad,pairs=observations()
    fixed,seen,reps=orbits(2)
    assert fixed==seen and len(reps)==6
    frames={((1<<125)-1)^sum(rows):rows for rows,_ in reps}
    data=json.loads((HERE/'fractional_covers.json').read_text())
    target={tuple(map(int,t.split('-')[:2])):int(t.split('-')[2])for t in data['tag'].split('_')}
    assert target.pop((12,1104))==2
    assert sum(s*n for (s,c),n in target.items())==101
    assert sum(n for n in target.values())==10
    assert sum(c*n for (s,c),n in target.items())+2208==9858
    checked={}
    def legal(mask,size,cost):
        if mask in checked:
            assert checked[mask]==(size,cost);return
        points=list(pts(mask));assert len(points)==size
        assert all(not(bad[i][j]&mask)for i,j in combinations(points,2))
        assert class_cost(points,pairs)==cost
        checked[mask]=(size,cost)
    for frame in data['frames']:
        free=int(frame['free']);assert free in frames
        for core in frames[free]:legal(core,12,1104)
        sums=[Fraction(0)]*125;counts=defaultdict(Fraction)
        distinct=set()
        for row in frame['weights']:
            mask=int(row['mask']);t=tuple(row['type'])
            assert t in target and mask&free==mask and mask not in distinct
            distinct.add(mask);legal(mask,*t)
            weight=Fraction(row['numerator'],row['denominator']);assert weight>0
            for p in pts(mask):sums[p]+=weight
            counts[t]+=weight
        assert len(distinct)==frame['positive_classes']==104
        assert counts==target
        assert sums==[(free>>p)&1 for p in range(125)]
    assert len({int(f['free'])for f in data['frames']})==5
    return {'verified_fractional_frames':5,'positive_classes_per_frame':104,
            'residual_points':101,'residual_label_weight':10,'full_cost':9858,
            'unique_legal_classes_checked':len(checked)}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,required=True);a=p.parse_args()
    print(json.dumps(verify(a.previous.resolve()),sort_keys=True,indent=2))
