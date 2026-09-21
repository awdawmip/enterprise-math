"""Guarded one-digit lifting of fixed-matching Heartbeat frame symmetries.

Exact local rational arithmetic; affine F_p solution families, not enumerated
ambient GL6 groups. Frames are analysis bases, not primitive native motions.
A matching of individually weighted atoms is a sufficient kernel certificate,
not the most general mass-row germ stabilizer. Every accepted frame is still
checked by the inherited full row certificate before probabilistic use.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from itertools import product

from .brc_transport import matrix, mm, inv, sm
from .heartbeat_switching_carry import _prime, _minimum, linear_carry_spread


def _nat(n, positive=False):
    if type(n) is not int or n < int(positive):
        raise ValueError('integer outside declared nonnegative/positive domain')
    return n


def _mod(x, modulus):
    x = F(x)
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def _rows_mod(a, modulus):
    return tuple(tuple(_mod(x, modulus) for x in row) for row in a)


def _flat(a):
    return tuple(x for row in a for x in row)


def _subtract(a, b):
    return tuple(tuple(x-y for x,y in zip(r,s)) for r,s in zip(a,b))


def _shape(a, dim=None):
    a = matrix(a)
    n = len(a)
    if n == 0 or n > 6 or any(len(row) != n for row in a) or (dim is not None and n != dim):
        raise ValueError('square matrices of one declared dimension in 1..6 required')
    return a


def _normalize_frame(a, p, depth):
    a = _shape(a)
    if _minimum(a,p) < 0 or _minimum(inv(a),p) < 0:
        raise ValueError('frame must preserve the standard p-lattice')
    modulus = p**depth
    values = _flat(_rows_mod(a,modulus))
    pivot = next(i for i,x in enumerate(values) if x%p)
    unit = pow(values[pivot],-1,modulus)
    vals = tuple(x*unit%modulus for x in values)
    n = len(a)
    return tuple(tuple(vals[i*n:(i+1)*n]) for i in range(n)), pivot


@dataclass(frozen=True)
class LinearLiftSpace:
    prime: int
    coefficients: tuple
    rhs: tuple
    rank: int
    particular: tuple | None
    basis: tuple
    obstruction: tuple | None

    @property
    def count(self):
        return 0 if self.particular is None else self.prime**len(self.basis)

    def verify(self):
        a,b,p = self.coefficients,self.rhs,self.prime
        dot=lambda x,y: sum(u*v for u,v in zip(x,y))%p
        if self.particular is None:
            y=self.obstruction
            if y is None or len(y)!=len(a) or any(dot(y,col) for col in zip(*a)) or dot(y,b)==0:
                raise ValueError('invalid no-lift obstruction')
        else:
            if any(dot(row,self.particular)!=v for row,v in zip(a,b)):
                raise ValueError('invalid particular lift')
            if any(dot(row,z) for z in self.basis for row in a):
                raise ValueError('invalid homogeneous correction')
        # Re-solving certifies rank, independence and exhaustiveness, not just soundness.
        if solve_modular_linear(a,b,p) != self:
            raise ValueError('noncanonical or incomplete affine-space certificate')
        return True

    def point(self, parameters=()):
        if self.particular is None:
            raise ValueError('NO_LIFT')
        parameters=tuple(parameters)
        if len(parameters)!=len(self.basis) or any(type(x) is not int or not 0<=x<self.prime for x in parameters):
            raise ValueError('one finite-field coefficient per free direction required')
        return tuple((x+sum(c*z[i] for c,z in zip(parameters,self.basis)))%self.prime
                     for i,x in enumerate(self.particular))


def solve_modular_linear(coefficients, rhs, prime):
    """Exact RREF, affine solution basis, or yA=0 with yb !=0."""
    p=_prime(prime)
    a=tuple(tuple(_mod(v,p) for v in row) for row in coefficients)
    b=tuple(_mod(v,p) for v in rhs)
    if not a or not a[0] or len(b)!=len(a) or any(len(row)!=len(a[0]) for row in a):
        raise ValueError('nonempty rectangular system required')
    m,n=len(a),len(a[0])
    rows=[list(row)+( [v] ) for row,v in zip(a,b)]
    transform=[[int(i==j) for j in range(m)] for i in range(m)]
    pivots=[]
    for j in range(n):
        k=len(pivots)
        found=next((i for i in range(k,m) if rows[i][j]),None)
        if found is None: continue
        rows[k],rows[found]=rows[found],rows[k]
        transform[k],transform[found]=transform[found],transform[k]
        u=pow(rows[k][j],-1,p)
        rows[k]=[x*u%p for x in rows[k]]
        transform[k]=[x*u%p for x in transform[k]]
        for i in range(m):
            if i!=k and rows[i][j]:
                c=rows[i][j]
                rows[i]=[(x-c*y)%p for x,y in zip(rows[i],rows[k])]
                transform[i]=[(x-c*y)%p for x,y in zip(transform[i],transform[k])]
        pivots.append(j)
    for i in range(len(pivots),m):
        if rows[i][-1]:
            return LinearLiftSpace(p,a,b,len(pivots),None,(),tuple(transform[i]))
    x=[0]*n
    for i,j in enumerate(pivots): x[j]=rows[i][-1]
    basis=[]
    for j in range(n):
        if j in pivots: continue
        z=[0]*n;z[j]=1
        for i,k in enumerate(pivots): z[k]=-rows[i][j]%p
        basis.append(tuple(z))
    return LinearLiftSpace(p,a,b,len(pivots),tuple(x),tuple(basis),None)


@dataclass(frozen=True)
class GermLiftProblem:
    prime: int
    sources: tuple
    targets: tuple
    guard: int
    dimension: int

    @classmethod
    def build(cls, sources, targets, prime):
        p=_prime(prime)
        src=tuple(_shape(a) for a in sources);dst=tuple(_shape(a) for a in targets)
        if not src or len(src)!=len(dst): raise ValueError('nonempty matched action tuples required')
        n=len(src[0])
        def primitive(a):
            _shape(a,n);inv(a)
            return sm(F(p)**(-_minimum(a,p)),a)
        src,dst=tuple(map(primitive,src)),tuple(map(primitive,dst))
        c=max(linear_carry_spread(a,p) for a in src+dst)
        return cls(p,src,dst,c,n)

    @property
    def digest(self):
        return sha256(repr(self).encode()).hexdigest()

    def seed(self, frame, multipliers, precision):
        """m=precision is action-germ depth; frame is stored at m+guard."""
        m=_nat(precision,True);p=self.prime
        s,pivot=_normalize_frame(_shape(frame,self.dimension),p,m+self.guard)
        u=tuple(_mod(v,p**m) for v in multipliers)
        if len(u)!=len(self.sources) or any(v%p==0 for v in u):
            raise ValueError('one p-adic unit scalar per matched action required')
        for a,b,v in zip(self.sources,self.targets,u):
            residual=_subtract(mm(mm(sm(p**self.guard,inv(b)),matrix(s)),a),sm(p**self.guard*v,matrix(s)))
            if any(_mod(x,p**(m+self.guard)) for x in _flat(residual)):
                raise ValueError('seed fails action-germ congruence at its declared precision')
        return GermLiftSeed(self.digest,m,s,u,pivot)


@dataclass(frozen=True)
class GermLiftSeed:
    problem_digest: str
    precision: int
    frame: tuple
    multipliers: tuple
    pivot: int


@dataclass(frozen=True)
class GermLiftCertificate:
    problem: GermLiftProblem
    seed: GermLiftSeed
    space: LinearLiftSpace

    def verify(self):
        if lift_germ_seed(self.problem,self.seed)!=self:
            raise ValueError('seed or equation binding mismatch')
        return self.space.verify()

    def instantiate(self, parameters=()):
        z=self.space.point(parameters)
        n,p,m,c=self.problem.dimension,self.problem.prime,self.seed.precision,self.problem.guard
        f=tuple(tuple(self.seed.frame[i][j]+p**(m+c)*z[n*i+j] for j in range(n)) for i in range(n))
        u=tuple(x+p**m*z[n*n+k] for k,x in enumerate(self.seed.multipliers))
        return self.problem.seed(f,u,m+1)

    def all_lifts(self, *, limit=4096):
        _nat(limit)
        if self.space.count>limit: raise ValueError('LIFT_LIMIT: affine family retained, not enumerated')
        return tuple(self.instantiate(c) for c in product(range(self.problem.prime),repeat=len(self.space.basis))) if self.space.count else ()


def lift_germ_seed(problem, seed):
    """Complete next-digit lifts for ONE declared atom matching.

    At germ depth m, frame depth is m+C. Frame corrections use p^(m+C),
    while projective unit scalars use p^m. These are NOT interchangeable.
    """
    if not isinstance(problem,GermLiftProblem) or not isinstance(seed,GermLiftSeed):
        raise TypeError('typed problem and seed required')
    if problem.seed(seed.frame,seed.multipliers,seed.precision)!=seed:
        raise ValueError('invalid or foreign seed')
    p,n,c,m=problem.prime,problem.dimension,problem.guard,seed.precision
    s=matrix(seed.frame);a_rows=[];rhs=[];atoms=len(problem.sources)
    for e,(a,b,u) in enumerate(zip(problem.sources,problem.targets,seed.multipliers)):
        left=sm(p**c,inv(b))
        residual=_subtract(mm(mm(left,s),a),sm(p**c*u,s))
        for i in range(n):
            for j in range(n):
                row=[_mod(left[i][k]*a[l][j]-(p**c*u if i==k and j==l else 0),p)
                     for k in range(n) for l in range(n)]
                row += [(-_mod(s[i][j],p) if q==e else 0) for q in range(atoms)]
                a_rows.append(tuple(row));rhs.append(_mod(-residual[i][j]/p**(m+c),p))
    a_rows.append(tuple(int(i==seed.pivot) for i in range(n*n+atoms)));rhs.append(0)
    return GermLiftCertificate(problem,seed,solve_modular_linear(a_rows,rhs,p))


def lift_seed_family(problem, seeds, target_precision, *, max_seeds=4096):
    """Breadth-first exact fixed-matching lifts. Budget failure never means no lift."""
    seeds=tuple(seeds);target_precision=_nat(target_precision,True);_nat(max_seeds,True)
    if not seeds: return {'status':'NO_LIFTS','seeds':(), 'layers':()}
    if len({s.precision for s in seeds})!=1 or seeds[0].precision>target_precision:
        raise ValueError('equal starting precisions not exceeding target required')
    for seed in seeds:
        if problem.seed(seed.frame,seed.multipliers,seed.precision)!=seed:
            raise ValueError('invalid or foreign seed')
    current=tuple(dict.fromkeys(seeds));layers=[]
    if len(current)>max_seeds:
        return {'status':'LIFT_LIMIT','seeds':current,'layers':()}
    while current[0].precision<target_precision:
        certs=tuple(lift_germ_seed(problem,s) for s in current)
        count=sum(c.space.count for c in certs)
        layers.append((current[0].precision,len(current),count))
        if count>max_seeds:
            return {'status':'LIFT_LIMIT','seeds':current,'layers':tuple(layers),'frontier_certificates':certs}
        current=tuple(s for c in certs for s in c.all_lifts(limit=max_seeds))
        if not current: return {'status':'NO_LIFTS','seeds':(),'layers':tuple(layers),'frontier_certificates':certs}
    return {'status':'COMPLETE','seeds':current,'layers':tuple(layers)}


def packet_matching_problem(packet, prime, atom_permutation):
    """Atom-bijective mass/port preservation is sufficient, not all row stabilizers."""
    from .heartbeat_carry_peak import _atoms
    atoms=_atoms(packet);pi=tuple(atom_permutation)
    if sorted(pi)!=list(range(len(atoms))): raise ValueError('a bijection of the actual atom table is required')
    for i,j in enumerate(pi):
        s,t,w,a,k=atoms[i];ss,tt,ww,b,kk=atoms[j]
        if (s,t,w*k)!=(ss,tt,ww*kk): raise ValueError('matching changes source, target or positive atom mass')
    return GermLiftProblem.build([a[3] for a in atoms],[atoms[j][3] for j in pi],prime)


def verify_lifted_peak_frame(packet, frame, prime, threshold):
    """Execute inherited full weighted-row test; no probability result from lift count."""
    from .heartbeat_peak_orbits import _row_equal
    from .heartbeat_carry_peak import _atoms
    p=_prime(prime);_nat(threshold,True)
    s=_shape(frame,6)
    if _minimum(s,p)<0 or _minimum(inv(s),p)<0: raise ValueError('nonintegral frame')
    atoms=_atoms(packet)
    for source in range(packet.state_count):
        row=tuple((t,w*k,a) for c,t,w,a,k in atoms if c==source)
        moved=tuple((t,w,mm(mm(s,a),inv(s))) for t,w,a in row)
        if not _row_equal(moved,row,p,threshold,'threshold'):
            raise ValueError('inherited weighted action-row certificate rejected frame')
    return True
