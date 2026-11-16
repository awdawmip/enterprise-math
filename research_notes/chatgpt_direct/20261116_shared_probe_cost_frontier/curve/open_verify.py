"""Check feasible tables and the label-count relaxation for unresolved middle budgets."""
from itertools import combinations
import json
import sys

from verify import ROOT, lower

sys.path.insert(0, str(ROOT.parent / 'bounds'))
from cyclic11 import observations, class_cost

bad, pair = observations()
out = {}
for label, entry in json.loads((ROOT / 'open_witnesses.json').read_text()).items():
    m = int(label)
    groups = entry['groups']
    assert len(groups) == m and all(groups)
    assert sorted(i for g in groups for i in g) == list(range(125))
    for group in groups:
        assert not any(bad[a][b] >> c & 1 for a, b, c in combinations(group, 3))
    feasible = sum(class_cost(group, pair) for group in groups)
    assert feasible == entry['cost']
    out[m] = [lower(125, m), feasible]
print(json.dumps(out, indent=2, sort_keys=True))
