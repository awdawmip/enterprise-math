"""Compute affine overlap of two unordered thirteen-class partitions."""
import argparse
from collections import Counter
import json
from pathlib import Path
import sys

def check(a,b,groupdir):
    sys.path.insert(0,str(groupdir))
    from generate import maps
    A={frozenset(r) for r in a}
    assert len(A)==len(b)==13
    lin,trans,_=maps()
    histogram=Counter()
    for l in lin:
        for t in trans:
            g=bytes(t[p] for p in l)
            overlap=sum(frozenset(g[p] for p in r) in A for r in b)
            histogram[overlap]+=1
    assert sum(histogram.values())==12000
    return {'affine_maps_by_shared_rows':{str(k):n for k,n in sorted(histogram.items())},
            'minimum_number_of_replacements':13-max(histogram)}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--group',required=True,type=Path)
    p.add_argument('tables',type=Path,nargs=2)
    args=p.parse_args()
    print(json.dumps(check(*(json.loads(f.read_text()) for f in args.tables),args.group.resolve()),indent=2))
