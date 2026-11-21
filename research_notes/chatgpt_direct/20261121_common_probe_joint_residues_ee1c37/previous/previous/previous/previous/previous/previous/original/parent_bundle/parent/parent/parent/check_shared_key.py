"""Shared current-key materialization with exact request snapshots.

All matching transitions use the unchanged inherited BRC kernel.  encode,
decode, expected_cache and abstract parent reducers are verification fixtures;
production words never call them.  Policy='guarded' permits a stale cache only
while its current source row is empty, and gates each copied bit by the actual
new reference row.  Policy='eager' clears that cache on retirement.
"""
from __future__ import annotations
from functools import lru_cache
from pathlib import Path
import argparse, json, sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'parent'))
import check_identity_index as prior
base, feedback = prior.base, prior.feedback
p, m, e, r = prior.p, prior.m, prior.e, prior.r
ONE, ZERO = prior.ONE, prior.ZERO
CHECKS = 0


def ck(value, label):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(label)


class Compiler(prior.Compiler):
    def __init__(self, H=base.H_DEFAULT, slots=2, index_start=None, policy='guarded'):
        if policy not in ('eager', 'guarded', 'feedback'):
            raise ValueError('Unknown current-key cache policy')
        # Parent construction emits programs by virtual dispatch; policy must
        # already exist, while commit() allows for not-yet-allocated cache rows.
        self.policy = policy
        super().__init__(H=H, slots=slots, index_start=index_start)
        self.full_key_members = self.members
        self.full_key_candidates = len(self.H)
        first = max(x for h in self.H for x in h) + 1
        self.shared = tuple(tuple(tuple(range(first+3*(t*self.bits+b),
                                               first+3*(t*self.bits+b)+3))
                                  for b in range(self.bits)) for t in range(self.d))
        self.shared_tags = frozenset(h for row in self.shared for h in row)
        self.H = set(self.H) | set(self.shared_tags)
        self.refresh = {}
        self.bind_copy = {}
        for t in range(self.d):
            word = self.clear_shared(t)
            for c in range(self.colors):
                for b in range(self.bits):
                    if self.key(t,c) >> b & 1:
                        word += self.emit_write((self.current[t].ports[c],), self.shared[t][b])
            self.refresh[t] = tuple(word)
        for op, word in list(self.programs.items()):
            if op[0] == 'reserve':
                self.programs[op] = word + self.refresh[op[1]]
            elif op[0] == 'release' and policy == 'eager':
                self.programs[op] = word + tuple(raw for t,h in enumerate(self.targets)
                                                if op[1] in h for raw in self.clear_shared(t))
            elif op[0] == 'bind':
                i,t = op[1:]
                suffix = self.clear_index(i)
                for b in range(self.bits):
                    ports = (self.shared[t][b][0],)
                    if policy == 'guarded':
                        ports = (self.refs[i].anchor,) + ports
                    suffix += self.emit_write(ports, self.index[i][b])
                self.programs[op] = self.base_programs[op] + tuple(suffix)
                self.bind_copy[i,t] = tuple(suffix)
        if policy == 'feedback':
            for op in list(self.programs):
                if op[0] in ('bind', 'reserve'):
                    del self.programs[op]  # Only the result-driven block graph is callable.
        self.H = frozenset(self.H)
        self.members = self.full_key_members + 3*self.d*self.bits
        self._raw = lru_cache(maxsize=500000)(self._uncached)
        self.calls = self.uses = 0

    def clear_shared(self, t):
        return [p.one(h[0]) for h in self.shared[t]]

    def commit(self, t):
        word = list(super().commit(t))
        if self.policy == 'eager' and hasattr(self, 'shared'):
            word += self.clear_shared(t)
        return tuple(word)

    def initial_cache(self, table):
        return tuple(0 if c is None else self.key(t,c)
                     for t,c in enumerate(table[0]))

    def encode(self, table, status=None, cache=None):
        J = list(super().encode(table, status))
        cache = self.initial_cache(table) if cache is None else tuple(cache)
        if len(cache) != self.d or any(code < 0 or code >= 1 << self.bits for code in cache):
            raise ValueError('Invalid cache fixture')
        for t,code in enumerate(cache):
            J.extend(self.shared[t][b] for b in range(self.bits) if code >> b & 1)
        return m.canon(J)

    def cache_codes(self, J):
        # Verification only: never used in production.
        return tuple(sum(1<<b for b,h in enumerate(row) if h in J) for row in self.shared)

    def strip_shared(self, J):
        return m.canon(h for h in J if h not in self.shared_tags)

    def decode(self, J):
        # Exact verification observer, including permitted stale records.
        cur,refs = [],[]
        for row in self.current:
            found=[c for c in range(self.colors) if row.cell(c) in J]
            ck(len(found)<=1, 'one current key per source')
            cur.append(found[0] if found else None)
        for row in self.refs:
            found=[(t,c) for t in range(self.d) for c in range(self.colors)
                   if row.cell(self.ix(t,c)) in J]
            ck(len(found)<=1, 'one key per reference')
            refs.append(found[0] if found else None)
        table=tuple(cur),tuple(refs)
        status=p.read(J,self.out)
        ck(status in (0,1), 'complete answer')
        cache=self.cache_codes(J)
        for t,c in enumerate(cur):
            if c is not None:
                ck(cache[t]==self.key(t,c), 'present source has exact shared key')
            elif self.policy=='eager':
                ck(cache[t]==0, 'eager absent source has zero shared key')
        ck(J==self.encode(table,status,cache), 'complete matching, exact request snapshots, empty workspace')
        return table,bool(status)

    def run(self, J, op, trace=False):
        if self.policy == 'feedback' and op[0] in ('bind', 'reserve'):
            # Read only the complete result produced by the original operation.
            K, mass, records = self.runword(J, self.base_programs[op], trace)
            answer = self.observe_result(K)
            if op[0] == 'bind':
                suffix = self.bind_copy[op[1],op[2]] if answer else tuple(self.clear_index(op[1]))
            else:
                suffix = self.refresh[op[1]] if answer else ()
            L, wm, more = self.runword(K, suffix, trace)
            if trace:
                offset = len(records)
                more = [dict(item, position=item['position']+offset) for item in more]
            return L, r.serial(mass,wm), records+more
        return super().run(J,op,trace)

    def metrics(self):
        return dict(assertions=CHECKS,policy=self.policy,slots=self.slots,targets=self.d,
                    colors=self.colors,bits=self.bits,members=self.members,
                    candidates=len(self.H),kernel_cache_misses=self.calls,
                    primitive_uses=self.uses)


def expected_cache(C, table, cache, op, after, result):
    out=list(cache)
    if op[0]=='reserve' and (C.policy!='feedback' or result):
        t=op[1]
        out[t]=0 if after[0][t] is None else C.key(t,after[0][t])
    elif C.policy=='eager':
        if op[0]=='release':
            for t,h in enumerate(C.targets):
                if op[1] in h:out[t]=0
        elif op[0]=='execute' and result:
            out[table[1][op[1]][0]]=0
    return tuple(out)


def audit(slots=1, canonical=False, policy='guarded', start=0, stop=None):
    C=Compiler(slots=slots,policy=policy)
    domain=base.domain(C,canonical=canonical)
    stop=len(domain) if stop is None else min(stop,len(domain))
    cases=0;mass=ZERO
    for n in range(start,stop):
        table=domain[n]
        cache=list(C.initial_cache(table))
        if policy in ('guarded','feedback'):
            # Empty rows also cover stale former keys and arbitrary detached bits.
            for t,c in enumerate(table[0]):
                if c is None:cache[t]=((n+1)*(t+3)) % (1<<C.bits)
        J=C.encode(table,(None,0,1)[n%3],cache)
        for op in base.Compiler.alphabet(C):
            after,answer=base.expected(C,table,op)
            want=C.encode(after,answer,expected_cache(C,table,cache,op,after,answer))
            K,wm,_=C.run(J,op)
            ck(K==want, f'full matching {n} {op} {policy}')
            ck(C.decode(K)==(after,answer),'abstract endpoint')
            cases+=1;mass=r.merge(mass,wm)
    return dict(mode='audit',domain_total=len(domain),slice=[start,stop],canonical=canonical,
                operations=cases,CWM=e.cw(mass),**C.metrics())


def costs():
    rows=[]
    old=prior.Compiler(slots=6)
    for policy in ('eager','guarded','feedback'):
        C=Compiler(slots=6,policy=policy)
        bind_rows=[]
        for t in range(C.d):
            cur=[None]*C.d;cur[t]=0;table=(tuple(cur),(None,)*6)
            J=C.encode(table);oldJ=old.encode(table)
            before_uses=C.uses
            K,_,_=C.run(J,('bind',0,t));actual_bind=C.uses-before_uses
            O,_,_=old.run(oldJ,('bind',0,t))
            ck(C.strip_shared(K)==O,'bind has unchanged request/index/status projection')
            ck(C.decode(K)==base.expected(C,table,('bind',0,t)), 'bind exact endpoint')
            total=actual_bind;before=len(old.programs['bind',0,t])
            suffix=(5 if policy=='guarded' else 4)*C.bits
            ck(total==3*C.colors+9+suffix,'bind formula')
            # Full create + six binds + six non-destructive validity reads.
            seq=[('reserve',t)]+[('bind',i,t) for i in range(6)]+[('valid',i) for i in range(6)]
            empty=((None,)*C.d,(None,)*6)
            A=C.encode(empty);B=old.encode(empty);ca=cb=0
            for op in seq:
                pre=C.uses;A,_,_=C.run(A,op);ca+=C.uses-pre
                pre=old.uses;B,_,_=old.run(B,op);cb+=old.uses-pre
                ck(C.strip_shared(A)==B,'lifecycle projection')
            bind_rows.append(dict(target=t,old_bind=before,new_bind=total,
                refresh=len(C.refresh[t]),bind_saving=before-total,
                bind_count_to_amortize=len(C.refresh[t])//(before-total)+1 if before>total else None,
                lifecycle_new=ca,lifecycle_old=cb))
        paths=[]
        for name,cur,q in [('A',(0,None,0),(0,0)),('B',(None,0,None),(1,0)),
                           ('C',(0,None,0),(2,0)),('stale',(1,None,0),(0,0)),('empty',(0,None,0),None)]:
            table=cur,(q,)+(None,)*5;J=C.encode(table)
            K,_,data=C.dispatch(J,0)
            after,value=base.expected(C,table,('execute',0))
            wantcache=expected_cache(C,table,C.initial_cache(table),('execute',0),after,value)
            ck(K==C.encode(after,value,wantcache),'execute complete endpoint')
            expect=8*C.bits+(8 if q else 0)+(2 if value else 0)+(C.bits if value and policy=='eager' else 0)
            ck(data['commands']==expect,'lookup path formula')
            paths.append(dict(name=name,commands=data['commands']))
        rows.append(dict(bind=bind_rows,paths=paths,**C.metrics()))
    return dict(mode='costs',rows=rows,assertions=CHECKS)


def snapshot_trace():
    C=Compiler(slots=6,policy='feedback');table=((None,)*C.d,(None,)*6);J=C.encode(table)
    sequence=[('reserve',0),('reserve',2),('bind',0,0),('copy',1,0),
              ('release',1),('bind',2,0),('reserve',0),('bind',3,0),
              ('same',0,1),('valid',0),('valid',3),('execute',0),('execute',3)]
    ann=base.ref.old.seed(J);protected=None;records=[];mass=e.prep(J)
    for op in sequence:
        cache=C.cache_codes(J);after,answer=base.expected(C,table,op)
        K,wm,log=C.run(J,op,trace=True);mass=r.serial(mass,wm)
        for step in log:
            ann,_,_=base.ref.old.raw_step(ann,step['command'],C.H)
            if protected is not None:ck(ann.names().get(C.targets[2])==protected,'unrelated C birth retained')
        ck(ann.matching==K,'annotated execution agrees with real kernel')
        if op==('reserve',2):protected=ann.names()[C.targets[2]]
        ck(K==C.encode(after,answer,expected_cache(C,table,cache,op,after,answer)),'trace full endpoint')
        records.append(dict(op=op,answer=answer,current=after[0],references=after[1],
                            cache_before=cache,cache_after=C.cache_codes(K),commands=len(log)))
        J,table=K,after
    return dict(mode='snapshot',records=records,CWM=e.cw(mass),**C.metrics())


def stale_domain():
    C=Compiler(slots=2,policy='guarded');cases=0;mass=ZERO
    for t in range(C.d):
        for i in range(C.slots):
            table=((None,)*C.d,tuple((0,0) if j==i else None for j in range(C.slots)))
            for code in range(1<<C.bits):
                cache=[0]*C.d;cache[t]=code
                J=C.encode(table,True,cache)
                K,wm,_=C.run(J,('bind',i,t))
                after,answer=base.expected(C,table,('bind',i,t))
                ck(K==C.encode(after,answer,cache),'every stale absent key is inert in guarded bind')
                cases+=1;mass=r.merge(mass,wm)
    return dict(mode='stale_domain',cases=cases,CWM=e.cw(mass),**C.metrics())


def failures():
    # Legitimately stale cache, but incorrectly remove the binding-presence gate.
    C=Compiler(slots=2,policy='guarded');empty=((None,)*C.d,(None,)*2)
    J=C.encode(empty);history=[]
    def run(op):
        nonlocal J
        J,_,logs=C.run(J,op,True);history.append(dict(op=op,trace=logs))
    run(('reserve',0));run(('release',1))
    ck(C.cache_codes(J)[0]==1,'cache is stale after normal retirement')
    C.H=set(C.H)
    bad=list(C.base_programs['bind',0,0])+C.clear_index(0)
    for b in range(C.bits):bad+=C.emit_write((C.shared[0][b][0],),C.index[0][b])
    C.H=frozenset(C.H);C._raw.cache_clear()
    J,_,logs=C.runword(J,bad,True);history.append(dict(op='bad_unguarded_bind',trace=logs))
    ck(C.refs[0].cell(0) not in J and C.index[0][0] in J,'phantom request directory')
    run(('reserve',0))
    ck(C.targets[0] in J,'new A exists')
    J,_,data=C.dispatch(J,0,True);history.append(dict(op='execute_phantom',trace=data['trace']))
    ck(data['valid'] and C.targets[0] not in J,'bad copy deletes new A despite empty reference')
    # Actual corrected path on the same lifecycle.
    D=Compiler(slots=2,policy='guarded');K=D.encode(empty)
    for op in [('reserve',0),('release',1),('bind',0,0),('reserve',0),('execute',0)]:
        K,_,_=D.run(K,op)
    ck(D.targets[0] in K and not D.observe_result(K),'guarded copy preserves new A')
    # A crash/omission in refresh is a separate invariant-breaking event.
    F=Compiler(slots=2,policy='guarded');table=((None,)*3,((0,0),None))
    A=F.encode(table)
    A,_,_=F.runword(A,F.base_programs['reserve',0])  # deliberately skip materialization
    A,_,_=F.run(A,('bind',1,0))
    ck(F.refs[1].cell(F.ix(0,1)) in A,'binding itself points to new instance')
    A,_,data2=F.dispatch(A,1)
    ck(not data2['valid'] and F.targets[0] in A,'missing cache refresh gives false negative')
    return dict(mode='failures',unguarded_stale_copy=history,
                missing_refresh_false_negative=True,corrected_lifecycle=True,assertions=CHECKS)


def export():
    output={}
    for policy in ('eager','guarded','feedback'):
        C=Compiler(slots=6,policy=policy)
        output[policy]=dict(members=C.members,candidates=sorted(C.H),index=C.index,shared=C.shared,
            fixed_programs={repr(op):w for op,w in C.programs.items()
                            if policy!='feedback' or op[0] not in ('bind','reserve')},
            feedback_cores={repr(op):w for op,w in C.base_programs.items() if op[0] in ('bind','reserve')},
            commits={t:C.commit(t) for t in range(C.d)},
            reads={repr(k):v for k,v in C.reads.items()},
            current_reads={repr(k):v for k,v in C.current_reads.items()},
            refresh=C.refresh,bind_copy={repr(k):v for k,v in C.bind_copy.items()},
            feedback_rule='reserve: refresh only on true; bind: copy on true, clear on false' if policy=='feedback' else None)
    return output


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=('audit','costs','snapshot','stale_domain','failures','export'))
    ap.add_argument('--slots',type=int,default=1);ap.add_argument('--policy',default='guarded')
    ap.add_argument('--canonical',action='store_true');ap.add_argument('--start',type=int,default=0);ap.add_argument('--stop',type=int)
    ap.add_argument('--out');args=ap.parse_args()
    if args.mode=='audit':out=audit(args.slots,args.canonical,args.policy,args.start,args.stop)
    elif args.mode=='snapshot':out=snapshot_trace()
    else:out=globals()[args.mode]()
    text=json.dumps(out,ensure_ascii=False,indent=2)+'\n'
    if args.out:Path(args.out).write_text(text)
    else:print(text)
