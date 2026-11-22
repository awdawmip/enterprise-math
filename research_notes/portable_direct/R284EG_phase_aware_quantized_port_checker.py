#!/usr/bin/env python3
"""R284EG: exhaustive common-phase quantization of R/W/RW Port orbit subsets.
Run beside the frozen R284CO and R284EE checkers; all computations are exact.
"""
import json
from pathlib import Path
from R284EE_diagonal_two_read_checker import readouts

PAIR_OFFSETS={'R':(0,1),'W':(0,64),'RW':(0,65)}
TRIPLE=(0,1,65)
FOUR=(0,1,64,65)

def collision_phases(values,width,offsets):
    bad=[]
    for phase in range(width):
        q=[(x-phase)//width for x in values]
        seen=set()
        for i in range(len(values)):
            key=tuple(q[i^delta] for delta in offsets)
            if key in seen:
                bad.append(phase)
                break
            seen.add(key)
    return bad

def main():
    f=readouts()  # uses frozen R284CO and asserts original full-domain SHA256
    assert len(f)==65536
    out={}
    for width in (61,72):
        failures={name:collision_phases(f,width,offs)
                  for name,offs in PAIR_OFFSETS.items()}
        failures['triple']=collision_phases(f,width,TRIPLE)
        failures['four']=collision_phases(f,width,FOUR)
        kinds=[]
        for phase in range(width):
            if any(phase not in failures[x] for x in PAIR_OFFSETS):
                kinds.append(2)
            elif phase not in failures['triple']:
                kinds.append(3)
            elif phase not in failures['four']:
                kinds.append(4)
            else:
                raise AssertionError(('four-read not injective',width,phase))
        out[str(width)]={'failed_phases':failures,
                         'adaptive_min_read_counts':{str(k):kinds.count(k)
                                                      for k in (2,3,4)}}
    assert out['61']['failed_phases']['R']==list(range(19))+list(range(33,61))
    assert out['61']['failed_phases']['W']==[23,32,45,46]
    assert out['61']['failed_phases']['RW']==[8,26,51]
    assert not out['61']['failed_phases']['triple']
    assert not out['61']['failed_phases']['four']
    assert out['61']['adaptive_min_read_counts']=={'2':61,'3':0,'4':0}
    assert all(out['72']['failed_phases'][x]==list(range(72))
               for x in PAIR_OFFSETS)
    good=[t for t in range(72) if t not in out['72']['failed_phases']['triple']]
    assert good==[3,7,8,9,10,55,56,57,65,66,67,68]
    assert not out['72']['failed_phases']['four']
    assert out['72']['adaptive_min_read_counts']=={'2':0,'3':12,'4':60}
    out.update({'schema':'R284EG_PHASE_AWARE_QUANTIZATION_V1',
                'source_commit':'acba2d8667903434aaa2a10720f43637fcc2421b',
                'source_blob_sha1':'b46e0f682b58e47c27094b4bea6fa4e55119a3ee',
                'frozen_codeword_sha256':'b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4',
                'states':65536,'scope':'Frozen Port exact finite phase classification',
                'review':'NOT_REVIEWED'})
    dest=Path(__file__).with_name('R284EG_phase_aware_quantized_port_certificate.json')
    dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({s:out[s]['adaptive_min_read_counts'] for s in ('61','72')}))

if __name__=='__main__':main()
