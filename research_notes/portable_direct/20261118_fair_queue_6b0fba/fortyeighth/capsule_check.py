"""Replay the positive-row, 24-setting product benchmark with exact rational weights."""
import argparse
import hashlib
import json
import sys
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path

KERNEL_SHA = "4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f"
RECEIPTS = {
    "twelfth/compatibility_checked.json": "738ee3e3789bb89954abba577dc695e4dea9f70d01bd324903fc8024d8f0172a",
    "seventeenth/context_checked.json": "45024f1fae8e21a313016db985e2cd59ade9f2485a4ddf11d75d5ae879aae799",
}
PM = tuple(tuple(3*i+j for j in range(3)) for i in range(3)) + tuple(
    tuple(3*i+j for i in range(3)) for j in range(3))
CELLS = list(product(range(4),range(8)))


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def bell(row):
    return tuple(2*row[x]+row[2+y] for x,y in product(range(2),repeat=2))


def pm(row):
    return tuple(sum(row[item]<<offset for offset,item in enumerate(context)) for context in PM)


def bbad(setting, output):
    return ((output.bit_count()&1) != (setting==3))


def mbad(setting, output):
    return ((output.bit_count()&1) != (setting==5))


def tv(p,q):
    return sum(abs(p.get(k,0)-q.get(k,0)) for k in CELLS)/2


def goal(i,j,e):
    return {(a,b):(e if bbad(i,a) else 1-e)/8 if not mbad(j,b) else F(0)
            for a,b in CELLS}


def optimum(e):
    return max(F(1,6), F(3,8)-e, e-F(5,8))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo",type=Path,help="enterprise-math checkout with src/enterprise_math/brc_weighted.py")
    ap.add_argument("--rounds",type=Path,default=Path(__file__).resolve().parents[1])
    args=ap.parse_args()
    if args.repo is None:
        args.repo=next((p for p in (Path.cwd(),*Path(__file__).resolve().parents)
                        if (p/"src/enterprise_math/brc_weighted.py").is_file()), None)
    if args.repo is None:
        ap.error("supply --repo pointing to enterprise-math")
    assert digest(args.repo/"src/enterprise_math/brc_weighted.py")==KERNEL_SHA
    sys.path.insert(0,str(args.repo/"src"))
    from enterprise_math import brc_weighted as brc
    docs=[]
    for source,sha in RECEIPTS.items():
        path=args.rounds/source
        assert digest(path)==sha
        docs.append(json.loads(path.read_text()))
    assert docs[0]["eta_three_quarters"]["parity_probabilities"]==["1/8"]*3+["7/8"]
    assert docs[1]["external_witness"]["local_three_bit_string_probabilities"]==["1/4"]*4
    btypes={};mtypes={}
    for row in product(range(2),repeat=4):
        b=bell(row);btypes[b]=sum(bbad(i,v) for i,v in enumerate(b))
    for row in product(range(2),repeat=9):
        m=pm(row);mtypes[m]=sum(mbad(i,v) for i,v in enumerate(m))
    assert len(btypes)==16 and len(mtypes)==512
    counts=Counter()
    for bl,ml in product(btypes.values(),mtypes.values()):
        assert (4-bl)*(6-ml)<=15 and bl*(6-ml)<=15 and ml>=1
        counts[bl,ml]+=1
    assert sum(counts.values())==8192
    muni=[v for v,e in mtypes.items() if e==1]
    assert len(muni)==96
    def single_rows(bl):
        B=[v for v,e in btypes.items() if e==bl]
        assert len(B)==8
        out=[Counter() for _ in range(24)]
        branch=brc.cwm_propagate(brc.cwm_edge(F(1,len(B))),brc.cwm_edge(F(1,len(muni))))
        for a,b in product(B,muni):
            for i,v in enumerate(a):
                for j,w in enumerate(b):
                    agg=out[6*i+j]
                    agg[v,w]=brc.cwm_recoalesce(agg.get((v,w),brc.CWM_ZERO),branch)
        for d in out:
            assert sum(x.total for x in d.values())==1 and sum(x.count for x in d.values())==768
        return [{k:z.total for k,z in x.items()} for x in out]
    one,three=single_rows(1),single_rows(3)
    grid=sorted({F(i,48) for i in range(49)}|{F(1,11),F(4,13),F(10,11)})
    settings=0
    for e in grid:
        f=min(F(3,4),max(F(1,4),e))
        mix=2*(f-F(1,4))
        for i,j in product(range(4),range(6)):
            k=6*i+j
            p={c:(1-mix)*one[k][c]+mix*three[k][c] for c in CELLS}
            q=goal(i,j,e)
            assert sum(p.values())==sum(q.values())==1 and tv(p,q)==optimum(e)
            settings+=1
    witnesses=[]
    for i,j in product(range(4),range(6)):
        inrow=one[i*6+j]
        target=goal(i,j,F(1,8))
        result=Counter();flips=Counter()
        for (a,b),mass in inrow.items():
            bt,mt=bbad(i,a),mbad(j,b)
            bflip=F(0) if not bt else F(1) if mt else F(2,5)
            for do,pr in [(0,1-bflip),(1,bflip)]:
                result[a^do,b^int(mt)]+=mass*pr
                flips[do,int(mt)]+=mass*pr
        assert all(result[k]==target[k] for k in CELLS)
        assert [flips[a,b] for a,b in ((0,0),(1,0),(0,1),(1,1))]==[F(3,4),F(1,12),F(1,8),F(1,24)]
        assert tv(inrow,target)==F(1,4)
        witnesses.append({f"{a}{b}":str(flips[a,b]) for a,b in sorted(flips)})
    def mass(n,j,p):
        return comb(n,j)*p**j*(1-p)**(n-j)
    rejection=sum(mass(128,j,F(5,8)) for j in range(96,129))
    miss=sum(mass(128,j,F(7,8)) for j in range(96))
    result=dict(future_protocol=dict(n=128,threshold=96,positive_row_upper_tail=str(rejection),
                positive_row_upper_tail_decimal=float(rejection), product_target_miss=str(miss),
                product_target_miss_decimal=float(miss)),kernel_sha256=KERNEL_SHA,source_receipt_hashes=RECEIPTS,
                common_rows=sum(counts.values()),failure_count_histogram={f"{b},{m}":n for (b,m),n in sorted(counts.items())},
                PM_one_failure_rows=len(muni),number_of_rational_e=len(grid),settingwise_tests=settings,
                CWM_product_rows_per_extreme=768,CWM_joins_per_extreme=24*768,paired_source_point=
                dict(eta="3/4",e="1/8",Bell_separate_TV="1/8",PM_separate_TV="1/6",
                     joint_minimax_TV="1/4",settings_repaired=len(witnesses),flip_flags_Bell_PM=witnesses[0]),
                experiment_event_rows=0)
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
