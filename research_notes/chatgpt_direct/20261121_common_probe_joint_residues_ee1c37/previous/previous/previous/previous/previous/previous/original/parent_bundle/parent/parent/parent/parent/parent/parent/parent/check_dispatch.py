"""Adaptive subset queries compiled from the inherited original BRC words.

Production observes only a complete result register. The decision tree and
candidate sets are compile-time objects; source/table decoders are test-only.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import argparse, json, sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_gate_phase as gate
feedback=gate.old.old
base=feedback.base
p,m,e,r=feedback.p,feedback.m,feedback.e,feedback.r
ONE,ZERO=feedback.ONE,feedback.ZERO
CHECKS=0

def ck(value, label):
    global CHECKS
    CHECKS += 1
    if not value: raise AssertionError(label)

@dataclass(frozen=True)
class Test:
    remaining:tuple[int,...]
    group:tuple[int,...]=()
    yes:int=-1
    no:int=-1
    @property
    def leaf(self): return len(self.remaining)==1


def tree_for(d:int)->tuple[Test,...]:
    """Outcome -1 is invalid; a positive query cannot include -1.

    Every split has floor(n/2) positive labels. Placing INVALID last makes the
    three-target tree: test {A,B}; if yes test A, otherwise test C.
    """
    if d<1: raise ValueError('positive target count required')
    nodes=[]
    def build(labels):
        ix=len(nodes);nodes.append(Test(labels))
        if len(labels)>1:
            k=len(labels)//2
            left=tuple(t for t in labels if t>=0)[:k]
            right=tuple(t for t in labels if t not in left)
            a,b=build(left),build(right)
            nodes[ix]=Test(labels,left,a,b)
        return ix
    build(tuple(range(d))+(-1,))
    return tuple(nodes)

class Compiler(feedback.Compiler):
    def __init__(self,H=base.H_DEFAULT,slots=2):
        super().__init__(H=H,slots=slots)
        self.tree=tree_for(self.d)
        self.queries={}
        for i in range(slots):
            for k,node in enumerate(self.tree):
                if not node.leaf:self.queries[i,k]=self.compile_group(i,node.group)
        self.leaf_words={}
        # Only positive outcomes can finish on a negative observation and need
        # the complete Boolean business result rewritten to true.
        for k,node in enumerate(self.tree):
            if node.leaf:continue
            for bit,child in ((True,node.yes),(False,node.no)):
                target=self.tree[child]
                if target.leaf and target.remaining[0]>=0:
                    t=target.remaining[0]
                    fix=() if bit else tuple(self.clearout()+[p.add(h) for h in p.reg(self.out,1)])
                    self.leaf_words[child]=fix+self.commit(t)
        all_new=[w for w in self.queries.values()]+list(self.leaf_words.values())
        for w in all_new:
            for raw in w:
                if raw[0]=='reserve':ck(tuple(raw[1]) in self.H,'every proposal is inherited')
        self.decision_reads=0

    def compile_group(self,i,S):
        if not S or len(set(S))!=len(S) or any(t<0 or t>=self.d for t in S):
            raise ValueError('query group is a nonempty set of declared targets')
        first=self.programs['match',i,S[0]]
        blocks=tuple(raw for t in S for raw in self.programs['match',i,t][2:2+4*self.colors])
        return tuple(self.clearout())+blocks+tuple(first[-7:])

    def dispatch(self,J,i,trace=False):
        if not 0<=i<self.slots:raise ValueError('invalid request slot')
        node=0;mass=e.prep(J);words=[];observations=[];logs=[]
        while not self.tree[node].leaf:
            w=self.queries[i,node]
            J,wm,log=self.runword(J,w,trace);mass=r.serial(mass,wm);words.extend(w);logs.extend(log)
            result=self.observe_result(J);self.decision_reads+=1
            spec=self.tree[node]
            observations.append(dict(node=node,group=spec.group,answer=result))
            node=spec.yes if result else spec.no
        label=self.tree[node].remaining[0]
        if label>=0:
            w=self.leaf_words[node]
            J,wm,log=self.runword(J,w,trace);mass=r.serial(mass,wm);words.extend(w);logs.extend(log)
        return J,mass,dict(outcome=label,reads=len(observations),observations=observations,
                           commands=len(words),word=tuple(words),trace=logs)

    def counters(self):
        return dict(assertions=CHECKS,original_kernel_cache_misses=self.calls,
                    original_command_uses=self.uses,feedback_reads=self.decision_reads,
                    slots=self.slots,targets=self.d,colors=self.colors,
                    members=self.members,candidates=len(self.H))


def outcome(table,i):
    cur,refs=table;q=refs[i]
    return q[0] if q is not None and cur[q[0]]==q[1] else -1


def audit(slots=2):
    C=Compiler(slots=slots);parent=feedback.Compiler(slots=slots)
    ck(C.H==parent.H and C.members==parent.members,'same matching inventory and candidate permissions')
    dom=base.domain(C);mass=ZERO;cost={};casecount=0;querycount=0
    for idx,tab in enumerate(dom):
        J=C.encode(tab,(None,0,1)[idx%3])
        for i in range(slots):
            want=base.expected(C,tab,('execute',i));label=outcome(tab,i)
            K,wm,data=C.dispatch(J,i)
            ck(C.decode(K)==want,'complete source/table/output and clean workspace')
            ck(data['outcome']==label,'explicit outcome class correct')
            ck(data['reads']<= (C.d).bit_length(),'balanced binary depth')
            rel={a for a in C.U if p.one(a) in data['word']}
            ck(rel==(set() if label<0 else {min(C.targets[label])}),'zero or one actual source release')
            key=str(label);cost.setdefault(key,set()).add(data['commands'])
            mass=r.merge(mass,wm);casecount+=1
            # Full group-query contracts, also for nodes not visited by dispatch.
            for k,node in enumerate(C.tree):
                if node.leaf:continue
                T,_,_=C.runword(J,C.queries[i,k])
                expected_bit=label in node.group
                ck(T==C.encode(tab,expected_bit),'query is source-preserving and its bit means group membership')
                querycount+=1
    return dict(mode='audit',domain=len(dom),dispatch_cases=casecount,group_contract_cases=querycount,
                cost_by_outcome={k:sorted(v) for k,v in cost.items()},CWM=e.cw(mass),**C.counters())


def costs_and_births():
    C=Compiler(slots=6);F=feedback.Compiler(slots=6);records=[]
    cases=[('A',(0,None,0),(0,0)),('B',(None,0,None),(1,0)),
           ('C',(0,None,0),(2,0)),('stale',(0,None,0),(1,0)),('empty',(0,None,0),None)]
    for name,cur,q in cases:
        tab=(cur,(q,)+(None,)*5);J=C.encode(tab)
        K,_,data=C.dispatch(J,0)
        L,_,olddata=F.feedback(J,0)
        ck(K==L,'identical exact endpoint to old linear dispatcher')
        st=base.ref.old.seed(J);initial=st.names();retired=[];created=[]
        for raw in data['word']:
            st,_,delta=base.ref.old.raw_step(st,raw,C.H)
            retired.extend(v[0] for v in delta['retired'] if v[0] in C.targets)
            created.extend(v[0] for v in delta['created'] if v[0] in C.targets)
            target=None if data['outcome']<0 else C.targets[data['outcome']]
            for h,identity in initial.items():
                if h in C.targets and h!=target:ck(st.names().get(h)==identity,'unrelated source creation preserved at every primitive')
        ck(st.matching==K,'annotated trace uses the same original matching kernel')
        ck(retired==([] if data['outcome']<0 else [C.targets[data['outcome']]]) and not created,'exact minimum source disturbance')
        records.append(dict(name=name,commands=data['commands'],feedback=data['reads'],
                            parent_commands=olddata['commands'],parent_feedback=olddata['feedback_reads'],
                            observations=data['observations'],source_retired=retired))
    return dict(mode='costs',examples=records,**C.counters())


def theory_checks():
    """Static compiler/planning checks; not counted as scientific BRC executions."""
    rows=[]
    for d in range(1,65):
        tree=tree_for(d);seen={};worst=0
        for label in tuple(range(d))+(-1,):
            ix=0;bits=[]
            while not tree[ix].leaf:
                n=tree[ix];b=label in n.group;bits.append(b);ix=n.yes if b else n.no
            ck(tree[ix].remaining==(label,),'tree distinguishes every action outcome')
            ck(tuple(bits) not in seen,'each complete transcript has unique meaning');seen[tuple(bits)]=label
            worst=max(worst,len(bits))
        ck(worst==d.bit_length(),'minimum binary outcome-identification depth reached')
        rows.append(dict(targets=d,outcomes=d+1,worst_binary_feedback=worst))
    # For four outcome labels every depth-2 full decision tree must split 2/2.
    # Restrict to positive subset tests, inherited cost 4*M*|S|+9, exact Boolean
    # result normalization (4 commands on a target-labelled false leaf) and commit.
    labels=(0,1,2,-1);trees=[];M=7
    for root in combinations((0,1,2),2):
        other=tuple(x for x in labels if x not in root)
        for yes_test in combinations(root,1):
            no_test=tuple(x for x in other if x>=0)
            paths=[]
            for lab in labels:
                first=lab in root;group=yes_test if first else no_test
                last=lab in group
                cost=4*M*(len(root)+len(group))+18
                if lab>=0:cost+=2+(0 if last else 4)
                paths.append(cost)
            trees.append(dict(root=root,second_yes=yes_test,second_no=no_test,
                              costs=paths,worst=max(paths)))
    ck(len(trees)==6 and all(t['worst']==108 for t in trees),'exact 2-query compiler class minimax is 108')
    return dict(mode='theory',finite_tree_checks=rows,two_feedback_trees=trees,assertions=CHECKS)


def failures():
    C=Compiler(slots=1);tab=((None,0,None),((1,0),));J=C.encode(tab)
    K,_,data=C.dispatch(J,0)
    ck(data['observations'][0]['answer'] and not data['observations'][1]['answer'],'B is established by positive group and negative A')
    # Drop only the four result-normalization commands; still execute commit B.
    words=tuple(x for obs in data['observations'] for x in C.queries[0,obs['node']])+C.commit(1)
    bad,_,trace=C.runword(J,words,True)
    ck(C.decode(bad)[0]==C.decode(K)[0] and C.observe_result(bad)==False,'target deleted but answer wrongly remains false without normalization')
    # A false group observation does not by itself establish invalidity.
    tc=((0,None,0),((2,0),));jc=C.encode(tc)
    first,_,_=C.runword(jc,C.queries[0,0]);ck(not C.observe_result(first),'valid C answers no to AB')
    good,_,d=C.dispatch(jc,0);ck(C.observe_result(good) and C.targets[2] not in good,'remaining C query resolves the negative group')
    # Stable-prefix knowledge is required: B was true, then a complete writer
    # destroys and recreates B. A is still false; stale group knowledge picks B.
    old=C.encode(tab);checked,_,_=C.runword(old,C.queries[0,0]);ck(C.observe_result(checked),'positive AB result was genuine')
    changed,_,_=C.run(checked,('release',1));changed,_,_=C.run(changed,('reserve',1))
    ck(not base.expected(C,C.decode(changed)[0],('valid',0))[1],'request became stale during unprotected gap')
    second_node=C.tree[0].yes
    checked2,_,_=C.runword(changed,C.queries[0,second_node]);ck(not C.observe_result(checked2),'A negative still holds')
    leaf=C.tree[second_node].no;final,_,_=C.runword(checked2,C.leaf_words[leaf])
    ck(C.targets[1] not in final and C.observe_result(final),'unprotected stale prefix deletes new B')
    # Query domain only excludes invalid as an action target, not as a live
    # representation. Repeatedly finding no A/B must not default to C.
    invalid=((0,None,0),((1,0),));ji=C.encode(invalid)
    correct,_,di=C.dispatch(ji,0);ck(di['outcome']==-1 and C.targets[2] in correct,'invalid outcome explicitly retained')
    return dict(mode='failures',omitted_normalization=dict(input=J,correct=K,incorrect=bad,trace=trace),
                negative_group_valid_C=d['observations'],race=dict(after_recreation=changed,end=final),
                invalid_transcript=di['observations'],**C.counters())


def omissions():
    C=Compiler(slots=1);rows=[]
    cases=[('A',((0,None,0),((0,0),))),('B',((None,0,None),((1,0),))),
           ('C',((0,None,0),((2,0),))),('none',((0,None,0),((1,0),)))]
    for name,tab in cases:
        for budget in (1,2):
            repeats=budget+1;J=C.encode(tab);want,_,normal=C.dispatch(J,0)
            frontier={(J,0,0,0,0):ONE};done={};states=edges=0
            # key J,node,phase(0=query/1=leaf),position,used
            while frontier:
                nxt={}
                for (state,node,phase,pos,used),mass in frontier.items():
                    w=C.queries[0,node] if phase==0 else C.leaf_words[node]
                    raw=w[pos//repeats];states+=1
                    for skip in range(2 if used<budget else 1):
                        after=state if skip else C._raw(state,raw)[0];C.uses+=1;edges+=1
                        phase2,node2,pos2=phase,node,pos+1;finished=False
                        if pos2==len(w)*repeats:
                            pos2=0
                            if phase==1:finished=True
                            else:
                                answer=C.observe_result(after);x=C.tree[node];node2=x.yes if answer else x.no
                                leaf=C.tree[node2]
                                if leaf.leaf:
                                    if leaf.remaining[0]<0:finished=True
                                    else:phase2=1
                        if finished:
                            ck(after==want,'protected adaptive actual-output route reaches exact endpoint')
                            key=used+skip;done[key]=r.merge(done.get(key,ZERO),r.serial(mass,ONE))
                        else:
                            key=(after,node2,phase2,pos2,used+skip)
                            nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
                frontier=nxt
            # Independent positional counts, static test combinatorics only.
            import math
            length=normal['commands']*repeats
            ck(all(done[k].count==math.comb(length,k) for k in range(budget+1)), 'all omission positions retained with CWM weights')
            rows.append(dict(case=name,budget=budget,commands=length,states=states,edges=edges,
                             CWM={str(k):e.cw(v) for k,v in done.items()}))
    return dict(mode='omissions',families=rows,**C.counters())

class DispatchRing(gate.PhaseRing):
    """Replace only the protected feedback business; phase is still read from gates."""
    def __init__(self,slots=1,actors=2,repeats=1):
        super().__init__(slots,actors,repeats)
        before=self.C
        self.C=Compiler(slots=slots)
        ck(self.C.H==before.H and self.C.members==before.members,'drop-in core with unchanged permissions')
    def word(self,i,pc,jobs):
        if pc.phase=='match':return self.C.queries[jobs[i][pc.job][1],pc.target]
        if pc.phase=='commit':return self.C.leaf_words[pc.target]
        return super().word(i,pc,jobs)
    def next(self,node,i,jobs,omit=False,check=True):
        pc=node.pcs[i]
        if pc.phase!='match':return super().next(node,i,jobs,omit,check)
        word=self.word(i,pc,jobs);raw=word[pc.pos//self.repeats];self.uses+=1
        if omit:after=node.J;ok=None;self.omissions+=1
        else:after,ok=self._raw(node.J,raw)
        nxt=replace(pc,pos=pc.pos+1)
        if nxt.pos==len(word)*self.repeats:
            bit=self.C.observe_result(after);test=self.C.tree[pc.target]
            chosen=test.yes if bit else test.no
            dst=self.C.tree[chosen]
            if dst.leaf:
                nxt=(self.begin(jobs[i],pc.job+1,pc.route) if dst.remaining[0]<0 else
                     gate.PC('commit',pc.job,chosen,route=pc.route))
            else:nxt=gate.PC('match',pc.job,chosen,route=pc.route)
        pcs=list(node.pcs);pcs[i]=nxt;out=gate.Node(after,tuple(pcs),node.turn)
        if check:self.invariant(out)
        return out,raw,ok,False


def ring_costs():
    rows=[]
    for phase in (0,1):
        for name,cur,q in [('A',(0,None,0),(0,0)),('B',(None,0,None),(1,0)),
                           ('C',(0,None,0),(2,0)),('stale',(0,None,0),(1,0))]:
            G=DispatchRing(6,2);tab=(cur,(q,)+(None,)*5);jobs=((('feedback',0),),())
            state=G.initial_node(tab,phase=phase);st=base.ref.old.seed(state.J)
            target=outcome(tab,0);keep={h:birth for h,birth in st.events if h in G.C.targets and (target<0 or h!=G.C.targets[target])}
            state,steps,grants=gate.complete(G,state,0,jobs,ann=[st,keep])
            ck(G.C.decode(G.core(state.J))==base.expected(G.C,tab,('execute',0)),'guarded full source and result')
            ck(gate.old.bit(state.J,G.lanes[0].reply)==(target>=0),'private reply contains business answer, not final branch sign')
            ck(state.pcs[0].route is None,'no persistent controller phase')
            rows.append(dict(case=name,phase=phase,steps=steps,members=G.members,candidates=len(G.H),grants=grants))
    return dict(mode='ring_costs',cases=rows,assertions=CHECKS,gate_assertions=gate.CHECKS)


def ring_finite(repeats=1,budget=0,case='execute_restart'):
    G=DispatchRing(1,2,repeats)
    table=((None,0,None),((1,0),)) if case.startswith('B_') else ((0,None,0),((0,0),))
    choices={'execute_restart':((('feedback',0),),(('release',1),('reserve',0))),
             'execute_execute':((('feedback',0),),(('feedback',0),)),
             'execute_bind':((('feedback',0),),(('bind',0,2),)),
             'B_execute_restart':((('feedback',0),),(('release',1),('reserve',1))),
             'B_execute_execute':((('feedback',0),),(('feedback',0),))}
    jobs=choices[case];start=G.initial_node(table)
    D={(start,0,()):ONE};terms={};states=edges=0
    while D:
        nxt={}
        for (node,used,grants),weight in D.items():
            states+=1
            if states>400000:raise RuntimeError('explicit graph budget reached')
            if all(q.phase in ('done','busy') for q in node.pcs):
                G.terminal(node,jobs,table,grants)
                key=(node,used,grants);terms[key]=r.merge(terms.get(key,ZERO),weight);continue
            for i,pc in enumerate(node.pcs):
                if pc.phase in ('done','busy'):continue
                for omit in range(2 if used<budget else 1):
                    nn,raw,ok,grant=G.next(node,i,jobs,omit=bool(omit));edges+=1
                    order=grants+((i,) if grant else ())
                    key=(nn,used+omit,order)
                    nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(weight,ONE))
        D=nxt
    masses={};orders=set()
    for (node,used,grants),mass in terms.items():
        masses[used]=r.merge(masses.get(used,ZERO),mass);orders.add(grants)
    ck(bool(terms),'all finite attempts terminate')
    return dict(mode='ring_finite',case=case,repeats=repeats,budget=budget,states=states,edges=edges,
                terminal_classes=len(terms),grant_orders=sorted(orders),CWM={str(k):e.cw(v) for k,v in masses.items()},
                original_kernel_cache_misses=G.calls,primitive_edges=G.uses,assertions=CHECKS,gate_assertions=gate.CHECKS)


def export():
    C=Compiler(slots=6);G=DispatchRing(6,2)
    return dict(scope='three targets, six request slots, complete-result feedback',
                tree=[vars(t) for t in C.tree],members=C.members,candidates=sorted(C.H),
                queries={str(k):v for k,v in C.queries.items()},leaf_words=C.leaf_words,
                ring=dict(members=G.members,candidates=len(G.H),entry=G.entry,phase_reads=G.phase_reads,
                          phase_clears=G.phase_clears,publish=G.publish,handoffs=G.handoffs))


def scaling():
    rows=[]
    for d in (1,2,3,4,7,15):
        H=tuple((3*t+1,3*t+2,3*t+3) for t in range(d))
        C=Compiler(H=H,slots=6);F=feedback.Compiler(H=H,slots=6)
        ck(C.H==F.H and C.members==F.members,'general-target implementation uses unchanged candidate pool')
        cases=[]
        # The same physical background realizes each valid target and invalidity.
        for label in tuple(range(d))+(-1,):
            q=(label,0) if label>=0 else (0,1)
            table=((0,)*d,(q,)+(None,)*5);J=C.encode(table)
            K,_,data=C.dispatch(J,0);L,_,olddata=F.feedback(J,0)
            ck(K==L,'scaled target execution exact original-kernel endpoint')
            ck(data['outcome']==label,'scaled query classification')
            ck(data['reads']<=d.bit_length(),'scaled optimal binary depth')
            cases.append(dict(label=label,steps=data['commands'],reads=data['reads'],old_steps=olddata['commands']))
        worst=max(x['steps'] for x in cases)
        if d>1 and d+1==1<<d.bit_length():
            ck(worst==4*C.colors*d+9*d.bit_length()+6,'power-of-two outcome exact worst primitive count')
        rows.append(dict(targets=d,members=C.members,candidates=len(C.H),max_feedback=max(x['reads'] for x in cases),
                         worst_steps=worst,old_worst=max(x['old_steps'] for x in cases),cases=cases,
                         original_kernel_cache_misses=C.calls,original_command_uses=C.uses))
    return dict(mode='scaling',rows=rows,assertions=CHECKS)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['audit','costs','theory','failures','omissions','ring_costs','ring_finite','programs','scaling'])
    parser.add_argument('--slots',type=int,default=2);parser.add_argument('--repeats',type=int,default=1)
    parser.add_argument('--budget',type=int,default=0);parser.add_argument('--case',default='execute_restart');parser.add_argument('--out')
    a=parser.parse_args()
    if a.mode=='audit':ans=audit(a.slots)
    elif a.mode=='costs':ans=costs_and_births()
    elif a.mode=='theory':ans=theory_checks()
    elif a.mode=='failures':ans=failures()
    elif a.mode=='omissions':ans=omissions()
    elif a.mode=='ring_costs':ans=ring_costs()
    elif a.mode=='scaling':ans=scaling()
    elif a.mode=='ring_finite':ans=ring_finite(a.repeats,a.budget,a.case)
    else:ans=export()
    text=json.dumps(ans,ensure_ascii=False,indent=2)+'\n'
    if a.out:Path(a.out).write_text(text)
    else:print(text)
