#!/usr/bin/env python3
"""U15: sequential relative-state exchange and source-backed scratch reuse.

Conditional register protocol, not native force, energy or calibrated time.
Run python check_u15.py. Old BRC scientific functions are unchanged.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import gzip, hashlib, importlib.util, json, sys

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'retained_phase.py'
if not SRC.exists():
    SRC=ROOT.parent/'20261009_cell_u14_retained_phase_8f3c72'/'retained_phase.py'
raw=SRC.read_bytes()
PIN='713bf2ddcce9abd5f8b3ddbd9990f102055ce90d'
if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!=PIN:
    raise RuntimeError('U14 dependency mismatch')
spec=importlib.util.spec_from_file_location('u15_pinned_u14',SRC)
p=importlib.util.module_from_spec(spec);sys.modules[spec.name]=p;spec.loader.exec_module(p)
r=p.r;ZERO,ONE=p.ZERO,p.ONE

@dataclass(frozen=True)
class Registers:
    phases:tuple[int,int,int]
    scratch:tuple[int,int]
    arrival_residues:tuple[int,int,int]

def validate(x,k):
    if type(k) is not int or k<2:raise ValueError('finite modulus >=2')
    if len(x.phases)!=3 or len(x.scratch)!=2 or len(x.arrival_residues)!=3:
        raise ValueError('wrong register arity')
    if any(type(v) is not int or not 0<=v<k for v in x.phases+x.scratch+x.arrival_residues):
        raise ValueError('invalid finite register value')

def drift(x,k,amount=1):
    validate(x,k)
    return Registers(tuple((a+amount)%k for a in x.phases),x.scratch,x.arrival_residues)

def operation(x,k,tag,inverse=False):
    """Each declared logical interaction reads/writes at most three registers.

    XA reads A,R,u; XC reads C,R,v. UA reads u,T_A,T_R; UC reads v,T_C,T_R.
    Source timestamps are immutable side information, never modified here.
    Three register arguments do NOT certify a primitive three-force event.
    """
    validate(x,k);ph=list(x.phases);mem=list(x.scratch);tt=x.arrival_residues
    if tag in ('XA','XC'):
        side,slot=(0,0) if tag=='XA' else (2,1)
        old=ph[side];ph[side]=(ph[1]+mem[slot])%k
        mem[slot]=(old-ph[1])%k  # this three-register map is its own inverse
    elif tag in ('UA','UC'):
        side,slot=(0,0) if tag=='UA' else (2,1)
        residual=(tt[1]-tt[side])%k
        mem[slot]=(mem[slot]+(residual if inverse else -residual))%k
    else:raise ValueError('unknown operation')
    return Registers(tuple(ph),tuple(mem),tt)

def tick(x,k,tag,inverse=False):
    # One declared clock tick: common source drift, then one interaction.
    # A full inverse reverses interaction and drift, not the forward schedule.
    return drift(operation(x,k,tag,True),k,-1) if inverse else operation(drift(x,k),k,tag)

def run(x,k,tags=('XA','XC','UA','UC'),inverse=False):
    trace=[];weight=ONE
    for tag in (tuple(reversed(tags)) if inverse else tags):
        y=tick(x,k,tag,inverse)
        weight=r.serial(weight,r.edge(1))
        trace.append({'operation':tag,'inverse':inverse,'before':x,'after':y,
                      'weight':weight,'native_event':False})
        x=y
    return x,trace

def consistent_passive_input(x,k,tick_at_capture_completion):
    return x.phases==tuple((tick_at_capture_completion-t)%k for t in x.arrival_residues)

def admission(x,k,now,arrivals,H=None,source_ids=('A:0','R:0','C:0'),clean=True):
    """Check a prepared local transaction, no native action admission.

    Actual source records and blank scratch must already be at the same Cell.
    now is the last arrival tick; no intervening phase edit is permitted under
    this timestamp-only witness. A future interface must include such edits.
    """
    validate(x,k)
    if len(arrivals)!=3 or any(type(t) is not int or t<1 for t in arrivals):
        raise ValueError('three actual arrival times')
    if len(source_ids)!=3 or len(set(source_ids))!=3:raise ValueError('distinct source occurrences')
    if now!=max(arrivals):raise ValueError('start at actual final arrival')
    if x.arrival_residues!=tuple(t%k for t in arrivals):raise ValueError('record/version mismatch')
    if not consistent_passive_input(x,k,now):raise ValueError('timestamp-only witness is stale')
    if x.scratch!=(0,0):raise ValueError('scratch is not blank')
    duration=4 if clean else 2
    if H is not None and (type(H) is not int or H<0):raise ValueError('nonnegative lifetime')
    if H is not None and now-min(arrivals)+duration>H:
        return {'status':'INSUFFICIENT_REMAINING_WINDOW','input':x,'trace':[],
                'source_ids':source_ids,'native_firing':False}
    tags=('XA','XC','UA','UC') if clean else ('XA','XC')
    y,tr=run(x,k,tags)
    # Observer output reserves these sources once; no material head is bound.
    return {'status':'CALIBRATED_RESERVED','input':x,'output':y,'trace':tr,
            'start_tick':now,'end_tick':now+duration,'arrivals':arrivals,
            'retained_source_ids':source_ids,'scratch_ids':('local-u','local-v'),
            'scratch_blank':y.scratch==(0,0),'native_firing':False,'head_binding':False,
            'history_erased':False,'reissue_allowed':False}

def encode(x):
    if isinstance(x,Registers):return {'phases':x.phases,'scratch':x.scratch,'arrival_residues':x.arrival_residues}
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return p.encode(x)

checks=0

def ck(test,label):
    global checks
    checks+=1
    if not test:raise AssertionError((checks,label))

def main():
    global checks
    checks=0;exhaust=[]
    # Full eight-register maps for small alphabets, without restricting histories.
    for k in (2,3):
        seen=set();count=ZERO
        for values in product(range(k),repeat=8):
            x=Registers(values[:3],values[3:5],values[5:])
            y,tr=run(x,k);back,_=run(y,k,inverse=True)
            ck(back==x,'all eight registers exactly restored by the actual inverse')
            ck(y.arrival_residues==x.arrival_residues,'side information not overwritten')
            seen.add(y);count=r.merge(count,tr[-1]['weight'])
        ck(len(seen)==k**8,'complete finite permutation')
        ck(count.count==count.total==k**8 and count.dominant==1,'actual BRC population of complete maps')
        exhaust.append({'k':k,'states':len(seen),'CWM':count})

    # Gates commute with common source drift, and XA/XC commute at fixed clock.
    local_checks=0
    for k in range(2,8):
        for a,b,u in product(range(k),repeat=3):
            x=Registers((a,b,0),(u,0),(0,0,0))
            y=operation(x,k,'XA');z=operation(y,k,'XA')
            ck(z==x,'relative exchange involution')
            ck(operation(drift(x,k),k,'XA')==drift(y,k),'relative storage is covariant to common drift')
            ck(operation(operation(x,k,'XA'),k,'XC')==operation(operation(x,k,'XC'),k,'XA'),
               'two exchanges algebraically commute despite serialized implementation')
            local_checks+=1

    # Positive clean implementation on passive-consistent captured snapshots.
    clean_counts=[]
    for k in range(2,7):
        total=ZERO
        for now_res,*times in product(range(k),repeat=4):
            ph=tuple((now_res-t)%k for t in times)
            x=Registers(ph,(0,0),tuple(times));y,tr=run(x,k)
            ck(len(set(y.phases))==1 and y.scratch==(0,0),'clean alignment on timestamp-consistent subspace')
            ck(y.phases[1]==(ph[1]+4)%k,'four actual drift ticks, not one renamed tick')
            two,_=run(x,k,('XA','XC'))
            old_ph,old_mem=p.exchange_align(ph,(0,0),k)
            ck(two.phases==tuple((a+1)%k for a in old_ph) and two.scratch==old_mem,
               'two-tick circuit realizes U14 plus the extra declared common drift')
            total=r.merge(total,tr[-1]['weight'])
        clean_counts.append({'k':k,'states':k**4,'CWM':total})

    # Directly consume an actual U14 route with retained, not fired, inputs.
    model=p.Protocol(4,(1,1,1),None)
    source_trace=model.trace([(1,1,1),(0,1,0),(0,1,0)])
    last=source_trace[-1];arr=last['arrival_ticks'];ph=last['state'].phases
    x=Registers(ph,(0,0),tuple(t%4 for t in arr))
    example=admission(x,4,3,arr,6)
    y=example['output']
    ck(ph==(2,0,2) and arr==(1,3,1),'original A/R/C retained source preparation')
    ck([t['after'].phases for t in example['trace']]==[(1,1,3),(2,2,2),(3,3,3),(0,0,0)],'all four intermediate source phases')
    ck([t['after'].scratch for t in example['trace']]==[(2,0),(2,2),(0,2),(0,0)],'scratch residual transfer and source-backed cleanup')
    ck(y.phases==(0,0,0) and y.scratch==(0,0),'exact main output')
    ck(not consistent_passive_input(y,4,7),'old arrival times alone no longer describe post-intervention phases')
    # Blindly use the same old timestamps on a new matching-phase snapshot.
    wrong=Registers((0,0,0),(0,0),x.arrival_residues)
    wrong_y,_=run(wrong,4)
    ck(wrong_y.scratch==(2,2),'uncertified stale history leaves nonblank records')
    try:admission(wrong,4,7,(5,7,5),None)
    except ValueError:ck(True,'stale timestamp witness rejected before update')
    else:ck(False,'stale witness admitted')
    for H in range(8):
        ans=admission(x,4,3,arr,H)
        ck((ans['status']=='CALIBRATED_RESERVED')==(H>=6),'full four-stage deadline includes original age2')
    ck(admission(x,4,3,arr,4,clean=False)['output'].scratch==(2,2),'two-stage result is aligned but scratch not recycled')

    # A finite controller cannot reset its correlated memory independently.
    # Exact fixed-reference relative fibers: no side information / sum / full pair.
    fibres=[]
    for k in range(2,9):
        maps={'none':{},'sum':{},'pair':{}}
        for da,dc in product(range(k),repeat=2):
            for name,h in (('none',0),('sum',(da+dc)%k),('pair',(da,dc))):
                maps[name].setdefault(h,[]).append((da,dc))
        sizes={name:max(map(len,table.values())) for name,table in maps.items()}
        ck(sizes=={'none':k*k,'sum':k,'pair':1},'conditional recoverability capacity')
        # Sum side information plus one relative component reconstructs both.
        for da,dc in product(range(k),repeat=2):
            h=(da+dc)%k
            ck((h-da)%k==dc,'one k-state residual is sufficient with sum side information')
        fibres.append({'k':k,'largest_indistinguishable_fibre':sizes})

    # Same marginal memory values, different source-memory association.
    correlation=[]
    for k in (2,3,4,5):
        correct=wronglaw=ZERO;full_correct={};full_wrong={};qm=p.lift(Q(1,k*k))
        scratch_laws=[{},{}];history_laws=[{},{}]
        for da,dc in product(range(k),repeat=2):
            yy=Registers((0,0,0),(da,dc),((-da)%k,0,(-dc)%k))
            zz=Registers((0,0,0),((da+1)%k,dc),yy.arrival_residues)
            for index,(inp,law) in enumerate(((yy,full_correct),(zz,full_wrong))):
                p.add(scratch_laws[index],inp.scratch,qm)
                p.add(history_laws[index],inp.arrival_residues,qm)
                out=operation(operation(inp,k,'UA'),k,'UC')
                p.add(law,out.scratch,qm)
        ck(scratch_laws[0]==scratch_laws[1] and history_laws[0]==history_laws[1],
           'both separate joint marginal CWM tables identical before cleanup')
        correct=full_correct.get((0,0),ZERO);wronglaw=full_wrong.get((0,0),ZERO)
        ck(correct.total==1 and wronglaw.total==0,'joint association controls cleanup though marginals agree')
        ck(full_wrong[(1,0)].total==1,'wrong association retains one full modular offset')
        correlation.append({'k':k,'correct_blank':correct.total,'wrong_blank':wronglaw.total,
                            'correct_law':full_correct,'wrong_law':full_wrong,
                            'scratch_marginal':scratch_laws[0],'history_marginal':history_laws[0]})

    # Execute all finite arrival-time combinations; join with unchanged BRC
    # first-arrival populations and compare against shifted U13 first-event law.
    horizon=10;probs=(Q(1,2),)*3;lengths=(1,3,1)
    singles=[p.f.first_arrivals(n,a,horizon) for n,a in zip(lengths,probs)]
    timing=[];route_cases=0
    for duration in (2,4):
        for H in range(11):
            byfinish={};accepted=ZERO;allmass=ZERO
            for arrivals in product(range(1,horizon+1),repeat=3):
                factors=[singles[i][t-1] for i,t in enumerate(arrivals)]
                if not all(w.live for w in factors):continue
                w=r.serial(r.serial(factors[0],factors[1]),factors[2]);allmass=r.merge(allmass,w)
                now=max(arrivals);regs=Registers(tuple((now-t)%4 for t in arrivals),(0,0),tuple(t%4 for t in arrivals))
                result=admission(regs,4,now,arrivals,H,clean=(duration==4))
                good=result['status']=='CALIBRATED_RESERVED'
                ck(good==(max(arrivals)-min(arrivals)<=H-duration),'duration is deducted from storage tolerance')
                route_cases+=1
                if good:
                    ck(len(set(result['output'].phases))==1,'actual sequential result aligned at finish')
                    accepted=r.merge(accepted,w);p.add(byfinish,now+duration,w)
            if H>=duration:
                curve=p.f.joined_first_curve(lengths,probs,H-duration,horizon)
                for tick_at_ready,ww in enumerate(curve,1):
                    ck(byfinish.get(tick_at_ready+duration,ZERO)==ww,'new full C/W/M completion curve equals shifted source curve')
                protocol=p.f.Protocol(p.f.example_plans(),probs,H-duration)
                eventual=protocol.solve(protocol.initial())[0]
            else:eventual=Q(0)
            ck(accepted.total<=eventual,'finite positive prefix never substitutes for all future')
            timing.append({'duration':duration,'H':H,'eventual_success':eventual,
                           'prefix_success':accepted,'by_completion_tick':byfinish})
    clock_exact={f"d{a['duration']}_H{a['H']}":str(a['eventual_success']) for a in timing if a['H'] in (2,4,6,8,10)}
    ck(clock_exact['d4_H4']=='1/343' and clock_exact['d4_H6']=='849/5488','main clean-protocol lifetime fractions')

    summary={'schema':'CELL_U15_SEQUENTIAL_CLEANUP_RESULTS_V1',
      'event_id':'EM-20261009-CELL-U15-SEQUENTIAL-CLEANUP-9D2F60',
      'checks':checks,'BRC_calls':dict(r.CALLS),'full_eight_register_states':sum(a['states'] for a in exhaust),
      'local_three_register_inputs':local_checks,'consistent_captured_snapshots':sum(a['states'] for a in clean_counts),
      'finite_arrival_protocol_cases':route_cases,'new_infinite_statement':'P_success(H,d)=P_U13(H-d) for H>=d; 0 otherwise',
      'example_start_tick':3,'example_end_tick':7,'example_output':encode(y),
      'exact_deadline_results':clock_exact,'side_information_fibre_checks':fibres,
      'joint_record_association_binary_TV':'1','scratch_recycled_only_with_valid_side_information':True,
      'native_force':False,'native_triad_certificate':False,'material_head_bound':False,
      'physical_clock':False,'mechanical_reaction':False,'prime_claim':False,'independent_review':False,
      'registration':'PRIOR_PLATFORM_BLOCK_PRESERVED_NO_RETRY',
      'old_full_suites_rerun':False}
    trace={'full_map_census':exhaust,'consistent_inputs':clean_counts,'source_preparation':source_trace,
           'example':example,'wrong_history_output':wrong_y,'conditional_fibres':fibres,
           'correlation_witnesses':correlation,'deadline_composition':timing}
    raw=(json.dumps(encode(trace),sort_keys=True,separators=(',',':'))+'\n').encode()
    packed=gzip.compress(raw,mtime=0);ev=ROOT/'evidence';ev.mkdir(exist_ok=True)
    (ev/'full_trace.json.gz').write_bytes(packed)
    summary.update(trace_bytes=len(raw),trace_sha256=hashlib.sha256(raw).hexdigest(),trace_compressed_sha256=hashlib.sha256(packed).hexdigest())
    (ev/'results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
