#!/usr/bin/env python3
"""Exact R672 S3 finite automaton verification; standard library only."""
from collections import deque, Counter
import json

SIGMA = 'ABC'
UNIT = (0,1,2)
TRANSPOSITIONS = {'A': (0,2,1), 'B': (2,1,0), 'C': (1,0,2)}

def product(g, h):
    return tuple(g[h[i]] for i in range(3))

def allowed(q):
    return ''.join(a for a in SIGMA if a not in q)

def step(s, x):
    h, q = s
    assert x in allowed(q)
    return (product(h, TRANSPOSITIONS[x]), (q+x)[-2:])

def reachable():
    initial = (UNIT, '')
    words = {initial: ''}
    queue = deque([initial])
    while queue:
        s = queue.popleft()
        for x in allowed(s[1]):
            nxt = step(s, x)
            if nxt not in words:
                words[nxt] = words[s] + x
                queue.append(nxt)
    return words

def recolor(states, sig):
    colors, out = {}, {}
    for state in states:
        if sig[state] not in colors:
            colors[sig[state]] = len(colors)
        out[state] = colors[sig[state]]
    return out

def moore(states):
    states = tuple(states)
    old = recolor(states, {s:s[0] for s in states})
    while True:
        signatures = {}
        for s in states:
            signatures[s] = (s[0], tuple(
                (x,old[step(s,x)]) if x in allowed(s[1]) else (x,None)
                for x in SIGMA))
        new = recolor(states, signatures)
        if all((old[s] == old[t]) == (new[s] == new[t])
               for s in states for t in states):
            return len(set(new.values()))
        old = new

def legal(q, word):
    for x in word:
        if x not in allowed(q):
            return False
        q = (q+x)[-2:]
    return True

def run():
    words = reachable()
    control = {q for _,q in words}
    probes = ('',) + tuple(SIGMA) + tuple(a+b for a in SIGMA for b in SIGMA)
    language_separated = all(
        any(legal(p,w) != legal(q,w) for w in probes)
        for p in control for q in control if p != q)
    counts = Counter(q for _,q in words)
    assert len(control) == 10 and len(words) == 40 and language_separated
    assert counts[''] == 1 and all(counts[q] == 1 for q in SIGMA)
    assert all(counts[q] == 6 for q in ('AB','AC','BA','BC','CA','CB'))
    assert moore(words) == 40

    def state(word):
        s = (UNIT, '')
        for x in word:
            s = step(s, x)
        return s
    assert state('AB')[0] == state('ACBA')[0] == (1,2,0)
    assert allowed(state('AB')[1]) == allowed(state('ACBA')[1]) == 'C'
    assert legal(state('AB')[1], 'CA')
    assert not legal(state('ACBA')[1], 'CA')
    ab = {str(h):w for (h,q),w in words.items() if q == 'AB'}
    assert len(ab) == 6

    data = {
      'schema':'R672_SECOND_ORDER_S3_MINIMAL_FUTURE_MACHINE_V1',
      'model':'V17 three 012-return blocks A,B,C with distinct S3 transpositions; auxiliary scheduler forbids either of two preceding block labels',
      'group_action':'right multiplication of full S3 slot permutations',
      'reachable_raw_states':len(words),
      'scheduler_control_states':len(control),
      'states_by_control_suffix':dict(sorted(counts.items())),
      'minimal_future_states':moore(words),
      'max_shortest_witness_length':max(map(len,words.values())),
      'AB_six_group_witnesses':ab,
      'two_step_language_separates_all_ten_control_states':language_separated,
      'counterexample':{
        'word1':'AB','word2':'ACBA','same_h':[1,2,0],
        'same_next_allowed':'C','future_suffix':'CA',
        'legal_after_word1':True,'legal_after_word2':False},
      'independent_moore_minimization_matches_proof':True,
      'pass':True
    }
    print(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))

if __name__ == '__main__':
    run()
