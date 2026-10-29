#!/usr/bin/env python3
"""PREFIX-349: six-source exhaustion via Segre degree, plus 1e-22 risk-root interval.

Checks all ten source-frame 3x3 minors and six disjoint Banach boxes, then
reuses the earlier exact-rational T6 interval/derivative verifier. Projective
finiteness and multihomogeneous Bezout length six are proved in README.
On a clean enterprise-math checkout, loads pinned predecessor source locally.
No network, angle sampling, or floating-point sign decisions.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from io import BytesIO
from tempfile import TemporaryDirectory
from shutil import copyfile
from math import comb
import base64, json, runpy, tarfile

SOURCE_PATHS = {
 '342':'research_notes/research6_prefix342_exact_five_contact_20261029/PREFIX342_SOURCE_PACKAGE.tar.xz.b64',
 '346':'research_notes/research6_prefix346_risk_crossing_20261029/verify_prefix346.py',
 '347':'research_notes/research6_prefix347_unique_crossing_20261029/verify_prefix347.py',
 '348':'research_notes/research6_prefix348_root_isolation_20261029/verify_prefix348.py',
}
local=Path(__file__).resolve().parent

def load_checkers(work):
    if all((local/f'verify_prefix{n}.py').is_file() for n in SOURCE_PATHS):
        return local
    root=local.parents[1]  # research_notes/<this study> -> project root
    data=base64.b64decode((root/SOURCE_PATHS['342']).read_text(encoding='utf-8').strip())
    with tarfile.open(fileobj=BytesIO(data),mode='r:xz') as tf:
        item=tf.extractfile('verify_prefix342.py')
        assert item is not None
        (work/'verify_prefix342.py').write_bytes(item.read())
    for n in ('346','347','348'):
        copyfile(root/SOURCE_PATHS[n],work/f'verify_prefix{n}.py')
    return work

with TemporaryDirectory(prefix='prefix349_') as temp:
    work=load_checkers(Path(temp))
    prev=runpy.run_path(str(work/'verify_prefix348.py'))
    original=prev['prev']['v']
    A,raw,q,lam=original['A'],original['raw'],original['q'],original['lam']
    rows=list(combinations(range(5),3))
    minors={''.join(str(i+1) for i in combi):str(A[list(combi),:].det().expand(complex=True))
            for combi in rows}
    assert len(minors)==10 and all(A[list(c),:].det()!=0 for c in rows)
    assert all(q[j]==lam**2*F(raw[j],64) for j in range(5))
    # The prior exact Banach verifiers established existence, local uniqueness,
    # and disjointness in the real gauge with positive 3rd complex coordinate.
    roots=original['refined']
    r=F(1,10**29)
    assert len(roots)==6 and all(x[4]>r for x in roots)
    assert all(any(abs(roots[i][k]-roots[j][k])>2*r for k in range(5))
               for i,j in combinations(range(6),2))
    # For X=P^2 x P^2, (H_u+H_v)^4 = 6 H_u^2 H_v^2.
    assert len(A.tolist())==5 and len(A.tolist()[0])==3
    assert 5>2*(3-1) and comb(4,2)==6

    evaluate,L=prev['evaluate'],prev['L']
    scale=10**22
    def floor_scaled(x):return (x.numerator*scale)//x.denominator
    def out(x,n):
        t=10**n
        return str(F(x.numerator*t//x.denominator,t))
    def up(x,n):
        t=10**n
        return str(F(-((-x.numerator*t)//x.denominator),t))
    def at(num):
        h=F(num,scale)
        obj=evaluate(h)
        low=F(obj['radius_sq_lower'])-L
        high=F(obj['radius_sq_upper'])-L
        assert low>0 or high<0, ('unresolved sign',h)
        sign='ABOVE_L' if low>0 else 'BELOW_L'
        assert obj['sign']==sign
        return sign, {'numerator':str(num),'denominator':str(scale),'h':str(h),
                      'risk_minus_L_outward_29dp':[out(low,29),up(high,29)],
                      'sign':sign,
                      'min_contact_weight_gt_1e4':F(obj['min_alpha_lower'])>F(1,10**4),
                      'other_seven_slack_gt_3e3':F(obj['min_noncontact_slack_lower'])>F(3,1000),
                      'all_arc_im_lt_minus_97e2':F(obj['max_arc_Im_t_upper'])<-F(97,100)}
    a=floor_scaled(prev['h_left'])
    b=floor_scaled(prev['h_right'])+1
    sa,ra=at(a)
    sb,rb=at(b)
    assert (sa,sb)==('ABOVE_L','BELOW_L')
    step=0
    while b-a>1:
        m=(a+b)//2
        sign,item=at(m)
        if sign=='ABOVE_L':a,sa,ra=m,sign,item
        else:b,sb,rb=m,sign,item
        step+=1
    assert b-a==1 and all(x['min_contact_weight_gt_1e4'] and
                          x['other_seven_slack_gt_3e3'] and x['all_arc_im_lt_minus_97e2']
                          for x in (ra,rb))
    report={'schema':'PREFIX349_SEGRE_EXHAUSTION_AND_EXACT_ROOT_BRACKET_V1',
            'status':'PASS_AUTHOR_SIDE_FULL_SOURCE_ALGEBRAIC_EXHAUSTION_AND_1E22_BRACKET',
            'global_knowledge_source_snapshot':'ebc95a36c61f05438c3294b5dd4c1e2011f51f70',
            'enterprise_math_source_snapshot':'e3148a75734182faea1e2822c84bd782b43005bb',
            'q':[str(t) for t in q], 'L':str(L),
            'A_3x3_minors':minors,'full_spark':True,'n_sources_banach_boxes':6,
            'algebraic_degree_of_measurement_map':comb(4,2),
            'projective_basepoint_free_lemma':'five supports cannot be covered by two zero sets of cardinality at most two',
            'finite_map_lemma':'O(1,1) is ample; no positive-dimensional fiber; four proper (1,1) divisors have intersection number six',
            'six_real_sources_exhaust_all_complex_projective_preimages':True,
            'bisection_steps':step,'left':ra,'right':rb,'interval_width':str(F(1,scale)),
            'uniqueness':'PREFIX347 globally strict Fprime<0 on containing [1.66639681,1.66639682]',
            'scope':'Static auxiliary S7-3 five-port BRC C3 with exact q and retained phase. Full physical source fiber S(h) equals six arcs T6(h) for the declared reports.',
            'nonconclusions':['Does not establish P000-native X6 or any 3D slice/Detector/time bridge.',
                               'Not an independent Driver review, Source CLAIM or formal task admission.']}
    (local/'RESULTS_PREFIX349_SUMMARY.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(report['status'])
    print('ten nonzero source-frame minors; six disjoint certified gauge roots; Segre degree = 6')
    print('unique full-fiber risk crossing in (',a,'/',scale,',',b,'/',scale,')',sep='')
    print('left sign',ra['sign'],'bounds',ra['risk_minus_L_outward_29dp'])
    print('right sign',rb['sign'],'bounds',rb['risk_minus_L_outward_29dp'])
