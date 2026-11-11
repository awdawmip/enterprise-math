"""Run scheduled address policies through unchanged original BRC words.

Only the verification harness reads complete tables. The controller receives
per-slot observations and actual business writes; the next address is the
public schedule. No request value is supplied by the harness to the planner.
"""
from __future__ import annotations
import argparse
from collections import Counter
from itertools import product
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'optimization'))
import check_cost_aware_kernel as core
from bellman_planner import key_cost, compatible


class ScheduledController(core.CostAwareController):
    """Execute one fixed stream of reserve/bind(destination,target)/release."""
    def __init__(self, compiler, rounds, *, initial='deficit', planner=None):
        super().__init__(compiler, initial=initial, planner=planner)
        self.rounds = tuple(rounds)
        self.index = 0
        self.operations = tuple(op for target, dst in self.rounds for op in (
            ('reserve', target), ('bind', dst, target), ('release', compiler.targets[target][0])))

    def scheduled_step(self, J, op):
        if self.index >= len(self.operations) or op != self.operations[self.index]:
            raise ValueError('Operation differs from the declared target/address schedule')
        answer = super().step(J, op)
        self.index += 1
        return answer


class CertifiedScript:
    """Preferred keys and scheduled probes; every create is checked against observations.

    If a preferred result fails on another input, select an actually certified
    key, or refine one unknown bit. This fallback never needs complete old keys.
    """
    def __init__(self, slots, rounds, keys, probe_plan=None):
        self.rounds = tuple(rounds)
        self.targets = tuple(t for t,d in rounds)
        self.keys = tuple(keys)
        self.slots = slots
        self.width = slots.bit_length()
        self.modulus = 1 << self.width
        self.probe_plan = {} if probe_plan is None else probe_plan

    def action(self, knowledge, position):
        for slot, bit in self.probe_plan.get(position, ()):
            if not knowledge[slot][0] & (1 << bit):
                return ('read', slot, bit)
        target = self.targets[position]
        first = 1 + target * (self.slots+1)
        legal = range(first, first + self.slots+1)
        preferred = self.keys[position]
        if preferred not in legal:
            raise ValueError('Preferred key outside target')
        def safe(key):
            return not any(compatible(p, key % self.modulus) for p in knowledge)
        if safe(preferred):
            return ('create', preferred)
        alternatives = [k for k in legal if safe(k)]
        if alternatives:
            return ('create', min(alternatives, key=lambda k:(key_cost(k,self.width),k)))
        for bit in reversed(range(self.width)):
            for slot,(mask,_) in enumerate(knowledge):
                if not mask & (1<<bit):
                    return ('read',slot,bit)
        raise AssertionError('M=r+1 leaves a free residue')


# Complete-table access below this line serves preparation and verification only.
CHECKS=0

def check(condition, message):
    global CHECKS
    CHECKS+=1
    if not condition:
        raise AssertionError(message)


def full_codes(C, table):
    return tuple(0 if ref is None else C.key(*ref) for ref in table[1])


def business_constant(C,target):
    return (len(C.free_reads[target]) + C.bits+2 + 8*C.color_bits+C.bits+10
            +len(C.programs['release',C.targets[target][0]]))


def check_address_lengths(C):
    suffixes=bind_runs=0
    word_examples=[]
    for t in range(C.d):
        for color in range(C.colors):
            key=C.key(t,color)
            top=(key>>(C.color_bits-1))&1
            expected=8*C.color_bits+C.bits+10+key.bit_count()+4*(1-top)
            for dst in range(C.slots):
                for last in (0,1):
                    suffix=C.address_writes[dst,key,last]
                    check(len(suffix)==C.bits+2+key.bit_count()+4*(1-last),'compiled suffix length for address')
                    suffixes+=1
                if color != (dst+2*t) % C.colors: continue
                current=tuple(color if j==t else None for j in range(C.d))
                refs=tuple(divmod((i+1)%(C.colors*C.d),C.colors) for i in range(C.slots))
                before=(current,refs)
                J,w,entry=C.addressed(C.encode(before,False),('bind',dst,t))
                expected_refs=list(refs);expected_refs[dst]=(t,color)
                check(w.count==1 and len(entry['word'])==expected,'actual addressed cost independent of destination')
                check(J==C.encode((current,tuple(expected_refs)),True),'original physical address update only the specified slot')
                check(entry['code']==key,'actual bind returns the created full key')
                bind_runs+=1
                if t==0 and dst in (0,C.slots-1):
                    word_examples.append({'target':t,'destination':dst,'key':key,'commands':expected})
    return {'slots':C.slots, 'compiled_nonempty_address_suffixes_checked':suffixes,
            'physical_address_bind_executions':bind_runs,'examples':word_examples}


class PhysicalAudit:
    """Whole-state original-word verification at every business boundary."""
    def __init__(self,C,initial_codes,rounds,*,planner=None,initial='deficit'):
        self.C=C
        self.rounds=tuple(rounds)
        self.controller=ScheduledController(C, self.rounds, planner=planner,initial=initial)
        self.initial_codes=tuple(initial_codes)
        self.table=((None,)*C.d,tuple(divmod(v-1,C.colors) if v else None for v in initial_codes))
        self.cache=C.initial_cache(self.table)
        self.J=C.encode(self.table,False,self.cache)
        self.used_pairs=set()
        self.boundaries=0
        self.physical_read_events=[]
        self.seed_commands=0

    def seed_read(self,slot,bit):
        C=self.C;ctl=self.controller;label=ctl.tree.labels[slot]
        mask,value=ctl.extra_bits.get(label,(0,0))
        check(not mask&(1<<bit) and bit>=label.depth,'public seed requests one unread bit')
        self.J,mass,_=C.runword(self.J,C.reads[slot,bit])
        answer=int(C.observe_result(self.J));self.seed_commands+=len(C.reads[slot,bit])
        ctl.extra_bits[label]=(mask|(1<<bit),value|(answer<<bit))
        self.used_pairs.add((label.initial_slot,bit))
        check(answer==(full_codes(C,self.table)[slot]>>bit)&1 and mass.count==1,'seed uses actual eight-command reader')
        check(self.J==C.encode(self.table,bool(answer),self.cache),'seed observes without changing any request or source')
        return answer

    def step(self,op,*,preparation=False):
        C=self.C;ctl=self.controller
        old_table=self.table;before_codes=full_codes(C,old_table)
        if preparation:
            self.J,mass,entry=ctl.step(self.J,op)
        else:
            self.J,mass,entry=ctl.scheduled_step(self.J,op)
        self.table,answer,self.cache=core.old.expected_selected(C,old_table,self.cache,op,entry)
        check(mass.count==1 and self.J==C.encode(self.table,answer,self.cache),
              'whole original matching after business operation (sources, both keys, result, scratch)')
        core.verify_controller(C,ctl,self.table)
        self.boundaries+=1
        for pair in entry['old_query_pairs']:
            check(pair not in self.used_pairs,'one physical read per initial-label bit')
            self.used_pairs.add(pair)
        after_codes=full_codes(C,self.table)
        if op[0]=='reserve':
            t=op[1];key=entry['key'];reads=[];readers=()
            for obs in entry['observations']:
                if obs[0]=='request_key_bit':
                    _,slot,bit,val,reason=obs
                    check(val==((before_codes[slot]>>bit)&1),'actual delivered bit equals this addressed full identity bit')
                    readers+=C.reads[slot,bit];reads.append((slot,bit,val))
                    self.physical_read_events.append((slot,bit,val))
            check(0<key and key not in before_codes and key%C.modulus not in {x%C.modulus for x in before_codes if x},'chosen key is full-key and residue fresh')
            check(before_codes==after_codes,'reserve leaves all request identities unchanged')
            check(entry['physical_last_before_create']==1 and entry['observations'][-1]==('target_available',t,1),
                  'required actual source result follows all vacancy reads')
            check(entry['word']==readers+C.free_reads[t]+C.create_words[t,key-C.key(t,0),1],
                  'original eight-command reader words, conflict check, original creation suffix in order')
            check(len(reads)==entry['vacancy_bit_reads'],'vacancy physical read count')
            entry['checked_reads']=reads
        elif op[0]=='bind':
            _,dst,t=op;key=entry['observed_business_code']
            check(self.table[0]==old_table[0] and key==C.key(t,old_table[0][t]),'bind reads genuine current creation')
            want=list(before_codes);want[dst]=key
            check(after_codes==tuple(want),'only specified destination may change; non-destination full identities preserved')
            last=(key>>(C.color_bits-1))&1
            word=C.presence_reads[t]+tuple(raw for b in range(C.color_bits) for raw in C.cache_reads[t,b])+C.address_writes[dst,key,last]
            check(word==entry['word'],'exact target check, shared low-bit readers and destination-addressed suffix')
            check(len(word)==8*C.color_bits+C.bits+10+key.bit_count()+4*(1-last),'per-bind cost at actual destination')
        elif op[0]=='release':
            check(after_codes==before_codes,'release preserves all full request identities')
            check(entry['word']==C.programs[tuple(op)] and all(c is None for c in self.table[0]),'one original release word and absent source')
        return entry

    def run(self,*,keep=(1,),repeat_check=None):
        c=self.C;ctl=self.controller
        initial_body_cost=ctl.commands
        initial_reads=ctl.vacancy_bit_reads
        initial_knowledge=ctl.knowledge()
        body_initial=full_codes(c,self.table)
        rounds=[];saved=[];keys=[];cost=reads=0
        for j,(target,dst) in enumerate(self.rounds):
            before_codes=full_codes(c,self.table)
            res=self.step(('reserve',target));binding=self.step(('bind',dst,target));release=self.step(('release',c.targets[target][0]))
            key=res['key'];keys.append(key);count=len(res['checked_reads']);reads+=count
            per=res['commands']+binding['commands']+release['commands'];cost+=per
            check(per==business_constant(c,target)+8*count+key_cost(key,c.color_bits),'actual full-round charge equality')
            check(ctl.commands-initial_body_cost==cost and ctl.vacancy_bit_reads-initial_reads==reads,'cumulative physical accounting')
            row={'round':j+1,'target':target,'destination':dst,'key':key,'round_commands':per,'cumulative_commands':cost,
                 'round_reads':count,'cumulative_reads':reads,'read_events':res['checked_reads'],
                 'codes_before':before_codes,'codes_after':full_codes(c,self.table),'word_lengths':(res['commands'],binding['commands'],release['commands'])}
            if repeat_check is not None: repeat_check(j+1,cost,reads,keys)
            if j+1 in keep: saved.append(row)
            rounds.append((per,count))
        check(ctl.index==len(ctl.operations),'entire declared schedule executed')
        fixed=sum(business_constant(c,t) for t,d in self.rounds)
        return {'initial_full_codes':self.initial_codes,'at_schedule_start_codes':body_initial,
                'at_schedule_start_knowledge':initial_knowledge,'body_commands':cost,'fixed_commands':fixed,
                'variable_commands':cost-fixed,'body_vacancy_reads':reads,'selected_keys':keys,
                'final_full_codes':full_codes(c,self.table),'final_knowledge':ctl.knowledge(),
                'checked_api_boundaries':self.boundaries,'selected_round_receipts':saved}


def compare_planner_trace(C, rounds, initial_codes, *, planner, keep=(),seed=(),copy=None):
    from schedule_planner import schedule_replay
    a=PhysicalAudit(C,initial_codes,rounds,planner=planner)
    if copy is not None:
        cp=a.step(('copy',*copy),preparation=True)
        prep_copy=cp['commands']
    else:prep_copy=0
    for slot,bit in seed:a.seed_read(slot,bit)
    got=a.run(keep=keep)
    residues=tuple(x%C.modulus for x in got['at_schedule_start_codes'])
    replay=schedule_replay(planner,residues,initial_knowledge=got['at_schedule_start_knowledge'])
    check(got['variable_commands']==replay['cost'],'original-kernel and per-slot information-state costs agree')
    check(got['selected_keys']==[e['key'] for e in replay['events'] if e['kind']=='create'],'actual chosen original keys agree with replay')
    check(got['body_vacancy_reads']==replay['vacancy_bit_reads'],'actual read count equals replay')
    check(tuple(x%C.modulus for x in got['final_full_codes'])==tuple(replay['final_residues']),'actual final ordered residues equal replay')
    check(tuple(got['final_knowledge'])==tuple(replay['final_knowledge']),'physical final ordered knowledge equals replay')
    read_events=[(e['slot'],e['bit'],e['answer']) for e in replay['events'] if e['kind']=='read']
    check(a.physical_read_events==read_events,'all actual read addresses, bits and answers equal decision replay')
    got.update(preparation_copy_commands=prep_copy,preparation_bit_commands=a.seed_commands,
               total_including_preparation=prep_copy+a.seed_commands+got['body_commands'])
    return got


def exact_cases():
    from schedule_planner import SchedulePlanner
    cases=((2,((0,0),(0,1),(0,0))), (3,((0,0),(1,2),(2,1),(0,0))))
    rows=[]
    for slots,rounds in cases:
        C=core.prior.Compiler(slots=slots);planner=SchedulePlanner(slots,rounds)
        v=planner.value(((0,0),)*slots,0);samples=[];witness=None;hist=Counter()
        for rs in product(range(C.modulus),repeat=slots):
            codes=tuple(x or C.modulus for x in rs)
            got=compare_planner_trace(C,rounds,codes,planner=planner,keep=range(1,len(rounds)+1))
            check(got['variable_commands']<=v,'per-input variable cost within minimax')
            if got['variable_commands']==v and witness is None: witness=got
            hist[got['body_commands']]+=1
            samples.append([list(rs),got['body_commands'],got['body_vacancy_reads'],got['selected_keys']])
        check(witness is not None and max(hist)==v+witness['fixed_commands'],'worst attained by static original input')
        rows.append(dict(slots=slots,rounds=rounds,original_preparation_count=len(samples),
                         worst_variable=v,fixed=witness['fixed_commands'],actual_worst=max(hist),histogram=dict(sorted(hist.items())),
                         worst_witness=witness,sample_format=['initial residues','original commands','reads','chosen full keys'],samples=samples))
    return rows


def aliases():
    from schedule_planner import SchedulePlanner
    C=core.prior.Compiler(slots=3)
    rounds=((0,2),(1,1),(2,0),(0,2))
    result=compare_planner_trace(C,rounds,(1,5,9),planner=SchedulePlanner(3,rounds),
              keep=range(1,5),copy=(2,0))
    check(tuple(result['at_schedule_start_codes'])==(1,5,1),'actual preparatory copy makes equal full identity; same-residue 5 remains separate')
    check(result['selected_round_receipts'][0]['codes_after'][0]==1 and result['selected_round_receipts'][0]['codes_after'][1]==5,
          'overwriting copy destination leaves its source identity and distinct same-residue slot intact')
    return result


def rotational_cases():
    rows=[];word_audits=[]
    for slots,s in ((6,2),(6,3),(14,3)):
        C=core.prior.Compiler(slots=slots);T=2*(s+1)+2;rounds=tuple((0,j%s) for j in range(T))
        if (slots,s) != (6,3): word_audits.append(check_address_lengths(C))
        codes=(2,)*(slots//2)+(3,)*(slots-slots//2)
        h=C.modulus//2
        cycle=sorted(range(h,C.colors+1),key=lambda k:(key_cost(k,C.color_bits),k))[:s+1]
        costs=sorted(key_cost(k,C.color_bits) for k in range(1,C.colors+1))[:s+1]
        check([key_cost(k,C.color_bits) for k in cycle]==costs,'certified high half contains a globally cheapest key cycle')
        def verify(n,cost,reads,keys):
            q,tail=divmod(n,len(cycle))
            check(keys[-1]==cycle[(n-1)%len(cycle)],'measured key cycle')
            check(cost==8*slots+n*business_constant(C,0)+q*sum(costs)+sum(costs[:tail]),'exact rotating word lower bound attained at each cumulative phase')
            check(reads==slots,'exactly one high-bit read per original slot')
        a=PhysicalAudit(C,codes,rounds,initial='high_half')
        got=a.run(keep=(1,s+1,2*(s+1),T),repeat_check=verify)
        rows.append({'slots':slots,'rotation_size':s,'rounds':T,'cycle':cycle,'cycle_weights':costs,'execution':got})
    return rows,word_audits


def parking_case():
    C=core.prior.Compiler(slots=6);codes=(2,)*3+(3,)*3
    rounds=((0,0),(0,1),(0,1),(0,1))
    greedy=PhysicalAudit(C,codes,rounds,initial='high_half').run(keep=range(1,5))
    planned=PhysicalAudit(C,codes,rounds,initial='high_half',planner=CertifiedScript(6,rounds,(5,4,6,4))).run(keep=range(1,5))
    check(greedy['selected_keys']==[4,5,6,5] and planned['selected_keys']==[5,4,6,4],'same target distinct destination future changes best first key')
    check(greedy['body_commands']==350 and planned['body_commands']==348 and greedy['body_vacancy_reads']==planned['body_vacancy_reads']==6,'parking improvement from weights alone')
    return {'rounds':rounds,'immediate':greedy,'planned':planned}


def expansion_case():
    C=core.prior.Compiler(slots=14);T=232;s=7;rounds=tuple((0,j%s) for j in range(T));codes=(2,)*7+(3,)*7
    high=(8,9,10,12,11,13,14,15);improved=high[:-1]+(4,)
    checkpoints=(1,7,8,16,216,223,224,225,231,232)
    def execute(expand):
        cycle=improved if expand else high;weights=tuple(key_cost(k,C.color_bits) for k in cycle)
        public_probes={7:tuple((i,2) for i in range(7,14))} if expand else None
        a=PhysicalAudit(C,codes,rounds,initial='high_half',planner=CertifiedScript(14,rounds,tuple(cycle[j%8] for j in range(T)),public_probes))
        def verify(n,cost,reads,keys):
            q,m=divmod(n,8);extra=7 if expand and n>=8 else 0
            check(keys[-1]==cycle[(n-1)%8] and reads==14+extra,'observed key cycle and classified original labels')
            check(cost==8*(14+extra)+business_constant(C,0)*n+q*sum(weights)+sum(weights[:m]),'actual cumulative eight-key schedule cost')
        result=a.run(keep=checkpoints,repeat_check=verify)
        check(all(row['round_reads']==0 for row in result['selected_round_receipts'] if row['round']>8),'retained evidence reused after round eight')
        result.pop('selected_keys');result['cycle']=cycle;result['cycle_weights']=weights
        return result
    first=execute(False);extra=execute(True)
    a={row['round']:row['cumulative_commands'] for row in first['selected_round_receipts']}
    b={row['round']:row['cumulative_commands'] for row in extra['selected_round_receipts']}
    delta={n:b[n]-a[n] for n in checkpoints};check(delta[8]==54 and delta[224]==0 and delta[232]==-2,'observed crossover')
    return {'slots':14,'rotation_size':7,'rounds':T,'fixed_per_round':business_constant(C,0),'baseline':first,'expanded':extra,'expansion_minus_baseline':delta}


def future_address_pair():
    from schedule_planner import SchedulePlanner
    C=core.prior.Compiler(slots=3);rounds=((0,0),(0,1),(0,0))
    p=SchedulePlanner(3,rounds);seed=tuple(product(range(3),range(2)))
    runs=[compare_planner_trace(C,rounds,codes,planner=p,seed=seed,keep=range(1,4))
          for codes in ((4,1,2),(4,2,1))]
    check(runs[0]['selected_keys']==[3,4,1] and runs[1]['selected_keys']==[3,4,2],'next-address-only counterexample via physical reads')
    check([r['variable_commands'] for r in runs]==[16,12] and all(r['preparation_bit_commands']==48 for r in runs),
          'equal real prepayment; differing future weight')
    return {'rounds':rounds,'first':runs[0],'second':runs[1]}


class FullKeyEvidence:
    """Mixed, typed evidence: old masked reads vs known full business result.

    This object has no connection to the verifier's original request table.
    It has one record per slot; in this fixture no alias-copy operation occurs.
    """
    def __init__(self,slots):
        self.slots=[('old',0,0) for _ in range(slots)]

    def observed_old_bit(self,slot,bit,value):
        kind,mask,known=self.slots[slot]
        assert kind=='old' and not mask&(1<<bit) and value in (0,1)
        self.slots[slot]=('old',mask|1<<bit, known|value<<bit)

    def accept_bind(self,slot,business_code):
        self.slots[slot]=('exact',business_code)

    def reasons(self,key):
        return tuple(('distinct_full_key' if key!=state[1] else None) if state[0]=='exact'
                     else ('observed_bit_mismatch' if key&state[1]!=state[2] else None)
                     for state in self.slots)

    def certified(self,key):
        return all(self.reasons(key))


def typed_case():
    from schedule_planner import SchedulePlanner
    C=core.prior.Compiler(slots=2);rounds=((0,0),(1,0));initial_codes=(1,1)
    before=((None,)*C.d,((0,0),(0,0)));table=before;cache=C.initial_cache(table);J=C.encode(table,False,cache)
    ev=FullKeyEvidence(C.slots);commands=0;seed=[];events=[]
    for slot in range(C.slots):
        word=C.reads[slot,1];J,w,_=C.runword(J,word);answer=int(C.observe_result(J))
        ev.observed_old_bit(slot,1,answer);commands+=len(word);seed.append((slot,1,answer))
        check(w.count==1 and len(word)==8 and J==C.encode(table,bool(answer),cache),'original single old bit and whole physical state')
    for j,((t,d),key) in enumerate(zip(rounds,(2,6))):
        physical_before=full_codes(C,table);evidence_before=list(ev.slots)
        reasons=ev.reasons(key)
        check(ev.certified(key),'all slots excluded by typed observable evidence')
        check(C.key(t,0)<=key<C.key(t,0)+C.colors and key not in physical_before,'test-only: legal full identity is fresh')
        if j==1:
            check(physical_before==(2,1) and key%C.modulus==physical_before[0]%C.modulus and reasons==('distinct_full_key','observed_bit_mismatch'),
                  'full identity safe despite occupied low residue')
            check(not ev.certified(2),'same prior full key remains blocked by bound request')
        old_commands=commands
        words=C.free_reads[t];J,w,_=C.runword(J,words);last=int(C.observe_result(J))
        check(w.count==1 and last==1 and J==C.encode(table,True,cache),'physical source conflict reader')
        color=key-C.key(t,0);create=C.create_words[t,color,last];J,w,_=C.runword(J,create)
        commands+=len(words)+len(create)
        table,answer,cache=core.old.expected_selected(C,table,cache,('reserve',t),{'color':color,'answer':bool(C.observe_result(J))})
        check(w.count==1 and J==C.encode(table,answer,cache) and full_codes(C,table)==physical_before,'whole original create: old non-revival and full matching')
        bind=('bind',d,t);old_refs=full_codes(C,table)
        J,w,b=C.addressed(J,bind);business_code=b['code'];ev.accept_bind(d,business_code);commands+=b['commands']
        table,answer,cache=core.old.expected_selected(C,table,cache,bind,{})
        check(w.count==1 and J==C.encode(table,answer,cache) and key==business_code,'original addressed business reader delivers full key')
        want=list(old_refs);want[d]=key
        check(full_codes(C,table)==tuple(want),'only designated destination overwritten')
        rel=('release',C.targets[t][0]);word=C.programs[rel];J,w,_=C.runword(J,word);commands+=len(word)
        table,answer,cache=core.old.expected_selected(C,table,cache,rel,{})
        check(w.count==1 and J==C.encode(table,answer,cache) and all(c is None for c in table[0]),'whole original release')
        check(commands-old_commands==business_constant(C,t)+key_cost(key,C.color_bits),'typed complete-round charge')
        events.append(dict(round=j+1,target=t,destination=d,key=key,physical_before=physical_before,
                           evidence_before=evidence_before, exclusion_reasons=reasons,
                           observed_business_code=business_code,after_codes=full_codes(C,table),
                           round_commands=commands-old_commands,cumulative_commands=commands))
    ops=tuple(op for t,d in rounds for op in (('reserve',t),('bind',d,t),('release',C.targets[t][0])))
    _,mass,legacy=core.run_case(C,before,ops,initial='high_half')
    check(mass.count==1,'separately rerun unchanged old greedy controller, whose fallback reads after source check')
    old_greedy={'body_commands':legacy['commands'],'body_vacancy_reads':legacy['vacancy_bit_reads'],
                'selected_keys':[e['key'] for e in legacy['entries'] if e['op'][0]=='reserve']}
    old_planned=PhysicalAudit(C,initial_codes,rounds,initial='high_half',planner=SchedulePlanner(2,rounds)).run(keep=(1,2))
    check(commands==149 and old_planned['body_commands']==151 and old_greedy['body_commands']==159,
          'three measured totals on identical preparation')
    return {'scope':'fixed mixed-evidence witness; no claim of an optimal mixed-state policy',
            'rounds':rounds,'initial_full_codes':initial_codes,'physical_seeds':seed,'preparation_commands':16,
            'all_targets_initially_absent':True,'typed_events':events,'typed_commands':commands,
            'fixed_commands':sum(business_constant(C,t) for t,_ in rounds),'typed_key_weights':[key_cost(k,C.color_bits) for k in (2,6)],
            'residue_planned':old_planned,'residue_greedy':old_greedy}


def omissions_case():
    from schedule_planner import SchedulePlanner
    C=core.prior.Compiler(slots=2);rounds=((0,1),(1,0));p=SchedulePlanner(2,rounds)
    table=((None,)*C.d,((0,0),(0,1)))
    operations=tuple(op for t,d in rounds for op in (('reserve',t),('bind',d,t),('release',C.targets[t][0])))
    def run(omit):return core.run_case(C,table,operations,controller_factory=lambda compiler:core.CostAwareController(compiler,planner=p),
                                     repeats=2,omitted=omit)
    J,w,control=run(())
    N=len(control['word']);check(w.count==1,'doubled control path')
    for i in range(N):
        J2,w2,a=run((i,))
        check(w2.count==1 and J2==J and a['semantic_prefixes']==control['semantic_prefixes']
              and a['final_table']==control['final_table'] and a['extra_old_bit_pairs']==control['extra_old_bit_pairs']
              and [e['observations'] for e in a['entries']]==[e['observations'] for e in control['entries']]
              and a['word']==control['word'],'all single omissions preserve complete original word, choices and original API boundaries')
    return {'rounds':rounds,'initial_full_codes':full_codes(C,table),'repeats':2,'expanded_positions':N,
            'runs_with_exactly_one_omission':N,'non_omitted_controls':1,
            'selected_keys':[e['key'] for e in control['entries'] if e['op'][0]=='reserve'],
            'final_full_codes':full_codes(C,control['final_table']),'distinct_old_reads':len(control['extra_old_bit_pairs']),
            'scope':'one fixed sequential schedule, no interleavings; every single omitted emission of a doubled original word'}

def palette_examples():
    import rotation_checks as rot
    rows=[]
    scenarios=((14,(0,0,1,1,0,1,1,0),26,24),
               (6,(0,0,1,1,0,0,0,0,1,0,0,0,0,0),46,44))
    for slots,ds,small,large in scenarios:
        C=core.prior.Compiler(slots=slots);b,_,high=rot.palettes(slots)
        ordered=rot.ordered(high,b);rounds=tuple((0,d) for d in ds);codes=(2,)*(slots//2)+(3,)*(slots//2)
        limited=rot.exact(ds,ordered[:3],b)
        if slots==14:
            expanded=rot.cheapest_and_common(ds,8,(9,10,12),b)[:2]
        else:
            expanded=rot.exact(ds,ordered,b)
        recordings=[]
        for expected,plan in zip((small,large),(limited,expanded)):
            weight,path=plan
            check(expected==weight,'independent interval/shadow planner weight')
            a=PhysicalAudit(C,codes,rounds,initial='high_half',planner=CertifiedScript(slots,rounds,path))
            got=a.run(keep=(1,len(ds)))
            check(got['selected_keys']==list(path) and got['body_vacancy_reads']==slots and got['body_commands']==len(ds)*business_constant(C,0)+8*slots+weight,
                  'old-bit exclusion, exact path and compiled original body fee')
            recordings.append(got)
        rows.append({'slots':slots,'destinations':ds,'three_key_weight':small,'four_key_weight':large,
                     'three_keys':recordings[0],'four_keys':recordings[1]})
    return rows


def lifetime_pair():
    from schedule_planner import LifetimePlanner
    C=core.prior.Compiler(slots=3);rounds=((0,0),(0,1));p=LifetimePlanner(3,rounds)
    seed=tuple(product(range(3),range(2)))
    xs=[compare_planner_trace(C,rounds,codes,planner=p,seed=seed,keep=(1,2)) for codes in ((1,1,2),(2,1,2))]
    reprs=[p.certificate(x['at_schedule_start_knowledge'],0) for x in xs]
    check(reprs[0]==reprs[1] and all(x['variable_commands']==10 and x['preparation_bit_commands']==48 for x in xs),
          'original BRC executes same effective lasting blockers from two different ordered states')
    return {'rounds':rounds,'certificates':reprs,'first':xs[0],'second':xs[1]}


def protected_schedule():
    from dataclasses import replace
    import check_batch_integration as integration
    from schedule_planner import LifetimePlanner
    gate,m,p=integration.gate,core.directed.m,core.directed.p
    class Ring(integration.BatchRing):
        def begin(self,jobs,k,route):
            if k<len(jobs) and jobs[k][0]=='fixed_schedule':return gate.PC('fixed_schedule',k,route=route)
            return super().begin(jobs,k,route)
    rounds=((0,0),(1,2),(2,1),(0,0));rows=[]
    for phase in (0,1):
        G=Ring(slots=3);C=G.C;ctl=ScheduledController(C,rounds,planner=LifetimePlanner(3,rounds))
        jobs=((('fixed_schedule',ctl.operations),),(('bind',2,2),))
        table=((None,)*C.d,((0,3),(0,3),(0,1)));cache=C.initial_cache(table)
        node=G.initial_node(table,phase=phase);entry_count=0
        while node.pcs[0].phase!='fixed_schedule':
            node,_,_,_=G.next(node,0,jobs);entry_count+=1
        held=node;J=held.J;boundaries=[J];reads=0
        extras=tuple(h for h in J if h not in C.H)
        for op in ctl.operations:
            check(op==ctl.operations[ctl.index],'protected declared schedule')
            J,w,e=ctl.step(J,op,trace=True);ctl.index+=1
            check(w.count==1,'protected path retained')
            boundaries.extend(x['after'] for x in e['trace'])
            table,answer,cache=core.old.expected_selected(C,table,cache,op,e)
            check(J==m.canon(C.encode(table,answer,cache)+extras),'whole protected BRC at every operation boundary')
            core.verify_controller(C,ctl,table)
            reads+=e['vacancy_bit_reads']
        refused=0
        for state in boundaries:
            check(G.lock(0) in state,'holder retains gate at every actual primitive boundary')
            blocked,n,admitted=gate.complete(G,replace(held,J=state),1,jobs)
            check(admitted==() and blocked.pcs[1].phase=='busy' and
                  tuple(h for h in blocked.J if h in C.H)==tuple(h for h in state if h in C.H),
                  'a complete other-writer attempt cannot modify any original relation while held')
            refused+=n
        pcs=list(held.pcs);pcs[0]=G.begin(jobs[0],held.pcs[0].job+1,held.pcs[0].route)
        node=replace(held,J=J,pcs=tuple(pcs));node,out,more=gate.complete(G,node,0,jobs)
        check(not more and gate.old.bit(node.J,G.lanes[0].reply)==answer,'publish private holder reply and hand off')
        node,n,admitted=gate.complete(G,node,1,jobs)
        check(admitted==(1,),'queued competitor actually admitted after handoff')
        table,next_answer,cache=core.prior.parent.expected(C,table,cache,jobs[1][0])
        want=C.encode(table,next_answer,cache)
        for actor,lane in enumerate(G.lanes):
            want=m.canon(want+p.reg(lane.admitted,1)+p.reg(lane.reply,int((answer,next_answer)[actor])))
            if actor!=node.turn:want=m.canon(want+(G.gate_pair[actor][phase^1],))
        check(node.J==want and entry_count+out==31,'full gate, physical replies, sources, addresses and scratch cleanup')
        rows.append({'phase':phase,'body_commands':ctl.commands,'wrapper_commands':entry_count+out,
                     'protected_total':entry_count+out+ctl.commands,'reads':reads,'primitive_boundaries':len(boundaries),
                     'refused_contender_commands':refused,'posthandoff_contender_commands':n,'members':G.members,
                     'candidate_relations':len(G.H),'additional_members_or_relations':0})
    return {'scope':'independent full other-writer attempt from each held boundary in each of two phases; not an arbitrary interleaving graph',
            'rounds':rounds,'initial_codes':(4,4,2),'contender':('bind',2,2),'runs':rows}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=HERE/'kernel_results.json')
    args=parser.parse_args()
    exact=exact_cases();alias=aliases();address=future_address_pair();typed=typed_case();stability=omissions_case()
    parking=parking_case();rotations,audits=rotational_cases();expansion=expansion_case();palettes=palette_examples();lifetime=lifetime_pair();gate=protected_schedule()
    result=dict(status='PASS',scope='single cooperative sequential successful round schedule; original command bodies, no lock fees',
                exact_residue_schedules=exact,copied_alias=alias,only_next_destination_counterexample=address,
                typed_full_key=typed,repeated_single_omissions=stability,parking=parking,rotations=rotations,
                addressed_word_audits=audits,late_extra_bit=expansion,irregular_four_keys=palettes,lifetime_pair=lifetime,protected_schedule=gate,local_assertions=CHECKS)
    args.out.write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    print('PASS',args.out,'local assertions',CHECKS)


if __name__=='__main__':
    main()
