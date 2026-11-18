"""Exact conditional bridge checks and integrity checks for the fifteen frozen interfaces."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import combinations, product
import json
from pathlib import Path
import sys


KERNEL_SHA = "4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f"
CATALOG_SHA = "492db641569d98311a5b1ac8cdd4c836c926bde1a110c3d3958d02f7cfa0ee99"
TASKSET_SHA = "67938367019efde367c045a7b6ae722ee866dbeba94978fd6ca693e90c37ad8d"
SETTINGS = tuple(product((0,1),repeat=2))
VERTICES = tuple(product((0,1),repeat=4))
ODD = tuple(v for v in VERTICES if sum(v)%2)


def l1(a,b):
    return sum(abs(x-y) for x,y in zip(a,b))


def cells(p):
    return ((1-p)/2,p/2,p/2,(1-p)/2)


def pair_from_margins(p,q,theta):
    return (1-p-q+theta,q-theta,p-theta,theta)


def route(kernel, strategies):
    """Branch identity is the full source assignment. Its normalized mass is declared input."""
    result = {}
    for x,y in SETTINGS:
        bags = defaultdict(lambda:kernel.CWM_ZERO)
        for strategy,weight in strategies:
            if not weight:
                continue
            ab = (strategy[x],strategy[2+y])
            flow = kernel.cwm_propagate(kernel.CWM_ONE,kernel.cwm_edge(weight))
            bags[ab] = kernel.cwm_recoalesce(bags[ab],flow)
        result[x,y] = tuple(bags[a,b].total for a,b in SETTINGS)
        assert sum(result[x,y])==1
    return result


def inverse(matrix):
    n = len(matrix)
    m = [[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(matrix)]
    for j in range(n):
        k = next((k for k in range(j,n) if m[k][j]),None)
        if k is None:
            return None
        m[k],m[j] = m[j],m[k]
        m[j] = [x/m[j][j] for x in m[j]]
        for i in range(n):
            if i != j and m[i][j]:
                c=m[i][j]
                m[i]=[a-c*b for a,b in zip(m[i],m[j])]
    return [row[n:] for row in m]


def simplex_tests(even):
    tests=[]
    for vertices in combinations(even,5):
        mat=[[1]*5]+[[v[j] for v in vertices] for j in range(4)]
        inv=inverse(mat)
        if inv is not None:
            # A common positive row multiplier preserves each barycentric sign.
            from math import lcm
            tests.append([[int(c*lcm(*(x.denominator for x in row))) for c in row] for row in inv])
    return tests


def in_hull(scaled, denominator, tests):
    vec = (denominator,*scaled)
    return any(all(sum(x*y for x,y in zip(row,vec))>=0 for row in test) for test in tests)


def integrity(repo):
    package=repo/'research_notes'
    taskmap=package/'DISCRETE_COMPATIBILITY_TASKSET_20261026.json'
    catalog=package/'DISCRETE_COMPATIBILITY_SOURCES_20261026.json'
    assert sha256(taskmap.read_bytes()).hexdigest()==TASKSET_SHA
    assert sha256(catalog.read_bytes()).hexdigest()==CATALOG_SHA
    refs={x['id']:x['url'] for x in json.loads(catalog.read_text())['sources']}
    frozen=json.loads(taskmap.read_text())['tasks']
    ledger=json.loads(Path(__file__).with_name('compatibility_interfaces.json').read_text())
    rows=ledger['interfaces']
    assert len(rows)==len(frozen)==15
    ready=[]
    for i,(row,task) in enumerate(zip(rows,frozen)):
        spec=task['spec']
        text=(repo/task['taskbook_path']).read_bytes()
        digest='sha1:'+sha1(b'blob '+str(len(text)).encode()+b'\x00'+text).hexdigest()
        record=json.loads((repo/task['publication_record_path']).read_text())
        assert digest==task['taskbook_blob_sha1']==record['taskbook_blob_sha1']
        assert record['publication_id']==row['publication'] and record['task_id']==row['task_id']
        assert row['uncertainty_contract'] and row['calibrated_numeric_budget'] is None
        assert row['task_id']==task['task_id'] and row['publication']==task['publication_id']
        assert row['depends_on']==spec['deps'] and row['source_ids']==spec['sources']
        assert row['source_links']==[refs[k] for k in spec['sources']]
        assert row['experiment_executed'] is False and row['successor_result'] is None
        if row['eligible_after_00_for_interface_audit']:
            ready.append(i)
            assert spec['deps']==[0]
    assert ready==[1,2,3,4,8,9,12]
    return ready


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',required=True,type=Path)
    parser.add_argument('--json',type=Path)
    args=parser.parse_args()
    ready=integrity(args.repo)
    core=args.repo/'src/enterprise_math/brc_weighted.py'
    assert sha256(core.read_bytes()).hexdigest()==KERNEL_SHA
    sys.path.insert(0,str(args.repo/'src'))
    from enterprise_math import brc_weighted as kernel

    by_parity=defaultdict(list)
    for s in VERTICES:
        h=route(kernel,[(s,F(1))])
        p=tuple(row[1]+row[2] for row in h.values())
        by_parity[p].append(s)
    even=tuple(by_parity)
    assert set(even)==set(VERTICES)-set(ODD) and all(len(v)==2 for v in by_parity.values())
    tests=simplex_tests(even)
    histogram=Counter()
    for ints in product(range(5),repeat=4):
        p=tuple(F(i,4) for i in ints)
        distance,v=min((l1(p,vertex),vertex) for vertex in ODD)
        gap=max(0,1-distance)/F(4)
        local=in_hull(ints,4,tests)
        assert local==(not gap)
        if gap:
            deviations=[abs(x-y)+gap for x,y in zip(p,v)]
            weights=[]
            for i,c in enumerate(deviations):
                neighbour=tuple(a^(i==j) for j,a in enumerate(v))
                weights.extend((s,c/2) for s in by_parity[neighbour])
            out=route(kernel,weights)
            assert max(l1(cells(q),row)/2 for q,row in zip(p,out.values()))==gap
        histogram[str(gap)]+=1
    margin_cases=0
    for p,q in product((F(i,8) for i in range(9)),repeat=2):
        lo=max(F(),p+q-1);hi=min(p,q)
        a,b,mid=[pair_from_margins(p,q,x) for x in (lo,hi,(lo+hi)/2)]
        assert all(min(v)>=0 and sum(v)==1 for v in (a,b,mid))
        assert l1(a,b)/2==2*(hi-lo) and l1(mid,a)/2==l1(mid,b)/2==hi-lo
        margin_cases+=1
    eta=F(3,4)
    target=(0,0,0,1)
    parity=tuple((1-eta)/2 if e==0 else (1+eta)/2 for e in target)
    winners=[s for v,ss in by_parity.items() if l1(v,target)==1 for s in ss]
    assert len(winners)==8
    boundary=route(kernel,[(s,F(1,8)) for s in winners])
    nearest=max(l1(cells(q),row)/2 for q,row in zip(parity,boundary.values()))
    chsh=sum((1 if g==0 else -1)*(1-2*q) for g,q in zip(target,parity))
    assert nearest==F(1,8) and chsh==3
    data=dict(kernel_sha256=KERNEL_SHA,ledger_rows=15,successors_for_interface_audit=ready,
              deterministic_assignments=16,even_vertices=len(even),invertible_five_vertex_simplices=len(tests),
              rational_grid=625,distance_histogram=dict(histogram),frechet_margin_tests=margin_cases,
              eta_three_quarters=dict(parity_probabilities=list(map(str,parity)),CHSH=str(chsh),
                                      nearest_local_eta='1/2',max_setting_TV=str(nearest)),
              physical_data_analysed=0,physical_verdict='MISSING_COMPONENT')
    payload=json.dumps(data,sort_keys=True,indent=2)+'\n'
    if args.json:args.json.write_text(payload)
    print('PASS',sha256(payload.encode()).hexdigest())


if __name__=='__main__':
    main()
