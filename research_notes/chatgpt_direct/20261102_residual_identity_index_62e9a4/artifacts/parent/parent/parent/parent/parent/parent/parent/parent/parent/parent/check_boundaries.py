"""Focused source/table coupling counterexamples and omission histories."""
from pathlib import Path
import argparse,json
import check_multitarget as c
p,m,e,r=c.p,c.m,c.e,c.r

def boundaries():
    C=c.Compiler(slots=2);traces={}
    # Same local color, different targets: must compare full typed identity.
    table=((0,None,0),((0,0),(2,0)));J=C.encode(table)
    K,_,log=C.run(J,('same',0,1),True);tab,value=C.decode(K)
    c.ck(not value and tab==table,'Target tag distinguishes equal local color')
    traces['equal_colors_distinct_targets']=dict(initial=J,end=K,trace=log)
    # A raw source change bypassing the compiled API leaves table evidence stale.
    table=((None,0,None),((1,0),None));J=C.encode(table)
    raw,_,_=e.step(J,p.one(1),C.H)
    bad,_,log=C.run(raw,('valid',0),True)
    c.ck(p.read(bad,C.out)==1 and not any(h in bad for h in C.targets),'Raw bypass leaves a stale valid record')
    safe,_,log2=C.run(J,('release',1),True)
    good,_,_=C.run(safe,('valid',0))
    goodtab,val=C.decode(good)
    c.ck(not val and goodtab==((None,None,None),((1,0),None)),'Compiled release updates whichever source event contains the member')
    traces['raw_bypass_vs_compiled_release']=dict(initial=J,bypassed_raw=raw,bad_end=bad,safe_end=good,bad_trace=log,safe_release_trace=log2)
    # A missed actual permission blocker can allocate a phantom current record.
    table=((0,None,None),(None,None));J=C.encode(table);word=C.programs[('reserve',1)]
    busy=tuple(sorted((C.current[1].ports[0],*C.block)))
    pos=word.index(p.add(busy));bad,_,log=C.runword(J,word,True,(pos,))
    c.ck(C.current[1].cell(0) in bad and C.targets[1] not in bad and C.targets[0] in bad,'One missed blocker breaks exact source/table invariant')
    traces['missed_creation_permission']=dict(initial=J,omitted_position=pos+1,end=bad,trace=log)
    # Domain closure matters: undeclared external source writer can block raw add.
    C2=c.Compiler(slots=2);foreign=(1,901,902);C2.H=frozenset(set(C2.H)|{foreign})
    J=m.canon((foreign,));bad,_,log=C2.run(J,('reserve',0),True)
    c.ck(C2.current[0].cell(0) in bad and C2.targets[0] not in bad,'External source event violates declared source/table preparation')
    traces['foreign_source_relation']=dict(initial=J,end=bad,trace=log)
    # Invalid execute restores logical source but actually recreates both events.
    table=((0,None,0),((1,0),None));J=C.encode(table)
    state=c.ref.old.seed(J);initialnames=state.names();word=C.programs[('execute',0)];freshlog=[]
    for i,rawop in enumerate(word):
        state,ok,delta=c.ref.old.raw_step(state,rawop,C.H)
        if any(h in C.targets for h,_ in tuple(delta['created'])+tuple(delta['retired'])):
            freshlog.append(dict(position=i+1,command=rawop,**delta))
    tab,bit=C.decode(state.matching)
    c.ck(tab==table and not bit,'Invalid execute preserves full logical table and physical source matching')
    c.ck(all(state.names()[h]!=initialnames[h] for h in (C.targets[0],C.targets[2])),'Raw source creation names refreshed under clear/rebuild')
    traces['physical_births']=dict(length=len(word),before={str(h):initialnames[h] for h in C.targets if h in initialnames},after={str(h):state.names()[h] for h in C.targets if h in state.names()},events=freshlog)
    # A true frame, disjoint from source and every table/work member, is retained.
    frame=(1001,1002,1003);C.H=frozenset(set(C.H)|{frame});J=m.canon(C.encode(table)+(frame,))
    K,_,_=C.run(J,('execute',0));c.ck(frame in K,'Disjoint frame retained')
    c.ck(m.canon(h for h in K if h!=frame)==C.encode(table,0),'Frame does not change protected observation')
    return dict(mode='boundaries',checks=c.CHECKS,kernel_calls=C.calls+C2.calls,command_uses=C.uses+C2.uses,
                direct_raw_calls=1,annotated_physical_calls=len(word),traces=traces)

def omissions():
    C=c.Compiler(slots=1)
    ops=(('reserve',0),('bind',0,0),('release',1),('reserve',1),('valid',0),('execute',0),('bind',0,1),('execute',0))
    word=tuple(raw for op in ops for raw in C.programs[op]);J=C.encode(((None,)*3,(None,)))
    target,_,_=C.runword(J,word);C.decode(target);rows=[]
    for f in (1,2):
        protected=tuple(raw for raw in word for _ in range(f+1));d={(J,0):e.prep(J)}
        for raw in protected:
            nd={}
            for (S,k),mass in d.items():
                C.uses+=1;T,_=C._raw(S,raw)
                q=(T,k);nd[q]=r.merge(nd.get(q,c.ZERO),r.serial(mass,c.ONE))
                if k<f:
                    q=(S,k+1);nd[q]=r.merge(nd.get(q,c.ZERO),r.serial(mass,c.ONE))
            d=nd
        totals={}
        for (S,k),mass in d.items():
            c.ck(S==target,'All protected joint source/reference omission branches have exact endpoint')
            totals[k]=r.merge(totals.get(k,c.ZERO),mass)
        # Independent position-only CWM recurrence, without model-state choices.
        positions={0:c.ONE}
        for _ in protected:
            nd={}
            for k,mass in positions.items():
                nd[k]=r.merge(nd.get(k,c.ZERO),r.serial(mass,c.ONE))
                if k<f:nd[k+1]=r.merge(nd.get(k+1,c.ZERO),r.serial(mass,c.ONE))
            positions=nd
        c.ck(positions==totals,'Source-aware histories preserve every omission position weight')
        rows.append(dict(budget=f,base_commands=len(word),protected_commands=len(protected),histories={str(k):e.cw(v) for k,v in totals.items()}))
    return dict(mode='omissions',ops=ops,rows=rows,checks=c.CHECKS,**C.stats())

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=('boundaries','omissions'));ap.add_argument('--out',required=True);a=ap.parse_args()
    result=boundaries() if a.mode=='boundaries' else omissions()
    Path(a.out).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(a.mode,{k:v for k,v in result.items() if k in ('checks','kernel_calls','command_uses','rows','annotated_physical_calls')})
