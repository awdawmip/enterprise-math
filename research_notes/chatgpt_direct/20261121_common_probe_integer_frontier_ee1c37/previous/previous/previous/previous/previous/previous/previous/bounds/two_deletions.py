"""Check every two-point deletion of each maximal class against the complete cheap-class counts."""
from collections import Counter
from itertools import combinations
import json
from cyclic11 import observations, class_cost, setbits
from geometry import inventory, linear_actions

def run():
    bad, obs = observations()
    parents, centers = inventory(linear_actions(), bad, obs)
    costs = {}
    for row in parents:
        for i,j in combinations(setbits(row),2):
            child = row ^ (1<<i) ^ (1<<j)
            assert child not in costs
            costs[child] = class_cost(list(setbits(child)),obs)
    histogram = dict(sorted(Counter(costs.values()).items()))
    # Independent complete size/cost enumeration, included in replay.py.
    assert histogram=={936:4500,944:12000,960:3000}
    return dict(parent_classes=len(parents),two_point_deletions=len(costs),cost_histogram=histogram)

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
