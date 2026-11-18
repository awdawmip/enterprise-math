"""Enumerate the ties at 960 and count every packing of their parent supports."""
import argparse
from collections import Counter
from itertools import combinations
import json,os,subprocess,sys
from pathlib import Path
from tempfile import TemporaryDirectory

HERE=Path(__file__).resolve().parent
def mask(xs):return sum(1<<x for x in xs)
def points(m):return [i for i in range(125) if (m>>i)&1]

def verify(previous,refinement):
    last=previous/'previous/previous'
    old=last/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(old)
    sys.path[:0]=[str(old/'bounds'),str(last/'group')]
    from cyclic11 import observations,class_cost
    from prior_bounds import observation_file
    from generate import maps
    other=json.loads((refinement/'result.json').read_text())['census']['all']
    assert max(v['maximum_gain']['value'] for k,v in other.items() if int(k)!=12)==900
    assert other['12']['maximum_gain']['value']==960
    with TemporaryDirectory() as tmp:
        w=Path(tmp)
        observation_file(w/'obs')
        subprocess.run(['c++','-O3','-std=c++20','-mpopcnt',HERE/'parents.cpp','-o',w/'parents'],check=True)
        scan=subprocess.run([w/'parents',w/'obs'],capture_output=True,text=True,check=True)
    visited,runner=map(int,scan.stderr.split())
    assert visited==160 and runner==914
    ties={}
    bad,menu=observations()
    for line in scan.stdout.splitlines():
        c,side,*r=map(int,line.split())
        assert len(r)==12 and len(set(r))==12 and r==sorted(r)
        assert not any((bad[i][j]>>k)&1 for i,j,k in combinations(r,3))
        a=tuple(x for i,x in enumerate(r) if (side>>i)&1)
        b=tuple(set(r)-set(a))
        assert class_cost(r,menu)==c and c-class_cost(a,menu)-class_cost(b,menu)==960
        ties.setdefault(tuple(r),[]).append(a)
    linear,tr,_=maps()
    directions=next(iter(ties))
    parents={}
    for l in linear:
        for t in tr:
            g=bytes(t[i] for i in l)
            p=mask(g[i] for i in directions)
            choices=parents.setdefault(p,set())
            for a in ties[directions]:
                c=mask(g[i] for i in a);choices.add(min(c,p^c))
    assert all(mask(r) in parents for r in ties)
    assert len(ties)==8 and sum(map(len,ties.values()))==48
    assert len(parents)==375 and {len(v) for v in parents.values()}=={6}
    S=sorted(parents)
    adj=[sum(1<<j for j,m in enumerate(S) if not q&m) for q in S]
    counts=Counter();best=[]
    def recurse(chosen,candidates):
        nonlocal best
        counts[len(chosen)]+=1
        if len(chosen)>len(best):best=chosen
        while candidates:
            bit=candidates&-candidates;candidates^=bit
            j=bit.bit_length()-1
            recurse(chosen+[j],candidates&adj[j])
    recurse([0],adj[0])
    assert [counts[n] for n in range(1,7)]==[1,114,1565,3200,576,0]
    all_packs={}
    for size,count in sorted(counts.items()):
        assert count*len(S)%size==0
        all_packs[size]=count*len(S)//size
    witness=[];covered=0
    for j in best:
        p=S[j];a=min(parents[p]);r=points(p);left=points(a);right=points(p^a)
        assert p&covered==0
        covered|=p
        c=class_cost(r,menu);costs=[class_cost(z,menu) for z in (left,right)]
        assert c-sum(costs)==960
        witness.append({'parent':r,'children':[left,right],'parent_cost':c,'child_costs':costs})
    return dict(normalized_size_twelve=visited,normalized_equal_parents=len(ties),
                normalized_equal_splits=sum(map(len,ties.values())),equal_parent_orbits=1,
                parent_supports=len(S),unordered_equal_splits_per_parent=6,second_largest_single_gain=runner,
                anchored_counts=dict(sorted(counts.items())),all_packing_counts=all_packs,
                maximum_disjoint_parents=len(witness),witness=witness)

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--previous',required=True,type=Path)
    ap.add_argument('--refinement',type=Path,default=HERE.parent/'refinement')
    a=ap.parse_args()
    print(json.dumps(verify(a.previous.resolve(),a.refinement.resolve()),sort_keys=True,indent=2))
