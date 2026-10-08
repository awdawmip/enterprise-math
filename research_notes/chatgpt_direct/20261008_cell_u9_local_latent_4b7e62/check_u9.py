#!/usr/bin/env python3
"""U9 finite exact BRC certificates. Run: python check_u9.py.

No Monte Carlo fit, infinite trajectory enumeration, mechanical reaction or
native triadic force claim. Infinite statements are proved in NOTE.md.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product, permutations, combinations
from collections import Counter,deque
import hashlib,gzip,json
import local_latent as m
r,u=m.r,m.u
ROOT=Path(__file__).resolve().parent;EV=ROOT/'evidence';EV.mkdir(exist_ok=True)
checks=0;transitions=Counter();details=[]

def ck(ok,label):
    global checks
    checks+=1
    if not ok:raise AssertionError((checks,label))

def add(a,b):return tuple(x+y for x,y in zip(a,b))

def test_edge(s,y,undo,w,q,kind,label):
    if y is None:
        transitions[kind+'_ineligible']+=1;return
    m.validate(y);ck(True,'new valid tree, paired paths and exclusion')
    ck(undo(y)==s,'exact inverse including every path word')
    delta=y.length()-s.length();a,b=w.decision(delta)
    ar,br=w.decision(-delta)
    ck(r.merge(a,b).total==1,'accept/reject budget retained')
    oldflux=r.serial(w.weight(s),r.serial(r.edge(q),a))
    newflux=r.serial(w.weight(y),r.serial(r.edge(q),ar))
    ck(oldflux==newflux,'full CWM pair balance at a symmetric proposal label')
    ck(w.weight(y).total/w.weight(s).total==w.lam**delta,'changed-segment ratio')
    transitions[kind+'_eligible']+=1
    # Every distinct label stays present, but avoid serializing duplicate full states.
    details.append({'kind':kind,'label':label,'before_L':s.length(),'after_L':y.length(),
                    'proposal':q,'accepted_flux':oldflux,'acceptance':a.total})

z=r.ZERO;e1=r.direction(0);e2=r.direction(2);e3=r.direction(4)
cells=(z,e1,add(e1,e2),e2);T=((0,1),(1,2),(2,3))
base=m.from_tree(cells,T)
Ptab=base.table();Qtab=base.table()
Ptab[0,1]=((4,0,5),());Qtab[0,1]=((5,0,4),())
P=m.make(cells,Ptab);S=m.make(cells,Qtab)
m.validate(P);m.validate(S)
ck(P.tree()==S.tree() and P.cells==S.cells and P.length()==S.length()==5,'same coarse input')

# Reversibility and exact BRC balance for ALL labels on these finite states.
inputs=[base,P,S,m.from_tree(cells,((0,1),(0,2),(0,3)),meeting=z)]
for lam in (Q(1,48),Q(1,36),Q(1,60)):
    w=m.Weights(lam)
    for si,s in enumerate(inputs):
        N=len(s.cells);E=N*(N-1)//2
        for a,p,g in product(range(N),r.PORTS,(False,True)):
            y=m.material(s,a,p,g)
            test_edge(s,y,lambda t,a=a,p=p,g=g:m.material(t,a,p^1,not g),
                      w,Q(1,96*N),'material',(si,a,p,g))
            if y is not None:
                ck(sum(sum(abs(xx-yy) for xx,yy in zip(x,y0)) for x,y0 in zip(s.cells,y.cells))==1,
                   'one actor, one native edge')
                oldmeet={e:m.endpoint(s.cells[e[0]],legs[0]) for e,legs in s.table().items()}
                newmeet={e:m.endpoint(y.cells[e[0]],legs[0]) for e,legs in y.table().items()}
                ck(oldmeet==newmeet,'no remote meeting teleport under actor move')
        for edge,p,g in product(combinations(range(N),2),r.PORTS,(False,True)):
            test_edge(s,m.meeting(s,edge,p,g),lambda t,e=edge,p=p,g=g:m.meeting(t,e,p,not g),
                      w,Q(1,96*E),'meeting',(si,edge,p,g))
        for edge in combinations(range(N),2):
            ww=s.table().get(edge,((),()))
            for side in (0,1):
                for j in range(len(ww[side])+2):
                    geo=Q(1,2**(j+1))
                    for p,g in product(r.PORTS,(False,True)):
                        test_edge(s,m.detour(s,edge,side,j,p,g),
                                  lambda t,e=edge,side=side,j=j,p=p,g=g:m.detour(t,e,side,j,p,not g),
                                  w,geo/Q(384*E),'detour',(si,edge,side,j,p,g))
                    test_edge(s,m.commute(s,edge,side,j),
                              lambda t,e=edge,side=side,j=j:m.commute(t,e,side,j),
                              w,geo/Q(16*E),'commute',(si,edge,side,j))
        for a,b,c in permutations(range(N),3):
            test_edge(s,m.slide(s,a,b,c),lambda t,a=a,b=b,c=c:m.slide(t,a,c,b),
                      w,Q(1,4*N*(N-1)*(N-2)),'slide',(si,a,b,c))

# New explicit marginal test: complete paired-path/tree states at TOTAL length
# <=5 for the original four-unit configuration. Each of 3 links has length>=1,
# so each individual link needs at most3. This is a proved finite cover.
w=m.Weights();pool={e:{} for e in combinations(range(4),2)}
for n in range(1,4):
    for word in product(r.PORTS,repeat=n):
        d=m.endpoint(z,word)
        for e in pool:
            if d!=u.difference(cells[e[1]],cells[e[0]]):continue
            for split in range(n+1):
                left=word[:split];right=tuple(p^1 for p in reversed(word[split:]))
                pool[e].setdefault(n,[]).append((left,right))

marg={n:r.brc.CWM_ZERO for n in range(3,6)};micro=[]
for tree in u.trees(4):
    for lens in product(range(1,4),repeat=3):
        if sum(lens)>5:continue
        for legs in product(*(pool[e].get(n,[]) for e,n in zip(tree,lens))):
            state=m.make(cells,dict(zip(tree,legs)));m.validate(state)
            ck(state.length()==sum(lens),'microstate length and meeting validity')
            L=state.length();marg[L]=r.merge(marg[L],w.weight(state));micro.append(state)
ck(len(set(micro))==len(micro),'split and tree identities give unique microstates')
ck({L:v.count for L,v in marg.items()}=={3:32,4:192,5:6624},'new exact joint coefficients')

# Independent expression route is inherited U8 positive BRC endpoint recurrence,
# not a newly implemented classical solver or an infinite cutoff dynamics.
o=u.Overlap();poly={n:r.brc.CWM_ZERO for n in range(3,6)}
for tree in u.trees(4):
    for lens in product(range(1,4),repeat=3):
        n=sum(lens)
        if n>5:continue
        mass=r.brc.CWM_ONE
        for e,k in zip(tree,lens):
            coeff=r.total(o.g(k,u.difference(cells[e[1]],cells[e[0]])) for split in range(k+1))
            mass=r.serial(mass,coeff)
        poly[n]=r.merge(poly[n],mass)
ck(poly==marg,'exact grouped marginal agrees in count,total,dominant')

# Same X, T, meeting Cells, total length and CWM score; different next positions.
lp,rp=m.position_query(P,w);lq,rq=m.position_query(S,w)
ck(r.total(lp.values()).total==1 and r.total(lq.values()).total==1,'complete position laws normalized')
ck(w.weight(P)==w.weight(S),'same positive CWM score')
tv=sum((abs(lp.get(k,r.brc.CWM_ZERO).total-lq.get(k,r.brc.CWM_ZERO).total)
        for k in lp.keys()|lq.keys()),Q(0))/2
ck(tv==Q(1,392),'exact non-lumpability witness for four-channel query')
pplus=list(cells);pplus[0]=e3;pplus=tuple(pplus)
pminus=list(cells);pminus[0]=r.direction(5);pminus=tuple(pminus)
ck(lp[pplus].total==Q(1,384) and lq[pplus].total==Q(1,18816),'positive-axis occupancy contrast')
ck(lp[pminus].total==Q(1,18816) and lq[pminus].total==Q(1,384),'negative-axis contrast')

# The witness is reachable from a single microstate by named permitted edits.
# Insert a backtrack at the start, then commute the second leg across +e1.
paths=[]
for sign,target in ((4,P),(5,S)):
    middle=m.detour(base,(0,1),0,0,sign,True)
    end=m.commute(middle,(0,1),0,1)
    ck(end==target,'controlled microstate preparation uses legal edits')
    aa,_=w.decision(2);bb,_=w.decision(0)
    q1=Q(1,4608);q2=Q(1,384)
    prep=r.serial(r.serial(r.edge(q1),aa),r.serial(r.edge(q2),bb))
    ck(prep.total>0,'controlled preparation has positive trial weight')
    paths.append({'target':target,'intermediate':middle,'selected_path_weight':prep})

# All abstract tree slides connected on N=3..5, realized at one common meeting.
# Finite verification supplements the general reduce-to-star proof.
slide_graph={}
for N in (3,4,5):
    cc=tuple(tuple(i*v for v in e1) for i in range(N));ts=u.trees(N)
    states={T:m.from_tree(cc,T,meeting=z) for T in ts};graph={T:set() for T in ts};edge_count=0
    for t,s in states.items():
        for a,b,c in permutations(range(N),3):
            y=m.slide(s,a,b,c)
            if y is None:continue
            m.validate(y);ck(m.slide(y,a,c,b)==s,'realized tree-slide involution')
            ck(y.tree() in states,'tree connectivity preserved without global score')
            graph[t].add(y.tree());edge_count+=1
    found={ts[0]};queue=deque(found)
    while queue:
        for v in graph[queue.popleft()]-found:found.add(v);queue.append(v)
    ck(len(found)==len(ts),'all labelled trees reachable by slides')
    slide_graph[N]={'trees':len(ts),'directed_labels':edge_count,'reached':len(found)}

# Geometric edit-index grammar has total1 and finite expected index1.
# Its tail is represented by the original recurrent BRC, not deleted.
r.CALLS['one_state_recurrent_cwm']+=1
geometric=r.brc.one_state_recurrent_cwm([Q(1,2)])
index_rows=[]
for J in range(9):
    prefix=r.total(r.serial(r.edge(Q(1,2)),geometric.depth(j)) for j in range(J+1))
    tail=r.serial(r.serial(r.edge(Q(1,2)),geometric.depth(J+1)),r.edge(geometric.total_mass_closure))
    ck(r.merge(prefix,tail).total==1,'all edit indices including inactive tail')
    index_rows.append((J,prefix.total,tail.total))

# A state-dependent uniform index would NOT have a symmetric proposal.
# For a one-letter leg growing to length three, q_forward=1/2, q_reverse=1/4
# if both choose among indices 0..length. Omitting the Hastings correction fails.
old_weight=w.power(1);new_weight=w.power(3);aa,bb=w.decision(2)
bad_forward=r.serial(old_weight,r.serial(r.edge(Q(1,2)),aa))
bad_reverse=r.serial(new_weight,r.serial(r.edge(Q(1,4)),bb))
ck(bad_forward.total==2*bad_reverse.total,'uniform-current-length proposal is asymmetric')
ck(bad_forward.total!=bad_reverse.total,'not silently using an invalid acceptance ratio')

# Quantify the memory bound at the main parameter; not physical energy.
# A single explicitly prepared square state gives Z >= lambda^3.
N=4;tN=len(u.trees(N));rho=12*w.lam
Zlower=w.power(3)
# unrestricted sum of L*lambda^L = 2(N-1)*rho*tN/(1-rho)^(2N-1)
Sone=o.series.total_mass_closure
upper=r.edge(2*(N-1)*tN)
upper=r.serial(upper,r.edge(rho))
for _ in range(2*N-1):upper=r.serial(upper,r.edge(Sone))
mean_bound=r.serial(upper,r.edge(1/Zlower.total)).total
ck(mean_bound>0,'finite conservative expected-record-length bound')

summary={'status':'CONDITIONAL_AUXILIARY_LOCAL_TRAIL_DYNAMICS_NOT_NATIVE_FORCE',
 'event_id':'EM-20261008-CELL-U9-LOCAL-LATENT-4B7E62','checks':checks,
 'BRC_calls':dict(r.CALLS),'transition_coverage':dict(transitions),
 'microstates_complete_total_length_le5':len(micro),
 'microstate_coefficients':{str(L):v.count for L,v in marg.items()},
 'material_proposal_labels_per_query':24*4,'exact_position_TV':str(tv),
 'P_positive_move':str(lp[pplus].total),'Q_positive_move':str(lq[pplus].total),
 'witness_same_length':P.length(),'witness_weight':str(w.weight(P).total),
 'tree_slide_graphs':slide_graph,'expected_length_upper_for_N4':str(mean_bound),
 'kernel_calls_global_score':False,'finite_path_cutoff_in_kernel':False,
 'stationary_marginal_exact_U8':True,'projected_trajectory_is_U8_Barker':False,
 'irreducibility_proved_range':'2<=N<=6','full_infinite_chain_enumerated':False,
 'native_force':False,'native_triad_lift':False,'physical_reaction':False,
 'physical_clock':False,'fixed_physical_resource_budget':False,'prime_claim':False,
 'independent_review':False,'literature_provider_query':'PLATFORM_BLOCKED_NOT_RETRIED'}
trace={'transition_records':details,'microstates':micro,'marginal':marg,
       'counterexample':{'P':P,'Q':S,'P_law':lp,'Q_law':lq,'P_proposals':rp,'Q_proposals':rq},
       'controlled_preparations':paths,'index_tail':index_rows}
raw=(json.dumps(m.encode(trace),sort_keys=True,separators=(',',':'))+'\n').encode()
packed=gzip.compress(raw,mtime=0)
summary.update(trace_sha256=hashlib.sha256(raw).hexdigest(),trace_bytes=len(raw),
               trace_compressed_sha256=hashlib.sha256(packed).hexdigest())
(EV/'full_trace.json.gz').write_bytes(packed)
(EV/'results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
