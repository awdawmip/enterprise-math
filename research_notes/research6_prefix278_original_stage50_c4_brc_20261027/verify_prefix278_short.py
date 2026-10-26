"""Original Stage50 C4-BRC replay; checkout verified bundle as ./source."""
from fractions import Fraction as Q
import hashlib, json, pathlib, sys
P=pathlib.Path(__file__).resolve().parent
assert hashlib.sha256((P/'source/stage50/interference.py').read_bytes()).hexdigest()=='43b23d47e5d3da191aeaeefefe4f378fea2166eefd228ae77475f7196ceca853'
sys.path.insert(0,str(P/'source'))
from stage50 import interference as h
packets={'A':{0:h.ONE,1:(Q(0),Q(-1))},
         'B':{0:(Q(2),Q(0)),1:(Q(0),Q(-1)),2:(Q(-1),Q(0))},
         'C':{0:h.ONE,1:(Q(0),Q(1)),2:(Q(4),Q(0)),3:(Q(0),Q(-2))}}
rows={}
for label,f in packets.items():
    assert h.moment(f,1)==(Q(0),Q(1,2))
    cur={}
    for lag in (1,2):
        scan=[]
        for phase in range(4):
            result=h.local(f,lag,phase)
            moment=h.moment(f,lag)
            expected=Q(5,18)*(1-h.cmul(h.PHASE[phase],moment)[0])
            assert result['probability']==expected
            assert result['compatible'] and result['norm_in']==result['norm_out']
            scan.append(str(result['probability']))
        cur[str(lag)]=scan
    rows[label]={'z':str(h.packet_z(f)),
                 'c1':[str(x) for x in h.moment(f,1)],
                 'c2':[str(x) for x in h.moment(f,2)],'external_prob':cur}
assert rows['A']['external_prob']['1']==rows['B']['external_prob']['1']==rows['C']['external_prob']['1']
assert [rows[k]['external_prob']['2'][0] for k in ('A','B','C')]==['5/18','10/27','25/99']
print('PREFIX278_ORIGINAL_STAGE50_BRC_PASS 24/24')
print(json.dumps(rows,ensure_ascii=False,indent=2))
