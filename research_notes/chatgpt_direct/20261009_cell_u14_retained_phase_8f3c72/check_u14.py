#!/usr/bin/env python3
"""U14 exact BRC checks. Not independent review, physical force or prime law."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import hashlib, json, gzip
import retained_phase as p
r=p.r
ROOT=Path(__file__).resolve().parent;EV=ROOT/'evidence';EV.mkdir(exist_ok=True)
checks=0

def ck(x,label):
    global checks
    checks+=1
    if not x:raise AssertionError((checks,label))

runs=[];traces=[]
# Full finite prefixes and infinite/finite-window positive-cycle solves.
params=((Q(1,2),)*3,(Q(1,3),)*3,(Q(1,2),Q(1,3),Q(2,3)))
for probs in params:
    for k in (1,2,3,4):
        for H in (0,1,2,4,None):
            model=p.Protocol(k,probs,H)
            vals=model.solve(model.initial());prefix=model.prefixes(10)
            original=model.base.solve(model.base.initial())
            ck(vals[0]+vals[1]==original[0] and vals[2]==original[1],
               'phase test partitions original readiness without changing transport or expiry')
            direct=p.joined_curve(model.lengths,model.a,k,H,10)
            accum=[p.ZERO]*3
            for n in range(10):
                for i,key in enumerate(('hit','phase_block','expired')):
                    accum[i]=r.merge(accum[i],prefix[key][n])
                ck(prefix['hit'][n]==direct[n],'finite first-ready identity in full C/W/M')
                ck(r.total(accum+[prefix['survival'][n]]).total==1,'ready,blocked,expired,live conservation')
                ck(accum[0].total<=vals[0]<=accum[0].total+prefix['survival'][n].total,
                   'finite prefix versus all-time result')
            for rec in tuple(model.closure_records):
                x=rec['state'];incoming=[p.ZERO]*3
                for bits,y,w in model.row(x):
                    for i,val in enumerate(model.solve(y)):
                        incoming[i]=r.merge(incoming[i],r.serial(w,p.lift(val)))
                ck(tuple(a.total for a in incoming)==rec['outcomes'],'every all-time first-step equation')
            if H is None:
                reference,rr=p.infinite_phase_success(model.lengths,model.a,k)
                ck(vals[0]==reference,'independent positive residue convolution equals orbit closure')
                ck(vals[2]==0 and vals[0]+vals[1]==1,'all sources arrive but phases may remain incompatible')
            if k==1:
                inherited=model.base.solve(model.base.initial())
                ck(vals[0]==inherited[0] and vals[2]==inherited[1] and vals[1]==0,
                   'no phase restriction reduces exactly to U13 interface')
            if H is not None and H<k:
                fresh_model=p.f.Protocol(model.plans,model.a,0)
                fresh=fresh_model.solve(fresh_model.initial())
                ck(vals[0]==fresh[0],'subperiod lifetime cannot accept nonsimultaneous residues')
            runs.append({'a':probs,'k':k,'H':H,'outcomes':vals,'transient_states':len(model.closure_records)})
            traces.append({'a':probs,'k':k,'H':H,'prefix':prefix,'positive_cycle_certificates':model.closure_records})

# Exact all-time values, divisibility inclusion and finite-window plateaus.
infinite=[]
for k in (1,2,3,4,6,8):
    model=p.Protocol(k);val=model.solve(model.initial())[0]
    direct,residues=p.infinite_phase_success(model.lengths,model.a,k)
    ck(val==direct,'all-time cyclic residue law')
    infinite.append({'k':k,'success':val,'residues':residues})
byk={x['k']:x['success'] for x in infinite}
ck(byk[2]==Q(23,81),'binary exact plateau')
ck(byk[4]==Q(4631,50625),'four-state exact plateau')
for small,large in ((1,2),(2,4),(4,8),(2,6),(3,6)):
    ck(byk[large]<=byk[small],'divisor relation gives nested compatibility, not primality')
windows=[]
for k in (2,3,4):
    last=None
    for H in range(9):
        model=p.Protocol(k,window=H);val=model.solve(model.initial())[0]
        rounded=p.Protocol(k,window=(H//k)*k)
        ck(val==rounded.solve(rounded.initial())[0],'window depends on floor(H/k) under congruence')
        if last is not None:ck(val>=last,'same probability space, nested lifetime events')
        windows.append({'k':k,'H':H,'success':val});last=val

# Deterministic arrival ages (2,0,2) pass period2 but never align for period4.
deterministic=[]
for k,want in ((1,True),(2,True),(3,False),(4,False)):
    model=p.Protocol(k,(1,1,1),None)
    tr=model.trace([(1,1,1),(0,1,0),(0,1,0)])
    ck(tr[-1]['ages']==(2,0,2),'actual retained arrival ages')
    ck((tr[-1]['state'].outcome=='READY_RESERVED')==want,'period-specific compatibility')
    ck(sum(model.solve(model.initial()))==1,'deterministic terminal law')
    deterministic.append({'k':k,'trace':tr})

# Same coarse header AND same maximum age, but different relative phases.
age_witness=[]
for H,want in ((4,Q(1,4)),(None,Q(1,3))):
    model=p.Protocol(2,window=H)
    old=model.trace([(1,0,1),(0,1,0),(0,1,0)])
    other=model.trace([(1,0,0),(0,1,1),(0,1,0)])
    x,y=old[-1],other[-1]
    ck(x['cells']==y['cells'] and x['state'].progress==y['state'].progress==(1,2,1),'same actual source positions and progress')
    ck(x['occurrences']==y['occurrences'],'same source ownership')
    ck(max(a for a in x['ages'] if a is not None)==max(a for a in y['ages'] if a is not None)==2,'same true maximum age')
    ck(x['state'].oldest==y['state'].oldest,'same U13-style compressed age')
    a=model.solve(x['state']);b=model.solve(y['state'])
    ck(a[0]==want and b[0]==0,'phase relationship invisible to maximum age changes future readiness')
    ck(x['weight'].total>0 and y['weight'].total>0,'both preparations use positive actual paths')
    age_witness.append({'H':H,'P':old,'Q':other,'P_outcomes':a,'Q_outcomes':b,
                        'ready_binary_TV':a[0]-b[0]})

# Exact scope certificate: full ages -> progress,max-age,age residues.
quotients=[]
for k in (2,3,4):
    for H in (2,3,4):
        model=p.Protocol(k,window=H);live={((0,0,0),(None,None,None)):p.ONE};hits=[]
        for tick in range(1,8):
            nxt={};hit=p.ZERO
            for (progress,ages),mass in live.items():
                phases=tuple(None if a is None else a%k for a in ages)
                compact=p.State(progress,phases,max((a for a in ages if a is not None),default=None))
                active=[i for i,j in enumerate(progress) if j<model.lengths[i]]
                for selected in product((0,1),repeat=len(active)):
                    bits=[0]*3;q=p.ONE
                    for i,b in zip(active,selected):bits[i]=b;q=r.serial(q,model.factors[i][b])
                    pp=tuple(j+b for j,b in zip(progress,bits))
                    aa=tuple(a+1 if a is not None else (0 if j==n else None)
                             for a,j,n in zip(ages,pp,model.lengths))
                    ph=tuple(None if a is None else a%k for a in aa)
                    mx=max((a for a in aa if a is not None),default=None)
                    if all(a is not None for a in aa):
                        out='READY_RESERVED' if len(set(ph))==1 else 'PHASE_BLOCKED_RETAINED'
                    elif mx is not None and mx>=H:out='EXPIRED_RETAINED'
                    else:out='PENDING'
                    yy=model.step(compact,tuple(bits))
                    ck(yy==p.State(pp,ph,mx,out),'full-age to modular-age exact transition intertwining')
                    term=r.serial(mass,q)
                    if out=='READY_RESERVED':hit=r.merge(hit,term)
                    elif out=='PENDING':p.add(nxt,(pp,aa),term)
            live=nxt;hits.append(hit)
        ck(hits==model.prefixes(7)['hit'],'full finite history and sufficient phase quotient agree in CWM')
        quotients.append({'k':k,'H':H,'hits':hits,'remaining_full_states':len(live)})

# Common invertible drift cannot turn unequal phases into equal phases.
# Exhaust small alphabets and all input triples, not new force dynamics.
for k in range(1,7):
    for ph in product(range(k),repeat=3):
        equal=len(set(ph))==1
        ck((len(set(p.common_shift(ph,k)))==1)==equal,'common invertible update preserves equality gate')

# Positive construction: a two-memory reversible local coupling at the common
# target transfers offsets instead of erasing them. All involved registers
# have explicit input identities; these are not primitive force occurrences.
align=[]
for k in (2,3,4,5):
    seen=set()
    for ph in product(range(k),repeat=3):
        for mem in product(range(k),repeat=2):
            new,records=p.exchange_align(ph,mem,k)
            ck(p.exchange_align(new,records,k,True)==(ph,mem),'complete reversible register map')
            seen.add((new,records))
            if mem==(0,0):ck(len(set(new))==1,'supplied blank records align the visible phases')
    ck(len(seen)==k**5,'finite mapping injective and surjective')
    recovered={}
    for a,c in product(range(k),repeat=2):
        ph=(a,0,c);new,mem=p.exchange_align(ph,(0,0),k)
        recovered[mem]=ph
        again,oldmem=p.exchange_align(new,mem,k)
        ck(tuple((v-ph[1])%k for v in ph)==tuple((v-again[1])%k for v in again),
           'reusing uncleared records brings the old relative offsets back')
        ck(oldmem==(0,0),'two exchanges restore memory but not a permanent reset')
    ck(len(recovered)==k*k,'all relative pairs require distinct recoverable outputs within stated carrier')
    align.append({'k':k,'full_map_states':k**5,'relative_input_states':k*k})
ph=(2,0,2);mem=(0,0);trace=[];weight=p.ONE
for update in range(2):
    new,records=p.exchange_align(ph,mem,4)
    weight=r.serial(weight,r.edge(1))
    trace.append({'phases_in':ph,'memories_in':mem,'phases_out':new,'memories_out':records,
                  'local_cell':p.m.endpoint(p.f.example_plans()[0].source,p.f.example_plans()[0].word),'positive_trace_weight':weight,
                  'source_ids':['A:one-use-0','R:one-use-0','C:one-use-0'],
                  'memory_ids':['prepared-local-memory-A','prepared-local-memory-C'],
                  'native_firing':False})
    ph,mem=new,records
ck(trace[0]['phases_out']==(1,1,1) and trace[0]['memories_out']==(2,2),'exact four-phase offset transfer')
ck(trace[1]['phases_out']==(0,2,0),'unchanged memory cannot be treated as a blank reservoir')

# All-future H->infinity loss bounds. They tend to phase-compatible mass, not1.
tails=[]
for k in (2,4):
    for H in (8,16,32):
        n=H+1;bernoulli={0:p.ONE}
        for _ in range(n):
            nxt={}
            for j,w in bernoulli.items():
                p.add(nxt,j,r.serial(w,r.edge(Q(1,2))))
                p.add(nxt,j+1,r.serial(w,r.edge(Q(1,2))))
            bernoulli=nxt
        bound=min(Q(1),r.total([bernoulli[0],bernoulli[0]]+[bernoulli[j] for j in (0,1,2)]).total)
        model=p.Protocol(k,window=H);val=model.solve(model.initial())[0]
        ck(0<=byk[k]-val<=bound,'finite lifetime error around a strictly subunit phase plateau')
        ck(bound==min(Q(1),Q(3+n+n*(n-1)//2,2**n)),'positive word-tail coefficient identity')
        tails.append({'k':k,'H':H,'success':val,'infinite_success':byk[k],'loss_upper':bound})

summary={'schema':'CELL_U14_RETAINED_PHASE_RESULTS_V1','event_id':'EM-20261009-CELL-U14-RETAINED-PHASE-8F3C72',
 'checks':checks,'BRC_calls':dict(r.CALLS),'parameter_window_cases':len(runs),'prefix_horizon':10,
 'infinite_phase_success':{str(a['k']):str(a['success']) for a in infinite},
 'binary_phase_window_success':{str(a['H']):str(a['success']) for a in windows if a['k']==2},
 'age_witness':{'H4_ready':['1/4','0'],'infinite_ready':['1/3','0'],'same_maximum_age':2},
 'logical_alignment':{'input_phases':[2,0,2],'blank_memories':[0,0],'output_phases':[1,1,1],
                      'output_memories':[2,2],'second_use_phases':[0,2,0]},
 'native_force':False,'native_incidence':False,'native_firing':False,'physical_clock':False,
 'physical_reaction':False,'prime_claim':False,'independent_review':False,
 'registration':'PRIOR_PLATFORM_BLOCK_PRESERVED_NO_RETRY','unchanged_source':'U13_U12_U11_U9_U8_U2_WEIGHTED_BRC'}
alltrace={'runs':runs,'certificates_and_prefixes':traces,'infinite_residues':infinite,'windows':windows,
          'deterministic':deterministic,'age_witness':age_witness,'quotient_checks':quotients,
          'alignment_exhaustion':align,'alignment_trace':trace,'tail_bounds':tails}
raw=(json.dumps(p.encode(alltrace),sort_keys=True,separators=(',',':'))+'\n').encode()
packed=gzip.compress(raw,mtime=0);(EV/'full_trace.json.gz').write_bytes(packed)
summary.update(trace_bytes=len(raw),trace_sha256=hashlib.sha256(raw).hexdigest(),trace_compressed_sha256=hashlib.sha256(packed).hexdigest())
(EV/'results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
