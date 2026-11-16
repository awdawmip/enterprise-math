"""Complete the classification of inexpensive eleven-label partitions with a nontrivial involution."""
import argparse
from collections import Counter
from functools import cache
from itertools import product
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent
BUDGET = 11291

def actions(linear):
    identity = bytes(range(125))
    def comp(a,b):
        return bytes(a[x] for x in b)
    inverse = {a:bytes(a.index(i) for i in identity) for a in linear}
    remaining = {a for a in linear if a != identity and comp(a,a) == identity}
    order = []
    while remaining:
        g = min(remaining)
        conjugates = {comp(h,comp(g,inverse[h])) for h in linear}
        remaining -= conjugates
        centralizer = [h for h in linear if comp(h,g)==comp(g,h)]
        order.append((g,len(conjugates),centralizer))
    assert [n for _,n,_ in order]==[3,3,6,1,6]
    return order

def points(m):
    while m:
        b = m & -m
        yield b.bit_length()-1
        m ^= b

def image(mask,action):
    return sum(1<<action[p] for p in points(mask))

def first_anchors(work,g,centralizer):
    maps = []
    for h in centralizer:
        for t in range(125):
            if g[t] == t:
                maps.append(bytes(25*((p//25+t//25)%5)+5*((p//5%5+t//5%5)%5)+(p%5+t%5)%5 for p in h))
    bank = set()
    for r,name in [(1,'fixed.rows'),(2,'pair.rows')]:
        with (work/name).open() as rows:
            for line in rows:
                if not line.startswith(('12 ','13 ')):
                    continue
                size,h,c,a,b = map(int,line.split())
                q = (b<<64)|a
                if r==2:
                    q |= image(q,g)
                bank.add((q,r))
    reps = []
    while bank:
        q,r = min(bank)
        orbit = {(image(q,t),r) for t in maps}
        assert orbit <= bank
        bank -= orbit
        reps.append((q,r))
    (work/'anchors').write_text(''.join(f'{r} {q%2**64} {q>>64}\n' for q,r in reps))
    return len(reps)

def swap_bound(fixed,paired,minimum):
    types = [(1,s,d,c) for (s,d),c in fixed.items()]
    types += [(2,s,0,2*(paired[s] if s>10 else minimum[s])) for s in range(1,14) if s<=10 or s in paired]
    @cache
    def lower(n,d,f,b):
        if min(n,d,f,b)<0 or d>n or n>13*(f+2*b):
            return 10**8
        if f+b==0:
            return 0 if n==d==0 else 10**8
        return min((c+lower(n-r*s,d-h,f-(r==1),b-(r==2)) for r,s,h,c in types if (r==1 if f else r==2)),default=10**8)
    return [v if (v:=lower(125,25,11-2*b,b))<10**8 else None for b in range(6)]

def verify(last,older,work):
    sys.path[:0] = [str(last/'group'),str(older/'bounds'),str(older/'curve')]
    from generate import maps
    from prior_bounds import observation_file
    from verify import MINIMA
    linear,_,_ = maps()
    (work/'linear').write_text(''.join(' '.join(map(str,h))+'\n' for h in linear))
    observation_file(work/'obs')
    def run(*args):
        return subprocess.run(list(map(str,args)),check=True,text=True,capture_output=True)
    for name in ['class_seeds','fixed','pair_orbits','skeletons','tails']:
        run('c++','-O3','-std=c++20','-mpopcnt', HERE/(name+'.cpp'),'-o',work/name)
    run(work/'class_seeds',work/'obs',work/'seeds')
    results = {}
    for i,(g,count,cent) in enumerate(actions(linear)):
        if i==0:
            continue
        (work/'perm').write_text(' '.join(map(str,g))+'\n')
        fix = run(work/'fixed',work/'obs',work/'fixed.rows',work/'perm')
        fixed = {(s,d):c for s,d,t,c in (map(int,l.split()) for l in fix.stdout.splitlines())}
        pairs = run(work/'pair_orbits',work/'linear',work/'seeds',work/'perm',work/'pair.rows')
        pairmin = {s:c for s,c in (map(int,l.split()) for l in pairs.stdout.splitlines())}
        result = {'linear_conjugates':count,'basis_images':[g[p] for p in (25,5,1)],
                  'fixed_point_count':sum(a==b for a,b in enumerate(g)), 'fixed_class_nodes':int(fix.stderr.strip()),
                  'pair_minima_sizes_11_to_13':pairmin}
        budget = 31250 if i==2 else BUDGET
        if i == 2:
            assert 13 not in pairmin
            bound = swap_bound(fixed,pairmin,MINIMA)
            assert min(v for v in bound if v is not None)>=11616
            result['unconditional_read_bounds_by_number_of_exchanged_pairs'] = bound
        n = first_anchors(work,g,cent)
        run1=run(work/'skeletons',work/'perm',work/'fixed.rows',work/'pair.rows',work/'anchors',budget,work/'tasks')
        assert not run1.stderr
        rows=[list(map(int,l.split())) for l in run1.stdout.splitlines()]
        assert len(rows)==n and {r[0] for r in rows}==set(range(n))
        tasks=(work/'tasks').read_text().splitlines()
        taskset=sorted(set(tasks))
        tallies=Counter(int(t.split()[2]) for t in taskset)
        (work/'short').write_text(''.join(t+'\n' for t in taskset))
        small=run(work/'tails',work/'obs',work/'short',0,len(taskset),budget)
        tail=[list(map(int,l.split())) for l in small.stdout.splitlines()]
        assert len(tail)==len(taskset) and all(idx==j and ok==0 for j,(idx,visits,ok) in enumerate(tail))
        result.update(anchors=n,raw_residuals=len(tasks),distinct_residuals=len(taskset),remaining_label_counts=dict(tallies),
                      residual_visits=sum(row[1] for row in tail),excluded_through=budget)
        if i == 2: assert n == 5 and not taskset
        results[i]=result
    return results

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--last',type=Path,required=True,help='directory containing group/generate.py')
    p.add_argument('--older',type=Path,required=True,help='directory containing bounds and curve')
    a=p.parse_args()
    with TemporaryDirectory() as tmp:
        print(json.dumps(verify(a.last.resolve(),a.older.resolve(),Path(tmp)),sort_keys=True,indent=2))
