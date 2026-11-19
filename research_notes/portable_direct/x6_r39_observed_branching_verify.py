#!/usr/bin/env python3
"""R39 exact finite observer-trace checker (ordinary Boolean automata; not physical BRC)."""
from collections import deque
from itertools import product
import json

ALPHABET = tuple(product((0, 1), (0, 1)))  # event, observed destination bit

def step(trans, obs, subset, symbol):
    event, observed = symbol
    result = 0
    for source in range(len(obs)):
        if subset & (1 << source):
            result |= trans[source * 2 + event]
    return result & sum((1 << j) for j, value in enumerate(obs) if value == observed)

def witness(machine_a, initial_a, machine_b, initial_b):
    trans_a, obs_a = machine_a
    trans_b, obs_b = machine_b
    if obs_a[initial_a] != obs_b[initial_b]:
        return ()  # empty observation is already a witness
    start = (1 << initial_a, 1 << initial_b)
    frontier = deque([(start, ())])
    visited = {start}
    while frontier:
        (left, right), word = frontier.popleft()
        for symbol in ALPHABET:
            lnext = step(trans_a, obs_a, left, symbol)
            rnext = step(trans_b, obs_b, right, symbol)
            if bool(lnext) != bool(rnext):
                return word + (symbol,)
            pair = (lnext, rnext)
            if lnext and pair not in visited:
                visited.add(pair)
                frontier.append((pair, word + (symbol,)))
    return None

def reachable_subsets(machine, initial):
    trans, obs = machine
    seen = {1 << initial}
    queue = deque(seen)
    while queue:
        s = queue.popleft()
        for symbol in ALPHABET:
            t = step(trans, obs, s, symbol)
            if t and t not in seen:
                seen.add(t)
                queue.append(t)
    return seen

def all_words(length):
    return product(ALPHABET, repeat=length)

def accepts(machine, initial, word):
    trans, obs = machine
    subset = 1 << initial
    for symbol in word:
        subset = step(trans, obs, subset, symbol)
        if not subset:
            return False
    return True

def brute_first_difference(ma, a, mb, b, cutoff):
    if ma[1][a] != mb[1][b]:
        return ()
    for length in range(1, cutoff+1):
        for word in all_words(length):
            if accepts(ma, a, word) != accepts(mb, b, word):
                return word
    return None

def bisimilar(machine, p, q):
    trans, obs = machine
    n = len(obs)
    pairs = {(a,b) for a in range(n) for b in range(n) if obs[a] == obs[b]}
    changed = True
    while changed:
        changed = False
        keep = set()
        for a,b in pairs:
            good = True
            for symbol in ALPHABET:
                a_succ = step(trans,obs,1<<a,symbol)
                b_succ = step(trans,obs,1<<b,symbol)
                AA = [i for i in range(n) if a_succ & (1<<i)]
                BB = [i for i in range(n) if b_succ & (1<<i)]
                if any(not any((u,v) in pairs for v in BB) for u in AA) or any(not any((u,v) in pairs for u in AA) for v in BB):
                    good = False
                    break
            if good:
                keep.add((a,b))
        if keep != pairs:
            changed = True
            pairs = keep
    return (p,q) in pairs


def run():
    machines = []
    for trans in product(range(4), repeat=4):
        for obs in product((0,1), repeat=2):
            machines.append((trans, obs))
    stats = {"machines":len(machines),"same_machine_pairs":0,"equal_language_pairs":0,"shortest_difference_depths":{},"maximum_cutoff":0,"cross_machine_pairs":0,"cross_shortest_difference_depths":{},"cross_long_witness":None}
    for machine in machines:
        for a in range(2):
            for b in range(2):
                stats['same_machine_pairs'] += 1
                cutoff = len(reachable_subsets(machine, a)) + len(reachable_subsets(machine,b))-1
                stats['maximum_cutoff'] = max(stats['maximum_cutoff'], cutoff)
                actual = witness(machine,a,machine,b)
                brute = brute_first_difference(machine,a,machine,b,cutoff)
                assert actual == brute, (machine,a,b,cutoff,actual,brute)
                if actual is None:
                    stats['equal_language_pairs'] += 1
                else:
                    d = str(len(actual))
                    stats['shortest_difference_depths'][d] = stats['shortest_difference_depths'].get(d,0)+1
                    assert len(actual) <= cutoff
    # Independent cross-machine checks sample a deterministic exhaustive stride across a 1,024-by-1,024 universe.
    for ix in range(0,len(machines),17):
        for jx in range(3,len(machines),29):
            ma,mb=machines[ix],machines[jx]
            a,b=ix%2,jx%2
            cutoff = len(reachable_subsets(ma,a))+len(reachable_subsets(mb,b))-1
            actual=witness(ma,a,mb,b)
            brute=brute_first_difference(ma,a,mb,b,cutoff)
            assert actual == brute, (ix,jx,cutoff,actual,brute)
            if actual is not None:
                d=str(len(actual))
                stats['cross_shortest_difference_depths'][d]=stats['cross_shortest_difference_depths'].get(d,0)+1
                if len(actual)>=3 and stats['cross_long_witness'] is None:
                    stats['cross_long_witness']={"machine_a":{"transitions":list(ma[0]),"readouts":list(ma[1]),"initial":a},"machine_b":{"transitions":list(mb[0]),"readouts":list(mb[1]),"initial":b},"word":[list(pair) for pair in actual],"depth":len(actual),"cutoff":cutoff}
            stats['cross_machine_pairs'] += 1
    # Pure branching example, five states p,q,u,v,z and one terminal t: use n=6.
    # States 0=p,1=q,2=u,3=v,4=z,5=t; event 0=a, event 1=b; event 2=c requires generalized alphabet.
    # This example is checked separately using an explicit 3-event observer-constant graph.
    transitions={
        0:{'a':{2,3}},
        1:{'a':{4}},
        2:{'b':{5}},
        3:{'c':{5}},
        4:{'b':{5},'c':{5}},
        5:{}
    }
    def language(s):
        out={()}
        current={(s,())}
        for _ in range(3):
            nxt=set()
            for state,word in current:
                for e,targets in transitions[state].items():
                    for v in targets:
                        nw=word+(e,)
                        out.add(nw)
                        nxt.add((v,nw))
            current=nxt
        return sorted(out)
    assert language(0)==language(1)
    # Compute greatest strong bisimulation as the repeated back-and-forth elimination relation.
    pairs={(i,j) for i in transitions for j in transitions}
    while True:
        revised=set()
        for i,j in pairs:
            compatible=True
            for e in ('a','b','c'):
                aa=transitions[i].get(e,set())
                bb=transitions[j].get(e,set())
                if any(not any((u,v) in pairs for v in bb) for u in aa) or any(not any((u,v) in pairs for u in aa) for v in bb):
                    compatible=False
                    break
            if compatible: revised.add((i,j))
        if revised == pairs: break
        pairs=revised
    assert (0,1) not in pairs
    assert language(0)==[(),('a',),('a','b'),('a','c')]
    stats['branch_counterexample']={"p_language":[list(t) for t in language(0)],"q_language":[list(t) for t in language(1)],"strong_bisimulation":False,"graph_state_count":6}
    stats['model']={"states":"2, with destination readout 0/1","event_labels":2,"exact_observed_symbols":4,"subset_support":"existential Boolean","finite_test":"all 1,024 two-state machines; all 4 ordered pairs per machine; 2,196 deterministically selected cross-machine pairs"}
    stats['result']='PASS'
    return stats

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True,ensure_ascii=False))
