#!/usr/bin/env python3
"""Independent Q19 source-fiber census of previously certified W21/W23 non-diagonal IDs.
Usage: python PREFIX956B_R6_JOINT_FIBER_AUDIT.py <PREFIX955 zip or source .bin>
Verifies SHA256 before work. Scans original XOR equation (not determinant inverse).
"""
import struct, hashlib, json, collections, zipfile, sys
from pathlib import Path
HERE=Path(__file__).parent
ZIP=Path(sys.argv[1]) if len(sys.argv)>1 else HERE/'PREFIX955_R6_quotient_fiber_verified_reproduction.zip'
EXPECTED='1caec71f97ddb97c60c8506629f65651f0f3030b3526aeca30195948ee0cff75'
P=19; H=1<<(P-1); Q0=H+1; N=1<<(P-2)

def fibers(k,a,b):
    x=k*a
    res=collections.defaultdict(list)
    for j in range(P):
        flip=x^(1<<j)
        for i in range(P):
            y=flip-(1<<i)
            if y>0 and y % b == 0:
                res[y//b].append((i,j))
    return dict(res)

def count_formula(x,d,p):
    if d==0:return p-(x&((1<<p)-1)).bit_count()
    z=abs(d); u=(z&-z).bit_length()-1; odd=z>>u
    m=(odd&(odd+1))==0
    if d<0: return int(m and u+odd.bit_length()<p and not ((x>>(u+odd.bit_length()))&1))
    n=int(m and u+odd.bit_length()<p and not ((x>>u)&1))
    if z.bit_count()==1:
        h=z.bit_length()-1
        n+=int(1<=h<=p and ((x>>(h-1))&1)!=0)
    elif z.bit_count()==2:
        v=(z^(1<<u)).bit_length()-1
        if v<p: n+=((x>>u)&1)+((x>>v)&1)
    return n

def main():
    if ZIP.suffix.lower()=='.zip':
        with zipfile.ZipFile(ZIP) as z:
            data=z.read('PREFIX955_NONDIAGONAL_IDS.bin')
    else:
        data=ZIP.read_bytes()
    assert hashlib.sha256(data).hexdigest()==EXPECTED
    assert len(data)==6203*8
    pairs=[struct.unpack_from('<Q',data,8*i)[0] for i in range(6203)]
    assert pairs==sorted(set(pairs))
    per_pair_mask=collections.Counter()
    joint_mult=collections.Counter(); fcount=collections.Counter()
    zeros=[0,0]; zero_cases=[]
    doubled=[0,0]; doub_examples=[]
    total_joint=0; any_zero_pairs=0
    multi_gap=[]; max_joint_pair=(None,0)
    per_gap_joint=collections.Counter(); per_gap_unique=collections.Counter()
    for ident in pairs:
        a=Q0+2*(ident//N); b=Q0+2*(ident%N)
        assert a!=b and Q0<=a<=2*H-1 and Q0<=b<=2*H-1
        f21=fibers(21,a,b); f23=fibers(23,a,b)
        assert f21 and f23
        gap_to_count=collections.Counter()
        zero_found=False
        for idx,(k,fs) in enumerate([(21,f21),(23,f23)]):
            for t, w in fs.items():
                d=k*a-t*b
                assert len(w)==count_formula(k*a,d,P), (a,b,k,t,d,w)
                if d==0:
                    zeros[idx]+=1; zero_cases.append((a,b,k,t,len(w)))
                    zero_found=True
                elif len(w)==2:
                    doubled[idx]+=1
                    if len(doub_examples)<10: doub_examples.append((a,b,k,t,d,w))
                elif len(w)>2:
                    raise AssertionError((a,b,k,t,d,w))
                fcount[(k,len(w),d==0)]+=1
        any_zero_pairs+=zero_found
        for t,w1 in f21.items():
            for T,w2 in f23.items():
                m=T-t
                assert 0<=m<=6,(a,b,t,T)
                gap_to_count[m]+=len(w1)*len(w2)
                per_gap_joint[m]+=len(w1)*len(w2)
                per_gap_unique[m]+=1
        mask=sum(1<<m for m in gap_to_count)
        per_pair_mask[mask]+=1
        if len(gap_to_count)>1:multi_gap.append({'a':a,'b':b,'gaps':dict(gap_to_count)})
        j=sum(gap_to_count.values())
        joint_mult[j]+=1
        total_joint+=j
        if j>max_joint_pair[1]:max_joint_pair=((a,b),j)
    out={
        'schema':'PREFIX956B_R6_Q19_JOINT_FIBER_AUDIT_V1',
        'scientific_input_commit':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'source':'PREFIX955_NONDIAGONAL_IDS.bin',
        'source_sha256':EXPECTED,
        'input_pairs':len(pairs),'all_input_pairs_source_verified':True,
        'per_gap_joint_named_witness_combinations':dict(sorted(per_gap_joint.items())),
        'per_gap_distinct_quotient_pairs_sum':dict(sorted(per_gap_unique.items())),
        'total_joint_named_witness_combinations':total_joint,
        'joint_named_multiplicity_histogram_per_moduli_pair':dict(sorted(joint_mult.items())),
        'gap_mask_histogram':dict(sorted(per_pair_mask.items())),
        'multi_gap_pairs':multi_gap,
        'single_core_nonzero_double_fibers':{'21':doubled[0],'23':doubled[1]},
        'single_core_zero_offset_fibers':{'21':zeros[0],'23':zeros[1]},
        'moduli_pairs_with_at_least_one_single_core_zero_offset':any_zero_pairs,
        'zero_offset_examples':zero_cases[:12],
        'double_fiber_examples':doub_examples,
        'largest_total_named_joint_multiplicity_moduli_pair':max_joint_pair,
        'total_single_core_quotient_fibers_count_by_type':{str(key):count for key,count in sorted(fcount.items())},
        'algorithm':'complete direct XOR named i,j enumeration for both cores for every certified non-diagonal pair; exact formula checked independently on every realized quotient fiber',
        'review_status':'AUTHOR_EXACT_FINITE_COMPUTATION; INDEPENDENT_MATH_REVIEW_PENDING'
    }
    target=HERE/'PREFIX956B_R6_JOINT_RESULTS.json'
    target.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('double_fiber_examples','total_single_core_quotient_fibers_count_by_type')},indent=2))

if __name__=='__main__':main()
