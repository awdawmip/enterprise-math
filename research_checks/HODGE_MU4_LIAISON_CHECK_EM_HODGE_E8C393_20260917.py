#!/usr/bin/env python3
"""Exact certificates for a special-fiber Weil-cycle continuation.

Reuses the pinned 2026-09-10 exterior arithmetic unchanged. The finite checks
below do not prove deformation unobstructedness, semiregularity, existence of
specified low-degree complete intersections, or the general Hodge conjecture.
Run this script beside its named dependency; only the standard library is used.
"""
from __future__ import annotations
import hashlib
import itertools
import json
import math
from pathlib import Path
from HODGE_FOUR_INTERSECTION_GRAPH_CHECK_EM_HODGE_E8C393_20260910 import (
    F, G, add, scale, wedge, product, integral, pi, pull, rank,
)

checks: list[str] = []

def check(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)
    checks.append(name)

UNITS = (G(F(1)), G(F(0),F(1)), G(F(-1)), G(F(0),F(-1)))

def graph(ts: tuple[int, int, int]) -> dict:
    """Fundamental exterior class of y_j = i**ts[j] x_j."""
    fs = []
    for j,t in enumerate(ts):
        a,b = UNITS[t].re, UNITS[t].im
        fx = {1<<(2*(j+3)):F(1), 1<<(2*j):-a, 1<<(2*j+1):b}
        fy = {1<<(2*(j+3)+1):F(1), 1<<(2*j):-b, 1<<(2*j+1):-a}
        fs.append(wedge(fx,fy))
    return product(fs)

def period_derivative(form: dict, i: int, j: int, imaginary: bool=False) -> dict:
    """Derivation induced by dot J(z) = C conjugate(z).

    Physical complex coordinates are x_1,x_2,x_3,y_1,y_2,y_3.
    C has upper-right block B and lower-left D^{-1} B^T,
    D=diag(1,1,3). B_ij is 1 or i in this exact basis.
    """
    images = {}
    def put(row: int, col: int, re: F, im: F) -> None:
        images[2*row] = {1<<(2*col):re, 1<<(2*col+1):im}
        images[2*row+1] = {1<<(2*col):im, 1<<(2*col+1):-re}
    b = G(F(0),F(1)) if imaginary else G(F(1))
    put(i,j+3,b.re,b.im)
    d = F(1 if j<2 else 3)
    put(j+3,i,b.re/d,b.im/d)
    out = {}
    for mask,c in form.items():
        inds = [k for k in range(12) if mask>>k & 1]
        for position,k in enumerate(inds):
            if k in images:
                fs = [{1<<a:F(1)} for a in inds]
                fs[position] = images[k]
                out = add(out,scale(product(fs),c))
    return out

def determinant(matrix: list[list[F]]) -> F:
    a = [row[:] for row in matrix]
    n = len(a)
    out = F(1)
    for j in range(n):
        p = next((i for i in range(j,n) if a[i][j]), None)
        if p is None:
            return F(0)
        if p != j:
            a[p],a[j] = a[j],a[p]
            out = -out
        z = a[j][j]
        out *= z
        for k in range(j,n):
            a[j][k] /= z
        for i in range(j+1,n):
            z = a[i][j]
            for k in range(j,n):
                a[i][k] -= z*a[j][k]
    return out

def exp_form(theta: dict, coefficient: int) -> dict:
    return add(*(scale(product([theta]*k),F(coefficient**k,math.factorial(k)))
                 for k in range(7)))

def degree_part(form: dict, codimension: int) -> dict:
    return {m:c for m,c in form.items() if m.bit_count() == 2*codimension}

def run() -> dict:
    dependency = Path(__file__).with_name(
        'HODGE_FOUR_INTERSECTION_GRAPH_CHECK_EM_HODGE_E8C393_20260910.py')
    b = dependency.read_bytes()
    blob = hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    check('unchanged_pinned_dependency',blob=='a88a9d3106031ba015d41772ce6629f210052ab1')
    labels = {s:[a for a in itertools.product(range(4),repeat=3) if sum(a)%4==s]
              for s in (0,2)}
    check('sixteen_positive_components',len(labels[0])==16)
    check('sixteen_negative_components',len(labels[2])==16)
    P = add(*(graph(a) for a in labels[0]))
    M = add(*(graph(a) for a in labels[2]))
    C = add(P,scale(M,-1))
    w = pi(graph((0,0,0)))
    q = product([add({3<<(2*j):F(1)},{3<<(2*(j+3)):F(1)}) for j in range(3)])
    theta = add(*[{3<<(2*j):F(1 if j<5 else 3)} for j in range(6)])
    theta3 = product([theta]*3)
    check('determinant_character_filter_C_equals_32w',C==scale(w,32))
    check('positive_class_16q_plus_16w',P==add(scale(q,16),scale(w,16)))
    check('negative_class_16q_minus_16w',M==add(scale(q,16),scale(w,-16)))
    check('pure_projector_fixed_point',pi(C)==C)
    check('pure_cycle_ample_degree_zero',integral(wedge(C,theta3))==0)
    check('pure_cycle_square_minus_2048',integral(wedge(C,C))==-2048)
    check('theta_annihilates_pure_cycle',not wedge(theta,C))

    dims = [0]*7
    edges = {1:0,2:0,3:0}
    for a in labels[0]:
        for b in labels[2]:
            changes = [(y-x)%4 for x,y in zip(a,b) if x!=y]
            s = len(changes)
            N = math.prod(4 if r==2 else 2 for r in changes)
            edges[s] += 1
            for k in range(2*(3-s)+1):
                dims[s+k] += N*math.comb(2*(3-s),k)
    check('clean_intersection_edge_counts',edges=={1:48,2:96,3:112})
    check('Ext_P_M_polynomial',dims==[0,192,1152,4480,1152,192,0])
    check('Hom_M_P_zero_by_Koszul_support_formula',dims[0]==0)
    check('1152_Ext2_channels',dims[2]==1152)
    check('Serre_duality_dimension_symmetry',dims==dims[::-1])
    check('same_sign_distinct_graphs_no_one_coordinate_change',all(
        sum(x!=y for x,y in zip(a,b))>=2
        for group in labels.values() for a in group for b in group if a!=b))

    directions = [(im,i,j) for im in (False,True) for i in range(3) for j in range(3)]
    qcols = []
    for k,(im,i,j) in enumerate(directions):
        dq = period_derivative(q,i,j,im)
        qcols.append(dq)
        check(f'pure_cycle_period_derivative_zero_{k}',not period_derivative(C,i,j,im))
        check(f'polarization_period_derivative_zero_{k}',not period_derivative(theta,i,j,im))
        check(f'positive_period_derivative_is_16dq_{k}',
              period_derivative(P,i,j,im)==scale(dq,16))
        check(f'negative_period_derivative_is_16dq_{k}',
              period_derivative(M,i,j,im)==scale(dq,16))
    masks = sorted(set().union(*(c.keys() for c in qcols)))
    rows = [[c.get(m,F(0)) for c in qcols] for m in masks]
    check('q_period_rank_14_real',rank(rows)==14)
    zero_columns = [k for k,c in enumerate(qcols) if not c]
    check('exact_free_period_coordinates',zero_columns==[0,4,9,13])
    constrained = [k for k in range(18) if k not in zero_columns]
    chosen, small = [], []
    for mask,row in zip(masks,rows):
        new = [row[k] for k in constrained]
        if rank(small+[new])>len(small):
            chosen.append(mask)
            small.append(new)
        if len(small)==14:
            break
    minor_det = determinant(small)
    check('nonzero_14_by_14_period_minor',minor_det!=0)

    # Liaison is proved in the note. Here only its formal Chern-character
    # consequences are checked, not geometric existence at these small t values.
    for t in (1,2,3):
        e = exp_form(theta,-t)
        f = product([add({0:F(1)},scale(e,-1))]*3)
        chS = add(scale(f,16),C)
        expected = {
            3:add(scale(theta3,16*t**3),C),
            4:scale(product([theta]*4),-24*t**4),
            5:scale(product([theta]*5),20*t**5),
            6:scale(product([theta]*6),-12*t**6),
        }
        for k in range(7):
            check(f'liaison_ch_degree_{k}_formal_t{t}',degree_part(chS,k)==expected.get(k,{}))
        check(f'liaison_twist_cancels_on_Weil_formal_t{t}',
              wedge(exp_form(theta,-3*t),C)==C)
        alpha = degree_part(chS,3)
        moments = [integral(wedge(alpha,pull(alpha,n))) for n in range(4)]
        lam = G(F(117),F(44))
        expected_m = [552960*t**6*125**n-2048*(lam**n).re for n in range(4)]
        check(f'liaison_four_moments_formal_t{t}',moments==expected_m)
        delta = moments[3]-30*moments[2]+2375*moments[1]-1781250*moments[0]
        check(f'liaison_detector_formal_t{t}',delta==933888*2048)
        for k in (0,1,4):
            h = integral(wedge(chS,exp_form(theta,k)))
            hp = 5760*t**3*k**3-25920*t**4*k**2+43200*t**5*k-25920*t**6
            check(f'liaison_Hilbert_polynomial_formal_t{t}_k{k}',h==hp)

    # Newton's identities for an existing stabilized bundle with ch=r+C.
    c = [{0:F(1)}]
    for k in range(1,7):
        v = {}
        if k>=3:
            v = scale(wedge(c[k-3],scale(C,math.factorial(3))),F(1,k))
        c.append(v)
    check('stabilized_bundle_c1_c2_zero',not c[1] and not c[2])
    check('stabilized_bundle_c3_equals_64w',c[3]==scale(w,64))
    check('stabilized_bundle_c4_c5_zero',not c[4] and not c[5])
    check('stabilized_bundle_c6_degree_minus4096',integral(c[6])==-4096)

    # A polarization-defined background repairs only the numerical equality
    # obstruction; no stability or unobstructedness is asserted for a direct sum.
    for n,t in ((3,1),(7,2)):
        eplus,eminus = exp_form(theta,t),exp_form(theta,-t)
        endch = wedge(add({0:F(n)},scale(eplus,-1)),add({0:F(n)},scale(eminus,-1)))
        check(f'background_rank_{n}_{t}',degree_part(endch,0)=={0:F((n-1)**2)})
        check(f'background_ch1_zero_{n}_{t}',not degree_part(endch,1))
        check(f'background_ch2_negative_{n}_{t}',
              degree_part(endch,2)==scale(product([theta]*2),-n*t*t))
        check(f'background_ch3_zero_{n}_{t}',not degree_part(endch,3))

    return {
        'status':'PASS_EXACT_IDENTITIES_ONLY',
        'researcher_id':'EM-HODGE-E8C393',
        'activity_id':'RA-D77892286633B21C12B83F98',
        'progress_event_id':'HODGE-MU4-LIAISON-E8C393-20260917',
        'checks':len(checks),'failures':0,
        'positive_graph_count':16,'negative_graph_count':16,
        'pure_cycle_multiplier_of_previous_seed':32,'pure_cycle_square':-2048,
        'Ext_P_M_dimensions_0_through_6':dims,
        'clean_intersection_pair_counts':edges,
        'ambient_period_complex_dimension':9,
        'positive_and_negative_class_period_kernel_complex_dimension':2,
        'two_layer_cone_ambient_lift_tangent_dimension_upper_bound':2,
        'bound_applies_to_all_1152_dim_Ext2_parameters':True,
        'q_period_minor':{'basis':'real B row-major, then imaginary B row-major',
            'exterior_row_masks':chosen,'column_indices':constrained,
            'matrix':[[str(x) for x in row] for row in small],
            'determinant':str(minor_det)},
        'liaison_sheaf_ch':'16*(1-exp(-t*theta))^3 + 32*w, t sufficiently large',
        'liaison_effective_cycle_class':'16*t^3*theta^3 + 32*w',
        'liaison_detector':933888*2048,
        'stabilized_bundle_ch':'r+32*w; exists on the special fiber; no explicit rank bound above',
        'stabilized_bundle_c6_degree':-4096,
        'stabilized_bundle_rank_lower_bound':6,
        'geometric_proof_status':'DERIVATION_CANDIDATE_IN_NOTE_INDEPENDENT_REVIEW_PENDING',
        'no_go_proof_status':'Bockstein/cohomology-flatness plus period calculation; not just Ext counts',
        'small_t_values_are_formal_checks_not_geometric_existence_claims':True,
        'very_general_target_seed_constructed':False,
        'semiregularity_proved':False,
        'independent_review_obtained':False,
        'accepted_theorem_or_parent_closure':False,
        'checks_performed':checks,
    }

if __name__=='__main__':
    try:
        print(json.dumps(run(),ensure_ascii=False,indent=2))
    except (AssertionError,ValueError,TypeError,FileNotFoundError) as exc:
        raise SystemExit(f'FAIL: {exc}')
