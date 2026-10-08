"""Positive-BRC reallocation selector; NEW TEST MODEL, NOT native force law.

Run: python check_selector.py
The previously verified assembly is imported, not re-executed. A new explicit
single-event heat-bath update is defined on its compatible assemblies. Occurrence
identities are never destroyed; removal means release of a reservation. The
finite state quotient is licensed only for this selector and its stated readouts.
All branch accumulation uses pinned positive BRC; all-depth hitting mass uses the
unchanged pinned finite_recurrent_mass_analysis. No random simulation is needed.
"""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from fractions import Fraction as Q
from pathlib import Path
from collections import deque
from itertools import combinations

ROOT=Path(__file__).resolve().parent

def load(name, path, blob):
    data=path.read_bytes()
    actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if actual!=blob: raise RuntimeError(f'pin mismatch: {path}')
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj

prior_path=ROOT/'prior_triad.py'
if not prior_path.exists():
    prior_path=ROOT.parent/'20261007_residual_triad_interface_7c2e8a/check_triad.py'
s=load('selector_pinned_assembly',prior_path,'662755ef82c2f433ca57da76b4ce44d63a407612')
r=s.r
rec_path=ROOT/'sources/brc_weighted_recurrent.py'
if not rec_path.exists(): rec_path=ROOT.parents[2]/'src/enterprise_math/brc_weighted_recurrent.py'
rec=load('selector_pinned_recurrent',rec_path,'4e6b3132580e3cd70a20a0d8bd4d28792b961afb')
CHECKS=0; REC_CALLS=0; POWER_CALLS=0

def ck(ok, label):
    global CHECKS
    CHECKS+=1
    if not ok: raise AssertionError(label)

def cwm(v): return dict(C=v.count,W=str(v.total),M=str(v.dominant))

def layout(eta):
    if eta<=0: raise ValueError('positive rational selector parameter required')
    I=frozenset(range(1,7))
    events=tuple(s.TestEvent(k,frozenset(h),r.edge(eta))
                 for k,h in [('A',(1,2,3)),('B',(1,4,5)),('C',(4,5,6))])
    poly=s.assemble(events,I)
    states=tuple(sorted(poly,key=lambda b:(len(b[0]),tuple(sorted(b[0])))))
    Z=r.total(poly.values()); norm=r.edge(Q(1)/Z.total)
    pi=tuple(r.serial(poly[j],norm) for j in states)
    return I,events,states,pi,Z


def transition(events,states,eta):
    """Every event/proposed-bit branch survives, including blocked proposals."""
    index={state[0]:i for i,state in enumerate(states)}
    rowmat=[]; proposal_rows=[]; bykey={e.key:e for e in events}
    choose=r.edge(Q(1,len(events)))
    bitweight=(r.edge(Q(1)/(1+eta)),r.edge(eta/(1+eta)))
    for i,(J,U) in enumerate(states):
        row=[r.brc.CWM_ZERO for _ in states]
        for e in events:
            rest=J-{e.key}
            used=frozenset().union(*(bykey[k].occurrences for k in rest))
            for bit in (0,1):
                weight=r.serial(choose,bitweight[bit])
                if bit==0:
                    nextJ=rest; effect='release' if e.key in J else 'stay_absent'
                elif not (e.occurrences & used):
                    nextJ=rest|{e.key}; effect='reserve' if e.key not in J else 'stay_present'
                else:
                    nextJ=J; effect='blocked_stay'
                j=index[frozenset(nextJ)]
                row[j]=r.merge(row[j],weight)
                proposal_rows.append(dict(state=sorted(J),event=e.key,proposal=bit,
                     successor=sorted(nextJ),effect=effect,weight=cwm(weight)))
                ck(states[j][1] == frozenset().union(*(bykey[k].occurrences for k in nextJ)),
                   'current allocation agrees with event identities')
        ck(r.total(row).total==1,'row mass conserved including blocked/stay branches')
        rowmat.append(tuple(row))
    return tuple(rowmat),proposal_rows


def reachability(P,start,target):
    seen={start};q=deque([start])
    while q:
        i=q.popleft()
        for j,v in enumerate(P[i]):
            if v.live and j not in seen:
                if j==target:return True
                seen.add(j);q.append(j)
    return start==target


def run_eta(eta):
    global REC_CALLS,POWER_CALLS
    I,E,states,pi,Z=layout(eta)
    P,proposals=transition(E,states,eta)
    index={J:i for i,(J,U) in enumerate(states)}
    target=index[frozenset(('A','C'))]; start=index[frozenset(('B',))]
    for i in range(len(states)):
        ck(P[i][i].total>0,'aperiodic self loop')
        for j in range(len(states)):
            ck(r.serial(pi[i],P[i][j]).total==r.serial(pi[j],P[j][i]).total,
               'detailed balance as positive branch product')
            ck(reachability(P,i,j),'finite selector is irreducible')
    for j in range(len(states)):
        value=r.total(r.serial(pi[i],P[i][j]) for i in range(len(states)))
        ck(value.total==pi[j].total,'stationary total mass')
    ck(Z.total==1+3*eta+eta*eta,'partition identity')
    expected_residual=r.total(r.serial(pi[i],r.edge(len(I-U)))
                            for i,(J,U) in enumerate(states) if I-U)
    ck(expected_residual.total==(6+9*eta)/(1+3*eta+eta*eta),'stationary residue identity')
    # A proposal word releasing B, reserving A then C is kept as one path.
    w=r.brc.CWM_ONE
    cur=start;route=[]
    for event,bit in [('B',0),('A',1),('C',1)]:
        pr=next(p for p in proposals if p['state']==sorted(states[cur][0])
                and p['event']==event and p['proposal']==bit)
        w=r.serial(w,r.edge(Q(pr['weight']['W'])))
        cur=index[frozenset(pr['successor'])]
        route.append(dict(event=event,proposal=bit,state=sorted(states[cur][0]),
                          unassigned=sorted(I-states[cur][1])))
    ck(cur==target and w.total==eta**2/(27*(1+eta)**3),'explicit escape branch')
    transient=[i for i in range(len(states)) if i!=target]
    mass=tuple(tuple(P[i][j].total for j in transient) for i in transient)
    analysis=rec.finite_recurrent_mass_analysis(mass);REC_CALLS+=1
    ck(analysis.stable and analysis.verify_stable_certificate(),'transient integer certificate')
    h=analysis.canonical_potential
    expect_B=h[transient.index(start)]
    formula=3*(eta+1)**2*(3*eta+1)/(2*eta**2)
    ck(expect_B==formula,'all-depth exact first-hit formula')
    # Full stochastic mass is NOT a stable summable all-depth mass matrix.
    full=rec.finite_recurrent_mass_analysis(tuple(tuple(v.total for v in row) for row in P));REC_CALLS+=1
    ck(not full.stable,'do not call recurrent stationary mass summable')
    # Killed finite paths, first-hit mass and the exact remaining first-hit cost.
    layer={start:r.brc.CWM_ONE};hit=r.brc.CWM_ZERO;prefix=r.brc.CWM_ZERO
    finite=[]
    for n in range(21):
        surviving=r.total(layer.values())
        ck(r.merge(hit,surviving).total==1,'hit plus surviving mass one')
        tail=r.total(r.serial(v,r.edge(h[transient.index(i)])) for i,v in layer.items())
        ck(r.merge(prefix,tail).total==expect_B,'prefix survival sum plus residual expectation')
        power=rec.recurrent_mass_power(mass,n);POWER_CALLS+=1
        for j in transient:
            ck(layer.get(j,r.brc.CWM_ZERO).total==power[transient.index(start)][transient.index(j)],
               'BRC path accumulation equals pinned recurrent power')
        finite.append(dict(step=n,survival=str(surviving.total),hit=str(hit.total),
                           future_mean_contribution=str(tail.total)))
        if n==20:break
        prefix=r.merge(prefix,surviving)
        nxt={}
        for i,v in layer.items():
            for j,k in enumerate(P[i]):
                if not k.live:continue
                contribution=r.serial(v,k)
                if j==target:hit=r.merge(hit,contribution)
                else:nxt[j]=r.merge(nxt.get(j,r.brc.CWM_ZERO),contribution)
        layer=nxt
    # Restore-time semantics: after a first hit the ORIGINAL chain can leave.
    leave=r.total(P[target][j] for j in transient)
    ck(leave.total==Q(2)/(3*(1+eta)),'hitting is not permanent absorption')
    return dict(eta=str(eta),states=[sorted(J) for J,U in states],
       stationary=[str(v.total) for v in pi],Z=str(Z.total),
       stationary_optimum=str(pi[target].total),stationary_mean_unassigned=str(expected_residual.total),
       hitting_mean_from_B=str(expect_B),transient_order=[sorted(states[i][0]) for i in transient],
       transient_mass=[[str(v) for v in row] for row in mass],
       integer_potential=list(analysis.primitive_integer_potential),
       full_transition=[[cwm(v) for v in row] for row in P],proposals=proposals,
       escape_route=route,escape_path_weight=cwm(w),finite_first_hit=finite,
       optimum_exit_probability=str(leave.total),native_force=False,physical_time=False)


def path_library(n):
    # A 3-uniform event library whose conflict graph is a path of 2n+1 nodes.
    # Adjacent nodes share one occurrence; padding occurrences are private.
    events=[];I=set();counter=2*n
    for j in range(2*n+1):
        h=set()
        if j:h.add(j-1)
        if j<2*n:h.add(j)
        while len(h)<3:h.add(counter);counter+=1
        I.update(h)
        name=('A'+str(j//2)) if j%2==0 else ('B'+str((j+1)//2))
        events.append(s.TestEvent(name,frozenset(h),r.edge(1)))
    return tuple(events),frozenset(I)


def check_bounded_exchange():
    out=[]
    for n in range(1,7):
        E,I=path_library(n);poly=s.assemble(E,I)
        old=frozenset(e.key for j,e in enumerate(E) if j%2)
        opt=frozenset(e.key for j,e in enumerate(E) if not j%2)
        better=[J for J,U in poly if len(J)>len(old)]
        ck(better==[opt],'unique improvement requires all even events')
        ck(all(len(old-J)==n for J in better),'strict improvement removes every old event')
        # Equal-cardinality swaps can move the defect, before the last addition.
        J=old;route=[sorted(J)]
        for i in range(n):
            J=(J-{'B'+str(i+1)})|{'A'+str(i)}
            ck(any(K==J for K,U in poly),'neutral defect transport remains compatible')
            ck(len(J)==n,'neutral exchange does not reduce unassigned count')
            route.append(sorted(J))
        J=J|{'A'+str(n)}
        ck(J==opt,'last addition gives strict improvement')
        out.append(dict(n=n,occurrences=len(I),events=[dict(key=e.key,occurrences=sorted(e.occurrences)) for e in E],
                        compatible_assemblies=len(poly),start=sorted(old),optimum=sorted(opt),
                        strict_improvement_min_old_removals=n,neutral_route=route+[sorted(J)]))
    return out


def check_early_optimization():
    I=frozenset(range(1,7))
    A=s.TestEvent('A',frozenset((1,2,3)),r.edge(1))
    B=s.TestEvent('B',frozenset((1,4,5)),r.edge(1))
    C=s.TestEvent('C',frozenset((4,5,6)),r.edge(1))
    first=s.factor(B); later=s.times(s.factor(A),s.factor(C))
    def opt(poly):
        best=max(len(k[0]) for k in poly)
        return {k:v for k,v in poly.items() if len(k[0])==best}
    early=opt(s.times(opt(first),later)); delayed=opt(s.times(first,later))
    ck({J for J,U in early}=={frozenset(('B',))},'early local optimizer traps B')
    ck({J for J,U in delayed}=={frozenset(('A','C'))},'delayed optimization attains AC')
    ck(early!=delayed,'Opt is not a congruent intermediate compression')
    return {'early':[s.row(k,v,I) for k,v in early.items()],
            'delayed':[s.row(k,v,I) for k,v in delayed.items()],
            'equation':'Opt(PQ) != Opt(Opt(P)Q)',
            'observation':'maximize allocated event count; NOT physical energy'}


def main():
    samples=[Q(1,10),Q(1,2),Q(1),Q(3,2),Q(2),Q(3),Q(10),Q(100)]
    runs=[run_eta(x) for x in samples]
    exchange=check_bounded_exchange()
    early=check_early_optimization()
    result=dict(schema='EM_RESIDUAL_SELECTOR_V1',status='NEW_CONDITIONAL_SELECTOR_NOT_NATIVE_FORCE',
        global_read='8004ac0e3f369a2ff2f81d53202c56bb20eb1e21',source_read='d6169e0d9a19408a677c9a5392dbff3cc1a09f66',
        samples=runs,bounded_exchange=exchange,early_optimization=early,assertions=CHECKS,BRC_calls=dict(r.CALLS),
        recurrent_analysis_calls=REC_CALLS,recurrent_power_calls=POWER_CALLS,
        old_suites_reexecuted=False,prior_function_source_unmodified=True,
        random_simulation=False,physical_law_proved=False,independent_review=False)
    data=(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    (ROOT/'results.json').write_bytes(data)
    print(json.dumps({k:result[k] for k in ('status','assertions','BRC_calls','recurrent_analysis_calls','recurrent_power_calls')},indent=2))
    print('samples',[(x['eta'],x['stationary_optimum'],x['hitting_mean_from_B']) for x in runs])
    print('results',len(data),hashlib.sha256(data).hexdigest())

if __name__=='__main__':main()
