"""Materialized target bits, maintained by original triadic words.

The index stores immutable request target provenance, not cached validity.
Production observes only full Boolean result registers. Decode/spec functions
are test-only. All matching transitions use the unmodified inherited BRC kernel.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from functools import lru_cache
from pathlib import Path
from itertools import product
import argparse, hashlib, json, sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_optimal_dispatch as prior
old=prior.parent
feedback,base=old.feedback,old.base
p,m,e,r=old.p,old.m,old.e,old.r
ONE,ZERO=old.ONE,old.ZERO
CHECKS=0

def ck(ok, message):
    global CHECKS
    CHECKS+=1
    if not ok: raise AssertionError(message)

class Compiler(feedback.Compiler):
    def __init__(self,H=base.H_DEFAULT,slots=2,index_start=None):
        super().__init__(H=H,slots=slots)
        self.parent_members=self.members;self.parent_candidates=len(self.H)
        self.bits=self.d.bit_length()
        first=self._next if index_start is None else index_start
        if first<self._next:raise ValueError('Index must be disjoint from existing source and working layout')
        self.index=tuple(tuple(tuple(range(first+3*(i*self.bits+b),first+3*(i*self.bits+b)+3))
                               for b in range(self.bits)) for i in range(slots))
        self.H=set(self.H)
        for row in self.index:self.H.update(row)
        self.reads={}
        for i,row in enumerate(self.index):
            for b,bit in enumerate(row):self.reads[i,b]=tuple(self.clearout()+self.emit_read(bit[0]))
        self.base_programs=dict(self.programs)
        # Atomicity is at the admitted API boundary, including this maintenance.
        for op,word in list(self.programs.items()):
            kind=op[0];suffix=[]
            if kind=='bind':
                i,t=op[1:];suffix=self.clear_index(i)
                for b in range(self.bits):
                    if (t+1)>>b&1:suffix+=self.emit_write((self.current[t].anchor,),self.index[i][b])
            elif kind=='copy' and op[1]!=op[2]:
                i,j=op[1:];suffix=self.clear_index(i)
                for b in range(self.bits):suffix+=self.emit_write((self.index[j][b][0],),self.index[i][b])
            elif kind=='drop':suffix=self.clear_index(op[1])
            self.programs[op]=word+tuple(suffix)
        self.repairs={}
        for i in range(slots):
            w=self.clear_index(i)
            for t in range(self.d):
                for c in range(self.colors):
                    for b in range(self.bits):
                        if (t+1)>>b&1:w+=self.emit_write((self.rp(i,t,c),),self.index[i][b])
            self.repairs[i]=tuple(w)
        self.H=frozenset(self.H)
        self.members=self.parent_members+3*slots*self.bits
        self._raw=lru_cache(maxsize=500000)(self._uncached)
        self.calls=self.uses=0

    def clear_index(self,i):return [p.one(bit[0]) for bit in self.index[i]]

    def encode(self,table,status=None):
        events=list(super().encode(table,status))
        for i,q in enumerate(table[1]):
            if q is not None:
                for b in range(self.bits):
                    if (q[0]+1)>>b&1:events.append(self.index[i][b])
        return m.canon(events)

    def strip_index(self,J):
        alltags=set(h for row in self.index for h in row)
        return m.canon(h for h in J if h not in alltags)

    def decode(self,J):
        # Independent exact test observation. Production never calls this.
        stripped=self.strip_index(J)
        cur=[];refs=[]
        for row in self.current:
            found=[c for c in range(self.colors) if row.cell(c) in stripped]
            ck(len(found)<=1,'unique current record');cur.append(found[0] if found else None)
        for row in self.refs:
            found=[(t,c) for t in range(self.d) for c in range(self.colors)
                   if row.cell(self.ix(t,c)) in stripped]
            ck(len(found)<=1,'unique request record');refs.append(found[0] if found else None)
        table=tuple(cur),tuple(refs);answer=p.read(J,self.out)
        ck(answer in (0,1),'complete result')
        ck(J==self.encode(table,answer),'whole state: source, directory, requests, output, clear work')
        return table,bool(answer)

    def dispatch(self,J,i,trace=False,delete=True,repeats=1,omitted=()):
        if not 0<=i<self.slots or repeats<1:raise ValueError('Invalid slot or repetition count')
        word=[];log=[];observations=[];mass=e.prep(J);code=0
        omit=set(omitted)
        def do(block):
            nonlocal J,mass
            expanded=tuple(raw for raw in block for _ in range(repeats))
            offset=len(word);local=tuple(k-offset for k in omit if offset<=k<offset+len(expanded))
            J,wm,records=self.runword(J,expanded,trace,local)
            mass=r.serial(mass,wm);word.extend(expanded);log.extend(records)
        # Precompiled bit-read blocks; all information used in control comes
        # from the full result register, never request/table inspection.
        for b in range(self.bits):
            do(self.reads[i,b]);value=self.observe_result(J)
            observations.append(('target_bit',b,value));code|=int(value)<<b
        if code>self.d:raise ValueError('Out-of-domain target index code')
        valid=False
        if code:
            t=code-1;do(self.programs['match',i,t]);valid=self.observe_result(J)
            observations.append(('match',t,valid))
            if delete and valid:do(self.commit(t))
        return J,mass,dict(code=code,valid=valid,commands=len(word),reads=len(observations),
                           observations=observations,word=tuple(word),trace=log)

    def run(self,J,op,trace=False):
        if op[0] in ('execute','valid'):
            K,w,d=self.dispatch(J,op[1],trace,delete=op[0]=='execute')
            return K,w,d['trace']
        return self.runword(J,self.programs[op],trace)

    def metrics(self):return dict(assertions=CHECKS,targets=self.d,slots=self.slots,colors=self.colors,bits=self.bits,
             members=self.members,parent_members=self.parent_members,candidates=len(self.H),
             parent_candidates=self.parent_candidates,kernel_cache_misses=self.calls,primitive_uses=self.uses)


def audit(slots=2,start=0,stop=None):
    C=Compiler(slots=slots);domain=base.domain(C);stop=len(domain) if stop is None else min(len(domain),stop)
    total=0;mass=ZERO;queries=0
    for n in range(start,stop):
        tab=domain[n];J=C.encode(tab,(None,0,1)[n%3])
        for op in base.Compiler.alphabet(C):
            K,wm,_=C.run(J,op);got=C.decode(K);want=base.expected(C,tab,op)
            ck(got==want,f'API correspondence {n} {op}')
            total+=1;mass=r.merge(mass,wm)
        for i in range(slots):
            for b in range(C.bits):
                K,_,_=C.runword(J,C.reads[i,b])
                want=bool(((tab[1][i][0]+1) if tab[1][i] else 0)>>b&1)
                ck(K==C.encode(tab,want),'index probe preserves all persistent relations');queries+=1
    return dict(mode='audit',domain=len(domain),start=start,stop=stop,api_cases=total,
                index_probe_cases=queries,CWM=e.cw(mass),**C.metrics())


def costs():
    C=Compiler(slots=6);F=feedback.Compiler(slots=6);rows=[]
    for label,cur,q in [('A',(0,None,0),(0,0)),('B',(None,0,None),(1,0)),
                        ('C',(0,None,0),(2,0)),('stale_B',(0,None,0),(1,0)),
                        ('stale_A',(1,None,0),(0,0)),('empty',(0,None,0),None)]:
        tab=cur,(q,)+(None,)*5;J=C.encode(tab);K,wm,data=C.dispatch(J,0)
        L,_,fd=F.feedback(F.encode(tab),0)
        ck(C.strip_index(K)==L,'exact old execute endpoint with index projected out')
        ck(C.decode(K)==base.expected(C,tab,('execute',0)),'indexed execute exact endpoint')
        st=base.ref.old.seed(J);names=st.names();retired=[]
        target=C.targets[q[0]] if data['valid'] else None
        for raw in data['word']:
            st,_,delta=base.ref.old.raw_step(st,raw,C.H)
            retired += [h for h,b in delta['retired'] if h in C.targets]
            for h,birth in names.items():
                if h in C.targets and h!=target:ck(st.names().get(h)==birth,'unrelated source birth retained every prefix')
        ck(st.matching==K,'annotated replay same primitive endpoint')
        ck(retired==([] if target is None else [target]),'zero or one source retirement')
        formula=8*C.bits+(4*C.colors+9 if q else 0)+(2 if data['valid'] else 0)
        ck(data['commands']==formula,'executed cost matches formula')
        rows.append(dict(name=label,commands=data['commands'],feedback=data['reads'],old_linear=fd['commands'],
                         source_retired=retired,observations=data['observations']))
    overhead={}
    for op,w in C.programs.items():
        if op[0] in ('bind','copy','drop'):overhead[str(op)]=len(w)-len(C.base_programs[op])
    tab=((0,None,0),((0,0),(2,0),None,(1,0),(0,1),(2,0)))
    raw=F.encode(tab,True);word=tuple(x for i in range(C.slots) for x in C.repairs[i])
    migrated,_,_=C.runword(raw,word)
    ck(migrated==C.encode(tab,True),'migration restores index from original request relations')
    return dict(mode='costs',paths=rows,update_overhead=overhead,migration_commands=len(word),
                worst_old=prior.minimax_formula(C.d,C.colors),worst_indexed=max(x['commands'] for x in rows),**C.metrics())


def scaling():
    rows=[]
    for d in (1,2,3,4,7,8,15,31):
        H=tuple((3*t+1,3*t+2,3*t+3) for t in range(d));C=Compiler(H,6)
        paths=[]
        for code in range(d+2):
            q=(code-1,0) if 1<=code<=d else (None if code==0 else (0,1))
            tab=(0,)*d,(q,)+(None,)*5;J=C.encode(tab);K,_,data=C.dispatch(J,0)
            ck(C.decode(K)==base.expected(C,tab,('execute',0)),'scaled execute')
            paths.append(data['commands'])
        row=dict(targets=d,bits=C.bits,old_minimax=prior.minimax_formula(d,7),
                 indexed_worst=max(paths),indexed_stale=paths[-1],indexed_empty=paths[0],
                 extra_members=C.members-C.parent_members,members=C.members,
                 candidate_count=len(C.H),worst_bind_overhead=max(len(C.programs['bind',0,t])-len(C.base_programs['bind',0,t]) for t in range(d)))
        ck(row['indexed_worst']==8*C.bits+4*C.colors+11,'indexed upper envelope exact')
        rows.append(row)
    return dict(mode='scaling',rows=rows,assertions=CHECKS)


def lifecycle(rounds=50):
    C=Compiler(slots=6);tab=((None,)*3,(None,)*6);J=C.encode(tab);mass=e.prep(J)
    counts={};cost=0;steps=0;records=[]
    def apply(op):
        nonlocal J,tab,mass,cost,steps
        want=base.expected(C,tab,op);before=C.uses
        J,wm,_=C.run(J,op);cost+=C.uses-before;steps+=1;mass=r.serial(mass,wm)
        ck(C.decode(J)==want,'continuous indexed API invariant');tab=want[0]
        counts[op[0]]=counts.get(op[0],0)+1
        if len(records)<35:records.append(dict(op=op,response=want[1],table=tab))
    for t in (0,2):apply(('reserve',t))
    for n in range(rounds):
        i=n%6;j=(i+1)%6;k=(i+2)%6
        for op in [('bind',i,0),('copy',j,i),('execute',i),('valid',j),('same',i,j),
                   ('reserve',0),('execute',j),('bind',i,2),('copy',k,i),
                   ('valid',k),('target_is',k,2),('bind',j,1),('drop',i),('copy',i,j),
                   ('bind',i,0),('copy',i,i)]:apply(op)
    return dict(mode='lifecycle',rounds=rounds,api_calls=steps,commands=cost,operations=counts,
                first_records=records,CWM=e.cw(mass),**C.metrics())


def failures():
    C=Compiler(slots=1);cases=[]
    # Stale route is not stale-instance permission: a positive local match is
    # required. The index intentionally continues pointing to the old target.
    tab=((1,None,0),((0,0),));J=C.encode(tab)
    good,_,data=C.dispatch(J,0)
    ck(not data['valid'] and C.decode(good)==base.expected(C,tab,('execute',0)),'stale ref remains invalid despite route')
    bad,_,_=C.runword(J,C.commit(0))
    ck(C.targets[0] not in bad,'unchecked route deletes new instance')
    cases.append(dict(name='route_is_not_validity',proper_commands=data['commands'],proper_valid=data['valid'],
                      bad_unchecked_source=[h for h in bad if h in C.targets]))
    # A slot rebind performed without changing the side index can cause a miss.
    tab=((0,None,0),((0,0),));J=C.encode(tab)
    corrupt,_,_=C.runword(J,C.base_programs['bind',0,2])
    out,_,info=C.dispatch(corrupt,0)
    ck(not info['valid'] and C.targets[2] in out,'outdated index can miss valid C')
    cases.append(dict(name='base_bind_without_index_maintenance',observations=info['observations'],
                      response=C.observe_result(out),remaining_source=[h for h in out if h in C.targets]))
    repaired,_,_=C.runword(corrupt,C.repairs[0]);fixed,_,_=C.dispatch(repaired,0)
    correct=base.expected(C,tab,('bind',0,2))[0]
    ck(C.decode(fixed)==base.expected(C,correct,('execute',0)),'bounded original-word index rebuild repairs miss')
    # One exact omission in the new bind suffix: omit the reserved tag itself.
    fresh=Compiler(slots=1);tab=((0,None,0),(None,));J=fresh.encode(tab)
    w=fresh.programs['bind',0,0];pos=w.index(p.add(fresh.index[0][0]))
    corrupt,_,_=fresh.runword(J,w,omitted=(pos,));K,_,info=fresh.dispatch(corrupt,0)
    ck(not info['valid'] and fresh.targets[0] in K,'unprotected tag-write omission can cause false negative')
    cases.append(dict(name='omitted_materialization',omitted_position=pos,commands=len(w),response=False))
    return dict(mode='failures',cases=cases,assertions=CHECKS)


def export():
    C=Compiler(slots=6)
    return dict(scope='exact target index; stable full API boundaries',bits=C.bits,index_layout=C.index,
                members=C.members,candidates=sorted(C.H),
                bit_reads={str(k):v for k,v in C.reads.items()},
                maintenance_words={str(k):v for k,v in C.programs.items() if k[0] in ('bind','copy','drop')},
                matches={str(k):v for k,v in C.programs.items() if k[0]=='match'},
                commits={str(t):C.commit(t) for t in range(C.d)},repairs=C.repairs,
                controller='read target bits LSB first; zero=>false; else MATCH(code-1); if true two-step commit')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['audit','costs','scaling','lifecycle','failures','programs'])
    ap.add_argument('--slots',type=int,default=2);ap.add_argument('--start',type=int,default=0)
    ap.add_argument('--stop',type=int);ap.add_argument('--out');a=ap.parse_args()
    ans=audit(a.slots,a.start,a.stop) if a.mode=='audit' else globals()[a.mode]() if a.mode!='programs' else export()
    text=json.dumps(ans,ensure_ascii=False,indent=2)+'\n'
    if a.out:Path(a.out).write_text(text)
    else:print(text)
