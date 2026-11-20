"""One observed absence certificate, several target creations.

Production accesses request information exclusively through inherited BRC reader
words and complete Boolean output. The temporary search tree, quota and residue
set are explicit finite controller state, not new atomic source operations.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from functools import lru_cache
from itertools import combinations_with_replacement
from pathlib import Path
import argparse, json, sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_vacancy as parent
base,p,m,e,r=parent.base,parent.p,parent.m,parent.e,parent.r
ONE,ZERO=parent.ONE,parent.ZERO
CHECKS=0

def ck(value,message):
    global CHECKS
    CHECKS+=1
    if not value:raise AssertionError(message)

@dataclass(frozen=True)
class Task:
    level:int
    prefix:int
    active:tuple[int,...]
    quota:int

@dataclass(frozen=True)
class Search:
    pending:tuple[Task,...]
    holes:tuple[int,...]=()
    task:Task|None=None
    at:int=0
    zeros:tuple[int,...]=()
    ones:tuple[int,...]=()
    reads:int=0


def advance(s:Search,b:int)->Search:
    """Resolve empty subtrees using static capacity, without consulting model state."""
    if s.task is not None:return s
    pending=list(s.pending);holes=list(s.holes)
    while pending:
        t=pending.pop(0)
        capacity=1<<(b-t.level)
        if not (0<t.quota<=capacity-len(t.active)):
            raise ValueError('Insufficient certified deficit')
        if not t.active:
            holes.extend(t.prefix+(j<<t.level) for j in range(t.quota))
        else:
            if t.level>=b:raise ValueError('Occupied singleton cannot be deficient')
            return Search(tuple(pending),tuple(holes),t,0,(),(),s.reads)
    return Search((),tuple(holes),None,0,(),(),s.reads)


def start_search(slots:int)->Search:
    b=slots.bit_length();B=1<<b
    return advance(Search((Task(0,0,tuple(range(slots)),B-slots),)),b)


def accept_bit(s:Search,value:int,b:int)->Search:
    """Consume one Boolean actually produced by a BRC read block."""
    if s.task is None or value not in (0,1):raise ValueError('Expected active read and Boolean')
    t=s.task;i=t.active[s.at]
    z=s.zeros+((i,) if value==0 else ())
    o=s.ones+((i,) if value==1 else ())
    if s.at+1<len(t.active):return replace(s,at=s.at+1,zeros=z,ones=o,reads=s.reads+1)
    groups=(z,o);capacity=1<<(b-t.level-1)
    eligible=sorted((v for v in (0,1) if len(groups[v])<capacity),key=lambda v:(len(groups[v]),v))
    quota=t.quota;tasks=[]
    for v in eligible:
        take=min(quota,capacity-len(groups[v]))
        if take:
            tasks.append(Task(t.level+1,t.prefix|(v<<t.level),groups[v],take));quota-=take
        if quota==0:break
    if quota:raise ValueError('Lost the vacancy deficit')
    return advance(Search(tuple(tasks)+s.pending,s.holes,reads=s.reads+1),b)


def select_color(C,t,holes):
    B=1<<C.color_bits
    # Only compile-time keys and actual observed certificate; no request-table access.
    for color in range(C.colors):
        if C.key(t,color)%B in holes:return color
    raise ValueError('Certificate does not cover this target')


def worst_read_bound(slots):
    b=slots.bit_length();k=(1<<b)-slots
    return sum(min(slots,k*((1<<j)-1)) for j in range(1,b+1))


class Compiler(parent.Compiler):
    def certify(self,J,trace=False,repeats=1,omitted=()):
        state=start_search(self.slots);words=[];logs=[];obs=[];mass=e.prep(J);omitted=set(omitted)
        while state.task is not None:
            task=state.task;slot=task.active[state.at];bit=task.level
            raw=self.reads[slot,bit];word=tuple(x for x in raw for _ in range(repeats));offset=len(words)
            J,weight,ll=self.runword(J,word,trace,{x-offset for x in omitted if offset<=x<offset+len(word)})
            val=int(self.observe_result(J));state=accept_bit(state,val,self.color_bits)
            if trace:logs.extend(dict(x,position=x['position']+offset) for x in ll)
            words.extend(word);obs.append((slot,bit,val));mass=r.serial(mass,weight)
        return J,mass,dict(holes=state.holes,read_bits=state.reads,word=tuple(words),trace=logs,
                           observations=tuple(obs),last=obs[-1][2],commands=len(words))

    def batch(self,J,targets,trace=False,repeats=1,omitted=()):
        if not targets or any(not 0<=t<self.d for t in targets):raise ValueError('Nonempty valid target sequence required')
        words=[];logs=[];mass=e.prep(J);omitted=set(omitted);cert=None;results=[];entries=[]
        def do(block):
            nonlocal J,mass
            offset=len(words);word=tuple(x for x in block for _ in range(repeats))
            J,w,ll=self.runword(J,word,trace,{x-offset for x in omitted if offset<=x<offset+len(word)})
            if trace:logs.extend(dict(x,position=x['position']+offset) for x in ll)
            words.extend(word);mass=r.serial(mass,w)
        for t in targets:
            begin=len(words);do(self.free_reads[t]);available=bool(self.observe_result(J))
            if not available:
                entries.append(dict(target=t,answer=False,color=None,commands=len(words)-begin));results.append(False);continue
            last=1
            if cert is None:
                offset=len(words)
                J,w,cert=self.certify(J,trace,repeats,{x-offset for x in omitted if x>=offset})
                mass=r.serial(mass,w);words.extend(cert['word'])
                if trace:logs.extend(dict(x,position=x['position']+offset) for x in cert['trace'])
                last=cert['last']
            color=select_color(self,t,cert['holes']);do(self.create_words[t,color,last]);results.append(True)
            entries.append(dict(target=t,answer=True,color=color,key=self.key(t,color),commands=len(words)-begin))
        return J,mass,dict(word=tuple(words),trace=logs,commands=len(words),answers=tuple(results),entries=entries,
                           certificate=None if cert is None else {k:cert[k] for k in ('holes','read_bits','observations','last')})


def controller_oracle(vals,b):
    # Test-only full values; production Compiler.certify uses actual BRC reads instead.
    s=start_search(len(vals))
    while s.task is not None:
        s=accept_bit(s,(vals[s.task.active[s.at]]>>s.task.level)&1,b)
    return s.holes,s.reads


def expected_batch(C,table,cache,targets):
    refs=table[1];keys=tuple(0 if x is None else C.key(*x) for x in refs)
    holes,_=controller_oracle(keys,C.color_bits)
    current=list(table[0]);cache=list(cache);answers=[]
    for t in targets:
        allowed=not any(current[v] is not None for v in C.conflicts[t])
        answers.append(allowed)
        if allowed:
            c=select_color(C,t,holes)
            ck((t,c) not in refs,'new identity is distinct from all retained references')
            current[t]=c;cache[t]=C.key(t,c)
    return (tuple(current),refs),tuple(cache),tuple(answers)


def theory(max_r=7):
    cases=0;rows=[]
    for slots in range(1,max_r+1):
        b=slots.bit_length();B=1<<b;k=B-slots;maximum=0;minread=10**9
        for vals in combinations_with_replacement(range(B),slots):
            holes,reads=controller_oracle(vals,b)
            ck(len(holes)==k and len(set(holes))==k,'exact number of distinct absence witnesses')
            ck(not set(holes)&set(vals),'all reported residues absent')
            for offset in range(B):
                C={(offset+j)%B for j in range(slots+1)}
                ck(bool(C&set(holes)),'certificate serves every target interval offset')
            ck(reads<=worst_read_bound(slots),'per-level exact worst bound')
            minread=min(minread,reads);maximum=max(maximum,reads);cases+=1
        witness=tuple(range(k,B));holes,reads=controller_oracle(witness,b)
        ck(reads==maximum==worst_read_bound(slots),'distinct-reference bound-attaining witness')
        rows.append(dict(slots=slots,width=b,residues=B,certificate_size=k,minimum=minread,maximum=maximum,
                         witness=witness,witness_holes=holes))
    return dict(mode='theory',histogram_preparations=cases,rows=rows,assertions=CHECKS)


def audit(slots=1,start=0,stop=None):
    C=Compiler(slots=slots);dom=base.domain(C);stop=len(dom) if stop is None else min(stop,len(dom));operations=0;mass=ZERO
    for n in range(start,stop):
        table=dom[n];cache=list(C.initial_cache(table))
        for t,c in enumerate(table[0]):
            if c is None:cache[t]=(7*n+3*t+1)%(1<<C.bits)
        J=C.encode(table,(None,False,True)[n%3],cache)
        for targets in ((0,2),(2,0),(0,1,2),(1,0,2),(0,0)):
            K,w,data=C.batch(J,targets)
            want,after_cache,answers=expected_batch(C,table,cache,targets)
            ck(data['answers']==answers,'every internal creation response correct')
            ck(K==C.encode(want,answers[-1],after_cache),'full matching source refs caches answer and cleanup')
            if data['certificate'] is not None:
                cert=data['certificate'];keys={0 if v is None else C.key(*v)%(1<<C.color_bits) for v in table[1]}
                ck(not set(cert['holes'])&keys,'actual BRC absence readings')
                ck(cert['read_bits']<=worst_read_bound(slots),'actual reads meet bound')
            oldtab=table
            for t in targets:oldtab,oldans=base.expected(C,oldtab,('reserve',t))
            ck(base.canon(C,want)==base.canon(C,oldtab),'same future-relevant identity partition')
            operations+=1;mass=r.merge(mass,w)
    ck(mass.count==operations,'CWM retains all state-batch preparations')
    return dict(mode='audit',slots=slots,domain=len(dom),slice=[start,stop],batches=operations,
                assertions=CHECKS,CWM=e.cw(mass),kernel_cache_misses=C.calls,primitive_uses=C.uses,
                members=C.members,candidates=len(C.H))


def costs(slots=6,d=3):
    H=base.H_DEFAULT if d==3 else tuple((3*i+1,3*i+2,3*i+3) for i in range(d))
    C=Compiler(H=H,slots=slots);old=parent.Compiler(H=H,slots=slots)
    ck(C.H==old.H and C.members==old.members,'no new physical members or candidate relations')
    b=C.color_bits;B=1<<b;k=B-slots
    cases=[('empty',(None,)*slots),('saturated_A',tuple((0,c) for c in range(slots)))]
    # Keys k..B-1 all exist among the first two target ranges for d>=2.
    cases.append(('bound_witness',tuple(divmod(key-1,C.colors) for key in range(k,B))))
    rows=[]
    for name,refs in cases:
        table=((None,)*d,refs);cache=tuple((1<<C.bits)-1 for _ in range(d));targets=(0,2) if d==3 else tuple(range(d))
        J=C.encode(table,False,cache);K,w,data=C.batch(J,targets,True)
        want,wcache,answers=expected_batch(C,table,cache,targets)
        ck(K==C.encode(want,answers[-1],wcache),'cost entire output')
        O=old.encode(table,False,cache);oldcost=0;oldread=0
        for t in targets:
            O,_,record=old.allocate(O,t);oldcost+=record['commands'];oldread+=record['read_bits']
        ck(base.canon(C,want)==base.canon(old,old.decode(O)[0]),'cost semantic equivalence')
        source=base.ref.old.seed(J)
        for item in data['trace']:source,_,_=base.ref.old.raw_step(source,item['command'],C.H)
        ck(source.matching==K,'birth-annotated actual execution')
        rows.append(dict(case=name,targets=targets,commands=data['commands'],parent_commands=oldcost,
                         read_bits=data['certificate']['read_bits'],parent_read_bits=oldread,
                         holes=data['certificate']['holes'],entries=data['entries']))
    return dict(mode='costs',slots=slots,targets=d,rows=rows,members=C.members,candidates=len(C.H),
                assertions=CHECKS,kernel_cache_misses=C.calls,primitive_uses=C.uses)


def failures():
    C=Compiler(slots=6);table=((None,)*3,(None,)*6);J=C.encode(table)
    J,_,cert=C.certify(J);holes=cert['holes'];last=cert['last'];c=select_color(C,0,holes)
    J,_,_=C.runword(J,C.create_words[0,c,last]);J,_,_=C.run(J,('bind',0,0));J,_,_=C.run(J,('release',1))
    # Deliberate misuse: a retained witness after a newly introduced identity reference.
    K,_,_=C.runword(J,C.free_reads[0]);K,_,_=C.runword(K,C.create_words[0,c,1]);V,_,_=C.run(K,('valid',0))
    ck(C.observe_result(V),'stale certificate revives newly bound old reference')
    fixed,_,fresh=C.batch(J,(0,));V,_,_=C.run(fixed,('valid',0))
    ck(not C.observe_result(V),'fresh certificate excludes newly retained identity')
    # Removing the observed key's residue repairs the certificate for this target.
    repaired=tuple(h for h in holes if h!=C.key(0,c)%(1<<C.color_bits))
    c2=select_color(C,0,repaired)
    ck(c2!=c,'local certificate repair chooses a different identity')
    R,_,_=C.runword(J,C.free_reads[0]);R,_,_=C.runword(R,C.create_words[0,c2,1]);V,_,_=C.run(R,('valid',0))
    ck(not C.observe_result(V),'repaired witness does not revive stale request')
    # Actual copy/drop operations do not introduce a previously absent nonempty key.
    table=((None,)*3,tuple((0,c) for c in range(6)));S=C.encode(table);S,_,cc=C.certify(S)
    for op in (('copy',1,0),('drop',0),('copy',2,0),('copy',3,1)):
        S,_,_=C.run(S,op);tab,_=C.decode(S)
        keys={C.key(*v)%(1<<C.color_bits) for v in tab[1] if v is not None}
        ck(not keys&set(cc['holes']),'actual copy/drop preserve certificate against nonempty keys')
    return dict(mode='failures',initial_certificate=holes,stale_selected_key=C.key(0,c),
                stale_reference_revived=True,fresh_key=fresh['entries'][0]['key'],repaired_certificate=repaired,
                repaired_key=C.key(0,c2),copy_drop_preservation=True,assertions=CHECKS)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['theory','audit','costs','failures'])
    ap.add_argument('--slots',type=int,default=1);ap.add_argument('--d',type=int,default=3)
    ap.add_argument('--max-r',type=int,default=7);ap.add_argument('--start',type=int,default=0);ap.add_argument('--stop',type=int)
    ap.add_argument('--out');args=ap.parse_args()
    if args.mode=='theory':result=theory(args.max_r)
    elif args.mode=='audit':result=audit(args.slots,args.start,args.stop)
    elif args.mode=='costs':result=costs(args.slots,args.d)
    else:result=failures()
    text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if args.out:Path(args.out).write_text(text)
    else:print(text)
