"""Sharp one-create specialization with an arbitrary fixed copy/drop prefix and suffix."""
from itertools import product
from pathlib import Path
import json
from oracle import Model
from certificates import optimum

def evaluate(r,events,x):
    model=Model(r,events);M=model.M;occ=list(range(r));codes=list(x)
    seen=set();born=r;fees=0;m=0;live=None;u=None;t=None
    def ref_price(s):
        if s<0:return model.copy_charge(0)
        return model.copy_charge(x[s])
    for e in events:
        if e[0]=='round':
            assert live is None
            _,t,d=e;live=set(occ)-{-1};u=len(live-seen)
            admitted=[k for k in model.keys(t) if k not in {x[o] for o in live}]
            occ[d]=born
        elif e[0]=='drop':
            d=e[1];fees+=model.q+9
            if occ[d]>=0 and occ[d]<r and x[occ[d]]==0:seen.add(occ[d])
            occ[d]=-1
        else:
            _,d,s=e;o=occ[s]
            if d==s:
                fees+=8
                if 0<=o<r and x[o]==0:seen.add(o)
            else:
                if o==born:m+=1
                else:fees+=ref_price(o)
                if 0<=o<r:seen.add(o)
                occ[d]=o
    assert live is not None
    classes={}
    for k in admitted:
        tag=(k>>(model.b-1)&1,k>>(model.q-1)&1)
        if tag not in classes or (k.bit_count(),k)<(classes[tag].bit_count(),classes[tag]):classes[tag]=k
    base=fees+model.fixed[t]+8*u
    offer=lambda k:base+model.weight(k)+m*model.copy_charge(k)
    best=min(offer(k) for k in classes.values());assert best==min(map(offer,admitted))
    return dict(best=best,eligible=admitted,extra_queries=u,descendant_copies=m,base=base,candidates_by_class=sorted(classes.values()),optimal_keys=[k for k in admitted if offer(k)==best])
def main():
    ops=[('copy',1,0),('copy',0,1),('copy',0,0),('drop',0)]
    xs=list(product(range(10),repeat=2));count=0;queries={};sz={}
    for a,b in product(ops,repeat=2):
        for k in (0,1,2): # one create before, between or after the two prescribed operations
            seq=[a,b];seq.insert(k,('round',(k+1)%3,k%2));seq=tuple(seq)
            for x in xs:
                v=evaluate(2,seq,x);assert v['best']==optimum(2,seq,x)[0]
                u=v['extra_queries'];queries[u]=queries.get(u,0)+1
                f=len(v['candidates_by_class']);sz[f]=sz.get(f,0)+1;count+=1
    r=39; x=[k for k in range(41,81) if k not in (48,79)]+[0];assert len(x)==r
    witness=[]
    for n in (0,1,2,9,10,11,12):
        e=(('round',1,0),)+(('copy',1,0),)*n
        v=evaluate(r,e,x); model=Model(r,e)
        assert v['extra_queries']==39 and v['eligible']==[48,79]
        both=[v['base']+model.weight(k)+n*model.copy_charge(k) for k in v['eligible']]
        witness.append(dict(n=n,keys=v['optimal_keys'],costs=both))
    assert witness[-3]['costs']==[1129,1129] and witness[-2]['costs']==[1200,1199]
    z=dict(status='PASS',closed_form_comparisons=count,extra_queries_hist=queries,representative_count_hist=sz,
        scope='pointwise exact for exactly one creation and any fixed copy/drop prefix and suffix; direct linear origin scan plus eligible-key scan; not physical BRC except separately stated',
        extremal=dict(r=39,target=1,old=x,keys=[48,79],certificate_reads=39,rows=witness))
    Path(__file__).with_name('one_creation_results.json').write_text(json.dumps(z,indent=2)+'\n')
    print('PASS',count,witness[-3:])
if __name__=='__main__':main()
