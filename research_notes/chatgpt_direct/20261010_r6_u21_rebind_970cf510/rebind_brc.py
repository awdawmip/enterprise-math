"""U21 contact-only first-return extension; all positive transfer composition is BRC.
No moving-body or primitive-force attribution. Same-author check, not review.
"""
from __future__ import annotations
import sys, types, hashlib, json, itertools
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parent
raw=(ROOT/'brc_weighted_source.py').read_text()
blob=hashlib.sha1(b'blob '+str(len(raw.encode())).encode()+b'\0'+raw.encode()).hexdigest()
assert blob=='3f205696709e847909958a153f8fe10d3f6b70f0'
# Inherited U21 loader adaptation: omit two unused symbolic-readout imports.
# Every scientific function body is unchanged. These readouts are never invoked.
adapted=raw.replace('from .brc_logarithm import LnExpr, ln\n','').replace('from .exact_arithmetic import DivisionExpr, division\n','')
mod=types.ModuleType('pinned_brc');sys.modules[mod.__name__]=mod
exec(compile(adapted,'pinned_brc','exec'),mod.__dict__)
calls={'edge':0,'alternative':0,'serial':0,'recurrent':0}
def edge(w):
    calls['edge']+=1
    return mod.cwm_edge(w) if w else mod.CWM_ZERO
def add(a,b):
    calls['alternative']+=1;return mod.cwm_recoalesce(a,b)
def mul(a,b):
    calls['serial']+=1;return mod.cwm_propagate(a,b)

# A transfer is (total-only CWM representative, pointed-time CWM representative).
# A k-step history has k time marks. Pointing is not a physical heartbeat.
# Finite raw branch CWM is kept separately for the one-step lumpability audit.
def ta(a,b):return (add(a[0],b[0]),add(a[1],b[1]))
def tm(a,b):return (mul(a[0],b[0]),add(mul(a[1],b[0]),mul(a[0],b[1])))
Z=(mod.CWM_ZERO,mod.CWM_ZERO)
def lift(w,time=1):return (edge(w),edge(w*time))
trace=[]
def star(a):
    if not a[0].live:return lift(F(1),0)
    calls['recurrent']+=1
    r=mod.one_state_recurrent_cwm([a[0].total])
    assert r.total_mass_stable
    c=edge(r.total_mass_closure)
    marked=mul(mul(c,a[1]),c)
    trace.append({'loop_mass':str(a[0].total),'loop_time_mass':str(a[1].total),'closure':str(c.total),'marked_closure':str(marked.total)})
    return c,marked

def full_row(s,x):
    row={n:mod.CWM_ZERO for n in range(5)}
    hist=[]
    for pair in range(6):
        for side in (1,2):
            n=sum(v!=0 for v in s)
            if pair>=4 or (s[pair]!=0 and s[pair]!=side):
                hist.append((n,F(1,12),(pair,side,'ineligible')))
            else:
                born=s[pair]==0
                a=x/(1+x) if born else 1/(1+x)
                hist.append((n+(1 if born else -1),a/12,(pair,side,'accept')))
                hist.append((n,(1-a)/12,(pair,side,'reject')))
    for n,w,label in hist:row[n]=add(row[n],edge(w))
    assert sum(v.total for v in row.values())==1
    return row,hist

checks=0;output=[];raw_rows=[]
for x in (F(1,48),F(1,2),F(1),F(2)):
    reps={};states=list(itertools.product(range(3),repeat=4))
    for s in states:
        n=sum(v!=0 for v in s);row,hist=full_row(s,x)
        if n in reps:assert mod.future_cwm_equivalent(reps[n],row)
        else:reps[n]=row
        checks+=1
        raw_rows.append({'x':str(x),'state':s,'branches':[{'target':n,'weight':str(w),'label':label} for n,w,label in hist]})
    b=x/(6*(1+x));d=1/(12*(1+x))
    for n,row in reps.items():
        assert row.get(n+1,mod.CWM_ZERO).total==(4-n)*b
        assert row.get(n-1,mod.CWM_ZERO).total==n*d
        checks+=2

    def eliminate(transient,targets):
        # Distinct start node preserves first-hit rather than zero-time stopping.
        nodes=['start']+list(transient)+list(targets)
        a={(i,j):Z for i in nodes for j in nodes}
        a['start',2]=lift(F(1),0)
        for i in transient:
            for j,v in reps[i].items():
                if j in nodes and v.live:a[i,j]=lift(v.total)
        active=nodes[:]
        for k in transient:
            c=star(a[k,k]);others=[v for v in active if v!=k]
            for i in others:
                for j in others:
                    a[i,j]=ta(a[i,j],tm(tm(a[i,k],c),a[k,j]))
            active=others
        return {t:a['start',t] for t in targets}

    hit=eliminate([0,1,2],[3])[3]
    before=eliminate([1,2],[0,3])
    expected=(1+x)*(24*x*x+8*x+1)/(8*x*x*x)
    p=(12*x*x+2*x)/(12*x*x+2*x+1)
    assert hit[0].total==1 and hit[1].total==expected
    assert before[3][0].total==p
    assert add(before[0][0],before[3][0]).total==1
    checks+=4
    # First-step differences check the symbolic all-x solution at exact inputs.
    u0=1/(4*b);u1=(1+d*u0)/(3*b);u2=(1+2*d*u1)/(2*b)
    t=[u0+u1+u2,u1+u2,u2,F(0)]
    for i in (0,1,2):
        terms=mod.CWM_ZERO
        for j,v in reps[i].items():
            if j<3:terms=add(terms,mul(edge(v.total),edge(t[j])))
        assert t[i]==add(edge(F(1)),terms).total
        checks+=1
    output.append({'x':str(x),'reconnect_eventually':str(hit[0].total),'mean_reconnect_proposals':str(hit[1].total),'reconnect_before_empty':str(before[3][0].total),'empty_before_reconnect':str(before[0][0].total),'mean_boundary_proposals':str(add(before[0][1],before[3][1]).total),'conditional_mean_reconnect_before_empty':str(before[3][1].total/before[3][0].total)})

result={'status':'CONDITIONAL_MODEL_DERIVATION_AND_EXECUTED_TYPED_BRC_UNREVIEWED','source_blob':blob,'input_scope':'U21 fixed square geometry, 12 uniformly proposed contact labels, positive x=eta*lambda','observer':'first hit of n=3 from n=2; proposal-count mark; competing n=0 boundary','strong_lumpability_scope':'full one-step target CWM by edge count; serial count/total/dominant for finite horizons; infinite closures TOTAL_ONLY','checks':checks,'brc_calls':calls,'results':output,'closure_trace':trace,'not_verified':['moving-body reconnection','physical heartbeat times','native triadic force','independent review','Source task execution authority']}
(ROOT/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(ROOT/'branches.json').write_text(json.dumps(raw_rows,separators=(',',':'))+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
