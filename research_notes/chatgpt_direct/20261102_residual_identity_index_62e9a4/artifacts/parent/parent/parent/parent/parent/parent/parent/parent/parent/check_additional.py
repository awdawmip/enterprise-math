"""Additional generic layouts, preservation planning, and repeated use checks."""
from pathlib import Path
import argparse,json
import check_selective as q

def plan(H,S,protected=()):
    """Choose a constant release set from declared candidates, never live data.

Priority: fewer candidate relations may be disturbed; then fewer suffix calls.
This minimizes that exact finite compile-time objective, not total physical cost.
"""
    banned=set().union(*(set(H[t]) for t in protected)) if protected else set()
    Rs=[R for R in q.minimal_transversals(H,S) if not set(R)&banned]
    if not Rs:
        witness=next(t for t in S if not (set(H[t])-banned))
        return dict(feasible=False,covered_target=witness)
    def cost(R):
        N=tuple(t for t,h in enumerate(H) if set(h)&set(R))
        return len(N),len(R)+3*len(N),R
    R=min(Rs,key=cost)
    return dict(feasible=True,releases=R,disturbance_family=tuple(t for t,h in enumerate(H) if set(h)&set(R)),objective=cost(R))

def generic():
    families=(
        ((1,2,3),(4,5,6)),
        ((1,2,3),(1,4,5),(1,6,7)),
        ((1,2,3),(1,4,5),(2,4,6)),
        ((1,2,3),(1,4,5),(1,6,7),(2,4,6),(2,5,7),(3,4,7),(3,5,6)),
    )
    rows=[];calls=uses=transitions=0
    for H0 in families:
        H=tuple(sorted(H0));sets=tuple((t,) for t in range(len(H)))+(tuple(range(len(H))),)
        specs=tuple((S,tuple(plan(H,S)['releases'])) for S in sets)
        C=q.Compiler(H,slots=1,specs=specs);dom=q.base.domain(C)
        for tab in dom:
            J=C.encode(tab)
            for S,R in specs:
                op=('execute_scope',0,S,R);K,_,_=C.run(J,op)
                q.ck(C.decode(K)==q.expected(C,tab,op),'General candidate-family exact contract')
                transitions+=1
        rows.append(dict(targets=H,domain=len(dom),specs=specs,members=C.members,candidates=len(C.H)))
        calls+=C.calls;uses+=C.uses
    H=q.base.H_DEFAULT
    q.ck(plan(H,(1,),(0,2))==dict(feasible=False,covered_target=1),'Planner returns exact incompatible preservation witness')
    q.ck(plan(H,(0,),(1,2))['disturbance_family']==(0,),'A has a preservation-compatible private release')
    return dict(mode='generic',cases=rows,transitions=transitions,checks=q.CHECKS,kernel_calls=calls,command_uses=uses,
                planner_examples=[plan(H,(1,),(0,2)),plan(H,(1,),(0,)),plan(H,(1,),(2,)),plan(H,(0,),(1,2))])

def cycle(rounds=80):
    C=q.Compiler(slots=6,specs=q.selected_specs());tab=((None,)*3,(None,)*6);J=C.encode(tab);named=q.base.ref.old.seed(J)
    actions=0;primitive=0;anchor_name=None;first=[]
    def apply(op):
        nonlocal tab,J,named,actions,primitive,anchor_name
        want=q.expected(C,tab,op);K,_,_=C.run(J,op)
        for raw in C.programs[op]:
            named,_,_=q.base.ref.old.raw_step(named,raw,C.H);primitive+=1
            if anchor_name is not None:
                q.ck(named.names().get(C.targets[2])==anchor_name,'C creation survives every primitive of every subsequent call')
        got=C.decode(K)
        q.ck(got==want and named.matching==K,'Repeated logical and creation-aware source executions agree')
        J=K;tab=got[0];actions+=1
        if len(first)<20:first.append(dict(op=op,result=got[1],table=tab))
    apply(('reserve',2));anchor_name=named.names()[C.targets[2]];apply(('reserve',0))
    for k in range(rounds):
        i=k%6;j=(i+1)%6
        for op in (('bind',i,0),('bind',j,2),('execute_scope',i,(0,),(2,)),('reserve',0),
                   ('execute_scope',i,(0,),(2,)),('execute_scope',j,(0,),(2,)),('valid',j),
                   ('execute_scope',i,(1,),(1,)),('same',i,j),('drop',i)):
            apply(op)
    q.ck(named.names()[C.targets[2]]==anchor_name,'Final C is still the initial physical occurrence')
    return dict(mode='cycle',rounds=rounds,actions=actions,primitive_prefixes=primitive,
                permanent_source=C.targets[2],initial_and_final_creation_name=anchor_name,
                checks=q.CHECKS,kernel_calls=C.calls,command_uses=C.uses,annotated_kernel_calls=q.base.ref.old.KERNEL_CALLS,
                first_actions=first,members=C.members,candidates=len(C.H))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=('generic','cycle'));p.add_argument('--out',required=True);a=p.parse_args()
    ans=generic() if a.mode=='generic' else cycle()
    Path(a.out).write_text(json.dumps(ans,ensure_ascii=False,indent=2)+'\n')
    print({k:v for k,v in ans.items() if k in ('mode','checks','transitions','actions','primitive_prefixes','kernel_calls','command_uses','annotated_kernel_calls')})
