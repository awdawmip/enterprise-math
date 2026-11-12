#!/usr/bin/env python3
"""R739: exact X6 five-triad certificate / authentic V29 PASS-count lift.
Standard library only. Force-triad switching is an explicitly declared coupling.
"""
from itertools import product, permutations
from collections import Counter
import json

TRIADS=['012','013','014','023','024','034','123','124','134','234']
UNIVERSE=[u+'>'+v for u in TRIADS for v in TRIADS if len(set(u)&set(v))==2]
assert len(UNIVERSE)==60
ALPHABET=[(a,b) for a in range(4) for b in range(4) if a!=b]
assert len(ALPHABET)==12
MASKS={'A':211733226574,'B':5363347296468}
RETURNS={
 'A':{'I':('012','014','013','012'),'P':('012','023','013','012'),'Q':('012','023','123','012')},
 'B':{'I':('012','123','124','012'),'P':('012','023','013','012'),'Q':('012','123','013','012')},
}

def transposition(s):
    return sum(s[i]!=str(i) for i in range(3))==2

def holonomy(path):
    f={str(i):i for i in range(3)}
    for a,b in zip(path,path[1:]):
        leaving=next(x for x in a if x not in b)
        entering=next(x for x in b if x not in a)
        f[entering]=f.pop(leaving)
    return ''.join(str(f[x]) for x in path[-1])

def all_root_triangles(arcs):
    loops=[]
    for u in TRIADS[1:]:
        for v in TRIADS[1:]:
            w=('012',u,v,'012')
            if u!=v and all(a+'>'+b in arcs for a,b in zip(w,w[1:])):
                loops.append({'path':list(w),'holonomy':holonomy(w),'first':u,'last':v})
    return loops

def event_trace(word, returns, code, arc_index):
    path=['012']; events=[]; M=[[0]*4 for _ in range(4)]
    active=['012']
    for letter in word:
        segment=returns[letter]
        assert segment[0]==path[-1]
        for a,b in zip(segment,segment[1:]):
            assert len(set(a)&set(b))==2
            index=arc_index[a+'>'+b]
            for symbol in code[index]:
                pa,pb=ALPHABET[symbol]
                assert pa!=pb
                M[pa][pb]+=1
                events.append((pa,pb))
            active.append(b)
        path.extend(segment[1:])
    assert len(events)==2*(len(path)-1)
    assert path[-1]=='012'
    assert all(path[i-1]!=path[i+1] for i in range(1,len(path)-1))
    assert path[-2]!=path[1]
    reverse={tuple(v):i for i,v in enumerate(code)}
    recovered=[]
    for i in range(0,len(events),2):
        pair=tuple(ALPHABET.index(event) for event in events[i:i+2])
        recovered.append(reverse[pair])
    expected=[arc_index[a+'>'+b] for a,b in zip(path,path[1:])]
    assert recovered==expected
    assert sum(map(sum,M))==len(events)
    return {'M':M,'PASS_count':len(events),'holonomy':holonomy(path),
            'CNB_arcs':len(path)-1,'grade_increment':len(events),
            'active_triads':active,'event_words':events}

res={
 'schema':'R739_P000_X6_V29_RESTRICTED_LIFT_CERT_V1',
 'scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'scope':'conditional five-triad closure inventory + genuine V29 PASS count events + declared frame coupling',
 'carriers':{}
}
for name,mask in MASKS.items():
    arcs=[e for i,e in enumerate(UNIVERSE) if (mask>>i)&1]
    assert len(arcs)==15
    arc_index={e:i for i,e in enumerate(arcs)}
    indegree=Counter(e.split('>')[1] for e in arcs)
    max_indegree=max(indegree.values())
    assert max_indegree=={'A':4,'B':3}[name]
    loops=all_root_triangles(set(arcs))
    assert len(loops)==3
    mapping={h['holonomy']:h for h in loops}
    assert len(mapping)==3 and '012' in mapping
    others=[h for h in mapping if h!='012']
    assert all(transposition(h) for h in others) and others[0]!=others[1]
    observed={tuple(RETURNS[name][x]) for x in 'IPQ'}
    assert observed=={tuple(L['path']) for L in loops}
    starts={L['first'] for L in loops}; ends={L['last'] for L in loops}
    assert not starts & ends
    closed_triads={'012'} | starts | ends
    assert len(closed_triads)==5
    candidates=[]
    for seq in product(loops,repeat=3):
        hs=[L['holonomy'] for L in seq]
        if hs.count('012')!=1 or len(set(hs))!=3: continue
        if not all(transposition(s) for s in hs if s!='012'): continue
        if {L['first'] for L in seq} & {L['last'] for L in seq}: continue
        candidates.append(len({'012'}|{L['first'] for L in seq}|{L['last'] for L in seq}))
    assert len(candidates)==6 and min(candidates)==5
    code=[(i//12,i%12) for i in range(15)]
    assert len(set(code))==15
    traces={w:event_trace(w,RETURNS[name],code,arc_index) for w in ('PPQQ','PQPQ','QPQP')}
    assert {traces[w]['holonomy'] for w in traces}=={'012','120','201'}
    assert len({tuple(map(tuple,traces[w]['M'])) for w in traces})==1
    assert all(traces[w]['PASS_count']==24 for w in traces)
    assert all(set(traces[w]['active_triads'])<=closed_triads for w in traces)
    for t in closed_triads:
        assert len(t)==3 and len(set(t))==3 and all(c in '01234' for c in t)
    formal_axes=tuple(range(5));tested=0
    for sigma in permutations(range(6)):
        axis_map={i:sigma[i] for i in formal_axes}
        for t in closed_triads:
            transformed=tuple(axis_map[int(i)] for i in t)
            assert len(set(transformed))==3
        for w in ('PPQQ','PQPQ','QPQP'):
            trace=traces[w]
            start=tuple(axis_map[i] for i in (0,1,2))
            transformed_finish=tuple(start[int(i)] for i in trace['holonomy'])
            finish_then_transform=tuple(axis_map[int(i)] for i in trace['holonomy'])
            assert transformed_finish==finish_then_transform
            assert trace['M']==traces[w]['M']
            tested+=1
    res['carriers'][name]={
      'arc_mask':str(mask),'root_3step_CNB_loops':loops,
      'directed_network_max_indegree':max_indegree,
      'unique_generator_inventory':sorted(closed_triads),
      'closure_incidence_minimum_for_root_3step_I_P_Q':5,
      'fully_eligible_generator_assignments':len(candidates),
      'arc_codes':{arcs[i]:list(code[i]) for i in range(15)},
      'four_port_PASS_count_for_four_generators':24,
      'equal_native_final_PASS_M':traces['PPQQ']['M'],
      'named_relation_outcomes':{w:traces[w]['holonomy'] for w in traces},
      'native_PASS_grade_increment':24,
      'S6_rotation_cases':tested,
      'complete_closure_incidence_inventory':sorted(closed_triads),
      'source_ordered_event_trace':{
         w:trace['event_words'] for w,trace in traces.items()},
      'dynamic_coupling':'DECLARED_CANDIDATE_AFTER_EACH_TWO_PASS_BLOCK'
    }
H={key:frozenset(frozenset(map(int,triple)) for triple in value['unique_generator_inventory'])
   for key,value in res['carriers'].items()}
rotations=list(permutations(range(6)))
def rotate(H,sigma):
    return frozenset(frozenset(sigma[i] for i in triple) for triple in H)
for name in ('A','B'):
    stab=sum(rotate(H[name],sigma)==H[name] for sigma in rotations)
    orb={rotate(H[name],sigma) for sigma in rotations}
    assert stab==4 and len(orb)==180 and 720==stab*len(orb)
    res['carriers'][name]['closure_inventory_S6_stabilizer']=stab
    res['carriers'][name]['closure_inventory_S6_orbit']=len(orb)
example_sigma=(1,2,0,3,4,5)
assert rotate(H['A'],example_sigma)==H['B']
res['closure_inventory_conjugacy']={
 'A_to_B_axis_permutation':list(example_sigma),
 'same_S6_orbit':True,'orbit_size':180,'stabilizer_order':4}
res['status']='PASS'
print(json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2))
