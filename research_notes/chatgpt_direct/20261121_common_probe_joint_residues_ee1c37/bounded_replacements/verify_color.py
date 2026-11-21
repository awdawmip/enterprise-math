"""Regenerate every radius-five candidate and check its rational dual exactly."""
from hashlib import sha256
from pathlib import Path
import argparse
import json
import struct
import subprocess

import verify

HERE=Path(__file__).resolve().parent


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work',type=Path,required=True)
    args=parser.parse_args();work=args.work.resolve();work.mkdir(parents=True,exist_ok=True)
    rows,costs=verify.initial()
    observation=verify.observations(work/'obs')
    subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',HERE/'bounded_replacements_export.cpp',
                    '-o',work/'export'],check=True)
    exported=json.loads(subprocess.check_output([str(work/'export'),str(work/'obs'),str(HERE/'initial.txt'),
                                                '5','9995',str(work/'columns')],text=True))
    assert exported=={'complete':True,'radius':5,'budget':9995,'rows':74582,'enumerated':522700}
    dual=json.loads((HERE/'color_dual.json').read_text())
    weights={int(p):v for p,v in dual['point_weights'].items()}
    label_weights=dual['label_weights'];scale=dual['scale']
    free=set(range(125))-set(rows[0])-set(rows[1])
    assert set(weights)==free and scale==100 and len(label_weights)==12
    recorded=list(map(int,(HERE/'color_dual.txt').read_text().split()))
    assert recorded==[scale,*label_weights,*(weights.get(p,0) for p in range(125))]
    raw=(work/'columns').read_bytes();assert len(raw)==24*74582
    min_slack=None;counts=[0]*12
    for lo,hi,c,label in struct.iter_unpack('<QQII',raw):
        mask=lo|(hi<<64);ids=[]
        while mask:
            bit=mask&-mask;ids.append(bit.bit_length()-1);mask-=bit
        assert set(ids)<=free and label in range(2,12)
        assert len(ids)==len(rows[label]) and len(set(ids)-set(rows[label]))<=5
        slack=scale*c-sum(weights[p]for p in ids)-label_weights[label]
        assert slack>=0
        min_slack=slack if min_slack is None else min(min_slack,slack)
        counts[label]+=1
    numerator=scale*sum(costs[:2])+sum(weights.values())+sum(label_weights[2:])
    lower=(numerator+scale-1)//scale
    assert min_slack==dual['minimum_slack']==3
    assert numerator==dual['lower_numerator']==989537 and lower==9896
    # Regenerate a positive control using this same integer-weight format.
    subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',HERE/'bounded_replacements_color.cpp',
                    '-o',work/'cover'],check=True)
    positive=json.loads(subprocess.check_output([str(work/'cover'),str(work/'obs'),str(HERE/'initial.txt'),
                                                 '2','9996',str(HERE/'color_dual.txt')],text=True))
    control=verify.check_positive(positive,rows)
    result={'complete':True,'observations':observation,'candidate_generation':exported,
            'candidate_bank_sha256':sha256(raw).hexdigest(),'columns_by_old_label':counts,
            'minimum_integer_slack':min_slack,'dual_denominator':scale,'lower_numerator':numerator,
            'integer_cost_lower_bound':lower,'positive_control':control,
            'radius5_cover_exhaustion':False,
            'source_sha256':{f:sha256((HERE/f).read_bytes()).hexdigest()for f in (
                'verify_color.py','verify.py','bounded_replacements_export.cpp',
                'bounded_replacements_color.cpp','color_dual.json','color_dual.txt','initial.txt')}}
    (work/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
