"""Exact checks on the original all-stale reference carrier. Python 3.10+."""
import argparse
from collections import Counter, defaultdict
import hashlib
import importlib.util
from itertools import combinations, product
import json
from math import comb, factorial, gcd, prod
from pathlib import Path
import sys


SEED = Path("research_notes/brc_alias_counting_bridge_20261028/VERIFY.py")
COMMIT = "e7b9fb5084f93a9b2dbc16225629b667fb7bf46c"
BLOB = "d9029ff47031580cc59cfd1e4502012d189a250f"


def load_seed(repo):
    path = repo / SEED
    data = path.read_bytes()
    assert hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest() == BLOB
    sys.path.insert(0, str(repo / "src"))
    spec = importlib.util.spec_from_file_location("alias_seed", path)
    seed = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = seed
    spec.loader.exec_module(seed)
    return seed


def observation(labels, d):
    return tuple(x == labels[(i+d) % len(labels)] for i, x in enumerate(labels))


def components(bits, d):
    r, g = len(bits), gcd(len(bits), d)
    counts = [0]*(r//g+1)
    for start in range(g):
        jumps = sum(not bits[(start+i*d) % r] for i in range(r//g))
        if jumps == 1:
            return None
        counts[max(1, jumps)] += 1
    return tuple(t for t, count in enumerate(counts) for _ in range(count))


def chromatic_blocks(parts):
    def factor(t, x):
        if t == 1:
            return x
        return (x-1)**t + (-1)**t*(x-1)
    values = [prod(factor(t, x) for t in parts) for x in range(sum(parts)+1)]
    counts = {}
    for k in range(sum(parts)+1):
        numerator = values[0]
        counts[k], rem = divmod(numerator, factorial(k))
        assert rem == 0 and counts[k] >= 0
        values = [b-a for a, b in zip(values, values[1:])]
    return {k: v for k, v in counts.items() if v}


def brc_blocks(parts, seed):
    """Use only positive serial/recoalescence operations on branch multiplicities."""
    def move(dest, key, history, ways):
        if ways:
            assert ways > 0
            term = seed.serial(history, seed.WeightHistogram.from_counts({1: ways}))
            dest[key] = seed.recoalesce(dest.get(key, seed.ZERO), term)

    start = {0: seed.ONE}
    for length in parts:
        current = {}
        for k, mass in start.items():
            move(current, (k, True), mass, k)
            move(current, (k+1, True), mass, 1)
        for step in range(1, length):
            following = {}
            for (k, same), mass in current.items():
                if not same:
                    move(following, (k, True), mass, 1)
                move(following, (k, False), mass, k-(1 if same else 2))
                move(following, (k+1, False), mass, 1)
            current = following
        start = {k: mass for (k, same), mass in current.items() if same == (length == 1)}
    return {k: mass.count for k, mass in start.items()}


def cnf_for(bits, d, seed):
    r = len(bits)
    cnf = seed.rgs_cnf(r)
    added = 0
    for i, bit in enumerate(bits):
        j = (i+d) % r
        term = seed.add_same(cnf, i+1, j+1)
        cnf.clauses.append((term if bit else -term,))
        added += 2*min(i+1,j+1)-1
    assert cnf.variables == (3*r*r-r)//2 + added
    assert len(cnf.clauses) == 4*r*r-3*r + 3*added + r
    assert max(map(len, cnf.clauses)) <= 3
    return cnf


def test_source(seed):
    sources = seed.source_pins()
    base = seed.brc_block_count_distribution(6)
    assert sum(h.count for h in base.values()) == 203
    return sources


def finite_proofs(seed):
    stats = Counter()
    cache = {}
    for r in range(2, 9):
        words = list(seed.rgs_sequences(r))
        for d in range(1,r):
            families = defaultdict(Counter)
            for word in words:
                families[observation(word,d)][max(word)] += 1
                stats['rgs_observations'] += 1
            g = gcd(r,d)
            assert len(families) == (2**(r//g)-r//g)**g
            for bits in product((False,True),repeat=r):
                parts = components(bits,d)
                stats['binary_patterns'] += 1
                if parts is None:
                    assert bits not in families
                    continue
                if parts not in cache:
                    cache[parts] = brc_blocks(parts,seed)
                    assert cache[parts] == chromatic_blocks(parts)
                assert cache[parts] == families[bits]
                stats['realized_patterns'] += 1
            assert sum(sum(seed.falling_factorial(r,k)*n for k,n in tab.items())
                       for tab in families.values()) == r**r
    for r in range(2,5):
        for d in range(1,r):
            for bits in product((False,True), repeat=r):
                cnf = cnf_for(bits,d,seed)
                result = Counter()
                for mask in range(1<<len(cnf.primary)):
                    val = seed.extend_assignment(cnf,mask)
                    word = seed.decode_if_rgs(cnf,val,r)
                    truth = word is not None and observation(word,d)==bits
                    assert seed.satisfies(cnf,val)==truth
                    if truth:
                        result[max(word)] += 1
                    stats['cnf_primary_assignments'] += 1
                parts = components(bits,d)
                assert result == ({} if parts is None else cache[parts])
                stats['fully_enumerated_cnfs'] += 1
    return dict(stats)


def completion_witness(bits, d):
    """Explicitly test the indispensability of each missing pair at the discrete quotient."""
    n=len(bits)
    parent=list(range(n))
    def find(i):
        while parent[i]!=i:
            i=parent[i]
        return i
    for i,same in enumerate(bits):
        if same:
            parent[find(i)]=find((i+d)%n)
    labels=[find(i) for i in range(n)]
    assert observation(labels,d)==bits
    reps=sorted(set(labels))
    forbidden={tuple(sorted((labels[i],labels[(i+d)%n]))) for i in range(n) if not bits[i]}
    witnesses=0
    for a,b in combinations(reps,2):
        if (a,b) in forbidden:
            continue
        altered=[a if x==b else x for x in labels]
        assert observation(altered,d)==bits
        changes=[(u,v) for u,v in combinations(reps,2)
                 if (labels[u]==labels[v])!=(altered[u]==altered[v])]
        assert changes==[(a,b)]
        witnesses+=1
    parts=components(bits,d)
    edges=sum(0 if t==1 else 1 if t==2 else t for t in parts)
    assert witnesses==comb(sum(parts),2)-edges
    return witnesses


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,required=True)
    args=ap.parse_args()
    seed=load_seed(args.repo)
    sources=test_source(seed)
    seed.BRC_CALLS.clear()
    counters=finite_proofs(seed)
    queries=0
    for r in range(2,9):
        for d in range(1,r):
            for bits in product((False,True),repeat=r):
                if components(bits,d):
                    queries+=completion_witness(bits,d)
    example_bits=tuple(c=="1" for c in "100010101010")
    parts=components(example_bits,3)
    assert parts
    h=brc_blocks(parts,seed)
    formula=chromatic_blocks(parts)
    assert h==formula
    q=cnf_for(example_bits,3,seed)
    scale_runs=[]
    for r,d in ((48,8),(64,1),(120,20)):
        bits=(False,)*r
        parts_large=components(bits,d)
        before=seed.BRC_CALLS.copy()
        blocks=brc_blocks(parts_large,seed)
        assert blocks==chromatic_blocks(parts_large)
        colouring=sum(n*seed.falling_factorial(r,k) for k,n in blocks.items())
        g=gcd(r,d); length=r//g
        assert colouring==((r-1)**length+(-1)**length*(r-1))**g
        scale_runs.append({"r":r,"d":d,"pattern":"all different","reachable_block_counts":len(blocks),
                           "partition_count_bits":sum(blocks.values()).bit_length(),"static_colour_bits":colouring.bit_length(),
                           "sha256_decimal_partition_count":hashlib.sha256(str(sum(blocks.values())).encode()).hexdigest(),
                           "positive_histogram_calls":dict(seed.BRC_CALLS-before)})
    output={"source_commit": COMMIT,"seed_path":str(SEED),"seed_git_blob":BLOB,"production_source_pins":sources,
            "scale_runs":scale_runs,"verified_counts":counters,"missing_pair_witnesses":queries,
            "positive_histogram_calls_excluding_seed_baseline":dict(seed.BRC_CALLS),
            "example":{"r":len(example_bits),"d":3,"pattern":"".join(str(int(x)) for x in example_bits),
                       "quotient_components":parts,"exact_block_histogram":h,"partitions":sum(h.values()),
                       "static_colours":sum(n*seed.falling_factorial(len(example_bits),k) for k,n in h.items()),
                       "extra_same_queries":completion_witness(example_bits,3),"cnf_variables":q.variables,
                       "cnf_clauses":len(q.clauses)}}
    print(json.dumps(output,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
