#!/usr/bin/env python3
"""R284DU: 8-source-bit exact label classifier and sharp coordinate support."""
import hashlib, json, itertools
from collections import Counter
from pathlib import Path
from R284DT_seven_window_affine_checker import residue,fast_observe,P,q3,FROZEN_SHA

FIELDS=('X','Y','Z','U2','U1','U0','W','R')

def classify(X,Y,Z,U2,U1,U0,W,R):
    if X:
        if W: return 55
        return 32 if U2 and (R or U1 and (Y or U0 and Z)) else 56
    if W:
        return 21 if U2 or R and (U1 or Y or U0 and Z) else 45
    return 44 if U2 and (R or U0 or U1 or Y or Z) or R and (U1 and Y or U0 and U1 and Z or U0 and Y and Z) else 63

def verify():
    rows={};count=Counter();qcount=Counter(); digest=hashlib.sha256()
    for bits in itertools.product((0,1),repeat=8):
        X,Y,Z,U2,U1,U0,W,R=bits
        low=1056+(X<<9)+(Y<<8)+(Z<<4)
        up=(U2<<3)+(U1<<2)+(U0<<1)
        i=(up<<12)|low|(W<<6)|R
        j=i^4096
        xi=residue(i);xj=residue(j)
        di,label_i=fast_observe(xi)
        dj,label_j=fast_observe(xj)
        lbl=classify(*bits)
        assert lbl==label_i==label_j
        assert (xj-xi)%P==(-q3(i&4095))%P
        rows[bits]=lbl;count[lbl]+=1;qcount[abs(di-dj)]+=1
        digest.update(bytes(bits)+bytes((lbl,)))
    assert len(rows)==256 and count==Counter({21:45,32:21,44:37,45:19,55:64,56:43,63:27})
    assert qcount==Counter({60:192,59:64})
    support={};witnesses={}
    for k,field in enumerate(FIELDS):
        examples=[]
        for a,l in rows.items():
            if a[k]: continue
            b=tuple(v ^ (j==k) for j,v in enumerate(a))
            if rows[b]!=l:examples.append((a,b,l,rows[b]))
        assert examples
        support[field]=len(examples)
        witnesses[field]={'input0':list(examples[0][0]),'input1':list(examples[0][1]),
                          'labels':[examples[0][2],examples[0][3]]}
    assert support=={'X':128,'Y':11,'Z':5,'U2':65,'U1':13,'U0':5,'W':128,'R':31}
    return {'schema':'R284DU_BOOLEAN_WINNER_LABEL_CERTIFICATE_V1','status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
            'source':'R284CO frozen det; R284DT seven certified windows; R284DQ eight skeletons',
            'frozen_sha256':FROZEN_SHA,
            'domain':'512 witness endpoint states (256 quotient by upper bit0)',
            'boolean_input_order':list(FIELDS),'input_cases':len(rows),
            'all_first_endpoints_match_exact_affine_winner':True,
            'all_partner_endpoints_match_same_label':True,
            'truth_table_sha256':digest.hexdigest(),'winner_counts':dict(sorted(count.items())),
            'pair_gaps':dict(sorted(qcount.items())),'essential_coordinate_edge_counts':support,
            'coordinate_indispensability_witnesses':witnesses,
            'frozen_upper_bit0_not_needed_for_label':True,
            'det_or_arc_calls_in_boolean_label_classifier':0,'review':'NOT_REVIEWED'}

if __name__=='__main__':
    cert=verify()
    path=Path(__file__).with_name('R284DU_boolean_winner_classifier_certificate.json')
    path.write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps(cert,ensure_ascii=False,indent=2))
