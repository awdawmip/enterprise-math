"""Frame-labeled, length-aware formal Schur extension of Weighted-BRC ports.

Pinned scalar law: src/enterprise_math/brc_recurrent_ports.py at
cc282835f44255b4d8c9895cfa131adfdd46a2db, blob24a7fd37e274c067eaf560036f51fae80baa1644.
This extension uses formal z-adic properness, not real numerical stability.
"""
from dataclasses import dataclass
import sympy as s


@dataclass(frozen=True)
class FormalPortSignature:
    boundary_labels: tuple
    effective: s.ImmutableMatrix
    hidden_determinant: s.Expr
    z: s.Symbol
    specialization_guards: tuple = ()


def schur_ports(matrix, labels, internal_labels, z):
    """Retain exact labeled boundary frames and hidden determinant.

    Input entries must be exact rational functions over rational coefficients
    and symbolic parameters, regular and zero at z=0. No numerical floats.
    Explicit invalid partitions and hidden singular specializations fail closed.
    """
    T = s.Matrix(matrix)
    if T.rows<1 or T.rows!=T.cols or not isinstance(z,s.Symbol):
        raise ValueError('nonempty square matrix and formal symbol required')
    labels = tuple(labels)
    if len(labels)!=T.rows or len(set(labels))!=len(labels):
        raise ValueError('one distinct hashable label per matrix state required')
    internal_labels = tuple(internal_labels)
    if not internal_labels or len(set(internal_labels))!=len(internal_labels):
        raise ValueError('nonempty distinct internal labels required')
    if not set(internal_labels)<set(labels):
        raise ValueError('internal labels must be a proper state subset')
    guards = set()
    for value in T:
        if value.has(s.Float) or not value.is_rational_function(*sorted(value.free_symbols|{z},key=str)):
            raise ValueError('exact rational function entries required')
        value = s.cancel(value)
        num,den = s.fraction(value)
        generators = sorted(value.free_symbols|{z},key=str)
        try:
            s.Poly(num,*generators,domain=s.QQ)
            s.Poly(den,*generators,domain=s.QQ)
        except (s.PolynomialError,s.CoercionFailed) as exc:
            raise ValueError('coefficients must lie in the rational parameter field') from exc
        if s.simplify(den.subs(z,0))==0 or s.simplify(num.subs(z,0))!=0:
            raise ValueError('matrix must be regular and zero at z=0')
        guard = s.factor(den.subs(z,0))
        if guard.free_symbols:
            guards.add(guard)
    I = [i for i,x in enumerate(labels) if x in set(internal_labels)]
    B = [i for i,x in enumerate(labels) if x not in set(internal_labels)]
    A,X,Y,D = T.extract(I,I),T.extract(I,B),T.extract(B,I),T.extract(B,B)
    H = s.eye(len(I))-A
    detH = s.factor(H.det())
    if detH==0:
        raise ValueError('singular hidden block')
    W = (D+Y*H.inv()*X).applyfunc(s.cancel)
    return FormalPortSignature(tuple(labels[i] for i in B),s.ImmutableMatrix(W),detH,z,tuple(sorted(guards,key=str)))


def same_labeled_ports(left,right, *, absolute_determinant=False, domain_sensitive=True):
    """Label-sensitive observer equivalence, not order-only matrix equality."""
    if not isinstance(left,FormalPortSignature) or not isinstance(right,FormalPortSignature):
        raise TypeError('formal port signatures required')
    if left.z != right.z or set(left.boundary_labels)!=set(right.boundary_labels):
        return False
    if domain_sensitive and set(left.specialization_guards)!=set(right.specialization_guards):
        return False  # conservative domain comparison, not a minimal zero-locus algorithm
    p = [right.boundary_labels.index(x) for x in left.boundary_labels]
    R = right.effective.extract(p,p)
    if any(s.cancel(x)!=0 for x in left.effective-R):
        return False
    return not absolute_determinant or s.cancel(left.hidden_determinant-right.hidden_determinant)==0


def specialize_ports(signature,replacements):
    """Exact partial parameter specialization, preserving original pole guards.

    A canceled denominator in the reduced port expression is not permission
    to specialize the original branch system through its pole.
    """
    from fractions import Fraction
    if not isinstance(signature,FormalPortSignature):
        raise TypeError('formal signature required')
    subs = {}
    for key,value in replacements.items():
        if not isinstance(key,s.Symbol) or key==signature.z:
            raise ValueError('only parameter symbols, not z, may be specialized')
        if isinstance(value,bool) or not isinstance(value,(int,Fraction,s.Rational)):
            raise TypeError('exact rational parameter value required')
        subs[key] = s.Rational(value.numerator,value.denominator)
    guards = tuple(s.factor(g.subs(subs, simultaneous=True)) for g in signature.specialization_guards)
    if any(g==0 for g in guards):
        raise ValueError('specialization hits an original parameter-pole guard')
    W = signature.effective.applyfunc(lambda v:s.cancel(v.subs(subs,simultaneous=True)))
    D = s.cancel(signature.hidden_determinant.subs(subs,simultaneous=True))
    for v in list(W)+[D]:
        if v.has(s.zoo,s.nan,s.oo,-s.oo):
            raise ValueError('nonfinite specialization')
        if s.simplify(s.denom(v).subs(signature.z,0))==0:
            raise ValueError('specialization loses formal regularity')
    if D==0:
        raise ValueError('specialized hidden determinant is identically zero')
    return FormalPortSignature(signature.boundary_labels,s.ImmutableMatrix(W),D,signature.z,
                               tuple(g for g in guards if g.free_symbols))
