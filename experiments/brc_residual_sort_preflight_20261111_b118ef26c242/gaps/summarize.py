"""Check root diagnostics and small-domain interval optimality; aggregate the 24 banks."""
import csv
import itertools
from collections import defaultdict
from pathlib import Path

here=Path(__file__).resolve().parent
def read(path):
    with path.open(newline='') as f:
        return list(csv.DictReader(f))

def small_exhaustion():
    tested = 0
    for mask in range(1, 256):
        data = [i for i in range(8) if mask>>i & 1]
        holes = [b-a-1 for a,b in zip(data,data[1:])]
        for k in (1,2,3):
            possible = []
            for num in range(min(k-1,len(holes))+1):
                for cuts in itertools.combinations(range(1,len(data)),num):
                    bounds = (0,*cuts,len(data))
                    possible.append(sum(data[end-1]-data[start]+1 for start,end in zip(bounds,bounds[1:])))
            assert min(possible)==data[-1]-data[0]+1-sum(sorted(holes,reverse=True)[:k-1])
            tested+=1
    return tested

def run():
    counts=small_exhaustion()
    data=read(here/'arrays.csv')
    spans=read(here/'intervals.csv')
    assert len(data)==72 and len(spans)==144
    reference={}
    for phase,family,algo,stage in ((5,'previous_million','observe','known4'),
                                    (5,'new_balanced_million','observe','fresh5'),
                                    (6,'new_balanced_million','deep_gate','fresh6')):
        for r in read(here.parent/f'phase{phase}'/'results'/'nodes.csv'):
            if r['algorithm']==algo and r['family']==family and r['depth']=='0':
                reference[stage,int(r['bank'])]=(int(r['actual_misses']),int(r['counter_slots']))
    assert len(reference)==24
    groups=defaultdict(list)
    for r in data:
        key=(r['stage'],int(r['bank']))
        assert (int(r['residual_n']),int(r['parent_cells']))==reference[key]
        assert int(r['residual_n'])==sum(int(r[f'source_{g}']) for g in 'ABC')
        matches=[s for s in spans if s['stage']==r['stage'] and s['bank']==r['bank'] and s['k']==r['k']]
        assert sum(int(s['occurrences']) for s in matches)==int(r['residual_n'])
        assert sum(int(s['high'])-int(s['low'])+1 for s in matches)==int(r['width'])
        groups[r['stage'],int(r['k'])].append(r)
    with (here/'group_summary.csv').open('w',newline='') as f:
        out=csv.writer(f)
        out.writerow(['stage','k','banks','fits','width_min','width_max','outside_min','outside_max',
                      'other_true_clusters_min','other_true_clusters_max','parent_grid_fits'])
        for stage in ('known4','fresh5','fresh6','all'):
            for k in (1,2,3):
                rows=[r for r in data if int(r['k'])==k and (stage=='all' or r['stage']==stage)]
                def values(name):return [int(r[name]) for r in rows]
                outside=[int(r['residual_n'])-max(int(r[f'source_{g}']) for g in 'ABC') for r in rows]
                out.writerow([stage,k,len(rows),sum(values('fits_budget')),min(values('width')),
                              max(values('width')),min(values('outside_largest_segment')),
                              max(values('outside_largest_segment')),min(outside),max(outside),
                              sum(values('parent_grid_fits'))])
    print(f'validated {len(reference)} frozen root counts and slot counts; {len(data)} covers; '
          f'{len(spans)} intervals; {counts} independent small-domain cover optima')

if __name__=='__main__':
    run()
