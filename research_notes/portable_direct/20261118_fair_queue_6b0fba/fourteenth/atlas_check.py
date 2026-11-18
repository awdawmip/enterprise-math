"""Registered home-chart transport and complete K4 partial-axis audit."""
import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from importlib.util import spec_from_file_location, module_from_spec
from itertools import combinations, permutations, product
from math import factorial, prod
from pathlib import Path
import json
import sys


EDGES=tuple(combinations(range(4),2))
STARS=frozenset(frozenset(i for i,e in enumerate(EDGES) if x in e) for x in range(4))
GROUP=tuple(tuple(EDGES.index(tuple(sorted((g[x],g[y])))) for x,y in EDGES)
            for g in permutations(range(4)))
MATCH=frozenset(frozenset((i,j)) for i,j in combinations(range(6),2)
                if not set(EDGES[i]).intersection(EDGES[j]))
PINS={
    'src/enterprise_math/cell_address.py':'b0ec81867994146ad69e81f73c74cfe58071c361150a84749be7a852536f1329',
    'src/enterprise_math/_cell_slice_codec.py':'9eb64264a59e23402c51d8aa20ff9a21ff37dec5f8bd80a97da2f54bbb48a70b',
    'src/enterprise_math/brc_weighted.py':'4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f',
    'EnterpriseMath/CellAddress/ThreeRegionSlice.lean':'2971ea97ba60f0a528a915c06152cb4aec9824fa85fae0bb88c0e76e4e921b02',
    'scripts/check_a3_recursive_shell_alignment_tomography.py':'28f3000ea052b78b7b7ec3ba34c3d880ed98666b61eef2888d1890cd11e61b04',
}


def signatures(labels):
    return Counter(tuple(i for i,e in enumerate(labels) if x in EDGES[e]) for x in range(4))


def extension_count(domain,target):
    left=signatures(domain)
    return prod(factorial(m) for m in left.values()) if left==signatures(target) else 0


def compose(left,right):
    return tuple(left[i] for i in right)


def image(g,family):
    return frozenset(frozenset(g[i] for i in block) for block in family)


def cycle_count(a,b):
    pending=set(range(6))
    count=0
    while pending:
        comp={min(pending)}
        while True:
            new=comp.union(*(edge for edge in a|b if edge & comp))
            if new==comp:break
            comp=new
        pending-=comp
        count+=1
    return count


def check_groups():
    counts=[]
    for k in range(7):
        hist=Counter()
        for domain in combinations(range(6),k):
            restricted=Counter(tuple(g[i] for i in domain) for g in GROUP)
            for target in permutations(range(6),k):
                n=extension_count(domain,target)
                assert n==restricted[target]
                hist[n]+=1
        counts.append(dict(size=k,by_extensions=sorted(hist.items())))
    assert sum(sum(cnt for _,cnt in x['by_extensions']) for x in counts)==13327
    available=set(permutations(range(6)))
    classes=[]
    while available:
        g=min(available)
        double={compose(compose(l,g),r) for l in GROUP for r in GROUP}
        assert double<=available
        available-=double
        cs={(cycle_count(MATCH,image(q,MATCH)),len(STARS&image(q,STARS))) for q in double}
        assert len(cs)==1
        cycles,overlap=cs.pop()
        assert overlap in (0,2**(cycles-1))
        classes.append(dict(representative=list(g),cycles=cycles,common_star=overlap,
                            permutations=len(double),relative_atlases=len(double)//24,
                            common_stabilizer=24*24//len(double)))
    assert len(classes)==len({(x['cycles'],x['common_star']) for x in classes})==6
    return counts,classes


@dataclass(frozen=True)
class Frame:
    axes:tuple
    anchor:tuple=(0,)*6

    def encode(self,codec,point):
        x=tuple(a-b for a,b in zip(point,self.anchor))
        if any(v for i,v in enumerate(x) if i not in self.axes):
            raise ValueError('OUTSIDE_FRAME')
        return self, codec.encode_raw_slice(tuple(x[i] for i in self.axes))

    def decode(self,codec,tagged):
        frame,address=tagged
        if frame!=self:raise ValueError('WRONG_EXTERNAL_FRAME')
        out=list(self.anchor)
        for i,v in zip(self.axes,codec.decode_raw_slice(address)):
            out[i]+=v
        return tuple(out)


def chart_and_paths(codec,brc):
    frame_a,frame_b,frame_c=Frame((0,1)),Frame((2,0)),Frame((0,3))
    pa,pb,pc=(0,)*6,(1,0,0,0,0,0),(2,0,0,0,0,0)
    frames=(frame_a,frame_b,frame_c)
    recode=lambda frm,addr:frm.encode(codec,addr[0].decode(codec,addr))
    c=0
    for x in range(-10,11):
        point=(x,0,0,0,0,0)
        addr=frame_a.encode(codec,point)
        for b,g in product(frames,repeat=2):
            assert recode(g,recode(b,addr))==recode(g,addr)
            assert recode(frame_a,recode(g,addr))==addr
            c+=1
    try: recode(frame_b,frame_a.encode(codec,(0,1,0,0,0,0)))
    except ValueError as e: assert str(e)=='OUTSIDE_FRAME'
    else: raise AssertionError('intersection check missing')
    try: codec.FinalCellAddress((0,1,1,0,0,0),frame='EXTERNAL_FRAME')
    except ValueError as e: assert str(e)=='UNKNOWN_OR_CHANGED_CELL_FRAME'
    else: raise AssertionError('registry boundary missing')

    # A stable native ID has one payload; aliases carry source and destination coordinates only.
    ids=('first/port-X','second/port-Y')
    weights=(F(1,2),F(2,3))
    rows={}
    for j,(x,y) in enumerate(((pa,pb),(pb,pc))):
        for frame in frames:
            start,end=frame.encode(codec,x),frame.encode(codec,y)
            canonical=(frame.decode(codec,start),frame.decode(codec,end),weights[j])
            previous=rows.setdefault(ids[j],canonical)
            assert previous==canonical
    def path_state(chains):
        out=brc.CWM_ZERO
        for chain in chains:
            value=brc.CWM_ONE
            for edge in chain:
                value=brc.cwm_propagate(value,brc.cwm_edge(rows[edge][2]))
            out=brc.cwm_recoalesce(out,value)
        return (out.count,str(out.total))
    aliases=[ids for f,g in product(frames,repeat=2)]
    actual=path_state(set(aliases));naive=path_state(aliases)
    assert actual==(1,'1/3') and naive==(9,'3')
    rows['another-port/same-endpoints']=rows[ids[0]]
    parallel=path_state([ids,('another-port/same-endpoints',ids[1])])
    assert parallel==(2,'2/3')
    stationary=[frame.encode(codec,pb)[1].coordinates for frame in (frame_a,frame_b)]
    moving=[frame_a.encode(codec,pa)[1].coordinates, Frame((0,1),pb).encode(codec,pb)[1].coordinates]
    assert stationary[0]!=stationary[1] and moving[0]==moving[1]
    return dict(triple_chart_checks=c,stationary_local_payloads=stationary,
                moving_local_payloads=moving,canonical_chain=actual,naive_chain=naive,
                distinct_parallel=parallel)


def shell_obstruction(root):
    path=root/'scripts/check_a3_recursive_shell_alignment_tomography.py'
    spec=spec_from_file_location('_frozen_a3_support',path)
    mod=module_from_spec(spec);spec.loader.exec_module(mod)
    s=(0,2,1,3)
    h=((0,1,2,3),(1,0,2,3))
    point=(1,-1,0,0)
    first=mod.prefix_move(3,2,s,point);second=mod.prefix_move(2,2,s,point)
    assert first==point and second==(-1,0,1,0)
    assert second not in {mod.r_act(q,first) for q in h}
    tests=0
    for g in mod.G:
        for x in mod.ball(2):
            lhs=mod.prefix_move(3,2,g,x)
            rhs=mod.prefix_move(2,2,g,x)
            mismatch=(mod.radius(x)==1 and mod.r_act(g,x)!=x)
            assert (lhs!=rhs)==mismatch
            tests+=1
    return dict(marker=point,large_action=first,small_action=second,same_H_orbit=False,
                all_state_checks=tests)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',required=True,type=Path)
    parser.add_argument('--json',type=Path)
    args=parser.parse_args()
    for p,d in PINS.items():assert sha256((args.repo/p).read_bytes()).hexdigest()==d
    sys.path.insert(0,str(args.repo/'src'))
    from enterprise_math import cell_address,brc_weighted
    counts,classes=check_groups()
    out=dict(source_sha256=PINS,all_partial_maps=counts,double_cosets=classes,
             addresses=chart_and_paths(cell_address,brc_weighted),a3=shell_obstruction(args.repo))
    data=json.dumps(out,sort_keys=True,indent=2)+'\n'
    if args.json:args.json.write_text(data)
    print('PASS',sha256(data.encode()).hexdigest())


if __name__=='__main__':main()
