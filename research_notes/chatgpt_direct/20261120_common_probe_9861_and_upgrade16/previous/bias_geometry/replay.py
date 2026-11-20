"""Exclude precisely the class profiles that could meet a biased optimum."""
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
from functools import cache
from itertools import product
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse
import importlib.util
import json
import os
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ELEVEN=HERE.parent/'eleven'
BASE=HERE.parent/'bias'
spec=importlib.util.spec_from_file_location('native_bias_menu',BASE/'replay.py')
bias=importlib.util.module_from_spec(spec)
spec.loader.exec_module(bias)


def dangerous(previous, denominator):
    sys.path.insert(0,str(previous/'mothers'))
    from costs import partitions
    catalog, visits, checksum=bias.census(previous)
    previous_bounds=json.loads((BASE/'result.json').read_text())
    assert checksum==previous_bounds['single_class_catalog_sha256']
    cap=previous_bounds['budget']
    assert (cap+1-bias.OPTIMAL)*denominator>previous_bounds['global_difference_cap']-bias.OPTIMAL_DIFFERENCE
    catalog[12,2]={1116:0}
    minimum={key:min(prices) for key,prices in catalog.items()}

    @cache
    def profile_bounds(slots, slack):
        if not slots:
            return (0,)+(-1,)*slack
        prefix=profile_bounds(slots[:-1],slack)
        key=slots[-1]
        out=[-1]*(slack+1)
        for price,difference in catalog[key].items():
            spent=price-minimum[key]
            for i in range(slack-spent+1):
                if prefix[i]>=0:
                    out[spent+i]=max(out[spent+i],prefix[i]+difference)
        return tuple(out)

    todo=[]
    for sizes in partitions(125,11):
        full=sizes.count(13)
        if full>=5 or (full==4 and cap<11365):
            continue
        if sum(min(minimum.get((s,i),10000) for i in (0,1)) for s in sizes)>cap:
            continue
        levels=sorted(set(sizes))
        possible=[(0,) if s in (1,13) else range(sizes.count(s)+1) for s in levels]
        for counts in product(*possible):
            p=tuple(s for s,n in zip(levels,counts) for _ in range(n))
            e=tuple(s for s,n in zip(levels,counts) for _ in range(sizes.count(s)-n))
            if len(p)<4 or (len(p)==4 and sum(p)<42):
                continue
            if any(sum(e[-k:])>bias.MOTHER_UNIONS[k] for k in range(1,len(e)+1)):
                continue
            large=e.count(12)+full
            if large>6:
                continue
            embedded_floor=sum(minimum[s,1] for s in e)+12*max(large-5,0)
            floor=embedded_floor+sum(minimum[s,0] for s in p)
            if floor>cap:
                continue
            slots=[(s,0) for s in p]+[(s,1) for s in e]
            if large==6:
                slots[slots.index((12,1))]=(12,2)
            diffs=profile_bounds(tuple(sorted(slots,reverse=True)),cap-floor)
            risk=[c for c in range(max(floor,bias.FIRST_OTHER),cap+1)
                  if diffs[c-floor]>=bias.OPTIMAL_DIFFERENCE+denominator*(c-bias.OPTIMAL)]
            if risk:
                todo.append((p,e,embedded_floor,max(risk)))
    return todo


def verify(previous, denominator, jobs):
    todo=dangerous(previous,denominator)
    keys=sorted({(len(e),sum(e)) for p,e,f,c in todo})
    third=previous/'previous/previous/previous'
    second=third/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(second)
    sys.path[:0]=[str(previous/'previous/parents'),str(third/'group'),str(second/'bounds')]
    from generate import maps
    from geometry import inventory,linear_actions
    from cyclic11 import observations
    from pairtypes import build
    from prior_bounds import observation_file
    forbidden,menus=observations()
    parents,centers=inventory(linear_actions(),forbidden,menus)
    rank={i:j for j,members in build(parents,centers) for i in members}
    parent_text=''.join(f'{m%2**64} {m>>64}\n' for m in parents)+' '.join(str(rank[i]) for i in range(1,250))+'\n'
    linear,translations,_=maps()
    label=lambda s: ','.join(map(str,s))
    with TemporaryDirectory() as tmp:
        w=Path(tmp)
        (w/'parent').write_text(parent_text)
        (w/'maps').write_bytes(b''.join(bytes(t[x] for x in g) for g in linear for t in translations))
        observation_file(w/'obs')
        def compile_source(name):
            src=previous/'mothers/union.cpp' if name=='union' else ELEVEN/(name+'.cpp')
            subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',src,'-o',w/name],check=True)
        with ThreadPoolExecutor(jobs) as pool:
            list(pool.map(compile_source,['union','census','bank','frame','native']))
        subprocess.run([w/'census',w/'obs',w/'seeds','0','0','0','1376','1560'],stdout=subprocess.DEVNULL,check=True)
        bank=subprocess.run([w/'bank',w/'parent',w/'maps',w/'seeds',w/'B','0 0 0 0 0 0 0 0 0 0 0 1376 1560 0'],capture_output=True,text=True,check=True)
        inventory_rows={str(s):[count,rows] for s,count,rows in (map(int,l.split()) for l in bank.stderr.splitlines())}
        assert inventory_rows['11']==[39,18920] and inventory_rows['12']==[4,540]
        def frames(item):
            k,s=item
            assert 13*(k-1)<s
            raw=w/f'raw{k}_{s}'
            with raw.open('w') as f:
                subprocess.run([w/'union',str(k),str(s),'-1','all'],input=parent_text,text=True,stdout=f,check=True)
            with raw.open() as f,(w/f'f{k}_{s}').open('w') as o:
                r=subprocess.run([w/'frame',w/'parent',w/'maps',str(k)],stdin=f,stdout=o,stderr=subprocess.PIPE,text=True,check=True)
            raw.unlink()
            raw_count,canon=map(int,r.stderr.split())
            assert canon>0 and raw_count>=canon
            return f'{k},{s}',[raw_count,canon]
        with ThreadPoolExecutor(jobs) as pool:
            locations=dict(pool.map(frames,keys))
        def exclude(item):
            p,e,floor,ceiling=item
            k,s=len(e),sum(e)
            assert sum(e[:2])>13 and min(p)>bias.MOTHER_UNIONS[k]-s
            family_count=locations[f'{k},{s}'][1]
            r=subprocess.run([w/'native',w/'obs',w/'parent',w/'B',w/f'f{k}_{s}',label(p),label(e),str(floor),str(ceiling),'0',str(family_count)],capture_output=True,text=True,check=True)
            counts=list(map(int,r.stderr.split()))
            assert not r.stdout and counts[0]==family_count and len(counts)==5 and counts[3:]==[0,0]
            return label(p)+'__'+label(e),[ceiling,floor,*counts]
        with ThreadPoolExecutor(jobs) as pool:
            cases=dict(pool.map(exclude,todo))
    return dict(weighted_radius=str(Fraction(1,denominator)),p_interval=[str(Fraction(denominator-1,2*denominator)),str(Fraction(denominator+1,2*denominator))],
                endpoint_counts=[4000,4000],profiles=len(todo),cases=cases,weighted_ties_from_other_tables=0,
                normalized_mother_locations=locations,large_exception_catalog=inventory_rows,
                search_nodes=sum(v[3] for v in cases.values()),family_profile_placements=sum(v[2] for v in cases.values()))


if __name__=='__main__':
    args=argparse.ArgumentParser(description=__doc__)
    args.add_argument('--previous',type=Path,required=True)
    args.add_argument('--jobs',type=int,default=3)
    args.add_argument('--denominator',type=int,default=None)
    a=args.parse_args()
    fi=HERE/'result.json'
    old=json.loads(fi.read_text()) if fi.exists() else None
    denom=a.denominator or Fraction(old['weighted_radius']).denominator
    value=verify(a.previous.resolve(),denom,a.jobs)
    if old and a.denominator is None:
        assert value==old
    print(json.dumps(value,indent=2,sort_keys=True))
