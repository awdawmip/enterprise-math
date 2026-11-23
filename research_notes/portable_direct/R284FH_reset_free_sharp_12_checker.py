"""R284FH: exact 4-cycle capacity n=12 for one omission and one read flip.

Model: fixed 4 words, arbitrarily many generations, non-atomic bit writes,
at most one omission per generation (persistent), at most one fresh read flip,
stateless 4-label/RETRY decoder, mandatory correct completed-generation reads,
no third label / no new-then-old within any publishing trace.

Only Python standard library. Running this file reproduces the lower-search
counts and tests the exhibited 12-bit witness against an independent BFS.
"""
from collections import deque, Counter
from itertools import combinations_with_replacement
import json

U=Q=1

def words_from_patterns(patterns):
    return tuple(0 if i==0 else sum(((p>>(i-1))&1)<<k
                for k,p in enumerate(patterns)) for i in range(4))

def bits(x,n):
    return tuple(k for k in range(n) if x & (1<<k))

def edge_order_default(words,n,i):
    return bits(words[i]^words[(i+1)%4],n)

def last_update_groups(words,n,phase):
    """Partitions active coordinates by most recent updating edge."""
    groups=[[] for _ in range(4)]
    for k in range(n):
        for age in range(1,5):
            e=(phase-age)%4
            if (words[e]^words[(e+1)%4]) & (1<<k):
                groups[e].append(k)
                break
        else:
            raise AssertionError('Unused constant coordinate: delete it first')
    return groups

def closed_form_stable(words,n,phase):
    """Exact all-history stable states for Q=1, independent of write order."""
    possible={0}
    for group in last_update_groups(words,n,phase):
        option=[0]+[1<<k for k in group]
        possible={r^v for r in possible for v in option}
    return {words[phase]^r for r in possible}

def stable_by_bfs(words,n,orders):
    """Independent transition fixed-point algorithm; not the above formula."""
    states=[set() for _ in range(4)]
    states[0].add(words[0])
    frontier=deque([(0,words[0])])
    while frontier:
        i,v=frontier.popleft()
        j=(i+1)%4
        for omitted in [None]+list(orders[i]):
            x=v
            for k in orders[i]:
                if k!=omitted:
                    x=(x&~(1<<k))|(words[j]&(1<<k))
            if x not in states[j]:
                states[j].add(x)
                frontier.append((j,x))
    return states

def masks(words,n,stable):
    """Read observation y forced to an epoch; then forced at physical x."""
    by_y=[0]*(1<<n)
    for i,states in enumerate(stable):
        for s in states:
            for y in [s]+[s^(1<<k) for k in range(n)]:
                by_y[y] |=1<<i
    collision=sum(v.bit_count()>1 for v in by_y)
    by_x=[by_y[x] for x in range(1<<n)]
    for x in range(1<<n):
        for k in range(n):
            by_x[x] |= by_y[x^(1<<k)]
    return by_y,by_x,collision

def first_valid_order(words,n,i,stable,by_x):
    """Exhaust fixed permutations, pruning any irreparably bad prefix."""
    j=(i+1)%4
    old=1<<i
    new=1<<j
    allowed=old|new
    changes=edge_order_default(words,n,i)
    scenarios=tuple((s,omit,False) for s in sorted(stable[i])
                    for omit in [None]+list(changes))
    nodes=0
    def visit(rest,cases,path):
        nonlocal nodes
        nodes+=1
        if not rest:
            return tuple(path)
        for k in rest:
            mask=1<<k
            target=words[j]&mask
            next_cases=[]
            good=True
            for physical,omitted,seen_new in cases:
                nxt=physical if k==omitted else (physical&~mask)|target
                forced=by_x[nxt]
                if (forced &~allowed) or ((forced & old) and
                     ((forced & new) or seen_new)):
                    good=False
                    break
                next_cases.append((nxt,omitted,
                                   seen_new or bool(forced&new)))
            if good:
                answer=visit(tuple(v for v in rest if v!=k),
                             tuple(next_cases),path+(k,))
                if answer is not None:
                    return answer
        return None
    return visit(changes,scenarios,()),nodes

def full_prefix_check(words,n,orders,stable,by_x):
    """Direct independent full-trace enumeration for the upper witness."""
    placements=0
    for i in range(4):
        j=(i+1)%4
        old=1<<i
        new=1<<j
        allowed=old|new
        for source in stable[i]:
            for omit in [None]+list(orders[i]):
                x=source
                seen_new=False
                for k in [None]+list(orders[i]):
                    if k is not None and k!=omit:
                        x=(x&~(1<<k))|(words[j]&(1<<k))
                    forced=by_x[x]
                    assert not (forced &~allowed), ('third',i,source,omit,k,x,forced)
                    assert not ((forced & old) and ((forced & new) or seen_new)), \
                           ('rollback',i,source,omit,k,x,forced)
                    seen_new |=bool(forced&new)
                    placements+=1
    return placements

def do_search(n):
    counts={'pattern_multisets':0,'pass_distance':0,
            'pass_stable':0,'pass_edge0_order':0}
    examples=[]
    for patterns in combinations_with_replacement(range(1,8),n):
        counts['pattern_multisets']+=1
        words=words_from_patterns(patterns)
        edges=[(words[i]^words[(i+1)%4]).bit_count() for i in range(4)]
        diagonals=[(words[i]^words[i+2]).bit_count() for i in range(2)]
        # Analytic necessary edge/diagonal distances for u=q=1.
        if min(edges)<7 or min(diagonals)<5:
            continue
        counts['pass_distance']+=1
        stable=[closed_form_stable(words,n,i) for i in range(4)]
        _,by_x,collisions=masks(words,n,stable)
        if collisions:
            continue
        counts['pass_stable']+=1
        order,nodes=first_valid_order(words,n,0,stable,by_x)
        if len(examples)<10:
            examples.append({
                'pattern_multiplicity':dict(sorted(Counter(patterns).items())),
                'words':words,'edges':edges,'diagonals':diagonals,
                'phase0_valid_order':order,'edge0_order_nodes':nodes})
        if order is not None:
            counts['pass_edge0_order']+=1
    return counts,examples

def main():
    lower={}
    samples={}
    for n in (10,11):
        lower[str(n)],samples[str(n)]=do_search(n)
        assert lower[str(n)]['pass_edge0_order']==0
    assert lower['10']=={'pattern_multisets':8008,'pass_distance':3,
                         'pass_stable':0,'pass_edge0_order':0},lower['10']
    assert lower['11']=={'pattern_multisets':12376,'pass_distance':47,
                         'pass_stable':3,'pass_edge0_order':0},lower['11']
    n=12
    words=(0,255,3855,4080)
    orders=((0,4,5,1,2,3,6,7),
            (4,5,8,9,6,10,7,11),
            (0,4,5,1,2,3,6,7),
            (4,5,8,9,6,10,7,11))
    for i in range(4):
        assert tuple(sorted(orders[i])) == edge_order_default(words,n,i)
    formula=[closed_form_stable(words,n,i) for i in range(4)]
    bfs=stable_by_bfs(words,n,orders)
    assert bfs==formula,'Independent cyclic-transition BFS differs from closed form'
    by_y,by_x,collisions=masks(words,n,formula)
    assert collisions==0
    for i in range(4):
        for s in formula[i]:
            assert by_y[s]==1<<i
    placements=full_prefix_check(words,n,orders,bfs,by_x)
    result={
      'statement':'n_min(1,1)=12 in the four-fixed-word, reset-free cyclic omission model',
      'verification':'exact integer exhaustive finite proof; independent BFS upper crosscheck',
      'domain':{'epochs':4,'per_edge_omissions':1,'per_read_flips':1,
                'read_decoder':'stateless forced-epoch-or-RETRY',
                'publication':'one ordered attempt per changed bit; intermediate reads allowed',
                'carryover':'unbounded number of cycles, no cleanup'},
      'lower':lower,'lower_survivors':samples,
      'upper':{'n':12,'words_decimal':words,'orders':orders,
               'edge_distances':[(words[i]^words[(i+1)%4]).bit_count() for i in range(4)],
               'diagonal_distances':[(words[i]^words[i+2]).bit_count() for i in range(2)],
               'stable_state_counts':[len(s) for s in bfs],
               'observed_state_counts':[sum(1 for v in by_y if v==(1<<i)) for i in range(4)],
               'physical_prefix_scenario_placements_checked':placements,
               'individual_read_options_checked':placements*(n+1),
               'validated':True},
      'limit':'No independent mathematical review; n>=12 is model-specific; frozen task pins unchanged.'
    }
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
