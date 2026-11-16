"""Rebuild all grouped quotient masks directly from allowed public inputs, then run complete cases."""
from pathlib import Path
from collections import Counter
from itertools import product,combinations
import tempfile, subprocess,shutil,json,sys

SOURCE=Path(__file__).resolve().parent


def forbidden():
    points=list(product(range(5),repeat=3)); bad=set()
    for d in (1,3):
        for origin in points:
            groups={}
            for i,row in enumerate(points):
                active=tuple(j for j in range(3) if (row[j]-origin[j])%5 in (0,d))
                groups.setdefault(active,[]).append((i,tuple(row[j] for j in active)))
            for group in groups.values():
                for (a,x),(b,y),(c,z) in combinations(group,3):
                    if len({x,y,z})==3:bad.add((a,b,c))
    assert len(bad)==47000
    return bad


def verify():
    with tempfile.TemporaryDirectory() as tmp:
        tmp=Path(tmp)
        for name in ['fixed_all.cpp','moving.cpp','case3_fast.cpp','geom.py','gen3.py','case2.py']:
            shutil.copy(SOURCE/name,tmp/name)
        edges=forbidden()
        (tmp/'triples.bin').write_bytes(b''.join(bytes(e) for e in sorted(edges)))
        def call(args):return subprocess.check_output(args,cwd=tmp,text=True)
        for n in ('fixed_all','moving','case3_fast'):
            call(['c++','-O3','-mpopcnt','-std=c++17',n+'.cpp','-o',n])
        fixed=call(['./fixed_all']);(tmp/'fixed_again.txt').write_text(fixed)
        histogram={}
        for line in fixed.splitlines():
            a,b,n=map(int,line.split());histogram[a,b]=n
        assert max(b for a,b in histogram)==4
        moving=call(['./moving']);counts={int(a):int(n) for a,n in (line.split() for line in moving.splitlines() if not line.startswith('visits'))}
        assert counts[11]>0 and not counts[12] and not counts[13]
        seed=[int(l.split()[1]) for l in (tmp/'p8_seed.txt').read_text().splitlines() if l.startswith('11 ')]
        images=set()
        for s in seed:
            for k,dy,dz in product((1,2),range(5),range(5)):
                bits=[i for i in range(50) if s>>i&1]
                img=0
                for i in bits:
                    x=k*(1+i//25)%5
                    img|=1<<(25*min(x,5-x)+5*((i//5*k+dy)%5)+(i*k+dz)%5)
                images.add(img)
        assert len(images)==500
        (tmp/'pdecomp.txt').write_text(''.join(f'{s}\n' for s in sorted(images)))
        # For k=0,1 physical pair capacity is 4(11-2k)+11k <50.
        # For k=4,5 five pairs contribute at most 11 points per moved class.
        # Check all joint counts of fixed labels, fixed points =25, moving histories per pair =11.
        def fixed_possible(k):
            combinations={(0,0)}
            for _ in range(11-2*k):
                combinations={(x+a,y+b) for x,y in combinations for a,b in histogram if x+a<=25 and y+b<=50}
            return any(x==25 and y+11*k>=50 for x,y in combinations)
        numeric=[fixed_possible(k) for k in range(6)]
        assert numeric==[False,False,True,True,False,False]
        geom=call([sys.executable,'geom.py']);prep=call([sys.executable,'gen3.py']);case2=call([sys.executable,'case2.py']);case3=call(['./case3_fast'])
        assert case2.endswith('no pattern k=2\n') and case3.endswith('CLOSED 56\n')
        states=[list(map(int,l.split()[1:])) for l in case3.splitlines() if l.startswith('CASE ')]
        assert len(states)==56 and all(not s[-1] for s in states)
        return dict(forbidden_triples=len(edges),fixed_class_profiles=[[a,b,n] for (a,b),n in sorted(histogram.items())],
                    moving_anchored_masks=counts,full_moving_eleven_masks=len(images),
                    pair_orbit_possible_from_counts=numeric,
                    case_two_totals=list(map(int,case2.splitlines()[-2].split())),case_three_shapes=len(states),
                    case_three_nodes=states[-1][1],case_three_completed_five_fixed_covers=states[-1][2],
                    case_three_distinct_remainders=states[-1][3],solution=False)

if __name__=='__main__':print(json.dumps(verify(),indent=2))
