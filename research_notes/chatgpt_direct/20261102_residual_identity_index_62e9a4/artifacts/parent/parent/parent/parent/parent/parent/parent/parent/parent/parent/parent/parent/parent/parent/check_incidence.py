"""Restoring incidence queries using the unchanged inherited triadic/CWM kernel.

All runtime commands are compiled independently of the source matching. Python
truth values below are only test expectations. No source incidence oracle is
used by the emitted reserve/release words.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from itertools import combinations, product
from functools import lru_cache
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_domain_guard as g
p,m,e,r,f=g.p,g.m,g.e,g.r,g.f
ONE,ZERO=g.ONE,g.ZERO
reader=g.reader
write=g.old.all_occupied_write
CHECKS=0

def ck(ok:bool,label:str):
    global CHECKS
    CHECKS+=1
    if not ok:raise AssertionError(label)

def emit_read(v,o,z):
    H,W,_=reader(v,o,z)
    return H,W+[p.one(o+1)]

def lit_pair(pre,post,u,v):
    # Before occupied / after vacant for each of two co-members.
    return (pre[u]+3,post[u]+4,pre[v]+3,post[v]+4)

def edge_test(U,a,edge,base=1000):
    U=tuple(sorted(U));edge=tuple(sorted(edge))
    if len(edge)!=3 or not set(edge)<=set(U) or a not in edge:
        raise ValueError('Target is a triple inside U containing the pivot')
    others=tuple(v for v in U if v!=a)
    pre={v:base+6*i for i,v in enumerate(others)}
    post={v:base+6*len(others)+6*i for i,v in enumerate(others)}
    out=base+12*len(others);work=out+7
    if set(U)&set(range(base+1,work+1)):raise ValueError('Private storage intersects source')
    H=set(combinations(U,3))|p.library(out);W=[];stages=[]
    for v in others:
        h,w=emit_read(v,pre[v],work);H|=h;W+=w
    stages.append(dict(name='before',end=len(W)))
    W.append(p.one(a));stages.append(dict(name='released',end=len(W)))
    for v in others:
        h,w=emit_read(v,post[v],work);H|=h;W+=w
    stages.append(dict(name='after',end=len(W)))
    u,v=tuple(x for x in edge if x!=a)
    h,w=write(lit_pair(pre,post,u,v),p.reg(out,1)[1],work);H|=h;W+=w
    W += [p.add(p.reg(out,0)[1]),p.add(p.reg(out,0)[0]),p.add(p.reg(out,1)[0])]
    stages.append(dict(name='verdict',end=len(W)))
    for u,v in combinations(others,2):
        h,w=write(lit_pair(pre,post,u,v),tuple(sorted((a,u,v))),work);H|=h;W+=w
    stages.append(dict(name='source_restored',end=len(W)))
    W += [p.one(o+5) for o in tuple(pre.values())+tuple(post.values())]
    stages.append(dict(name='clean',end=len(W)))
    return dict(H=H,word=W,stages=stages,U=U,pivot=a,edge=edge,pre=pre,post=post,
                status=out,work=work)

def pool_test(U,V,base=1000):
    """Certify: the only events touching a six-member pool are one internal triple.

Four fixed pivots hit every triple in the pool. Every source intervention is
restored before the next pivot. Previous samples are of the same restored J.
"""
    U=tuple(sorted(U));V=tuple(sorted(V))
    if len(V)!=6 or not set(V)<=set(U):raise ValueError('V must be six members in U')
    pre={v:base+6*i for i,v in enumerate(U)}
    post_slots=tuple(base+6*len(U)+6*i for i in range(len(U)-1))
    out=base+6*len(U)+6*(len(U)-1);work=out+7
    if set(U)&set(range(base+1,work+1)):raise ValueError('Private storage intersects source')
    H=set(combinations(U,3))|p.library(out);W=[];stages=[]
    for v in U:
        h,w=emit_read(v,pre[v],work);H|=h;W+=w
    stages.append(dict(name='before',end=len(W)))
    for a in V[:4]:
        others=tuple(v for v in U if v!=a);post=dict(zip(others,post_slots))
        W.append(p.one(a))
        for v in others:
            h,w=emit_read(v,post[v],work);H|=h;W+=w
        for u,v in combinations((x for x in V if x!=a),2):
            T={a,u,v}
            ports=lit_pair(pre,post,u,v)+tuple(pre[x]+4 for x in V if x not in T)
            h,w=write(ports,p.reg(out,1)[1],work);H|=h;W+=w
        for u,v in combinations(others,2):
            h,w=write(lit_pair(pre,post,u,v),tuple(sorted((a,u,v))),work);H|=h;W+=w
        W += [p.one(o+5) for o in post_slots]
        stages.append(dict(name=f'pivot_{a}_restored',end=len(W)))
    W += [p.add(p.reg(out,0)[1]),p.add(p.reg(out,0)[0]),p.add(p.reg(out,1)[0])]
    W += [p.one(o+5) for o in pre.values()]
    stages.append(dict(name='clean',end=len(W)))
    return dict(H=H,word=W,stages=stages,U=U,V=V,pivots=V[:4],pre=pre,status=out,work=work)

def is_pool(J,V):
    touched=[h for h in J if set(h)&set(V)]
    return len(touched)==1 and set(touched[0])<=set(V)

@lru_cache(None)
def catalog(U):
    _,d=e.catalog(tuple(combinations(U,3)))
    return tuple(sorted(d))

def info(C):
    return dict(commands=len(C['word']),members=len(set().union(*C['H'])),
                candidate_events=len(C['H']),status_offset=C['status'],stages=C['stages'])

def run_case(C,J,truth,keep=False):
    z=f.execute(J,C['word'],C['H'],keep=keep)
    ck(z['end']==m.canon(J+p.reg(C['status'],int(truth))),
       'entire source restored; correct complete status; private work empty')
    return z

def edge_cases(n,start,stop):
    U=tuple(range(1,n+1));D=catalog(U);C=edge_test(U,1,(1,2,3));mass=ZERO
    rows=[]
    for index in range(start,min(stop,len(D))):
        J=D[index];run_case(C,J,(1,2,3) in J)
        mass=r.merge(mass,e.prep(J));rows.append(dict(index=index,source=J,expected=int((1,2,3) in J)))
        f.raw_step.cache_clear()
    return dict(domain_size=len(D),cases=len(rows),rows=rows,CWM=e.cw(mass),**info(C))

def pool_cases(n,start,stop):
    U=tuple(range(1,n+1));V=U[:6];D=catalog(U);C=pool_test(U,V);mass=ZERO;rows=[]
    for index in range(start,min(stop,len(D))):
        J=D[index];good=is_pool(J,V);run_case(C,J,good)
        mass=r.merge(mass,e.prep(J));rows.append(dict(index=index,source=J,expected=int(good)))
        f.raw_step.cache_clear()
    return dict(domain_size=len(D),cases=len(rows),rows=rows,CWM=e.cw(mass),**info(C))

def guarded_decoder():
    """Add an exact-incidence prepass to the parent's 741-call domain guard.

The source may cross V into six named external members, all inside U. Source
registers 1..36 and every private work member remain separate from this U.
"""
    V=tuple(range(49,55));U=V+tuple(range(201,207))
    C=pool_test(U,V,base=1000);P=g.build();status=C['status']
    # A complete predicate register has both ports occupied. Open it before
    # using its +3 as the positive tail signal; preserve a private copy? Not
    # needed: we clean it only after the parent's entire guarded operation.
    W=C['word']+[p.one(status+1)];H=C['H']|P['H'];prefix=len(W)
    cut=next(x['end'] for x in P['stages'] if x['name']=='signed_occupancy_snapshot')
    end=next(x['end'] for x in P['stages'] if x['name']=='domain_certified')
    W+=P['word'][:cut]
    for b in P['guards']:
        h,w=write(tuple(b['support'])+(status+3,),P['valid'],P['work']);H|=h;W+=w
    W+=P['word'][end:]+[p.one(status+5)]
    return dict(H=H,word=W,status=P['status'],outputs=P['outputs'],inputs=P['inputs'],
                source_universe=U,V=V,pool=C,parent=P,prefix=prefix,
                stages=[dict(name='clean',end=len(W))])

def integrations(first,last):
    C=guarded_decoder();P=C['parent'];out=[];mass=ZERO
    for row in P['rows'][first:last]:
        T=row['residue'];side=g.j.init(row['sorted'],P['inputs'])
        original=m.canon(side+(T,))
        # Same V occupancy, three different crossing source events.
        crossing=tuple(tuple(sorted((v,201+2*i,202+2*i))) for i,v in enumerate(T))
        spoof=m.canon(side+crossing)
        a=f.execute(original,C['word'],C['H'])['end']
        ck(a==m.canon(original+p.reg(P['status'],1)+g.j.init(row['bits'],P['outputs'])),
           'valid code accepted and actual data copied; exact source restored')
        f.raw_step.cache_clear()
        b=f.execute(spoof,C['word'],C['H'])['end']
        ck(b==m.canon(spoof+p.reg(P['status'],0)),
           'same occupancy cross-boundary counterfeit rejected with all source edges preserved')
        f.raw_step.cache_clear()
        # Execute parent on the actual spoof, not just infer its old failure.
        c=f.execute(spoof,P['word'],P['H']|set(crossing))['end']
        ck(p.read(c,P['status'])==1,'parent occupancy guard actually accepts the spoof')
        f.raw_step.cache_clear()
        out.append(dict(bits=row['bits'],residue=T,crossing=crossing,new_valid_accept=True,
                        old_spoof_accept=True,new_spoof_accept=False))
        mass=r.merge(mass,e.prep(original));mass=r.merge(mass,e.prep(spoof))
    return dict(rows=out,cases=len(out)*2,CWM=e.cw(mass),**info(C))

def boundaries():
    rows=[];U=tuple(range(1,7));C=edge_test(U,1,(1,2,3))
    J=m.canon(((1,2,3),(4,5,6)));K=m.canon(((1,2,4),(3,5,6)))
    A=run_case(C,J,True,True);B=run_case(C,K,False,True)
    ck(m.used(J)==m.used(K),'equal entire occupancy, different incidence')
    rows.append(dict(name='same_occupancy_different_incidence',true_run=A,false_run=B))
    # Missing BEFORE: after-free alone would identify every candidate in an
    # empty source as matching. The actual complete word rejects and restores.
    rows.append(dict(name='preexisting_vacancy',run=run_case(C,(),False,True)))
    # Incomplete external universe: source event reaches an unlisted member.
    outside=m.canon(((1,2,99),));H=C['H']|set(outside)
    z=f.execute(outside,C['word'],H,keep=True)
    ck(z['end']!=m.canon(outside+p.reg(C['status'],0)),
       'unknown outside endpoint prevents restoration; finite support bound is essential')
    rows.append(dict(name='unlisted_endpoint',run=z))
    # Dynamic interference between release and post-sample creates false causal
    # attribution. Pivot is initially free. External release of an unrelated
    # (2,3,6) makes both target co-members vanish. The new word reconstructs 123.
    I=((2,3,6),);cut=next(s['end'] for s in C['stages'] if s['name']=='released')
    mid=f.execute(I,C['word'][:cut],C['H'])['end']
    mid=f.execute(mid,[p.one(2)],C['H'])['end']
    z=f.execute(mid,C['word'][cut:],C['H'],keep=True)
    ck(p.read(z['end'],C['status'])==1,'concurrent unrelated removal can fake the release signature')
    rows.append(dict(name='external_change_during_intervention',source=I,cut=cut,run=z))
    # Primitive source erasure is necessarily real; exact endpoint restoration
    # is not preservation of historical creation identity.
    # Omit just the actual release: initially present target gets a false negative.
    omission=f.execute(J,C['word'],C['H'],omitted=(cut-1,),keep=True)
    ck(p.read(omission['end'],C['status'])==0 and tuple(h for h in omission['end'] if set(h)<=set(U))==J,
       'omitted intervention can suppress positive evidence')
    rows.append(dict(name='unprotected_intervention_omission',run=omission))
    # Honest disjoint source frame retained, including when source is empty.
    frame=(8001,8002,8003)
    Z=f.execute(m.canon(J+(frame,)),C['word'],C['H']|{frame})['end']
    ck(Z==m.canon(J+(frame,)+p.reg(C['status'],1)),'disjoint untouched frame retained')
    return dict(rows=rows,**info(C))

def tomography():
    """All 20 edge predicates reconstruct the full six-member source matching."""
    U=tuple(range(1,7));D=catalog(U);rows=[]
    for J in D:
        observed=[]
        for edge in combinations(U,3):
            C=edge_test(U,edge[0],edge);Z=run_case(C,J,edge in J)['end']
            if p.read(Z,C['status']):observed.append(edge)
            f.raw_step.cache_clear()
        ck(m.canon(observed)==J,'all candidate edge predicates recover exact source, not just support')
        rows.append(dict(source=J,reconstructed=observed))
    return dict(source_matchings=len(D),queries=len(D)*20,rows=rows)

def stats():
    return dict(assertions=CHECKS,uncached_kernel_calls=f.CALLS,transition_uses=f.USES)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('mode');ap.add_argument('--n',type=int,default=6)
    ap.add_argument('--first',type=int,default=0);ap.add_argument('--last',type=int,default=99999)
    ap.add_argument('--out',required=True);args=ap.parse_args()
    if args.mode=='edge':z=edge_cases(args.n,args.first,args.last)
    elif args.mode=='pool':z=pool_cases(args.n,args.first,args.last)
    elif args.mode=='integration':z=integrations(args.first,args.last)
    elif args.mode=='boundaries':z=boundaries()
    elif args.mode=='tomography':z=tomography()
    elif args.mode=='programs':
        cases=[edge_test(tuple(range(1,n+1)),1,(1,2,3)) for n in (6,9,12)]
        cases += [pool_test(tuple(range(1,n+1)),tuple(range(1,7))) for n in (6,9,12)]
        cases += [guarded_decoder()]
        z=dict(programs=[dict(summary=info(c),word=c['word'],candidates=sorted(c['H'])) for c in cases])
    else:raise ValueError('unknown mode')
    z['new_checks']=stats();Path(args.out).write_text(json.dumps(z,ensure_ascii=False,indent=2))
    print(json.dumps(dict(mode=args.mode,cases=z.get('cases'),**stats()),ensure_ascii=False))
if __name__=='__main__':main()
