"""Replay the public H/U/C source and audit bounded-delay timestamp encodings."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from functools import cache
from hashlib import sha1, sha256
from itertools import combinations, product
import json
from math import gcd
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent
SIZE = 12
DEN = 384 * 3 * SIZE


def originals(repo):
    book = repo / 'research_tasks/RS-EULER-RR-02-ACTIVE-SOURCE-20261011.md'
    b = book.read_bytes()
    assert sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest() == '26d55961d6f0cfa214abd24b820c02c74bd0cd52'
    old = HERE.parent / 'seventyeighth/aperture_check.py'
    assert sha256(old.read_bytes()).hexdigest() == '77299a430908181c7de17050380a5dc3037dd3fd43b6d4292e9bdcb08307f53a'
    module = runpy.run_path(str(old))
    contact_path = HERE.parent / 'ninetieth/recorders_check.py'
    assert sha256(contact_path.read_bytes()).hexdigest() == 'f1af1e08c97d50ca1996796774fc6f1693fcc4ace1d9453837345a46a9d49f31'
    contact = runpy.run_path(str(contact_path))['signed_unit_contact']
    return module['source'](repo), module['source_atom'], module['published_cycle'],contact


def histories(step, macro):
    states = list(product(range(3), range(2), range(8), range(4), range(2)))
    prefixes = [{x:x for x in states}]
    for gate in 'HUC':
        prefixes.append({x:step(y, gate) for x,y in prefixes[-1].items()})
    assert all(prefixes[3][x] == macro(x) for x in states)
    inv = {y:x for x,y in prefixes[3].items()}
    columns = {}
    for u in range(3):
        current = {y:x for x,y in prefixes[u].items()}
        for k in range(SIZE):
            columns[k,u] = tuple(current[x][0] for x in states)
            current = {x:inv[y] for x,y in current.items()}
        assert all(prefixes[u][current[x]] == x for x in states)
    return states,columns


def classification(states, columns):
    words = list(zip(*(columns[k,0] for k in range(SIZE))))
    periods = Counter(next(d for d in range(1,13) if all(w[t]==w[(t+d)%12] for t in range(12))) for w in words)
    assert periods == {4:240,12:144}
    groups = defaultdict(list)
    for key,c in sorted(columns.items()):
        groups[c].append(key)
    sizes = [len(set(c for (k,u),c in columns.items() if k<=d)) for d in range(SIZE)]
    assert sizes == [1,3,6,9,12,15,18,20,23,26,29,31]
    pair_witnesses = []
    for (k,l) in combinations(range(SIZE), 2):
        i = next(i for i in range(len(states)) if columns[k,0][i]!=columns[l,0][i])
        j,j2 = columns[k,0][i],columns[l,0][i]
        a = 3-j-j2
        assert sorted((j,j2,a)) == [0,1,2]
        pair_witnesses.append((k,l,i,a))
    phase_differences = {}
    for u,v in combinations(range(3),2):
        phase_differences[str((u,v))] = [sum(a!=b for a,b in zip(columns[k,u],columns[k,v])) for k in range(12)]
    sequence = tuple(columns[k,u] for k in range(12) for u in range(3))
    assert all(any(sequence[i]!=sequence[(i+s)%36] for i in range(36)) for s in range(1,36))
    for d in range(35):
        worst = max(len({columns[((j+2-u)//3)%12,u] for j in range(d+1)}) for u in range(3))
        assert worst == min(12, 1+(d+2)//3)
    out = dict(channel_orbit_periods=dict(periods), end_phase_blind_class_counts_by_max_C=sizes,
               nonsingleton_phase_classes=sorted(cell for cell in groups.values() if len(cell)>1),
               unknown_end_phase_disagreements=phase_differences, source_microclock_minimal_period=36,
               distinct_macro_phase_pairs=len(pair_witnesses), pair_witnesses_k_l_stateindex_reference=pair_witnesses)
    return words, out


def costs(words):
    grouped = Counter(tuple(sum(1<<i for i,j in enumerate(w) if j==s) for s in range(3)) for w in words)
    cost = []
    for mask in range(1<<SIZE):
        wrong = 0
        for triple,n in grouped.items():
            h = [(mask & a).bit_count() for a in triple]
            wrong += n*sum(min(h[j],h[(j+1)%3]) for j in range(3))
        cost.append(wrong)
    return cost


def optimal_tables(cost):
    full = (1<<SIZE)-1
    @cache
    def best(m,q):
        if q==1:
            return cost[m],(m,)
        first = m & -m
        s = m
        answer = (DEN+1,None)
        while s:
            if s & first and (m^s).bit_count()>=q-1:
                value,parts = best(m^s,q-1)
                candidate = (value+cost[s],(s,)+parts)
                if candidate[0]<answer[0]:
                    answer = candidate
            s = (s-1)&m
        return answer

    optimum = [best(full,q) for q in range(1,SIZE+1)]
    # Independent restricted-growth enumeration. Each unlabelled partition occurs once.
    low = [DEN+1]*(SIZE+1)
    partition_counts = Counter()
    groups = [0]*SIZE
    def enumerate_partitions(i,q,value):
        if i==SIZE:
            low[q] = min(low[q],value)
            partition_counts[q] += 1
            return
        bit = 1<<i
        for t in range(q):
            old = groups[t]
            groups[t] = old|bit
            enumerate_partitions(i+1,q,value+cost[old|bit]-cost[old])
            groups[t] = old
        groups[q] = bit
        enumerate_partitions(i+1,q+1,value)
        groups[q] = 0
    enumerate_partitions(0,0,0)
    assert low[1:]==[v for v,_ in optimum] and sum(partition_counts.values()) == 4213597
    return optimum,partition_counts


def residues(words):
    out = {}
    for d in (1,2,3,4,6,12):
        hits_plain = hits_contact = 0
        for w in words:
            for h in range(d):
                cell = Counter(w[h::d])
                hits_plain += 3*max(cell.values())
                for a in range(3):
                    hits_contact += cell[a]+max(cell[(a+1)%3],cell[(a+2)%3])
        out[d] = dict(no_first_contact=str(Fraction(hits_plain,DEN)),
                      with_first_contact=str(Fraction(hits_contact,DEN)))
    return out


def autonomous_clocks(cost, optimal):
    curves=[]
    for q in range(1,SIZE+1):
        options={}
        for tail in range(q):
            for cycle in range(1,q-tail+1):
                groups=defaultdict(int)
                for k in range(SIZE):
                    state=k if k<tail else tail+(k-tail)%cycle
                    groups[state] |= 1<<k
                options[tail,cycle]=sum(cost[g] for g in groups.values())
        best=min(options.values())
        assert best==optimal[q-1][0] if q!=3 else Fraction(best,DEN)==Fraction(35,288)
        curves.append(dict(internal_states=q,minimum_risk=str(Fraction(best,DEN)),
                           best_tail_cycle=[list(k) for k,v in options.items() if v==best],
                           reversible_minimum_risk=str(Fraction(min(v for (t,c),v in options.items() if t==0),DEN))))
    return curves


def source_runs(states, words, step, brc, contact, parts):
    bins = defaultdict(lambda:brc.CWM_ZERO)
    calls = Counter()
    size = DEN*2
    for i,(x,w) in enumerate(zip(states,words)):
        for mask in parts:
            cell = Counter(w[t] for t in range(12) if mask>>t&1)
            for a,sign in product(range(3),(-1,1)):
                choices = [(a+sign)%3,(a-sign)%3]
                decision = max(choices,key=lambda j:cell[j])
                for k in range(12):
                    if not mask>>k&1:
                        continue
                    j = w[k]
                    first = int(j!=a)
                    r = (a+sign*first)%3
                    second = int(first and decision==(a-sign)%3)
                    result = (r+sign*second)%3
                    assert (result==j) == (not first or decision==j)
                    past = x
                    for _ in range((-k)%12):
                        for command in 'HUC':
                            past = step(past,command)
                    assert past[0]==j
                    ports=[j,a,a]
                    mass=contact(ports,2,sign*first,(1,sign),brc.cwm_edge(Fraction(1,size)),brc,calls)
                    assert ports[2]==r
                    for _ in range(k):
                        for command in 'HUC':
                            past = step(past,command)
                            mass = brc.cwm_propagate(mass,brc.CWM_ONE)
                    assert past==x
                    ports[0]=past[0]
                    mass=contact(ports,2,sign*second,(1,sign),mass,brc,calls)
                    assert ports==[x[0],a,result]
                    bins[result==j] = brc.cwm_recoalesce(bins[result==j],mass)
                    calls['worlds']+=1
                    calls['executed_source_microsteps']+=3*k
                    calls['first_contacts']+=first
                    calls['second_contacts']+=second
    assert sum(v.total for v in bins.values())==1
    return dict(wrong_probability=str(bins[False].total),
                positive_source_and_receiver_slot_propagations=calls['executed_source_microsteps']+2*calls['worlds'],
                **calls)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo',required=True,type=Path)
    args=ap.parse_args()
    brc,step,macro,contact=originals(args.repo)
    states,columns=histories(step,macro)
    words,source=classification(states,columns)
    cost=costs(words)
    tables,counts=optimal_tables(cost)
    pairs=[cost[1|(1<<d)] for d in range(1,7)]
    assert pairs==[384,192,336,120,288,240]
    assert cost[1|4|16]==cost[1|16|256]==288
    for mask in range(1,1<<SIZE):
        if mask.bit_count()<=5:
            assert cost[mask]>=120*(mask.bit_count()-1)
    risk=[]
    for q,(value,parts) in enumerate(tables,1):
        risk.append(dict(labels=q,error=str(Fraction(value,DEN)),
                         partition=[[k for k in range(12) if m>>k&1] for m in parts]))
    native=source_runs(states,words,step,brc,contact,tables[2][1])
    assert native['wrong_probability']==risk[2]['error']=='1/9'
    print(json.dumps(dict(source=source, residue_clock_accuracy=residues(words),optimal_exports=risk,
                          partition_counts=dict(counts),two_lag_cost_by_separation=pairs,autonomous_finite_window_clocks=autonomous_clocks(cost,tables),positive_original_input_run=native),
                     ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__':main()
