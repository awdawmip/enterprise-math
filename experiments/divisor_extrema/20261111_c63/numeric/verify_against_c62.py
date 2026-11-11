"""Cross-check C63 certificates against a user-supplied C62 reproduction zip.

  python3 verify_against_c62.py PATH/prime_quantum_schedule_extrema_c62.zip
"""
import argparse
from fractions import Fraction
from functools import lru_cache
import json
from pathlib import Path
import sys
import tempfile
from zipfile import ZipFile

from certify_schedules import apply_map, block_maps, compute, derivative_lower, terminal_lower


def pair(value):
    return Fraction(*map(int,value))


def verify(archive_path):
    checked_states = block_checks = enumerated = 0
    with tempfile.TemporaryDirectory() as directory, ZipFile(archive_path) as archive:
        root = Path(directory,"prime_quantum_schedule_extrema_c62")
        for member in archive.namelist():
            if member.endswith(".py") and member.startswith(root.name + "/"):
                dest = Path(directory,member).resolve()
                if not dest.is_relative_to(root):
                    raise ValueError("Unexpected archive path")
                dest.parent.mkdir(parents=True,exist_ok=True)
                dest.write_bytes(archive.read(member))
        sys.path.insert(0,str(root))
        import schedule_extrema as c62
        inherited = json.loads(archive.read(root.name+"/results/enumeration_frontier.json"))

        @lru_cache(None)
        def cached_blocks(r,c):
            return list(block_maps(r,c))

        for row, old in zip(compute(10),inherited,strict=True):
            k = row['k']
            assert k == old['k']
            exact_min = Fraction(int(old['min']['numerator']),int(old['min']['denominator']))
            assert old['min_words']==[[1]*(k-1)+[0,0]]
            assert exact_min == pair(row['exact_ahead_delta']) < pair(row['exact_competitor_lower'])
            assert exact_min == c62.delta(c62.ahead_allocation(k))
            checked_states+=1
            for r in range(1,k):
                for c in range(2,k+2):
                    for m,(a,b,h) in enumerate(cached_blocks(r,c)):
                        q0,q1,q2 = c62.block_weights(m,r,c)
                        assert Fraction(a,h) == 7*q0/q2
                        assert Fraction(b,h) == q1/q2
                        block_checks+=1
            if k>7:
                continue
            all_bounds = []
            exact_competitor = None
            for path in c62.compositions(k-1,k+1):
                c = k+1-path[0]
                lower = Fraction(1)
                u,v = Fraction(1),Fraction(0)
                for r,m in zip(range(k-1,0,-1),path[1:-1],strict=True):
                    mobius = cached_blocks(r,c)[m]
                    u,v = apply_map(mobius,u),apply_map(mobius,v)
                    lower *= derivative_lower(mobius)
                    c -= m
                lower *= terminal_lower(c)
                actual = c62.delta(path)
                assert lower<=actual
                if path != tuple(old['min_words'][0]):
                    all_bounds.append(lower)
                    exact_competitor = min(actual,exact_competitor) if exact_competitor is not None else actual
                enumerated+=1
            assert min(all_bounds)==pair(row['exact_competitor_lower'])<=exact_competitor
    return dict(c62_complete_frontiers_checked=checked_states,
                block_weight_ratio_checks_with_repetitions_across_k=block_checks,
                full_paths_checked_through_k7=enumerated)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive',type=Path)
    args=parser.parse_args()
    print(json.dumps(verify(args.archive),indent=2))
