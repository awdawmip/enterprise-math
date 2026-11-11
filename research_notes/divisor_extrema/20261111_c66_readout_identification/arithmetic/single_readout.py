"""Deterministic finite-field separation of all measured H values; Python 3 and g++.

Builds block/terminal coefficients from rational model sources, checks small cases
against the three-tail exact reference, and calls the fast projective enumerator.
"""
import argparse
from fractions import Fraction
from math import comb
from pathlib import Path
import json
import subprocess
import sys
import tempfile

PRIME = 2**61 - 1


def reduce_field(value):
    value = Fraction(value)
    return value.numerator * pow(value.denominator, -1, PRIME) % PRIME


def gap_rank(gaps):
    """Zero-based lexicographic rank among weak compositions of the fixed total."""
    left=sum(gaps)
    rank=0
    for index,value in enumerate(gaps[:-1]):
        later=len(gaps)-1-index
        rank+=sum(comb(left-m+later-1,later-1) for m in range(value))
        left-=value
    return rank


def sample_words(k):
    size=k+1
    paths=[(1,)*(k-1)+(0,0), (k-1,)+(0,)*k, (0,)*k+(k-1,)]
    mixed=[0]*size
    for i in range(k-1):
        mixed[(i*i+5*i+3)%size]+=1
    return paths+[tuple(mixed)]


def run(model, max_full, max_cut):
    sys.path.insert(0, str(model.resolve()))
    from observed_four import tail_forms
    from suffix_limits import all_gaps, block
    from observable_minimum import hilbert_ratio

    nmax = max(max_full, max_cut)
    rows = [str(nmax)]
    for stock in range(2, nmax+2):
        forms = tail_forms(stock)
        # Extreme columns derived also directly by the real affine log-slopes.
        ranked = sorted(forms, key=lambda row: row[0]/row[1])
        hi, lo = ranked[-1], ranked[0]
        assert hi[0]*lo[1] > lo[0]*hi[1]
        rows.append(' '.join(str(reduce_field(z)) for z in (*hi,*lo)))
    for r in range(1, nmax+1):
        for stock in range(2, nmax+2):
            for m in range(stock-1):
                a,b,c,d = block(r,stock,m)
                assert a == 0 and b > 0 and c != 0
                rows.append(f'{b%PRIME} {c%PRIME} {d%PRIME} {int(c>0)}')
    requests = [('full',k) for k in range(2,max_full+1)]
    if max_cut>=max_full: # lower cuts are certified by the tested full families
        requests.extend(('cut',q) for q in range(max(2,max_full),max_cut+1))
    for family,n in requests:
        rows.append(f'{family} {n}')
        if family=='full':
            reference=(sorted((i,reduce_field(hilbert_ratio(n,path))) for i,path in enumerate(all_gaps(n)))
                       if n<=7 else sorted((gap_rank(path),reduce_field(hilbert_ratio(n,path))) for path in sample_words(n)))
        else:
            reference=[]
        rows.append(str(len(reference)))
        rows.extend(f'{i} {v}' for i,v in reference)
    with tempfile.TemporaryDirectory() as temp:
        executable = Path(temp)/'census'
        subprocess.run(['g++','-O3','-std=c++17',str(Path(__file__).with_suffix('.cpp')),'-o',str(executable)], check=True)
        ret = subprocess.run([str(executable)],input='\n'.join(rows)+'\n',text=True,stdout=subprocess.PIPE,check=True)
    results=[]
    lines=ret.stdout.splitlines()
    joint=[row.split() for row in lines if row.startswith('joint ')]
    assert len(joint)==1
    _,joint_count,joint_duplicates=joint[0]
    assert int(joint_count)==sum(comb(2*k-1,k) for k in range(2,max_full+1))
    assert int(joint_duplicates)==0,ret.stdout
    family_rows=[row for row in lines if not row.startswith('joint ')]
    for (family,n),line in zip(requests,family_rows,strict=True):
        tag,size,count,repeat,total,least,greatest = line.split()
        assert (tag,int(size))==(family,n) and int(count)==comb(2*n-1,n)
        # Zero modular coincidences proves exact rational separation.
        assert int(repeat)==0, ret.stdout
        if tag=='full' and n<=7:
            exact=[reduce_field(hilbert_ratio(n,gaps)) for gaps in all_gaps(n)]
            assert (len(set(exact)),sum((i+1)*h for i,h in enumerate(exact))%PRIME,min(exact),max(exact)) == (
                int(count),int(total),int(least),int(greatest))
        results.append(dict(family=tag,scale=n,count=int(count),modular_duplicates=int(repeat),
                            enumeration_sum_mod_p=int(total),min_residue=int(least),max_residue=int(greatest)))
    return dict(prime=PRIME,inputs=[0,1],full_through=max_full,fixed_canonical_cut_through=max(max_full-1,max_cut),
                original_three_tail_rational_check_through=min(7,max_full),
                joint_full=dict(count=int(joint_count),duplicates=int(joint_duplicates)),censuses=results)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model',type=Path,required=True,help='C64 checks directory')
    parser.add_argument('--full',type=int,default=16)
    parser.add_argument('--cut',type=int,default=16)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=run(args.model,args.full,args.cut)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
