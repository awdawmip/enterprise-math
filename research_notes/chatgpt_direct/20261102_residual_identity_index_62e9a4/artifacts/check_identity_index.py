"""Packed (target, colour) lookup with real triadic maintenance and verification.

Production control consumes only complete Boolean output registers. encode,
decode, base.expected and domain are verification/fixture functions, not lookup
oracles. All state-changing instructions use the unchanged inherited BRC core.
"""
from __future__ import annotations
from functools import lru_cache
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'parent'))
import check_route_index as previous
base, feedback = previous.base, previous.feedback
p, m, e, r = previous.p, previous.m, previous.e, previous.r
ONE, ZERO = previous.ONE, previous.ZERO
CHECKS = 0


def ck(ok: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(message)


class Compiler(feedback.Compiler):
    """An optional redundant index of the *whole* registered reference key."""

    def __init__(self, H=base.H_DEFAULT, slots: int = 2, index_start=None):
        super().__init__(H=H, slots=slots)
        self.parent_members = self.members
        self.parent_candidates = len(self.H)
        self.bits = (self.d * self.colors).bit_length()
        first = self._next if index_start is None else index_start
        if first < self._next:
            raise ValueError('Index overlaps the existing source or workspace')
        self.index = tuple(tuple(tuple(range(first + 3*(i*self.bits+b),
                                              first + 3*(i*self.bits+b) + 3))
                                 for b in range(self.bits)) for i in range(slots))
        self.tags = frozenset(h for row in self.index for h in row)
        self.H = set(self.H) | set(self.tags)
        self.reads = {(i,b): tuple(self.clearout() + self.emit_read(bit[0]))
                      for i,row in enumerate(self.index) for b,bit in enumerate(row)}
        # Exact lookup needs only the corresponding current-record port, because
        # its index-to-reference invariant has already identified the request.
        self.current_reads = {(t,c): tuple(self.clearout() + self.emit_read(self.current[t].ports[c]))
                              for t in range(self.d) for c in range(self.colors)}
        # An arbitrary hint must verify BOTH its current endpoint and its
        # referring endpoint. Each of these blocks is exactly 13 instructions.
        self.pair_checks = {(i,t,c): tuple(self.clearout()
                             + self.emit_write((self.current[t].ports[c], self.rp(i,t,c)), self.marker)
                             + self.emit_read(self.marker[0]) + [p.one(self.marker[1])])
                            for i in range(slots) for t in range(self.d) for c in range(self.colors)}
        self.base_programs = dict(self.programs)
        for op, word in list(self.programs.items()):
            suffix = []
            if op[0] == 'bind':
                i,t = op[1:]
                suffix = self.clear_index(i)
                for c in range(self.colors):
                    for b in range(self.bits):
                        if self.key(t,c) >> b & 1:
                            suffix += self.emit_write((self.rp(i,t,c),), self.index[i][b])
            elif op[0] == 'copy' and op[1] != op[2]:
                i,j = op[1:]
                suffix = self.clear_index(i)
                for b in range(self.bits):
                    suffix += self.emit_write((self.index[j][b][0],), self.index[i][b])
            elif op[0] == 'drop':
                suffix = self.clear_index(op[1])
            self.programs[op] = word + tuple(suffix)
        self.repairs = {}
        for i in range(slots):
            w = self.clear_index(i)
            for t in range(self.d):
                for c in range(self.colors):
                    for b in range(self.bits):
                        if self.key(t,c) >> b & 1:
                            w += self.emit_write((self.rp(i,t,c),), self.index[i][b])
            self.repairs[i] = tuple(w)
        self.H = frozenset(self.H)
        self.members = self.parent_members + 3*slots*self.bits
        self._raw = lru_cache(maxsize=500000)(self._uncached)
        self.calls = self.uses = 0

    def key(self, t: int, c: int) -> int:
        return 1 + t*self.colors + c

    def clear_index(self, i):
        return [p.one(bit[0]) for bit in self.index[i]]

    def encode(self, table, status=None):
        ev = list(super().encode(table, status))
        for i,q in enumerate(table[1]):
            code = 0 if q is None else self.key(*q)
            ev.extend(self.index[i][b] for b in range(self.bits) if code >> b & 1)
        return m.canon(ev)

    def strip_index(self, J):
        return m.canon(h for h in J if h not in self.tags)

    def decode(self, J):
        # Test-only observation of the complete persistent and working state.
        cur, refs = [], []
        for row in self.current:
            found = [c for c in range(self.colors) if row.cell(c) in J]
            ck(len(found) <= 1, 'unique current instance')
            cur.append(found[0] if found else None)
        for row in self.refs:
            found = [(t,c) for t in range(self.d) for c in range(self.colors)
                     if row.cell(self.ix(t,c)) in J]
            ck(len(found) <= 1, 'unique reference')
            refs.append(found[0] if found else None)
        table = tuple(cur), tuple(refs)
        answer = p.read(J,self.out)
        ck(answer in (0,1), 'complete Boolean answer')
        ck(J == self.encode(table, answer), 'entire source/reference/key/output state and empty work')
        return table, bool(answer)

    def dispatch(self, J, i, trace=False, delete=True, mode='exact', repeats=1, omitted=()):
        """exact: correct index required; hint: arbitrary bits, verify then scan."""
        if not 0 <= i < self.slots or repeats < 1 or mode not in ('exact','hint'):
            raise ValueError('Invalid lookup parameters')
        word, logs, observations = [], [], []
        mass = e.prep(J)
        omissions = set(omitted)
        def do(block):
            nonlocal J, mass
            expanded = tuple(raw for raw in block for _ in range(repeats))
            offset = len(word)
            local = tuple(k-offset for k in omissions if offset <= k < offset+len(expanded))
            J, wm, records = self.runword(J,expanded,trace,local)
            mass = r.serial(mass,wm)
            word.extend(expanded); logs.extend(records)
        code = 0
        for b in range(self.bits):
            do(self.reads[i,b])
            bit = self.observe_result(J)
            observations.append(('key_bit',b,bit))
            code |= int(bit) << b
        in_range = 1 <= code <= self.d*self.colors
        hit = False
        if mode == 'exact' and code > self.d*self.colors:
            raise ValueError('Key index is outside the exact coding domain')
        if in_range:
            # Arithmetic here is precompiled address selection from observed
            # bits; it never inspects the source or a reference row.
            t,c = divmod(code-1,self.colors)
            do(self.current_reads[t,c] if mode == 'exact' else self.pair_checks[i,t,c])
            hit = self.observe_result(J)
            observations.append(('current_port' if mode=='exact' else 'pair_witness',t,c,hit))
            if hit and delete:
                do(self.commit(t))
        if mode == 'hint' and not hit:
            for t in range(self.d):
                do(self.programs['match',i,t])
                bit = self.observe_result(J)
                observations.append(('fallback_match',t,bit))
                if bit:
                    if delete: do(self.commit(t))
                    break
        valid = self.observe_result(J)
        return J, mass, dict(code=code, hit=hit, valid=valid, mode=mode,
             commands=len(word), feedback=len(observations), observations=observations,
             word=tuple(word), trace=logs)

    def run(self, J, op, trace=False):
        if op[0] in ('execute','valid'):
            K,wm,data = self.dispatch(J,op[1],trace,delete=op[0]=='execute')
            return K,wm,data['trace']
        return self.runword(J,self.programs[op],trace)

    def metrics(self):
        return dict(assertions=CHECKS, targets=self.d, slots=self.slots, colors=self.colors,
                    key_bits=self.bits, members=self.members, candidates=len(self.H),
                    kernel_cache_misses=self.calls, primitive_uses=self.uses)


def audit(slots=2,canonical=False):
    C=Compiler(slots=slots);domain=base.domain(C,canonical=canonical);cases=probes=0;mass=ZERO
    for n,table in enumerate(domain):
        J=C.encode(table,(None,0,1)[n%3])
        for op in base.Compiler.alphabet(C):
            K,wm,_=C.run(J,op)
            ck(C.decode(K)==base.expected(C,table,op),f'full API {n} {op}')
            cases+=1;mass=r.merge(mass,wm)
        for i in range(slots):
            for b in range(C.bits):
                K,_,_=C.runword(J,C.reads[i,b])
                code=0 if table[1][i] is None else C.key(*table[1][i])
                ck(K==C.encode(table,bool(code>>b&1)), 'key probe restores source and work')
                probes+=1
    return dict(mode='audit',canonical=canonical,domain=len(domain),cases=cases,probe_cases=probes,CWM=e.cw(mass),**C.metrics())


def costs():
    C=Compiler(slots=6);old=previous.Compiler(slots=6);rows=[]
    for label,cur,q in [('A',(0,None,0),(0,0)),('B',(None,0,None),(1,0)),
                        ('C',(0,None,0),(2,0)),('stale_A',(1,None,0),(0,0)),
                        ('stale_B',(0,None,0),(1,0)),('empty',(0,None,0),None)]:
        table=cur,(q,)+(None,)*5;J=C.encode(table)
        K,_,data=C.dispatch(J,0)
        O,_,before=old.dispatch(old.encode(table),0)
        ck(C.strip_index(K)==old.strip_index(O),'same logical endpoint as target index')
        ck(C.decode(K)==base.expected(C,table,('execute',0)),'exact key endpoint')
        st=base.ref.old.seed(J);initial=st.names();retired=[]
        target=C.targets[q[0]] if data['valid'] else None
        for raw in data['word']:
            st,_,delta=base.ref.old.raw_step(st,raw,C.H)
            retired.extend(h for h,n in delta['retired'] if h in C.targets)
            for h,n in initial.items():
                if h in C.targets and h!=target:ck(st.names().get(h)==n,'unrelated source birth every prefix')
        ck(st.matching==K and retired==([] if target is None else [target]), 'exact source footprint')
        formula=8*C.bits+(8 if q else 0)+(2 if data['valid'] else 0)
        ck(data['commands']==formula,'exact executed cost')
        H,_,hint=C.dispatch(J,0,mode='hint')
        ck(C.strip_index(H)==C.strip_index(K),'exact-index hint endpoint')
        rows.append(dict(name=label,key=data['code'],commands=data['commands'],old_target_index=before['commands'],
                         checked_hint=hint['commands'],observations=data['observations'],retired=retired))
    updates={str(op):len(w)-len(C.base_programs[op]) for op,w in C.programs.items()
             if op[0] in ('bind','copy','drop') and (len(op)<2 or op[1]==0)}
    table=((0,None,0),((0,0),(2,0),None,(1,0),(0,1),(2,0)))
    raw=feedback.Compiler.encode(C,table,True)
    w=tuple(raw for i in range(C.slots) for raw in C.repairs[i])
    migrated,_,_=C.runword(raw,w)
    ck(migrated==C.encode(table,True),'migration generates exact key index and keeps old answer')
    old_encoded=old.encode(table,True)
    convert=tuple(raw for i in range(C.slots) for raw in old.clear_index(i))+w
    converted,_,_=C.runword(old_encoded,convert)
    ck(converted==C.encode(table,True),'old target directory retired and full key directory created')
    return dict(mode='costs',paths=rows,updates=updates,migration_commands=len(w),
                target_directory_conversion_commands=len(convert),**C.metrics())


def hints():
    C=Compiler(slots=2);F=feedback.Compiler(slots=2);cases=hits=0;mass=ZERO
    domain=base.domain(C,canonical=True)
    for table in domain:
        original=F.encode(table)
        for i in range(C.slots):
            baseline,_,_=F.feedback(original,i)
            other=C.encode(table)
            other,_,_=C.runword(other,C.clear_index(i))
            for code in range(1<<C.bits):
                J,_,_=C.runword(other,tuple(p.add(C.index[i][b]) for b in range(C.bits) if code>>b&1))
                K,wm,data=C.dispatch(J,i,mode='hint')
                ck(C.strip_index(K)==baseline,'arbitrary full-key hint has baseline endpoint')
                ck(tuple(h for h in K if h in C.tags)==tuple(h for h in J if h in C.tags),'hint bits retained')
                q=table[1][i]
                want=bool(q is not None and table[0][q[0]]==q[1] and code==C.key(*q))
                ck(data['hit']==want,'hit iff true request and current joint witness')
                cases+=1;hits+=int(data['hit']);mass=r.merge(mass,wm)
    return dict(mode='hints',domain=len(domain),canonical=True,cases=cases,hits=hits,CWM=e.cw(mass),**C.metrics())


def failures():
    C=Compiler(slots=1);out=[]
    # Replace stale request's directory by the CURRENT label. Exact lookup
    # relies on an invariant it no longer has; the pair-verified hint is safe.
    table=((1,None,0),((0,0),));J=C.encode(table)
    J,_,_=C.runword(J,C.clear_index(0))
    code=C.key(0,1)
    J,_,_=C.runword(J,[p.add(C.index[0][b]) for b in range(C.bits) if code>>b&1])
    bad,_,bd=C.dispatch(J,0);good,_,gd=C.dispatch(J,0,mode='hint')
    ck(bd['valid'] and C.targets[0] not in bad,'unchecked stale key can delete current replacement')
    ck(not gd['valid'] and C.targets[0] in good,'paired witness rejects wrong reference key')
    out.append(dict(name='stale_request_current_key',source_before=base.source(C,table[0]),
                    arbitrary_hint=code,bad_response=bd['valid'],verified_response=gd['valid'],
                    bad_source=[h for h in bad if h in C.targets],verified_source=[h for h in good if h in C.targets],
                    observations=gd['observations']))
    # The obsolete hint names an existing unrelated target; current-only
    # verification says yes, whereas request+current says no then finds C.
    table=((0,None,0),((2,0),));J=C.encode(table)
    J,_,_=C.runword(J,C.clear_index(0))
    code=C.key(0,0)
    J,_,_=C.runword(J,[p.add(C.index[0][b]) for b in range(C.bits) if code>>b&1])
    bad,_,_=C.dispatch(J,0);good,_,gd=C.dispatch(J,0,mode='hint')
    ck(C.targets[0] not in bad and C.targets[2] in bad,'current-only wrong target deleted')
    ck(C.targets[0] in good and C.targets[2] not in good,'full witness miss falls back to correct target')
    out.append(dict(name='wrong_existing_target',hint=code,verified_observations=gd['observations'],
                    bad_source=[h for h in bad if h in C.targets],good_source=[h for h in good if h in C.targets]))
    # Two currently valid references can share a key. It says nothing about
    # whether they are the same physical reference row or the same caller.
    return dict(mode='failures',cases=out,**C.metrics())


def lifecycle(rounds=20):
    C=Compiler(slots=6);table=((None,)*3,(None,)*6);J=C.encode(table);commands=actions=0;records=[]
    def apply(op):
        nonlocal table,J,commands,actions
        want=base.expected(C,table,op);before=C.uses
        J,_,_=C.run(J,op);commands+=C.uses-before;actions+=1
        ck(C.decode(J)==want,'whole maintained full key API lifecycle');table=want[0]
        if len(records)<30:records.append(dict(op=op,table=table,response=want[1]))
    apply(('reserve',0));apply(('reserve',2))
    for n in range(rounds):
        i=n%6;j=(i+1)%6;k=(i+2)%6
        for op in [('bind',i,0),('copy',j,i),('valid',j),('execute',i),('valid',j),('same',i,j),
                   ('reserve',0),('execute',j),('bind',i,2),('copy',k,i),('target_is',k,2),
                   ('bind',j,1),('drop',i),('copy',i,j),('bind',i,0),('copy',i,i)]:
            apply(op)
    return dict(mode='lifecycle',rounds=rounds,api_calls=actions,commands=commands,records=records,**C.metrics())


def workload():
    C=Compiler(slots=6);T=previous.Compiler(slots=6);rows=[]
    for t in range(C.d):
        cur=(None,0,None) if t==1 else (0,None,0);table=cur,(None,)*6
        J=C.encode(table);K=T.encode(table)
        J,_,_=C.run(J,('bind',0,t));K,_,_=T.run(K,('bind',0,t))
        readnew=readold=0
        # Validity queries preserve the target, so repeated reading is genuine.
        for _ in range(20):
            b=C.uses;J,_,_=C.run(J,('valid',0));readnew+=C.uses-b
            b=T.uses;K,_,_=T.run(K,('valid',0));readold+=T.uses-b
        ck(C.strip_index(J)==T.strip_index(K),'same live state after repeated true validity reads')
        newbind=len(C.programs['bind',0,t]);oldbind=len(T.programs['bind',0,t])
        saving=(readold-readnew)//20
        excess=newbind-oldbind
        break_even=None if saving<=0 else excess//saving+1
        rows.append(dict(target=t,key_bind=newbind,target_bind=oldbind,
                         key_valid=readnew//20,target_valid=readold//20,
                         strictly_better_after_reads=break_even,
                         twenty_read_new_total=newbind+readnew,twenty_read_old_total=oldbind+readold))
    return dict(mode='workload',rows=rows,**C.metrics())


def scaling():
    rows=[]
    # Full colour-state execution, not just evaluation of the formula.
    for d,slots in ((1,1),(3,2),(3,6),(3,14),(3,30),(7,6),(15,6),(31,6)):
        H=tuple((3*t+1,3*t+2,3*t+3) for t in range(d));C=Compiler(H,slots);cases=0
        longest=0
        for t in range(d):
            for c in range(C.colors):
                table=tuple(c if j==t else 0 for j in range(d)),((t,c),)+(None,)*(slots-1)
                K,_,data=C.dispatch(C.encode(table),0)
                ck(C.decode(K)==base.expected(C,table,('execute',0)), 'scaled full key')
                longest=max(longest,data['commands']);cases+=1
        table=(0,)*d,((0,1),)+(None,)*(slots-1)
        K,_,stale=C.dispatch(C.encode(table),0);ck(not C.decode(K)[1],'scaled stale')
        table=(0,)*d,(None,)*slots
        K,_,empty=C.dispatch(C.encode(table),0);ck(not C.decode(K)[1],'scaled empty')
        ck(longest==8*C.bits+10,'full key exact valid length')
        rows.append(dict(targets=d,slots=slots,colors=C.colors,bits=C.bits,cases=cases+2,
                         exact_valid=longest,exact_stale=stale['commands'],empty=empty['commands'],
                         old_target_valid=8*d.bit_length()+4*C.colors+11,
                         pair_verified_hit=8*C.bits+15,members=C.members,candidates=len(C.H)))
    return dict(mode='scaling',rows=rows,assertions=CHECKS)


def export():
    C=Compiler(slots=6)
    return dict(controller='read all full key bits; code 0=false; code(t,c): direct current-port read, then commit iff true; hint mode uses 13-step pair check and fallback',
                bits=C.bits,layout=C.index,members=C.members,candidates=sorted(C.H),
                reads={str(k):v for k,v in C.reads.items()},current_reads={str(k):v for k,v in C.current_reads.items()},
                pair_checks={str(k):v for k,v in C.pair_checks.items()},
                maintenance={str(k):v for k,v in C.programs.items() if k[0] in ('bind','copy','drop')},repairs=C.repairs)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=('audit','costs','hints','failures','lifecycle','workload','scaling','programs'))
    ap.add_argument('--slots',type=int,default=2);ap.add_argument('--canonical',action='store_true');ap.add_argument('--out');a=ap.parse_args()
    ans=audit(a.slots,a.canonical) if a.mode=='audit' else export() if a.mode=='programs' else globals()[a.mode]()
    text=json.dumps(ans,ensure_ascii=False,indent=2)+'\n'
    if a.out:Path(a.out).write_text(text)
    else:print(text)
