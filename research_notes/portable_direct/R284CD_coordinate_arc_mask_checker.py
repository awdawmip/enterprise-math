#!/usr/bin/env python3
"""R284CD: exhaustive coordinate-mask arc indexes; Python 3 + NumPy.
python R284CD_coordinate_arc_mask_checker.py > R284CD_recomputed.json
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json
import numpy as np

P=17179869143
D0,D3,Z1,Z2,Z3=1120832,1651128,390139,394465,1497639
M=2*P
COORDS=('u1','a11','x','y','u2','w','a22','z','u3','g','h','r')

def words_for_lower(L):
    u1,a11,x,y,u2,w,a22,z,u3,g,h,r=L
    t,s=6-a11,13-a22
    U=t*s-x*w
    V=-r*U-z*(t*h+x*g)-y*(w*h+s*g)
    p1,p2=s*u1+x*u2,t*u2+w*u1
    q1=-r*p1-u1*z*h+x*z*u3+y*(u2*h+s*u3)
    q2=-r*p2+t*z*u3+u1*z*g+y*(w*u3-u2*g)
    q3=U*u3+p1*g+p2*h
    k=(U*D3+V,p1*D3+q1,p2*D3+q2,q3)
    base=(D0*k[0]-Z1*k[1]-Z2*k[2]-Z3*k[3]-sum(k))%P
    return [(base-sum(v for j,v in enumerate(k) if bits>>j&1))%P
            for bits in range(16)]

def arcs_for_mask(words,cols,idx):
    k=len(cols)
    size=1<<(12-k)
    group=np.zeros(4096,dtype=np.int64)
    for pos in cols:
        group=2*group+((idx>>(11-pos))&1)
    arr=np.sort(words[np.argsort(group,kind='stable')].reshape(1<<k,size*16),axis=1)
    gaps=np.concatenate((np.diff(arr,axis=1),(P+arr[:,0]-arr[:,-1])[:,None]),axis=1)
    j=np.argmax(gaps,axis=1)
    return arr[np.arange(1<<k),(j+1)%(size*16)].tolist(),(P-gaps[np.arange(1<<k),j]).tolist()

def overlap(starts,widths):
    # Doubled circular coordinate for exact closed radius 59/2.
    events=[]
    for a,w in zip(starts,widths):
        lo=(2*a-59)%M
        length=2*w+118
        assert 0<length<M
        hi=lo+length
        if hi<M: events += [(lo,1),(hi,-1)]
        elif hi>M: events += [(lo,1),(M,-1),(0,1),(hi-M,-1)]
        else: events += [(lo,1),(M,-1),(0,1),(0,-1)]
    events.sort(key=lambda e:(e[0],-e[1]))  # inclusive ends
    active=peak=at=0
    for x,d in events:
        active+=d
        if x<M and active>peak: peak,at=active,x
    assert active==0
    return peak,at,events

def independent_endpoint_check(starts,widths,events,peak):
    coords={0}|{x for x,d in events if x<M}
    assert peak==max(sum(((x-2*a+59)%M)<=2*w+118
                         for a,w in zip(starts,widths)) for x in coords)
    return len(coords)

def main():
    words=np.array([words_for_lower(L) for L in product((1,2),repeat=12)],dtype=np.int64)
    tops=[sum((v-1)<<j for j,v in enumerate(row)) for row in product((1,2),repeat=4)]
    digest=sha256(b''.join(int(words[i,b]).to_bytes(8,'big') for b in tops for i in range(4096))).hexdigest()
    assert digest=='b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4'
    idx=np.arange(4096,dtype=np.int64)
    results={}
    score=[]
    expected=(1,2,4,6,8,8,4,7,13,22,39,70,128)
    for k in range(13):
        cases=[]
        for cols in combinations(range(12),k):
            starts,widths=arcs_for_mask(words,cols,idx)
            peak,witness,events=overlap(starts,widths)
            score.append((sum(1<<j for j in cols),peak))
            cases.append((peak,sum(widths),cols,witness,max(widths),starts,widths,events))
        best=min(cases,key=lambda x:(x[0],x[1],x[2]))
        peak,total,cols,witness,largest,starts,widths,events=best
        hist=Counter(x[0] for x in cases)
        assert peak==expected[k]
        if k in (6,7):
            assert list(cols)==([0,1,2,4,5,6] if k==6 else [0,1,2,4,5,6,8])
            assert hist[peak]==1
            checked=independent_endpoint_check(starts,widths,events,peak)
        else: checked=None
        entry={'groups':1<<k,'masks_tested':len(cases),'best_overlap':peak,
               'number_best_masks':hist[peak], 'best_mask':[COORDS[j] for j in cols],
               'best_mask_positions_zero_based':list(cols),
               'max_lower_checks':peak*(1<<(12-k)),
               'max_top_thresholds':4*peak*(1<<(12-k)),
               'peak_witness_doubled_coordinate':witness,
               'largest_covering_arc_width':largest,'sum_covering_arc_widths':total}
        if k in (6,7):
            entry['arc_pairs']=[[a,w] for a,w in zip(starts,widths)]
            entry['direct_checked_endpoint_count']=checked
        results[str(k)]=entry
    assert len(score)==4096 and len({a for a,b in score})==4096
    stream=''.join(f'{m:04d}:{v:03d}\n' for m,v in sorted(score))
    report={'schema':'EM_R284CD_EXACT_COORDINATE_ARC_MASK_FRONTIER_V1',
            'R284BZ_R284CC_codeword_sha256':digest,
            'all_4096_mask_peaks_sha256':sha256(stream.encode('ascii')).hexdigest(),
            'mask_peak_hash_format':'sorted (mask,peak) ascending mask, line %04d:%03d newline',
            'noise_radius':'rho<59/2',
            'all_binary_4_by_4_matrices':65536,
            'coordinate_names':COORDS,'results_by_selected_coordinate_count':results,
            'status':'AUTHOR_FINITE_EXACT_NOT_INDEPENDENTLY_REVIEWED'}
    assert report['all_4096_mask_peaks_sha256']=='d18f850b3240eba3c369f3860ef103f90c26476986e7caa119c24b43b4d6dc2e'
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
