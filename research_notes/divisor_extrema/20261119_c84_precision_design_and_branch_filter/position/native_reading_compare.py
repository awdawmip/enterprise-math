"""Compare quarter and midpoint stocks using original certified finite readings."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import numpy as np
import critical_bins as C
from native import native_tail_ratios


def singletons(keys):
    _,inv,counts=np.unique(keys,axis=0,return_inverse=True,return_counts=True)
    return counts[inv]==1


def experiment(c,B,precisions):
    assert B%4==0
    stocks=[c,c+B//4,c+B//2,c+B]
    C.prepare(stocks[-1]); C.terminal.cache_clear()
    pmax=max(precisions)
    rows=[]; labels=[]; rational_checks=0
    for v in range(2,c+1):
        for w in range(2,v+1):
            middle=C.block(v,w,3,C.terminal(w))
            values=[C.full_width(n,v,middle) for n in stocks]
            if c<=8:
                for n,(lo,hi) in zip(stocks,values):
                    tails=native_tail_ratios(n,v,w)
                    exact=max(tails)/min(tails)
                    assert isinstance(exact,Fraction) and lo<=exact*C.UNIT<=hi
                    rational_checks+=1
            rows.append([C.bin_number(value,pmax+1,(0,1))-(1<<(pmax+1))
                         for value in values])
            labels.append((v,w))
    table=np.asarray(rows,dtype=np.int64)
    outcomes=[]; witnesses=[]
    for p in precisions:
        bins=table//(1<<(pmax-p))
        for origin in product(range(2),repeat=3):
            qkeys=(bins[:,[0,1,3]]+np.asarray(origin))//2
            mkeys=(bins[:,[0,2,3]]+np.asarray(origin))//2
            endpoint=singletons(qkeys[:,[0,2]])
            quarter=singletons(qkeys); midpoint=singletons(mkeys)
            assert np.all(quarter|~endpoint) and np.all(midpoint|~endpoint)
            outcomes.append({'p':p,'origins_halves':list(origin),
                             'endpoint':int(endpoint.sum()),
                             'quarter':int(quarter.sum()),'midpoint':int(midpoint.sum())})
            for name,won,lost,losing_keys,winning_keys in [
                ('quarter_only',quarter,midpoint,mkeys,qkeys),
                ('midpoint_only',midpoint,quarter,qkeys,mkeys)]:
                if any(x['kind']==name for x in witnesses): continue
                idx=np.flatnonzero(won & ~lost)
                if len(idx):
                    i=int(idx[0]); competitors=np.flatnonzero(np.all(losing_keys==losing_keys[i],axis=1))
                    assert len(competitors)>=2
                    witnesses.append({'kind':name,'p':p,'origins_halves':list(origin),
                                      'source':labels[i],
                                      'losing_cell':losing_keys[i].tolist(),
                                      'same_losing_cell_labels':[labels[int(j)] for j in competitors],
                                      'winning_cell':winning_keys[i].tolist()})
    return {'c':c,'outer_gap':B,'stocks':stocks,'n':len(rows),
            'read_intervals':4*len(rows),'rational_enclosures':rational_checks,
            'interval_bits':C.BITS,'outcomes':outcomes,'witnesses':witnesses}


def main():
    results=[]
    for case in [(8,4,[4,6,8,10]),(64,16,[8,10,12,14,16,18]),
                 (256,64,[10,12,14,16,18,20])]:
        x=experiment(*case); results.append(x)
        print({'c':x['c'],'n':x['n'],'quarter_more':sum(o['quarter']>o['midpoint'] for o in x['outcomes']),
               'midpoint_more':sum(o['midpoint']>o['quarter'] for o in x['outcomes']),
               'ties':sum(o['midpoint']==o['quarter'] for o in x['outcomes'])},flush=True)
    out={'scope':'Finite full-stock comparisons with the same first/last stocks, p, source population and corresponding origins; not a limit proof',
         'cases':results}
    Path(__file__).with_name('native_position_comparison.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__': main()
