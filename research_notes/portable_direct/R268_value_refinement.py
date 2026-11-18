#!/usr/bin/env python3
"""R268: exact F13 value-profile refinement of R267 support classes.
Scientific frozen pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
"""
from fractions import Fraction as F
from collections import defaultdict
from math import ceil, log2
from pathlib import Path
import json, hashlib

s=F(67,169); J=1184397599; T=989553240; K=3805974000
P=13; PERIOD=2184
w=(144,576,1440,4320,17280,86400,518400)

def mul(poly,root):
    ans=[F(0)]*(len(poly)+1)
    for j,c in enumerate(poly):
        ans[j]-=c*root
        ans[j+1]+=c
    return ans

def cp(ids,a,b):
    poly=[F(1)]
    for i in ids: poly=mul(poly,a[i])
    for i in ids:
        q=[F(1)]
        for j in ids:
            if j!=i: q=mul(q,a[j])
        for j,c in enumerate(q): poly[j]-=b[i]*c
    return poly

def run():
    tau=(1691*s-2615)/(2615*s-3539)
    a=[F(1,5),F(1,4),F(3,10),F(9,20),s,F(2,3),tau]
    b=[F(13,60)]+[F(5,18)*abs(F(1,2)-a[i]) for i in range(1,7)]
    pi=[b[i]/(1-a[i]) for i in range(7)]
    z=sum(b[i]/(1-a[i])**2 for i in range(7))
    rho=[b[i]/(z*(1-a[i])**2) for i in range(7)]
    assert sum(pi)==1
    sequences={}; taps=0; max_degree=0
    for m in range(63):
        ids=[0]+[i+1 for i in range(6) if (m>>i)&1]
        d=len(ids); taps+=d; max_degree=max(max_degree,d)
        poly=[c*T**(d-i) for i,c in enumerate(cp(ids,a,b))]
        assert all(c.denominator==1 for c in poly)
        coeff=[int(c)%P for c in poly]
        state=[F(1)]*d; seq=[]
        for k in range(3+d):
            if k>=3:
                q=F(J*T**k,K)*w[m.bit_count()]*sum(rho[i]*state[j] for j,i in enumerate(ids))
                assert q.denominator==1
                seq.append(int(q)%P)
            total=sum(pi[i]*state[j] for j,i in enumerate(ids))
            state=[a[i]*state[j]+(1-a[i])*total for j,i in enumerate(ids)]
        for n in range(d,PERIOD+d):
            seq.append(-sum(coeff[j]*seq[n-d+j] for j in range(d))%P)
        assert seq[:d]==seq[PERIOD:PERIOD+d],('periodicity',m)
        sequences[m]=tuple(seq[:PERIOD])
    assert taps==249 and max_degree==6
    support_groups=defaultdict(list); value_groups=defaultdict(list)
    for m,v in sequences.items():
        support_groups[tuple(int(bool(x)) for x in v)].append(m)
        value_groups[v].append(m)
    assert len(support_groups)==7
    assert sorted(min(g) for supp,g in support_groups.items() if any(supp))==[9,10,12,13,24,26]
    assert len(support_groups[tuple([0]*PERIOD)])==39
    assert sum(any(v[i] for v in sequences.values()) for i in range(PERIOD))==2182
    witness=None
    bool_profiles={m:tuple(bool(x) for x in v) for m,v in sequences.items()}
    for k in range(PERIOD):
        for m in range(63):
            for n in range(m+1,63):
                if sequences[m][k]!=sequences[n][k] and bool_profiles[m]==bool_profiles[n]:
                    witness={
                        'labels':[m,n], 'k':k+3,
                        'residues':[sequences[m][k],sequences[n][k]],
                        'boolean_outputs':[bool(sequences[m][k]),bool(sequences[n][k])],
                        'shift_a':int((-sequences[m][k])%P),
                        'translated_zeros':[1, int((sequences[n][k]-sequences[m][k])%P==0)]
                    }
                    break
            if witness:break
        if witness:break
    assert witness is not None
    details=[]
    for supp,labels in sorted(support_groups.items(),key=lambda e:min(e[1])):
        details.append({
            'support_class_representative':min(labels),'labels':labels,
            'class_size':len(labels),
            'distinct_residue_profiles':len({sequences[m] for m in labels}),
            'nonzero_phases':sum(supp)
        })
    hist=defaultdict(int)
    for labels in value_groups.values():hist[len(labels)]+=1
    first_prefix=next(L for L in range(1,250)
                      if len({seq[:L] for seq in sequences.values()})==len(value_groups))
    histogram=defaultdict(int)
    for i in range(PERIOD):
        histogram[len({v[i] for v in sequences.values()})]+=1
    result={
        'schema':'R268_EXACT_MOD13_PROFILE_REFINEMENT_V1',
        'pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
        'parameter':'67/169','modulus':13,'k_start':3,'joint_period':PERIOD,
        'source_count':63,'integer_recurrence_taps':taps,
        'max_recurrence_degree':max_degree,
        'support_classes':len(support_groups),
        'residue_profile_classes':len(value_groups),
        'minimum_prefix_distinguishing_all_profiles':first_prefix,
        'short_prefixes_all_labels':{str(m):list(sequences[m][:first_prefix]) for m in range(63)},
        'distinct_residues_per_event_histogram':{str(k):v for k,v in sorted(histogram.items())},
        'support_details':details,
        'exact_class_size_histogram':{str(k):v for k,v in sorted(hist.items())},
        'residue_profile_labels':[labels for v,labels in sorted(value_groups.items(),key=lambda x:min(x[1]))],
        'same_support_different_value_witness':witness,
        'bits_to_index_support_profiles':ceil(log2(len(support_groups))),
        'bits_to_index_full_residue_profiles':ceil(log2(len(value_groups))),
        'validation':'63 exact rational initializations, 249 integer-scaled recurrence taps; complete 2184-step period per mask checked against d initial values; exhaustive value and Boolean partitions.'
    }
    assert first_prefix==2
    assert len(value_groups)==25
    assert witness['labels']==[9,14] and witness['k']==3
    out=Path(__file__).with_name('R268_verification.json')
    out.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+'\n')
    print('R268 PASS',len(support_groups),len(value_groups),first_prefix,witness)
    print('verification_sha256',hashlib.sha256(out.read_bytes()).hexdigest())
    return result

if __name__=='__main__':run()
