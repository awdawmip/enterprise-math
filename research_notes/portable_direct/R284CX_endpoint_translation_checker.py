#!/usr/bin/env python3
"""Exact local branch/endpoint mechanism for four known exceptional Port pairs."""
import json
from pathlib import Path
from R284CO_spectral_witness_checker import P,words,arcs,dist,FROZEN_SHA
X,A=words(),arcs()
PAIRS=((6055669926,12724715924,19,18,(6,)),
       (6051057018,12720103016,19,18,(6,)),
       (6048093436,12717139434,19,18,(6,)),
       (10044326029,14547547380,37,21,(0,1)))
items=[]
for rank,(x,y,ax,ay,changed_pos) in zip((779,1263,1563,7587),PAIRS):
    ix,iy=X.index(x),X.index(y)
    upperx,uppery=ix//4096,iy//4096
    lowerx,lowery=ix%4096,iy%4096
    # source lower[0] maps binary position 11; lower[11] maps position 0.
    diffs=[pos for pos in range(12) if ((lowerx>>(11-pos))&1)!=((lowery>>(11-pos))&1)]
    assert upperx==uppery and diffs==list(changed_pos)
    valsx=[dist(x,a) for a in A]; valsy=[dist(y,a) for a in A]
    mx=max(valsx);my=max(valsy)
    assert mx==my and valsx.count(mx)==valsy.count(my)==1
    assert valsx[ax]==mx and valsy[ay]==my
    sx,wx=A[ax];sy,wy=A[ay]
    dx=(x-sx)%P;dy=(y-sy)%P
    bx='right-end' if dx-wx<P-dx else 'left-start'
    by='right-end' if dy-wy<P-dy else 'left-start'
    if rank!=7587:
        assert bx==by=='right-end'
        assert y-x==(P-(sx+wx)+(sy+wy))==6669045998
        assert mx==x+P-(sx+wx)==y-(sy+wy)
    else:
        assert bx==by=='left-start'
        assert y-x==sy-sx==4503221351
        assert dx==dy and mx==P-dx
    items.append({'rank':rank,'codeword_pair':[x,y],'source_matrix_indices':[ix,iy],
                  'flipped_lower_indices_zero_based':changed_pos,'changed_upper_entries':0,
                  'translated_by':y-x,'unique_d64':mx,'critical_arc_ids_zero_based':[ax,ay],
                  'critical_arcs':[[sx,wx],[sy,wy]],'branch':[bx,by],
                  'second_max_gap':[mx-sorted(valsx)[-2],my-sorted(valsy)[-2]]})
cert={'schema':'R284CX_EXACT_ENDPOINT_TRANSLATION_MECHANISM_V1',
      'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
      'frozen_population_sha256':FROZEN_SHA,'P':P,
      'endpoint_identity_A':{'arc19_right':sum(A[19]),'arc18_right':sum(A[18]),
           'shift_P_minus_right19_plus_right18':P-sum(A[19])+sum(A[18])},
      'start_identity_B':{'arc37_start':A[37][0], 'arc21_start':A[21][0],
           'shift_start21_minus_start37':A[21][0]-A[37][0]},
      'pairs':items,'scope':'These four tied level-64 witnesses only; residual all-level nonuniqueness established in R284CW.'}
out=Path(__file__).with_name('R284CX_endpoint_translation_certificate.json')
out.write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'pair_shifts':[i['translated_by'] for i in items],
  'level64':[i['unique_d64'] for i in items],
  'gaps':[i['second_max_gap'] for i in items],
  'endpoint_shift':cert['endpoint_identity_A']['shift_P_minus_right19_plus_right18'],
  'start_shift':cert['start_identity_B']['shift_start21_minus_start37']},ensure_ascii=False))
