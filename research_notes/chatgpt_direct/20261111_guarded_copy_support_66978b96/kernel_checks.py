"""Real original BRC branch execution. The physical table is an audit oracle only."""
from pathlib import Path
from collections import Counter
from itertools import product
from dataclasses import replace, dataclass
import importlib.util, json, argparse, sys

BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE.parent/'copylife'))
spec=importlib.util.spec_from_file_location('parent_copy_kernel', BASE.parent/'copylife'/'kernel_checks.py')
prior=importlib.util.module_from_spec(spec);sys.modules[spec.name]=prior;spec.loader.exec_module(prior)
core=prior.core
COUNT=0

def ck(cond,msg):
    global COUNT
    COUNT+=1
    if not cond:raise AssertionError(msg)

@dataclass(frozen=True)
class Join:
    # Pure suffix control has no physical table or access to the actual route.
    full_key:int
    guard:bool|None
    def possibilities(self):
        if self.guard is None:return {0,self.full_key}
        return {self.full_key if self.guard else 0}

def joined_prefix(p, mode):
    p.drop(2)
    g=bool(p.C.observe_result(p.J))
    ck(g==p.events[-1]['present'],'branch test is the actual business reply')
    d=2 if g else 1
    key=p.copy(d,0)
    p.drop(0);p.drop(1)
    # Explicit projection; forgetting the guard also erases destination and
    # derived locations. A caller who retains them has not forgotten the branch.
    return Join(key,g if mode=='remember' else None), g,d

def suffix(p,j,T,*,recover=False):
    s=j.possibilities();reads=0;keys=[];latest=0;cum=[]
    if recover and len(s)==2:
        # The set is {0,k}; a set bit distinguishes them in one original probe.
        bit=(j.full_key & -j.full_key).bit_length()-1
        s={j.full_key if p.probe(2,bit) else 0};reads+=1
    for step in range(T):
        K=min((k for k in range(1,5) if k not in s and k!=latest),key=lambda k:(prior.key_cost(k,2),k))
        before=p.probes
        ck(p.round(0,0,K)==K and p.probes==before,'real controller follows projected certificate and makes no hidden query')
        keys.append(K);latest=K;cum.append(p.cost)
    return keys,cum,reads

def summarize(p):
    return [dict(op=e['op'],reply=e.get('delivered') if e.get('delivered') is not None else e.get('present',e.get('key',e.get('answer'))),cumulative=e['cumulative']) for e in p.events]

def branch_rows():
    C=core.prior.Compiler(slots=3);rows=[]
    for g in [False,True]:
        for mode,rec in [('remember',False),('forget',False),('forget',True)]:
            x=(2,3,int(g));p=prior.Physical(C,x);j,b,d=joined_prefix(p,mode)
            codes=p.codes();prefix=p.cost
            ck(codes==(0,0,2*int(g)) and prefix==82 and b==g,'postdominator maps and equal actual prefix charge')
            negative=None
            if mode=='remember' and g:
                # Optimistically intersecting blockers would choose 2 on this branch.
                negative=p.negative_fork(0,2,2)
            keys,cs,_=suffix(p,j,6,recover=rec)
            rows.append(dict(guard=g,mode=mode,recover=rec,destination=d,prefix=prefix,
                incoming_join=sorted(j.possibilities()),join_slots=codes,keys=keys,
                cumulative=cs,extra_bit_reads=p.probes,negative_branch=negative,actual_words=summarize(p)))
    for g in [False,True]:
        remember,blind,repair=[r for r in rows if r['guard']==g]
        for i in range(6):
            T=i+1
            ck(blind['cumulative'][i]-remember['cumulative'][i]==(0 if g else 2*T),'blind avoidance overhead')
            ck(repair['cumulative'][i]-remember['cumulative'][i]==8,'one restoring observation')
            ck(min(repair['cumulative'][i],blind['cumulative'][i])-remember['cumulative'][i]==(0 if g else min(8,2*T)),'exact per-preparation overhead')
    return rows

def finite_sweep():
    C=core.prior.Compiler(slots=3);by=Counter();worst_by={};hist=Counter()
    # All three initial full identities vary independently over the legal 0..12.
    for x in product(range(13),repeat=3):
        p=prior.Physical(C,x);j,g,d=joined_prefix(p,'remember');keys,cs,n=suffix(p,j,1)
        key=keys[0];math=min(((prior.key_cost(k,2),k) for k in range(1,5) if not(g and k==x[0])))
        gq=lambda k: 37 if k==0 else 38+k.bit_count()+4*(1-((k>>3)&1))
        ck((prior.key_cost(key,2),key)==math and not p.probes,'physical optimum with no paid vacancy reads')
        ck(p.cost==39+gq(x[0])+62+math[0],'actual word including input-dependent copy length')
        by[g]+=1;hist[p.cost]+=1
        if str(g) not in worst_by or p.cost>worst_by[str(g)]['total']:
            worst_by[str(g)]=dict(x=x,total=p.cost,selected=key)
    return dict(old_domain='all independent 0..12 including empty',runs=sum(by.values()),false=by[False],true=by[True],cost_histogram=hist,worst=worst_by)

def peek_case(m):
    C=core.prior.Compiler(slots=2);rows=[]
    for v in (0,1):
        for peek in (False,True):
            p=prior.Physical(C,(2,v));p.drop(0)
            for b in (1,2,3):ck(p.probe(1,b)==0,'genuine common incoming certificate for {0,1}')
            prep=p.cost;old_low=p.probe(1,0) if peek else None
            k1=6 if peek and old_low else 4
            ck(p.round(1,0,k1)==k1,'first B choices valid on common state')
            p.drop(1);guard=bool(C.observe_result(p.J))
            k2=6 if k1==4 else 4
            ck(p.round(1,1,k2)==k2,'complementary chosen B key')
            dst,src=(0,1) if guard else (1,0)
            for i in range(m):
                kop=p.copy(dst,src)
                ck(kop==(k2 if guard else k1),'destinations and complete physical response match true guard')
            cp=k2 if guard else k1
            adjusted=p.cost-prep
            ck(adjusted==153+8*int(peek)+(43 if cp==4 else 44)*m,'actual adaptive experiment full accounting')
            rows.append(dict(old=(2,v),roles_public_seed='drop0 plus three real eight-command probes',paid_entry=prep,
                 preobserve=peek,guard=guard,chosen=(k1,k2),copy_src=src,copy_dst=dst,copied=cp,
                 body=adjusted,total=p.cost,extra_reads_in_body=int(peek)))
    return rows


def parity_chain():
    C=core.prior.Compiler(slots=5);rows=[]
    for bits in product(range(2),repeat=2):
        for mode in ('retain_parity','forget_avoid','forget_read'):
            x=(4,1,0,*bits);p=prior.Physical(C,x)
            xkey=p.copy(2,0);ykey=p.copy(2,1);p.drop(2);prep=p.cost
            ck((xkey,ykey)==(4,1),'data identities originated from genuine copies')
            parity=0;traject=[]
            for src in (3,4):
                p.drop(src);reply=int(C.observe_result(p.J));parity^=reply
                if reply: acts=((2,0),(0,1),(1,2))
                else: acts=((2,0),(0,2),(2,0))
                for d,s in acts:p.copy(d,s)
                p.drop(2);traject.append(dict(guard=reply,cumulative=p.cost))
            p.drop(1);pre=p.cost
            ck(pre-prep==382 and prep==118,'fixed common body of both branching routes; all actual lengths')
            # Only the retained bit, or the new real observation, or the joint
            # set {1,4} may be passed downstream. No derived original action
            # transcript is lent to the deliberately forgotten interface.
            if mode=='retain_parity':may_have_4=(parity==0)
            elif mode=='forget_read':may_have_4=(p.probe(0,2)==1)
            else:may_have_4=True
            chosen=5 if may_have_4 else 4;costs=[]
            for i in range(5):
                old=p.probes
                ck(p.round(0,2,chosen)==chosen and p.probes==old,'one allowed certified key selected with no hidden probes')
                p.drop(2);costs.append(p.cost)
            rows.append(dict(guards=bits,mode=mode,prep=prep,all_prefix=pre,event_checks=traject,
                             holder_at_join=(4 if parity==0 else 1),key=chosen,totals=costs,additional_reads=p.probes))
        a,b,c=rows[-3:];odd=sum(bits)%2
        ck(all(y-x==2*(i+1)*odd and z-x==8 for i,(x,y,z) in enumerate(zip(a['totals'],b['totals'],c['totals']))),'parity recovery and avoiding gap on all four actual branches')
    return rows


def real_policy_sweep():
    imp=importlib.util.spec_from_file_location('branch_oracle_for_kernel', BASE/'oracle.py')
    logic=importlib.util.module_from_spec(imp);sys.modules[imp.name]=logic;imp.loader.exec_module(logic)
    C=core.prior.Compiler(slots=2);rows=[]
    for kind in ('first_copy_key','first_chosen_key'):
        P=logic.Program(2)
        if kind=='first_copy_key':
            end=P.add(('round',1,0));erase=P.add(('drop',0),end)
            left=P.add(('copy',1,0),erase);right=P.add(('copy',0,1),erase)
            l=P.add(('round',0,0),left);r=P.add(('round',0,0),right)
            top=P.add(('copy',1,0),l,[(k,r) for k in range(1,10,2)])
        else:
            end=P.add(('round',0,1));erase=P.add(('drop',0),end)
            left=P.add(('copy',1,0),erase);right=P.add(('copy',0,1),erase)
            top=P.add(('round',1,0),left,[(4,right)])
        planner=logic.Domains(P);wv=logic.Worlds(P).value()
        ck(wv==planner.value(),'independent Cartesian physical oracle gives same minimax')
        hist=Counter();arms=Counter();worst=None;first_by_arm={}
        for ini in product(range(10),repeat=2):
            p=prior.Physical(C,ini);st=planner.start;route=[];start_answer=None
            while st[0]>=0:
                pc=st[0];e=P.nodes[pc][0];act=planner.dp(*st)[1]
                if act[0]=='read':obs=p.probe(act[1],act[2])
                else:
                    if e[0]=='round':
                        ck(not p.ledger.blocks(act[1]),'original typed ledger affirms planner action')
                        obs=p.round(e[1],e[2],act[1]);ck(obs==act[1],'original binding delivers the selected key')
                    elif e[0]=='copy':
                        obs=p.copy(e[1],e[2])
                        if e[1]==e[2]:obs=int(C.observe_result(p.J))
                    elif e[0]=='drop':p.drop(e[1]);obs=int(C.observe_result(p.J))
                    elif e[0]=='bit':obs=p.probe(e[1],e[2])
                    else:raise AssertionError(e)
                    route.append(dict(pc=pc,event=e,answer=obs))
                    if pc==top:start_answer=obs
                st=planner.advance(st,act,obs)
            projected,_,endtab=planner.replay(ini)
            ck((projected,endtab)==(p.cost,p.codes()),'physical execution matches independent compiled-policy simulation')
            dest=next(v['event'][1] for v in route[1:] if v['event'][0]=='copy')
            arms[dest]+=1;hist[p.cost]+=1
            item=dict(input=ini,actual_guard=start_answer,pc_route=route,additional_reads=p.probes,total=p.cost)
            if dest not in first_by_arm:first_by_arm[dest]=item
            if worst is None or p.cost>worst['total']:worst=item
        ck(len(arms)==2 and max(hist)==wv and sum(hist.values())==100,'both physically reachable arms and minimax attained')
        rows.append(dict(guard=kind,original_inputs=100,graph=P.nodes,source_domain_minimax=planner.value(),explicit_world_minimax=wv,physical_max=max(hist),histogram=hist,selected_destinations=arms,example_by_arm=first_by_arm,worst=worst))
    return rows


def endogenous_leaf():
    C=core.prior.Compiler(slots=2);out=[]
    for key in (2,3):
        P=prior.Physical(C,(0,0))
        for i in (0,1):ck(P.probe(i,1)==0,'same control observations exclude 2 and 3')
        obs=P.round(0,0,key);prefix=P.cost;run=(obs==2)
        if run:ck(P.copy(1,0)==obs,'chose the key that actually triggers copy')
        out.append(dict(chosen=obs,entered_copy=run,cost_before_guard=prefix,completed=P.cost,read_count=P.probes))
    ck([v['completed'] for v in out]==[123,82],'gated leaf constrains achievable primitive costs')
    return out

def protected():
    import check_batch_integration as integration
    gate,m,p=integration.gate,core.directed.m,core.directed.p
    class Ring(integration.BatchRing):
        def begin(self,jobs,k,route):
            if k<len(jobs) and jobs[k][0]=='adaptive':return gate.PC('adaptive',k,route=route)
            return super().begin(jobs,k,route)
    jobs=((('adaptive',),),(('copy',1,0),));rows=[]
    for phase,g in product(range(2),(False,True)):
        G=Ring(slots=3);C=G.C;au=prior.Physical(C,(2,3,int(g)),capture=True)
        node=G.initial_node(au.table,phase=phase);entry=0
        while node.pcs[0].phase!='adaptive':node,_,_,_=G.next(node,0,jobs);entry+=1
        held=node;au.J=held.J;au.extras=tuple(h for h in held.J if h not in C.H)
        j,bit,d=joined_prefix(au,'remember');ks,_,_=suffix(au,j,1)
        ck(bit==g and len(au.states)==au.cost==len(au.raw_words),'held original full word and branch')
        states=[held.J]+au.states
        for st in states:
            ck(G.lock(0) in st,'lock still belongs to adaptive action')
            blocked,n,grants=gate.complete(G,replace(held,J=st),1,jobs)
            ck(grants==() and blocked.pcs[1].phase=='busy' and tuple(h for h in blocked.J if h in C.H)==tuple(h for h in st if h in C.H),'competing original copy refused without touching any kernel relation')
        pcs=list(held.pcs);pcs[0]=G.begin(jobs[0],held.pcs[0].job+1,held.pcs[0].route)
        n=replace(held,J=au.J,pcs=tuple(pcs));answer=bool(C.observe_result(au.J));n,ext,more=gate.complete(G,n,0,jobs)
        ck(not more and gate.old.bit(n.J,G.lanes[0].reply)==answer,'private return')
        n,ct,grants=gate.complete(G,n,1,jobs);ck(grants==(1,),'competitor can acquire after handoff')
        aft,ans,cache=core.old.expected_selected(C,au.table,au.cache,jobs[1][0],{});want=C.encode(aft,ans,cache)
        for a,lane in enumerate(G.lanes):
            want=m.canon(want+p.reg(lane.admitted,1)+p.reg(lane.reply,int((answer,ans)[a])))
            if a!=n.turn:want=m.canon(want+(G.gate_pair[a][phase^1],))
        ck(want==n.J,'full physical state, gates and private replies after handoff')
        checks=0
        if phase==0:
            for i,cmd in enumerate(au.raw_words):
                cur=states[i]
                for rep in (1,2):
                    cur,_=C._raw(cur,cmd)
                    ck(cur==states[i+1],'single or repeated physical copy of each primitive gives reference boundary')
                    checks+=1
        rows.append(dict(phase=phase,guard=g,keys=ks,destination=d,body=au.cost,gate_entry=entry,gate_exit=ext,total=entry+au.cost+ext,refused_at_boundaries=len(states),competitor_admitted_commands=ct,duplicate_local_equalities=checks,members=G.members,candidates=len(G.H)))
    return rows

def main():
    arg=argparse.ArgumentParser();arg.add_argument('--out',type=Path,default=BASE/'kernel_results.json');a=arg.parse_args()
    o=dict(status='PASS',word_unit='physical original commands',dependent_copy=branch_rows(),sweep=finite_sweep(),preobserve={m:peek_case(m) for m in (8,9,16)},parity_chain=parity_chain(),exact_policy=real_policy_sweep(),endogenous_leaf=endogenous_leaf(),protected=protected())
    o['assertions_here']=COUNT;o['inherited_kernel_assertions_in_this_run']=prior.CHECKS
    a.out.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n');print(o['sweep'],o['assertions_here'])
if __name__=='__main__':main()
