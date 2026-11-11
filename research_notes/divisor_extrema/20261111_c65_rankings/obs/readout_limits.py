"""Outward-rounded ratio envelopes for the eight stationary three-tail suffixes."""
import argparse
from fractions import Fraction as Q
import json
from pathlib import Path

from finite_certificate import read_model, schedule_matrix
from suffix_limits import block,compose,interval_image,enclose_decimals,derivative_ratio
from observed_four import word_forms


SUFFIXES=('1100','1010','1001','0020','0110','0101','0002','0011')


def selected_forms(model,word):
    gap=tuple(map(int,word))
    forms=word_forms(model,4,gap)
    active=1 if gap[-1]<=1 else 2
    assert all(b*(a+b)>0 for a,b in forms)
    slopes=[a/b for a,b in forms]
    assert {slopes[0],slopes[active]}=={min(slopes),max(slopes)}
    return forms[0],forms[active]


def evaluate(line,u):
    a,b=line
    return a*u+b


def determinant(lines):
    (a,b),(c,d)=lines
    return abs(a*d-b*c)


def pointwise_ratio_envelope(chosen,reference,interval):
    factor=determinant(chosen)/determinant(reference)
    lo=hi=factor
    for line,base in zip(chosen,reference):
        quotient=[evaluate(base,x)/evaluate(line,x) for x in interval]
        lo*=min(quotient)
        hi*=max(quotient)
    return lo,hi


def compute(model):
    ref=selected_forms(model,'1100')
    common=(1,0,0,1)
    table={}
    for k in range(4,22):
        if k>4:
            common=compose(common,block(k-1,k,1))
        if k not in (4,5,12,20):
            continue
        interval=interval_image(common,(Q(0),Q(1)))
        data={}
        for code in SUFFIXES:
            forms=selected_forms(model,code)
            envelope=pointwise_ratio_envelope(forms,ref,interval)
            data[code]=enclose_decimals(envelope,30)
        table[k]=data
    X,Y='0002','0011'
    unit=(Q(0),Q(1))
    adjacent={}
    for earlier,later in zip(SUFFIXES,SUFFIXES[1:]):
        envelope=pointwise_ratio_envelope(
            selected_forms(model,earlier),selected_forms(model,later),unit)
        assert envelope[1]<1
        adjacent[earlier+'/'+later]=enclose_decimals(envelope,12)
    ho=pointwise_ratio_envelope(selected_forms(model,X),selected_forms(model,Y),unit)
    mx,my=[schedule_matrix(tuple(map(int,s)),model,True,4) for s in (X,Y)]
    tv=sorted(derivative_ratio(mx,my,x) for x in unit)
    assert Q(95907171,10**8)<ho[0]<=ho[1]<Q(95908149,10**8)
    assert Q(105174383,10**8)<tv[0]<=tv[1]<Q(105175392,10**8)
    return {'adjacent_log_ratio_all_inputs':adjacent,
            'permanent_reversal_all_inputs':{'X':X,'Y':Y,
                'TV_X_over_Y':[str(v) for v in tv],
                'logH_X_over_Y':[str(v) for v in ho]},
            'normalization': 'ln(H_suffix)/ln(H_A)',
            'enclosures_for_all_later_k_and_limit':table}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    res=compute(read_model(args.model))
    args.output.write_text(json.dumps(res,indent=2)+'\n')
    print(res['enclosures_for_all_later_k_and_limit'][20])
