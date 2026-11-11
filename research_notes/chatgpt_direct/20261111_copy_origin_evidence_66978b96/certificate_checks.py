from pathlib import Path
from itertools import product
import json
from certificates import optimum,replay
from oracle import Model,DomainBellman
R=lambda t,d:('round',t,d)
C=lambda d,s:('copy',d,s)
D=lambda d:('drop',d)
S=[(C(1,0),R(0,0)),(C(0,0),D(1),R(0,0)),(R(0,1),C(1,0),R(1,0),D(1),R(0,0)),(R(1,0),C(1,0),D(0),R(1,0)),(R(2,0),C(1,0)),(C(0,1),C(1,0),D(0),R(0,1),D(1)),(D(0),C(1,0),R(0,0),C(1,0)),(R(0,1),C(1,1),D(0),R(0,1)),(C(0,1),D(0),C(1,1))]
def harness(r,ev,x,p):
    m=Model(r,ev); live=list(x);cost=0
    def read(i,b):
        nonlocal cost
        cost+=8;return live[i]>>b&1
    def do(e,k):
        nonlocal cost
        if e[0]=='round':
            t,d=e[1:];assert k in m.keys(t) and k not in live
            cost+=m.fixed[t]+m.weight(k);live[d]=k
        elif e[0]=='drop':
            a=live[e[1]];live[e[1]]=0;cost+=m.q+9;return bool(a)
        else:
            d,s=e[1:];a=live[s];live[d]=a;cost+=8 if d==s else m.copy_charge(a)
            return bool(a) if d==s else a
    n,changed=replay(r,ev,p,read,do)
    return cost,n,changed
def main():
    xs=list(product(range(10),repeat=2));stats=[]
    for ev in S:
        plans={};vals=[]
        for x in xs:
            p=optimum(2,ev,x);c,_,changed=harness(2,ev,x,p)
            assert not changed and c==p[0]==DomainBellman(2,ev,x,early_probes=False).value()
            plans[p[1:]]=p;vals.append(c)
        checks=sum(harness(2,ev,x,p)[2] for p in plans.values() for x in xs)
        stats.append(dict(events=ev,pointwise_range=[min(vals),max(vals)],unique_instructions=len(plans),replays=len(plans)*len(xs),online_fallbacks=checks))
    ret=dict(status='PASS',old_tables_per_schedule=100,pointwise_equalities=len(xs)*len(S),cross_replays=sum(a['replays'] for a in stats),fallbacks=sum(a['online_fallbacks'] for a in stats),cases=stats)
    Path(__file__).with_name('certificate_results.json').write_text(json.dumps(ret,indent=2)+'\n');print(ret['pointwise_equalities'],ret['cross_replays'],ret['fallbacks'])
if __name__=='__main__':main()
