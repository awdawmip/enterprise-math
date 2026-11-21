"""Exact finite algebra and radical constants for C87's low-half theorem."""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).parent
SOURCE=ROOT.parent/'positions'/'mellin_chambers.json'


def root20(q,bits=112):
    q=F(q);scale=1<<bits
    left=0;right=scale*max(1,q.numerator//q.denominator+1)
    numerator=q.numerator*scale**20;denominator=q.denominator
    while right-left>1:
        middle=(left+right)//2
        if denominator*middle**20<=numerator:left=middle
        else:right=middle
    assert denominator*left**20<=numerator<denominator*right**20
    return F(left,scale),F(right,scale)


def radical_sum(constant,terms):
    low=high=F(constant)
    for coefficient,base in terms:
        coefficient=F(coefficient);a,b=root20(base)
        if coefficient>=0:low+=coefficient*a;high+=coefficient*b
        else:low+=coefficient*b;high+=coefficient*a
    return low,high


def clean(d):return {key:value for key,value in d.items()if value}


def run():
    source=json.loads(SOURCE.read_text())
    chambers={}
    for row in source['chambers']:
        chambers[row['r_index'],row['s_index']]={
            tuple(F(term[name])for name in ['a_r','b_s','c_rs']):F(term['weight'])
            for term in row['terms']}
    # s^p E(r), encoded with all scalar powers absorbed in the arguments.
    correction={
        (F(0),F(0),F(1)):F(1),
        (F(0),F(0),F(3,2)):F(-2),
        (F(0),F(0),F(2)):F(1),
        (F(0),F(1),F(-2)):F(1),
        (F(0),F(1),F(-1)):F(1),
        (F(0),F(1),F(-3,2)):F(-2),
        (F(0),F(1,2),F(-1,2)):F(-2),
        (F(0),F(1,2),F(1,2)):F(-2),
        (F(0),F(1,2),F(0)):F(4),
    }
    calculated=defaultdict(F,chambers[0,0])
    for key,value in correction.items():calculated[key]+=value
    assert clean(calculated)==chambers[1,0]
    for (a,b,c),value in correction.items():calculated[b,a,c]+=value
    assert clean(calculated)==chambers[1,1]

    # e(2)=6+4*2^q-9*(3/2)^q-(1/2)^q, q=1/20.
    e2=radical_sum(6,[(4,2),(-9,F(3,2)),(-1,F(1,2))])
    assert e2[1]<0
    # C(p)+p(p-1)[2^(q+1)+(1/2)3^q-3/2]+2e(2).
    delta=radical_sum(F(12617,800),[
        (F(1,3),F(1,6)),(-1,F(1,3)),(-6,F(1,2)),
        (F(8,3),F(2,3)),(-9,F(3,2)),
        (F(-739,200),2),(F(861,800),3)])
    assert delta[0]>F(37,500)
    result={
        'status':'PASS',
        'arithmetic':'Fraction; exact integer twentieth-power comparisons',
        'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'chamber_10_is_00_plus_one_correction':True,
        'chamber_11_is_00_plus_two_corrections':True,
        'e2_bounds':[str(x)for x in e2],
        'delta_half_bounds':[str(x)for x in delta],
        'display_e2':[float(x)for x in e2],
        'display_delta_half':[float(x)for x in delta],
        'certified_strict_delta_lower':'37/500',
        'theorem_domain':'0<r<=1/2 and 0<s<=1/2',
        'conclusion':'T(r,s)>(37/500)*(r*s)^(41/20)',
        'floating_values_are_display_only':True,
    }
    (ROOT/'low_half_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    return result


if __name__=='__main__':print(json.dumps(run(),indent=2))
