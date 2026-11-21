"""Verify short integer clique cuts and surviving fractional covers exactly."""
import argparse,json,sys
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
HERE=Path(__file__).resolve().parent

def points(mask):
    while mask:
        bit=mask&-mask;yield bit.bit_length()-1;mask-=bit

def verify(previous,source):
    second=previous/'previous/previous/previous/previous/previous'
    sys.path.insert(0,str(second/'bounds'))
    from cyclic11 import observations,class_cost
    bad,menus=observations()
    original=json.loads(source.read_text())
    cuts=json.loads((HERE/'clique_cuts.json').read_text())
    after=json.loads((HERE/'after_one_cut_covers.json').read_text())
    stars=json.loads((HERE/'lifted_star_cuts.json').read_text())
    assert original['tag']==cuts['source_tag']==after['tag']==stars['source_tag']
    targets={tuple(map(int,t.split('-')[:2])):int(t.split('-')[2])for t in original['tag'].split('_')}
    assert targets.pop((12,1104))==2
    assert sum(s*n for (s,c),n in targets.items())==101
    assert sum(c*n for (s,c),n in targets.items())+2208==9858
    oldframes={f['frame']:f for f in original['frames']};newframes={f['frame']:f for f in after['frames']}
    assert set(oldframes)==set(newframes)=={1,2,3,4,5}
    assert {cut['frame']for cut in cuts['cuts']}==set(oldframes)
    assert {cut['frame']for cut in stars['cuts']}==set(oldframes)and len(stars['cuts'])==5
    native_checked={}
    def audit(frame):
        free=int(frame['free']);counts=defaultdict(Fraction);sums=defaultdict(Fraction);assigned={}
        assert free.bit_count()==101
        for row in frame['weights']:
            mask=int(row['mask']);t=tuple(row['type']);pts=list(points(mask))
            assert t in targets and mask&free==mask and mask not in assigned
            if mask not in native_checked:
                assert len(pts)==t[0]
                assert all(not(bad[a][b]&mask)for a,b in combinations(pts,2))
                assert class_cost(pts,menus)==t[1]
                native_checked[mask]=t
            assert native_checked[mask]==t
            weight=Fraction(row['numerator'],row['denominator']);assert weight>0
            assigned[mask]=weight;counts[t]+=weight
            for p in pts:sums[p]+=weight
        assert counts==targets
        assert all(sums[i]==((free>>i)&1)for i in range(125))
        assert len(assigned)==frame['positive_classes']==104
        return assigned
    results=[]
    def star_lhs(weights,cut):
        m=int(cut['anchor_mask']);point=cut['point']
        assert not(m>>point&1)and cut['rhs']==1
        return weights.get(m,Fraction(0))+sum((v for n,v in weights.items()if n>>point&1 and n&m),Fraction(0))
    for cut in cuts['cuts']:
        i=cut['frame'];old=oldframes[i];new=newframes[i]
        assert cut['kind']=='pairwise_intersecting_clique'and cut['rhs']==1
        assert old['free']==cut['free']==new['free']
        before=audit(old);revised=audit(new)
        masks=list(map(int,cut['class_masks']))
        assert len(set(masks))==len(masks)==cut['cardinality']
        assert all(a&b for a,b in combinations(masks,2))
        common=masks[0]
        for m in masks:common&=m
        assert common==0
        indices=cut['support_indices']
        assert [int(old['weights'][j]['mask'])for j in indices]==masks
        lhs=sum((before[m]for m in masks),Fraction(0))
        assert lhs==Fraction(cut['lhs_numerator'],cut['lhs_denominator'])>1
        assert lhs-1==Fraction(cut['margin_numerator'],cut['margin_denominator'])
        newlhs=sum((revised.get(m,Fraction(0))for m in masks),Fraction(0))
        assert newlhs==Fraction(new['cut_lhs_numerator'],new['cut_lhs_denominator'])<=1
        star=next(c for c in stars['cuts']if c['frame']==i)
        assert star['free']==old['free']
        anchor=int(star['anchor_mask']);point=star['point']
        compatible=sum((v for m,v in before.items()if m>>point&1 and not(m&anchor)),Fraction(0))
        assert before[anchor]==Fraction(star['anchor_weight'])and compatible==Fraction(star['compatible_point_weight'])
        oldstar=star_lhs(before,star)
        assert oldstar-1==Fraction(star['violation'])>0
        all_values=[sum((revised.get(int(m),Fraction(0))for m in c['class_masks']),Fraction(0))for c in cuts['cuts']]
        all_values.extend(star_lhs(revised,c)for c in stars['cuts'])
        assert len(all_values)==10 and max(all_values)<=1
        results.append({'frame':i,'clique_size':len(masks),'old_lhs':str(lhs),'old_lifted_star_lhs':str(oldstar),'new_lhs':str(newlhs),'new_maximum_over_all_ten_cuts':str(max(all_values)),'new_positive_classes':len(revised)})
    assert len(results)==5
    return {'cuts_verified':10,'explicit_clique_cuts':5,'lifted_star_clique_cuts':5,'old_fractional_points_strictly_separated':5,'integer_covers_removed':0,'new_fractional_covers_verified':5,'new_covers_satisfying_all_ten_cuts':5,'native_legal_classes_checked':len(native_checked),'whole_relaxation_proved_infeasible':False,'cases':results}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,required=True);p.add_argument('--fractional-source',type=Path,default=HERE.parent/'lower/fractional_covers.json');a=p.parse_args()
    result=verify(a.previous.resolve(),a.fractional_source.resolve())
    expected=HERE/'result.json'
    if expected.exists():assert json.loads(expected.read_text())==result
    print(json.dumps(result,indent=2,sort_keys=True))
