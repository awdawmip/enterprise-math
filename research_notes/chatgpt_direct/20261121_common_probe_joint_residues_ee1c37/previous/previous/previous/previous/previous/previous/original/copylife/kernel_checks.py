"""Original BRC schedules with copies/drops and typed observation reuse.
All complete initial tables appear only in Physical (preparation and independent
audit). Ledger and its decisions only receive real reader/business answers.
"""
from __future__ import annotations
import argparse
import json
from dataclasses import dataclass
from itertools import product
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'optimization'))
import check_cost_aware_kernel as core
from bellman_planner import key_cost

CHECKS=0
def ck(value,msg):
    global CHECKS
    CHECKS+=1
    if not value: raise AssertionError(msg)

@dataclass(eq=False)
class Fact:
    who:str
    mask:int=0
    value:int=0
    nonempty:bool|None=None
    price_class:tuple|None=None

class Ledger:
    def __init__(self,r,q,limit,*,use_copy=True,use_presence=True,use_price=False):
        self.r,self.q,self.limit=r,q,limit
        self.use_copy,self.use_presence,self.use_price=use_copy,use_presence,use_price
        self.slots=[Fact('old:'+str(i)) for i in range(r)];self.serial=0

    def learn(self,index,b,v):
        f=self.slots[index];flag=1<<b
        ck(not (f.mask&flag) or bool(f.value&flag)==bool(v),'answers on one lineage consistent')
        f.mask|=flag
        if v:f.value|=flag

    def exact(self,f,k):
        ck((k&f.mask)==f.value and (f.nonempty is None or f.nonempty==bool(k)),'disclosed full value consistent with prior evidence')
        f.mask=(1<<self.q)-1;f.value=k;f.nonempty=bool(k)

    def copy(self,d,s,out,*,code=None,price=None):
        f=self.slots[s]
        if d!=s:
            if self.use_copy:
                if code is None:raise ValueError('missing permitted complete addressed-copy return')
                self.exact(f,code)
            elif code is not None:raise ValueError('unpermitted copy return')
            if self.use_price:
                if price is None:raise ValueError('missing charged command length')
                def pi(k):
                    if not k:return 9*self.q+1
                    return 9*self.q+2+k.bit_count()+4*(1-((k>>(self.q-1))&1))
                f.price_class=tuple(k for k in range(self.limit+1) if pi(k)==price)
            elif price is not None:raise ValueError('unpermitted command length')
            self.slots[d]=f
        else:
            if code is not None or price is not None:raise ValueError('self-copy has no full-value return')
        if self.use_presence:
            ck(f.nonempty is None or f.nonempty==bool(out),'retained presence answer consistent')
            f.nonempty=bool(out)
            if not out:self.exact(f,0)

    def drop(self,d,out):
        if self.use_presence:
            f=self.slots[d]
            if f.nonempty is not None:ck(f.nonempty==bool(out),'drop returns previous presence')
            f.nonempty=bool(out)
            if not out:self.exact(f,0)
        self.slots[d]=Fact('empty',(1<<self.q)-1,0,False)

    def bind(self,d,k):
        self.serial+=1; self.slots[d]=Fact('write:'+str(self.serial),(1<<self.q)-1,k,bool(k))

    def blocks(self,k):
        return tuple(i for i,f in enumerate(self.slots) if f.nonempty is not False and k&f.mask==f.value and (f.price_class is None or k in f.price_class))

    def snapshot(self):
        return [dict(origin=f.who,mask=f.mask,value=f.value,present=f.nonempty) for f in self.slots]

    def action(self,t,preferred=None):
        legal=range(t*(self.r+1)+1,(t+1)*(self.r+1)+1)
        if preferred is not None and preferred not in legal:raise ValueError('invalid preferred key')
        if preferred is not None and not self.blocks(preferred):return ('create',preferred)
        safe=[k for k in legal if not self.blocks(k)]
        if safe:return ('create',min(safe,key=lambda k:(key_cost(k,self.r.bit_length()),k)))
        for b in range(self.q):
            for i,f in enumerate(self.slots):
                if not f.mask>>b&1:return ('read',i,b)
        raise AssertionError('r+1 choices cannot all be blocked by r exact slots')

class Physical:
    def __init__(self,C,initial,*,capture=False,**features):
        self.C=C;self.initial=tuple(initial)
        self.table=((None,)*C.d,tuple(None if k==0 else divmod(k-1,C.colors) for k in initial))
        self.cache=C.initial_cache(self.table);self.J=C.encode(self.table,False,self.cache)
        self.ledger=Ledger(C.slots,C.bits,C.d*C.colors,**features)
        self.cost=0;self.probes=0;self.events=[];self.copy_bits=0
        self.rounds=0;self.copies=0;self.capture=capture;self.states=[];self.raw_words=[];self.extras=()

    def encoded(self,table,answer,cache):
        return core.directed.m.canon(self.C.encode(table,answer,cache)+self.extras)

    def runword(self,J,word):
        K,w,log=self.C.runword(J,word,trace=self.capture)
        if self.capture:
            self.states.extend(row['after'] for row in log);self.raw_words.extend(word)
        return K,w,log

    def addressed(self,J,op):
        K,w,data=self.C.addressed(J,op,trace=self.capture)
        if self.capture:
            self.states.extend(row['after'] for row in data['trace']);self.raw_words.extend(data['word'])
        return K,w,data

    def codes(self):return tuple(0 if v is None else self.C.key(*v) for v in self.table[1])

    def observation_audit(self):
        codes=self.codes()
        for k,f in zip(codes,self.ledger.slots):
            ck((k&f.mask)==f.value and (f.nonempty is None or f.nonempty==bool(k)) and (f.price_class is None or k in f.price_class),'every evidence bit and every presence answer sound')
        for i,f in enumerate(self.ledger.slots):
            for j,g in enumerate(self.ledger.slots):
                if f is g:ck(codes[i]==codes[j],'retained aliases have equal physical full identity')

    def checked(self,op,J,mass,entry=None):
        self.table,ans,self.cache=core.old.expected_selected(self.C,self.table,self.cache,op,entry or {})
        ck(mass.count==1 and J==self.encoded(self.table,ans,self.cache),'independent full matching incl sources, references, shared keys, output, scratch')
        self.J=J;return bool(ans)

    def probe(self,i,b):
        w=self.C.reads[i,b]
        J,mass,_=self.runword(self.J,w);v=int(self.C.observe_result(J))
        ck(len(w)==8 and mass.count==1 and J==self.encoded(self.table,bool(v),self.cache),'original individual reader is nonmutating')
        self.J=J;self.cost+=len(w);self.probes+=1
        self.ledger.learn(i,b,v);self.observation_audit()
        self.events.append(dict(op=['read',i,b],answer=v,commands=len(w),cumulative=self.cost))
        return v

    def copy(self,d,s):
        C=self.C;before=self.codes();op=('copy',d,s)
        J,w,data=self.addressed(self.J,op);v=self.checked(op,J,w)
        obs=data['observations']
        if d!=s:
            ck(len(obs)==C.bits and all(row[0]=='reference_key_bit' and row[1]==s and row[2]==j for j,row in enumerate(obs)),'addressed copy returns all q bits in order')
            k=sum(row[3]<<j for j,row in enumerate(obs));last=(k>>(C.bits-1))&1
            ck(k==data['code']==before[s],'actual q-bit copy transcript and delivered code agree with physical key')
            expected=(9*C.bits+2+k.bit_count()+4*(1-last)) if k else 9*C.bits+1
            evidence=tuple(a for row in obs for a in C.reads[s,row[2]])
            ck(data['word']==evidence+C.address_writes[d,k,last],'copy has original q reader words followed by original addressed writer')
            self.copy_bits+=len(obs);self.copies+=1
        else:
            k=None;expected=len(C.base_programs[op])
            ck(not obs,'self-copy has no bit transcript')
            ck('code' not in data and tuple(data['word'])==tuple(C.base_programs[op]),'same-slot branch has no value disclosure')
        ck(data['commands']==expected,'physical copy length equals exact formula')
        self.ledger.copy(d,s,v,code=k if self.ledger.use_copy else None,price=data['commands'] if d!=s and self.ledger.use_price else None)
        self.observation_audit();self.cost+=data['commands']
        self.events.append(dict(op=op,before=before,after=self.codes(),delivered=k,bits=obs,present=v,commands=data['commands'],cumulative=self.cost,ledger=self.ledger.snapshot()))
        return k

    def drop(self,d):
        C=self.C;before=self.codes();op=('drop',d);word=C.programs[op]
        J,w,_=self.runword(self.J,word);v=self.checked(op,J,w)
        ck(v==bool(before[d]),'drop reports previous presence')
        self.ledger.drop(d,v);self.observation_audit();self.cost+=len(word)
        self.events.append(dict(op=op,before=before,after=self.codes(),present=v,commands=len(word),cumulative=self.cost,ledger=self.ledger.snapshot()))

    def round(self,t,d,preferred):
        C=self.C;start=self.cost;prior=self.codes();snap=self.ledger.snapshot()
        while True:
            action=self.ledger.action(t,preferred)
            if action[0]=='create':break
            self.probe(*action[1:])
        key=action[1]; ck(key not in prior and C.key(t,0)<=key<C.key(t,0)+C.colors,'independent positive full identity freshness')
        word=C.free_reads[t];J,w,_=self.runword(self.J,word);L=int(C.observe_result(J))
        ck(L==1 and w.count==1 and J==self.encoded(self.table,True,self.cache),'mandatory actual source conflict reader')
        col=key-C.key(t,0);cw=C.create_words[t,col,L];K,w,_=self.runword(J,cw)
        self.checked(('reserve',t),K,w,dict(color=col,answer=bool(C.observe_result(K))))
        op=('bind',d,t);K,w,out=self.addressed(self.J,op);self.checked(op,K,w)
        ck(out['code']==key and len(out['observations'])==1+C.color_bits,'actual business bind reconstructs complete target identity')
        self.ledger.bind(d,out['code'])
        op=('release',C.targets[t][0]);rw=C.programs[op];K,w,_=self.runword(self.J,rw);self.checked(op,K,w)
        self.observation_audit()
        labels=[len(word),len(cw),len(out['word']),len(rw)]
        self.cost+=sum(labels);self.rounds+=1
        self.events.append(dict(op=['round',t,d],requested_key=preferred,key=key,before=prior,after=self.codes(),before_ledger=snap,
                                business_words=labels,commands_including_extra_reads=self.cost-start,cumulative=self.cost))
        return key

    def negative_fork(self,t,k,i):
        """Isolated negative control: bypass only selection, then ask original valid on a surviving reference."""
        C=self.C; before=self.codes()
        ck(self.ledger.blocks(k) and before[i]==k,'forbidden choice rejected by live lineage')
        J,w,prior=C.dispatch(self.J,i,delete=False)
        ck(not prior['valid'] and prior['code']==k and w.count==1,'fork start: stale request is invalid')
        # The surrounding positive-run matching is immutable; no forged copy or source answer.
        J,w,_=C.runword(J,C.free_reads[t]);last=int(C.observe_result(J));ck(last==1,'actual free source in fork')
        J,w,_=C.runword(J,C.create_words[t,k-C.key(t,0),last]);ck(w.count==1,'negative create executes physically')
        J,w,after=C.dispatch(J,i,delete=False);ck(w.count==1 and after['valid'] and after['code']==k,'same retained stale identity revives on bypass')
        return dict(request_slot=i,request_origin=self.ledger.slots[i].who,retained_full_key=before[i],forced_key=k,before_valid=prior['valid'],after_valid=after['valid'],scope='diagnostic branch only; no negative command is charged to either correct schedule')

    def receipt(self):
        return dict(initial=self.initial,total=self.cost,extra_vacancy_reads=self.probes,mandatory_copy_key_bits=self.copy_bits,
                    business_rounds=self.rounds,nonself_copies=self.copies,final_codes=self.codes(),events=self.events)

def lifetime_pair():
    C=core.prior.Compiler(slots=2);out={}
    for use in (True,False):
        x=Physical(C,(1,2),use_copy=use)
        x.probe(0,1);x.probe(1,0)
        ck(x.round(0,1,3)==3,'one initial observation per slot certifies A3')
        ck(x.copy(1,0)==1 and x.codes()==(1,1),'copy preserves old source and erases newly bound A3')
        ck(not x.ledger.blocks(3),'discarded new key A3 is already free under both observers')
        if not use:
            ck(x.ledger.blocks(4)==(0,1),'opaque source copy does not certify B4 from prior old bit')
            x.probe(1,0)
        ck(not x.ledger.blocks(4),'obtained evidence excludes B4 for both descendants')
        ck(x.round(1,0,4)==4 and x.codes()==(4,1),'original source slot overwritten yet copied old1 remains')
        ck(x.ledger.slots[1].who=='old:0','copied request is old, distinct from new controlled B4')
        fork=x.negative_fork(0,1,1)
        x.drop(1);ck(not x.ledger.blocks(1),'true last copy retired permits full key1 reuse')
        ck(x.round(0,0,1)==1,'original A1 re-created only after last old copy retired')
        out['use_full_copy' if use else 'opaque_full_copy']=dict(**x.receipt(),negative_fork=fork)
    ck(out['opaque_full_copy']['total']-out['use_full_copy']['total']==8,'equal selected complete keys and same business; one paid real bit saved')
    return out

def self_copy_empty():
    C=core.prior.Compiler(slots=1);r={}
    for use in (True,False):
        p=Physical(C,(0,),use_presence=use);p.copy(0,0)
        if not use:p.probe(0,0)
        ck(p.round(0,0,1)==1,'self-copy false or paid bit excludes preferred positive key')
        r['use_presence' if use else 'discard_presence']=p.receipt()
    ck(r['discard_presence']['total']-r['use_presence']['total']==8,'false self-copy immediately proves slot empty')
    for old in (1,2):
        p=Physical(C,(old,));p.copy(0,0)
        ck(p.ledger.slots[0].mask==0 and p.ledger.slots[0].nonempty is True and p.ledger.blocks(1) and p.ledger.blocks(2),'self-copy TRUE cannot identify a nonempty code')
    return r

def one_palette(slots,code,t,bit,keys,n):
    C=core.prior.Compiler(slots=slots);outs=[]
    for k in keys:
        p=Physical(C,(code,)*slots)
        for i in range(slots):p.probe(i,bit)
        ck(p.round(t,0,k)==k,'actual original observations certify preferred palette key')
        cumulative=[p.cost];copy_costs=[]
        for j in range(n):
            start=p.cost; p.copy(1,0);cumulative.append(p.cost);copy_costs.append(p.cost-start)
        outs.append(dict(k=k,cumulative=cumulative,copy_costs=copy_costs,receipt=p.receipt()))
    return outs

def price_reversals():
    r3=one_palette(3,1,1,0,(6,8),1)
    ck(r3[0]['cumulative'][0]+2==r3[1]['cumulative'][0] and r3[1]['cumulative'][1]+3==r3[0]['cumulative'][1],'r3 three command preference reversal after just one mandatory copy')
    r2=one_palette(2,1,1,0,(4,6),3)
    ck([a-b for a,b in zip(r2[0]['cumulative'],r2[1]['cumulative'])]==[2,1,0,-1],'r2 third mandatory copy changes preferred key')
    c=one_palette(2,8,2,0,(7,9),1)
    ck(c[0]['cumulative']==[84,129] and c[1]['cumulative']==[86,126],'r2 target C strict optimum reverses after first copy')
    zp=one_palette(2,0,1,2,(4,6),3)
    ck([row['cumulative'] for row in zp]==[row['cumulative'] for row in r2],'two matching cost families via different physical observations')
    return {'three_slots_B_nonempty':r3,'two_slots_B_nonempty':r2,'two_slots_C_nonempty':c,'two_slots_B_empty':zp}

def disclosure_prices():
    C=core.prior.Compiler(slots=2);rows={}
    for use,price,name in [(True,False,'full'),(False,True,'length_and_presence'),(False,False,'presence_only')]:
        p=Physical(C,(1,1),use_copy=use,use_price=price)
        p.copy(1,0);allowed=tuple(k for k in range(1,C.d*C.colors+1) if p.ledger.blocks(k))
        if name=='length_and_presence':ck(allowed==(1,2,4),'exact indistinguishable positive codes from command length 43')
        if name=='presence_only':p.probe(0,0)
        key=p.round(0,0,2 if not price else 3)
        rows[name]=dict(**p.receipt(),possible_positive_full_keys_after_copy=allowed,selected=key)
    ck([v['total'] for v in rows.values()]==[107,109,115],'three distinct pointwise optimal real costs by visibility of copy return')
    return rows

def word_audit():
    rec=[]
    for r in (1,2,3,6):
        C=core.prior.Compiler(slots=r);copies=selfc=dp=0;prices={}
        for code in range(C.d*C.colors+1):
            for s in range(r):
                init=[(2*j+1)%(C.d*C.colors+1) for j in range(r)];init[s]=code
                for d in range(r):
                    p=Physical(C,init)
                    p.copy(d,s)
                    if d==s:selfc+=1
                    else:
                        copies+=1;prices[str(code)]=p.cost
                p=Physical(C,init);p.drop(s);dp+=1
        rec.append(dict(slots=r,width=C.bits,legal_codes_including_zero=C.d*C.colors+1,copy_nonself=copies,copy_self=selfc,
                        drop=dp,members=C.members,candidates=len(C.H),paid_copy_by_source_code=prices))
    return rec

def full_policy_run(C,planner,initial):
    """Call the policy only with observations supplied by original business/bit words."""
    p=Physical(C,initial);st=planner.start;events=planner.events;replies=[]
    while st[0]<len(events):
        t=st[0];e=events[t];act=planner.action(st)
        if act[0]=='read':
            _,i,b=act;ans=p.probe(i,b);replies.append(('read',i,b,ans))
        elif act[0]=='round':
            _,target,d=e;k=act[1]
            ck(not p.ledger.blocks(k),'independent typed evidence certifies all planner choices before creation')
            ans=p.round(target,d,k);ck(ans==k,'original controller executed exact selected key');replies.append(('round',target,d,ans))
        else:
            ck(act==('operation',),'planner actually requested next mandatory word')
            if e[0]=='copy':
                ans=p.copy(e[1],e[2])
                if e[1]==e[2]:ans=p.events[-1]['present']
            else:
                p.drop(e[1]);ans=p.events[-1]['present']
            replies.append(tuple(e)+(ans,))
        st=planner.advance(st,act,ans)
    # Offline comparison only after the physical policy has finished.
    predicted,tr,held=planner.replay(tuple(initial))
    ck(predicted==p.cost and held==p.codes(),'entire actual cost and endpoint agree with independent static preparation replay')
    return p.cost,dict(initial=initial,final=p.codes(),vacancy_reads=p.probes,action_replies=replies,total=p.cost)

def policy_sweeps():
    from oracle import DomainBellman
    from collections import Counter
    C=core.prior.Compiler(slots=2);rows=[]
    schedules=[
      (('round',0,0),('copy',0,1),('drop',1),('round',1,1)),
      (('copy',0,0),('round',0,1),('copy',1,0),('drop',0),('round',2,1))]
    for events in schedules:
        planner=DomainBellman(2,events);val=planner.value();hist=Counter();maxrow=None;floor=None
        for inp in product(range(C.d*C.colors+1),repeat=2):
            ans,r=full_policy_run(C,planner,inp);hist[ans]+=1
            if floor is None or ans<floor['total']:floor=r
            if maxrow is None or ans>maxrow['total']:maxrow=r
        ck(max(hist)==val and sum(hist.values())==100,'all 100 full tables run; physical worst equals adversarial full-information cost')
        rows.append(dict(events=events,all_physical_preparations=sum(hist.values()),histogram=hist,planner_minimax=val,
                         first_worst=maxrow,first_minimum=floor))
    return rows

def shield_and_omissions():
    from dataclasses import replace
    import check_batch_integration as integration
    gate,m,p=integration.gate,core.directed.m,core.directed.p
    class Ring(integration.BatchRing):
        def begin(self,jobs,k,route):
            if k<len(jobs) and jobs[k][0]=='copy_sequence':return gate.PC('copy_sequence',k,route=route)
            return super().begin(jobs,k,route)
    initial=(1,2);runs=[]
    jobs=((('copy_sequence',),),(('copy',1,0),))
    for phase in (0,1):
        G=Ring(slots=2);C=G.C;au=Physical(C,initial,capture=True)
        node=G.initial_node(au.table,phase=phase);entry=0
        while node.pcs[0].phase!='copy_sequence':
            node,_,_,_=G.next(node,0,jobs);entry+=1
        held=node;au.J=held.J;au.extras=tuple(h for h in held.J if h not in C.H)
        au.probe(0,1);au.probe(1,0);au.round(0,1,3);au.copy(1,0);au.round(1,0,4);au.drop(1);au.round(0,0,1)
        ck(au.cost==277 and len(au.states)==len(au.raw_words)==au.cost,'all held command boundaries collected')
        refused=0;states=[held.J]+au.states
        for st in states:
            ck(G.lock(0) in st,'holder retains lock at every command boundary')
            blocked,n,grants=gate.complete(G,replace(held,J=st),1,jobs)
            ck(grants==() and blocked.pcs[1].phase=='busy' and tuple(h for h in blocked.J if h in C.H)==tuple(h for h in st if h in C.H),
               'other full copy cannot change any original relation before handoff')
            refused+=n
        pcs=list(held.pcs);pcs[0]=G.begin(jobs[0],held.pcs[0].job+1,held.pcs[0].route)
        node=replace(held,J=au.J,pcs=tuple(pcs));answer=bool(C.observe_result(au.J))
        node,ext,more=gate.complete(G,node,0,jobs)
        ck(not more and gate.old.bit(node.J,G.lanes[0].reply)==answer,'holder private reply')
        node,n,grants=gate.complete(G,node,1,jobs);ck(grants==(1,),'competitor really acquired after handoff')
        after,nextanswer,cache=core.old.expected_selected(C,au.table,au.cache,jobs[1][0],{})
        want=C.encode(after,nextanswer,cache)
        for actor,lane in enumerate(G.lanes):
            want=m.canon(want+p.reg(lane.admitted,1)+p.reg(lane.reply,int((answer,nextanswer)[actor])))
            if actor!=node.turn:want=m.canon(want+(G.gate_pair[actor][phase^1],))
        ck(node.J==want,'physical ports and all BRC relations at handoff')
        omissions=None
        if phase==0:
            # Prove every doubled pair returns the reference state when none, first,
            # or second emission is absent -- a compositional all-pattern test.
            toggles=0;transitions=0
            for j,raw in enumerate(au.raw_words):
                prior,want=states[j:j+2]
                for count in (1,2):
                    v=prior
                    for rep in range(count):
                        v,_=C._raw(v,raw)
                    ck(v==want,'one or both emissions yield the same logical primitive state')
                    transitions+=1
                toggles+=int(prior!=want)
            omissions=dict(original_commands=au.cost,doubled_emissions=2*au.cost,checked_local_transitions=transitions,
                state_changing_commands=toggles,admissible_pair_masks=3,all_logical_endpoints_unchanged=True,
                scope='one or both emissions of each doubled command present; composition of local equalities on this exact held body; excludes both missing and does not cover wrapper omissions')
        runs.append(dict(phase=phase,body=au.cost,gate_entry=entry,gate_exit=ext,protected_total=au.cost+entry+ext,
              held_boundaries=len(states),other_copy_refused_attempts=len(states),other_copy_refused_commands=refused,
              admitted_after_handoff_commands=n,members=G.members,candidates=len(G.H),additional_inventory=0,omission_check=omissions))
    return dict(initial=initial,contender=jobs[1][0],runs=runs)

def main():
    global CHECKS
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,default=HERE/'kernel_results.json');args=parser.parse_args()
    out=dict(status='PASS',scope='Original BRC body, free initial target sources. All masks use true observations; complete tables and isolated invalid paths are separate test oracles.',
          lifetime_pair=lifetime_pair(),self_copy=self_copy_empty(),price_reversals=price_reversals(),observation_hierarchy=disclosure_prices(),word_audit=word_audit(),physical_minimax=policy_sweeps(),protected=shield_and_omissions())
    out['assertions']=CHECKS
    args.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(status='PASS',checks=CHECKS,lifetime_totals=[v['total'] for v in out['lifetime_pair'].values()],self_copy_totals=[v['total'] for v in out['self_copy'].values()],reversals={key:[v['cumulative'] for v in val] for key,val in out['price_reversals'].items()})))
if __name__=='__main__':main()
