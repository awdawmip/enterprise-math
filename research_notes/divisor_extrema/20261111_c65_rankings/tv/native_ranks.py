"""C65 direct positive BRC branch checks at the fifth-place switch and r=3 cut."""
import argparse
from collections import Counter
from fractions import Fraction as Q
import json
from pathlib import Path
import sys

RATES=(Q(1,4),Q(1),Q(4))
TAILS=("557","575","755")


def run(brc,compact,probes):
    count=Counter()

    def serial(hist,weight):
        count["histogram_serial"]+=1
        return brc.histogram_serial(hist,brc.weight_histogram([weight]))

    def merge(a,b):
        count["histogram_recoalesce"]+=1
        return brc.histogram_recoalesce(a,b)

    def propagate(stock,word,prior,initial_branches):
        inventory=list(stock)
        histograms=[brc.weight_histogram([p] if p else []) for p in prior]
        for sym in word:
            dest=[brc.weight_histogram([]) for _ in RATES]
            pos="2357".index(sym)
            assert inventory[pos]>0
            for s,hist in enumerate(histograms):
                if hist.is_zero:continue
                total=inventory[0]+inventory[1]+RATES[s]*inventory[2]+inventory[3]
                weight=Q(inventory[pos])*(RATES[s] if sym=="5" else 1)/total
                if sym=="3": updates=((0,Q(7,8)),(s,Q(1,8)))
                else: updates=((min(s+1,2) if sym=="2" else s,Q(1)),)
                for target,prob in updates:
                    dest[target]=merge(dest[target],serial(hist,weight*prob))
            histograms=dest
            inventory[pos]-=1
        assert inventory==[0,0,2,1]
        predicted=initial_branches*2**word.count("3")
        assert sum(h.count for h in histograms)==predicted
        # Every complete-tail mass retains the raw branch weight and multiplicity.
        # All three tails contain only 5 and 7, so the state stays fixed.
        tail_masses=[]
        for j,tail in enumerate(TAILS):
            all_terms=brc.weight_histogram([])
            for s,hist in enumerate(histograms):
                five,seven=2,1
                likelihood=Q(1)
                for sym in tail:
                    total=RATES[s]*five+seven
                    likelihood*= (RATES[s]*five if sym=="5" else seven)/total
                    five-=int(sym=="5");seven-=int(sym=="7")
                assert likelihood==probes.T[s][j]
                if not hist.is_zero:all_terms=merge(all_terms,serial(hist,likelihood))
            assert all_terms.count==predicted
            tail_masses.append(all_terms.total_mass)
            count["complete_tails"]+=1
            count["complete_branches_with_multiplicity"]+=all_terms.count
        total=sum(h.total_mass for h in histograms)
        assert sum(tail_masses)==total
        return [h.total_mass/total for h in histograms],tail_masses

    def observe(inputs):
        (p,a),(q,b)=inputs
        delta=sum(abs(x-y) for x,y in zip(p,q))/2
        ratios=[x/y for x,y in zip(a,b)]
        return delta,max(ratios)/min(ratios)

    full=[]
    for k in (12,13):
        words={"A":(1,)*(k-1)+(0,0),"E":(2,0)+(1,)*(k-3)+(0,0),
               "F":(1,)*(k-3)+(0,1,1,0)}
        measured={}
        for label,path in words.items():
            word='23'.join('5'*m for m in path)
            v,H=observe([propagate((k,k,k+1,1),word,tuple(Q(i==s) for i in range(3)),1)
                         for s in (0,1)])
            assert v==compact.total_variation(k,path)
            assert H==probes.hilbert_ratio(k,path)
            measured[label]=[v,H]
        ratio={p:str(measured[p][0]/measured["A"][0]) for p in ('E','F')}
        assert (measured['E'][0]<measured['F'][0])==(k==12)
        full.append(dict(k=k,checked_labels=list(words),TV_ratio_over_A=ratio,
                         E_H_minus_one_over_F=str((measured['E'][1]-1)/(measured['F'][1]-1))))
    suffixes=["1100","1010","1001","0020","0110","0101","0011","0002"]
    records={}
    endpoints=(Q(1,3),Q(4,5))
    for code in suffixes:
        path=tuple(map(int,code))
        word='23'.join('5'*m for m in path)
        inputs=[]
        for u in endpoints:
            direct=propagate((3,3,4,1),word,(Q(7,8),u/8,(1-u)/8),3)
            z=u;c=4
            for r,m in zip((3,2,1),path[:-1]):
                z=compact.evaluate(compact.block(r,c,m),z)
                c-=m
            assert direct[0][2]==compact.evaluate(compact.terminal(c),z)
            inputs.append(direct)
        v,H=observe(inputs)
        records[code]=(v,H)
    assert sorted(suffixes,key=lambda s:records[s][0])==suffixes
    cut=dict(inputs=list(map(str,endpoints)),physical_suffix_TV_order=suffixes,
             observed_H_order=sorted(suffixes,key=lambda s:records[s][1]),
             TV_ratios_over_A={s:str(v/records['1100'][0]) for s,(v,H) in records.items()},
             H_minus_one_ratios_over_A={s:str((H-1)/(records['1100'][1]-1)) for s,(v,H) in records.items()})
    return dict(status="PASS",source="enterprise-math src/enterprise_math/brc_histogram.py@de41b8c",
                full=full,cut=cut,count=dict(count))


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--c64",type=Path,required=True)
    parser.add_argument("--native-root",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    sys.path[:0]=[str(args.native_root.resolve()),str(args.c64.resolve())]
    from enterprise_math import brc_histogram
    import suffix_limits,observable_minimum
    report=run(brc_histogram,suffix_limits,observable_minimum)
    args.output.write_text(json.dumps(report,indent=2)+"\n")
    print(report['status'],report['cut']['observed_H_order'],report['count'])
