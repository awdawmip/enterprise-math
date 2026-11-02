"""Exact dispatch planning; production transitions use inherited BRC words.

Planning handles finite specifications, integer call weights and command lengths.
Production dispatch consumes only complete Boolean results; the decoded source
and the ideal executor are used exclusively by checks.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
from fractions import Fraction
import argparse
import json
import sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_dispatch as parent
base,feedback=parent.base,parent.feedback
p,e,r=parent.p,parent.e,parent.r
ONE,ZERO=parent.ONE,parent.ZERO
CHECKS=0

def ck(ok:bool,label:str)->None:
    global CHECKS
    CHECKS+=1
    if not ok: raise AssertionError(label)

@dataclass(frozen=True)
class Plan:
    labels:tuple[int,...]
    group:tuple[int,...]=()
    yes:Plan|None=None
    no:Plan|None=None
    @property
    def leaf(self)->bool:return len(self.labels)==1


def terminal_cost(label:int,last:bool)->int:
    if label<0:
        if last: raise ValueError('invalid outcome cannot be reached on a true subset answer')
        return 0
    return 2+(0 if last else 4)


def flatten(plan:Plan)->tuple[parent.Test,...]:
    nodes=[]
    def put(x:Plan)->int:
        ix=len(nodes);nodes.append(parent.Test(x.labels))
        if not x.leaf:
            assert x.yes is not None and x.no is not None
            a,b=put(x.yes),put(x.no)
            nodes[ix]=parent.Test(x.labels,x.group,a,b)
        return ix
    put(plan)
    return tuple(nodes)


def path_specs(plan:Plan,colors:int)->dict[int,dict]:
    rows={}
    def visit(q:Plan,used:int,transcript:tuple,bit:bool):
        if q.leaf:
            lab=q.labels[0]
            rows[lab]=dict(commands=used+terminal_cost(lab,bit),reads=len(transcript),transcript=transcript)
        else:
            c=4*colors*len(q.group)+9
            visit(q.yes,used+c,transcript+((q.group,True),),True)
            visit(q.no,used+c,transcript+((q.group,False),),False)
    visit(plan,0,(),False)
    return rows


def balanced(labels:tuple[int,...])->Plan:
    if len(labels)==1:return Plan(labels)
    g=tuple(x for x in labels if x>=0)[:len(labels)//2]
    rest=tuple(x for x in labels if x not in g)
    return Plan(labels,g,balanced(g),balanced(rest))


def minimax_formula(d:int,colors:int)->int:
    if d<1 or colors<1:raise ValueError('positive counts required')
    return 4*colors*d+9*d.bit_length()+(2 if d&(d-1)==0 else 6)


@lru_cache(None)
def count_dp(k:int,invalid:bool,last:bool,depth:int,colors:int)->int:
    """Independent symmetric Bellman recurrence, no use of the closed form."""
    if k+int(invalid)==1:return terminal_cost(-1 if invalid else 0,last)
    if depth<=0:return 10**20
    return min(4*colors*s+9+max(count_dp(s,False,True,depth-1,colors),
                               count_dp(k-s,invalid,False,depth-1,colors))
               for s in range(1,k+1) if invalid or s<k)


def weighted_plan(weights:dict[int,int],colors:int,cap:int|None=None,
                  depth:int|None=None)->tuple[Plan,dict]:
    """Minimize exact weighted command sum, optionally with a worst-path cap.

    All labels, including zero-weight ones, must remain distinguishable.
    Compilation enumerates finite subsets. The original BRC runtime does not
    inspect weights, source labels or this planning recursion.
    """
    if colors<1 or len(weights)<2 or -1 not in weights:
        raise ValueError('need invalid label, at least one target, and positive colors')
    if set(weights)-{-1}!=set(range(len(weights)-1)):
        raise ValueError('targets must be contiguous nonnegative labels')
    if any(type(w) is not int or w<0 for w in weights.values()) or not sum(weights.values()):
        raise ValueError('nonnegative integer weights, positive total required')
    labels=tuple(range(len(weights)-1))+(-1,)
    maxdepth=len(labels)-1 if depth is None else depth
    @lru_cache(None)
    def solve(C:tuple[int,...],last:bool,budget:int|None,h:int):
        if len(C)==1:
            cost=terminal_cost(C[0],last)
            if budget is not None and cost>budget:return None
            return (weights[C[0]]*cost,cost,0,Plan(C))
        if h<=0 or (budget is not None and budget<0):return None
        best=None;valid=tuple(x for x in C if x>=0)
        for size in range(1,len(valid)+1):
            for S in combinations(valid,size):
                other=tuple(x for x in C if x not in S)
                if not other:continue
                cost=4*colors*size+9
                nextbudget=None if budget is None else budget-cost
                a=solve(S,True,nextbudget,h-1);b=solve(other,False,nextbudget,h-1)
                if a is None or b is None:continue
                result=(cost*sum(weights[x] for x in C)+a[0]+b[0],cost+max(a[1],b[1]),
                        1+max(a[2],b[2]),Plan(C,S,a[3],b[3]))
                if best is None or result[:3]<best[:3]:best=result
        return best
    ans=solve(labels,False,cap,maxdepth)
    if ans is None:raise ValueError('no exact dispatcher satisfies the specified cap/depth')
    return ans[3],dict(weighted_commands=ans[0],total_weight=sum(weights.values()),
                       mean_commands=str(Fraction(ans[0],sum(weights.values()))),
                       worst_commands=ans[1],max_feedback=ans[2],planner_states=solve.cache_info().currsize)


@lru_cache(None)
def all_plans(labels:tuple[int,...])->tuple[Plan,...]:
    """Exhaustive labelled trees for an independent small-domain certificate."""
    if len(labels)==1:return (Plan(labels),)
    out=[];valid=tuple(x for x in labels if x>=0)
    for size in range(1,len(valid)+1):
        for S in combinations(valid,size):
            rest=tuple(x for x in labels if x not in S)
            if not rest:continue
            for a in all_plans(S):
                for b in all_plans(rest):out.append(Plan(labels,S,a,b))
    return tuple(out)


class Compiler(parent.Compiler):
    def __init__(self,plan:Plan,H=base.H_DEFAULT,slots:int=2):
        super().__init__(H=H,slots=slots)
        if set(plan.labels)!=set(range(self.d))|{-1}:raise ValueError('plan target domain mismatch')
        self.plan=plan;self.tree=flatten(plan);self.queries={};self.leaf_words={}
        for i in range(slots):
            for k,node in enumerate(self.tree):
                if not node.leaf:self.queries[i,k]=self.compile_group(i,node.group)
        for k,node in enumerate(self.tree):
            if node.leaf:continue
            for bit,child in ((True,node.yes),(False,node.no)):
                dst=self.tree[child]
                if dst.leaf and dst.remaining[0]>=0:
                    fix=() if bit else tuple(self.clearout()+[p.add(h) for h in p.reg(self.out,1)])
                    self.leaf_words[child]=fix+self.commit(dst.remaining[0])
        for word in (*self.queries.values(),*self.leaf_words.values()):
            for raw in word:
                if raw[0]=='reserve':ck(tuple(raw[1]) in self.H,'new plan uses only inherited candidates')


def theory()->dict:
    checks=[]
    for M in (1,2,3,7,19):
        for d in range(1,129):
            want=minimax_formula(d,M)
            dp=count_dp(d,True,False,d,M)
            short=count_dp(d,True,False,d.bit_length(),M)
            actual=max(x['commands'] for x in path_specs(balanced(tuple(range(d))+(-1,)),M).values())
            ck(want==dp==short==actual,'closed form, unrestricted DP, minimum-depth DP and balanced tree agree')
        checks.append(dict(colors=M,targets_checked=list(range(1,129))))
    plans=all_plans((0,1,2,-1));scores=[]
    for pl in plans:
        spec=path_specs(pl,7)
        scores.append((pl,max(x['commands'] for x in spec.values()),max(x['reads'] for x in spec.values()),spec))
    cases=[]
    for weight in ({0:1,1:1,2:1,-1:1},{0:80,1:10,2:5,-1:5},{0:5,1:5,2:10,-1:80}):
        for cap in (108,110,113,None):
            pl,info=weighted_plan(weight,7,cap)
            feasible=[s for s in scores if cap is None or s[1]<=cap]
            target=min(sum(weight[i]*s[3][i]['commands'] for i in weight) for s in feasible)
            ck(info['weighted_commands']==target,'weighted Bellman value matches every labelled tree')
            cases.append(dict(weights=weight,cap=cap,**info,paths=path_specs(pl,7)))
    frontier=[]
    weight={0:80,1:10,2:5,-1:5};best=10**30
    for w in sorted({s[1] for s in scores}):
        eligible=[s for s in scores if s[1]<=w]
        value=min(sum(weight[i]*s[3][i]['commands'] for i in weight) for s in eligible)
        if value<best:
            frontier.append(dict(worst_cap=w,weighted_commands=value,mean=str(Fraction(value,100))));best=value
    return dict(mode='theory',checks=checks,all_four_outcome_trees=len(plans),weighted_cases=cases,
                pareto_80_10_5_5=frontier,assertions=CHECKS,static_planning_not_native_execution=True)


def modes_for(slots:int):
    M=slots+1;w={0:80,1:10,2:5,-1:5}
    ordinary=balanced((0,1,2,-1));mean,_=weighted_plan(w,M)
    capped,_=weighted_plan(w,M,minimax_formula(3,M))
    return [('balanced',ordinary),('weighted_mean',mean),('weighted_capped',capped)]


def audit(slots:int=2)->dict:
    out=[]
    for name,plan in modes_for(slots):
        C=Compiler(plan,slots=slots);old=parent.Compiler(slots=slots)
        ck(C.members==old.members and C.H==old.H,'unchanged member inventory and candidate library')
        domain=base.domain(C);mass=ZERO;cases=0;queries=0;spec=path_specs(plan,C.colors)
        for index,table in enumerate(domain):
            J=C.encode(table,(None,0,1)[index%3])
            for i in range(slots):
                K,wm,data=C.dispatch(J,i);expected=base.expected(C,table,('execute',i));label=parent.outcome(table,i)
                ck(C.decode(K)==expected,'exact source, references, response and cleaned workspace')
                ck(data['outcome']==label,'outcome identification correct')
                ck(data['commands']==spec[label]['commands'] and data['reads']==spec[label]['reads'],'static cost equals executed word')
                releases={a for a in C.U if p.one(a) in data['word']}
                ck(releases==(set() if label<0 else {min(C.targets[label])}),'zero or one actual source release')
                mass=r.merge(mass,wm);cases+=1
                for node,test in enumerate(C.tree):
                    if test.leaf:continue
                    T,_,_=C.runword(J,C.queries[i,node])
                    ck(T==C.encode(table,label in test.group),'all selected queries preserve the full source and report set membership')
                    queries+=1
        out.append(dict(name=name,domain=len(domain),dispatch_cases=cases,query_cases=queries,
                        CWM=e.cw(mass),paths=spec,kernel_cache_misses=C.calls,command_uses=C.uses,
                        members=C.members,candidates=len(C.H)))
    return dict(mode='audit',slots=slots,plans=out,assertions=CHECKS)


def actual_costs()->dict:
    rows=[]
    for name,plan in modes_for(6):
        C=Compiler(plan,slots=6);mass=ZERO;wm_sum=0;records=[]
        for label,w in ((0,80),(1,10),(2,5),(-1,5)):
            cur=(None,0,None) if label==1 else (0,None,0)
            q=(label,0) if label>=0 else (1,0)
            table=(cur,(q,)+(None,)*5);J=C.encode(table)
            K,wm,data=C.dispatch(J,0)
            ck(C.decode(K)==base.expected(C,table,('execute',0)),'scenario execution is correct on all outcomes')
            state=base.ref.old.seed(J);initial=state.names();retired=[];created=[]
            for raw in data['word']:
                state,_,delta=base.ref.old.raw_step(state,raw,C.H)
                retired.extend(x[0] for x in delta['retired'] if x[0] in C.targets)
                created.extend(x[0] for x in delta['created'] if x[0] in C.targets)
                for h,identity in initial.items():
                    if h in C.targets and (label<0 or h!=C.targets[label]):
                        ck(state.names().get(h)==identity,'unaffected source birth preserved at each actual primitive')
            ck(state.matching==K and not created,'same kernel trace and no source reconstruction')
            ck(retired==([] if label<0 else [C.targets[label]]),'exact minimum source retirement')
            for _ in range(w):mass=r.merge(mass,wm)
            wm_sum+=w*data['commands']
            records.append(dict(outcome=label,weight=w,commands=data['commands'],reads=data['reads'],
                                observations=data['observations'],retired=retired))
        ck(mass.count==100 and mass.total==100,'CWM retains the 100 declared workload labels')
        rows.append(dict(plan=name,cases=records,weighted_commands=wm_sum,mean=str(Fraction(wm_sum,100)),
                         scenario_CWM=e.cw(mass),members=C.members,candidates=len(C.H),kernel_calls=C.calls,
                         command_uses=C.uses))
    return dict(mode='actual_costs',weights_are_declared_scenario_not_empirical_frequencies=True,
                plans=rows,assertions=CHECKS)


class PlannedRing(parent.DispatchRing):
    def __init__(self,slots=1,actors=2,repeats=1,kind='mean'):
        super().__init__(slots,actors,repeats)
        old=self.C
        w={0:80,1:10,2:5,-1:5}
        cap=None if kind=='mean' else minimax_formula(3,slots+1)
        plan,_=weighted_plan(w,slots+1,cap)
        self.C=Compiler(plan,slots=slots)
        ck(self.C.H==old.H and self.C.members==old.members,'protected wrapper still uses identical permissions')


def ring_costs()->dict:
    rows=[]
    for kind in ('mean','capped'):
        for phase in (0,1):
            for label in (0,1,2,-1):
                G=PlannedRing(6,2,kind=kind)
                cur=(None,0,None) if label==1 else (0,None,0)
                q=(label,0) if label>=0 else (1,0)
                table=(cur,(q,)+(None,)*5);jobs=((('feedback',0),),())
                node=G.initial_node(table,phase=phase)
                st=base.ref.old.seed(node.J)
                keep={h:b for h,b in st.events if h in G.C.targets and (label<0 or h!=G.C.targets[label])}
                node,steps,grants=parent.gate.complete(G,node,0,jobs,ann=[st,keep])
                ck(G.C.decode(G.core(node.J))==base.expected(G.C,table,('execute',0)),'wrapped source and complete response')
                ck(parent.gate.old.bit(node.J,G.lanes[0].reply)==(label>=0),'private answer is business outcome')
                ck(node.pcs[0].route is None,'phase remains gate-derived, no persistent route')
                rows.append(dict(kind=kind,phase=phase,label=label,commands=steps,grants=grants,
                                 members=G.members,candidates=len(G.H)))
    return dict(mode='ring_costs',rows=rows,assertions=CHECKS)


def ring_graph(repeats:int=3,budget:int=2)->dict:
    """Actual primitive-level interleavings with shared omission budget."""
    G=PlannedRing(1,2,repeats);table=((0,None,0),((0,0),))
    jobs=((('feedback',0),),(('release',1),('reserve',0)))
    start=G.initial_node(table);front={(start,0,()):ONE};terms={};states=edges=0
    while front:
        nxt={}
        for (node,used,order),mass in front.items():
            states+=1
            if states>200000:raise RuntimeError('finite graph budget exceeded')
            if all(q.phase in ('done','busy') for q in node.pcs):
                G.terminal(node,jobs,table,order)
                key=(node,used,order);terms[key]=r.merge(terms.get(key,ZERO),mass);continue
            for i,pc in enumerate(node.pcs):
                if pc.phase in ('done','busy'):continue
                for skip in range(2 if used<budget else 1):
                    nn,raw,ok,grant=G.next(node,i,jobs,omit=bool(skip));edges+=1
                    key=(nn,used+skip,order+((i,) if grant else ()))
                    nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
        front=nxt
    totals={};orders=set()
    for (node,used,order),mass in terms.items():
        totals[used]=r.merge(totals.get(used,ZERO),mass);orders.add(order)
    ck(bool(terms),'finite protected attempts reach exact checked endpoints')
    return dict(mode='ring_graph',repeats=repeats,total_omission_budget=budget,states=states,edges=edges,
                terminal_classes=len(terms),orders=sorted(orders),CWM={str(k):e.cw(v) for k,v in totals.items()},
                original_kernel_cache_misses=G.calls,primitive_transition_uses=G.uses,assertions=CHECKS,
                parent_invariant_assertions=parent.gate.CHECKS)


def scaling()->dict:
    rows=[]
    for d in (1,2,3,4,5,6,7,8,15,16,31):
        H=tuple((3*t+1,3*t+2,3*t+3) for t in range(d))
        plan=balanced(tuple(range(d))+(-1,));C=Compiler(plan,H=H,slots=6)
        costs=[]
        for lab in tuple(range(d))+(-1,):
            q=(lab,0) if lab>=0 else (0,1);table=((0,)*d,(q,)+(None,)*5)
            J=C.encode(table);K,wm,data=C.dispatch(J,0)
            ck(C.decode(K)==base.expected(C,table,('execute',0)),'general-size primitive dispatch exact')
            costs.append(data['commands'])
        ck(max(costs)==minimax_formula(d,C.colors),'formula attained in actual BRC execution')
        rows.append(dict(targets=d,executed_outcomes=d+1,worst_commands=max(costs),costs=costs,
                         kernel_cache_misses=C.calls,command_uses=C.uses,members=C.members,candidates=len(C.H)))
    return dict(mode='scaling',rows=rows,assertions=CHECKS)


def export()->dict:
    out=[]
    for name,plan in modes_for(6):
        C=Compiler(plan,slots=6)
        out.append(dict(name=name,tree=[vars(n) for n in C.tree],paths=path_specs(plan,C.colors),
                        queries={str(k):v for k,v in C.queries.items()},leaf_words=C.leaf_words,
                        members=C.members,candidates=sorted(C.H)))
    return dict(mode='programs',plans=out)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['theory','audit','costs','ring_costs','ring_graph','scaling','programs'])
    ap.add_argument('--slots',type=int,default=2);ap.add_argument('--out',required=True)
    a=ap.parse_args()
    ans={'theory':theory,'audit':lambda:audit(a.slots),'costs':actual_costs,'ring_costs':ring_costs,
         'ring_graph':ring_graph,'scaling':scaling,'programs':export}[a.mode]()
    Path(a.out).write_text(json.dumps(ans,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in ans.items() if k not in ('rows','plans','checks','weighted_cases')},ensure_ascii=False)[:1200])
