"""Compare menu/receipt enumeration and stratified physical runs with archived returns."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
parser=argparse.ArgumentParser()
parser.add_argument('--original',type=Path,default=ROOT/'original')
parser.add_argument('--record',action='store_true')
parser.add_argument('--labels',type=int,nargs='*')
args=parser.parse_args()
sys.path.insert(0,str(ROOT/'curve'))
sys.path.insert(0,str(args.original.resolve()))
from verify import cheap_line_partitions
from frontier9.native.replay_joint import run

open_tables=json.loads((ROOT/'curve/open_witnesses.json').read_text())
labels=args.labels or [11,12,13,14,15,16,17,18,19,20,21,25,32,42,63,64,125]
for m in labels:
    if m==11:
        code=list(map(int,(ROOT/'native/eleven.txt').read_text().split()))
    elif m==12:
        code=list(map(int,(ROOT/'bounds/twelve_10147.txt').read_text().split()))
    else:
        if str(m) in open_tables:
            groups=open_tables[str(m)]['groups']
        else:
            groups=cheap_line_partitions(m)
        assert sorted(i for g in groups for i in g)==list(range(125))
        code=[0]*125
        for j,group in enumerate(groups):
            for i in group:code[i]=j
    value=run(code,1)
    path=ROOT/'native'/f'm{m}.json'
    if args.record:path.write_text(json.dumps(value,indent=2,sort_keys=True)+'\n')
    else:assert json.loads(path.read_text())==json.loads(json.dumps(value)),m
    print(m,value['joint']['by_queries'],value['joint']['full_raw_sample'],flush=True)
