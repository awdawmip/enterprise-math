"""Actual preferred-key graph menus after selector emission. All policy feedback is explicit."""
from argparse import ArgumentParser
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from projected.kernel.subset_kernel import emit
from copylife.kernel_checks import Physical,core

FALL=5
GRAPHS={'star':((0,1),(0,2)), 'triangle':((0,1),(1,2),(2,0))}
COVER={'star':(0,), 'triangle':(0,1)}
def payload(a,i):return 2+(i+a)%3

def prefix(C,initial):
    P=Physical(C,initial)
    h=0
    for i in range(4):
        P.drop(i);h|=int(C.observe_result(P.J))<<i
    for j in range(1,5):
        slot=3+j
        assert P.copy(8,slot)==j
        P.drop(slot);assert P.copy(9,8)==j
        assert P.copy(slot if h>>(j-1)&1 else 9,8)==j
        P.drop(8);P.drop(9)
    return P,h

def policy(graph,mode,msg,probe,send,next_menu):
    # Only the public message is passed over the join; no earlier code table or history.
    a=msg&1
    saved={}
    for j,i in enumerate(COVER[graph]):
        if mode=='stored':saved[payload(a,i)]=msg>>(j+1)&1
        elif mode=='early':saved[payload(a,i)]=probe(payload(a,i),'early')
    first=send(FALL if a else 1)
    t=next_menu(first)  # public late choice first disclosed here
    a_emitted=int(first==FALL)
    assert first in (1,FALL)
    for i in GRAPHS[graph][t]:
        key=payload(a_emitted,i)
        val=saved[key] if key in saved else probe(key,'late')
        send(FALL if val else key)
    return t

def once(C,h,graph,mode,t_input):
    initial=[h>>i&1 for i in range(4)]+list(range(1,5))+[0,0]
    P,observed=prefix(C,initial);pre=P.cost;before=P.codes()
    a=observed&1
    msg=a
    if mode=='stored':
        for j,i in enumerate(COVER[graph]):msg|=((observed>>(payload(a,i)-1))&1)<<(j+1)
    del a,observed
    trace=[];keys=[];lengths=[];reveals=[]
    def probe(key,stage):
        val=P.probe(3+key,(key&-key).bit_length()-1)
        assert stage==('late' if reveals else 'early')
        trace.append((stage,key,val));return val
    def submit(key):
        old=P.cost
        event=emit(P,[key])[0];k=event['bind_delivered']
        keys.append(k);lengths.append(P.cost-old);return k
    def next_menu(first):
        assert keys==[first] and not reveals
        reveals.append(t_input);return t_input
    t=policy(graph,mode,msg,probe,submit,next_menu)
    a=h&1
    want=[FALL if a else 1]
    for i in GRAPHS[graph][t]:
        k=payload(a,i)
        want.append(FALL if h>>(k-1)&1 else k)
    assert want==keys and before==P.codes() and P.cost==pre+sum(lengths)+8*len(trace) and len(reveals)==1
    return dict(guard=h,menu=t,deliveries=keys,early=sum(st=='early' for st,k,v in trace),late=sum(st=='late' for st,k,v in trace),
                prefix=pre,queries=trace,business=sum(lengths),total=P.cost)

def main():
    ap=ArgumentParser();ap.add_argument('--out',type=Path,default=Path(__file__).with_name('menu_kernel_results.json'));a=ap.parse_args()
    C=core.prior.Compiler(slots=10)
    rows=[];stats=[]
    for graph,es in GRAPHS.items():
        stats_by={}
        for mode in ('selector_only','early','stored'):
            group=[once(C,h,graph,mode,t) for h in range(16) for t in range(len(es))]
            rows.extend(dict(graph=graph,policy=mode,**r) for r in group)
            stats_by[mode]=dict(s=1+(len(COVER[graph]) if mode=='stored' else 0),max_early=max(r['early'] for r in group),
                                max_late=max(r['late'] for r in group),max_total=max(r['total'] for r in group))
            assert stats_by[mode]['max_late']==(2 if mode=='selector_only' else 1)
        stats.append(dict(graph=graph,policies=stats_by))
    for graph,es in GRAPHS.items():
        for h in range(16):
            for t in range(len(es)):
                rr=[r for r in rows if r['graph']==graph and r['guard']==h and r['menu']==t]
                assert len({tuple(r['deliveries']) for r in rr})==len({r['business'] for r in rr})==1
    pre={r['prefix'] for r in rows};assert len(pre)==1
    out=dict(status='PASS',physical_count=len(rows),prefix=pre.pop(),inventory=dict(slots=C.slots,members=C.members,candidates=len(C.H)),graphs=GRAPHS,cover=COVER,
             scope='10-slot original kernel; 4 real guard replies, fixed equal-length prefix. Late selector-dependent menus disclosed only after the full bound selector key. Sequential bodies, no gate charge. Original prices are concrete policy runs; coverage optimum is a bit/delay theorem.',
             measures=stats,physical=rows)
    a.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print('PASS',len(rows),out['prefix'],out['inventory'],stats)
if __name__=='__main__':main()
