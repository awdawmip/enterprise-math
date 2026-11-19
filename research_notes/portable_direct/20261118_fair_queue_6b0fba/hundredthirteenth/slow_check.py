"""Exact feedback-word and modular-column replay, Python 3.10+. See slow.md for inputs."""
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import combinations, product
import json
from math import gcd
from pathlib import Path

WIDTH = 4
L = 2 ** WIDTH
MODULI = (7, 21, 35, 13, 31, 17, 151, 257)
BITS = (0, 1)
HELPER_SHA = "b79a92b28b0528e7e8a3b026c9716e9379f1ef21f891ad8f4db36f6a384dc62e"
STREAM_SHA = "635d0c4aee0aaa8d58bb0244835e08e5caa0f6a94926a5213519f40db992a257"


def file_sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def word(h):
    return ''.join(map(str, h))


def zero_mass(length, order):
    q, r = divmod(length, order)
    return F((order - r)*q*q + r*(q + 1)**2, length*length)


def zero_diagnostics():
    pairs = 0
    for m in range(1, 10):
        n = 2**m
        for d in range(1, n):
            b = (n - 1)//d
            gap = zero_mass(n,d) - zero_mass(n,d+1)
            assert gap == F(2, n*n)*sum(min(j, n - j*d) for j in range(1, b+1))
            assert gap**2 / zero_mass(n,d) >= F(4,3*n**3)
            pairs += 1
    return pairs


def kernel(lib, rd, sim):
    memo, rows = {}, {}
    charge = Counter()
    for d in range(1, WIDTH+1):
        for u in product(BITS, repeat=d-1):
            bind = rd.Ops()
            w = lib.bind_word(rd,bind,sim,u+(0,))
            charge['reduced_bindings'] += 1
            charge['reduced_binding_kernel_calls'] += len(bind.observer.operations)
            for D in range(1, 2**d, 2):
                op = rd.Ops()
                memo[u,D] = rd.carry(op,w,D,rd.eye())
                charge['reduced_carry_queries'] += 1
                charge['reduced_carry_kernel_calls'] += len(op.observer.operations)
    for h in product(BITS, repeat=WIDTH):
        op = rd.Ops()
        w = lib.bind_word(rd,op,sim,h)
        vectors = [rd.alpha(op,w,x) for x in range(L)]
        row = {}
        for R in range(1, L):
            g = R & -R
            d = WIDTH - (g.bit_length()-1)
            want = g*(-1)**h[d-1]*memo[h[:d-1],R//g]
            direct = sum(op.dot(vectors[x],vectors[x+R]) for x in range(L-R))
            assert want == direct
            charge['independent_direct_pairs'] += L-R
            row[R] = direct
        charge['direct_bindings'] += 1
        charge['direct_vectors'] += len(vectors)
        charge['direct_binding_vectors_and_dots_kernel_calls'] += len(op.observer.operations)
        rows[h] = row
    for a,b in combinations(range(1,L),2):
        if (a & -a) != (b & -b):
            assert sum(row[a]*row[b] for row in rows.values()) == 0
            charge['orthogonal_lag_pairs'] += 1
    assert all(sum(row[a] for row in rows.values()) == 0 for a in range(1,L))
    return rows,dict(charge)


def native_tree(lib, sim):
    frontier = {(): sim.initial()}
    masses = {(): F(1)}
    charges = Counter()
    final_work = {}
    for i in range(WIDTH):
        nxt = {}
        for h,(state,den) in frontier.items():
            plan = sim.branch_plan(state,den,h)
            charges['branch_plan'] += 1
            for bit, mass in enumerate(plan.masses):
                v = h+(bit,)
                masses[v] = mass
                if mass:
                    child = sim.materialize(plan,bit)
                    nxt[v] = child
                    charges['materialize'] += 1
                    field = lib.raw_field(*child)
                    work = {label:sum(x*x for x in row.values()) for label,row in field.items()}
                    assert mass == sum(work.values())
                    if sim.N == 151 and i+1 == WIDTH:
                        final_work[v] = work
        frontier = nxt
    return masses,dict(charges),final_work


def fixture(lib,api,sim,rows,N):
    calls = api[2]
    returns, queries = [], []
    before = len(calls)
    for R in range(1,L):
        hit, cols = lib.certify(sim,WIDTH,R)
        queries.append([R,hit,cols])
        if hit:
            returns.append(R)
    lookup_cost = len(calls)-before
    d = min(returns,default=L)
    assert returns == list(range(d,L,d))
    before = len(calls)
    masses, charges, final_work = native_tree(lib,sim)
    charges['tree_new_stage45_records'] = len(calls)-before
    charges['discovery_new_stage45_records'] = lookup_cost
    charges['discovery_modular_column_requests'] = sum(len(query[2]) for query in queries)
    levels = []
    for i in range(WIDTH+1):
        level = {}
        for z in product(BITS,repeat=i):
            h = z+(0,)*(WIDTH-i)
            active = [r for r in returns if r % (1<<(WIDTH-i)) == 0]
            est = (1+F(2,L)*sum(rows[h][r] for r in active))/2**i
            assert est == masses.get(z,0)
            level[z] = est
        assert sum(level.values()) == 1
        # d==L is a capped class: all d>=L remain nonreturning in this depth.
        di = d // gcd(d, 1<<(WIDTH-i))
        assert level[(0,)*i] == zero_mass(2**i,di)
        levels.append(level)
    energies = []
    for i in range(1,WIDTH+1):
        lag = [r for r in returns if (r & -r) == 2**(WIDTH-i)]
        energy = F()
        for z, parent in levels[i-1].items():
            h = z+(0,)*(WIDTH-i+1)
            A = F(2,L)*sum(rows[h][r] for r in lag)
            assert levels[i][z+(0,)]-levels[i][z+(1,)] == A/2**(i-1)
            if not parent:
                assert A == 0
            energy += A*A/2**(i-1)
        energies.append(energy)
    chi = sum((L*p-1)**2 for p in levels[-1].values())/L
    assert sum(energies) == chi
    report = dict(N=N,short_returns=returns,ordered_probe_log=queries,
                  charges=charges,prefix_masses=[[str(p) for p in v.values()] for v in levels],
                  native_leaf_count=sum(p>0 for p in levels[-1].values()),
                  uniform_reference_layer_energies=list(map(str,energies)),chi_squared=str(chi))
    if d == L-1:
        decisions, weights = Counter(),Counter()
        certificate = []
        labels = lib.labels_for_validation(sim,WIDTH)[:-1]
        assert len(set(labels)) == L-1 and labels[0] == labels[-1]
        tails = {w:F(1,L-2) for w in labels[1:-1]}
        for h, prob in levels[-1].items():
            delta = 2+2*rows[h][d]
            status = ('EXACT_BOUNDARY' if not delta else
                      'CERTIFIED_TRUNCATION' if 4*delta <= L-2 else 'RETAIN_RESIDUAL')
            work = final_work[h]
            assert all(work.get(label,0) == F(1,L*L) for label in tails)
            tv = sum(abs(work.get(w,0)/prob - tails.get(w,0)) for w in set(work)|set(tails))/2
            assert tv == delta/(L-2+delta)
            decisions[status] += 1
            weights[status] += prob
            certificate.append([word(h),str(delta),str(prob),status,str(delta/(L-2+delta))])
        report['boundary_cases'] = certificate
        report['boundary_counts'] = dict(decisions)
        report['boundary_born_weights'] = {s:str(p) for s,p in weights.items()}
    return report,levels


def main():
    parser=argparse.ArgumentParser(__doc__)
    for name in ('repo','stage','audit'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--wave18',type=Path,default=Path(__file__).resolve().parents[1]/
                        'eighteenth'/'return_defect_check.py')
    args=parser.parse_args()
    assert file_sha(args.wave18) == HELPER_SHA
    stream = args.repo/'research_notes/directed_recovery/20260926_C6438C/optimization/streaming/lazy_streaming.py'
    assert file_sha(stream) == STREAM_SHA
    spec=importlib.util.spec_from_file_location('prior_defect',args.wave18)
    lib=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lib)
    api=lib.imports(args.repo.resolve(),args.stage.resolve(),args.audit.resolve())
    cls,_,calls,bank,rd,_=api
    reports, runs = [], []
    for idx,N in enumerate(MODULI):
        before = len(calls)
        sim=cls(N,2,WIDTH,bank,61)
        admission_cost = len(calls)-before
        if idx==0:
            rows,kcost=kernel(lib,rd,sim)
        result,levels=fixture(lib,api,sim,rows,N)
        result['charges']['admission_new_stage45_records'] = admission_cost
        reports.append(result)
        runs.append(levels)
    separation = []
    for a,b in combinations(range(len(reports)),2):
        da = min(reports[a]['short_returns'],default=L)
        db = min(reports[b]['short_returns'],default=L)
        def tag(d,i): return min(2**i,d//gcd(d,1<<(WIDTH-i)))
        predicted=next((i for i in range(1,WIDTH+1) if tag(da,i)!=tag(db,i)),None)
        actual=next((i for i in range(1,WIDTH+1) if runs[a][i]!=runs[b][i]),None)
        zero=next((i for i in range(1,WIDTH+1) if runs[a][i][(0,)*i]!=runs[b][i][(0,)*i]),None)
        assert predicted==actual==zero
        separation.append([MODULI[a],MODULI[b],actual])
    out=dict(width=WIDTH,dimension=61,base=2,bank_sha256=lib.BANK,helper_sha256=HELPER_SHA,
             stream_sha256=STREAM_SHA,conditional_gate_epsilon='1/2',fixtures=reports,
             feedback_comparison=kcost,least_prefix_that_separates=separation,
             all_adjacent_fingerprint_gaps_checked=zero_diagnostics(),
             signed_lag_table={word(h):[str(v) for v in row.values()] for h,row in rows.items()})
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
