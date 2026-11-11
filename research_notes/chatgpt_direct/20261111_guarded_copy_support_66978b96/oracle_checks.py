"""Verify exact values on a physical-reply branch DAG in two independent state spaces."""
import argparse,json
from pathlib import Path
from itertools import product
from collections import Counter
from oracle import Program,Domains,Worlds,fork_m

def examples():
    ans=[]
    # Full observed key of a nonself copy; two routes then reconverge at a round.
    p=Program(2);w=p.add(('round',0,1));s=p.add(('copy',1,0),w);d=p.add(('drop',0),w)
    p.add(('copy',0,1),d,[(1,s),(4,s)]);ans.append(('complete_copy_reply_join',p))
    # Drop/presence chooses between asymmetric destinations and addresses.
    p=Program(2);u=p.add(('round',1,0));a=p.add(('copy',0,1),u);b=p.add(('copy',1,0),u)
    p.add(('drop',0),a,[(1,b)]);ans.append(('drop_routes_copy',p))
    # Self-copy gives presence, not the old key. Nonself replies further fork.
    p=Program(2);a=p.add(('round',2,1));b=p.add(('round',1,0))
    x=p.add(('copy',0,1),a,[(0,b),(2,b)])
    y=p.add(('copy',1,0),b,[(1,a),(4,a)])
    p.add(('copy',0,0),x,[(1,y)]);ans.append(('nested_presence_and_code',p))
    # Selected actual written key determines whether one copy runs.
    p=Program(2);a=p.add(('copy',1,0));p.add(('round',0,0),-1,[(2,a)]);ans.append(('choice_changes_own_leaf',p))
    # Mandatory bit is a genuine paid operation and can dispatch addresses.
    p=Program(2);w=p.add(('round',0,1));a=p.add(('copy',0,1),w);b=p.add(('copy',1,0),w)
    p.add(('bit',1,0),a,[(1,b)]);ans.append(('native_bit_routes_copy',p))
    ans+=[('delayed_selection_n'+str(m),fork_m(m)) for m in (0,9,16)]
    return ans

def fixed_first(x):
    v=x[0]&1
    if v:
        v=(x[1]>>1)&1
        return (4 if v else 6),2
    if not x[1]&1:return 5,2
    return (4 if (x[0]>>1)&1 else 6),3

def public_formula(m):
    p=fork_m(m)
    rows=[]
    for x in product(range(10),repeat=2):
        k1,n=fixed_first(x);assert k1 not in x
        chosen=min((k for k in p.keys(1) if k!=k1),key=lambda k:p.create_price(1,k))
        copied=chosen if x[1] else k1
        v=8*n+p.create_price(1,k1)+13+p.create_price(1,chosen)+m*p.cp(copied)
        rows.append((v,x,k1,chosen,copied))
    assert max(y[0] for y in rows)==177+44*m
    return rows

def main():
    data=[];counts=0;xs=list(product(range(10),repeat=2))
    for name,p in examples():
        D=Domains(p);W=Worlds(p);g=D.value()
        assert W.value()==g
        h=Counter();pw=Counter();term=Counter();worst=[];sample=[]
        for x in xs:
            F=Domains(p,actual=x);v=F.value()
            assert v==W.value(x)==F.replay(x)[0]
            z,tr,_=D.replay(x);assert z<=g;h[z]+=1;pw[v]+=1;counts+=1
            term[tr[-1][0] if tr else -1]+=1
            if z==g:worst.append(x)
            if x in ((0,0),(5,6),(6,5)):sample.append({'initial':x,'point':v,'uniform_run':z,'uniform_trace':tr})
        assert worst
        data.append(dict(name=name,program=p.nodes,uniform=g,point_histogram=sorted(pw.items()),uniform_histogram=sorted(h.items()),terminal_pc_histogram=sorted(term.items()),worst_witness=worst[0],selected_traces=sample))
        if name=='choice_changes_own_leaf':assert W.value((0,0))==82
        if name.startswith('delayed_selection_n'):
            m=int(name.split('_n')[-1]);assert g==177+44*m
            assert max(t[0] for t in public_formula(m))==g
    # Physically attainable common seed: slot0=0, slot1 in {0,1}.
    # Both independent models verify every m up through the strict transition and beyond.
    selective=[]
    for m in range(18):
        p=fork_m(m);D=Domains(p,(1,3));W=Worlds(p,(1,3));blind=Domains(p,(1,3),forbid_preprobes=[len(p.nodes)-1])
        g=D.value();base=153+43*m
        assert W.value()==g==base+min(m,8) and blind.value()==base+m
        assert max(D.replay((0,j))[0] for j in (0,1))==g
        assert all(W.value((0,j))==Domains(p,(1,3),(0,j)).value()==base for j in (0,1))
        act=D.dp(*D.start)[1]
        assert act[0]==('read' if m>8 else 'round')
        selective.append(dict(m=m,point_each=base,uniform=g,uniform_no_preprobe=blind.value(),first_action=act,
                              costs_by_visible_guard=[D.replay((0,j))[0] for j in (0,1)],initial_receipt_cost=37))
    rt=dict(status='PASS',scope='Finite original-word cost control, distinct from separate physical runs. Unrestricted s=2: independent original positive codes 1..9 or empty 0. Conditional seed: paid 37 physically, excluded from body rows.',
            unseeded_programs=data,pointwise_comparisons=counts,uniform_comparisons=len(data),
            full_input_uniform_closed_form='177+44m, all integer m>=0, same policy; see notes for proof',conditional_cases=selective,
            conditional_closed_form='153+43m+min(m,8); pointwise 153+43m; forbidding advance queries 153+44m')
    return rt
if __name__=='__main__':
    q=argparse.ArgumentParser();q.add_argument('--out','--output',dest='out',type=Path,default=Path(__file__).with_name('oracle_results.json'));a=q.parse_args()
    z=main();a.out.write_text(json.dumps(z,indent=2,sort_keys=True)+'\n')
    print('PASS',z['pointwise_comparisons'],[v['uniform'] for v in z['unseeded_programs']],len(z['conditional_cases']))
