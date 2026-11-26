"""Per-call exact reference check, not only aggregate graph equality."""
import json
from collections import Counter
from math import comb
from mask_hall import MaskOracle
from gal_path_hall import Bound,bitlist
from peel_hall import cut_reference

class Checked(MaskOracle):
    def paired_cut(self,a,b,d,t,L):
        wa=self.classes(a,d);wb=self.classes(b,d)
        opts={u:wa.get(u,0)|(wb.get(u,0)<<(d+1)) for u in bitlist(t)}
        caps=[comb(d,j) for j in range(d+1)]*2
        ans=super().paired_cut(a,b,d,t,L)
        assert ans==(cut_reference(opts,caps)<=L)
        self.threshold_stats['exact_cut_checks']+=1
        return ans

def main():
    rows=json.load(open('gap_target.json'))['rows'];total=Counter()
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*a=map(int,line.split());st=list(zip(a[::2],a[1::2]));b=Bound(st)
        for j in range(2):
            d=k+j;r=rows[2*i+j];o=Checked(b,st)
            assert o.v(b.full,d,b.full)==r['cap'];assert o.graphs(d,r['qs'],r['goals'])==r['adj']
            total.update(o.threshold_stats)
        b.clear()
    print(json.dumps(dict(total),sort_keys=True))
if __name__=='__main__':main()
