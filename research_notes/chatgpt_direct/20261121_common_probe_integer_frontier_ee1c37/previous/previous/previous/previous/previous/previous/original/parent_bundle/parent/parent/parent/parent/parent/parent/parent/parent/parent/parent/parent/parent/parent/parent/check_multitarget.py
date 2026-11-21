"""Multi-target reference API coupled to actual triadic source relations.

Production is a fixed reserve/release word per API. Test-only decoders/specs are
never called by runword. Target-tagged colors preserve logical creation classes
at complete macro boundaries. execute uses a declared clear/rebuild of the raw
source; it preserves logical identity, not physical birth identity or histories.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from itertools import product, combinations
from pathlib import Path
import argparse, json, sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_triadic_refs as old
p,m,e,r=old.p,old.m,old.e,old.r
ONE,ZERO=old.ONE,old.ZERO
ref=old.ref
H_DEFAULT=((1,2,3),(1,4,5),(4,5,6))
CHECKS=0
SPEC_KERNEL=0

def ck(ok,label):
    global CHECKS
    CHECKS+=1
    if not ok: raise AssertionError(label)

@dataclass(frozen=True)
class Row:
    anchor:int
    control:int
    ports:tuple[int,...]
    def cell(self,c):return tuple(sorted((self.anchor,self.control,self.ports[c])))

class Compiler:
    def __init__(self,H=H_DEFAULT,slots=2):
        self.targets=tuple(sorted(tuple(sorted(h)) for h in H))
        if not self.targets or slots<1:raise ValueError('Nonempty targets and at least one reference slot required')
        if len(set(self.targets))!=len(self.targets) or any(len(set(h))!=3 for h in self.targets):raise ValueError('Distinct triple candidates required')
        self.U=tuple(sorted(set().union(*map(set,self.targets))))
        self.d=len(self.targets);self.slots=slots;self.colors=slots+1
        self._next=max(self.U)+1
        def make_row(n):
            a=self._next;self._next+=n+2
            return Row(a,a+1,tuple(range(a+2,a+2+n)))
        self.current=tuple(make_row(self.colors) for _ in self.targets)
        self.refs=tuple(make_row(self.d*self.colors) for _ in range(slots))
        self.back=make_row(self.colors)
        a=self._next;self.block=(a,a+1);self.marker=(a+2,a+3,a+4);self.success=(a+5,a+6,a+7);self.work=a+8;self.out=a+8;self._next=a+15
        self.members=len(self.U)+self._next-(max(self.U)+1)
        self.H=set(self.targets)|p.library(self.out)|{self.marker,self.success}
        for row in self.current+(self.back,):self.H.update(row.cell(c) for c in range(self.colors))
        for row in self.refs:self.H.update(row.cell(j) for j in range(self.d*self.colors))
        self.programs={op:tuple(self._compile(op)) for op in self.alphabet()}
        self.H=frozenset(self.H)
        self.calls=self.uses=0
        self._raw=lru_cache(maxsize=400000)(self._uncached)
    def ix(self,t,c):return t*self.colors+c
    def rp(self,i,t,c):return self.refs[i].ports[self.ix(t,c)]
    def clearout(self):return [p.one(self.out+1),p.one(self.out+5)]
    def emit_write(self,ports,target):
        hh,word=old.write(tuple(ports),target,self.work);self.H|=hh;return list(word)
    def emit_read(self,port,invert=False):
        hh,word,_=old.reader(port,self.out,self.work,invert=invert);self.H|=hh;return list(word)
    def emit_local_equal(self,t,i):
        w=[]
        for c in range(self.colors):w+=self.emit_write((self.current[t].ports[c],self.rp(i,t,c)),self.marker)
        return w+self.emit_read(self.marker[0])+[p.one(self.marker[1])]
    def alphabet(self):
        d,n=self.d,self.slots
        return (tuple(('reserve',t) for t in range(d))+tuple(('release',a) for a in self.U)
                +tuple(('bind',i,t) for i in range(n) for t in range(d))
                +tuple((k,i) for k in ('drop','present','valid','execute') for i in range(n))
                +tuple((k,i,j) for k in ('copy','same') for i in range(n) for j in range(n))
                +tuple(('target_is',i,t) for i in range(n) for t in range(d)))
    def _compile(self,op):
        kind=op[0];w=self.clearout()
        if kind=='reserve':
            t=op[1];cur=self.current[t];h=self.targets[t]
            # Conflict membership is compiled from the declared source incidence.
            for b,k in enumerate(self.targets):
                if set(h)&set(k):w+=self.emit_write((self.current[b].anchor,),self.marker)
            w+=self.emit_read(self.marker[0],invert=True)+[p.one(self.marker[1]),p.one(self.out+1)]
            for c in range(self.colors):
                block=tuple(sorted((cur.ports[c],*self.block)));self.H.add(block)
                w+=self.emit_write((self.out+4,),block)  # false permission blocks allocation
                for i in range(self.slots):w+=self.emit_write((self.rp(i,t,c),),block)
                w += [p.add(cur.cell(c)),p.one(self.block[0])]
            w+=self.emit_write((cur.anchor,),h)
            w += [p.add(p.reg(self.out,0)[0]),p.add(p.reg(self.out,1)[0])]
        elif kind=='release':
            a=op[1];w+=self.emit_read(a)+[p.one(a)]
            # Every possible alias of this raw member is covered; matching ensures
            # at most one of these current rows was occupied.
            w += [p.one(self.current[t].anchor) for t,h in enumerate(self.targets) if a in h]
        elif kind in ('bind','copy'):
            i=op[1];dst=self.refs[i]
            if kind=='bind':
                t=op[2];w += [p.one(dst.anchor)]
                for c in range(self.colors):w+=self.emit_write((self.current[t].ports[c],),dst.cell(self.ix(t,c)))
            elif i!=op[2]:
                src=self.refs[op[2]];w += [p.one(dst.anchor)]
                for j in range(self.d*self.colors):w+=self.emit_write((src.ports[j],),dst.cell(j))
            w+=self.emit_read(dst.anchor)
        elif kind in ('drop','present'):
            row=self.refs[op[1]];w+=self.emit_read(row.anchor)
            if kind=='drop':w += [p.one(row.anchor)]
        elif kind=='same':
            i,j=op[1:]
            if i==j:w+=self.emit_read(self.refs[i].anchor)
            else:
                for v in range(self.d*self.colors):w+=self.emit_write((self.refs[i].ports[v],self.refs[j].ports[v]),self.marker)
                w+=self.emit_read(self.marker[0])+[p.one(self.marker[1])]
        elif kind=='target_is':
            i,t=op[1:]
            for c in range(self.colors):w+=self.emit_write((self.rp(i,t,c),),self.marker)
            w+=self.emit_read(self.marker[0])+[p.one(self.marker[1])]
        elif kind=='valid':
            i=op[1]
            for t in range(self.d):
                for c in range(self.colors):w+=self.emit_write((self.current[t].ports[c],self.rp(i,t,c)),self.marker)
            w+=self.emit_read(self.marker[0])+[p.one(self.marker[1])]
        elif kind=='execute':
            i=op[1]
            for t in range(self.d):
                if t:w+=self.clearout()
                w+=self.emit_local_equal(t,i)+[p.one(self.out+1)]
                w+=self.emit_write((self.out+3,),self.success)
                for c in range(self.colors):
                    w+=self.emit_write((self.current[t].ports[c],self.out+4),self.back.cell(c))
                w+=[p.one(self.current[t].anchor)]
                for c in range(self.colors):w+=self.emit_write((self.back.ports[c],),self.current[t].cell(c))
                w+=[p.one(self.back.anchor)]
            # Physical-source reconciliation. This deliberate reconstruction is
            # observed only at the complete API boundary.
            w += [p.one(a) for a in self.U]
            for t,h in enumerate(self.targets):w+=self.emit_write((self.current[t].anchor,),h)
            w+=self.clearout()+self.emit_read(self.success[0])+[p.one(self.success[1])]
        else:raise ValueError(op)
        return w
    def _uncached(self,J,raw):
        self.calls+=1;K,_,ok=e.step(J,raw,self.H);return K,bool(ok)
    def runword(self,J,word,trace=False,omitted=()):
        omit=frozenset(omitted);mass=e.prep(J);log=[]
        for k,raw in enumerate(word):
            self.uses+=1
            K,ok=(J,None) if k in omit else self._raw(J,raw)
            mass=r.serial(mass,ONE)
            if trace:log.append(dict(position=k+1,command=raw,before=J,after=K,success=ok))
            J=K
        return J,mass,log
    def run(self,J,op,trace=False):return self.runword(J,self.programs[op],trace)
    def encode(self,table,status=None):
        cur,rr=table
        ev=[]
        for t,c in enumerate(cur):
            if c is not None:ev += [self.targets[t],self.current[t].cell(c)]
        for row,q in zip(self.refs,rr):
            if q is not None:ev.append(row.cell(self.ix(*q)))
        if status is not None:ev+=p.reg(self.out,int(status))
        return m.canon(ev)
    def decode(self,J):
        # Test-only exact observation, never used by production compilation/run.
        cur=[];rr=[]
        for row in self.current:
            cc=[c for c in range(self.colors) if row.cell(c) in J]
            if len(cc)>1:raise AssertionError('Multiple current colors')
            cur.append(cc[0] if cc else None)
        for row in self.refs:
            qs=[(t,c) for t in range(self.d) for c in range(self.colors) if row.cell(self.ix(t,c)) in J]
            if len(qs)>1:raise AssertionError('Multiple reference records')
            rr.append(qs[0] if qs else None)
        table=(tuple(cur),tuple(rr));bit=p.read(J,self.out)
        ck(bit in (0,1),'Complete Boolean response')
        ck(J==self.encode(table,bit),'Exact source/table invariant and empty work area')
        return table,bool(bit)
    def stats(self):
        return dict(targets=self.targets,source_members=self.U,slots=self.slots,colors_per_target=self.colors,
                    members=self.members,candidates=len(self.H),kernel_calls=self.calls,command_uses=self.uses,
                    lengths={str(op):len(w) for op,w in self.programs.items()})

def source(C,cur):return m.canon(C.targets[t] for t,c in enumerate(cur) if c is not None)

def expected(C,table,op):
    """Independent test reducer. Source changes call the inherited raw kernel."""
    global SPEC_KERNEL
    cur,rr=map(list,table);k=op[0];value=False
    if k=='reserve':
        t=op[1];before=source(C,cur)
        after,_,value=e.step(before,p.add(C.targets[t]),frozenset(C.targets));SPEC_KERNEL+=1
        if C.targets[t] not in before and C.targets[t] in after:
            used={q[1] for q in rr if q is not None and q[0]==t}
            cur[t]=next(c for c in range(C.colors) if c not in used)
    elif k=='release':
        before=source(C,cur);after,_,value=e.step(before,p.one(op[1]),frozenset(C.targets));SPEC_KERNEL+=1
        cur=[c if C.targets[t] in after else None for t,c in enumerate(cur)]
    elif k=='bind':
        i,t=op[1:];rr[i]=None if cur[t] is None else (t,cur[t]);value=rr[i] is not None
    elif k=='copy':rr[op[1]]=rr[op[2]];value=rr[op[1]] is not None
    elif k=='drop':value=rr[op[1]] is not None;rr[op[1]]=None
    elif k=='present':value=rr[op[1]] is not None
    elif k=='target_is':value=rr[op[1]] is not None and rr[op[1]][0]==op[2]
    elif k=='same':value=rr[op[1]] is not None and rr[op[1]]==rr[op[2]]
    elif k in ('valid','execute'):
        q=rr[op[1]];value=q is not None and cur[q[0]]==q[1]
        if k=='execute' and value:
            after,_,ok=e.step(source(C,cur),p.one(min(C.targets[q[0]])),frozenset(C.targets));SPEC_KERNEL+=1
            cur=[c if C.targets[t] in after else None for t,c in enumerate(cur)]
    else:raise ValueError(op)
    return (tuple(cur),tuple(rr)),bool(value)

def canon(C,table):
    cur,rr=table;seen=[{} for _ in C.targets]
    def col(t,c):
        if c not in seen[t]:seen[t][c]=len(seen[t])
        return seen[t][c]
    a=tuple(None if c is None else col(t,c) for t,c in enumerate(cur))
    b=tuple(None if q is None else (q[0],col(*q)) for q in rr)
    return a,b

def domain(C,canonical=False):
    _,cat=e.catalog(C.targets);tables=set()
    choices=(None,)+tuple((t,c) for t in range(C.d) for c in range(C.colors))
    for J in cat:
        inds=[C.targets.index(h) for h in J]
        for cs in product(range(C.colors),repeat=len(inds)):
            cur=[None]*C.d
            for t,c in zip(inds,cs):cur[t]=c
            for rr in product(choices,repeat=C.slots):
                tab=tuple(cur),tuple(rr);tables.add(canon(C,tab) if canonical else tab)
    return tuple(sorted(tables,key=repr))

def named_from(C,table):
    cur,rr=table
    ev=tuple((C.targets[t],100+t*C.colors+c) for t,c in enumerate(cur) if c is not None)
    qs=tuple(None if q is None else (C.targets[q[0]],100+q[0]*C.colors+q[1]) for q in rr)
    return ref.Machine(ref.old.NamedState(ev,1000),qs)

def named_op(C,op):
    k=op[0]
    if k=='reserve':return ('reserve',C.targets[op[1]])
    if k=='bind':return ('bind',op[1],C.targets[op[2]])
    if k in ('present','target_is'):return ('target',op[1])
    return op

def smoke():
    C=Compiler(slots=2);table=((None,)*C.d,(None,)*C.slots);J=C.encode(table);steps=[]
    ops=(('reserve',0),('bind',0,0),('reserve',2),('bind',1,2),('same',0,1),('reserve',1),
         ('release',1),('valid',0),('valid',1),('reserve',1),('release',4),('reserve',1),
         ('execute',0),('bind',0,1),('copy',1,0),('same',0,1),('execute',0),('valid',1),
         ('reserve',0),('bind',0,0),('same',0,1),('target_is',1,1))
    for op in ops:
        want=expected(C,table,op);K,_,_=C.run(J,op);got=C.decode(K)
        ck(got==want,f'Smoke {op}: {got} vs {want}')
        steps.append(dict(op=op,before=table,after=got[0],response=got[1],source=source(C,got[0][0]),commands=len(C.programs[op])))
        J=K;table=got[0]
    return dict(mode='smoke',steps=steps,checks=CHECKS,spec_kernel=SPEC_KERNEL,**C.stats())

def audit(slots,canonical,start=0,stop=None):
    C=Compiler(slots=slots);dom=domain(C,canonical);stop=len(dom) if stop is None else min(stop,len(dom));mass=ZERO;count=0
    for ix in range(start,stop):
        tab=dom[ix];J=C.encode(tab,None if ix%3==0 else ix%2)
        for op in C.alphabet():
            K,_,_=C.run(J,op);got=C.decode(K);want=expected(C,tab,op)
            ck(got==want,f'Full exact {ix} {tab} {op}: {got} != {want}')
            count+=1;mass=r.merge(mass,ONE)
    return dict(mode='audit',canonical=canonical,domain=len(dom),start=start,stop=stop,transitions=count,
                checks=CHECKS,spec_kernel=SPEC_KERNEL,CWM=e.cw(mass),**C.stats())

def histories(depth=4):
    C=Compiler(slots=2);ops=(('reserve',0),('reserve',1),('reserve',2),('release',1),('release',4),('bind',0,0),('bind',1,2),('valid',0),('same',0,1),('execute',0))
    tab=((None,)*3,(None,)*2);J=C.encode(tab);d={(J,()):ONE};layers=[]
    for level in range(depth):
        nxt={}
        for (J,hs),mass in d.items():
            table=tab if level==0 else C.decode(J)[0]
            for op in ops:
                K,_,_=C.run(J,op);got=C.decode(K);ck(got==expected(C,table,op),'History source and reference refinement')
                key=(K,hs+(got[1],));nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
        d=nxt;total=ZERO
        for mass in d.values():total=r.merge(total,mass)
        ck(total.count==len(ops)**(level+1),'All CWM history multiplicities retained')
        layers.append(dict(depth=level+1,classes=len(d),CWM=e.cw(total)))
    return dict(mode='histories',layers=layers,checks=CHECKS,**C.stats())

def cycle(rounds=100):
    C=Compiler(slots=6);tab=((None,)*3,(None,)*6);J=C.encode(tab);ideal=ref.empty(6);records=[];count=0;maxclasses=0;used=set()
    def apply(op):
        nonlocal J,ideal,count,maxclasses
        expected_machine,val=ref.step(ideal,named_op(C,op),frozenset(C.targets))
        if op[0]=='present':val=val is not None
        if op[0]=='target_is':val=val==C.targets[op[2]]
        J,_,_=C.run(J,op);table,bit=C.decode(J)
        ck(ref.key(named_from(C,table))==ref.key(expected_machine) and bit==bool(val),'Fresh names vs physical multi-target compiler')
        ideal=expected_machine;count+=1
        pairset={(t,c) for t,c in enumerate(table[0]) if c is not None}|{q for q in table[1] if q is not None}
        maxclasses=max(maxclasses,len(pairset));used.update(pairset)
        if count<40:records.append(dict(op=op,source=source(C,table[0]),table=table,response=bit))
    for i in range(6):
        apply(('reserve',0));apply(('bind',i,0));apply(('release',1))
    apply(('reserve',0));apply(('reserve',2))
    for j in range(rounds):
        i=j%6
        for op in (('bind',i,0),('bind',(i+1)%6,2),('same',i,(i+1)%6),('reserve',1),
                   ('release',1),('valid',i),('release',4),('reserve',1),('bind',(i+2)%6,1),
                   ('copy',(i+3)%6,(i+2)%6),('same',(i+2)%6,(i+3)%6),('execute',i),
                   ('execute',(i+2)%6),('valid',(i+3)%6),('reserve',0),('reserve',2)):
            apply(op)
        if j%5==0:apply(('drop',(i+4)%6))
    return dict(mode='cycle',rounds=rounds,api_actions=count,max_live_typed_classes=maxclasses,
                used_typed_colors=sorted(used),ideal_next_name=ideal.state.next_name,initial_trace=records,
                checks=CHECKS,**C.stats())

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=('smoke','audit','histories','cycle','programs'))
    ap.add_argument('--slots',type=int,default=2);ap.add_argument('--canonical',action='store_true');ap.add_argument('--start',type=int,default=0);ap.add_argument('--stop',type=int);ap.add_argument('--depth',type=int,default=4);ap.add_argument('--rounds',type=int,default=100);ap.add_argument('--out')
    a=ap.parse_args()
    if a.mode=='smoke':result=smoke()
    elif a.mode=='audit':result=audit(a.slots,a.canonical,a.start,a.stop)
    elif a.mode=='histories':result=histories(a.depth)
    elif a.mode=='cycle':result=cycle(a.rounds)
    else:
        C=Compiler(slots=a.slots);result=dict(layout=dict(current=[row.__dict__ for row in C.current],refs=[row.__dict__ for row in C.refs],back=C.back.__dict__,block=C.block,marker=C.marker,success=C.success,work=C.work,out=C.out),stats=C.stats(),candidates=sorted(C.H),programs={str(k):v for k,v in C.programs.items()})
    text=json.dumps(result,ensure_ascii=False,indent=2)
    if a.out:Path(a.out).write_text(text+'\n',encoding='utf-8')
    else:print(text)
