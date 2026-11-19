"""Positive-source checks and exact finite optimization for approximate return."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import hashlib
from itertools import combinations, permutations, product
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
TASK = 'research_tasks/RS-EULER-RECORDER-A03-CALIBRATION-REUSE-20261012.md'


def shell_weights(m,d):
    """Integer numerator proportional to the Green occupancy of each labelled state."""
    scale = 1
    while scale < d:
        scale *= m
    level = 1
    weights = []
    for i in range(1,d+1):
        if i > level:
            level *= m
        weights.append(scale//level)
    return weights


def sharp_value(m,d):
    power = 1
    depth = 0
    while power*m <= d:
        power *= m
        depth += 1
    return 1/(depth+1 + F(d,power*(m-1)))


def fixed_error(m,weights):
    weights = sorted(weights,reverse=True)
    return sum(max(F(0), F(m*a-weights[i//m],m)) for i,a in enumerate(weights))/sum(weights)


def solve(matrix, rhs):
    rows = [[F(q) for q in row]+[F(b)] for row,b in zip(matrix,rhs)]
    n = len(rows)
    for col in range(n):
        k = next((i for i in range(col,n) if rows[i][col]), None)
        if k is None:
            return None
        rows[col],rows[k] = rows[k],rows[col]
        pivot = rows[col][col]
        rows[col] = [q/pivot for q in rows[col]]
        for i in range(n):
            if i != col and rows[i][col]:
                a = rows[i][col]
                rows[i] = [v-a*w for v,w in zip(rows[i],rows[col])]
    return tuple(row[-1] for row in rows)


def vertex_check(m,d):
    # All linear regions of the sorted simplex. Enumerate their vertices independently of the Green formula.
    planes = set()
    for i in range(d):
        row = [0]*d
        row[i] = 1
        if i+1 < d:
            row[i+1] = -1
        planes.add(tuple(row))
        row = [0]*d
        row[i] += m
        row[i//m] -= 1
        planes.add(tuple(row))
    points = set()
    for active in combinations(sorted(planes),d-1):
        x = solve([(1,)*d,*active],[1]+[0]*(d-1))
        if x is not None and x[-1]>=0 and all(a>=b for a,b in zip(x,x[1:])):
            points.add(x)
    values = [(fixed_error(m,x),x) for x in points]
    best = min(z for z,x in values)
    attaining = [x for z,x in values if z==best]
    w = shell_weights(m,d)
    assert attaining == [tuple(F(a,sum(w)) for a in w)]
    assert best == sharp_value(m,d)
    return dict(m=m,d=d,vertices=len(points),best=str(best))


def all_bijections(m,weights):
    d = len(weights)
    source = [w for w in weights for _ in range(m)]
    target = [m*w for w in sorted(weights,reverse=True)]+[0]*(d*(m-1))
    best = 2*m*sum(weights)
    count = 0
    for seq in permutations(range(d*m)):
        score = sum(max(0,t-source[i]) for t,i in zip(target,seq))
        best = min(score,best)
        count += 1
    tv = F(best,m*sum(weights))
    assert tv==fixed_error(m,weights)
    return dict(m=m,weights=weights,permutations=count,tv=str(tv))


def load(repo):
    raw = (repo/TASK).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()=='7dc8fa38f2131d21ef03ea4c305bedda2fbb9cb8'
    path = HERE.parent/'ninetieth'/'recorders_check.py'
    assert hashlib.sha256(path.read_bytes()).hexdigest()=='f1af1e08c97d50ca1996796774fc6f1693fcc4ace1d9453837345a46a9d49f31'
    sys.path.insert(0,str(path.parent))
    from recorders_check import load as pinned_load, signed_unit_contact
    return pinned_load(repo),signed_unit_contact


def native(kernel,contact,d,k,shared,perfect=False):
    p=3
    m=p if shared else p**k
    occupied = d//m if perfect else d
    weights=shell_weights(m,occupied)+[0]*(d-occupied)
    norm=sum(weights)
    account=Counter()
    world_count=0
    joint=defaultdict(lambda: kernel.CWM_ZERO)
    target=Counter()
    initialized=set()
    for s in range(occupied):
        for a0,j0,sheet in product(range(p),range(p),(-1,1)):
            ref=[(a0+i)%p for i in range(k)]
            source=[(j0+i*i)%p for i in range(k)]
            base=F(weights[s],18*norm)
            target[a0,j0,sheet,s,(0,)*k]=base
            for inputs in product(range(p),repeat=1 if shared else k):
                us=inputs*k if shared else inputs
                w=kernel.cwm_edge(base/m)
                c=s
                output=[]
                if shared:
                    # Sibling scratch ports remain jointly available. Subtract original input u0 before using it.
                    prepared=[us[0]]+[(u-us[0])%p for u in us[1:]]
                    account['block_subtractions']+=k-1
                else:
                    prepared=list(us)
                for i,u in enumerate(prepared):
                    if not shared or i==0:
                        t=p*c+u
                        z,c=divmod(t,d)
                        account['radix_permutations']+=1
                    else:
                        z=u
                    initialized.add((i,ref[i],us[i]))
                    # A known offset control realizes the declared reversible permutation of (memory,raw offset).
                    ports=[source[i],ref[i],(ref[i]+us[i])%p]
                    w=contact(ports,2,z-us[i],(1,sheet),w,kernel,account)
                    assert ports[2]==(ref[i]+z)%p
                    w=contact(ports,2,source[i]-ref[i],(1,sheet),w,kernel,account)
                    assert ports[0]==source[i] and ports[1]==ref[i]
                    output.append((ports[2]-source[i])%p)
                key=(a0,j0,sheet,c,tuple(output))
                joint[key]=kernel.cwm_recoalesce(joint[key],w)
                world_count+=1
    assert sum(row.count for row in joint.values())==world_count
    joint={key:row.total for key,row in joint.items()}
    assert sum(joint.values())==sum(target.values())==1
    tv=sum(max(0,t-joint.get(q,0)) for q,t in target.items())
    failure=sum(w for (*_,z),w in joint.items() if any(z))
    assert tv==sharp_value(m,occupied)
    assert failure== (0 if perfect else tv)
    return dict(d=d,k=k,access='shared_block' if shared else 'fresh_stream',perfect=perfect,
                support=occupied,initial_integer_weights=weights,worlds=world_count,
                joint_tv=str(tv),failure=str(failure),receiver_and_control_operations=dict(account),
                reference_raw_offset_pairs_by_position=len(initialized))


def two_dates():
    verified = {}
    for p in range(2,26):
        weights=[2*p*p]+[p]*(p-1)+[2]*(p*p-p)
        e1=fixed_error(p,weights)
        e2=fixed_error(p*p,weights)
        assert e1==e2==F(3*(p-1),5*p-3)
        verified[p]=str(e1)
    def partitions(n,d,cap):
        if d==0:
            if not n:
                yield ()
            return
        for i in range(min(cap,n), (n+d-1)//d-1,-1):
            for tail in partitions(n-i,d-1,i):
                yield (i,)+tail
    count=0
    best=F(1)
    for weights in partitions(36,9,36):
        count+=1
        best=min(best,max(fixed_error(3,weights),fixed_error(9,weights)))
    assert best==F(1,2)
    w=shell_weights(9,9)
    assert fixed_error(3,w)==F(10,17) and fixed_error(9,w)==F(8,17)
    return dict(p_squared_all_p=verified,ternary_36_unit_sorted_preparations=count,
                ternary_best=str(best),terminal_two_only_first='10/17',terminal_two_only_second='8/17')


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo',type=Path,required=True)
    args=ap.parse_args()
    kernel,contact=load(args.repo.resolve())
    vertices=[vertex_check(m,d) for m,d in product((2,3,5),range(1,6))]
    perm=[all_bijections(m,x) for m,x in ((2,[3,1]),(3,[3,1]),(2,[5,3,2]),(2,[4,2,1,1]))]
    grid=0
    for m in (2,3,4,5,9,27,81):
        for d in range(1,251):
            w=shell_weights(m,d)
            assert fixed_error(m,w)==sharp_value(m,d)
            grid+=1
    cases=[native(kernel,contact,*x) for x in [(2,1,False),(7,2,False),(9,2,False),(9,2,True),
                                                (9,2,False,True),(9,2,True,True),(10,3,False)]]
    batches=[]
    for m,d in ((3,9),(3,31),(9,9),(9,95)):
        weights=shell_weights(m,d)
        losses=[]
        for n in range(1,7):
            loss=fixed_error(m**n,weights)
            assert loss==sharp_value(m,d)*sum(min(F(1),F(d,m**i)) for i in range(n))
            losses.append(str(loss))
        batches.append(dict(base=m,d=d,joint_losses=losses))
    result=dict(positive_world_models=cases,consecutive_batches=batches,global_vertex_checks=vertices,permutation_checks=perm,
                all_integer_dimensions_checked=grid, one_or_two_dates=two_dates())
    print(json.dumps(result,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
