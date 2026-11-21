"""Independent multiset generating-function check of all frozen E2 prices.

Unlike the main slot recursion, this uses each available price as an unbounded
coin and tracks class count, price excess and marginal-defect capacity.
"""
import argparse
from collections import defaultdict
from hashlib import sha256
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mother',type=Path,default=HERE.parent/'integer_cuts/mother12')
    p.add_argument('--defect',type=Path,default=HERE.parent/'mother_sublevels_D')
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    bindings=json.loads((HERE/'bindings.json').read_text())
    for item in bindings['dependencies']:
        if (item['root'],item['path']) in [('mother','catalog.txt'),('defect','cost_defect_catalog.json')]:
            source=getattr(args,item['root'])/item['path']
            assert sha256(source.read_bytes()).hexdigest()==item['sha256']
    data=defaultdict(set)
    for line in (args.mother/'catalog.txt').read_text().splitlines():
        size,embedded,cost,_=map(int,line.split())
        data[size,embedded].add(cost)
    defects={(r['size'],r['cost']):r['maximum_defect_upper_bound']
             for r in json.loads((args.defect/'cost_defect_catalog.json').read_text())['rows']}
    expected=json.loads((HERE/'expected.json').read_text())
    top=expected['excluded_through']
    assert top<9912 # The complete size plan has precisely the two families below this boundary.
    def multiset(size,count,excess):
        base=min(data[size,0]);state={(0,0,0):1}
        for price in sorted(data[size,0]):
            if price-base>excess: break
            delta=defects.get((size,price), min(3*(size-2),(price-{9:557,10:744}[size])//3))
            nxt=defaultdict(int)
            for (n,c,d),ways in state.items():
                for copies in range(count-n+1):
                    v=c+copies*(price-base)
                    if v>excess:break
                    nxt[n+copies,v,min(9,d+copies*delta)]+=ways
            state=nxt
        return {(c,d):ways for (n,c,d),ways in state.items() if n==count}
    totals=defaultdict(int);kept=defaultdict(int)
    ten10=multiset(10,10,top-9840)
    for c12 in data[12,1]:
        for (extra,d),ways in ten10.items():
            price=c12+1296+7440+extra
            if price<=top:
                totals[price]+=ways
                if d==9:kept[price]+=ways
    nine10=multiset(10,9,top-9845)
    for c9 in data[9,0]:
        delta=defects.get((9,c9),min(21,(c9-557)//3))
        for (extra,d),ways in nine10.items():
            price=2592+c9+6696+extra
            if price<=top:
                totals[price]+=ways
                if d+delta>=9:kept[price]+=ways
    checked=[]
    for cost in range(9867,top+1):
        row=expected['layers'][str(cost)]
        assert totals[cost]==row['exact_price_patterns'],(cost,totals[cost],row)
        assert kept[cost]==row['surviving_typed_patterns'],(cost,kept[cost],row)
        checked.append({'cost':cost,'price_patterns':totals[cost],'surviving_patterns':kept[cost]})
    result={'independent_price_dp_passed':True,'layers':len(checked),
            'price_patterns':sum(r['price_patterns'] for r in checked),
            'surviving_typed_patterns':sum(r['surviving_patterns'] for r in checked),
            'costs':checked,'scope':'Price arithmetic only; native cover results are checked by replay.py.'}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='costs'},sort_keys=True))


if __name__=='__main__':
    main()
