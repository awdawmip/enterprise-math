"""Exact minimax planning with a fixed schedule of (target, bind destination).

Runtime interface: value(ordered masks/values, position) and action(...).
No exact old residue table is accepted by either planner.  Reading one actual bit
costs 8 original commands. Fixed business words are charged by the BRC harness.
The replay and static-witness routines below the planners are verification only.
"""
from __future__ import annotations

from functools import lru_cache
from math import comb


def key_weight(key, width):
    return 2 * key.bit_count() + 4 * (1 - ((key >> (width - 1)) & 1))


def set_observation(state, slot, bit, answer):
    mask, value = state[slot]
    flag = 1 << bit
    if answer not in (0, 1) or mask & flag:
        raise ValueError("Expected a fresh bit and a Boolean answer")
    return state[:slot] + ((mask | flag, value | (answer << bit)),) + state[slot + 1:]


def replace_known(state, slot, residue, width):
    return state[:slot] + (((1 << width) - 1, residue),) + state[slot + 1:]


class _Schedule:
    def __init__(self, slots, rounds=None, *, schedule=None):
        if rounds is not None and schedule is not None:
            raise ValueError("Supply rounds or schedule, not both")
        seq = tuple(tuple(x) for x in (rounds if rounds is not None else schedule))
        if type(slots) is not int or slots < 1 or any(
            len(x) != 2 or type(x[0]) is not int or type(x[1]) is not int
            or x[0] < 0 or not 0 <= x[1] < slots for x in seq
        ):
            raise ValueError("Expected positive slot count and valid (target,destination) pairs")
        self.slots, self.rounds, self.schedule = slots, seq, seq
        self.targets = tuple(t for t, d in seq)
        self.destinations = tuple(d for t, d in seq)
        self.colors = slots + 1
        self.width = slots.bit_length()
        self.modulus = 1 << self.width
        self.full = self.modulus - 1
        self.keys = tuple(tuple(range(1 + t * self.colors, 1 + (t + 1) * self.colors))
                          for t in self.targets)

    def _input(self, knowledge, position, terminal=True):
        if (type(position) is not int or position < 0 or position > len(self.rounds)
                or (not terminal and position == len(self.rounds))
                or len(knowledge) != self.slots):
            raise ValueError("Knowledge length or schedule position mismatch")
        state = tuple(tuple(p) for p in knowledge)
        if any(len(p) != 2 or not all(type(x) is int for x in p)
               or not 0 <= p[0] <= self.full or not 0 <= p[1] <= self.full or p[1] & ~p[0]
               for p in state):
            raise ValueError("Invalid observed mask/value pair")
        return state


class LabelledSchedulePlanner(_Schedule):
    """Independent reference recurrence in physical slot order and mask/value pairs."""
    def __init__(self, slots, rounds=None, *, schedule=None):
        super().__init__(slots, rounds, schedule=schedule)
        self.decisions = {}
        self.query_options = self.create_options = 0
        self.evaluate = lru_cache(maxsize=None)(self._evaluate)

    def _evaluate(self, state, position):
        if position == len(self.rounds):
            return 0
        best = None
        action = None
        for key in self.keys[position]:
            rho = key % self.modulus
            if any((rho & mask) == value for mask, value in state):
                continue
            self.create_options += 1
            next_state = replace_known(state, self.destinations[position], rho, self.width)
            candidate = key_weight(key, self.width) + self.evaluate(next_state, position + 1)
            if best is None or candidate < best:
                best, action = candidate, ('create', key)
        for bit in reversed(range(self.width)):
            for slot, (mask, _) in enumerate(state):
                if mask & (1 << bit):
                    continue
                self.query_options += 1
                candidate = 8 + max(self.evaluate(set_observation(state, slot, bit, a), position)
                                    for a in (0, 1))
                if best is None or candidate < best:
                    best, action = candidate, ('read', slot, bit)
        assert best is not None
        self.decisions[state, position] = action
        return best

    def value(self, knowledge, position):
        return self.evaluate(self._input(knowledge, position), position)

    def action(self, knowledge, position):
        state = self._input(knowledge, position, False)
        self.evaluate(state, position)
        return self.decisions[state, position]

    def metrics(self):
        n = self.evaluate.cache_info()
        return dict(states=n.currsize, nonterminal_states=len(self.decisions),
                    terminal_states=n.currsize-len(self.decisions),
                    cache_hits=n.hits, query_actions=self.query_options,
                    creation_actions=self.create_options)


class SchedulePlanner(_Schedule):
    """Exact orbit cache; slots in remaining effective write set retain their addresses.

    At each position the tuple starts with the distinguished physical slots in
    increasing order; the remaining entries are a sorted multiset of ternary
    observation codes. Identical anonymous patterns offer one possible query
    per unread bit. An answer updates exactly one copy of its pattern.
    """
    def __init__(self, slots, rounds=None, *, schedule=None):
        super().__init__(slots, rounds, schedule=schedule)
        self.named = tuple(tuple(sorted(set(self.destinations[i:-1])))
                           for i in range(len(self.rounds)))
        self.anonymous = tuple(tuple(s for s in range(slots) if s not in named)
                               for named in self.named)
        self.powers = tuple(3 ** b for b in range(self.width))
        self.pattern_count = 3 ** self.width
        self.encode = {}
        self.unknown = []
        self.compat_domain = []
        self.full_code = {}
        for code in range(self.pattern_count):
            mask = value = 0
            for bit, power in enumerate(self.powers):
                digit = (code // power) % 3
                mask |= (digit != 0) << bit
                value |= (digit == 2) << bit
            self.encode[mask, value] = code
            self.unknown.append(tuple(bit for bit in reversed(range(self.width))
                                      if not (mask & (1 << bit))))
            self.compat_domain.append(sum(1 << z for z in range(self.modulus)
                                          if (z & mask) == value))
            if mask == self.full:
                self.full_code[value] = code
        self._keys_with_cost = tuple(tuple((k, k % self.modulus, key_weight(k, self.width))
                                           for k in kk) for kk in self.keys)
        # An anonymous index can never become named in a later suffix.
        self.transfer = []
        for i, named in enumerate(self.named[:-1]):
            next_named = self.named[i+1]
            dest_index = named.index(self.destinations[i])
            keep = tuple(named.index(s) for s in next_named)
            retire = tuple(j for j,s in enumerate(named) if s not in next_named)
            self.transfer.append((dest_index, keep, retire))
        self.cache = [{} for _ in self.rounds]
        self.query_options = self.create_options = self.cache_hits = 0

    def _canonical(self, state, i):
        codes = tuple(self.encode[p] for p in state)
        return tuple(codes[j] for j in self.named[i]) + tuple(
            sorted(codes[j] for j in self.anonymous[i]))

    @staticmethod
    def _insert_refinement(state, index, new, d):
        if index < d:
            return state[:index] + (new,) + state[index+1:]
        return state[:d] + tuple(sorted(state[d:index] + (new,) + state[index+1:]))

    def _after_write(self, state, i, rho):
        dest, keep, retire = self.transfer[i]
        named = state[:len(self.named[i])]
        named = named[:dest] + (self.full_code[rho],) + named[dest+1:]
        return tuple(named[j] for j in keep) + tuple(
            sorted(state[len(named):] + tuple(named[j] for j in retire)))

    def _solve(self, state, i):
        cache = self.cache[i]
        hit = cache.get(state)
        if hit is not None:
            self.cache_hits += 1
            return hit[0]
        d = len(self.named[i])
        covered = 0
        for code in state:
            covered |= self.compat_domain[code]
        best = None
        action = None
        for key, rho, fee in self._keys_with_cost[i]:
            if covered & (1 << rho):
                continue
            self.create_options += 1
            candidate = fee if i+1 == len(self.rounds) else (
                fee + self._solve(self._after_write(state, i, rho), i+1))
            if best is None or candidate < best:
                best, action = candidate, ('create', key)
        # These final-round cuts use a proved lower bound of one additional
        # read plus the globally cheapest legal key. They never apply earlier.
        if i+1 == len(self.rounds) and best is not None and best <= 8+min(
                w for _, _, w in self._keys_with_cost[i]):
            cache[state] = best, action
            return best
        for index, code in enumerate(state):
            if index > d and state[index-1] == code:
                continue
            for bit in self.unknown[code]:
                self.query_options += 1
                power = self.powers[bit]
                left = self._solve(self._insert_refinement(state,index,code+power,d),i)
                if best is not None and 8 + left >= best:
                    continue
                right = self._solve(self._insert_refinement(state,index,code+2*power,d),i)
                candidate = 8 + max(left,right)
                if best is None or candidate < best:
                    best = candidate
                    action = ('named', self.named[i][index],bit) if index < d else (
                        'anonymous',code,bit)
        assert best is not None
        cache[state] = best, action
        return best

    def value(self, knowledge, position):
        state = self._input(knowledge, position)
        if position == len(self.rounds):
            return 0
        return self._solve(self._canonical(state, position), position)

    def action(self, knowledge, position):
        state = self._input(knowledge, position, False)
        canon = self._canonical(state, position)
        self._solve(canon, position)
        a = self.cache[position][canon][1]
        if a[0] == 'create':
            return a
        if a[0] == 'named':
            return 'read', a[1],a[2]
        # Physical indices still exist at the execution boundary.
        physical = next(j for j in self.anonymous[position] if self.encode[state[j]]==a[1])
        return 'read', physical, a[2]

    def metrics(self):
        P = self.pattern_count
        return dict(nonterminal_states=sum(map(len,self.cache)),
                    states_by_position=[len(c) for c in self.cache],
                    named_at_positions=self.named,
                    orbit_capacity_by_position=[P**len(d)*comb(P+self.slots-len(d)-1,
                                                self.slots-len(d)) for d in self.named],
                    cache_hits=self.cache_hits, query_actions=self.query_options,
                    creation_actions=self.create_options)


def schedule_replay(planner, initial_residues, initial_knowledge=None):
    """Verification oracle: actual truth feeds one queried bit and checks safety."""
    residues = list(initial_residues)
    state = tuple(initial_knowledge) if initial_knowledge is not None else ((0,0),)*planner.slots
    if len(residues)!=planner.slots or any(not 0 <= z < planner.modulus or z&m !=v
                                          for z,(m,v) in zip(residues,state)):
        raise ValueError('Non-realizable physical residue table')
    pos = cost = queries = 0
    events=[]
    while pos<len(planner.rounds):
        action = planner.action(state,pos)
        if action[0]=='read':
            _,slot,bit=action
            answer=residues[slot]>>bit & 1
            state=set_observation(state,slot,bit,answer)
            queries+=1;cost+=8
            events.append(dict(kind='read',round=pos,slot=slot,bit=bit,answer=answer))
        else:
            _,key=action
            assert key in planner.keys[pos]
            rho=key%planner.modulus
            assert all(rho&m !=v for m,v in state) and rho not in residues
            dest=planner.destinations[pos];w=key_weight(key,planner.width)
            state=replace_known(state,dest,rho,planner.width)
            residues[dest]=rho;cost+=w
            events.append(dict(kind='create',round=pos,target=planner.targets[pos],
                               destination=dest,key=key,key_weight=w))
            pos+=1
    return dict(cost=cost,vacancy_bit_reads=queries,events=events,
                final_knowledge=state,final_residues=residues)


def worst_static_witness(planner, initial_knowledge=None):
    """Lift an attaining adversarial path back to one static initial residue table."""
    initial = tuple(initial_knowledge) if initial_knowledge is not None else ((0,0),)*planner.slots
    state = initial
    constraints = list(initial)
    live=[True]*planner.slots
    pos=0
    while pos<len(planner.rounds):
        action=planner.action(state,pos)
        if action[0]=='read':
            _,slot,bit=action
            branches=[set_observation(state,slot,bit,a) for a in (0,1)]
            values=[planner.value(s,pos) for s in branches]
            answer=int(values[1]>values[0])
            assert live[slot]
            state=branches[answer]
            constraints[slot]=state[slot]
        else:
            _,key=action
            dest=planner.destinations[pos]
            state=replace_known(state,dest,key%planner.modulus,planner.width)
            live[dest]=False
            pos+=1
    residues=tuple(v for m,v in constraints)
    out=schedule_replay(planner,residues,initial)
    assert out['cost']==planner.value(initial,0)
    return dict(initial_residues=residues,initial_constraints=constraints,**out)


class LifetimePlanner(_Schedule):
    """Exact cost game using expiration-tagged unknowns and last known blockers.

    A currently stored value blocks through its first remaining prescribed write,
    including that round's creation.  A write at the last round has no observable
    successor, so expiry T stands for survival through the horizon. Fully known
    equal residues need only their latest expiry. Exact physical slots are used
    when lifting an abstract read to the original executor.
    """
    def __init__(self, slots, rounds=None, *, schedule=None):
        super().__init__(slots, rounds, schedule=schedule)
        T=len(self.rounds)
        expiry=[T]*slots
        self.lifetimes=[None]*T
        self.new_life=[None]*T
        for i in reversed(range(T)):
            dest=self.destinations[i]
            self.new_life[i]=expiry[dest]
            if i<T-1:
                expiry[dest]=i
            self.lifetimes[i]=tuple(expiry)
        # Compile predicate domains separately from the cache representation.
        self.domains={}
        self.fresh={}
        for mask in range(self.modulus):
            for v in range(self.modulus):
                if v & ~mask: continue
                self.domains[mask,v]=sum(1<<r for r in range(self.modulus) if r & mask==v)
                self.fresh[mask,v]=tuple(j for j in reversed(range(self.width))
                                        if not mask & (1<<j))
        self.compiled_keys=tuple(tuple((k,k%self.modulus,key_weight(k,self.width)) for k in kk)
                                 for kk in self.keys)
        self.cache=[{} for _ in self.rounds]
        self.query_options=self.create_options=self.cache_hits=0

    def _represent(self, state, position):
        unknown=[]
        latest=[-1]*self.modulus
        for p,expiry in zip(state,self.lifetimes[position]):
            m,v=p
            if m==self.full: latest[v]=max(latest[v],expiry)
            else: unknown.append((expiry,m,v))
        return tuple(sorted(unknown)),tuple(latest)

    def certificate(self, knowledge, position):
        return self._represent(self._input(knowledge,position,False),position)

    def _refine(self, U, L, index, bit, answer):
        expiry,mask,value=U[index]
        flag=1<<bit
        nm,nv=mask|flag,value|(answer<<bit)
        if nm==self.full:
            L=L[:nv]+(max(L[nv],expiry),)+L[nv+1:]
            return U[:index]+U[index+1:],L
        return tuple(sorted(U[:index]+((expiry,nm,nv),)+U[index+1:])),L

    def _write(self, U, L, i, z):
        remaining=tuple(u for u in U if u[0]>i)
        new_life=self.new_life[i]
        next_L=tuple(max(old if old>i else -1,new_life if k==z else -1)
                     for k,old in enumerate(L))
        return remaining,next_L

    def _solve(self,U,L,i):
        cache=self.cache[i]
        state=U,L
        hit=cache.get(state)
        if hit is not None:
            self.cache_hits+=1
            return hit[0]
        occupied=sum(1<<z for z,e in enumerate(L) if e>=i)
        for expiry,m,v in U:
            occupied|=self.domains[m,v]
        best=None;action=None
        for k,z,w in self.compiled_keys[i]:
            if occupied & (1<<z):continue
            self.create_options+=1
            candidate=w
            if i+1<len(self.rounds):
                uu,ll=self._write(U,L,i,z)
                candidate+=self._solve(uu,ll,i+1)
            if best is None or candidate<best:
                best,action=candidate,('create',k)
        if i+1==len(self.rounds) and best is not None and best<=8+min(
                w for _,_,w in self.compiled_keys[i]):
            cache[state]=best,action
            return best
        for index,(e,m,v) in enumerate(U):
            if index and U[index]==U[index-1]:continue
            for bit in self.fresh[m,v]:
                self.query_options+=1
                uu,ll=self._refine(U,L,index,bit,0)
                left=self._solve(uu,ll,i)
                if best is not None and 8+left>=best:continue
                uu,ll=self._refine(U,L,index,bit,1)
                right=self._solve(uu,ll,i)
                candidate=8+max(left,right)
                if best is None or candidate<best:
                    best,action=candidate,('refine',e,m,v,bit)
        assert best is not None
        cache[state]=best,action
        return best

    def value(self, knowledge, position):
        state=self._input(knowledge,position)
        if position==len(self.rounds):return 0
        return self._solve(*self._represent(state,position),position)

    def action(self,knowledge,position):
        state=self._input(knowledge,position,False)
        u,l=self._represent(state,position)
        self._solve(u,l,position)
        a=self.cache[position][u,l][1]
        if a[0]=='create':return a
        _,e,m,v,bit=a
        slot=next(j for j,(p,ej) in enumerate(zip(state,self.lifetimes[position]))
                  if p==(m,v) and e==ej)
        return 'read',slot,bit

    def metrics(self):
        return dict(nonterminal_states=sum(map(len,self.cache)),
                    states_by_position=[len(c) for c in self.cache],
                    expiry_by_position=self.lifetimes,
                    cache_hits=self.cache_hits,query_actions=self.query_options,
                    creation_actions=self.create_options)


def lifetime_capacity(width, named, anonymous):
    """Number of different expiration certificates for unrestricted partial patterns.

    This is the image size, not a prediction of reachable states at a fixed suffix
    after prior business writes. For a derivation see lifetime_proof.md.
    """
    from math import perm
    if width<1 or min(named,anonymous)<0:
        raise ValueError("Expected positive width and nonnegative slot counts")
    B=1<<width
    partial=3**width-B
    total=0
    for finite_known in range(named+1):
        f=finite_known
        choices_finite_unknown=comb(named,f)*partial**(named-f)
        for anonymous_known in range(anonymous+1):
            k=anonymous_known
            choices_anon_unknown=comb(partial+anonymous-k-1,anonymous-k)
            for s in ([0] if k==0 else range(1,min(B,k)+1)):
                if f==0:
                    finite_latest=1
                elif s:
                    finite_latest=sum(comb(f,j)*perm(B-s,j) for j in range(min(f,B-s)+1))
                else:
                    finite_latest=sum(comb(f-1,j-1)*perm(B,j) for j in range(1,min(f,B)+1))
                total+=choices_finite_unknown*choices_anon_unknown*comb(B,s)*finite_latest
    return total
