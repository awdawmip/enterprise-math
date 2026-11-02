"""Scope-indexed conditional execution over the unchanged triadic BRC kernel.

The public API fixes the allowed target set and a compiled release transversal.
Neither the production word nor its runner decodes a request or chooses a target
at runtime. Logical results are observed at full macro boundaries. Source birth
preservation is checked separately, for the primitive occurrence annotation.
"""
from __future__ import annotations
from itertools import combinations, product
from pathlib import Path
import argparse, json, sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_multitarget as base
p,m,e,r=base.p,base.m,base.e,base.r
ONE,ZERO=base.ONE,base.ZERO
CHECKS=0

def ck(ok,label):
    global CHECKS
    CHECKS+=1
    if not ok: raise AssertionError(label)

def powerset(values, nonempty=False):
    values=tuple(values)
    for size in range(1 if nonempty else 0,len(values)+1):
        yield from combinations(values,size)

def minimal_transversals(H,S):
    """Finite symbolic compilation; no execution-state queries occur here."""
    U=tuple(sorted(set().union(*(set(H[t]) for t in S))))
    out=[]
    for R in powerset(U,True):
        if all(set(R)&set(H[t]) for t in S) and not any(set(Q)<=set(R) for Q in out):out.append(R)
    return tuple(out)

def default_specs(H):
    return tuple((S,R) for S in powerset(range(len(H)),True) for R in minimal_transversals(H,S))

class Compiler(base.Compiler):
    def __init__(self,H=base.H_DEFAULT,slots=2,specs=None):
        H=tuple(sorted(tuple(sorted(h)) for h in H))
        self.scopes=default_specs(H) if specs is None else tuple((tuple(S),tuple(R)) for S,R in specs)
        U=set().union(*(set(h) for h in H))
        for S,R in self.scopes:
            if (not S or len(set(S))!=len(S) or not set(S)<=set(range(len(H)))
                    or not R or len(set(R))!=len(R) or not set(R)<=U
                    or not all(set(R)&set(H[t]) for t in S)):
                raise ValueError('A nonempty public scope and a release transversal are required')
        super().__init__(H,slots)
    def alphabet(self):
        return super().alphabet()+tuple(('execute_scope',i,S,R) for S,R in self.scopes for i in range(self.slots))
    def _compile(self,op):
        if op[0]!='execute_scope':return super()._compile(op)
        _,i,S,R=op
        w=self.clearout()
        for index,t in enumerate(S):
            if index:w+=self.clearout()
            w+=self.emit_local_equal(t,i)+[p.one(self.out+1)]
            w+=self.emit_write((self.out+3,),self.success)
            for c in range(self.colors):
                w+=self.emit_write((self.current[t].ports[c],self.out+4),self.back.cell(c))
            w+=[p.one(self.current[t].anchor)]
            for c in range(self.colors):w+=self.emit_write((self.back.ports[c],),self.current[t].cell(c))
            w+=[p.one(self.back.anchor)]
        # Only original source events incident with R can have been destroyed.
        w += [p.one(a) for a in R]
        for t,h in enumerate(self.targets):
            if set(h)&set(R):w+=self.emit_write((self.current[t].anchor,),h)
        w+=self.clearout()+self.emit_read(self.success[0])+[p.one(self.success[1])]
        return w

def expected(C,tab,op):
    if op[0]!='execute_scope':return base.expected(C,tab,op)
    _,i,S,_=op;q=tab[1][i]
    if q is not None and q[0] in S:return base.expected(C,tab,('execute',i))
    return tab,False

def expected_length(C,S,R):
    N=[t for t,h in enumerate(C.targets) if set(R)&set(h)]
    return len(S)*(11*C.colors+15)+len(R)+3*len(N)+9

def selected_specs():
    return (((0,),(2,)),((1,),(1,)),((1,),(4,)),((2,),(6,)),((0,1,2),(1,4)))

def audit(slots=2,canonical=False,start=0,stop=None,all_scopes=False):
    C=Compiler(slots=slots,specs=None if all_scopes else selected_specs())
    dom=base.domain(C,canonical);stop=len(dom) if stop is None else min(stop,len(dom))
    ops=tuple(op for op in C.programs if op[0]=='execute_scope')
    count=0;mass=ZERO
    for ix in range(start,stop):
        tab=dom[ix];J=C.encode(tab,None if ix%3==0 else ix%2)
        for op in ops:
            word=C.programs[op]
            ck(len(word)==expected_length(C,op[2],op[3]),'Length identity')
            K,_,_=C.runword(J,word);got=C.decode(K)
            ck(got==expected(C,tab,op),'Exact full source/table/result contract')
            # The raw release footprint is statically inspectable, not a decoder.
            # Parent release tuple syntax is checked via p.one, rather than presumed.
            src_release={a for a in C.U if p.one(a) in word}
            ck(src_release==set(op[3]),'Exactly the declared source releases')
            count+=1;mass=r.merge(mass,ONE)
    return dict(mode='audit',slots=slots,canonical=canonical,all_scopes=all_scopes,
                domain=len(dom),start=start,stop=stop,scopes=C.scopes,transitions=count,
                CWM=e.cw(mass),checks=CHECKS,kernel_calls=C.calls,command_uses=C.uses,
                inherited_assertions=base.CHECKS,members=C.members,candidates=len(C.H))

def run_named(C,J,word,keep=False):
    state=base.ref.old.seed(J);initial=state.names();log=[];source_births=[];visited=[]
    for pos,raw in enumerate(word,1):
        state,ok,delta=base.ref.old.raw_step(state,raw,C.H)
        moved=[(h,n) for h,n in tuple(delta['created'])+tuple(delta['retired']) if h in C.targets]
        if moved:source_births.append(dict(position=pos,command=raw,created=[x for x in delta['created'] if x[0] in C.targets],retired=[x for x in delta['retired'] if x[0] in C.targets]))
        if keep:log.append(dict(position=pos,command=raw,success=ok,matching=state.matching))
        visited.append(state.names())
    return state,initial,source_births,visited,log

def births():
    C=Compiler(slots=1,specs=selected_specs());dom=base.domain(C)
    pairs=0;stats=[]
    for tab in dom:
        J=C.encode(tab)
        for S,R in C.scopes:
            op=('execute_scope',0,S,R);word=C.programs[op]
            state,initial,events,visited,_=run_named(C,J,word)
            ck(C.decode(state.matching)==expected(C,tab,op),'Named endpoint equals logical reducer')
            for h in base.source(C,tab[0]):
                retired=any(h==tuple(q[0]) for ev in events for q in ev['retired'])
                ck(retired==bool(set(h)&set(R)),'Initial source occurrence retired iff hit by R')
                if not set(h)&set(R):
                    ck(all(v.get(h)==initial[h] for v in visited),'Unhit birth is preserved at every primitive prefix')
            pairs+=1
    # Fully explicit stale request: A and C present; request points to missing B.
    C6=Compiler(slots=6,specs=selected_specs())
    table=((0,None,0),((1,0),None,None,None,None,None));J=C6.encode(table)
    for tag,op in (('old_global',('execute',0)),('new_global',('execute_scope',0,(0,1,2),(1,4))),
                   ('scope_A',('execute_scope',0,(0,),(2,))),
                   ('scope_B_via_1',('execute_scope',0,(1,),(1,))),
                   ('scope_B_via_4',('execute_scope',0,(1,),(4,))),
                   ('scope_C',('execute_scope',0,(2,),(6,)))):
        state,initial,events,visited,log=run_named(C6,J,C6.programs[op],True)
        ck(C6.decode(state.matching)==(table,False),'All stale-request cases logically agree')
        before={str(h):initial[h] for h in base.source(C6,table[0])}
        after={str(h):state.names()[h] for h in base.source(C6,table[0])}
        stats.append(dict(case=tag,op=op,length=len(C6.programs[op]),before=before,after=after,source_events=events,trace=log))
    return dict(mode='births',full_tables=len(dom),pairs=pairs,examples=stats,checks=CHECKS,
                annotated_kernel_calls=base.ref.old.KERNEL_CALLS,kernel_calls=C.calls+C6.calls,
                command_uses=C.uses+C6.uses,inherited_assertions=base.CHECKS)

def finite_footprints():
    H=base.H_DEFAULT;C=Compiler(slots=1);_,cat=e.catalog(H)
    rows=[]
    for S in powerset(range(len(H)),True):
        all_R=[R for R in powerset(C.U) if all(set(R)&set(H[t]) for t in S)]
        for F in powerset(range(len(H))):
            union=set().union(*(set(H[t]) for t in F)) if F else set()
            condition=all(set(H[t])-union for t in S)
            feasible=[R for R in all_R if not set(R)&union]
            ck(bool(feasible)==bool(condition),'Exact protected-family feasibility')
        for R in minimal_transversals(H,S):
            N=tuple(t for t,h in enumerate(H) if set(R)&set(h))
            # Every source matching is obtained from the original BRC catalog.
            maximum=max(sum(bool(set(h)&set(R)) for h in J) for J in cat)
            rows.append(dict(scope=S,releases=R,disturbance_family=N,max_initial_events_touched=maximum))
    # For B, preserving both disjoint A and C is impossible; either one is possible.
    B=(1,);protect={*H[0],*H[2]}
    ck(not any(not set(R)&protect for R in minimal_transversals(H,B)),'No B execute can preserve both A and C in fixed-word language')
    return dict(mode='footprints',source_matchings=len(cat),rows=rows,checks=CHECKS,
                scopes=len(tuple(powerset(range(3),True))),minimal_transversals=len(rows),kernel_calls=0)

def histories(depth=5):
    C=Compiler(slots=1,specs=selected_specs())
    ops=(('reserve',0),('reserve',1),('reserve',2),('bind',0,0),('bind',0,1),('bind',0,2),
         ('execute_scope',0,(0,),(2,)),('execute_scope',0,(1,),(1,)),('execute_scope',0,(2,),(6,)))
    tab=((None,)*3,(None,));J=C.encode(tab);D={(J,()):ONE};layers=[]
    for k in range(depth):
        nxt={}
        for (J,history),mass in D.items():
            table=tab if k==0 else C.decode(J)[0]
            for op in ops:
                K,_,_=C.run(J,op);got=C.decode(K)
                ck(got==expected(C,table,op),'History contract')
                key=(K,history+(got[1],));nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
        D=nxt;total=ZERO
        for weight in D.values():total=r.merge(total,weight)
        ck(total.count==len(ops)**(k+1),'All declared histories retained')
        layers.append(dict(depth=k+1,classes=len(D),CWM=e.cw(total)))
    return dict(mode='histories',ops=ops,layers=layers,checks=CHECKS,kernel_calls=C.calls,command_uses=C.uses,
                inherited_assertions=base.CHECKS)

def omissions():
    C=Compiler(slots=1,specs=selected_specs());rows=[]
    cases=[('valid_A',((0,None,0),((0,0),)),('execute_scope',0,(0,),(2,))),
           ('stale_B',((0,None,0),((1,0),)),('execute_scope',0,(1,),(1,)))]
    for name,tab,op in cases:
        J=C.encode(tab);baseword=C.programs[op];wanted,_,_=C.run(J,op)
        for f in (1,2):
            word=tuple(raw for raw in baseword for _ in range(f+1));D={(J,0):e.prep(J)}
            for raw in word:
                nxt={}
                for (S,k),mass in D.items():
                    C.uses+=1;T,_=C._raw(S,raw);key=(T,k)
                    nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
                    if k<f:
                        key=(S,k+1);nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
                D=nxt
            totals={}
            for (S,k),mass in D.items():
                ck(S==wanted,'Protected exact endpoint')
                totals[k]=r.merge(totals.get(k,ZERO),mass)
            positions={0:ONE}
            for _ in word:
                nxt={}
                for k,mass in positions.items():
                    nxt[k]=r.merge(nxt.get(k,ZERO),r.serial(mass,ONE))
                    if k<f:nxt[k+1]=r.merge(nxt.get(k+1,ZERO),r.serial(mass,ONE))
                positions=nxt
            ck(positions==totals,'Independent position CWM agrees')
            rows.append(dict(case=name,budget=f,length=len(word),base_length=len(baseword),histories={str(k):e.cw(v) for k,v in totals.items()}))
    return dict(mode='omissions',rows=rows,checks=CHECKS,kernel_calls=C.calls,command_uses=C.uses)

def failures():
    C=Compiler(slots=2,specs=selected_specs());tab=((0,None,0),((0,0),None));J=C.encode(tab);op=('execute_scope',0,(0,),(2,));word=C.programs[op]
    # Removing a required target hit leaves an invalid physical source/current table pair.
    ix=word.index(p.one(2));K,_,log=C.runword(J,word,True,(ix,))
    ck(C.targets[0] in K and not any(C.current[0].cell(c) in K for c in range(C.colors)),'Missing source release leaves a deleted target physically present')
    # A real late outside release breaks the full boundary invariant.
    safe,_,_=C.run(J,op);late,_,_=e.step(safe,p.one(4),C.H)
    ck(C.targets[2] not in late and C.current[2].cell(0) in late,'Outside update invalidates untouched-target correspondence')
    # Scope is an explicit API parameter; a valid request to C must not be executed by scope A.
    tab2=((0,None,0),((2,0),None));K2,_,_=C.run(C.encode(tab2),op)
    ck(C.decode(K2)==(tab2,False),'Wrong target is rejected by scope rather than silently dispatched')
    old,_,_=C.run(C.encode(tab2),('execute',0));ck(C.targets[2] not in old,'Global and scoped operation semantics are distinct')
    # Releasing a shared pivot but restoring only the named target loses a bystander.
    tab3=((0,None,0),((1,0),None));op3=('execute_scope',0,(1,),(1,));w3=C.programs[op3]
    start=w3.index(p.one(1))+1
    # Drop the complete three-command restoration block for A from the compiled suffix.
    # The first source reconstruction after the release is for A.
    broken=w3[:start]+w3[start+3:]
    K3,_,log3=C.runword(C.encode(tab3),broken,True)
    ck(C.targets[0] not in K3 and C.current[0].cell(0) in K3,'Every touched neighbor, not just allowed target, needs reconstruction')
    return dict(mode='failures',checks=CHECKS,kernel_calls=C.calls,command_uses=C.uses,
                missed_release=dict(omitted_position=ix+1,initial=J,end=K,trace=log),
                missing_neighbor_restore=dict(initial=C.encode(tab3),end=K3,trace=log3),
                one_external_kernel_call=1)

def programs():
    C=Compiler(slots=6,specs=selected_specs())
    return dict(mode='programs',layout=dict(current=[x.__dict__ for x in C.current],refs=[x.__dict__ for x in C.refs],
               back=C.back.__dict__,block=C.block,marker=C.marker,success=C.success,work=C.work,out=C.out),
               members=C.members,candidates=sorted(C.H),words={str(op):w for op,w in C.programs.items() if op[0]=='execute_scope'},
               lengths={str(op):len(w) for op,w in C.programs.items() if op[0]=='execute_scope'})

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=('audit','births','footprints','histories','omissions','failures','programs'))
    ap.add_argument('--slots',type=int,default=2);ap.add_argument('--canonical',action='store_true');ap.add_argument('--all-scopes',action='store_true')
    ap.add_argument('--start',type=int,default=0);ap.add_argument('--stop',type=int);ap.add_argument('--out',required=True)
    a=ap.parse_args()
    if a.mode=='audit':result=audit(a.slots,a.canonical,a.start,a.stop,a.all_scopes)
    else:result={'births':births,'footprints':finite_footprints,'histories':histories,'omissions':omissions,'failures':failures,'programs':programs}[a.mode]()
    Path(a.out).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print({k:v for k,v in result.items() if k in ('mode','checks','kernel_calls','command_uses','transitions','domain','pairs','minimal_transversals','annotated_kernel_calls','members')})
