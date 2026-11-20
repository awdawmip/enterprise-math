"""Finite cross-checks. Numerical min/max claims are always labelled by input/game."""
from itertools import product
from pathlib import Path
from collections import Counter
import argparse, json
from oracle import DomainBellman,WorldBellman

D=('drop',0);S=('copy',0,0);C=('copy',1,0);A=('round',0,0);B=('round',1,0)
CASES=[
 ('copy_first', (C,A)),
 ('presence_first',(S,A)),
 ('drop_then_create',(D,A)),
 ('copy_outlives_source',(A,('copy',0,1),('drop',1),('round',1,1))),
 ('self_copy_drop_mix',(S,('round',0,1),C,D,('round',2,1))),
 ('new_key_copied_three',(B,C,C,C)),
]
def replay_api(p,x):
    """Driver consumes strategy.action and advances exclusively on allowed feedback."""
    st=p.start;table=list(x);ops=[];cost=0
    while st[0]<len(p.events):
        act=p.action(st);e=p.events[st[0]]
        if act[0]=='read':
            i,bit=act[1:];res=(table[i]>>bit)&1;cost+=8
        elif act[0]=='round':
            res=act[1];assert res not in table and res in p.keys(e[1]);table[e[2]]=res
            cost+=p.weight(res)+p.charge_business*p.fixed[e[1]]
        elif e[0]=='copy':
            val=table[e[2]];table[e[1]]=val
            res=val if e[1]!=e[2] and p.visible_copy else bool(val)
            cost+=(p.copy_charge(val) if e[1]!=e[2] else 8)*p.charge_business
        else:
            res=bool(table[e[1]]);table[e[1]]=0;cost+=(p.q+9)*p.charge_business
        ops.append((act,res));st=p.advance(st,act,res)
    return cost,ops,table

def price_family():
    base=(B,);p=DomainBellman(2,base)
    maxima={4:[0,None],5:[0,None],6:[0,None]};witnesses=[]
    for x in product(range(10),repeat=2):
        v,tr,last=p.replay(x);k=tr[-1][-1]
        if v>maxima[k][0]:maxima[k]=[v,x]
    assert [maxima[k][0] for k in (4,5,6)]==[95,89,93]
    def take_tree(st):
        a=p.action(st)
        if a[0]=='round':return {'key':a[1]}
        return {'read':a[1:],'0':take_tree(p.advance(st,a,0)),'1':take_tree(p.advance(st,a,1))}
    rates=[p.copy_charge(k) for k in (4,5,6)];assert rates==[43,44,44]
    finite=[]
    for z in (6,5,4,float('-inf')):
        p1=DomainBellman(2,base);q1=WorldBellman(2,base)
        wts={4:z,5:8,6:4}
        p1.weight=lambda k:wts[k];q1.weight=lambda k:wts[k]
        g=p1.value();assert g==q1.value()
        finite.append(dict(discounted_key4_weight='negative_infinity' if z==float('-inf') else z,exact_uniform_minimax=g))
    assert [a['exact_uniform_minimax'] for a in finite]==[95,94,93,93]
    for n in range(7):
        es=base+(C,)*n;p0=DomainBellman(2,es,(0,0));q0=DomainBellman(2,es)
        uni=q0.value();pt=p0.value()
        assert uni==max(95+43*n,93+44*n) and pt==min(87+43*n,85+44*n)
        if n:
            changed=base+((C,('drop',1))*(n-1))+(C,)
            assert DomainBellman(2,changed,(0,0)).value()==pt+13*(n-1)
        witnesses.append(dict(copies=n,uniform_minimax=uni,empty_table_pointwise=pt,empty_table_witness=p0.replay((0,0))[1],distinct_copy_prices=rates))
    return dict(domain=[0,9],one_policy_all_horizons=take_tree(p.start),base_cost_maxima_by_key=maxima,
                discounted_leaf_checks=finite,finite_prefixes=witnesses,
                general_proof='oracle_notes.md, independent hand lower bounds and one fixed safe tree')

def run():
    out=[];N=0
    for name,es in CASES:
        px=DomainBellman(2,es);wx=WorldBellman(2,es);M=px.value()
        assert M==wx.value()==DomainBellman(2,es,early_probes=False).value()
        count=Counter();point=Counter();backend=0;worst=None
        for x in product(range(10),repeat=2):
            t=DomainBellman(2,es,x)
            v=t.value()
            assert v==wx.value_on(x)==DomainBellman(2,es,x,early_probes=False).value()
            a,b,c=replay_api(t,x);assert a==t.replay(x)[0]==v
            m,_,_=replay_api(px,x);assert m==px.replay(x)[0]<=M
            count[m]+=1;point[v]+=1;N+=1
            if m==M and worst is None:worst=x
        assert max(count)==M
        out.append(dict(name=name,events=es,inputs=100,point_cost_histogram=point,
                        uniform_cost_histogram=count,uniform_worst=M,uniform_witness=worst,
                        uniform_physical_trace=px.replay(worst)[1],world_dp_states=wx.dp.cache_info().currsize))
    retained=DomainBellman(2,(C,A),(1,1));discarded=DomainBellman(2,(C,A),(1,1),visible_copy=False)
    assert retained.value()==107 and discarded.value()==115
    return dict(status='PASS',scope='independent control decision games (not native BRC); self-copy/drop provide presence, nonself copy full code; all figures are original body command costs for default three-target library, no wrapper',
                number_of_pointwise_domain_vs_world_equalities=N,number_of_uniform_minimax_equalities=len(CASES),
                inputs_replayed_by_each_of_pointwise_and_uniform_policies=N,
                no_early_probes_equalities_pointwise=N,no_early_probes_equalities_minimax=len(CASES),
                schedules=out,identity_disclosure=dict(comparison='copy result vs only its presence and copied-alias relation; the mandatory copy costs the same on this input',
                initial=(1,1),events=(C,A),full=retained.replay((1,1)),presence_and_alias_only=discarded.replay((1,1))),
                delayed_copy_prices=price_family())
if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('oracle_results.json'))
    args=ap.parse_args();res=run();args.output.write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n');print('PASS',res['number_of_pointwise_domain_vs_world_equalities'],[x['uniform_worst'] for x in res['schedules']])
