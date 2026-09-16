"""Exact integer address check; no floating accuracy or novelty certificate."""
from itertools import product
from pathlib import Path
import json


def verify(path: Path) -> dict:
    w = json.loads(path.read_text())
    K = w['K']; p, q = w['generators']; normal = w['annihilator']
    dot = lambda a, b: sum(x*y for x, y in zip(a,b))
    cross = [p[1]*q[2]-p[2]*q[1],p[2]*q[0]-p[0]*q[2],p[0]*q[1]-p[1]*q[0]]
    assert cross == normal == [1,-7,6]
    assert dot(normal,p) == dot(normal,q) == 0
    cube = set(product(range(-K,K+1),repeat=3))
    plane = {k for k in cube if dot(normal,k) == 0}
    generated = {(7*a-6*b,a,b) for a,b in product(range(-K,K+1),repeat=2) if abs(7*a-6*b)<=K}
    assert plane == generated == {tuple(k) for k in w['modes']}
    assert len(plane) == w['retained_mode_count_including_zero'] == 33
    assert len(plane-{(0,0,0)}) == w['retained_nonzero_mode_count'] == 32
    in_box_pairs = 0
    for a,b in product(plane,repeat=2):
        c = tuple(x+y for x,y in zip(a,b))
        if c in cube:
            assert c in plane
            in_box_pairs += 1
    return {'status':'PASS_EXACT_INTEGER_LABEL_CHECK','retained_labels':len(plane),'ordered_pairs_checked':len(plane)**2,'ordered_pairs_landing_in_box':in_box_pairs,'zero_is_an_allowed_label_not_asserted_nonzero_amplitude':True,'certifies':'finite address enumeration and retained pair closure only','does_not_certify':['floating trajectory accuracy','continuum model','novelty','generic speedup']}


if __name__ == '__main__':
    print(json.dumps(verify(Path(__file__).with_name('lattice_witness.json')),indent=2))
