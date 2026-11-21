"""Exact optimum and number of tables with a single nonextendible six-point label."""
from collections import Counter
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse,json,sys,subprocess
HERE=Path(__file__).resolve().parent

def verify(base,previous):
    sys.path[:0]=[str(previous/'previous/previous/previous/bounds'),str(previous/'parents')]
    from geometry import normalize,inventory,linear_actions,shifted,image
    from cyclic11 import observations,class_cost,P as coords
    from pairtypes import build
    bad,menus=observations();actions=linear_actions();parents,centers=inventory(actions,bad,menus)
    canon=normalize(parents,centers,actions)
    ranks={}
    for j,rs in build(parents,centers):
        for i in rs:ranks[i]=j
    bank=''.join(f'{m%(1<<64)} {m>>64}\n' for m in parents)+' '.join(str(ranks[i])for i in range(1,250))+'\n'
    with TemporaryDirectory()as wk:
        exe=Path(wk)/'union'
        subprocess.run(['c++','-O3','-mpopcnt','-std=c++20',base/'union.cpp','-o',exe],check=True)
        source=subprocess.check_output([exe,'11','119','-1','all'],input=bank,text=True)
    types=Counter();frames=0
    for line in source.splitlines():
        if not line.startswith('0 '):continue
        frame=list(map(int,line.split()));assert len(frame)==11
        mask=(1<<125)-1
        for i in frame:mask&=~parents[i]
        hole=[i for i in range(125)if mask>>i&1]
        assert len(hole)==6;frames+=1
        if any(bad[a][b]>>c&1 for a,b,c in combinations(hole,3)):continue
        assert not any(mask&p==mask for p in parents)
        types[canon(frame)]+=1
    assert len(types)==1
    pk=next(iter(types));doc=json.loads((HERE/'assignment.json').read_text())
    cert=doc[','.join(map(str,pk))]
    assert types[pk]==cert['multiplicity']
    family=[parents[i]for i in pk];full=(1<<125)-1
    for m in family:full&=~m
    family.append(full)
    w=cert['weights'];common=[i for i in range(125)if sum(m>>i&1 for m in family)>1]
    ix={v:i for i,v in enumerate(common)};assert len(w)==len(common)+12
    pool=[];menus_checked=0;private=[]
    for j,m in enumerate(family):
        shared=[p for p in common if m>>p&1]
        required=[i for i in range(125)if m>>i&1 and i not in ix];opts=[];private.append(len(required))
        for mask in range(1<<len(shared)):
            take=[y for i,y in enumerate(shared) if mask>>i&1]
            value=w[len(common)+j]+sum(w[ix[y]] for y in take);row=required+take
            actual=10000*class_cost(row,menus)
            assert value<=actual;menus_checked+=1
            if value==actual:opts.append((sum(1<<i for i in take),sum(1<<i for i in row)))
        pool.append(opts)
    overlap=max((parents[0]&m).bit_count()for m in parents[1:])
    assert min(private[:-1])>overlap
    table=cert['partition']
    assert sorted(sum(table,[]))==list(range(125)) and len(table)==12
    assert all(all(m>>i&1 for i in r) for m,r in zip(family,table))
    minimum=sum(class_cost(r,menus)for r in table)
    assert sum(w)==minimum*10000==cert['lp_lower']
    assert minimum==cert['cost'] and menus_checked==cert['menu_options']
    order=sorted(range(12),key=lambda j:len(pool[j]));optima=set();shared_mask=sum(1<<x for x in common)
    def place(at,used,groups):
        if at==12:
            if used==shared_mask:optima.add(tuple(sorted(groups)))
            return
        for ext,group in pool[order[at]]:
            if not used&ext:place(at+1,used|ext,groups+[group])
    place(0,0,[])
    target=set(family[:-1]);stab=[]
    for a in actions:
        for d in coords:
            f=[shifted(coords[j],d)for j in a]
            if all(image(m,f) in target for m in family[:-1]):stab.append(f)
    todo=set(optima);classes=[]
    while todo:
        x=min(todo);orbit={tuple(sorted(image(m,f)for m in x))for f in stab}
        assert orbit<=todo;todo-=orbit;classes.append(len(orbit))
    automorphisms=len(actions)*len(coords);assert automorphisms%len(stab)==0
    copies=automorphisms//len(stab);hist=Counter(s*copies for s in classes)
    return dict(minimum=minimum,normalized_maximum_families=frames,legal_six_point_families=sum(types.values()),
                family_orbits=len(types),shared_points=len(common),local_options=menus_checked,
                maximum_parent_pair_overlap=overlap,minimum_private_inside_parent=min(private[:-1]),
                parent_family_stabilizer=len(stab),actual_parent_families=copies,
                optimal_per_family=len(optima),optimal_unlabeled_tables=copies*len(optima),
                optimal_affine_orbits={str(k):v for k,v in sorted(hist.items())})

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--base',type=Path,required=True);p.add_argument('--previous',type=Path,required=True)
    a=p.parse_args();out=verify(a.base.resolve(),a.previous.resolve());expected=HERE/'result.json'
    if expected.exists():assert out==json.loads(expected.read_text())
    print(json.dumps(out,indent=2,sort_keys=True))
