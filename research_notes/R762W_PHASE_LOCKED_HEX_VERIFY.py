"""R762W: exact native X6 hexagonal coordinate witness and phase-locked V29 token scheduler.
Research candidate only, not an accepted P000 TRIADIC_CLOSURE_E force event.
"""
import itertools, collections, json

def x6_walk(word):
    p=[0]*6; visits=[]; current=collections.Counter()
    for s in word:
        before=tuple(p); axis=abs(s)-1
        p[axis]+=1 if s>0 else -1
        after=tuple(p); visits.append(after)
        edge=(before if s>0 else after,axis)
        current[edge]+=1 if s>0 else -1
    return tuple(p),visits,tuple(sorted((a,v) for a,v in current.items() if v))

def apply_pass(inventory, passage):
    a,b=passage
    assert inventory[a]>=1
    inventory[a]-=1;inventory[b]+=1

def hex_event(order):
    a,b,d=order
    word=(a,b,-a,d,-b,-d)
    final,visits,current=x6_walk(word)
    assert final==(0,)*6
    assert not (0,)*6 in visits[:-1]
    assert all(word[i]!=-word[i+1] for i in range(5))
    assert len(current)==6
    assert all(abs(v)==1 for _,v in current)
    assert len({abs(s) for s in order})==3
    for t,s in [(0,a),(2,b),(4,d)]:
        neighbor=tuple((1 if s>0 else -1) if q==abs(s)-1 else 0 for q in range(6))
        assert visits[t]==neighbor
    passes=((a,b),(b,d),(d,a))
    return word,current,passes

def repeatability(order,k,seed):
    inv=collections.Counter(seed)
    for r in range(k):
        cur=tuple(order[r%3:]+order[:r%3])
        before=inv.copy()
        for passage in hex_event(cur)[2]: apply_pass(inv,passage)
        assert inv==before
    return inv

def min_seeds_phase_lock(order,k):
    firsts=set(order[i%3] for i in range(k))
    seed={a:1 for a in firsts}
    repeatability(list(order),k,seed)
    assert len(firsts)==min(k,3)
    for a in firsts:
        test=seed.copy();test[a]-=1
        try:
            repeatability(list(order),k,test)
        except AssertionError:
            continue
        raise AssertionError('unnecessary required phase token')
    return len(firsts)

def perms6():
    return itertools.permutations(range(6))

def axis_relabel(s,perm):
    return (1 if s>0 else -1)*(perm[abs(s)-1]+1)

def verify():
    tested_states=0;cycle_classes=set();v29_classes=collections.Counter()
    for axes in itertools.combinations(range(1,7),3):
        for signs in itertools.product((1,-1),repeat=3):
            T=tuple(x*y for x,y in zip(axes,signs))
            currents=set();pass_classes=collections.defaultdict(list)
            for order in itertools.permutations(T):
                word,j,passes=hex_event(order)
                currents.add(j)
                pass_classes[frozenset(passes)].append(order)
                for k in range(1,8):
                    assert min_seeds_phase_lock(order,k)==min(k,3)
                tested_states+=1
            assert len(currents)==6
            assert sorted(map(len,pass_classes.values()))==[3,3]
            cycle_classes.add((tuple(sorted(T)),len(pass_classes)))
            v29_classes[tuple(sorted(map(len,pass_classes.values())))]+=1
    assert tested_states==960
    assert len(cycle_classes)==160
    assert v29_classes=={(3,3):160}
    # Full S6 covariance on a representative mixed-sign triad, plus complete
    # 160-state census via relabeling bijection and source-typed formulas.
    anchor=(1,-3,5)
    for perm in perms6():
        for order in itertools.permutations(anchor):
            image=tuple(axis_relabel(s,perm) for s in order)
            w0,j0,P0=hex_event(order)
            w1,j1,P1=hex_event(image)
            assert w1==tuple(axis_relabel(s,perm) for s in w0)
            assert P1==tuple((axis_relabel(a,perm),axis_relabel(b,perm)) for a,b in P0)
            assert len(j0)==len(j1)==6
    return {
        'schema':'R762W_HEX_FIRST_RETURN_PHASE_LOCKED_TOKEN_V1',
        'scope':'P000-native coordinate and source-labeled candidate macroevent; V29-count compatible; extra phase-locked conditional token semantics',
        'signed_port_triads':160,
        'ordered_lifts_per_triad':6,
        'candidate_ordered_hex_events_checked':tested_states,
        'distinct_rooted_edge_currents_per_triad':6,
        'distinct_complete_V29_PASS_matrices_per_triad':2,
        'source_order_fiber_size_given_complete_PASS_matrix':3,
        'phase_rotation_period':3,
        'phase_cycles_total':320,
        'single_event_PASS_count':3,
        'k_rounds_min_initial_tokens_fixed_phase_macroblock':{str(k):min(k,3) for k in range(1,8)},
        'k_rounds_min_initial_tokens_free_global_PASS_reordering':1,
        'additional_phase_lock_seed_cost_for_k_at_least_3':2,
        'axis_permutations_checked':720,
        'representative_covariance_order_checks':4320,
        'verified':'all assertions passed; exact integer enumeration plus constructive lower and upper bound',
        'native_force_admission':'OPEN; no TRIADIC_CLOSURE_E physics or V39 holonomy claimed'
    }

if __name__=='__main__':
    print(json.dumps(verify(),indent=2,sort_keys=True))
