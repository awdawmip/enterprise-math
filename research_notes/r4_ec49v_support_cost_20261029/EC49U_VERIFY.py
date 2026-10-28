#!/usr/bin/env python3
"""EC49U exact certificate: positive-rational two-source BRC observer.

All arithmetic is fractions.Fraction. This verifies finite extreme points;
the all-real behavioral-policy reduction is proved in PROOF.md.
"""
from fractions import Fraction as F
from itertools import product, combinations
from hashlib import sha256
from pathlib import Path
import json

S = (1, 0, -1)
HIST = (0, 1, 2)
OBS = (0, 1)
Z = (0, 1, 2)
LAM = F(1, 18)
OPTIONS = (None, ('A', 0), ('A', 1), ('B', 0), ('B', 1))


def fraction(x):
    return f'{x.numerator}/{x.denominator}' if x.denominator != 1 else str(x.numerator)


def u_kernel(w, u, eta):
    return F(1, 2) + (2*u - 1) * eta * S[w]


def source_wz(source, w, z):
    if source == 'P':
        return F(1, 6) if w == z else F(1, 12)
    if source == 'Q':
        return F(1, 9)
    raise ValueError(source)


def atom(source, w, u, z, eta):
    return source_wz(source, w, z) * u_kernel(w, u, eta)


def delta(w, u, z, eta):
    return atom('P', w, u, z, eta) - atom('Q', w, u, z, eta)


def validate_sources(eta):
    assert F(0) <= eta < F(1, 2)
    for src in ('P', 'Q'):
        atoms = [atom(src, w, u, z, eta) for w in HIST for u in OBS for z in Z]
        assert len(atoms) == 18 and all(a > 0 for a in atoms)
        assert sum(atoms) == 1
        for w in HIST:
            for u in OBS:
                assert sum(atom(src, w, u, z, eta) for z in Z) == u_kernel(w, u, eta)/3
    for w in HIST:
        for u in OBS:
            for z in Z:
                assert delta(w, u, z, eta) == u_kernel(w, u, eta) * F(3*(w == z)-1, 36)


def optimized_s_value(fiber, eta):
    """After each code and U, choose S iff its acceptance advantage exceeds S cost.
    Terminal acceptance mask is positive signed P-Q coefficient for each Z.
    """
    benefit = F(0)
    for u in OBS:
        signed_positive = sum(max(F(0), sum(delta(w,u,z,eta) for w in fiber)) for z in Z)
        source_mass = sum(u_kernel(w,u,eta)/3 for w in fiber)
        benefit += max(F(0), signed_positive - LAM*source_mass)
    return benefit


def independent_bruteforce_local(fiber, eta):
    """Independent check: eight explicit terminal masks per U, plus no-S.
    No use of the positive-part terminal optimization identity.
    """
    out=F(0)
    for u in OBS:
        candidate_values=[F(0)]
        source_mass=sum(atom('Q',w,u,z,eta) for w in fiber for z in Z)
        for mask in product((0,1),repeat=3):
            advantage=sum(delta(w,u,z,eta)*mask[z] for w in fiber for z in Z)
            candidate_values.append(advantage-LAM*source_mass)
        out+=max(candidate_values)
    return out


def code_fiber_profit(fiber, tag, eta):
    if not fiber:
        return F(0)
    first_cost = 1 if tag == 'A' else 2
    return optimized_s_value(fiber, eta) - LAM*first_cost*F(len(fiber),3)


def deterministic_value(assignment, eta):
    value = F(0)
    for code in OPTIONS[1:]:
        fiber = tuple(w for w in HIST if assignment[w] == code)
        value += code_fiber_profit(fiber, code[0], eta)
    return value


def exact_support(eta):
    rows = []
    for assignment in product(OPTIONS, repeat=3):
        rows.append((deterministic_value(assignment, eta), assignment))
    maximum = max(value for value, _ in rows)
    witnesses = [assignment for value, assignment in rows if value == maximum]
    assert len(rows) == 125
    return maximum, witnesses, rows


def full_witness(eta):
    """prob(STOP)=1/8, prob(A then S)=41/48, prob(B then S)=1/48;
       accept Z=W on the S paths. Full controller retains W.
    """
    p_a = F(41,48)
    p_b = F(1,48)
    p_s = p_a+p_b
    assert 1-p_s == F(1,8)
    alpha_beta = {}
    costs={}
    for src in ('P','Q'):
        alpha_beta[src] = sum((p_s*atom(src,w,u,z,eta)) for w in HIST for u in OBS for z in Z if z==w)
        costs[src] = {
            'stage1':p_a+2*p_b,
            'stage2':p_s,
            'total':p_a+2*p_b+p_s,
        }
    return alpha_beta, costs


def compressed_cost_companion(eta):
    """STOP=11/96, A+S=84/96, B-only=1/96, accept never, D=0.
       Not trace-cost-equivalent to full_witness: there is no cost-3 path.
    """
    p_stop,p_a_s,p_b_only=F(11,96),F(84,96),F(1,96)
    assert p_stop+p_a_s+p_b_only==1
    alpha_beta={src:F(0) for src in ('P','Q')}
    costs={src:{'stage1':p_a_s+2*p_b_only,'stage2':p_a_s,'total':2*p_a_s+2*p_b_only} for src in ('P','Q')}
    return alpha_beta,costs


def check_eta(eta,expected_max,expected_gap):
    validate_sources(eta)
    support,witnesses,rows=exact_support(eta)
    assert support==expected_max, (eta,support,expected_max)
    groups={}
    for size in (1,2,3):
        for f in combinations(HIST,size):
            assert optimized_s_value(f,eta)==independent_bruteforce_local(f,eta)
            groups[''.join(map(str,f))]={
                'post_u_optimized_s_value':fraction(optimized_s_value(f,eta)),
                'profit_if_A':fraction(code_fiber_profit(f,'A',eta)),
                'profit_if_B':fraction(code_fiber_profit(f,'B',eta)),
            }
    full_acc,full_cost=full_witness(eta)
    companion_acc,companion_cost=compressed_cost_companion(eta)
    assert full_acc=={'P':F(7,16),'Q':F(7,24)}
    assert full_cost=={src:{'stage1':F(43,48),'stage2':F(7,8),'total':F(85,48)} for src in ('P','Q')}
    assert companion_cost==full_cost
    assert companion_acc=={'P':F(0),'Q':F(0)}
    h_wit = full_acc['P']-full_acc['Q']-LAM*(full_cost['P']['total']+full_cost['Q']['total'])/2
    assert h_wit==F(41,864)
    gap=h_wit-support
    assert gap==expected_gap and gap>0
    return {
        'eta':fraction(eta),
        'strictly_positive_source_atoms_per_source':18,
        'number_of_deterministic_compressed_prefix_assignments':len(rows),
        'independent_terminal_masks_checked_per_nonempty_fiber_U':8,
        'independent_terminal_enumeration_per_source_eta':7*2*8,
        'support_H_max':fraction(support),
        'support_attaining_prefix_assignment_examples':[str(w) for w in witnesses[:3]],
        'support_attaining_assignments_count':len(witnesses),
        'group_fiber_table':groups,
        'full_acceptance_pair':{k:fraction(v) for k,v in full_acc.items()},
        'compressed_cost_matched_companion_acceptance_pair':{k:fraction(v) for k,v in companion_acc.items()},
        'both_policies_source_stage_costs':{src:{name:fraction(v) for name,v in x.items()} for src,x in full_cost.items()},
        'full_H_value':fraction(h_wit),
        'strict_linear_separation_margin':fraction(gap),
    }


def main():
    tests=[
        (F(1,200),F(1,27),F(1,96)),
        (F(5,12),F(1,24),F(5,864)),
    ]
    result={
        'schema':'EC49U_EXACT_FRACTION_CERTIFICATE_V1',
        'description':'Two-source positive BRC observer; all-real proof is separate from Fraction enumeration',
        'witness_policy':'STOP 1/8; A+S 41/48; B+S 1/48; accept if Z=W; fully retain W',
        'compressed_companion':'STOP 11/96; A+S 84/96; B-only 1/96; constant D; reject terminal',
        'linear_functional':'H=alpha-beta-(E_PT+E_QT)/36',
        'verification_semantics':'Fraction only; exhaustive 5^3=125 pure initial choices and optimal local S/terminal masks, per eta',
        'results':[check_eta(*q) for q in tests],
        'status':'AUTHOR_PROVED_EXACT_CHECK_PASS_UNREVIEWED_NOT_ADMITTED',
    }
    path=Path(__file__).with_name('EXACT_REPORT.json')
    data=json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    path.write_text(data,encoding='utf-8')
    print('EC49U exact checks PASS')
    for r in result['results']:
        print('eta:',r['eta'],'max H compressed:',r['support_H_max'],'full H:',r['full_H_value'],'gap:',r['strict_linear_separation_margin'])
    print('wrote',path.name,'bytes',len(data.encode('utf-8')),'sha256',sha256(data.encode('utf-8')).hexdigest())

if __name__=='__main__':main()
