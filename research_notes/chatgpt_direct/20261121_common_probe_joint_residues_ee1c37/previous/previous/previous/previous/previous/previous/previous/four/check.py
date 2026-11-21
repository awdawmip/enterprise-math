"""Verify every history and every menu of the new four-component partition."""
from collections import Counter, defaultdict
from itertools import combinations, product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
POINTS = list(product(range(5), repeat=4))


def shift(index, t):
    x = POINTS[index]
    result = 0
    for value in x:
        result = 5 * result + (value+t) % 5
    return result


def verify():
    data = json.loads((HERE / "certificate.json").read_text())
    groups = []
    seen = set()
    for template in data["templates"]:
        for t in range(5):
            g = [shift(i,t) for i in template]
            assert seen.isdisjoint(g) and len(g) == len(set(g))
            seen.update(g)
            groups.append(g)
    for g in data["remainder"]:
        assert seen.isdisjoint(g) and len(g) == len(set(g))
        seen.update(g)
        groups.append(g)
    assert seen == set(range(625))
    for group in groups:
        blocks = [{i for i in group if POINTS[i][j] == a} for j in range(4) for a in range(5)]
        assert all(not x & y or x <= y or y <= x for x,y in combinations(blocks,2))

    labels = {i:c for c,g in enumerate(groups) for i in g}
    edge_pairs = list(combinations(range(5),2))
    cases = 0
    for menu in product(edge_pairs,repeat=4):
        observed = [{} for _ in groups]
        for i,p in enumerate(POINTS):
            active = sum(1 << j for j in range(4) if p[j] in menu[j])
            high = sum(1 << j for j in range(4) if p[j] == menu[j][1])
            observed[labels[i]].setdefault(active,set()).add(high)
        for situations in observed:
            for active, outputs in situations.items():
                assert len(outputs) <= 2
                if len(outputs) == 2:
                    a,b = outputs
                    assert (a ^ b) & active
        cases += 1
    u4 = len(groups)
    u8 = 8 * 5**5 + 5 * u4
    u12 = 7 * 5**9 + 65*u8
    return dict(four_histories=len(seen),four_messages=u4,full_menus=cases,
                history_menu_checks=625*cases, sizes=sorted(Counter(map(len,groups)).items()),
                eight_bound=u8,twelve_bound=u12)


if __name__ == "__main__":
    print(json.dumps(verify(),indent=2))
