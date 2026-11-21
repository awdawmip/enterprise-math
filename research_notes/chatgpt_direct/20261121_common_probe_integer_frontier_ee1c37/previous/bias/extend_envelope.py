"""Exact cost/imbalance envelope, reusing the completed radius-1/5 exclusion."""
import argparse
import importlib.util
import json
import sys
import time
from fractions import Fraction
from itertools import product
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous-work', type=Path, required=True)
    parser.add_argument('--cap', type=int, default=11667)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    start = time.time()
    script = args.previous_work / 'bias/plan_extended.py'
    spec = importlib.util.spec_from_file_location('original_plan', script)
    plan = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(plan)
    print(json.dumps({'phase':'catalog_ready','elapsed':time.time()-start}), flush=True)
    cap = args.cap
    bounds, witnesses = {}, {}
    profiles = 0
    for sizes in plan.partitions(125, 11):
        full = sizes.count(13)
        if full >= 5:
            continue
        if sum(min(plan.minimum.get((s, embedded), 10000) for embedded in (0,1)) for s in sizes) > cap:
            continue
        levels = sorted(set(sizes))
        choices = [(0,) if s in (1,13) else range(sizes.count(s)+1) for s in levels]
        for counts in product(*choices):
            proper = tuple(s for s,n in zip(levels,counts) for _ in range(n))
            embedded = tuple(s for s,n in zip(levels,counts) for _ in range(sizes.count(s)-n))
            if len(proper) < 4 or (len(proper)==4 and sum(proper)<42):
                continue
            if any(sum(embedded[-k:]) > plan.mod.bias.MOTHER_UNIONS[k] for k in range(1,len(embedded)+1)):
                continue
            large = embedded.count(12) + full
            if large > 6:
                continue
            slots = [(s,0) for s in proper] + [(s,1) for s in embedded]
            if large == 6:
                slots[slots.index((12,1))] = (12,2)
            floor = sum(plan.minimum[key] for key in slots)
            if floor > cap:
                continue
            profiles += 1
            values = plan.profile_bounds(tuple(sorted(slots,reverse=True)), cap-floor)
            first = max(floor,11365 if full==4 else 11301)
            for cost in range(first,cap+1):
                imbalance = values[cost-floor]
                if imbalance > bounds.get(cost,-1):
                    bounds[cost] = imbalance
                    witnesses[cost] = [proper,embedded,floor]
    rows = []
    for cost, upper in sorted(bounds.items()):
        # Proven q=5 exclusion and C == A (mod 2) give 5t-d >= 2.
        allowed = min(upper,5*(cost-11292)+106)
        if allowed > 108:
            ratio = Fraction(cost-11292,allowed-108)
            rows.append((ratio,cost,upper,allowed,witnesses[cost]))
    rows.sort()
    radius = rows[0][0]
    tail = Fraction(cap+1-11292,1611-108)
    result = {'cap':cap,'profiles':profiles,'catalog_sha256':plan.checksum,
              'candidate_radius':str(radius),'tail_radius_lower_bound':str(tail),
              'limiting_pairs':[{'radius':str(r),'cost':c,'spectrum_upper_A':a,'allowed_upper_A':b,'profile':p}
                                for r,c,a,b,p in rows if r==radius],
              'first_candidates':[{'radius':str(r),'cost':c,'spectrum_upper_A':a,'allowed_upper_A':b}
                                  for r,c,a,b,p in rows[:30]],
              'difference_by_total':bounds,
              'used_geometric_lemma':'completed q=5 weighted exclusion; 5(C-11292)-(A-108)>=2',
              'endpoint_uniqueness':'not implied; equality candidates require geometric exclusion',
              'elapsed_seconds':time.time()-start}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='difference_by_total'},indent=2),flush=True)


if __name__ == '__main__':
    main()
