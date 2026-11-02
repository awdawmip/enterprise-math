"""Result-driven execution using inherited triadic queries and two-step commit.

The new controller observes ONLY the fully formed Boolean result register.
It is an explicit control-language extension: Branch is not a reserve/release
primitive. Source/table updates use the unchanged inherited BRC kernel.
Correctness assumes the table and source are stable during the full operation.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from itertools import product

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_selective as prior
base=prior.base
p,m,e,r=base.p,base.m,base.e,base.r
ONE,ZERO=base.ONE,base.ZERO
CHECKS=0

def ck(value, label):
    global CHECKS
    CHECKS+=1
    if not value: raise AssertionError(label)

class Compiler(base.Compiler):
    def alphabet(self):
        return super().alphabet()+tuple(('match',i,t) for i in range(self.slots) for t in range(self.d))
    def _compile(self,op):
        if op[0]=='match':
            _,i,t=op
            return self.clearout()+self.emit_local_equal(t,i)
        return super()._compile(op)
    def observe_result(self,J):
        """Explicit feedback port; observes neither requests nor actual source.

        Requires the entire encoded Boolean, including both head and tail.
        Partial output is a protocol error, not an inferred 0 or 1.
        """
        b0=all(h in J for h in p.reg(self.out,0))
        b1=all(h in J for h in p.reg(self.out,1))
        if b0==b1: raise ValueError('Feedback requires exactly one complete Boolean output')
        return bool(b1)
    def commit(self,t):
        # Called only on an actual positive local equality observation.
        return (p.one(min(self.targets[t])),p.one(self.current[t].anchor))
    def feedback(self,J,i,trace=False):
        if not 0<=i<self.slots:raise ValueError('Reference slot out of range')
        mass=e.prep(J);branches=[];word=[];log=[]
        for t in range(self.d):
            probe=self.programs[('match',i,t)]
            J,pm,plog=self.runword(J,probe,trace)
            mass=r.serial(mass,pm);word.extend(probe);log.extend(plog)
            bit=self.observe_result(J);branches.append((t,bit))
            if bit:
                commit=self.commit(t)
                J,pm,plog=self.runword(J,commit,trace)
                mass=r.serial(mass,pm);word.extend(commit);log.extend(plog)
                break
        return J,mass,dict(branches=branches,word=tuple(word),commands=len(word),feedback_reads=len(branches),trace=log)


def stats(C):
    return dict(assertions=CHECKS,kernel_calls=C.calls,command_uses=C.uses,
                members=C.members,candidates=len(C.H),slots=C.slots,targets=C.targets)

def audit(slots=2,start=0,stop=None):
    C=Compiler(slots=slots);B=base.Compiler(slots=slots)
    ck(C.members==B.members and C.H==B.H,'No new matching members or candidates')
    dom=base.domain(C);stop=len(dom) if stop is None else min(stop,len(dom))
    count=0;paths={};mass=ZERO
    for idx in range(start,stop):
        table=dom[idx];J=C.encode(table,None if idx%3==0 else idx%2)
        for i in range(slots):
            K,wm,data=C.feedback(J,i)
            want=base.expected(C,table,('execute',i))
            ck(C.decode(K)==want,'Exact full source/table/result endpoint')
            q=table[1][i];t=q[0] if q is not None and want[1] else None
            src_rel={a for a in C.U if p.one(a) in data['word']}
            ck(src_rel==(set() if t is None else {min(C.targets[t])}),'Path-dependent exact source release set')
            probes=C.d if t is None else t+1
            ck(data['commands']==probes*(4*C.colors+9)+(2 if t is not None else 0),'Executed raw length')
            ck(data['feedback_reads']==probes,'Feedback observations separately counted')
            path=str(tuple(b for _,b in data['branches']));paths[path]=paths.get(path,0)+1
            mass=r.merge(mass,wm);count+=1
    ck(mass.count==count,'CWM retains every input/slot occurrence')
    return dict(mode='audit',domain=len(dom),start=start,stop=stop,cases=count,paths=paths,CWM=e.cw(mass),**stats(C))


def named_feedback(C,st,i,keep=False):
    logs=[];branches=[];words=[];changes=[];prefixes=[]
    def run(word):
        nonlocal st
        for raw in word:
            st,ok,delta=base.ref.old.raw_step(st,raw,C.H)
            words.append(raw)
            src_created=[v for v in delta['created'] if v[0] in C.targets]
            src_retired=[v for v in delta['retired'] if v[0] in C.targets]
            if src_created or src_retired:
                changes.append(dict(step=len(words),created=src_created,retired=src_retired))
            prefixes.append({h:n for h,n in st.events if h in C.targets})
            if keep:logs.append(dict(step=len(words),operation=raw,success=ok,source=prefixes[-1],delta=delta))
    for t in range(C.d):
        run(C.programs[('match',i,t)])
        bit=C.observe_result(st.matching);branches.append((t,bit))
        if bit:run(C.commit(t));break
    return st,dict(branches=branches,word=words,changes=changes,prefixes=prefixes,trace=logs)


def births():
    C=Compiler(slots=1);dom=base.domain(C);cases=0
    for table in dom:
        st=base.ref.old.seed(C.encode(table));initial=st.names()
        final,data=named_feedback(C,st,0)
        want=base.expected(C,table,('execute',0));ck(C.decode(final.matching)==want,'Named exact endpoint')
        q=table[1][0];deleted=C.targets[q[0]] if want[1] else None
        for h in base.source(C,table[0]):
            if h==deleted:
                ck(h not in final.names(),'Valid target is deleted')
            else:
                ck(all(v.get(h)==initial[h] for v in data['prefixes']),'Every surviving source birth persists at every primitive prefix')
        retired=[tuple(v[0]) for row in data['changes'] for v in row['retired']]
        ck(retired==([] if deleted is None else [deleted]),'Zero or exactly one real source retirement')
        ck(not any(row['created'] for row in data['changes']),'No source reconstruction')
        cases+=1
    C6=Compiler(slots=6);examples=[]
    for name,cur,q in [('stale_B',(0,None,0),(1,0)),('stale_A',(1,None,0),(0,0)),('valid_A',(0,None,0),(0,0)),('valid_C',(0,None,0),(2,0)),('valid_B',(None,0,None),(1,0)),('empty',(0,None,0),None)]:
        tab=(cur,(q,)+(None,)*5);initial=base.ref.old.seed(C6.encode(tab))
        end,record=named_feedback(C6,initial,0)
        ck(C6.decode(end.matching)==base.expected(C6,tab,('execute',0)),'Six-slot example endpoint')
        examples.append(dict(name=name,table=tab,branches=record['branches'],commands=len(record['word']),
                             source_before=[v for v in initial.events if v[0] in C6.targets],
                             source_after=[v for v in end.events if v[0] in C6.targets],changes=record['changes']))
    return dict(mode='births',cases=cases,examples=examples,annotated_kernel_calls=base.ref.old.KERNEL_CALLS,**stats(C))


def histories(depth=5):
    C=Compiler(slots=1)
    ops=(('reserve',0),('reserve',1),('reserve',2),('bind',0,0),('bind',0,1),('bind',0,2),('feedback',0),('release',1),('release',4))
    J=C.encode(((None,)*3,(None,)));D={(J,()):ONE};layers=[]
    for level in range(depth):
        nxt={}
        for (J,answers),weight in D.items():
            table=C.decode(J)[0] if level else ((None,)*3,(None,))
            for op in ops:
                if op[0]=='feedback':K,wm,_=C.feedback(J,op[1]);want=base.expected(C,table,('execute',op[1]))
                else:K,wm,_=C.run(J,op);want=base.expected(C,table,op)
                got=C.decode(K);ck(got==want,'Feedback composes with actual API words')
                key=(K,answers+(got[1],));nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(weight,wm))
        D=nxt;total=ZERO
        for w in D.values():total=r.merge(total,w)
        ck(total.count==len(ops)**(level+1),'All histories, no postselection')
        layers.append(dict(depth=level+1,classes=len(D),CWM=e.cw(total)))
    return dict(mode='histories',alphabet=ops,layers=layers,**stats(C))


def failures():
    C=Compiler(slots=1);table=((0,None,0),((0,0),));J=C.encode(table)
    # A real successful test is followed by a complete source lifecycle before commit.
    st=base.ref.old.seed(J);before=st.names();rows=[]
    def namedrun(word,label):
        nonlocal st
        for raw in word:st,ok,delta=base.ref.old.raw_step(st,raw,C.H)
        rows.append(dict(stage=label,source=[v for v in st.events if v[0] in C.targets],table=C.decode(st.matching),matching=st.matching))
    namedrun(C.programs[('match',0,0)],'positive_check')
    saved=C.observe_result(st.matching);ck(saved,'Actual check was true')
    namedrun(C.programs[('release',1)],'competing_release')
    namedrun(C.programs[('reserve',0)],'competing_recreation')
    newbirth=st.names()[C.targets[0]]
    ck(newbirth!=before[C.targets[0]],'New physical source occurrence')
    ck(not base.expected(C,C.decode(st.matching)[0],('valid',0))[1],'Original request is stale before commit')
    namedrun(C.commit(0),'commit_using_saved_true')
    ck(C.targets[0] not in st.matching,'Stale feedback deletes the new occurrence')
    ck(st.names()[C.targets[2]]==before[C.targets[2]],'Unrelated C remains physically intact even in race')
    # A missing probe can create a false positive; controller requires trustworthy result.
    stale=((0,None,0),((1,0),));S=C.encode(stale);probe=C.programs[('match',0,0)];witness=None
    for ix in range(len(probe)):
        T,_,trace=C.runword(S,probe,True,(ix,))
        try:bit=C.observe_result(T)
        except ValueError:continue
        if bit:
            V,_,_=C.runword(T,C.commit(0))
            if C.targets[0] not in V:
                witness=dict(omitted_position=ix+1,omitted_command=probe[ix],initial=S,after_probe=T,end=V,trace=trace);break
    ck(witness is not None,'Single omitted check can produce harmful false success')
    # A complete result is required by the feedback port.
    S1,_,_=C.run(J,('match',0,0));broken,_=C._raw(S1,p.one(C.out+5))
    try:C.observe_result(broken)
    except ValueError:rejected=True
    else:rejected=False
    ck(rejected,'Partial output is refused, not treated as 0')
    # A missing commit release breaks source/table coupling.
    V,_,_=C.runword(S1,C.commit(0),omitted=(0,))
    ck(C.targets[0] in V and not any(C.current[0].cell(c) in V for c in range(C.colors)),'Commit omission needs its own protection')
    return dict(mode='failures',check_use_race=rows,false_positive_omission=witness,
                partial_response_rejected=rejected,commit_omission_end=V,**stats(C))


def omissions():
    C=Compiler(slots=1);rows=[]
    cases=[('valid_A',((0,None,0),((0,0),))),('stale_B',((0,None,0),((1,0),))),('valid_B',((None,0,None),((1,0),)))]
    for name,table in cases:
        initial=C.encode(table);wanted,_,normal=C.feedback(initial,0)
        for f in (1,2):
            active={(initial,0,()):ONE};final={};total_ops=0
            def advance(D,word):
                for raw in word:
                    nxt={}
                    for (J,k,path),mass in D.items():
                        C.uses+=1;K,_=C._raw(J,raw);key=(K,k,path)
                        nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
                        if k<f:
                            key=(J,k+1,path);nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
                    D=nxt
                return D
            for t in range(C.d):
                probe=tuple(raw for raw in C.programs[('match',0,t)] for _ in range(f+1))
                active=advance(active,probe);next_active={};success={}
                for (J,k,path),mass in active.items():
                    bit=C.observe_result(J);key=(J,k,path+(bit,))
                    dst=success if bit else next_active;dst[key]=r.merge(dst.get(key,ZERO),mass)
                if success:
                    commit=tuple(raw for raw in C.commit(t) for _ in range(f+1))
                    for key,mass in advance(success,commit).items():final[key]=r.merge(final.get(key,ZERO),mass)
                active=next_active
            for key,mass in active.items():final[key]=r.merge(final.get(key,ZERO),mass)
            totals={};paths=set()
            for (J,k,path),mass in final.items():
                ck(J==wanted,'Protected adaptive execution exact endpoint')
                totals[k]=r.merge(totals.get(k,ZERO),mass);paths.add(path)
            ck(paths=={tuple(b for _,b in normal['branches'])},'All protected histories take the correct control path')
            length=normal['commands']*(f+1);positions={0:ONE}
            for _ in range(length):
                nxt={}
                for k,mass in positions.items():
                    nxt[k]=r.merge(nxt.get(k,ZERO),r.serial(mass,ONE))
                    if k<f:nxt[k+1]=r.merge(nxt.get(k+1,ZERO),r.serial(mass,ONE))
                positions=nxt
            ck(positions==totals,'All actual branch-path omission histories retained')
            rows.append(dict(case=name,budget=f,length=length,branches=list(paths)[0],histories={str(k):e.cw(v) for k,v in totals.items()}))
    return dict(mode='omissions',rows=rows,**stats(C))


def cycle(rounds=100):
    C=Compiler(slots=6);tab=((None,)*3,(None,)*6);st=base.ref.old.seed(C.encode(tab));sentinel=None;actions=raws=0;records=[]
    def apply(op):
        nonlocal st,tab,sentinel,actions,raws
        if op[0]=='feedback':
            want=base.expected(C,tab,('execute',op[1]));oldst=st
            st,data=named_feedback(C,st,op[1]);count=len(data['word'])
            if sentinel is not None:ck(all(v.get(C.targets[2])==sentinel for v in data['prefixes']),'C birth remains through every feedback prefix')
        else:
            want=base.expected(C,tab,op);count=len(C.programs[op])
            for cmd in C.programs[op]:
                st,_,_=base.ref.old.raw_step(st,cmd,C.H)
                if sentinel is not None:ck(st.names().get(C.targets[2])==sentinel,'C birth remains through other primitive prefixes')
        got=C.decode(st.matching);ck(got==want,'Sequential operation and full state')
        tab=got[0];actions+=1;raws+=count
        if len(records)<30:records.append(dict(op=op,table=tab,response=got[1],commands=count))
    apply(('reserve',2));sentinel=st.names()[C.targets[2]]
    apply(('bind',5,2))
    for n in range(rounds):
        i=n%4
        for op in (('reserve',0),('bind',i,0),('copy',4,i),('feedback',i),('reserve',0),('feedback',4),('valid',5),('same',i,4)):
            apply(op)
    return dict(mode='cycle',rounds=rounds,api_actions=actions,raw_commands=raws,preserved_C_name=sentinel,
                trace_prefix=records,annotated_kernel_calls=base.ref.old.KERNEL_CALLS,**stats(C))


def controls():
    rows=[]
    for slots in (1,2,6):
        C=Compiler(slots=slots);L=4*C.colors+9
        rows.append(dict(slots=slots,members=C.members,candidates=len(C.H),test_length=L,
                         absent_or_stale=3*L,valid_A=L+2,valid_B=2*L+2,valid_C=3*L+2,
                         parent_universal=len(C.programs[('execute',0)])))
    # Concrete terminal paths distinguish k simultaneously present targets and rejection.
    lower=[]
    for k in range(1,5):
        H=tuple(tuple(range(3*t+1,3*t+4)) for t in range(k));C=Compiler(H,slots=1)
        cur=(0,)*k;words=[];responses=[]
        for t in list(range(k))+[None]:
            q=None if t is None else (t,0);table=(cur,(q,));J=C.encode(table)
            K,_,data=C.feedback(J,0);ck(C.decode(K)==base.expected(C,table,('execute',0)),'Disjoint control lower-bound family')
            words.append(tuple(data['word']));responses.append(data['branches'])
        ck(len(set(words))==k+1,'k+1 distinct source-action paths are realized')
        lower.append(dict(coexisting_targets=k,distinct_paths=len(set(words)),feedback_paths=responses))
    return dict(mode='controls',costs=rows,lower_bound_witnesses=lower,assertions=CHECKS)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['audit','births','histories','failures','omissions','cycle','controls'])
    ap.add_argument('--slots',type=int,default=2);ap.add_argument('--start',type=int,default=0);ap.add_argument('--stop',type=int)
    ap.add_argument('--rounds',type=int,default=100);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args()
    if a.mode=='audit':result=audit(a.slots,a.start,a.stop)
    elif a.mode=='cycle':result=cycle(a.rounds)
    else:result=globals()[a.mode]()
    def encode(obj):
        if isinstance(obj,set):return sorted(obj)
        raise TypeError(type(obj).__name__)
    # Convert tuple-keyed dictionaries in full traces into readable key strings.
    def clean(x):
        if isinstance(x,dict):return {str(k):clean(v) for k,v in x.items()}
        if isinstance(x,(tuple,list)):return [clean(v) for v in x]
        return x
    a.output.write_text(json.dumps(clean(result),ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('trace_prefix','examples','check_use_race','false_positive_omission')},ensure_ascii=False))

if __name__=='__main__':main()
