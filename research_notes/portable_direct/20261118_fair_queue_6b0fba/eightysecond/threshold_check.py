#!/usr/bin/env python3
"""An exact quadratic-field certificate; no trajectories are generated."""
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path
from zipfile import ZipFile


@dataclass(frozen=True)
class Quadratic:
    a: F = F(0)
    b: F = F(0)

    def __add__(self, other):
        z = scalar(other)
        return Quadratic(self.a + z.a, self.b + z.b)

    __radd__ = __add__

    def __neg__(self):
        return Quadratic(-self.a, -self.b)

    def __sub__(self, other):
        return self + -scalar(other)

    def __rsub__(self, other):
        return scalar(other) + -self

    def __mul__(self, other):
        z = scalar(other)
        return Quadratic(self.a*z.a + 3*self.b*z.b, self.a*z.b + self.b*z.a)

    __rmul__ = __mul__

    def sign(self):
        if self.b == 0:
            return (self.a > 0) - (self.a < 0)
        if self.a == 0 or (self.a > 0) == (self.b > 0):
            return 1 if self.b > 0 else -1
        discr = self.a*self.a - 3*self.b*self.b
        assert discr != 0
        return ((discr > 0) - (discr < 0)) * (1 if self.a > 0 else -1)

    def __lt__(self, other):
        return (self - other).sign() < 0

    def pair(self):
        return [str(self.a), str(self.b)]


def scalar(x):
    return x if isinstance(x, Quadratic) else Quadratic(F(x))


def certify():
    half = scalar(F(1,2))
    s = Quadratic(F(0),F(1,2))  # positive sqrt(3)/2
    h = 1 - s
    radius_squared = Quadratic(F(2),F(-1))
    assert scalar(0)<h<half<s<scalar(1)
    assert s*s + half*half == scalar(1)
    assert h*h + half*half == radius_squared

    planes = []
    for i in (-1,1):
        planes += [(i,0,half),(0,i,half)]
        for j in (-1,1):
            planes.append((i,j,half+h))
    vertices = set()
    pairs_compared = 0
    for (a,b,c),(d,e,f) in combinations(planes,2):
        det = a*e-b*d
        if not det:
            continue
        scale = F(1,det)
        x = (e*c-b*f)*scale
        y = (a*f-d*c)*scale
        pairs_compared += 1
        if all((i*x+j*y-k).sign()<=0 for i,j,k in planes):
            vertices.add((x,y))
    expected = {(i*u,j*v) for u,v in permutations((h,half)) for i,j in product((-1,1),repeat=2)}
    assert vertices == expected and len(vertices)==8
    # Limits on the two open arcs bordering the positive y=1/2 line.
    arc_limits = ((s-1,half),(s-1,half-1))
    assert all(p in expected for p in arc_limits)
    assert all(x*x+y*y==radius_squared for x,y in vertices)
    # y^2(1-y^2) - 3/16 = (y^2 - 1/4)(3/4 - y^2).
    factor_coeff = [F(-1,4)*F(3,4), F(3,4)+F(1,4),-1]
    assert factor_coeff == [F(-3,16),1,-1]
    # For b with |b1| >= |b2| >= 0 the support is (1/2)|b1| + h|b2|.
    # Express any such b as u(1,0)+v(1,1) with u,v >= 0 and check both rays.
    extrema = []
    peak = (half,h)
    for bx,by in ((1,0),(1,1)):
        best = max(bx*x+by*y for x,y in vertices)
        assert bx*peak[0]+by*peak[1] == best
        extrema.append(best.pair())

    # Static rational open-cell witnesses with positive angular neighbourhoods.
    axis = (F(1),F(0))
    corner = (F(20,29),F(21,29))
    labels = set()
    for point in (axis,corner):
        assert sum(v*v for v in point) == 1
        for u,v in permutations(point):
            for a,b in product((-1,1),repeat=2):
                x,y = a*u,b*v
                assert abs(x)!=F(1,2) and abs(y)!=F(1,2)
                labels.add(((x+F(1,2))//1,(y+F(1,2))//1))
    assert labels==set(product((-1,0,1),repeat=2))-{(0,0)}
    # In Z[i], -beta+(1-i)gamma=1. Neither Gaussian prime is a unit.
    beta = (2,-1)
    gamma = (2,1)
    re, im = gamma
    bezout = (-beta[0]+re+im, -beta[1]+im-re)
    assert bezout==(1,0) and all(x*x+y*y==5 for x,y in (beta,gamma))
    assert (5%2)==1
    # Original correction is one exact matrix-vector product, not an orbit run.
    re, im = (F(2,10), F(-1,10))
    correction = ((3*re-4*im)/5,(4*re+3*im)/5)
    assert correction==(F(1,5),F(1,10))
    return {'field':'Q(sqrt(3)); entries [a,b] denote a+b*sqrt(3)',
            'eight_halfspaces':[[a,b,c.pair()] for a,b,c in planes],
            'nonparallel_boundary_pairs':pairs_compared,
            'vertices':[[x.pair(),y.pair()] for x,y in sorted(vertices)],
            'common_squared_radius':radius_squared.pair(),
            'arc_endpoint_one_sided_residues':[[a.pair(),b.pair()] for a,b in arc_limits],
            'first_octant_polynomial_identity_ascending':[str(c) for c in factor_coeff],
            'support_values_on_positive_ordered_cone_rays':extrema,
            'open_cells_on_each_periodic_phase':sorted(labels),
            'static_open_cell_witnesses':[[str(v) for v in p] for p in (axis,corner)],
            'gaussian_bezout_result':bezout,'corrected_matrix_product':[str(v) for v in correction],
            'scientific_trajectory_runs':0,'native_BRC_sensor_calls':0}


def verify_local_original(archive):
    expected='1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d'
    if sha256(archive.read_bytes()).hexdigest()!=expected:
        raise ValueError('Original archive fingerprint differs from the published task.')
    members={
        'CONVERSATION_FRONTIER.md':'ef087c9039d82dc4d58614e0fc091a4dd96020760d80e45591c7b0b74a16b807',
        'evidence/rational_cell_continuation/INFINITE_OBSERVATION_AND_CERTIFIED_ZERO_TAIL_20261002.md':
            '28c1cf7d19e12fe27fd8c46e12bdfb74d15776ba4de30c9c32808237d2b09638',
        'evidence/rational_cell_continuation/INFINITE_OBSERVATION_PROOF_RECEIPT_20261002.json':
            'be5286e3f225dad348079ce53bc3a66deffed06276100a4a3786e02901719a63',
        'taskbooks/P20.md':'c4bee7286e0ee510bd4fbcd83df7d8d6a87e7330a253bb185d81fa06027bb6c9',
    }
    with ZipFile(archive) as z:
        for path,digest in members.items():
            assert sha256(z.read(path)).hexdigest()==digest
    return {'registered_archive_fingerprint':expected,'verified_members':len(members),
            'source_reproduced':False}


def main():
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--out',type=Path)
    cli.add_argument('--intake',type=Path,help='Optional registered original in local storage.')
    args=cli.parse_args()
    result={'finite_algebra':certify()}
    if args.intake:
        result['source_verification']=verify_local_original(args.intake)
    data=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.out:
        args.out.write_text(data,encoding='utf-8')
    else:
        print(data,end='')

if __name__=='__main__':
    main()
