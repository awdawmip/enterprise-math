"""Fixed reserve/release compilation of a one-object dynamic reference API.

All production state is the inherited unlabelled triadic matching. There is no
runtime color chooser, equality oracle, or metadata table. Python decoding and
the parent's named interpreter are used only by tests. Correctness is at complete
API boundaries in a closed, sequential environment.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from functools import lru_cache
import argparse, json, sys
ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'parent'
if not PARENT.exists(): PARENT=Path('/mnt/data/alias_parent')
sys.path.insert(0,str(PARENT))
import check_dynamic_alias as ref
p,m,e,r=ref.p,ref.m,ref.e,ref.r
ONE,ZERO=ref.ONE,ref.ZERO
reader=ref.old.prior.reader
write=ref.old.prior.write
HLOG=(1,2,3)
CHECKS=0

def ck(v,msg):
    global CHECKS
    CHECKS+=1
    if not v: raise AssertionError(msg)

@dataclass(frozen=True)
class Row:
    anchor:int
    control:int
    ports:tuple[int,...]
    def cell(self,c): return tuple(sorted((self.anchor,self.control,self.ports[c])))

class Compiler:
    def __init__(self,slots:int):
        if slots<1: raise ValueError('At least one registered reference slot required')
        self.slots=slots;self.colors=slots+1
        nxt=1;rows=[]
        for _ in range(slots+2):
            rows.append(Row(nxt,nxt+1,tuple(range(nxt+2,nxt+2+self.colors))))
            nxt+=self.colors+2
        self.rows=tuple(rows[:-1]);self.back=rows[-1]
        self.block=(nxt,nxt+1);nxt+=2
        self.marker=tuple(range(nxt,nxt+3));nxt+=3
        self.work=nxt;nxt+=1
        self.out=nxt-1;nxt+=6
        self.members=nxt-1
        self.H={row.cell(c) for row in rows for c in range(self.colors)}|p.library(self.out)|{self.marker}
        self.programs={op:tuple(self._compile(op)) for op in self.alphabet()}
        self.H=frozenset(self.H)
        self.calls=0;self.uses=0
        self._raw=lru_cache(maxsize=300000)(self._uncached)
    def alphabet(self):
        n=self.slots
        return (('create',),('destroy',))+tuple((kind,i) for kind in ('bind','drop','valid','present','execute') for i in range(n))+tuple((kind,i,j) for kind in ('copy','same') for i in range(n) for j in range(n))
    def emit_write(self,ports,target):
        h,w=write(tuple(ports),target,self.work);self.H|=h;return list(w)
    def emit_read(self,port,invert=False):
        h,w,_=reader(port,self.out,self.work,invert=invert);self.H|=h;return list(w)
    def emit_copy(self,src,dst):
        return [op for c in range(self.colors) for op in self.emit_write((src.ports[c],),dst.cell(c))]
    def emit_equal(self,a,b):
        if a==b:return self.emit_read(a.anchor)
        w=[]
        for c in range(self.colors):w+=self.emit_write((a.ports[c],b.ports[c]),self.marker)
        return w+self.emit_read(self.marker[0])+[p.one(self.marker[1])]
    def _compile(self,op):
        kind=op[0];cur=self.rows[0]
        # Output is private and may hold the preceding call's complete result.
        w=[p.one(self.out+1),p.one(self.out+5)]
        if kind=='create':
            w+=self.emit_read(cur.anchor,invert=True)
            for c in range(self.colors):
                block=tuple(sorted((cur.ports[c],*self.block)))
                self.H.add(block)
                for row in self.rows[1:]:w+=self.emit_write((row.ports[c],),block)
                w += [p.add(cur.cell(c)),p.one(self.block[0])]
        elif kind=='destroy':
            w+=self.emit_read(cur.anchor)+[p.one(cur.anchor)]
        elif kind in ('bind','copy'):
            dst=self.rows[op[1]+1];src=cur if kind=='bind' else self.rows[op[2]+1]
            if src!=dst:w += [p.one(dst.anchor)]+self.emit_copy(src,dst)
            w+=self.emit_read(dst.anchor)
        elif kind=='drop':
            row=self.rows[op[1]+1];w+=self.emit_read(row.anchor)+[p.one(row.anchor)]
        elif kind=='present':w+=self.emit_read(self.rows[op[1]+1].anchor)
        elif kind in ('same','valid'):
            a=self.rows[op[1]+1];b=cur if kind=='valid' else self.rows[op[2]+1]
            w+=self.emit_equal(a,b)
        elif kind=='execute':
            w+=self.emit_equal(cur,self.rows[op[1]+1])
            # Retain current color only on the false branch. This deliberately
            # refines logical identity, not the birth identity of a physical cell.
            w+=[p.one(self.out+1)]
            for c in range(self.colors):
                w+=self.emit_write((cur.ports[c],self.out+4),self.back.cell(c))
            w+=[p.one(cur.anchor)]
            w+=self.emit_copy(self.back,cur)
            w += [p.one(self.back.anchor),p.add(p.reg(self.out,0)[0]),p.add(p.reg(self.out,1)[0])]
        else:raise ValueError(op)
        return w
    def _uncached(self,J,op):
        self.calls+=1
        out,_,ok=e.step(J,op,self.H)
        return out,bool(ok)
    def runword(self,J,word,trace=False,omitted=()):
        omitted=frozenset(omitted);mass=e.prep(J);log=[]
        for t,raw in enumerate(word):
            self.uses+=1
            if t in omitted:K,ok=J,None
            else:K,ok=self._raw(J,raw)
            mass=r.serial(mass,ONE)
            if trace:log.append(dict(position=t+1,command=raw,before=J,after=K,success=ok))
            J=K
        return J,mass,log
    def run(self,J,op,trace=False):return self.runword(J,self.programs[op],trace)
    def encode(self,colors,status=None):
        if len(colors)!=len(self.rows):raise ValueError('Wrong row count')
        J=tuple(row.cell(c) for row,c in zip(self.rows,colors) if c is not None)
        if status is not None:J+=p.reg(self.out,status)
        return m.canon(J)
    def decode(self,J):
        # Test-only observer. Production command compilation never calls this.
        values=[]
        for row in self.rows:
            cs=[c for c in range(self.colors) if row.cell(c) in J]
            if len(cs)>1:raise AssertionError('Multiple one-hot cells in a row')
            values.append(cs[0] if cs else None)
        value=p.read(J,self.out)
        if value not in (0,1):raise AssertionError('Response is not a complete bit')
        ck(J==self.encode(tuple(values),value),'Exact postcondition: only table and complete response, no temporary events')
        return tuple(values),bool(value)
    def stats(self):
        return dict(slots=self.slots,colors=self.colors,members=self.members,candidates=len(self.H),kernel_calls=self.calls,command_uses=self.uses,lengths={str(k):len(v) for k,v in self.programs.items()})

# Independent specification adapter: reuses the parent's actual named interpreter.
def ideal(colors):
    cur,*slots=colors
    ev=() if cur is None else ((HLOG,cur+1),)
    qs=tuple(None if c is None else (HLOG,c+1) for c in slots)
    return ref.Machine(ref.old.NamedState(ev,1000),qs)

def parent_op(op):
    k=op[0]
    if k=='create':return ('reserve',HLOG)
    if k=='destroy':return ('release',1)
    if k=='bind':return ('bind',op[1],HLOG)
    if k=='present':return ('target',op[1])
    return op

def expected(colors,op,M):
    z,value=ref.step(ideal(colors),parent_op(op),frozenset({HLOG}),palette=M)
    ns=z.state.names();out=(None if HLOG not in ns else ns[HLOG]-1,)+tuple(None if q is None else q[1]-1 for q in z.refs)
    return out,bool(value)

def canonical(colors):
    seen={};out=[]
    for c in colors:
        if c is None:out.append(None)
        else:
            if c not in seen:seen[c]=len(seen)
            out.append(seen[c])
    return tuple(out)

def audit(slots,start,stop,canonical_only=False):
    C=Compiler(slots);choices=(None,)+tuple(range(C.colors))
    if canonical_only:
        domain=tuple(sorted({canonical(x) for x in product(choices,repeat=slots+1)},key=repr))
    else:domain=tuple(product(choices,repeat=slots+1))
    mass=ZERO;count=0
    for index in range(start,min(stop,len(domain))):
        cs=domain[index];old_status=index%3-1
        J=C.encode(cs,None if old_status<0 else old_status)
        for op in C.alphabet():
            K,_,_=C.run(J,op);got=C.decode(K);want=expected(cs,op,C.colors)
            ck(got==want,f'Refinement {cs} {op}: {got} != {want}')
            mass=r.merge(mass,ONE);count+=1
    return dict(mode='audit',domain_size=len(domain),start=start,stop=min(stop,len(domain)),transitions=count,checks=CHECKS,CWM=e.cw(mass),**C.stats())

def smoke():
    C=Compiler(6);cs=(None,)*7;J=C.encode(cs);rows=[]
    ops=(('create',),('bind',0),('copy',1,0),('destroy',),('create',),('valid',0),('same',0,1),('bind',2),('execute',0),('execute',2),('same',0,1),('drop',0),('drop',1),('create',),('bind',3))
    for op in ops:
        want=expected(cs,op,C.colors);K,_,_=C.run(J,op);got=C.decode(K)
        ck(got==want,'Six-reference semantic chain')
        rows.append(dict(op=op,before=cs,after=got[0],response=got[1],commands=len(C.programs[op])))
        J=K;cs=got[0]
    return dict(rows=rows,checks=CHECKS,**C.stats())

def cycle(rounds=1000):
    C=Compiler(6);J=C.encode((None,)*7);I=ref.empty(6);steps=0;maximum=0;used=set();counts={}
    def apply(op):
        nonlocal J,I,steps,maximum
        I,val=ref.step(I,parent_op(op),frozenset({HLOG}))
        J,_,_=C.run(J,op);cs,bit=C.decode(J)
        ck(canonical(cs)==canonical((None if not I.state.events else I.state.events[0][1],)+tuple(None if x is None else x[1] for x in I.refs)) and bit==bool(val),'Actual finite physical implementation vs fresh-name interpreter')
        used.update(c for c in cs if c is not None);maximum=max(maximum,len(set(c for c in cs if c is not None)))
        steps+=1;counts[op[0]]=counts.get(op[0],0)+1
    for i in range(6):
        apply(('create',));apply(('bind',i));apply(('destroy',))
    apply(('create',))
    for j in range(rounds):
        i=j%6
        apply(('bind',i));apply(('copy',(i+1)%6,i));apply(('same',i,(i+1)%6))
        apply(('destroy',));apply(('create',));apply(('valid',i));apply(('execute',i))
        if j%5==0:apply(('drop',(i+2)%6))
        if j%7==0:apply(('present',(i+3)%6))
    return dict(rounds=rounds,API_actions=steps,counts=counts,ideal_next_name=I.state.next_name,max_live_classes=maximum,colors_used=sorted(used),checks=CHECKS,**C.stats())

def histories(depth=4):
    C=Compiler(2);ops=(('create',),('destroy',),('bind',0),('bind',1),('copy',1,0),('drop',0),('valid',0),('same',0,1))
    J=C.encode((None,)*3);d={(J,()):ONE};layers=[]
    for level in range(depth):
        nxt={}
        for (J,history),mass in d.items():
            # Empty initial response is handled separately only at level zero.
            cs=(None,)*3 if level==0 else C.decode(J)[0]
            for op in ops:
                K,_,_=C.run(J,op);got=C.decode(K);want=expected(cs,op,C.colors)
                ck(got==want,'All-history macro refinement')
                key=(K,history+(got[1],));nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
        d=nxt;total=ZERO
        for mass in d.values():total=r.merge(total,mass)
        ck(total.count==len(ops)**(level+1),'All histories kept with positive CWM multiplicity')
        layers.append(dict(depth=level+1,classes=len(d),CWM=e.cw(total)))
    return dict(layers=layers,checks=CHECKS,**C.stats())

def faults():
    C=Compiler(1);ops=(('create',),('bind',0),('destroy',),('create',),('valid',0))
    word=tuple(raw for op in ops for raw in C.programs[op]);initial=C.encode((None,None))
    target=C.runword(initial,word)[0];out=[]
    for budget in (1,2):
        repeated=tuple(raw for raw in word for _ in range(budget+1))
        d={(initial,0):ONE}
        for raw in repeated:
            nxt={}
            for (J,miss),mass in d.items():
                C.uses+=1;K,_=C._raw(J,raw)
                key=(K,miss);nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
                if miss<budget:
                    key=(J,miss+1);nxt[key]=r.merge(nxt.get(key,ZERO),r.serial(mass,ONE))
            d=nxt
        totals={}
        for (K,miss),mass in d.items():
            ck(K==target,'Shared omission budget across complete compiled lifecycle')
            totals[miss]=r.merge(totals.get(miss,ZERO),mass)
        out.append(dict(budget=budget,base_length=len(word),protected_length=len(repeated),counts={str(k):e.cw(v) for k,v in totals.items()}))
    return dict(results=out,checks=CHECKS,**C.stats())

def boundaries():
    C=Compiler(1);cur,slot=C.rows
    # A single omitted actual busy-marker write lets a stale reference revive.
    J=C.encode((None,0));word=C.programs[('create',)]
    busy=tuple(sorted((cur.ports[0],*C.block)))
    pos=word.index(p.add(busy))
    K,_,log=C.runword(J,word,trace=True,omitted=(pos,))
    bad=C.decode(K)[0];ck(bad==(0,0),'Omitted used-color record reuses still referenced color')
    V,_,_=C.run(K,('valid',0));ck(C.decode(V)[1],'Stale reference actually revived')
    # Ordinary invalid execution preserves logical state at the API boundary,
    # but temporarily opens the encoded current row.
    before=(1,0);J=C.encode(before)
    K,_,trace=C.run(J,('execute',0),trace=True)
    ck(C.decode(K)==(before,False),'Invalid execution exact logical endpoint')
    transient=[t for t in trace if not any(cur.cell(c) in t['after'] for c in range(C.colors))]
    ck(bool(transient),'Microstep observer can see temporary absence')
    # Closed-reference assumption: a hidden old color is allowed to be reused.
    J=C.encode((None,None));K,_,_=C.run(J,('create',));cs,_=C.decode(K)
    ck(cs[0]==0,'Free color chosen by physical competition')
    hidden_return=m.canon(K+(slot.cell(0),))
    V,_,_=C.run(hidden_return,('valid',0));ck(C.decode(V)[1],'Externally reintroduced hidden old reference matches reused color')
    # Two cells cannot literally share the color member in a matching.
    wrong=((300,310,320),(301,310,321));L=()
    for edge in wrong:L,_,_=e.step(L,p.add(edge),frozenset(wrong))
    ck(len(L)==1,'Naive shared-member identity cannot store two aliases')
    return dict(single_omission_position=pos+1,omission_trace=log,invalid_execute_trace=trace,transient_absence_positions=[x['position'] for x in transient],naive_alias_result=L,checks=CHECKS,**C.stats())

def programs():
    out={}
    for n in (1,2,4,6):
        C=Compiler(n)
        out[str(n)]={'layout':{'rows':[dict(anchor=x.anchor,control=x.control,ports=x.ports) for x in C.rows], 'backup':dict(anchor=C.back.anchor,control=C.back.control,ports=C.back.ports),'block_members':C.block,'marker':C.marker,'work':C.work,'output_offset':C.out},'library':sorted(C.H),'programs':[dict(action=k,commands=v) for k,v in C.programs.items()],**C.stats()}
    return out

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['smoke','audit','cycle','histories','faults','boundaries','programs']);ap.add_argument('--slots',type=int,default=2);ap.add_argument('--start',type=int,default=0);ap.add_argument('--stop',type=int,default=100000);ap.add_argument('--canonical',action='store_true');ap.add_argument('--rounds',type=int,default=1000);ap.add_argument('--depth',type=int,default=4);ap.add_argument('--out',required=True)
    a=ap.parse_args()
    if a.mode=='audit':z=audit(a.slots,a.start,a.stop,a.canonical)
    elif a.mode=='cycle':z=cycle(a.rounds)
    elif a.mode=='histories':z=histories(a.depth)
    else:z=globals()[a.mode]()
    Path(a.out).write_text(json.dumps(z,ensure_ascii=False,indent=2)+'\n')
    if a.mode!='programs':print(json.dumps({k:v for k,v in z.items() if k not in ('rows','lengths','omission_trace','invalid_execute_trace')},ensure_ascii=False))
