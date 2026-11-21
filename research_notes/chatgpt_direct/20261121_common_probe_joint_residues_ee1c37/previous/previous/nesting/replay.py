"""Decide whether two globally minimum-cost tables can be successive refinements."""
from collections import defaultdict
from functools import cache
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse,json,os,subprocess,sys
HERE=Path(__file__).resolve().parent

def indices(m):
    while m:
        bit=m&-m
        yield bit.bit_length()-1
        m-=bit

def mask(xs):return sum(1<<x for x in xs)

def verify(previous):
    fifth=previous/'previous'
    fourth=fifth/'previous'
    third=fourth/'previous'
    second=third/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(second)
    sys.path[:0]=[str(third/'group'),str(second/'curve'),str(second/'bounds')]
    from generate import maps
    from verify import MINIMA,lower,cheap_line_partitions
    from cyclic11 import class_cost,observations
    from prior_bounds import observation_file
    bad,menus=observations()
    linear,translations,_=maps()
    seeds=defaultdict(set)
    with TemporaryDirectory()as tmp:
        d=Path(tmp);observation_file(d/'menu')
        subprocess.run(['c++','-O3','-mpopcnt','-std=c++17',HERE/'bank.cpp','-o',d/'enum'],check=True)
        subprocess.run([d/'enum',d/'menu',d/'seeds'],stdout=subprocess.DEVNULL,check=True)
        for line in (d/'seeds').read_text().splitlines():
            s,price,*r=map(int,line.split());assert price==MINIMA[s]
            seeds[s].add(tuple(r))
    seeds[1]={(0,)}
    bank={}
    for size,rows in seeds.items():
        linear_images={tuple(sorted(f[x]for x in r))for r in rows for f in linear}
        bank[size]={mask(t[x]for x in r)for r in linear_images for t in translations}
    @cache
    def child_counts(m,t):
        # Bit j records a partition into j eligible child classes.
        if not m:return 1
        size=m.bit_count()
        if size<t:return 0
        possible=2 if size in (t,t+1) and m in bank.get(size,()) else 0
        if size<2*t:return possible
        anchor=m&-m
        for n in (t,t+1):
            if n>size-t:continue
            for extra in combinations(indices(m^anchor),n-1):
                r=anchor|mask(extra)
                if r in bank[n]:possible|=child_counts(m^r,t)<<1
        return possible
    def counts(options):
        possible=1
        for opt in options:
            acc=0
            for j in indices(opt):acc|=possible<<j
            possible=acc
        return possible
    by_size={}
    for s,rs in seeds.items():
        for t in range(1,s+1):
            opt=0
            for r in rs:opt|=child_counts(mask(r),t)
            by_size[s,t]=opt
    def read(path):return json.loads(path.read_text())
    extra=read(HERE/'extra_tables.json')
    def validate(rows,k):
        assert sorted(sum(rows,[]))==list(range(125)) and len(rows)==k
        assert not any(bad[x][y]>>z&1 for r in rows for x,y,z in combinations(sorted(r),3))
        assert sum(class_cost(r,menus)for r in rows)==lower(125,k)
    for k,allrows in extra.items():
        for rows in allrows:validate(rows,int(k))
    def solve(rows,n):
        t=125//n
        return bool((counts([child_counts(mask(r),t)for r in rows])>>n)&1)
    exact={}
    specific=read(fourth/'eleven_six_counts/groups.json')+[read(fifth/'eleven_equal/groups.json'),read(fifth/'c3/groups.json')]
    for label,table in zip(('eleven_orbit_A','eleven_orbit_B','eleven_orbit_C','symmetric_twelve'),specific):
        exact[label]=[n for n in range(14,126)if solve(table,n)]
    results={};totals=dict(yes=0,no=0,open=0)
    for k in range(13,125):
        if k==13:
            base=[read(third/'asymmetric8721/groups.json')]
        else:
            base=[cheap_line_partitions(k)]
            if k==17:base.append(read(previous/'refinement/optimal17.json'))
            base.extend(extra.get(str(k),[]))
        sizes=[len(r)for r in base[0]]
        if k>=14:
            a,b=divmod(125,k);allowed={a,a+1} if b else {a}
            assert all(s in allowed for s in range(1,14)if MINIMA[s]+lower(125-s,k-1)==lower(125,k))
        d=dict(yes=[],no=[],open=[])
        for n in range(k+1,126):
            t,rem=divmod(125,n);allowed={t,t+1} if rem else {t}
            assert all(s in allowed for s in range(1,14)if MINIMA[s]+lower(125-s,n-1)==lower(125,n))
            yes=any(solve(tab,n)for tab in base)
            if k==13:possible=yes
            else:possible=bool(counts([by_size.get((s,t),0)for s in sizes])>>n&1)
            assert not yes or possible
            label='yes' if yes else 'open' if possible else 'no'
            d[label].append(n);totals[label]+=1
        results[str(k)]=d
    assert sum(totals.values())==6328
    return dict(all_minimum_classes_by_size={str(k):len(v)for k,v in sorted(bank.items())},
                unequal_budgets_from_13_to_125=totals,budgets=results,special_orbits=exact)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',required=True,type=Path)
    print(json.dumps(verify(p.parse_args().previous.resolve()),sort_keys=True,separators=(',',':')))
