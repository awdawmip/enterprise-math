#!/usr/bin/env python3
"""Recompute the positive ternary recorder, six-column FCC chart diagram and signed macro time laws."""
import argparse
from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from collections import Counter
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path
import runpy
import sys

HERE = Path(__file__).resolve().parent
VPATH = 'experiments/x6_nonfcc_observer_switch_v42_20260906/check_nonfcc_observer_switch.py'
QPATH = 'experiments/x6_triadic_rotation_v1_20260906/check_triadic_rotation.py'
EPATH = 'research_notes/chatgpt_direct/20261011_EULER_RELATIONAL_RECORDING.md'
POINTS = tuple(product(range(3), repeat=3))
ZERO = (0, 0, 0)

def apply_columns(cols, x):
    return tuple(sum(x[i] * cols[i][j] for i in range(3)) % 3 for j in range(3))

def record(x):
    j, a, r = x
    return (j, a, (r + j - a) % 3)

def cycle_lengths(f):
    unseen, lengths = set(POINTS), []
    while unseen:
        x, n = min(unseen), 0
        while x in unseen:
            unseen.remove(x)
            n += 1
            x = f[x]
        lengths.append(n)
    return sorted(lengths)

def max_decoded(lengths, targets):
    # Allocate one source orbit at a time to an unused divisible target orbit.
    sizes = sorted(set(targets))
    limits = tuple(targets.count(d) for d in sizes)
    states = {(0,) * len(sizes)}
    for n in lengths:
        after = set(states)
        for state in states:
            for i, d in enumerate(sizes):
                if n % d == 0 and state[i] < limits[i]:
                    out = list(state)
                    out[i] += 1
                    after.add(tuple(out))
        states = after
    return max(sum(a*b for a,b in zip(v,sizes)) for v in states)

def pure_check(qsource):
    q = qsource['q_triad']((0,1,2))
    target = {x:record(x) for x in POINTS}
    target_cycles = cycle_lengths(target)
    eye = ((1,0,0),(0,1,0),(0,0,1))
    diag = (1,1,1)
    rows = []
    for t in range(6):
        qt = qsource['power'](q,t)
        action = {x:tuple(y % 3 for y in qsource['act'](qt,x+ZERO)[:3]) for x in POINTS}
        lengths = cycle_lengths(action)
        common = sum(d*min(lengths.count(d),target_cycles.count(d)) for d in set(target_cycles))
        best, once, twice = 0, 0, 0
        for cols in product(POINTS, repeat=3):
            # All linear intertwiners, then invertible preparation encoders.
            if all(apply_columns(cols,action[e])==record(c) for e,c in zip(eye,cols)):
                best=max(best,len({apply_columns(cols,x) for x in POINTS}))
            fixed=tuple(sum(row[i] for row in cols)%3 for i in range(3))
            j,a,r = cols
            destination=tuple((j[i]+r[i])%3 for i in range(3))
            if action[fixed]!=fixed or action[j]!=destination:
                continue
            if len({apply_columns(cols,x) for x in POINTS})!=27:
                continue
            once += 1
            twice += action[destination]==tuple((j[i]+2*r[i])%3 for i in range(3))
        rows.append({'delay':t,'source_cycles':dict(Counter(lengths)),'lossless_invariant_size':common,'largest_image':max_decoded(lengths,target_cycles),'largest_affine_image':best,'prepared_invertible_linear_one':once,'prepared_invertible_linear_two':twice})
    assert [v['largest_image'] for v in rows]==[9,14,23,9,23,14]
    assert [v['largest_affine_image'] for v in rows]==[9,1,9,1,9,1]
    assert [v['prepared_invertible_linear_one'] for v in rows]==[0,0,36,0,36,0]
    assert all(v['prepared_invertible_linear_two']==0 for v in rows)
    prep = [x for x in POINTS if x[1]==x[2]]
    saturation = {s for x in prep for s in (x,record(x),record(record(x)))}
    assert len(saturation)==21
    return {'record_cycles':dict(Counter(target_cycles)), 'prepared':len(prep), 'prepared_saturation':len(saturation),'by_delay':rows}

def atlas_check(V):
    full, partial, bad = {}, {}, []
    for role in permutations(range(6),3):
        cols = tuple(V[i] for i in role)
        observed = {}
        for x in POINTS:
            y = apply_columns(cols,x)
            observed.setdefault(y,set()).add(apply_columns(cols,record(x)))
        if any(len(v)!=1 for v in observed.values()):
            bad.append(role)
            continue
        f = {y:next(iter(v)) for y,v in observed.items()}
        (full if len(f)==27 else partial)[role] = f
    data = set(tuple(f[x] for x in POINTS) for f in full.values())
    global_maps = sorted(data)
    spectrum=Counter()
    ext=Counter()
    for f in global_maps:
        table=dict(zip(POINTS,f))
        matches_full=[r for r,g in full.items() if g==table]
        matches_partial=[r for r,g in partial.items() if all(table[x]==y for x,y in g.items())]
        spectrum[(len(matches_full),len(matches_partial))]+=1
        ext.update(matches_partial)
    assert len(full)==96 and len(partial)==8 and len(bad)==16
    assert len(global_maps)==32 and len(ext)==8 and set(ext.values())=={3}
    assert max(s+t for s,t in spectrum)==6
    out_hist=Counter(len({f[i] for f in global_maps}) for i in range(len(POINTS)))
    assert out_hist=={1:1,11:12,13:14}
    example=[(j,a,4) for j in (0,3) for a in (1,2,5)]
    assert all(r in full for r in example) and len({tuple(full[r][x] for x in POINTS) for r in example})==1
    return {'axes':['AB','CD','AC','BD','BC','AD'],'V':V,'good_rank3':len(full),'good_rank2':sorted(partial),'blocked_rank2':sorted(bad),'global_actions_forced':len(global_maps),'simultaneous_counts':{f'{i} full + {j} plane':n for (i,j),n in sorted(spectrum.items())},'extensions_of_each_valid_plane':sorted(ext.values()),'number_of_distinct_outputs_per_known_point':dict(out_hist),'six_role_example':example}

def rank(matrix):
    pivots = {}
    for v in matrix:
        row = list(map(Fraction, v))
        for i, pivot in sorted(pivots.items()):
            c = row[i]
            if c:
                row = [a - c*b for a, b in zip(row, pivot)]
        i = next((i for i, x in enumerate(row) if x), None)
        if i is not None:
            pivots[i] = [v / row[i] for v in row]
    return len(pivots)


def positive_check(adapter, brc):
    calls = Counter()
    atoms = Counter()
    terminal = {}
    for j, sheet0, field, vertex, flag, a, r in product(range(3),range(2),range(8),range(4),range(2),range(3),range(3)):
        z = (j,sheet0,field,vertex,flag,a,r)
        for sheet in range(2):
            out = z
            branch = brc.cwm_edge(Fraction(1,3456))
            calls['edge'] += 1
            for atom in adapter['instructions'](z,'E',sheet):
                atoms[atom] += 1
                out = adapter['primitive'](out,atom,sheet)
                branch = brc.cwm_propagate(branch,brc.CWM_ONE)
                calls['propagate'] += 1
            assert out == (*z[:-1],record((j,a,r))[2])
            key = (sheet,out[0],out[-2],out[-1])
            terminal[key] = brc.cwm_recoalesce(terminal.get(key,brc.CWM_ZERO),branch)
            calls['recoalesce'] += 1
    assert len(terminal)==54 and all(t.total==Fraction(1,27) and t.count==128 for t in terminal.values())
    return {'joint_states':3456, 'receiver_sheets':2,'named_positive_outputs_per_sheet':27,'each_output_mass':'1/27','per_world_certificate':dict(calls),'receiver_instructions':dict(atoms)}


def ternary_rows(native):
    ready = [x for x in POINTS if x[1]==x[2]]
    cal = {u for x in ready for u in (x,record(x),record(record(x)))}
    assert len(cal)==21
    profile = Counter()
    for role in permutations(range(6),3):
        mat = native['matS'](role)
        project = {x:tuple(a%3 for a in native['mv'](mat,x)) for x in POINTS}
        if len(set(project.values()))==27:
            continue
        def pair(x):
            return (project[x],project[record(x)])
        phases = [ready,[record(x) for x in ready],[record(record(x)) for x in ready]]
        counts = tuple(len({project[x] for x in level}) for level in phases)
        good = len(set(map(pair,POINTS)))==9
        occupation = Counter(project[x] for x in cal) if not good else Counter()
        fiber = {}
        # All weights are positive integers; the chosen offset prevents accidental uniformity.
        for z,x in enumerate(POINTS):
            y=project[x]
            masses=fiber.setdefault(y,[0,0,0])
            masses[(x[0]-x[1])%3] += (1+z)*(1+z)+2
        for masses in fiber.values():
            w=sum(masses);u=masses[0]-masses[2];v=masses[1]-masses[2]
            assert (w-u-v)%3==0 and ((w-u-v)//3)==masses[2]
        # Each observer row is the indicator of a separate phase/readout bin.
        def separate_rank(cases):
            bins = [(t,y) for t in range(3) for y in set(project.values())]
            def coords(x):
                return [project[x],project[record(x)],project[record(record(x))]]
            columns=[coords(x) for x in cases]
            return rank([[col[t]==y for col in columns] for t,y in bins])
        dims=tuple(separate_rank(cases) for cases in (POINTS,sorted(cal),ready))
        if good:
            assert dims==(9,9,9)
        else:
            assert dims==(21,18,9)
            assert Counter(occupation.values())=={2:6,3:3}
            # Total variation between true uniform triples and their Markov gluing.
            paths=Counter(tuple(project[u] for u in (x,record(x),record(record(x)))) for x in POINTS)
            ab=Counter();bc=Counter();center=Counter()
            for (a,b,c),n in paths.items():
                ab[a,b]+=n;bc[b,c]+=n;center[b]+=n
            domain=set(project.values())
            tv=sum(abs(Fraction(paths[a,b,c],27)-Fraction(ab[a,b]*bc[b,c],27*center[b])) for a,b,c in product(domain,repeat=3))/2
            assert tv==Fraction(2,3)
        profile[(counts,dims)]+=1
    return [{'visible_calibrated_by_phase':cs,'separate_observation_ranks_full_saturation_ready':rs,'roles':v} for (cs,rs),v in sorted(profile.items())]


def weak(total, size):
    if size == 1:
        yield (total,)
        return
    for x in range(total+1):
        for other in weak(total-x,size-1):
            yield (x,)+other


def margins(row):
    return tuple(tuple(sum(row[3*s+d] for s in range(3) for d in range(3) if (s+t*d)%3==z)
                       for z in range(3)) for t in range(3))


def count_integral(m):
    x,y,z=m
    if sum(x)!=sum(y) or sum(x)!=sum(z):
        return 0
    # Signed 3-by-3 coupling with prescribed first two marginals.
    b=[[0,0,x[0]],[0,0,x[1]],[y[0],y[1],x[2]-y[0]-y[1]]]
    diff=[z[k]-sum(b[i][j] for i in range(3) for j in range(3) if (i+j+k)%3==0) for k in range(3)]
    if (diff[1]-diff[0])%3:
        return 0
    beta=(diff[1]-diff[0])//3
    for j,mult in ((0,diff[1]-beta),(2,beta)):
        b[0][j]+=mult
        b[1][(j+1)%3]+=mult
        b[0][(j+1)%3]-=mult
        b[1][j]-=mult
    row=tuple(b[s][(s+d)%3] for s in range(3) for d in range(3))
    assert margins(row)==m
    slack=sum(min(row[3*s+d] for s in range(3)) for d in range(3))
    return (slack+2)*(slack+1)//2 if slack>=0 else 0


def marginal_census():
    valid=observed=total=0
    for n in range(7):
        truth=Counter(margins(row) for row in weak(n,9))
        total+=sum(truth.values())
        opts=list(weak(n,3))
        for m in product(opts,repeat=3):
            size=count_integral(m)
            assert size==truth[m]
            if size:
                valid+=1
            observed+=1
    uniform2 = ((6,6,6),)*3
    assert count_integral(uniform2)==28
    # Subtracting one unit in each cell reduces every margin entry by three.
    assert count_integral(((3,3,3),)*3)==10
    return {'mass_at_most':6,'nonnegative_source_tables':total,'equal_total_margin_triples':observed,
            'feasible_margin_triples':valid,'uniform_mass_two_nonnegative_solutions_per_line':28,
            'uniform_mass_two_strictly_positive_solutions_per_line':10}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path.cwd())
    parser.add_argument('--adapter',type=Path,default=HERE.parent/'hundredninth'/'feedback_check.py')
    args=parser.parse_args()
    gatebook='research_tasks/RS-EULER-RR-09-NATIVE-BRIDGE-20261011.md'
    check='research_notes/chatgpt_direct/20261011_EULER_RELATIONAL_RECORDING_CHECKPOINT.json'
    brc_file='src/enterprise_math/brc_weighted.py'
    pins={VPATH:'b00d3a283b84bf2082eeb0e69b4d750eaf18fd38b90c36f6e1d711eca15763d2',
          QPATH:'42a04380e294281e56fca8c26cb278bfdcd0c2d668b119f25a29dc9ec6f9c477',
          EPATH:'76093e17469197d950ec5c540cc876d1bc3713efc673f1b92f187fdac381a4ef',
          gatebook:'c4856c05d5a1e946ce06cc6554afa280547a6fbf48a4e6de9da95f6b6e247d3f',
          check:'02b2a319736fa19a6e79fad488e469008cbb90b04bfbb1bea5d3f61c8df5aa60',
          brc_file:'4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f'}
    for rel,digest in pins.items():
        assert sha256((args.repo/rel).read_bytes()).hexdigest()==digest,rel
    assert json.loads((args.repo/check).read_bytes())['proof']['sha256']==pins[EPATH]
    assert 'E(j,a,r)=(j,a,r+j-a).' in (args.repo/EPATH).read_text()
    adapter_sha=sha256(args.adapter.read_bytes()).hexdigest()
    assert adapter_sha=='868595349d4ed76eee8c8cd7376afa43e20e409d99e4c7c648b70fd966884621'
    with redirect_stdout(StringIO()):
        native=runpy.run_path(str(args.repo/VPATH))
        rotation=runpy.run_path(str(args.repo/QPATH))
    adapter=runpy.run_path(str(args.adapter))
    sys.path.insert(0,str((args.repo/'src').resolve()))
    from enterprise_math import brc_weighted
    output={'registered_task':'RS-EULER-RR-09-NATIVE-BRIDGE-20261011','source_sha256':pins,
            'public_gate_adapter_sha256':adapter_sha,'positive_gate':positive_check(adapter,brc_weighted),
            'fcc':atlas_check(native['V']),'calibrated_and_positive_readouts':ternary_rows(native),
            'three_time_integer_marginals':marginal_census(),'fixed_macro_time':pure_check(rotation)}
    print(json.dumps(output,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
