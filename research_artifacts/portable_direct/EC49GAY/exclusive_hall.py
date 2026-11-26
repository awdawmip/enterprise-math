"""EC49GAY extension: exact exclusive-target cuts before joint matching."""
from collections import Counter
from math import comb
from time import perf_counter_ns
import json
import threshold_hall as prev
from mask_hall import MaskOracle
from gal_path_hall import Bound,bitlist
from peel_hall import cut_reference

class ExclusiveOracle(MaskOracle):
    def paired_cut(self,a,b,d,t,L):
        st=self.threshold_stats;st['cut_calls']+=1
        sa=t&a&~self.profile(a,d)[0];sb=t&b&~self.profile(b,d)[0]
        z=t&~(sa|sb);k=t.bit_count()-L
        if z.bit_count()>=k:
            st['zero_hits']+=1;return True
        u=sa&~sb;v=sb&~sa;x=sa&sb
        # The old exact individual Hall oracle is reused on EXCLUSIVE live targets.
        # These counts and the shared target bound count each target at most once.
        if self.hall(a,d,u)+self.hall(b,d,v)+x.bit_count()<=L:
            st['exclusive_hits']+=1;return True
        wa=self.classes(a,d);wb=self.classes(b,d)
        opts={w:wa.get(w,0)|(wb.get(w,0)<<(d+1)) for w in bitlist(t&~z)}
        st['fallbacks']+=1;st['zero_removed']+=z.bit_count()
        return prev.at_most(opts,[comb(d,j) for j in range(d+1)]*2,L,st)

class Checked(ExclusiveOracle):
    def paired_cut(self,a,b,d,t,L):
        wa=self.classes(a,d);wb=self.classes(b,d)
        opts={w:wa.get(w,0)|(wb.get(w,0)<<(d+1)) for w in bitlist(t)}
        caps=[comb(d,j) for j in range(d+1)]*2
        ans=super().paired_cut(a,b,d,t,L)
        assert ans==(cut_reference(opts,caps)<=L)
        self.threshold_stats['exact_cut_checks']+=1
        return ans

def run():
    old=json.load(open('gap_target.json'))['rows'];out={}
    for mode in ('zero','exclusive','exclusive','zero','checked'):
        agg=Counter();search=Counter();rows=[];elapsed=0
        for i,line in enumerate(open('ga_nodes.txt')):
            k,n,*a=map(int,line.split());st=list(zip(a[::2],a[1::2]));b=Bound(st)
            for j in range(2):
                d=k+j;r=old[2*i+j];o=MaskOracle(b,st,False) if mode=='zero' else ExclusiveOracle(b,st) if mode=='exclusive' else Checked(b,st)
                t0=perf_counter_ns();assert o.v(b.full,d,b.full)==r['cap'];assert o.graphs(d,r['qs'],r['goals'])==r['adj'];elapsed+=perf_counter_ns()-t0
                agg.update(o.threshold_stats);search.update(o.stats);rows.append([i,d,dict(o.threshold_stats)])
            b.clear()
        out.setdefault(mode,[]).append({'stats':dict(agg),'search':dict(search),'ns':elapsed,'rows':rows})
    # Extra hall_misses are expected from exclusive checks; all actual search outcomes equal.
    base=out['zero'][0]['search'];assert all({k:v for k,v in r['search'].items() if k!='hall_misses'}=={k:v for k,v in base.items() if k!='hall_misses'} for runs in out.values() for r in runs)
    print(json.dumps(out,separators=(',',':')))
if __name__=='__main__':run()
