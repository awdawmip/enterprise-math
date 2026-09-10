#!/usr/bin/env python3
"""Exact dense-occupancy conservative/residual and quantum-comparison checks.

The integer exchange is imported unchanged from event 15. The quantum layer
ADDS tensor-product states, Born measurements and the stated unitary: it does
not derive these from P000, integer conservation, or classical hidden data.
Dependencies: Python 3, SymPy. All tested coefficients/results are exact.
No PDE forcing, reservoir fitted to a loss, continuum limit, or physical claim.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent / 'ns_native_integer_exchange_d5c00d' / 'check_exchange.py'
EXPECTED = '90018aba469afdc3b2c8cd44fff1a442d5b830943c92f381dbcca5802968e493'
EVENT = 'NS-DENSE-CONSERVATIVE-RESIDUAL-20260910-D5C00D-16'

def load_parent():
    if hashlib.sha256(PARENT.read_bytes()).hexdigest() != EXPECTED:
        raise ValueError('Parent source changed: re-audit before reuse')
    spec = importlib.util.spec_from_file_location('prior_exchange16', PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot load verified parent')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module

def basis(n, i):
    v = sp.zeros(n, 1)
    v[i] = 1
    return v

def ptrace(rho, n, keep):
    """Partial trace, preserving the specified order of retained registers."""
    if rho.shape != (2**n, 2**n) or len(set(keep)) != len(keep):
        raise ValueError('Dimension or register mismatch')
    bits = [tuple((i >> (n-1-k)) & 1 for k in range(n)) for i in range(2**n)]
    omit = [k for k in range(n) if k not in keep]
    out = sp.zeros(2**len(keep))
    for i, a in enumerate(bits):
        ai = sum(a[k] << (len(keep)-1-t) for t, k in enumerate(keep))
        for j, b in enumerate(bits):
            if all(a[k] == b[k] for k in omit):
                bj = sum(b[k] << (len(keep)-1-t) for t, k in enumerate(keep))
                out[ai, bj] += rho[i, j]
    return sp.simplify(out)

def perm_matrix(n, old_to_new):
    if sorted(old_to_new) != list(range(n)):
        raise ValueError('Expected a register permutation')
    u = sp.zeros(2**n)
    for x in range(2**n):
        y = 0
        for k, dst in enumerate(old_to_new):
            y |= ((x >> (n-1-k)) & 1) << (n-1-dst)
        u[y, x] = 1
    return u

def run():
    old = load_parent()
    def exchange(q):
        out = list(q)
        out[1:4] = old.reflect3(q[1:4])
        return tuple(out)
    def ledger(q):
        total = sum(x*x for x in q)
        resolved = Fraction(sum(q[:3])**2 + sum(q[3:])**2, 3)
        return (Fraction(total), resolved, Fraction(total)-resolved)
    classical_cases = 0
    for q in product(range(-1, 2), repeat=6):
        y = exchange(q)
        assert exchange(y) == q and sum(y) == sum(q)
        a, b = ledger(q), ledger(y)
        assert a[0] == b[0] and b[1]-a[1] == -(b[2]-a[2])
        classical_cases += 1
    q0 = (0, 3, 3, 0, 0, 0)
    q1 = exchange(q0)
    assert q1 == (0, 1, 1, 4, 0, 0) and exchange(q1) == q0
    assert ledger(q0) == (18, 12, 6)
    assert ledger(q1) == (18, Fraction(20,3), Fraction(34,3))

    G = sp.ones(3)*sp.Rational(2,3) - sp.eye(3)
    U = sp.eye(8)
    ids = (4, 2, 1)  # |100>, |010>, |001>
    for i in range(3):
        for j in range(3):
            U[ids[i], ids[j]] = G[i,j]
    number = sp.diag(*[i.bit_count() for i in range(8)])
    assert U.H*U == sp.eye(8) and U*U == sp.eye(8)
    assert U*number == number*U
    for p in permutations(range(3)):
        V = perm_matrix(3, p)
        assert V*U == U*V
    psi0 = basis(8, 4)
    psi = U*psi0
    rho = psi*psi.H
    assert sp.trace(rho*number) == 1 and number*psi == psi
    assert U*psi == psi0
    bc = ptrace(rho, 3, (1,2))
    assert bc == sp.Matrix([[1,0,0,0],[0,4,4,0],[0,4,4,0],[0,0,0,0]])/9
    pt = sp.zeros(4)
    for a,b,c,d in product(range(2),repeat=4):
        pt[2*a+d,2*c+b] = bc[2*a+b,2*c+d]
    minor = pt.extract((0,3),(0,3)).det()
    assert minor == -sp.Rational(16,81)
    rb, rc = ptrace(bc,2,(0,)), ptrace(bc,2,(1,))
    chi = bc-sp.kronecker_product(rb,rc)
    assert ptrace(chi,2,(0,)) == sp.zeros(2)
    assert ptrace(chi,2,(1,)) == sp.zeros(2)
    # Correlation residual is not an extra local-energy reservoir.
    n2 = sp.diag(0,1)
    assert sp.trace(chi*(sp.kronecker_product(n2,sp.eye(2))+
                         sp.kronecker_product(sp.eye(2),n2))) == 0
    deph = sp.diag(*rho.diagonal())
    assert ptrace(deph,3,(1,)) == ptrace(rho,3,(1,))
    assert ptrace(deph,3,(2,)) == ptrace(rho,3,(2,))
    assert sp.trace(deph*number) == 1
    return_deph = U*deph*U.H
    assert return_deph[4,4] == sp.Rational(11,27)
    assert sp.trace(deph*deph) == sp.Rational(11,27)

    X = sp.Matrix([[0,1],[1,0]])
    Y = sp.Matrix([[0,-sp.I],[sp.I,0]])
    Z = sp.diag(1,-1)
    I = sp.eye(2)
    left = (X,Y)
    right = ((3*X+4*Y)/5,(3*X-4*Y)/5)
    correlations = []
    probabilities = []
    for a, A in enumerate(left):
        assert A.H == A and A*A == I
        row = []
        for b, B in enumerate(right):
            assert sp.simplify(B.H-B) == sp.zeros(2) and sp.simplify(B*B-I) == sp.zeros(2)
            E = sp.simplify(sp.trace(bc*sp.kronecker_product(A,B)))
            row.append(E)
            probs = {}
            for s,t in product((-1,1), repeat=2):
                val = sp.simplify(sp.trace(bc*sp.kronecker_product((I+s*A)/2,(I+t*B)/2)))
                assert val.is_Rational and val >= 0
                probs[(s,t)] = val
            assert sum(probs.values()) == 1
            assert all(sum(probs[s,t] for t in (-1,1)) == sp.Rational(1,2) for s in (-1,1))
            assert all(sum(probs[s,t] for s in (-1,1)) == sp.Rational(1,2) for t in (-1,1))
            probabilities.append({'settings':[a,b], 'probabilities':{f'{s},{t}':str(v) for (s,t),v in probs.items()}})
        correlations.append(row)
    bell = correlations[0][0]+correlations[0][1]+correlations[1][0]-correlations[1][1]
    assert bell == sp.Rational(112,45) and bell > 2
    classical_chsh = []
    for a0,a1,b0,b1 in product((-1,1), repeat=4):
        val = a0*(b0+b1)+a1*(b0-b1)
        assert abs(val) == 2
        classical_chsh.append(val)

    # These are channel diagnostics, not extra dynamics imposed on the closed model.
    channels = [(I,), (X,), (Y,), (Z,), ((I+Z)/2,(I-Z)/2),
                ((I+X)/2,(I-X)/2),
                (sp.diag(1,sp.Rational(3,5)),sp.Matrix([[0,sp.Rational(4,5)],[0,0]]))]
    ns_checks = 0
    for ks in channels:
        assert sum((k.H*k for k in ks),sp.zeros(2)) == I
        for side in (0,1):
            for r,s in product(range(4),repeat=2):
                E = sp.zeros(4); E[r,s] = 1
                out = sp.zeros(4)
                for k in ks:
                    op = sp.kronecker_product(k,I) if side == 0 else sp.kronecker_product(I,k)
                    out += op*E*op.H
                assert ptrace(out,2,(1-side,)) == ptrace(E,2,(1-side,))
                ns_checks += 1

    # Exact residual-memory equation, derived from the same G (not fitted).
    A = G[0,0]; B = G[:1,1:]; C = G[1:,:1]; D = G[1:,1:]
    xs=[]; v=sp.Matrix([1,0,0]); memory_checks=0
    for n in range(24):
        xs.append(v[0]); assert (v.H*v)[0] == 1
        rhs=A*xs[n]+sum((B*(D**(n-1-j))*C)[0]*xs[j] for j in range(n))
        v=G*v
        assert sp.simplify(rhs-v[0]) == 0
        assert (B*(D**n)*C)[0] == 8/sp.Integer(3)**(n+2)
        memory_checks+=1
    # Restricted unmeasured orbit is finite; no claim that all qubit states are finite.
    orbit={tuple(basis(8,i)) for i in ids}
    while True:
        nxt=orbit|{tuple(U*sp.Matrix(v)) for v in orbit}
        if nxt == orbit: break
        orbit=nxt
    assert len(orbit)==6

    # Transport B into E through a ternary cycle on B,D,E; D,E begin unexcited.
    # Old B goes to E, E to D, D to B. Source B,D are at c; E at c+e_j.
    V=perm_matrix(5,(0,4,2,1,3))
    v0=sp.kronecker_product(psi,basis(4,0));v1=V*v0
    transported=v1*v1.H
    assert ptrace(transported,5,(4,2)) == bc
    assert ptrace(transported,5,(1,3)) == sp.diag(1,0,0,0)
    assert V.H*v1 == v0
    for i in range(32):
        dest=next(j for j in range(32) if V[j,i] == 1)
        assert dest.bit_count() == i.bit_count()
    edges=0
    zero=(0,)*6
    for axis,sign in product(range(6),(-1,1)):
        neighbor=tuple(sign*int(k==axis) for k in range(6))
        positions=(zero,zero,zero,zero,neighbor)
        for src,dst in enumerate((0,4,2,1,3)):
            d=sum(abs(x-y) for x,y in zip(positions[src],positions[dst]))
            assert d<=1
            edges+=int(d==1)
    return {
      'schema':'EM_DENSE_CONSERVATIVE_RESIDUAL_RESULTS_V1','event_id':EVENT,
      'status':'EXACT_FINITE_ALGEBRA_AND_CONDITIONAL_QUANTUM_COMPARISON',
      'sympy_version_tested':sp.__version__, 'parent_sha256':EXPECTED,
      'classical':{'cross_block_cases':classical_cases,'initial':q0,'after':q1,
                   'total_resolved_residual_before':list(map(str,ledger(q0))),
                   'total_resolved_residual_after':list(map(str,ledger(q1))),
                   'reversible':True},
      'quantum':{'unitary_and_involution':True,'full_excitation_commutator_zero':True,
                 'participant_permutations':6,'single_excitation_amplitudes':['-1/3','2/3','2/3'],
                 'BC_density':[[str(x) for x in row] for row in bc.tolist()],
                 'partial_transpose_principal_minor':str(minor),
                 'CHSH_exact':str(bell),'correlations':[[str(x) for x in row] for row in correlations],
                 'bell_probabilities':probabilities,'classical_deterministic_assignments':16,
                 'non_signalling_matrix_unit_checks':ns_checks,
                 'coherent_return_probability':'1','dephased_return_probability':'11/27',
                 'residual_memory_steps':memory_checks,'restricted_unmeasured_states':len(orbit),
                 'transport_basis_states':32,'signed_native_neighbor_routes':12,
                 'nonzero_register_transport_edges':edges},
      'nonclaims':['No derivation of quantum tensor-product/Born rules from P000.',
                  'Dense occupancy is not continuum density or mandatory entanglement.',
                  'Quantum correlation residual is not an extra physical energy reservoir.',
                  'The exact finite circuit is not a finite-alphabet construction of unrestricted quantum theory.',
                  'No faster-than-light signalling, force-law admission, NS theorem, independent review or Lean build.']}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=HERE/'results_16.json')
    args=parser.parse_args()
    data=run();text=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
    args.output.write_text(text,encoding='utf-8')
    print(text)

if __name__ == '__main__':main()
