"""Reconstruct the 24 minimum partitions at the origin and translate their centers."""
from pathlib import Path
from itertools import permutations, product
from collections import Counter
import json

def check(source):
    origin_table=json.loads((source/'curve/open_witnesses.json').read_text())['13']['groups']
    coordinates=list(product(range(5),repeat=3))
    def number(p):return 25*(p[0]%5)+5*(p[1]%5)+p[2]%5
    def normalized(classes):return tuple(sorted(tuple(sorted(c)) for c in classes))
    def transport(partition,f):return normalized([f[i] for i in row] for row in partition)
    table=normalized(origin_table)
    assert len(table)==13 and sorted(x for row in table for x in row)==list(range(125))
    linear=[]
    for perm,signs,d in product(permutations(range(3)),product((-1,1),repeat=3),(1,2)):
        linear.append([number([p[perm[j]]*signs[j]*d for j in range(3)]) for p in coordinates])
    at_origin={transport(table,g) for g in linear}
    neg=[number([-v for v in p]) for p in coordinates]
    assert all(transport(t,neg)==t for t in at_origin)
    fixed=[number(t) for t in coordinates if transport(table,[number([2*a-b for a,b in zip(t,p)]) for p in coordinates])==table]
    assert fixed==[0]
    return {'origin_orbit':len(at_origin),'origin_stabilizer':len(linear)//len(at_origin),'centers_per_table':len(fixed),'all_centers_orbit':125*len(at_origin)//len(fixed)}

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument('--older',type=Path,default=Path(__file__).resolve().parents[2]/'round2/delivery')
    print(json.dumps(check(p.parse_args().older.resolve()),indent=2))
