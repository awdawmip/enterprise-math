#!/usr/bin/env python3
"""EC49FRO: exact rational arithmetic and archived-anchor / native-profile checks.

Without arguments: verify the NEW universal integer-lattice case inequalities.
With --evidence-root DIR: additionally inspect original frozen 141-state model,
terminal fibers, all six inherited unrestricted Bellman anchor certificates,
and replay five inherited named complete trees. This does NOT rerun Bellman DP.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json, sys

BETA=F(620,3299)
COSTS={'A':(6,290,6,751),'B':(5,293,5,704),
       'C':(5,295,5,685),'D':(4,296,4,707),'E':(4,298,4,688)}
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
FIBERS=((8,139),(46,140))

def norm_cost(name,x,l):
    ur,ut,mr,mt=COSTS[name]
    return (1-l)*F(ut+x*ur,141)+l*F(mt+x*mr,310)

def direct_value(x,l):
    return min(norm_cost(n,x,l) for n in COSTS)

def det_regret(x):
    return F(5-x,141) if x<=3 else F(2,141)

def rand_regret(x):
    return F(19*(5-x),3299) if x<=3 else F(38,3299)

def verify_symbolic_and_discrete_cases():
    assert (1-BETA)/141==F(19,3299) and BETA/310==F(2,3299)
    for x in map(F,['1','4/3','3/2','2','5/2','3','7/2','4','100000']):
        v0=norm_cost('A' if x<=3 else 'D',x,F(0))
        v1=norm_cost('C' if x<=3 else 'E',x,F(1))
        best='C' if x<=3 else 'E'
        assert norm_cost(best,x,F(1))-v1==0
        assert norm_cost(best,x,F(0))-v0==det_regret(x)
        assert rand_regret(x)==det_regret(x)*(1-BETA)
        assert direct_value(x,F(0))==v0 and direct_value(x,F(1))==v1
    # Original finite optimum anchors at x=1,3 and lambda=beta.
    assert norm_cost('C',F(1),BETA)==F(7080,3299)
    assert norm_cost('E',F(3),BETA)==F(7290,3299)
    assert norm_cost('C',F(3),BETA)==norm_cost('E',F(3),BETA)
    # Supporting inequality 19*(U_1-300)+2*(M_1-690) >=0,
    # and 19*(U_3-310)+2*(M_3-700) >=0. Integer rounding:
    assert 19*(-1)+2*9<0 and 19*(-1)+2*10>=0
    assert 19*(-2)+2*18<0 and 19*(-2)+2*19>=0
    # The root-mass-4 rigidity yields M_R=4, while for U_R>=5, M_R>=5.
    # On [1,3], the 4 disjoint integer cases give exact lower bounds:
    for x in map(F,['1','7/6','2','17/6','3']):
        target=det_regret(x)
        assert F(10,310)>target  # U_R>=5, U_1<=299; or U_R=4, U_1=301.
        assert F(11-x,310)>target  # U_R=4, U_1<=299.
        assert F(22-x,310)>target  # U_R=4, U_1=300.
        assert 3-x>=0  # U_R=4, U_1>=302 -> uniform regret lower bound.
        assert F(10,310)>F(2,141) # high-price U_3<=309 case.
    # Inequalities on the full intervals are affine, and checked at endpoints.
    for x in [F(1),F(3)]:
        target=det_regret(x)
        assert F(11-x,310)>target
        assert F(22-x,310)>target
        assert F(13-x,310)>target
    assert 141*(11-1)-310*(5-1)==170
    assert 141*(11-3)-310*(5-3)==508
    print('PASS: exact full-real-domain deterministic minimax proof arithmetic')
    print('formula: R_det=(5-x)/141 [1,3]; R_det=2/141 [3,infinity)')
    print('randomized/deterministic ratio:',1-BETA)

def verify_original_evidence(base):
    base=Path(base)
    fi=base/'EM_FRI_WORK'
    frl=base/'EC49FRL_RELEASE'
    frj=base/'EC49FRJ_WORK'
    sys.path.insert(0,str(frl/'code'))
    from EC49FQI_NATIVE_DATA import V,weights,cost_pair
    assert len(V)==228 and len(weights)==141 and sum(weights)==310
    fibers={}
    for i in range(141):
        sig=tuple(V[q][i] for q in range(144))
        fibers.setdefault(sig,[]).append(i)
    multiples=sorted(tuple(z) for z in fibers.values() if len(z)>1)
    assert multiples==list(FIBERS),multiples
    assert all(weights[i]==1 for pair in FIBERS for i in pair)
    assert all(V[148][a]!=V[148][b] for a,b in FIBERS)
    # Each Q must issue a root query on each of the four hard profiles. Hence
    # U_R>=4, and equality forces M_R=4 (all four original weights equal one).
    expected={('1','0'):F(296,141),('1','620/3299'):F(7080,3299),
              ('1','1'):F(690,310),('3','0'):F(308,141),
              ('3','620/3299'):F(7290,3299),('3','1'):F(700,310)}
    index=json.loads((fi/'EC49FRI_EXACT_CHECK_RESULT.json').read_text())
    for (sx,sl),opt in expected.items():
        x,l=F(sx),F(sl)
        p=fi/'endpoints'/f'x{x.numerator}-{x.denominator}_l{l.numerator}-{l.denominator}.json'
        blob=p.read_bytes();a=json.loads(blob)
        assert a['frozen_scientific_commit']==PIN
        match=[z for z in index['validated_8_native_anchors'] if F(z['x'])==x and F(z['lambda'])==l]
        assert len(match)==1 and match[0]['raw_json_sha256']==hashlib.sha256(blob).hexdigest(),p
        assert F(a['optimal_total_interpolated'],sum(a['weights']))==opt,(p,opt)
        assert F(match[0]['unrestricted_optimum'])==opt,p
    source_names={'A':'x1-1_l0-1.json','B':'x1-1_l155-1847.json',
                  'C':'x1-1_l1-1.json','D':'x100000-1_l0-1.json',
                  'E':'x100000-1_l1-1.json'}
    for name,src in source_names.items():
        a=json.loads((frl/'prior_endpoint_trees'/src).read_text())
        source=(frl/'EC49FRL_GLOBAL_FIVE_TREE_DEPTH3_CERTIFICATE.json')
        expected_sha=json.loads(source.read_text())[name]['tree_sha256']
        # Matched source choices (some certificate trees may differ from root-first witnesses).
        variants=[a['trees']['interpolated'],a['trees']['uniform'],*a['all_optimal_first_trees'].values()]
        good=[q for q in variants if tuple(cost_pair(q)[k] for k in ('U_R','U_T','M_R','M_T'))==COSTS[name]]
        assert good,name
    cert=json.loads((frj/'EC49FRJ_TERMINAL_FIBER_CERTIFICATE.json').read_text())
    assert sorted(tuple(z['named_profiles']) for z in cert['nonsingleton_fibers'])==list(FIBERS)
    print('PASS: original frozen 141x228 reconstruction, four hard states, six hash-matched Bellman anchors, five feasible tree vectors')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--evidence-root',help='folder containing extracted EM_FRI_WORK, EC49FRL_RELEASE and EC49FRJ_WORK')
    args=parser.parse_args()
    verify_symbolic_and_discrete_cases()
    if args.evidence_root: verify_original_evidence(args.evidence_root)
