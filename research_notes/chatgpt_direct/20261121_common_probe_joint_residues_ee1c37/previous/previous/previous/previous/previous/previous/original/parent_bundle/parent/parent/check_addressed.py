"""Context-decoded binding and key-addressed copy on the pinned BRC substrate.

Production observations inspect only the complete Boolean output register.
Known target t is an API argument, not a test-only reading of the current row.
All physical updates go through the unchanged inherited triadic kernel.
"""
from __future__ import annotations
from functools import lru_cache
from pathlib import Path
import argparse, json, sys
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'parent'))
import check_shared_key as prior
base, p, m, e, r = prior.base, prior.p, prior.m, prior.e, prior.r
ONE, ZERO = prior.ONE, prior.ZERO
CHECKS = 0

def ck(ok, text):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(text)


class Compiler(prior.Compiler):
    def __init__(self, H=base.H_DEFAULT, slots=2, index_start=None):
        super().__init__(H=H, slots=slots, index_start=index_start, policy='feedback')
        self.parent_candidates = self.H
        self.color_bits = (self.colors - 1).bit_length()
        self.modulus = 1 << self.color_bits
        self.decode_low = tuple({self.key(t,c) % self.modulus:c
                                 for c in range(self.colors)} for t in range(self.d))
        self.H = set(self.H)
        self.presence_reads = {t:tuple(self.clearout()+self.emit_read(row.anchor))
                               for t,row in enumerate(self.current)}
        self.cache_reads = {(t,b):tuple(self.clearout()+self.emit_read(self.shared[t][b][0]))
                             for t in range(self.d) for b in range(self.color_bits)}
        # Suffix selection uses only the observed code and last Boolean bit.
        self.address_writes = {}
        for i in range(slots):
            for code in range(self.d*self.colors+1):
                for last in (0,1):
                    w = [p.one(self.refs[i].anchor)] + self.clear_index(i)
                    if code:
                        t,c = divmod(code-1,self.colors)
                        w += [p.add(self.refs[i].cell(self.ix(t,c)))]
                        w += [p.add(self.index[i][b]) for b in range(self.bits) if code >> b & 1]
                    if bool(code) != bool(last):
                        w += self.clearout() + [p.add(h) for h in p.reg(self.out,int(bool(code)))]
                    self.address_writes[i,code,last] = tuple(w)
        self.H = frozenset(self.H)
        self._raw = lru_cache(maxsize=500000)(self._uncached)
        self.calls = self.uses = 0

    def addressed(self, J, op, trace=False, repeats=1, omitted=()):
        if op[0] not in ('bind','copy') or repeats < 1:
            raise ValueError('Expected bind or copy, with a positive repeat count')
        if op[0]=='copy' and op[1]==op[2]:
            word=tuple(raw for raw in self.base_programs[op] for _ in range(repeats))
            K,mass,log=self.runword(J,word,trace,omitted)
            return K,mass,dict(word=word,trace=log,commands=len(word),observations=[],self_copy=True)
        words=[]; logs=[]; observations=[]; mass=e.prep(J)
        omitted=set(omitted)
        def do(block):
            nonlocal J,mass
            start=len(words)
            ww=tuple(raw for raw in block for _ in range(repeats))
            local={v-start for v in omitted if start<=v<start+len(ww)}
            J,wm,ll=self.runword(J,ww,trace,local)
            if trace:
                ll=[dict(x,position=x['position']+start) for x in ll]
            mass=r.serial(mass,wm);words.extend(ww);logs.extend(ll)
        code=0; last=0
        if op[0]=='bind':
            i,t=op[1:]
            do(self.presence_reads[t]);present=self.observe_result(J)
            observations.append(('current_present',t,present))
            if present:
                low=0
                for b in range(self.color_bits):
                    do(self.cache_reads[t,b]);last=int(self.observe_result(J))
                    observations.append(('shared_low_bit',t,b,last));low |= last << b
                try:
                    color=self.decode_low[t][low]
                except KeyError as exc:
                    raise ValueError('Low-bit observation outside the declared current-key image') from exc
                code=self.key(t,color)
            do(self.address_writes[i,code,last])
        else:
            i,src=op[1:]
            for b in range(self.bits):
                do(self.reads[src,b]);last=int(self.observe_result(J))
                observations.append(('reference_key_bit',src,b,last));code |= last << b
            if code>self.d*self.colors:
                raise ValueError('Reference key outside the exact coding domain')
            do(self.address_writes[i,code,last])
        return J,mass,dict(word=tuple(words),trace=logs,commands=len(words),observations=observations,code=code)

    def run(self,J,op,trace=False):
        if op[0] in ('bind','copy'):
            K,wm,data=self.addressed(J,op,trace)
            return K,wm,data['trace']
        return super().run(J,op,trace)

    def metrics(self):
        return dict(assertions=CHECKS,slots=self.slots,targets=self.d,colors=self.colors,
                    key_bits=self.bits,color_bits=self.color_bits,members=self.members,
                    candidates=len(self.H),new_candidates=len(self.H-self.parent_candidates),
                    kernel_cache_misses=self.calls,primitive_uses=self.uses)


def expected_word_length(C,op,table):
    if op[0]=='copy':
        if op[1]==op[2]:return len(C.base_programs[op])
        ref=table[1][op[2]]
        if ref is None:return 9*C.bits+1
        code=C.key(*ref);last=(code>>(C.bits-1))&1
        return 9*C.bits+2+code.bit_count()+4*(1-last)
    t=op[2];c=table[0][t]
    if c is None:return C.bits+9
    code=C.key(t,c);last=(code>>(C.color_bits-1))&1
    return 8*C.color_bits+C.bits+10+code.bit_count()+4*(1-last)


def audit(slots=1,start=0,stop=None,all_ops=False):
    C=Compiler(slots=slots);domain=base.domain(C)
    stop=len(domain) if stop is None else min(len(domain),stop)
    operations=masscount=0; mass=ZERO
    for n in range(start,stop):
        table=domain[n];cache=list(C.initial_cache(table))
        for t,c in enumerate(table[0]):
            if c is None:cache[t]=(7*n+3*t+1)%(1<<C.bits)
        J=C.encode(table,(None,0,1)[n%3],cache)
        ops=base.Compiler.alphabet(C)
        if not all_ops:ops=[op for op in ops if op[0] in ('bind','copy')]
        for op in ops:
            after,value=base.expected(C,table,op)
            wantcache=prior.expected_cache(C,table,cache,op,after,value)
            pre=C.uses;K,wm,_=C.run(J,op)
            ck(K==C.encode(after,value,wantcache),f'whole matching audit {n}, {op}')
            if op[0] in ('bind','copy'):
                ck(C.uses-pre==expected_word_length(C,op,table),'exact operation length')
            operations+=1;mass=r.merge(mass,wm)
    ck(mass.count==operations,'all preparations/operations retained by positive CWM')
    return dict(mode='audit',domain_total=len(domain),slice=[start,stop],all_ops=all_ops,
                operations=operations,CWM=e.cw(mass),**C.metrics())


def costs(slots=6,H=base.H_DEFAULT):
    C=Compiler(H=H,slots=slots);old=prior.Compiler(H=H,slots=slots,policy='feedback')
    rows=[]
    for t in range(C.d):
        lengths=[]
        for c in range(C.colors):
            cur=[None]*C.d;cur[t]=c
            table=tuple(cur),(None,)*slots
            J=C.encode(table,False);O=old.encode(table,False)
            K,_,data=C.addressed(J,('bind',0,t))
            pre=old.uses;L,_,_=old.run(O,('bind',0,t));oldlen=old.uses-pre
            ck(K==L,'unchanged encoding and full endpoint versus shared snapshot parent')
            ck(data['commands']==expected_word_length(C,('bind',0,t),table),'bind length formula')
            ck(C.decode(K)==base.expected(C,table,('bind',0,t)),'bind semantic result')
            lengths.append(dict(color=c,key=C.key(t,c),commands=data['commands']))
        empty=((None,)*C.d,(None,)*slots)
        K,_,dat=C.addressed(C.encode(empty,True,cache=[(1<<C.bits)-1]*C.d),('bind',0,t))
        ck(K==C.encode(empty,False,cache=[(1<<C.bits)-1]*C.d),'absent source ignores arbitrary shared bytes')
        rows.append(dict(target=t,parent=oldlen,new_min=min(x['commands'] for x in lengths),
                         new_max=max(x['commands'] for x in lengths),absent=dat['commands'],paths=lengths))
    copyrows=[]
    if slots>1:
        for t in range(C.d):
            for c in range(C.colors):
                # Includes stale references, with the actual source entirely empty.
                table=((None,)*C.d,((t,c),)+(None,)*(slots-1))
                J=C.encode(table,True);O=old.encode(table,True)
                K,_,data=C.addressed(J,('copy',1,0))
                pre=old.uses;L,_,_=old.run(O,('copy',1,0));oldlen=old.uses-pre
                ck(K==L,'old stale class copied exactly')
                ck(data['commands']==expected_word_length(C,('copy',1,0),table),'copy length formula')
                copyrows.append(dict(target=t,color=c,key=C.key(t,c),commands=data['commands']))
        empty=((None,)*C.d,(None,)*slots)
        K,_,data=C.addressed(C.encode(empty,True),('copy',1,0))
        ck(K==C.encode(empty,False),'empty copy clears destination and returns false')
        copy_summary=dict(parent=oldlen,nonempty_min=min(x['commands'] for x in copyrows),
                          nonempty_max=max(x['commands'] for x in copyrows),empty=data['commands'],paths=copyrows)
    else:copy_summary=None
    return dict(mode='costs',bind=rows,copy=copy_summary,**C.metrics())


def scaling():
    rows=[]
    for d,slots in ((1,1),(3,1),(3,2),(3,6),(3,7),(3,14),(3,30),(7,6),(15,6)):
        H=tuple((3*i+1,3*i+2,3*i+3) for i in range(d))
        row=costs(slots,H)
        # Retain summary; per-code paths for main example are separately saved.
        rows.append(dict(d=d,slots=slots,M=slots+1,q=row['key_bits'],b=row['color_bits'],
                         bind_parent=row['bind'][0]['parent'],bind_max=max(x['new_max'] for x in row['bind']),
                         bind_min=min(x['new_min'] for x in row['bind']),absent=row['bind'][0]['absent'],
                         copy=None if row['copy'] is None else {k:v for k,v in row['copy'].items() if k!='paths'},
                         members=row['members'],candidates=row['candidates'],new_candidates=row['new_candidates']))
    return dict(mode='scaling',rows=rows,assertions=CHECKS)


def lifecycle(rounds=12):
    C=Compiler(slots=6);old=prior.Compiler(slots=6,policy='feedback')
    table=((None,)*C.d,(None,)*6);J=C.encode(table);O=old.encode(table)
    state=base.ref.old.seed(J);protected=None;actions=commands=oldcommands=0;records=[]
    def run(op):
        nonlocal J,O,table,state,protected,actions,commands,oldcommands
        before=C.uses;K,_,logs=C.run(J,op,True);commands+=C.uses-before
        before=old.uses;L,_,_=old.run(O,op);oldcommands+=old.uses-before
        ck(K==L,'full lifecycle state equality')
        want=base.expected(C,table,op)
        ck(C.decode(K)==want,'lifecycle abstract correspondence')
        for step in logs:
            state,_,_=base.ref.old.raw_step(state,step['command'],C.H)
            if protected is not None:ck(state.names().get(C.targets[2])==protected,'C creation retained in every primitive prefix')
        ck(state.matching==K,'creation annotation matches physical kernel')
        if op==('reserve',2) and protected is None:protected=state.names()[C.targets[2]]
        table=want[0];J=K;O=L;actions+=1
        if len(records)<40:records.append(dict(op=op,result=want[1],table=table,commands=len(logs)))
    run(('reserve',2))
    for n in range(rounds):
        i=n%6;j=(i+1)%6;k=(i+2)%6
        for op in (('reserve',0),('bind',i,0),('copy',j,i),('same',i,j),('valid',i),
                   ('release',1),('bind',k,0),('valid',j),('same',i,j),('reserve',0),
                   ('bind',k,0),('execute',j),('execute',k),('copy',i,j),('drop',j),('copy',i,i)):
            run(op)
    return dict(mode='lifecycle',rounds=rounds,api_calls=actions,commands=commands,parent_commands=oldcommands,
                trace=records,CWM='Sequential path; all operations use inherited kernel',**C.metrics())


def failures():
    C=Compiler(slots=6);out={}
    # Same low bits, different known target: context is an indispensable part of decoding.
    b=C.color_bits;u=C.key(0,0)%(1<<b)
    ck(u==C.key(1,1)%(1<<b),'across-target residue collision exists')
    out['context_collision']=dict(target0_key=C.key(0,0),target1_key=C.key(1,1),low_bits=u,bits=b)
    # Too few bits, within ONE target. This is a physically reachable allocator state.
    table=((None,)*3,(None,)*6);J=C.encode(table)
    for i in range(4):
        for op in (('reserve',0),('bind',i,0),('release',1)):
            J,_,_=C.run(J,op);table=base.expected(C,table,op)[0]
    J,_,_=C.run(J,('reserve',0));table=base.expected(C,table,('reserve',0))[0]
    ck(table[0][0]==4,'four retained old labels make color4 current')
    K,_,good=C.addressed(J,('bind',4,0),True)
    after,want=base.expected(C,table,('bind',4,0));ck(K==C.encode(after,want,C.initial_cache(table)),'correct b-bit binding')
    short=C.color_bits-1;low=0;B=J;word=[]
    for j in range(short):
        ww=C.cache_reads[0,j];B,_,_=C.runword(B,ww);word.extend(ww)
        low |= int(C.observe_result(B)) << j
    candidates=[c for c in range(C.colors) if C.key(0,c)%(1<<short)==low]
    badcode=C.key(0,min(candidates));last=int(C.observe_result(B))
    B,_,_=C.runword(B,C.address_writes[4,badcode,last])
    got=C.decode(B)
    ck(got[0][1][4]==(0,0) and after[1][4]==(0,4),'insufficient key bits bind wrong historical class')
    out['short_decoder']=dict(actual_current=4,read_bits=short,low=low,candidates=candidates,
                               decoded_reference=got[0][1][4],expected_reference=after[1][4])
    # Query answer is not the API answer. Omit the final normalization deliberately.
    tab=((0,None,0),(None,)*6);A=C.encode(tab)
    K,_,data=C.addressed(A,('bind',0,0),True)
    ck(data['word'][-4:]==tuple(C.clearout()+[p.add(h) for h in p.reg(C.out,1)]),'this path needs false-to-true normalization')
    B,_,_=C.runword(A,data['word'][:-4])
    ck(not C.observe_result(B) and C.refs[0].cell(C.ix(0,0)) in B,'without normalization binding is real but answer false')
    out['answer_normalization']=dict(expected=True,observed=False,reference_exists=True)
    # A valid nonempty key can have an all-zero LOW residue.
    P=Compiler(slots=7,H=((1,2,3),));tab=((7,),(None,)*7)
    K,_,dat=P.addressed(P.encode(tab),('bind',0,0))
    ck(P.key(0,7)==8 and dat['code']==8 and P.observe_result(K),'presence disambiguates low-zero nonempty key')
    out['nonempty_zero_residue']=dict(key=8,color=7,bits=P.color_bits,result=True,commands=dat['commands'])
    return dict(mode='failures',cases=out,assertions=CHECKS)


def export():
    C=Compiler(slots=6)
    return dict(members=C.members,candidates=sorted(C.H),new_candidates=sorted(C.H-C.parent_candidates),
                full_key_bits=C.bits,color_bits=C.color_bits,
                known_target_decoders=C.decode_low,presence_reads=C.presence_reads,
                cache_reads={repr(k):v for k,v in C.cache_reads.items()},
                address_writes={repr(k):v for k,v in C.address_writes.items()},
                binding_control='presence -> low shared bits -> target-specific decode -> fixed destination write',
                copy_control='full source index bits -> fixed destination write; self-copy uses parent presence')


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=('audit','costs','scaling','lifecycle','failures','export'))
    ap.add_argument('--slots',type=int,default=1);ap.add_argument('--start',type=int,default=0);ap.add_argument('--stop',type=int)
    ap.add_argument('--all-ops',action='store_true');ap.add_argument('--targets',type=int);ap.add_argument('--out');a=ap.parse_args()
    ans = (audit(a.slots,a.start,a.stop,a.all_ops) if a.mode=='audit' else
           costs(a.slots,tuple((3*i+1,3*i+2,3*i+3) for i in range(a.targets))) if a.mode=='costs' and a.targets else
           globals()[a.mode]())
    text=json.dumps(ans,ensure_ascii=False,indent=2)+'\n'
    if a.out:Path(a.out).write_text(text)
    else:print(text)
