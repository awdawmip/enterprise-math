"""Cooperative triadic admission around the inherited feedback executor.

Every matching transition calls the unchanged inherited kernel. Controller
branches inspect complete Boolean registers only. Schedules, source decoding,
and accepted-order recording are test observers, not production decision inputs.

Contract: atomic original primitives, unique non-reentrant participant slots,
closed access paths, private outputs, no omissions or external writes. This is
cooperative mutual exclusion plus feedback, not a new conditional-release primitive.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from functools import lru_cache
from pathlib import Path
from collections import defaultdict
import argparse, json, sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_feedback as old
base,p,m,e,r=old.base,old.p,old.m,old.e,old.r
ONE,ZERO=old.ONE,old.ZERO
CHECKS=0

def ck(ok,why):
    global CHECKS
    CHECKS+=1
    if not ok: raise AssertionError(why)

def bit(J,o):
    """Feedback reads only a complete private six-member Boolean register."""
    a=all(h in J for h in p.reg(o,0));b=all(h in J for h in p.reg(o,1))
    if a==b: raise ValueError('Expected exactly one complete Boolean register')
    return bool(b)

@dataclass(frozen=True)
class Lane:
    a:int; b:int; work:int; admitted:int; reply:int

@dataclass(frozen=True)
class PC:
    phase:str='entry'
    job:int=0
    target:int=0
    pos:int=0

@dataclass(frozen=True)
class Node:
    J:tuple
    pcs:tuple[PC,...]
    order:tuple[int,...]=()

class Guard:
    def __init__(self,slots=1,actors=2):
        if actors<1:raise ValueError('At least one participant required')
        self.C=old.Compiler(slots=slots)
        self.actors=actors
        self.core_members=frozenset().union(*(frozenset(h) for h in self.C.H))
        self.g=max(self.core_members)+1
        self.lanes=[];H=set(self.C.H);entry=[];exit_words=[]
        for i in range(actors):
            n=self.g+1+15*i
            v=Lane(n,n+1,n+2,n+2,n+8)
            self.lanes.append(v)
            lock=tuple(sorted((self.g,v.a,v.b)));H.add(lock)
            hh,rd,_=base.old.reader(v.b,v.admitted,v.work);H.update(hh)
            hh,cp=p.copy_program(self.C.out,v.reply,v.work);H.update(hh)
            # Clear previous payload/entry flag, then acquire and privately verify.
            entry.append(tuple(p.clear_word(v.reply)+p.clear_word(v.admitted)+[p.add(lock)]+rd))
            exit_words.append(tuple(cp+[p.one(v.a)]))
        self.lanes=tuple(self.lanes);self.H=frozenset(H)
        self.entry=tuple(entry);self.exit=tuple(exit_words)
        self.members=len(frozenset().union(*(frozenset(h) for h in self.H)))
        self.calls=self.uses=0
        self._raw=lru_cache(maxsize=500000)(self._uncached)
    def lock(self,i):
        v=self.lanes[i];return tuple(sorted((self.g,v.a,v.b)))
    def _uncached(self,J,raw):
        self.calls+=1;K,_,ok=e.step(J,raw,self.H);return K,bool(ok)
    def runword(self,J,word):
        mass=e.prep(J)
        for raw in word:
            self.uses+=1;J,_=self._raw(J,raw);mass=r.serial(mass,ONE)
        return J,mass
    def core(self,J):return m.canon(h for h in J if set(h)<=self.core_members)
    def start_pc(self,joblist,k):
        if k==len(joblist):return PC('publish',k)
        return PC('match' if joblist[k][0]=='feedback' else 'fixed',k)
    def word(self,i,pc,jobs):
        if pc.phase=='entry':return self.entry[i]
        if pc.phase=='fixed':return self.C.programs[jobs[i][pc.job]]
        if pc.phase=='match':return self.C.programs[('match',jobs[i][pc.job][1],pc.target)]
        if pc.phase=='commit':return self.C.commit(pc.target)
        if pc.phase=='publish':return self.exit[i]
        raise ValueError('Finished actor has no enabled step')
    def next(self,node,i,jobs,check=True):
        pc=node.pcs[i];word=self.word(i,pc,jobs);raw=word[pc.pos]
        self.uses+=1;K,ok=self._raw(node.J,raw)
        new=replace(pc,pos=pc.pos+1);order=node.order
        if new.pos==len(word):
            if pc.phase=='entry':
                acquired=bit(K,self.lanes[i].admitted)
                if check:ck(acquired==(self.lock(i) in K),'Private entry result equals own live token')
                new=self.start_pc(jobs[i],0) if acquired else PC('busy')
                if acquired:order=order+(i,)
            elif pc.phase in ('fixed','commit'):
                new=self.start_pc(jobs[i],pc.job+1)
            elif pc.phase=='match':
                positive=self.C.observe_result(K)
                if positive:new=PC('commit',pc.job,pc.target)
                elif pc.target+1<self.C.d:new=PC('match',pc.job,pc.target+1)
                else:new=self.start_pc(jobs[i],pc.job+1)
            elif pc.phase=='publish':new=PC('done',pc.job)
        pcs=list(node.pcs);pcs[i]=new;ans=Node(K,tuple(pcs),order)
        if check:self.invariant(ans)
        return ans,raw,ok
    def invariant(self,node):
        owners=[i for i in range(self.actors) if self.lock(i) in node.J]
        ck(len(owners)<=1,'Shared gate permits at most one owner token')
        body=[i for i,c in enumerate(node.pcs) if c.phase in ('fixed','match','commit','publish')]
        ck(len(body)<=1,'At most one shared body is executing')
        for i in body:ck(self.lock(i) in node.J,'Every body step is protected by its own token')
    def done(self,node):return all(c.phase in ('done','busy') for c in node.pcs)
    def terminal(self,node,jobs,initial_table):
        ck(self.done(node),'Complete attempt histories only')
        tab=initial_table;last=None;answers={}
        for i in node.order:
            value=None
            for op in jobs[i]:
                spec=('execute',op[1]) if op[0]=='feedback' else op
                tab,value=base.expected(self.C,tab,spec)
            answers[i]=value;last=value
        want=self.C.encode(tab,last)
        for i,v in enumerate(self.lanes):
            accepted=i in node.order
            want=m.canon(want+p.reg(v.admitted,int(accepted)))
            if accepted:want=m.canon(want+p.reg(v.reply,int(answers[i])))
            ck(node.pcs[i].phase==('done' if accepted else 'busy'),'Busy and completed are distinct outcomes')
        ck(node.J==want,'Entire endpoint: exact source/table/flags/private replies, no hidden work')
        return tuple((i,answers.get(i,'BUSY')) for i in range(self.actors))
    def stats(self):
        return dict(assertions=CHECKS,kernel_calls=self.calls,primitive_uses=self.uses,
                    members=self.members,base_members=self.C.members,candidates=len(self.H),
                    base_candidates=len(self.C.H),actors=self.actors,slots=self.C.slots,
                    separately_called_parent_kernel=self.C.calls,separately_called_parent_uses=self.C.uses,
                    entry_length=len(self.entry[0]),reply_and_unlock_length=len(self.exit[0]))


def explore(G,table,jobs,max_states=400000):
    init=Node(G.C.encode(table),tuple(PC() for _ in jobs))
    frontier={init:e.prep(init.J)};term={};layers=[];states=edges=0;steps=0
    while frontier:
        nxt={};states+=len(frontier)
        if states>max_states:raise RuntimeError('Declared exploration state budget exceeded')
        for node,mass in frontier.items():
            if G.done(node):
                key=(node,G.terminal(node,jobs,table))
                term[key]=r.merge(term.get(key,ZERO),mass)
                continue
            for i,pc in enumerate(node.pcs):
                if pc.phase in ('busy','done'):continue
                q,_,_=G.next(node,i,jobs);edges+=1
                nxt[q]=r.merge(nxt.get(q,ZERO),r.serial(mass,ONE))
        layers.append([steps,len(frontier)]);frontier=nxt;steps+=1
    total=ZERO;classes=[]
    for (node,ans),mass in term.items():
        total=r.merge(total,mass)
        classes.append(dict(order=node.order,responses=ans,CWM=e.cw(mass)))
    ck(bool(term),'Exploration terminates with completed attempts')
    return dict(states=states,edges=edges,terminal_classes=len(term),CWM=e.cw(total),
                outcomes=classes,layers=layers)


def run_schedule(G,table,jobs,schedule,finish_order=(),named=False):
    node=Node(G.C.encode(table),tuple(PC() for _ in jobs));trace=[]
    st=base.ref.old.seed(node.J) if named else None
    initial_names=st.names() if named else {}
    for i in schedule:
        before=node
        node,raw,ok=G.next(node,i,jobs)
        row=dict(actor=i,raw=raw,phase=before.pcs[i].phase,next_phase=node.pcs[i].phase)
        if named:
            st,_,d=base.ref.old.raw_step(st,raw,G.H)
            ck(st.matching==node.J,'Named trace uses same original matching transition')
            row['source_retired']=[v for v in d['retired'] if v[0] in G.C.targets]
            row['source_created']=[v for v in d['created'] if v[0] in G.C.targets]
            row['source_names']=[v for v in st.events if v[0] in G.C.targets]
        trace.append(row)
    for i in finish_order:
        while node.pcs[i].phase not in ('done','busy'):
            before=node;node,raw,ok=G.next(node,i,jobs)
            row=dict(actor=i,raw=raw,phase=before.pcs[i].phase,next_phase=node.pcs[i].phase)
            if named:
                st,_,d=base.ref.old.raw_step(st,raw,G.H)
                ck(st.matching==node.J,'Named remaining matching transition')
                row['source_retired']=[v for v in d['retired'] if v[0] in G.C.targets]
                row['source_created']=[v for v in d['created'] if v[0] in G.C.targets]
                row['source_names']=[v for v in st.events if v[0] in G.C.targets]
            trace.append(row)
    ans=G.terminal(node,jobs,table) if G.done(node) else None
    return node,dict(initial_table=table,final_responses=ans,order=node.order,
                    steps=len(trace),trace=trace,source_initial=list(initial_names.items()))


def smoke():
    G=Guard(slots=1,actors=2);table=((0,None,0),((0,0),))
    jobs=((('feedback',0),),(('release',1),('reserve',0)))
    # Holder completes acquisition+positive match; writer attempts entry meanwhile.
    positive=len(G.entry[0])+len(G.C.programs[('match',0,0)])
    node,rec=run_schedule(G,table,jobs,[0]*positive+[1]*11,(0,),named=True)
    ck(rec['final_responses']==((0,True),(1,'BUSY')),'Writer cannot enter check/commit gap')
    C=G.C.targets[2]
    names=dict(rec['source_initial'])
    ck(all(dict(x['source_names']).get(C)==names[C] for x in rec['trace']),
       'Untouched C birth persists in every concurrent prefix')
    ck(not any(x['source_created'] for x in rec['trace']),'Feedback case creates no source event')
    # Writer wins and recreates before the execute call begins its body.
    end,rev=run_schedule(G,table,jobs,[],(1,0),named=True)
    ck(rev['final_responses']==((0,False),(1,True)),'Old request is stale after guarded recreation')
    return dict(mode='smoke',guarded_gap=rec,writer_first=rev,**G.stats())


def all_interleavings(case):
    G=Guard(slots=1,actors=2)
    table=((0,None,0),((0,0),))
    cases={
       'execute_restart':((('feedback',0),),(('release',1),('reserve',0))),
       'execute_execute':((('feedback',0),),(('feedback',0),)),
       'execute_bind':((('feedback',0),),(('bind',0,2),)),
       'release_create':((('release',1),),(('reserve',1),)),
    }
    data=explore(G,table,cases[case])
    return dict(mode='interleavings',case=case,jobs=cases[case],result=data,**G.stats())


def entry_histories(actors=3):
    G=Guard(slots=1,actors=actors);J=G.C.encode(((None,)*3,(None,)))
    # Complete entry attempts only; the successful owner retains the token.
    D={(J,(0,)*actors):e.prep(J)};edges=0;states=0
    for _ in range(11*actors):
        states+=len(D);nxt={}
        for (J,pc),mass in D.items():
            for i,k in enumerate(pc):
                if k==11:continue
                G.uses+=1;K,_=G._raw(J,G.entry[i][k]);pp=list(pc);pp[i]+=1
                key=K,tuple(pp);nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE));edges+=1
        D=nxt
    total=ZERO;winners={}
    for (J,pc),mass in D.items():
        got=tuple(bit(J,v.admitted) for v in G.lanes)
        ck(sum(got)==1,'Exactly one private entry succeeds before any unlock')
        winner=got.index(True);ck(G.lock(winner) in J,'Success corresponds to real token')
        ck(all(not p.restrict(J,v.reply) for v in G.lanes),'Busy is not a fabricated application false')
        winners[winner]=r.merge(winners.get(winner,ZERO),mass);total=r.merge(total,mass)
    return dict(mode='entry_histories',states=states,edges=edges,CWM=e.cw(total),
                winner_weights={str(i):e.cw(x) for i,x in winners.items()},**G.stats())


def emit_programs():
    rows=[]
    for slots in (1,2,6):
        G=Guard(slots,2)
        rows.append(dict(slots=slots,gate=G.g,lanes=[v.__dict__ for v in G.lanes],
                         entry=G.entry,reply_unlock=G.exit,H=sorted(G.H),
                         inherited_result=G.C.out,stats=G.stats(),
                         controller='entry flag -> BUSY or guarded body; copy shared result before private unlock'))
    return rows

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['smoke','entries','interleavings','programs'])
    ap.add_argument('--case',default='execute_restart');ap.add_argument('--actors',type=int,default=3)
    ap.add_argument('--out',required=True);args=ap.parse_args()
    if args.mode=='smoke':ans=smoke()
    elif args.mode=='entries':ans=entry_histories(args.actors)
    elif args.mode=='programs':ans=emit_programs()
    else:ans=all_interleavings(args.case)
    Path(args.out).write_text(json.dumps(ans,ensure_ascii=False,indent=2),encoding='utf8')
    print(json.dumps({k:v for k,v in ans.items() if k not in ('guarded_gap','writer_first','result')} if isinstance(ans,dict) else {'program_sets':len(ans)},ensure_ascii=False))
