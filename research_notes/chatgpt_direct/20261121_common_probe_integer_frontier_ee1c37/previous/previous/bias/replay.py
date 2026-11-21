"""Certify the common-action bias interval using exact native class costs."""
from collections import defaultdict
from fractions import Fraction
from functools import cache
from itertools import product
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse
import hashlib
import json
import os
import subprocess
import sys

HERE = Path(__file__).resolve().parent
OPTIMAL = 11292
OPTIMAL_DIFFERENCE = 108
FIRST_OTHER = 11301
LAST_EXPLICIT = 11350
MOTHER_UNIONS = (0, 13, 26, 39, 52, 65, 78, 85)


def census(previous):
    third = previous / 'previous/previous/previous'
    second = third / 'previous'
    os.environ['NATIVE_PROBE_PREVIOUS'] = str(second)
    sys.path[:0] = [str(second / 'bounds'), str(third / 'group')]
    from cyclic11 import observations
    from geometry import inventory, linear_actions
    from prior_bounds import observation_file

    forbidden, menus = observations()
    parents, centers = inventory(linear_actions(), forbidden, menus)
    assert len(parents) == len(centers) == 250
    with TemporaryDirectory() as tmp:
        temp = Path(tmp)
        observation_file(temp / 'menus')
        (temp / 'parents').write_text(''.join(f'{m%(2**64)} {m>>64}\n' for m in parents))
        subprocess.run(['c++', '-std=c++20', '-O3', '-mpopcnt', HERE/'menu.cpp', '-o', temp/'enumerate'], check=True)
        run = subprocess.run([temp/'enumerate', temp/'menus', temp/'parents'], text=True, capture_output=True, check=True)
    visits = dict(tuple(map(int, line.split())) for line in run.stderr.splitlines())
    catalog = defaultdict(dict)
    for line in run.stdout.splitlines():
        size, embedded, price, difference = map(int, line.split())
        catalog[size, embedded][price] = difference
        assert difference <= price and (difference-price) % 2 == 0
    assert catalog[12, 1] == {1104: 0, 1116: 0}
    return catalog, visits, hashlib.sha256(run.stdout.encode()).hexdigest()


def solve(previous):
    sys.path.insert(0, str(previous/'mothers'))
    from costs import partitions
    catalog, visits, checksum = census(previous)
    types = list(catalog)
    least = {key: min(prices) for key, prices in catalog.items()}
    peak = {key: max(prices.values()) for key, prices in catalog.items()}

    @cache
    def difference_cap(points, classes):
        if classes == 0:
            return 0 if points == 0 else -100000
        return max((peak[key]+difference_cap(points-key[0], classes-1)
                    for key in types if classes-1 <= points-key[0] <= 13*(classes-1)),
                   default=-100000)

    global_cap = difference_cap(125, 11)
    # (12,2) is a 12-point set made by deleting an outer point. The class is
    # also available under (12,1). Type 2 is used only when a puncture is forced.
    catalog[12, 2] = {1116: 0}
    least[12, 2] = 1116

    @cache
    def max_by_slack(profile, slack):
        # An unattained exact price has value -1. Nonnegative entries bound
        # |sum of signed differences| from above by their absolute sum.
        if not profile:
            return [0]+[-1]*slack
        key = profile[-1]
        smaller = max_by_slack(profile[:-1], slack)
        values = [-1]*(slack+1)
        for c,d in catalog[key].items():
            delta = c-least[key]
            if delta > slack:
                continue
            for n in range(slack+1-delta):
                if smaller[n] >= 0 and smaller[n]+d > values[n+delta]:
                    values[n+delta] = smaller[n]+d
        return values

    bounds = {}
    certificate = {}
    profiles = 0
    for sizes in partitions(125,11):
        full = sizes.count(13)
        # All five-full solutions are already classified; six or more are impossible.
        if full >= 5 or sum(min(least.get((s,e),10000) for e in (0,1)) for s in sizes)>LAST_EXPLICIT:
            continue
        sizes_used = sorted(set(sizes))
        choices = [(0,) if s in (1,13) else range(sizes.count(s)+1) for s in sizes_used]
        for counts in product(*choices):
            proper = [s for s,n in zip(sizes_used,counts) for _ in range(n)]
            embedded = [s for s,n in zip(sizes_used,counts) for _ in range(sizes.count(s)-n)]
            if len(proper)<4 or (len(proper)==4 and sum(proper)<42):
                continue
            if any(sum(embedded[-k:])>MOTHER_UNIONS[k] for k in range(1,len(embedded)+1)):
                continue
            large = embedded.count(12)+full
            if large>6:
                continue
            slots = [(s,0) for s in proper]+[(s,1) for s in embedded]
            floor = sum(least[t] for t in slots)
            if floor>LAST_EXPLICIT:
                continue
            profiles+=1
            for _ in range(max(0,large-5)):
                slots[slots.index((12,1))]=(12,2)
            profile=tuple(sorted(slots, reverse=True))
            floor=sum(least[t] for t in profile)
            if floor>LAST_EXPLICIT:
                continue
            values=max_by_slack(profile,LAST_EXPLICIT-floor)
            first=max(floor,11365 if full==4 else FIRST_OTHER)
            for price in range(first,LAST_EXPLICIT+1):
                d=values[price-floor]
                if d>bounds.get(price,-1):
                    bounds[price]=d
                    certificate[price]=profile
    limiting=min((Fraction(c-OPTIMAL,d-OPTIMAL_DIFFERENCE),c,d)
                 for c,d in bounds.items() if d>OPTIMAL_DIFFERENCE)
    radius,total,difference=limiting
    assert Fraction(LAST_EXPLICIT+1-OPTIMAL,global_cap-OPTIMAL_DIFFERENCE)>radius
    return dict(single_class_cases=sum(visits.values()), enumeration_visits=visits,
                single_class_catalog_sha256=checksum, global_difference_cap=global_cap,
                budget=LAST_EXPLICIT, size_and_embedding_profiles=profiles,
                difference_by_total=bounds, weighted_radius=str(radius),
                p_interval=[str((1-radius)/2),str((1+radius)/2)],
                limiting_relaxed_pair=[total,difference], limiting_slots=certificate[total])


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous', required=True, type=Path)
    previous=parser.parse_args().previous.resolve()
    result=solve(previous)
    canonical=json.dumps(result,indent=2,sort_keys=True)+'\n'
    receipt=HERE/'result.json'
    if receipt.exists():
        assert json.loads(canonical)==json.loads(receipt.read_text())
    print(canonical,end='')
