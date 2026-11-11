"""Two separate original units with a single shared recovery probe after both actual selectors."""
import argparse,copy,json,sys
from collections import Counter
from itertools import combinations,product
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent))
from adaptive.phase.phase_kernel import F,rewrite
from adaptive.graph.feedback_graph import V,E,audit,fcol
from projected.kernel.subset_kernel import prefix,initial,emit,marker_slot,least_one,core
P=list(product(V,repeat=2));MAPS=('identity','doubling')
def enc(h):
    return ((h[0]+2*h[1])%5)//2
def first(p,e):
    j=e+6;start=p.cost
    k=p.copy(13,marker_slot(j));assert k in (0,j)
    p.drop(13)
    delivered=emit(p,[11 if k==j else j])[0]['bind_delivered']
    return dict(code=delivered,paid=p.cost-start,observed_copy=k)
def second(e,h):
    return audit(e,h)[1]
def alternatives(message,kind,edges,firsts):
    M=F[kind]
    w=[h for h in P if enc(h)==message and all(audit(e,M[v])[0]==k for v,e,k in zip(h,edges,firsts))]
    return sorted(set(tuple(second(e,M[v]) for v,e in zip(h,edges))for h in w))
def recover(message,kind,edges,firsts,probe):
    outs=alternatives(message,kind,edges,firsts);assert 1<=len(outs)<=2
    if len(outs)==1:return outs[0],outs,[]
    # Outputs differ in an inside-edge component. Its requested vertex marker tests exactly those two alternatives.
    g=next(i for i in (0,1) if outs[0][i]!=outs[1][i])
    assert firsts[g]==11
    j=E[edges[g]][0]+1;ans=probe(g,j)
    k=11 if ans else j;remaining=[x for x in outs if x[g]==k]
    assert len(remaining)==1
    return remaining[0],outs,[(g,j,ans)]

def geometry():
    joint_conflict=0;four_edges=0;rectangle_checks=0
    for a,b in combinations(P,2):
        assert any(all(audit(e,F[name][av])[0]==audit(e,F[name][bv])[0] for e,av,bv in zip(eds,a,b)) and
                   tuple(audit(e,F[name][av])[1] for e,av in zip(eds,a))!=tuple(audit(e,F[name][bv])[1]for e,bv in zip(eds,b))
                   for name in MAPS for eds in P);joint_conflict+=1
    for name in MAPS:
        M=F[name]
        for e1,e2 in P:
            rect=[h for h in P if M[h[0]] in E[e1] and M[h[1]] in E[e2]]
            assert len(rect)==len({(h[0]+2*h[1])%5 for h in rect})==4
            rectangle_checks+=1
            msg_count=Counter(enc(h)for h in rect);assert max(msg_count.values())<=2
            four_edges+=int(name=='identity')
    assert four_edges==25 and (2*four_edges)%4!=0
    return dict(conflicting_unordered_world_pairs=joint_conflict,both_inside_rectangles=rectangle_checks,
                id_squares=four_edges,vertex_degree_in_squares=4,required_twocolor_incidences=50)

def run():
    C=core.prior.Compiler(slots=15);geom=geometry()
    rows=[];representatives={};query_hist=Counter();fee_hist=Counter();preps=0;writers=0
    for h in P:
        base=[prefix(C,initial(v),route=fcol)for v in h]
        actual=tuple(sum(int(q.events[i]['present'])<<i for i in range(3))for q in base);msg=enc(actual);preps+=2
        assert all(q.cost==2346 for q in base);assert h==actual
        for q in base:q.events=[]
        for name in MAPS:
            units=base if name==MAPS[-1] else [copy.deepcopy(p,{id(C):C})for p in base]
            for q in units:
                w=rewrite(q,F[name]);assert w['cost']==1222;q.events=[];writers+=1
            for eds in P:
                ps=units if eds==P[-1] else [copy.deepcopy(p,{id(C):C})for p in units]
                fresh=[p.cost for p in ps];banks=[p.codes()for p in ps]
                assert fresh==[3568,3568]
                firsts=[first(p,e)for p,e in zip(ps,eds)]
                def probe(g,j):return ps[g].probe(marker_slot(j),least_one(j))
                K,outs,tr=recover(msg,name,eds,tuple(i['code']for i in firsts),probe)
                seconds=[emit(p,[k])[0]for p,k in zip(ps,K)]
                actual_second=tuple(j['bind_delivered']for j in seconds)
                assert actual_second==tuple(audit(e,F[name][i])[1]for i,e in zip(h,eds))
                assert all((fr['code'],se['bind_delivered'])==audit(e,F[name][i])for i,e,fr,se in zip(h,eds,firsts,seconds))
                assert banks==[p.codes() for p in ps]
                delta=sum(p.cost for p in ps)-sum(fresh)
                assert delta==sum(a['paid']for a in firsts)+8*len(tr)+sum(sum(j['words']) for j in seconds)
                total=sum(p.cost for p in ps)
                tag=(name,len(outs),tuple(i['code']==11 for i in firsts))
                if tag not in representatives:representatives[tag]=dict(h=h,map=name,menu=eds,message=msg,firsts=firsts,
                    possible_seconds=outs,real_probe=tr,real_seconds=seconds,total=total)
                rows.append([*h,name,*eds,msg,*[i['code']for i in firsts],*actual_second,*([*tr[0]]if tr else [-1,-1,-1]),total])
                query_hist[name,len(tr)]+=1;fee_hist[total]+=1
    assert preps==50 and writers==100 and len(rows)==1250
    return dict(status='PASS',physical_prefixes=preps,physical_intervening_writers=writers,paired_programs=len(rows),
        actual_first_deliveries=2*len(rows),actual_second_deliveries=2*len(rows),supplementary_queries=sum(k*n for (_,k),n in query_hist.items()),
        query_histogram=[dict(map=n,reads=k,paths=v)for (n,k),v in sorted(query_hist.items())],
        min_total=min(fee_hist),max_total=max(fee_hist),joint_preparation_and_writers=7136,geometry=geom,
        required_messages_for_query_budget={'0':25,'1':3,'2':1},
        row_columns=['old1','old2','writer_map','menu1','menu2','message','first1','first2','second1','second2','read_component','read_key','read_answer','charged_total'],
        rows=rows,representatives=list(representatives.values()),
        scope='Each original immutable prepared pair reused for the two writer maps. Each post-update matching forked across 25 future menu pairs; private mutable tables are independent. Count 1250 actual pairs of suffix executions, not 1250 costly independent re-preparations. Paid queries are shared recovery only, beyond both mandatory prefix and business paths.')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=HERE/'joint_repair_results.json');a=p.parse_args()
    d=run();a.out.write_text(json.dumps(d,indent=1,sort_keys=True)+'\n');print('PASS',d['paired_programs'],d['physical_intervening_writers'],d['query_histogram'],d['min_total'],d['max_total'])
