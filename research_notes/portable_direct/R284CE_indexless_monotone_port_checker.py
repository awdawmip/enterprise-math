#!/usr/bin/env python3
"""R284CE: exact standard-library reproduction of indexless Port arcs."""
from itertools import permutations, product
from hashlib import sha256
from collections import defaultdict
import json
from pathlib import Path

P = 17179869143
D = (1120832, 6, 13, 1651128)
Z = (0, 390139, 394465, 1497639)
SELECTED = (0,1,2,4,5,6)
SUFFIX = (3,7,8,9,10,11)
PERMS = [(p, -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1)
         for p in permutations(range(4))]


def det(a):
    return sum(sign*a[0][p[0]]*a[1][p[1]]*a[2][p[2]]*a[3][p[3]]
               for p,sign in PERMS)


def matrix(l, top):
    u1,a11,x,y,u2,w,a22,z,u3,g,h,r=l
    c=[[1+(top>>j&1) for j in range(4)],
       [u1,a11,x,y],[u2,w,a22,z],[u3,g,h,r]]
    m=[[-c[i][j] for j in range(4)] for i in range(4)]
    for i in range(4): m[i][i]+=D[i]
    for j in (1,2,3): m[0][j]-=Z[j]
    return m


def formula(l,top):
    u1,a11,x,y,u2,w,a22,z,u3,g,h,r=l
    t,s=6-a11,13-a22
    u=t*s-x*w
    v=-r*u-z*(t*h+x*g)-y*(w*h+s*g)
    p1,p2=s*u1+x*u2,t*u2+w*u1
    q1=-r*p1-u1*z*h+x*z*u3+y*(u2*h+s*u3)
    q2=-r*p2+t*z*u3+u1*z*g+y*(w*u3-u2*g)
    q3=u*u3+p1*g+p2*h
    k=(u*D[3]+v,p1*D[3]+q1,p2*D[3]+q2,q3)
    base=D[0]*k[0]-Z[1]*k[1]-Z[2]*k[2]-Z[3]*k[3]-sum(k)
    return base-sum(k[j] for j in range(4) if (top>>j)&1)


def lower_for_key(key, nonselected_value):
    l=[nonselected_value]*12
    for j,pos in enumerate(SELECTED):
        l[pos]=1+((key>>(5-j))&1)
    return tuple(l)


def mobius(a):
    a=list(a)
    for j in range(6):
        for m in range(64):
            if m&(1<<j): a[m]-=a[m^(1<<j)]
    return a


def evaluate(coeff,key,mod=None):
    total=sum(c for mask,c in enumerate(coeff) if mask&key==mask)
    return total%mod if mod else total


def max_overlap_closed(arcs):
    mod=2*P
    events=defaultdict(list)
    for a,w in arcs:
        lo=(2*a-59)%mod
        hi=lo+2*w+118
        if hi<mod:
            events[lo].append(1); events[hi].append(-1)
        elif hi>mod:
            events[lo].append(1);events[mod].append(-1)
            events[0].append(1);events[hi-mod].append(-1)
        else:
            events[lo].append(1);events[mod].append(-1)
            events[0].append(1);events[0].append(-1)
    active=best=witness=0
    for x in sorted(events):
        # Starts are counted first, to include exact closed interval endpoints.
        for e in sorted(events[x],reverse=True):
            active+=e
            if x<mod and active>best: best,witness=active,x
    assert active==0
    return best,witness


def main():
    cert=json.loads(Path(__file__).with_name(
        'R284CE_indexless_monotone_port_verification.json').read_text())
    assert cert['model']['p']==P
    v=(10,12,5,1)
    row_lower=[]
    for i in range(4):
        lo=(D[i]-2)*v[i]-sum((2+Z[j] if i==0 else 2)*v[j]
                                  for j in range(4) if j!=i)
        row_lower.append(lo)
    assert row_lower==[3056632,16,9,1651072]
    assert row_lower==cert['uniform_lower_bound_Mv']

    arcs=[]; all_words=[]
    for key in range(64):
        # Each group contains exactly 64 lower states x 16 top states.
        l_lo=lower_for_key(key,2); l_hi=lower_for_key(key,1)
        bottom=formula(l_lo,15)
        top=formula(l_hi,0)
        assert bottom==det(matrix(l_lo,15))
        assert top==det(matrix(l_hi,0))
        width=top-bottom
        assert 0<width<P//2
        start=bottom%P
        arcs.append((start,width))
        words=[]
        for suffix in product((1,2),repeat=6):
            lower=list(l_hi)
            for pos,val in zip(SUFFIX,suffix):lower[pos]=val
            for row in range(16):
                residue=formula(lower,row)%P
                assert (residue-start)%P<=width
                words.append(residue);all_words.append(residue)
        words.sort()
        gaps=[words[j+1]-words[j] for j in range(1023)]
        gaps.append(P+words[0]-words[-1])
        biggest=max(gaps)
        assert gaps.count(biggest)==1
        pos=gaps.index(biggest)
        assert words[(pos+1)%1024]==start
        assert width==P-biggest

    assert len(all_words)==65536 and len(set(all_words))==65536
    sorted_words=sorted(all_words)
    min_gap=min([sorted_words[i+1]-sorted_words[i] for i in range(65535)]
                +[P+sorted_words[0]-sorted_words[-1]])
    assert min_gap==59==cert['min_global_codeword_circular_gap']
    assert min(w for a,w in arcs)==cert['arc_span_min']
    assert max(w for a,w in arcs)==cert['arc_span_max']
    asc=mobius([a for a,w in arcs])
    wc=mobius([w for a,w in arcs])
    masks=[i for i in range(64) if asc[i]%P or wc[i]]
    assert masks==[0,1,2,4,8,10,12,16,17,20,32,33,34]
    calculated=[[i,asc[i]%P,wc[i]] for i in masks]
    assert calculated==cert['coefficient_pairs_sorted_mask_alpha_mod_p_beta']
    assert all((evaluate(asc,g,P),evaluate(wc,g))==arcs[g] for g in range(64))
    digest_arcs=sha256(''.join(f'{a}:{w}\n' for a,w in arcs).encode()).hexdigest()
    assert digest_arcs==cert['group_arc_ascii_sha256']
    overlap,witness=max_overlap_closed(arcs)
    assert overlap==4==cert['max_closed_59_over_2_arc_overlap']
    assert witness==cert['closed_overlap_witness_doubled_position']
    lower_order=list(product((1,2),repeat=12))
    top_order=[sum((b-1)<<j for j,b in enumerate(row))
               for row in product((1,2),repeat=4)]
    src=sha256(b''.join((formula(l,top)%P).to_bytes(8,'big')
                         for top in top_order for l in lower_order)).hexdigest()
    assert src==cert['frozen_codeword_sha256']
    print(json.dumps({'status':'PASS','all_matrices':65536,
      'group_count':64,'crosschecked_extremizer_determinants':128,
      'min_gap':min_gap,'max_group_overlap':overlap,
      'group_arc_sha256':digest_arcs,'frozen_codeword_sha256':src},indent=2))


if __name__=='__main__':
    main()
