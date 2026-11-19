"""Reconstruct exact kernel enclosures and verify the two signed-budget enumerations."""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import comb, isqrt
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
L, BUDGET = 5040, 2332
SHIFT, STAR, PROJ = 2**20, 4096, 16384


def determinant(rows):
    a = [r[:] for r in rows]
    n = len(a)
    previous, sign = 1, 1
    for j in range(n-1):
        k = next((i for i in range(j,n) if a[i][j]), None)
        if k is None:
            return 0
        if k != j:
            a[j],a[k] = a[k],a[j]
            sign = -sign
        for i in range(j+1,n):
            coeff = a[i][j]
            for t in range(j+1,n):
                new = a[j][j]*a[i][t]-coeff*a[j][t]
                a[i][t], remainder = divmod(new,previous)
                assert remainder == 0
        previous = a[j][j]
    return sign*a[-1][-1]


def certify_basis():
    raw = (ROOT/'moments_basis.json').read_bytes()
    data = json.loads(raw)
    ds, k = data['denominators'],data['signed_basis']
    assert data['grid']==L and ds==[d for d in range(2,BUDGET+2) if L%d==0]
    assert len(ds)==57 and len(k)==50 and all(len(row)==len(ds) for row in k)
    xs = [L//d for d in ds]
    matrix = [[comb(x,j) for x in xs] for j in range(7)]
    assert all(sum(a*b for a,b in zip(row,moment))==0 for row in k for moment in matrix)
    keep = [i for i,x in enumerate(xs) if x not in range(3,10)]
    minor = determinant([[row[i] for i in keep] for row in k])
    index = determinant([[comb(x,j) for x in range(3,10)] for j in range(7)])
    assert abs(minor)==index==1
    return ds, [[z*(d-1) for z,d in zip(row,ds)] for row in k], dict(
        basis_sha256=sha256(raw).hexdigest(), projected_kernel_minor=minor,
        consecutive_binomial_minor=index, omitted_reciprocals=list(range(3,10)))


def input_data(ds,rows):
    n = len(ds)
    stars,lengths = [],[]
    head = [[len(rows),n,BUDGET],ds]
    projector = [[F(int(j==k)) for k in range(n)] for j in range(n)]
    tail = []
    for row in rows:
        mu, star = [],list(map(F,row))
        for u,norm in zip(stars,lengths):
            v = sum(a*b for a,b in zip(row,u))/norm
            mu.append(v)
            star=[a-v*b for a,b in zip(star,u)]
        norm=sum(v*v for v in star)
        assert norm>0
        bound=F(2*BUDGET**2*SHIFT**2)/norm
        head.append(row+[v*SHIFT//1 for v in mu]+[v*STAR//1 for v in star]
                    +[isqrt(bound.numerator//bound.denominator)+1,
                      max(abs(v) for v in star).__ceil__()])
        # P_i annihilates the as-yet-unassigned rows b_0,...,b_(i-1).
        for j in range(n):
            tail.append([(-((-x*PROJ)//1)) for x in projector[j]])
        dual=[v/norm for v in star]
        for j in range(n):
            for k in range(j,n):
                projector[j][k] -= star[j]*dual[k]
                projector[k][j] = projector[j][k]
        stars.append(star)
        lengths.append(norm)
    return '\n'.join(' '.join(map(str,r)) for r in head+tail)+'\n'


def run(exe,data,ds,mode):
    p=subprocess.run([str(exe),mode],input=data,text=True,capture_output=True,check=True)
    hits=[]
    receipt={}
    for line in p.stdout.splitlines():
        kind,*vals=line.split()
        ns=list(map(int,vals))
        if kind=='HIT':
            left,right,*z=ns
            assert len(z)==len(ds)
            assert left==sum((d-1)*max(0,u) for d,u in zip(ds,z))
            assert right==sum((d-1)*max(0,-u) for d,u in zip(ds,z))
            moments=[sum(F(u,d**j) for d,u in zip(ds,z)) for j in range(8)]
            assert moments[:7]==[0]*7 and moments[7]!=0
            observed_seventh=sum(u*(1-F(1,d))**7 for d,u in zip(ds,z))
            assert observed_seventh==-moments[7]
            hits.append(dict(positive=left,negative=right,seventh_H_difference=str(observed_seventh),
                             signed={d:u for d,u in zip(ds,z) if u}))
        elif kind=='NODES':
            receipt['visited_by_remaining_dimension']=ns
        elif kind=='CUTS':
            receipt['rejected_by_remaining_dimension']=ns
        elif kind=='BOUNDS':
            receipt['max_sum_abs_digits'],receipt['max_field_error_scale32']=ns
        else:
            raise ValueError(line)
    assert {tuple((r['positive'],r['negative'])) for r in hits}=={(2332,2276),(2276,2332)}
    assert len(hits)==2 and hits[0]['signed']=={d:-u for d,u in hits[1]['signed'].items()}
    receipt['accepted_including_both_orientations']=hits
    receipt['visited_total']=sum(receipt['visited_by_remaining_dimension'])
    receipt['rejected_total']=sum(receipt['rejected_by_remaining_dimension'])
    return receipt


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cxx',default='c++')
    p.add_argument('--tight-only',action='store_true',help='run only the separating-hyperplane variant')
    args=p.parse_args()
    ds,rows,certificate=certify_basis()
    data=input_data(ds,rows)
    with tempfile.TemporaryDirectory() as d:
        exe=Path(d)/'signed_enumeration'
        subprocess.run([args.cxx,'-std=c++17','-O3','-fsanitize=signed-integer-overflow',
                        '-fno-sanitize-recover=signed-integer-overflow',str(ROOT/'moments_enum.cpp'),
                        '-o',str(exe)],check=True)
        modes=['tight'] if args.tight_only else ['tight','basic']
        results={mode:run(exe,data,ds,mode) for mode in modes}
    assert results['tight']['visited_by_remaining_dimension'][0]==5
    if 'basic' in results:
        assert results['basic']['visited_by_remaining_dimension'][0]==97
        assert results['basic']['accepted_including_both_orientations']==results['tight']['accepted_including_both_orientations']
    print(json.dumps(dict(grid=L,budget_per_side=BUDGET,kernel_rank=len(rows),
                          denominators=ds,basis_certificate=certificate,
                          integer_input_sha256=sha256(data.encode()).hexdigest(),
                          runs=results),sort_keys=True,indent=2))


if __name__=='__main__':
    main()
