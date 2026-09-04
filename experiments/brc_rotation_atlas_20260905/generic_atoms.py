"""Extend the preceding BRC valuation-atom compiler to Q(parameters)[y].

Uses SymPy exact fraction-field polynomial gcd/squarefree arithmetic, not
irreducible factorization or numerical roots. Regular guards retain scalar
zeros/poles, coefficient denominators, atom discriminants, collisions and
optional endpoint contacts. Generic validity does not include guard zeros.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations
from typing import Iterable, Mapping
import sympy as s


def _exact(expr):
    out = s.sympify(expr)
    if out.has(s.Float):
        raise TypeError("exact rational-function coefficients required; no floats")
    return out


@dataclass(frozen=True)
class Atom:
    profile: tuple[int, ...]
    polynomial: s.Poly


@dataclass(frozen=True)
class Certificate:
    variable: s.Symbol
    parameters: tuple[s.Symbol, ...]
    scalars: tuple[s.Expr, ...]
    atoms: tuple[Atom, ...]
    refinement_gcd_calls: int = 0

    @property
    def field(self):
        return s.QQ.frac_field(*self.parameters) if self.parameters else s.QQ

    def reconstruct(self):
        return tuple(s.Poly(c*s.prod(a.polynomial.as_expr()**a.profile[i] for a in self.atoms),
                            self.variable,domain=self.field)
                     for i,c in enumerate(self.scalars))


def _setup(factors, variable, parameters):
    parameters = tuple(parameters)
    if not isinstance(variable,s.Symbol) or any(not isinstance(p,s.Symbol) for p in parameters):
        raise TypeError("variable/parameters must be symbols")
    if variable in parameters or len(set(parameters)) != len(parameters):
        raise ValueError("variable and distinct parameters must be disjoint")
    field = s.QQ.frac_field(*parameters) if parameters else s.QQ
    polys = tuple(s.Poly(_exact(f.as_expr() if isinstance(f,s.Poly) else f),variable,domain=field)
                  for f in factors)
    if any(f.is_zero for f in polys):
        raise ValueError("zero polynomial has no finite root-atom certificate")
    return polys,parameters,field


def compile_atoms(factors: Iterable, variable: s.Symbol, parameters=()) -> Certificate:
    polys,parameters,field = _setup(factors,variable,parameters)
    atoms: list[Atom] = []
    calls = 0
    one = s.Poly(1,variable,domain=field)
    for i,f in enumerate(polys):
        # sqf_list is squarefree decomposition, not irreducible factorization.
        for layer,e in f.monic().sqf_list()[1]:
            residual = layer.monic()
            refined = []
            for atom in atoms:
                calls += 1
                common = atom.polynomial.gcd(residual).monic()
                outside = atom.polynomial.exquo(common)
                if outside.degree() > 0:
                    refined.append(Atom(atom.profile,outside))
                if common.degree() > 0:
                    if atom.profile[i] != 0:
                        raise AssertionError("overlapping squarefree layers")
                    profile = list(atom.profile); profile[i] = int(e)
                    refined.append(Atom(tuple(profile),common))
                    residual = residual.exquo(common)
            if residual.degree() > 0:
                profile = [0]*len(polys); profile[i] = int(e)
                refined.append(Atom(tuple(profile),residual))
            grouped = {}
            for atom in refined:
                grouped[atom.profile] = grouped.get(atom.profile,one)*atom.polynomial
            atoms = [Atom(v,g.monic()) for v,g in sorted(grouped.items())]
    return Certificate(variable,parameters,tuple(f.LC() for f in polys),tuple(atoms),calls)


def verify_certificate(factors: Iterable, cert: Certificate) -> bool:
    """Structural check independent of compiler counters/processing order."""
    try:
        polys,_,field = _setup(factors,cert.variable,cert.parameters)
        if len(polys) != len(cert.scalars) or any(c == 0 for c in cert.scalars):
            return False
        seen = set()
        for a in cert.atoms:
            if len(a.profile) != len(polys) or any(type(e) is not int or e < 0 for e in a.profile):
                return False
            if not any(a.profile) or a.profile in seen:
                return False
            seen.add(a.profile)
            g = a.polynomial
            if g.gens != (cert.variable,) or g.domain != field or g.degree() <= 0 or g.LC() != 1:
                return False
            if g.gcd(g.diff()).degree() != 0:
                return False
        if any(a.polynomial.gcd(b.polynomial).degree() != 0 for a,b in combinations(cert.atoms,2)):
            return False
        return cert.reconstruct() == polys
    except (ValueError,TypeError,s.PolynomialError,s.CoercionFailed):
        return False


def signature(cert: Certificate):
    return cert.scalars,tuple((a.profile,a.polynomial) for a in cert.atoms)


@dataclass(frozen=True)
class Guard:
    parameters: tuple[s.Symbol, ...]
    factors: tuple[s.Poly, ...]
    conditions: tuple[tuple[str,s.Expr], ...]

    @property
    def polynomial(self):
        """Optional expanded product; routine specialization keeps factors sparse."""
        return s.Poly(s.prod(p.as_expr() for p in self.factors), *self.parameters, domain=s.QQ)

    def at(self, values: Mapping):
        if set(values) != set(self.parameters):
            raise ValueError("supply every parameter, and no extra values")
        if any(not _exact(v).is_Rational for v in values.values()):
            raise TypeError("this reference specialization accepts exact rational values")
        result = s.Integer(1)
        for p in self.factors:
            value = p.as_expr().subs(values, simultaneous=True)
            if value == 0:
                return s.Integer(0)
            result *= value
        return result


def regular_guard(cert: Certificate, endpoints=None) -> Guard:
    if not cert.parameters:
        raise ValueError("a parameter guard requires at least one parameter")
    conditions: list[tuple[str,s.Expr]] = []
    params = cert.parameters
    factors: list[s.Poly] = []
    seen = set()

    def add_poly(expr,label):
        p = s.Poly(_exact(expr),*params,domain=s.QQ)
        if p.is_zero:
            raise ValueError(f"persistent degeneracy: {label}")
        if p.total_degree() > 0:
            p = p.sqf_part().monic()
            if p not in seen:
                seen.add(p); factors.append(p)
            conditions.append((label,p.as_expr()))

    def denominator(expr,label):
        _,den = s.fraction(s.cancel(expr))
        add_poly(den,label+' denominator')

    def nonzero(expr,label):
        num,den = s.fraction(s.cancel(expr))
        add_poly(num,label+' numerator'); add_poly(den,label+' denominator')

    for i,c in enumerate(cert.scalars):
        nonzero(c,f'scalar[{i}]')
    for j,a in enumerate(cert.atoms):
        for c in a.polynomial.all_coeffs():
            denominator(c,f'atom[{j}] coefficient')
        nonzero(a.polynomial.resultant(a.polynomial.diff()),f'atom[{j}] squarefree')
        if endpoints is not None:
            if len(endpoints) != 2 or not all(_exact(e).is_Rational for e in endpoints):
                raise TypeError("two exact rational endpoints required")
            if not endpoints[0] < endpoints[1]:
                raise ValueError("ordered endpoints required")
            for end in endpoints:
                nonzero(a.polynomial.eval(end),f'atom[{j}] endpoint {end}')
    for j,k in combinations(range(len(cert.atoms)),2):
        nonzero(cert.atoms[j].polynomial.resultant(cert.atoms[k].polynomial),f'collision[{j},{k}]')
    return Guard(params,tuple(factors),tuple(conditions))


def specialize(cert: Certificate, guard: Guard, values: Mapping) -> Certificate:
    if guard.parameters != cert.parameters or guard.at(values) == 0:
        raise ValueError("exceptional parameter: recompile the specialized factors separately")
    y = cert.variable
    subst = lambda e: s.cancel(e.subs(values,simultaneous=True))
    result = Certificate(y,(),tuple(subst(c) for c in cert.scalars),
                         tuple(Atom(a.profile,s.Poly(subst(a.polynomial.as_expr()),y,domain=s.QQ))
                               for a in cert.atoms))
    factors = tuple(subst(f.as_expr()) for f in cert.reconstruct())
    if not verify_certificate(factors,result):
        raise AssertionError("regular specialization did not preserve the certificate")
    return result


def transform_parameters(cert: Certificate, substitution: Mapping) -> Certificate:
    """Automorphism facade: only bijective permutations of all parameters."""
    if set(substitution) != set(cert.parameters) or set(substitution.values()) != set(cert.parameters):
        raise ValueError("only a parameter permutation is certified here")
    tr = lambda e: e.subs(substitution,simultaneous=True)
    return Certificate(cert.variable,cert.parameters,tuple(tr(c) for c in cert.scalars),
                       tuple(Atom(a.profile,s.Poly(tr(a.polynomial.as_expr()),cert.variable,domain=cert.field))
                             for a in cert.atoms))
