"""EC49GAU: exact capacity peeling for finite target-resource graphs."""
from collections import Counter
from functools import lru_cache
from random import Random
from time import perf_counter_ns
from math import comb
import json
from gal_path_hall import Bound, bitlist
from joint_hall import HallOracle
from tail_hall import match


def peel(opts, caps, stats):
    """opts maps target IDs to category bitmasks; caps are nonnegative integers."""
    opts = dict(opts)
    caps = list(caps)
    paid = 0
    active = sum(1 << i for i, c in enumerate(caps) if c)
    stats['calls'] += 1
    stats['targets'] += len(opts)
    stats['edges_before'] += sum((m & active).bit_count() for m in opts.values())
    while opts:
        single = Counter()
        for t, m in list(opts.items()):
            m &= active
            if not m:
                del opts[t]
                stats['dead'] += 1
            else:
                opts[t] = m
                if m & (m-1) == 0:
                    single[m] += 1
        if single:
            for bit, count in single.items():
                j = bit.bit_length()-1
                take = min(count, caps[j])
                paid += take
                caps[j] -= take
                if not caps[j]:
                    active &= ~bit
                stats['singleton_paid'] += take
                stats['singleton_lost'] += count-take
            opts = {t:m for t,m in opts.items() if m not in single}
            continue
        degree = Counter(b for m in opts.values() for b in bitlist(m))
        rich = sum(b for b, count in degree.items() if caps[b.bit_length()-1] >= count)
        if not rich:
            break
        remove = [t for t,m in opts.items() if m & rich]
        paid += len(remove)
        stats['rich_paid'] += len(remove)
        for t in remove:
            del opts[t]
        active &= ~rich
    stats['core_targets'] += len(opts)
    stats['core_edges'] += sum(m.bit_count() for m in opts.values())
    return paid + match({t:tuple(b.bit_length()-1 for b in bitlist(m)) for t,m in opts.items()},caps)


def cut_reference(opts,caps):
    n=len(opts)
    return n-max(sum(m & ~s == 0 for m in opts.values())-sum(caps[b.bit_length()-1] for b in bitlist(s)) for s in range(1<<len(caps)))


class PeelOracle(HallOracle):
    def __init__(self,b,st):
        super().__init__(b,st,True)
        self.peel_stats=Counter()
        @lru_cache(None)
        def classes(s,d):
            words=self.profile(s,d)[2]
            # Every word in a sign-count class has identical eligibility.
            return {t:sum(1<<j for j in {w.bit_length() and (w.bit_length()-1).bit_count() for w in bitlist(m)}) for t,m in words.items()}
        self.classes=classes

    def paired(self,a,b,d,l,r,x):
        wa=self.classes(a,d); wb=self.classes(b,d)
        opts={t:(wa.get(t,0) if t&(l|x) else 0)|((wb.get(t,0) if t&(r|x) else 0)<<(d+1)) for t in bitlist(l|r|x)}
        self.stats['paired_calls']+=1
        return peel(opts,[comb(d,j) for j in range(d+1)]*2,self.peel_stats)


def main():
    rng=Random(49261127); syn=Counter()
    for _ in range(3000):
        m=rng.randrange(1,9); n=rng.randrange(0,33)
        caps=[rng.randrange(7) for _ in range(m)]
        opts={t:rng.randrange(1<<m) for t in range(n)}
        assert peel(opts,caps,syn)==cut_reference(opts,caps)
    old=json.load(open('gap_target.json'))['rows']; totals={m:Counter() for m in ('word','peel')}; times=Counter(); aggregate=Counter(); rows=[]
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*a=map(int,line.split()); st=list(zip(a[::2],a[1::2])); b=Bound(st)
        for h in range(2):
            row=old[2*i+h]; d=k+h; assert (row['i'],row['d'])==(i,d)
            rr={'i':i,'d':d,'checks':{}}
            for m,o in [('word',HallOracle(b,st,True)),('peel',PeelOracle(b,st))]:
                t0=perf_counter_ns(); assert o.v(b.full,d,b.full)==row['cap']; adj=o.graphs(d,row['qs'],row['goals']); times[m]+=perf_counter_ns()-t0
                assert adj==row['adj']; totals[m].update(o.stats); rr['checks'][m]=dict(o.stats)
                if m=='peel':aggregate.update(o.peel_stats);rr['peel']=dict(o.peel_stats)
            assert rr['checks']['word']==rr['checks']['peel']; rows.append(rr)
        b.clear()
    print(json.dumps({'synthetic':dict(syn),'stats':{m:dict(v) for m,v in totals.items()},'peel':dict(aggregate),'times_ns':dict(times),'rows':rows},sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
