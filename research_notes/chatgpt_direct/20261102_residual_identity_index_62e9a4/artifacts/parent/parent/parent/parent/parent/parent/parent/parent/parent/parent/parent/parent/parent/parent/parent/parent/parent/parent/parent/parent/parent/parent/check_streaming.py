"""Streaming evidence conjunction using unchanged triadic/BRC primitives.

Conditional finite matching model, not native physics. The consumer observes
only final YES/NO/UNKNOWN, not each past sampled bit. Words are input-independent.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from itertools import product
from functools import lru_cache
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT/'parent'/'parent'/'parent'/'parent'))
import check_publication as b
p,a,e,m,r = b.p,b.a,b.e,b.m,b.r
ONE,ZERO = b.ONE,b.ZERO
CHECKS=CALLS=USES=0

def ck(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok: raise AssertionError(label)

@lru_cache(maxsize=None)
def raw_step(J,op):
    global CALLS
    CALLS += 1
    H={op[1]} if op[0]=='reserve' else set()
    K,_,ok=e.step(J,op,H)
    return K,ok

def step(J,op,H):
    global USES
    USES+=1
    if op[0]=='reserve' and op[1] not in H: raise ValueError('Undeclared candidate')
    return raw_step(J,op)

def put(d,key,w): d[key]=r.merge(d.get(key,ZERO),w)
def total(values):
    w=ZERO
    for v in values:w=r.merge(w,v)
    return w

def execute(J,W,H,keep=False,omitted=()):
    initial=J;rows=[];mass=e.prep(J);omitted=set(omitted)
    for i,op in enumerate(W):
        before=J
        J,ok=(J,None) if i in omitted else step(J,op,H)
        mass=r.serial(mass,ONE)
        if keep:rows.append(dict(slot=i+1,op=op,invoked=i not in omitted,success=ok,before=before,after=J))
    return dict(initial=initial,end=J,commands=len(W),CWM=e.cw(mass),trace=rows)

def destructive_and(left,sample,out):
    """Consume two full private operands, leave full output and restored zero.

Original majority: 2 target clears + three 9-step copies + rest. Empty target
makes its clears unnecessary. The first two inputs have no later users: omit
only their four source-header reconstruction proposals, then remove their two
remaining tails once the gate is done. Constant and gate workspace stay intact.
"""
    if len({left,sample,out,400,1000,1010,1020})!=7:
        raise ValueError('Operands, output, constant and scratch must be distinct')
    H,W=b.old.majority((left,sample,400),out)
    omitted_positions={0,1,7,8,16,17}
    body=[op for i,op in enumerate(W) if i not in omitted_positions]
    return H,body+[p.one(left+5),p.one(sample+5)]

def collector(k,overwrite=False,indices=None):
    """Finite checked address instance: 2..6 workers; output offsets 500,700."""
    if not 2<=k<=6:raise ValueError('Concrete address allocator supports 2..6')
    specs=[b.spec(i) for i in range(k)]
    H=set(p.library(400)); W=[];stages=[]
    if overwrite:W+=p.clear_word(500)+p.clear_word(700)
    W += [p.add(s[key]) for key in ('pos','neg') for s in specs]
    H |= {s[key] for s in specs for key in ('pos','neg')}
    indices=list(range(k)) if indices is None else list(indices)
    if len(indices)!=k or any(not 0<=i<k for i in indices):raise ValueError('Bad scan list')
    read_work=800
    h,w,_=a.reader(300,500,read_work);H|=h;W+=w
    cur=700 if k%2 else 720
    h,w,_=a.reader(310+indices[0],cur,read_work);H|=h;W+=w
    stages.append(dict(index=indices[0],end=len(W),acc=cur,read_end=len(W),sample=cur))
    for index in indices[1:]:
        out=720 if cur==700 else 700
        h,w,_=a.reader(310+index,740,read_work);H|=h;W+=w;read_end=len(W)
        h,w=destructive_and(cur,740,out);H|=h
        gate_start=len(W);W+=w
        stages.append(dict(index=index,end=len(W),acc=out,read_end=read_end,
                           sample=740,gate_start=gate_start,old_acc=cur,clear_old=gate_start+39))
        cur=out
    ck(cur==700,'fixed output register from compile-time parity')
    return H,W,stages

def setup(source,k,overwrite=False):
    S=[b.spec(i) for i in range(k)];HC,WC,stages=collector(k,overwrite)
    H=a.SOURCE_H|HC|set().union(*(s['H'] for s in S))
    J=m.canon(source+p.reg(400,0)+tuple(s['guard'] for s in S))
    return H,J,S,WC,stages

def producing(S,overlap=False):
    if not overlap:return [op for s in S for op in s['W']]
    return [s['W'][0] for s in S]+[op for s in S for op in s['W'][1:]]

def result_code(J):return p.read(J,500),p.read(J,700)
def private_members():
    return set(range(501,507))|set(range(701,707))|set(range(721,727))|set(range(741,747))|set(range(401,407))|set(range(1001,1007))|set(range(1011,1017))|set(range(1021,1027))|{800,1030}

def gate_cases():
    H,W=destructive_and(700,740,720);rows=[]
    ck(len(W)==41,'41 original commands in consuming gate')
    for x,y in product((0,1),repeat=2):
        J=m.canon(p.reg(700,x)+p.reg(740,y)+p.reg(400,0))
        z=execute(J,W,H,True)
        ck(z['end']==m.canon(p.reg(720,x&y)+p.reg(400,0)), 'full consuming gate contract')
        rows.append(dict(bits=[x,y],run=z))
    return rows

def static_truth():
    """All Boolean signal preparations, not all claims of source provenance."""
    rows=[]
    for k in range(2,7):
        H,W,stages=collector(k)
        # Replace publisher attempts by stable, disjoint signal events in this
        # isolated gate test. No assertion these synthetic signals encode source.
        W=W[2*k:];signals=[(port,20000+2*j,20001+2*j) for j,port in enumerate([300]+list(range(310,310+k)))]
        H|=set(signals)
        cases=0
        for bits in product((0,1),repeat=k+1):
            J=m.canon(p.reg(400,0)+tuple(h for h,bit in zip(signals,bits) if bit))
            z=execute(J,W,H)
            expected=m.canon(J+p.reg(500,bits[0])+p.reg(700,int(all(bits[1:]))))
            ck(z['end']==expected,'all bits: exact final predicate and no private residue')
            cases+=1
        rows.append(dict(k=k,cases=cases))
    return rows

def integration_cases():
    rows=[];full=[]
    _,domain=e.catalog(a.SOURCE_H)
    for k in (2,3,6):
        for source in sorted(domain):
            if a.signed(source)<0:continue
            H,J,S,WC,stages=setup(source,k)
            ck(len(WC)==49*k-35,'stream first-round length')
            ck(len(set().union(*H))==11*k+61,'actual total declared member inventory')
            ck(len(private_members())==50,'constant private collector storage')
            for overlap in (False,True):
                prod=[p.one(4)]+producing(S,overlap)
                start=execute(J,prod,H)['end']
                z=execute(start,WC,H,keep=(k==6 and source==(a.P,a.HN) and overlap))
                code=(1,0) if a.signed(source) else (0,1)
                ck(result_code(z['end'])==code,'full source-to-stream result')
                base=tuple(h for h in z['end'] if set(h).isdisjoint(private_members()))
                ck(z['end']==m.canon(base+p.reg(400,0)+p.reg(500,code[0])+p.reg(700,code[1])), 'scratch, consumed inputs and spare accumulator clear')
                ck(b.old.protected(J,z['end']),'original source E/P/evidence preserved')
                hr,wr,_=collector(k,True)
                nxt=execute(z['end'],wr,H|hr)
                ck(nxt['end']==z['end'],'same-generation repeat has exactly same full endpoint')
                rows.append(dict(k=k,source=source,overlap=overlap,code=code,
                                 first_commands=1+7*k+len(WC),round=len(WC),repeat_round=len(wr),inventory=len(set().union(*H))))
                if z['trace']:full.append(z)
    return dict(cases=rows,representative=full)

def failures():
    rows={}
    # First poll is genuinely too early. Required reset makes later NO possible.
    H,J,S,WC,stages=setup(p.reg(3,0),2)
    early=execute(J,[p.one(4)]+WC,H)
    ck(result_code(early['end'])==(0,0),'early poll is UNKNOWN')
    ready=execute(early['end'],producing(S),H)['end']
    wrong=execute(ready,WC,H,True)
    ck(result_code(wrong['end'])==(0,0),'omitting round reinitialization traps old zero')
    hr,wr,_=collector(2,True);right=execute(ready,wr,H|hr,True)
    ck(result_code(right['end'])==(0,1),'new round genuinely resamples after reset')
    rows['no_round_reset']=wrong;rows['round_reset_control']=right
    # Duplicate an already-negative lane instead of covering all named lanes.
    H,J,S,_,_=setup(p.reg(3,1),2)
    ready=execute(J,[p.one(4)]+producing(S,True),H)['end']
    hb,wb,_=collector(2,indices=[1,1]);bad=execute(ready,wb,H|hb,True)
    ck(result_code(bad['end'])==(1,1),'duplicate lane is not full coverage')
    rows['duplicate_scan_index']=bad
    # Keep a consumed accumulator tail: later use of that output slot is unsafe.
    k=3;H,W,stages=collector(k);W=W[2*k:]
    signals=[(310+i,20000+2*i,20001+2*i) for i in range(k)];H|=set(signals)
    J=m.canon(p.reg(400,0)+tuple(signals[:2]))
    omit=stages[1]['clear_old']-2*k
    bad=execute(J,W,H,True,(omit,))
    ck(p.read(bad['end'],700)==1,'uncleared spent accumulator causes false all-ones result')
    rows['consumed_accumulator_not_cleared']=bad
    H,W=destructive_and(700,740,720)
    J=m.canon(p.reg(700,1)+p.reg(740,1)+p.reg(400,0))
    earlyclear=W[:1]+[p.one(705)]+W[1:]
    bad=execute(J,earlyclear,H,True)
    ck(p.read(bad['end'],720)==0,'clearing operand before its copy finishes destroys evidence')
    rows['operand_cleared_too_early']=bad
    return rows

def shuffle(source,k=2):
    H,J,S,WC,stages=setup(source,k)
    J=execute(J,[p.one(4)],H)['end']
    words=[s['W'] for s in S]+[WC];lengths=tuple(map(len,words))
    # Witness bits record the consumer's actual read outcomes, not values used
    # to execute its instructions. Fold-boundary invariant is checked online.
    read_events={st['read_end']:(j,st['sample']) for j,st in enumerate(stages)}
    ends={st['end']:(j,st['acc']) for j,st in enumerate(stages)}
    d={((0,)*(k+1),J,()):e.prep(J)};peak=1
    for _ in range(sum(lengths)):
        nd={}
        for (pcs,K,seen),mass in d.items():
            for i,pos in enumerate(pcs):
                if pos==lengths[i]:continue
                pp=list(pcs);pp[i]+=1;pp=tuple(pp)
                L,_=step(K,words[i][pos],H);ss=seen
                ck(b.old.protected(J,L),'source evidence unchanged under full interleaving')
                if i==k and pp[i] in read_events:
                    j,o=read_events[pp[i]];v=p.read(L,o)
                    ck(v in (0,1) and p.restrict(L,o)==p.reg(o,v),'sample is complete before fold')
                    ck(len(ss)==j,'fixed named scan index')
                    ss=ss+(v,)
                if i==k and pp[i] in ends:
                    j,o=ends[pp[i]]
                    ck(p.restrict(L,o)==p.reg(o,int(all(ss))),'accumulator exactly equals actual sampled prefix conjunction')
                put(nd,(pp,L,ss),r.serial(mass,ONE))
        d=nd;peak=max(peak,len(d))
    outcomes={}
    for (pcs,K,seen),mass in d.items():
        code=result_code(K)
        ck(code in ((0,0),(1,0),(0,1)),'no conflicting source assertion')
        ck(not code[0] or a.signed(source)==1,'YES has source witness')
        ck(not code[1] or a.signed(source)==0,'NO has complete named negative coverage')
        put(outcomes,code,mass)
        hr,wr,_=collector(k,True)
        L=execute(K,wr,H|hr)['end']
        ck(result_code(L)==((1,0) if a.signed(source) else (0,1)),'one complete later round after publication resolves')
    expected=b.old.positional_mass(lengths,0,0)[0]
    ck(total(d.values())==expected,'all shuffle history weights conserved')
    return dict(k=k,source=source,lengths=lengths,peak_states=peak,terminal_states=len(d),CWM=e.cw(expected),outcomes=[dict(code=c,CWM=e.cw(w)) for c,w in sorted(outcomes.items())])

def omission_family(source,k,f,overlap):
    H,J,S,WC,_=setup(source,k)
    basic=[p.one(4)]+producing(S,overlap)+WC
    W=a.rep(basic,f)
    d={(J,0):e.prep(J)}
    for op in W:
        nd={}
        for (K,j),mass in d.items():
            L,_=step(K,op,H);put(nd,(L,j),r.serial(mass,ONE))
            if j<f:put(nd,(K,j+1),r.serial(mass,ONE))
        d=nd
    reference=execute(J,basic,H)['end'];layers={}
    for (K,j),mass in d.items():
        ck(K==reference,'protected complete endpoint, not only same reported bit')
        put(layers,j,mass)
    ck(layers==a.layers(len(W),f),'all global-budget omission histories retained')
    return dict(k=k,f=f,source=source,overlap=overlap,length=len(W),layers=[dict(omissions=j,CWM=e.cw(w)) for j,w in sorted(layers.items())])

def erased_history_cases():
    """Actual differing sample histories, then identical final matching.

Each chosen subset publishes before this round's proposals. All remaining
producers finish before sampling, but their messages are proposed only after
sampling and folding. Thus the final messages are identical; the past snapshot
really differed. It is an explicitly lossy observation change, not fake data.
"""
    rows=[]
    for k in range(2,7):
        H,J,S,WC,stages=setup(p.reg(3,0),k)
        end_by_answer={};weights={};sample_patterns=[]
        for bits in product((0,1),repeat=k):
            early=[op for ss,v in zip(S,bits) if v for op in ss['W']]
            late=[op for ss,v in zip(S,bits) if not v for op in ss['W']]
            head=execute(J,[p.one(4)]+early+WC[:2*k]+late,H)['end']
            actual=tuple(int(ss['neg'] in head) for ss in S)
            ck(actual==bits,'genuine published message pattern before sampling')
            z=execute(head,WC[2*k:]+WC[:2*k],H)
            value=p.read(z['end'],700)
            ck(value==int(all(bits)), 'fold captures its actual earlier samples')
            if value in end_by_answer:ck(z['end']==end_by_answer[value],'same conjunction yields identical whole final state after later publication')
            else:end_by_answer[value]=z['end']
            put(weights,value,ONE);sample_patterns.append(bits)
        rows.append(dict(k=k,distinct_past_samples=len(sample_patterns),whole_final_states=len(end_by_answer),weights=[dict(answer=x,CWM=e.cw(w)) for x,w in sorted(weights.items())]))
    # Stage matters: a prefix consisting only of a negative source-contact
    # record is not proof that every lane has negative evidence.
    H,J,S,WC,stages=setup(p.reg(3,1),2)
    prod=[p.one(4),S[1]['W'][0]]+S[0]['W']+S[1]['W'][1:]
    K=execute(J,prod,H)['end']
    prefix=execute(K,WC[:stages[0]['end']],H,True)
    ck(p.read(prefix['end'],500)==1 and p.read(prefix['end'],stages[0]['acc'])==1,'prefix all-negative summary can coexist with true positive source')
    tail=execute(prefix['end'],WC[stages[0]['end']:],H,True)
    ck(result_code(tail['end'])==(1,0),'remaining named input discharges false early completeness inference')
    return dict(classes=rows,premature_completion=dict(prefix=prefix,suffix=tail))

def minimal_summary():
    rows=[]
    for j in range(1,7):
        classes={0:[],1:[]}
        for prefix in product((0,1),repeat=j):
            H,W=destructive_and(700,740,720)
            acc=prefix[0]
            for bit in prefix[1:]:
                K=execute(m.canon(p.reg(700,acc)+p.reg(740,bit)+p.reg(400,0)),W,H)['end']
                acc=p.read(K,720)
            classes[acc].append(prefix)
        ck(len(classes[0])==2**j-1 and len(classes[1])==1,'two future-conjunction equivalence classes at fixed index')
        rows.append(dict(prefix_length=j,class_sizes={str(v):len(ps) for v,ps in classes.items()}))
    return rows

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['cases','shuffle0','shuffle1','faults','erasure'],default='cases');ap.add_argument('--output',default='results.json');ns=ap.parse_args()
    if ns.mode=='cases':out=dict(gates=gate_cases(),truth=static_truth(),integration=integration_cases(),failures=failures(),minimal_summary=minimal_summary())
    elif ns.mode.startswith('shuffle'):
        bit=int(ns.mode[-1]);source=(a.HP,) if bit else m.canon((a.P,a.HN));out=dict(shuffle=shuffle(source))
    elif ns.mode=='erasure':out=erased_history_cases()
    else:
        out=dict(families=[omission_family((a.HP,) if bit else m.canon((a.P,a.HN)),k,f,overlap)
            for k in (2,3,6) for f in (1,2) for bit in (0,1) for overlap in (False,True)])
    out.update(schema='EM_STREAMING_RESIDUAL_FOLD_V1',checks=CHECKS,uncached_kernel_calls=CALLS,transition_uses=USES)
    Path(ns.output).write_text(json.dumps(out,ensure_ascii=False,separators=(',',':'))+'\n')
    print(json.dumps({key:out[key] for key in ('checks','uncached_kernel_calls','transition_uses')}))
if __name__=='__main__':main()
