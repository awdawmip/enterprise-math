"""All-prefix relational decoding in the pinned reservation model.

A partial event is not automatically an erased logical record. All scientific
state transitions and positive coefficients reuse the source-pinned BRC code.
This is a conditional finite controller model, NOT native six-axis dynamics.
No inherited main suite is executed. Run with Python 3.11+.
"""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from itertools import product
from pathlib import Path

ROOT=Path(__file__).resolve().parent
P=ROOT/'pinned/check_fault.py'
if hashlib.sha256(P.read_bytes()).hexdigest()!='b34cb8e656e5d7cefb7db9caf8229f9379eddfd578259edcae6b0b828230b82e':
    raise RuntimeError('parent source pin mismatch')
sp=importlib.util.spec_from_file_location('prefix_pinned_fault',P)
f=importlib.util.module_from_spec(sp);sys.modules[sp.name]=f;sp.loader.exec_module(f)
z,k,e,m,r=f.z,f.k,f.e,f.m,f.r
ZERO,ONE=k.ZERO,k.ONE
CHECKS=0;CALLS=0

def ck(ok,label):
    global CHECKS
    CHECKS+=1
    if not ok: raise AssertionError(label)

def cw(w):return dict(C=w.count,W=str(w.total),M=str(w.dominant))
def put(d,key,w):d[key]=r.merge(d.get(key,ZERO),w)
def block(J,i):return m.canon(h for h in J if 6*i+1<=min(h)<=6*i+6)
def normalize(B,i):return m.canon(tuple(x-6*i for x in h) for h in B)
A,B=map(m.canon,k.patterns(0))
H0=k.library(1)

def partial_read(J):
    """0/1 for any nonempty single-side submatching, None for empty."""
    if not J:return None
    if all(h in A for h in J):return 0
    if all(h in B for h in J):return 1
    raise ValueError('outside declared seven-state local library')

def complete_only(J):
    return 0 if J==A else 1 if J==B else None

def vote(values):
    a=values.count(0);b=values.count(1)
    return 0 if a>b else 1 if b>a else None

def read_data(J,n,coarse=False):
    obs=complete_only if coarse else partial_read
    return tuple(obs(normalize(block(J,i),i)) for i in range(n))

def step(J,op,H):
    global CALLS
    nxt,delta,ok=e.step(J,op,H);CALLS+=1
    # Executed primitive's coefficient is the original positive BRC unit.
    w=r.serial(ONE,ONE)
    ck(all(h in H for h in nxt),'candidate permission retained')
    ck(len(m.used(nxt))==3*len(nxt),'no duplicated occurrence allocation')
    return nxt,w,ok

def execute(x,commands,nregs=None,keep=True):
    n=len(x);nr=n if nregs is None else nregs
    J=k.state(nr,sum(v<<i for i,v in enumerate(x)))
    H=k.library(nr);w=e.prep(J);trace=[]
    for op in commands:
        J,u,ok=step(J,op,H);w=r.serial(w,u)
        if keep:trace.append(dict(command=op,success=ok,data=read_data(J,n),
            coarse=read_data(J,n,True),state=J,vacancy=6*nr-len(m.used(J))))
    return dict(initial=x,state=J,data=read_data(J,n),CWM=cw(w),trace=trace)

def local_certificates():
    I,cat=e.catalog(H0);states=tuple(sorted(cat));ck(len(states)==7,'seven actual BRC assemblies')
    table={};traces=[]
    for value in (0,1):
        for J0 in states:
            J=J0;seq=[J];coeff=e.prep(J)
            for op in z.reset_word(0,value):
                J,w,_=step(J,op,H0);coeff=r.serial(coeff,w);seq.append(J)
            ck(J==(A if value==0 else B),'pinned word still writes target from every legal state')
            table[J0,value]=seq
            if J0==(A if value==0 else B):
                ck(all(partial_read(t)==value for t in seq),'correct record decodable at every primitive prefix')
                ck(all(t for t in seq),'correct record never completely emptied by its own reset')
            traces.append(dict(initial=J0,target=value,states=seq,partial=[partial_read(t) for t in seq],CWM=cw(coeff)))
    # A decoding observer is not a replacement for the actual dynamic state.
    s1=A;s2=m.canon((A[0],));n1,_,_=step(s1,('release',1),H0);n2,_,_=step(s2,('release',1),H0)
    ck(partial_read(s1)==partial_read(s2)==0 and partial_read(n1)!=partial_read(n2),
       'new logical observer is NOT a quotient for arbitrary future release')
    alphabet=[('release',i) for i in range(1,7)]+[('reserve',h) for h in sorted(H0)]
    fault={}
    for bit in (0,1):
        current={(A if bit==0 else B):ONE};combined={}
        for t in range(5):
            for J,w in current.items():put(combined,J,w)
            ck(r.total(current.values()).count==10**t,'all confined faulty command words retained')
            if t==4:break
            nxt={}
            for J,w in current.items():
                for op in alphabet:
                    v,u,_=step(J,op,H0);put(nxt,v,r.serial(w,u))
            current=nxt
        ck(r.total(combined.values()).count==11111,'all local faulty prefixes length0..4')
        fault[bit]=combined
    return states,table,fault,traces

def all_prefix_products(states,table,fault):
    """BRC product over local-prefix families, not an assumed schedule law.

Commutation across disjoint registers permits each prefix combination to be
realized by an interleaving. Coefficients count local-prefix selections and
fault words, NOT the number/probability of global scheduling histories.
"""
    rows=[];digest=hashlib.sha256();states_checked=0
    for original in (0,1):
        for wrong in range(-1,5):
            x=tuple(original^(i==wrong) for i in range(5))
            for bad in range(5):
                fam={():ONE}
                for i in range(5):
                    if i==bad:local=fault[x[i]]
                    else:
                        local={}
                        for J in table[A if x[i]==0 else B,original]:put(local,J,ONE)
                    nxt={}
                    for pref,pw in fam.items():
                        for J,jw in local.items():put(nxt,pref+(J,),r.serial(pw,jw))
                    fam=nxt
                total=r.total(fam.values());ck(total.count==11111*5**4,'typed prefix-product multiplicity')
                for Jtuple,w in fam.items():
                    values=tuple(partial_read(J) for J in Jtuple)
                    ck(vote(values)==original,'all-prefix five-record correctness under one input and one lane fault')
                    ck(sum(v==original for v in values)>=3,'three permanent correct record signals remain')
                    digest.update(repr((original,wrong,bad,Jtuple,cw(w))).encode());states_checked+=1
                rows.append(dict(original=original,initial_wrong=wrong,bad_lane=bad,
                    distinct_prefix_states=len(fam),CWM=cw(total)))
    return dict(cases=len(rows),state_checks=states_checked,rows=rows,digest=digest.hexdigest(),
                interpretation='prefix tuples and confined faulty words; not schedule probabilities')

def witnesses():
    # Complete current-data collision at the SAME command position after two writes.
    w0=z.reset_word(0,1)+z.reset_word(1,0)
    w1=z.reset_word(0,1)+z.reset_word(1,0)
    p=execute((0,0,0,1),w0);q=execute((1,1,0,1),w1)
    ck(p['state']==q['state'] and p['data']==(1,0,0,1),'four-record full-state ambiguity')
    # original0: initially bad3, bad repair0. original1: initially bad2, bad repair1.
    # Two original values; same data command word and same 8-step phase.
    s0=z.reset_word(0,1)+z.reset_word(2,0)+z.reset_word(1,0)[:1]
    s1=z.reset_word(0,1)+z.reset_word(2,0)+z.reset_word(1,1)[:1]
    a=execute((0,0,0,0,1),s0);b=execute((1,1,1,0,1),s1)
    ca=read_data(a['state'],5,True);cb=read_data(b['state'],5,True)
    ck(ca==cb==(1,None,0,0,1),'erasing partial membership produces exact observation collision')
    ck(a['state']!=b['state'] and vote(a['data'])==0 and vote(b['data'])==1,
       'retained partial triple resolves the coarse collision')
    # All source-stage pointers one step advanced: every register is partial,
    # yet all partial signals are correct, with 15 simultaneous vacancies.
    parallel=[]
    for original in (0,1):
        x=(original,)*5;words=[z.reset_word(i,original) for i in range(5)]
        cmd=[words[i][phase] for phase in range(4) for i in range(5)]
        ans=execute(x,cmd)
        ck(all(vote(t['data'])==original for t in ans['trace']),'all-prefix round-robin logical preservation')
        ck(ans['trace'][4]['coarse']==(None,)*5,'full-codeword-only observer loses every signal')
        ck(ans['trace'][4]['vacancy']==15,'parallel partial records cost fifteen vacancies')
        parallel.append(ans)
    # Two questionable sites may empty, while the remaining three partial
    # records still carry original0 at the peak21.
    x=(0,0,0,0,1);targets=(1,0,0,0,0);ws=[z.reset_word(i,targets[i]) for i in range(5)]
    cmd=[ws[i][phase] for phase in range(4) for i in range(5)]
    par=execute(x,cmd);ck(all(vote(t['data'])==0 for t in par['trace']),'concurrent worst-site example still decodes')
    ck(max(t['vacancy'] for t in par['trace'])==21,'concurrency changes resource peak, not logical guarantee')
    return dict(four_record_collision=[p,q],coarse_five_collision=[a,b],
                concurrent_correct=parallel,concurrent_two_questionable=par)

def materialized_controller(n=5):
    """No original-value oracle: healthy targets are read from stored input copies.

One designated channel's stored decision is flipped. The general theorem
allows arbitrary confined fault commands; this is one resource-bearing trace.
"""
    x=(0,0,0,0,1);nr=n+n*n+n;H=k.library(nr)
    J=k.state(nr,sum(b<<i for i,b in enumerate(x)));w=e.prep(J);tr=[]
    initial_data=tuple(block(J,i) for i in range(n))
    def write(J,idx,value,kind):
        nonlocal w
        for phase,op in enumerate(z.reset_word(idx,value)):
            before=J;J,u,ok=step(J,op,H);w=r.serial(w,u)
            ck(all(block(before,i)==block(J,i) for i in range(nr) if i!=idx),'strict write footprint')
            ck(vote(read_data(J,n))==0,'materialized protocol data decodes at EVERY command prefix')
            vacancy=6*nr-len(m.used(J));ck(vacancy<=6,'serialized full-register block has peak6')
            tr.append(dict(kind=kind,register=idx,phase=phase,command=op,success=ok,
                           data=read_data(J,n),vacancy=vacancy,state=J))
        return J
    for lane in range(n):
        for j in range(n):
            raw=partial_read(normalize(block(J,j),j));ck(raw is not None,'snapshot source saturated')
            J=write(J,n+n*lane+j,raw,'private_copy')
        observed=tuple(partial_read(normalize(block(J,n+n*lane+j),n+n*lane+j)) for j in range(n))
        decision=vote(observed);ck(decision is not None,'healthy initial snapshot has definite majority')
        if lane==0:decision=1-decision
        J=write(J,n+n*n+lane,decision,'private_decision')
        ck(tuple(block(J,i) for i in range(n))==initial_data,'data held during all input acquisition')
    for lane in range(n):
        value=partial_read(normalize(block(J,n+n*n+lane),n+n*n+lane))
        J=write(J,lane,value,'commit_own_data')
    ck(read_data(J,n)==(1,0,0,0,0),'one faulty lane remains confined at end')
    ck(len(tr)==4*(n*n+2*n)==140,'all copies, decisions and submissions counted')
    return dict(registers=nr,occurrences=6*nr,commands=len(tr),CWM=cw(w),trace=tr,
                fault='private lane0 decision flip',read_control_native_calibrated=False)

def repeat_checked():
    # A different faulty repair address each round; no fresh outside data noise.
    n=5;J=k.state(n,16);H=k.library(n);tr=[]
    for turn in range(10):
        snapshot=read_data(J,n);target=vote(snapshot);ck(target==0,'end-of-round invariant supplies next snapshot')
        bad=turn%n;targets=tuple(1-target if i==bad else target for i in range(n))
        for i in range(n):
            for op in z.reset_word(i,targets[i]):
                J,w,ok=step(J,op,H);ck(vote(read_data(J,n))==0,'changing faulty address still prefix-safe')
        tr.append(dict(round=turn,end=read_data(J,n)))
        ck(sum(v!=0 for v in read_data(J,n))<=1,'at most one bad output remains')
    return dict(rounds=10,ends=tr,scope='no new external data noise; at most one confined faulty lane per round')

def main():
    states,table,fault,local=local_certificates()
    products=all_prefix_products(states,table,fault)
    wit=witnesses();controller=materialized_controller();repeated=repeat_checked()
    result=dict(schema='EM_RELATIONAL_PREFIX_FIDELITY_V1',
      event_id='EM-20261011-RESIDUAL-PREFIX-FIDELITY-7C2E8A',
      status='CONDITIONAL_EXECUTED_TYPED_BRC_UNREVIEWED',
      global_read='64b02b8fd4181f35ba83a102b3f5aa1672e5738b',
      source_read='e23c8d2dfc9df6f5e00dc7220d1d8d3433a77d01',
      local_paths=local,prefix_products=products,witnesses=wit,
      full_controller=controller,repeated=repeated,
      assertions=CHECKS,actual_primitive_calls=CALLS,BRC_calls=dict(r.CALLS),
      native_mapping_supplied=False,independent_review=False,old_main_suites_executed=False)
    raw=(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    (ROOT/'results.json').write_bytes(raw)
    summary={q:result[q] for q in ('event_id','status','assertions','actual_primitive_calls','BRC_calls')}
    summary.update(prefix_cases=products['cases'],prefix_state_checks=products['state_checks'],
        materialized_registers=controller['registers'],materialized_commands=controller['commands'],
        results_bytes=len(raw),results_sha256=hashlib.sha256(raw).hexdigest(),
        inherited_helper_assertions=e.CHECKS+m.CHECKS+k.CHECKS+z.CHECKS+f.CHECKS)
    (ROOT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
