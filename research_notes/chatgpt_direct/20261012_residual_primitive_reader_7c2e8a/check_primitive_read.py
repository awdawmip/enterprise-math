"""Fixed-word relational copying, majority and correction via pinned positive BRC.

Every transition uses the unchanged release/reserve kernel. Word builders depend
only on addresses, not on input values, success flags, or a majority oracle.
Cross-register triples are explicit NEW candidate permissions, not native physics.
Python 3.11+; standard library only. No inherited main suite is run.
"""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path

ROOT=Path(__file__).resolve().parent
P=ROOT/'pinned/exchange_core.py'
raw=P.read_bytes()
if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!='f45165d7144d342d6cf9233ea77a04a51d2b96e3':
    raise RuntimeError('parent source pin mismatch')
sp=importlib.util.spec_from_file_location('primitive_pinned_exchange',P)
e=importlib.util.module_from_spec(sp);sys.modules[sp.name]=e;sp.loader.exec_module(e)
m,r=e.m,e.r
ONE,ZERO=r.brc.CWM_ONE,r.brc.CWM_ZERO
CHECKS=0;PRIMITIVES=0;PROTOCOLS=0

def ck(ok,label):
    global CHECKS
    CHECKS+=1
    if not ok: raise AssertionError(label)

def reg(o,bit):
    if bit not in (0,1): raise ValueError('preparation bit must be zero or one')
    pattern=(((1,2,3),(4,5,6)),((1,2,4),(3,5,6)))[bit]
    return m.canon(tuple(o+x for x in h) for h in pattern)

def library(o):return set(reg(o,0)+reg(o,1))
def one(i):return ('release',i)
def add(h):return ('reserve',tuple(sorted(h)))
def restrict(J,o):return m.canon(h for h in J if set(h)<=set(range(o+1,o+7)))
def read(J,o):
    K=restrict(J,o)
    if not K:return None
    if set(K)<=set(reg(o,0)):return 0
    if set(K)<=set(reg(o,1)):return 1
    return 'OUTSIDE_LOCAL_ALPHABET'

def clear_word(o):return [one(o+1),one(o+5)]

def copy_program(src,dst,anc,clear_target=False):
    """A fixed 9/11-command program. Source full; private ancilla initially free."""
    if set(range(src+1,src+7))&set(range(dst+1,dst+7)):
        raise ValueError('overlapping registers')
    if anc in set(range(src+1,src+7))|set(range(dst+1,dst+7)):
        raise ValueError('ancilla overlaps data')
    probe=tuple(sorted((src+3,dst+3,anc)))
    H=library(src)|library(dst)|{probe}
    W=clear_word(dst) if clear_target else []
    W += [one(src+1),add(probe),add(reg(dst,1)[1]),add(reg(dst,0)[1]),
          one(anc),add(reg(src,0)[0]),add(reg(src,1)[0]),
          add(reg(dst,0)[0]),add(reg(dst,1)[0])]
    return H,W

def majority_program(probe_order=(0,1,2)):
    """Three inputs, three disposable copies, one output, one free ancilla."""
    inputs=(0,6,12);copies=(18,24,30);out=36;anc=43
    H=set().union(*(library(o) for o in inputs+copies+(out,)))
    W=clear_word(out)
    for src,dst in zip(inputs,copies):
        hh,ww=copy_program(src,dst,anc);H|=hh;W+=ww
    W += [one(o+1) for o in copies]
    probes=[tuple(sorted((a+3,b+3,out+3))) for a,b in combinations(copies,2)]
    H|=set(probes);W += [add(probes[i]) for i in probe_order]
    # Default-one first: a successful pair-zero probe inhibits this event.
    W += [add(reg(out,1)[1]),add(reg(out,0)[1])]
    for o in copies: W += [one(o+5),one(o+3)]
    W += [add(reg(out,0)[0]),add(reg(out,1)[0])]
    return H,W,probes

def correction_program():
    H,W,probes=majority_program()
    for dst in (0,6,12):
        hh,ww=copy_program(36,dst,43,True);H|=hh;W+=ww
    W += clear_word(36)
    return H,W,probes

def run(J,H,word,I,keep=False,protected=()):
    """No branch on a readout or success flag selects the next command."""
    global PRIMITIVES,PROTOCOLS
    PROTOCOLS+=1;initial=J;w=e.prep(J);trace=[]
    init_free=len(I)-len(m.used(J));peak=init_free
    ck(m.used(J)<=I,'preparation in declared inventory')
    protected_values={o:read(J,o) for o in protected}
    for n,op in enumerate(word,1):
        before=J;J,delta,ok=e.step(J,op,H);PRIMITIVES+=1
        w=r.serial(w,ONE)
        ck(m.used(J)<=I,'no invented or moved-to-unknown occurrence')
        ck(len(m.used(J))==3*len(J),'disjoint triadic allocation')
        ck(all(h in H for h in J),'all active events explicitly permitted')
        ck(w==ONE,'single deterministic source keeps CWM unit even when blocked')
        for o,value in protected_values.items():
            ck(read(J,o)==value,'protected source keeps logical information at each prefix')
        free=len(I)-len(m.used(J));peak=max(peak,free)
        if keep: trace.append(dict(index=n,command=op,success=ok,state=J,
                                  free_occurrences=free))
    return dict(initial=initial,end=J,commands=len(word),initial_free=init_free,
                peak_free=peak,CWM=e.cw(w),trace=trace)

def combined(bits,offsets=(0,6,12)):
    return m.canon(h for o,b in zip(offsets,bits) for h in reg(o,b))

def main():
    out={};I13=frozenset(range(1,14));H,W=copy_program(0,6,13)
    copies=[]
    for b in (0,1):
        ans=run(reg(0,b),H,W,I13,True,(0,))
        ck(ans['end']==combined((b,b),(0,6)),'fixed copier preserves source and makes equal target')
        ck(ans['commands']==9 and ans['peak_free']==10,'copy exact declared footprint/peak')
        copies.append(ans)
    _,target_catalog=e.catalog(library(6))
    ck(len(target_catalog)==7,'all seven target preparations from inherited BRC')
    hclear,wclear=copy_program(0,6,13,True);overwrites=[]
    for b in (0,1):
        for target in sorted(target_catalog):
            ans=run(m.canon(reg(0,b)+target),hclear,wclear,I13,False,(0,))
            ck(ans['end']==combined((b,b),(0,6)),'fixed overwrite handles all seven old target states')
            overwrites.append(dict(source=b,target=target,end=ans['end'],peak=ans['peak_free']))
    # Without the declared coupling, the target is a fixed default, not a copy.
    no_bridge=[]
    for b in (0,1):
        ans=run(reg(0,b),library(0)|library(6),W[:1]+W[2:],I13,True,(0,))
        ck(read(ans['end'],6)==1 and restrict(ans['end'],0)==reg(0,b),'omitting bridge removes transfer')
        no_bridge.append(ans)
    # The two head-only partial sources are erased by the first command.
    partial=[]
    for b in (0,1): partial.append(run(m.canon((reg(0,b)[0],)),H,W,I13,True))
    ck(partial[0]['end']==partial[1]['end'],'arbitrary readable partial sources are outside copier guarantee')
    # Exposed tails do retain their value, but are completed rather than exactly restored.
    for b in (0,1):
        ans=run(m.canon((reg(0,b)[1],)),H,W,I13,False,(0,))
        ck(ans['end']==combined((b,b),(0,6)),'canonical exposed tail can feed same construction')
    wrong_order=list(W);wrong_order[2],wrong_order[3]=wrong_order[3],wrong_order[2]
    wrong_order_run=run(reg(0,1),H,wrong_order,I13,True,(0,))
    ck(read(wrong_order_run['end'],6)==0,'phase priority is a real premise, not arbitrary permutation invariance')
    out['copy']=dict(traces=copies,overwrites=overwrites,no_bridge=no_bridge,wrong_order=wrong_order_run,
                     partial_source_collision=partial,library=sorted(H),word=W)
    # The NOT variant is a fixed relabeling of target members 3 and 4.
    def swap(x):return {9:10,10:9}.get(x,x)
    Hnot={tuple(sorted(map(swap,h))) for h in H}
    Wnot=[(op[0],swap(op[1])) if op[0]=='release' else add(map(swap,op[1])) for op in W]
    not_tr=[]
    for b in (0,1):
        ans=run(reg(0,b),Hnot,Wnot,I13,True,(0,))
        ck(ans['end']==combined((b,1-b),(0,6)),'fixed target rail exchange implements complement')
        not_tr.append(ans)
    out['not_gate']=not_tr
    HM,WM,probes=majority_program();I43=frozenset(range(1,44));truth=[];variants=0
    _,outcat=e.catalog(library(36))
    for bits in product((0,1),repeat=3):
        original=combined(bits);b=int(sum(bits)>=2) # expected answer: checker only
        ans=run(original,HM,WM,I43,True,(0,6,12))
        ck(ans['end']==m.canon(original+reg(36,b)),'majority retains exact original sources and clears all temporary events')
        ck(ans['commands']==45 and ans['peak_free']==28,'majority command and absolute free-resource count')
        truth.append(dict(input=bits,output=b,run=ans))
        for target in sorted(outcat):
            q=run(m.canon(original+target),HM,WM,I43,False,(0,6,12))
            ck(q['end']==ans['end'],'majority ignores old legal output after fixed clear')
        for perm in permutations(range(3)):
            hh,ww,_=majority_program(perm)
            q=run(original,hh,ww,I43,False,(0,6,12));variants+=1
            ck(q['end']==ans['end'],'all six pair-probe orders have identical full endpoints')
    out['majority']=dict(truth_table=truth,library=sorted(HM),word=WM,
                          probe_order_protocols=variants,inputs_preserved=True,
                          scratch_empty_at_end=True,original_is_not_runtime_argument=True)
    HC,WC,cprobes=correction_program();correct=[];faults=[];badwitness=None
    for bits in product((0,1),repeat=3):
        original=combined(bits);b=int(sum(bits)>=2);expected=combined((b,b,b))
        ans=run(original,HC,WC,I43,True)
        ck(ans['end']==expected,'all-eight fixed-word majority correction')
        ck(len(WC)==80 and ans['peak_free']==28,'correction includes cleanup and full resource accounting')
        q=run(ans['end'],HC,WC,I43)
        ck(q['end']==ans['end'],'complete-program endpoint idempotence')
        correct.append(dict(input=bits,output=b,run=ans))
        for omitted in range(len(WC)):
            qq=run(original,HC,WC[:omitted]+WC[omitted+1:],I43)
            data=tuple(read(qq['end'],o) for o in (0,6,12))
            success=qq['end']==expected
            faults.append(dict(input=bits,omitted=omitted+1,command=WC[omitted],
                               exact_expected_output=success,data=data,end=qq['end']))
            if bits==(0,0,1) and WC[omitted]==add(cprobes[0]):
                ck(qq['end']==combined((1,1,1)),'single omitted shared pair test corrupts all three commits')
                badwitness=run(original,HC,WC[:omitted]+WC[omitted+1:],I43,True)
    ck(badwitness is not None,'concrete one-command omission retained')
    out['correction']=dict(word=WC,library=sorted(HC),traces=correct,
                            single_omission_cases=faults,shared_omission_witness=badwitness,
                            single_omission_exact_successes=sum(x['exact_expected_output'] for x in faults))
    # Product of disjoint external frame and this machine is genuinely unchanged.
    frame=(1001,1002,1003)
    q=run(m.canon(combined((0,0,1))+(frame,)),HC|{frame},WC,I43|frozenset(frame))
    ck(q['end']==m.canon(combined((0,0,0))+(frame,)),'disjoint frame retained exactly')
    # BRC family: all eight proven inputs, with honest source multiplicity.
    family={}
    for row in correct:
        J=row['run']['end'];w=r.serial(r.edge(Fraction(1,8)),ONE)
        family[J]=r.merge(family.get(J,ZERO),w)
    ck(len(family)==2 and all(w.count==4 and w.total==Fraction(1,2) and w.dominant==Fraction(1,8) for w in family.values()),
       'coalesced outputs preserve original positive source mass and count')
    ck(r.total(family.values()).total==1,'no postselected mass removal')
    out['family']=[dict(state=J,CWM=e.cw(w)) for J,w in sorted(family.items())]
    # Source snapshots, program hashes, and execution scope are explicit.
    out.update(schema='EM_PRIMITIVE_RELATIONAL_READER_V1',
       event_id='EM-20261012-RESIDUAL-PRIMITIVE-READER-7C2E8A',
       global_read='1456227f3469360bf36a5ec7becb4938e4062f98',
       source_read='d659acfecf3727fc7b3dacb37e9038563c1fc389',
       status='CONDITIONAL_EXECUTED_TYPED_BRC_UNREVIEWED',
       assertions=CHECKS,primitive_calls=PRIMITIVES,protocols=PROTOCOLS,
       BRC_calls=dict(r.CALLS),new_cross_event_permissions=True,
       runtime_read_or_majority_oracle=False,native_permission_verified=False,
       independent_review=False,old_main_suites_executed=False)
    raw=(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    (ROOT/'results.json').write_bytes(raw)
    summary={key:out[key] for key in ('event_id','status','global_read','source_read','assertions','primitive_calls','protocols','BRC_calls')}
    summary.update(copy_commands=9,copy_with_overwrite_commands=11,majority_commands=45,
        correction_and_cleanup_commands=80,declared_occurrences=43,
        majority_absolute_peak_free=28,truth_table_inputs=8,omission_cases=len(faults),
        omission_exact_successes=out['correction']['single_omission_exact_successes'],
        results_bytes=len(raw),results_sha256=hashlib.sha256(raw).hexdigest(),
        inherited_helper_checks=e.CHECKS+m.CHECKS)
    (ROOT/'summary.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(summary,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
