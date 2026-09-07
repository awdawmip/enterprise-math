"""Independent symbolic row checks and selected boundaries; no N-prefix scan."""

import hashlib
import json
from math import factorial
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'experiments/owner_shell_length_20260907'))
import shell_length as shell


def add(*polys):
    result = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            result[monomial] = result.get(monomial,0) + coefficient
    return {m:c for m,c in result.items() if c}


def scale(poly,c):
    return {m:c*a for m,a in poly.items() if c*a}


def multiply(left,right):
    result = {}
    for (i,j),a in left.items():
        for (k,l),b in right.items():
            m=(i+k,j+l)
            result[m]=result.get(m,0)+a*b
    return {m:c for m,c in result.items() if c}


def constant(c):
    return {(0,0):c} if c else {}


def main():
    b,t={(1,0):1},{(0,1):1}
    rows=[(0,1,-1,-5,(16,-24,24)),(0,0,1,3,(16,-8,16)),
          (0,1,1,3,(16,-8,16)),(0,0,3,3,(16,8,40)),
          (0,1,3,3,(16,8,40)),(1,1,3,3,(16,8,16))]
    identities=[]
    for r,(dp,dq,B0,D0,lower) in enumerate(rows):
        N=add(scale(multiply(b,b),6),scale(b,2*r),constant(r),scale(t,2))
        k=add(scale(b,6),constant(r))
        p,q=add(b,constant(dp)),add(b,constant(dq))
        A=add(N,scale(multiply(p,p),-1),scale(multiply(q,q),-1))
        B=add(k,scale(p,-1),scale(q,-1))
        D=add(scale(A,4),scale(multiply(B,B),-1))
        assert B == add(scale(b,4),constant(B0))
        assert D == add(scale(t,8),constant(D0))
        margin=add(multiply(add(B,constant(4)),add(B,constant(4))),scale(D,-3))
        extra=(r*r-2*r+3)//12
        assert extra == int(r==5)
        # Substitute t=2b+extra into the exact polynomial for its lower bound.
        lower_poly={}
        for (i,j),c in margin.items():
            assert j in (0,1)
            term={(i,0):c}
            lower_poly=add(lower_poly,term if j==0 else multiply(term,add(scale(b,2),constant(extra))))
        assert lower_poly == {(2,0):lower[0],(1,0):lower[1],(0,0):lower[2]}
        upper_gap=add(scale(N,6),scale(multiply(add(k,constant(2)),add(k,constant(2))),-1))
        assert upper_gap == add(scale(t,12),scale(b,-24),constant(-(r*r-2*r+4)))
        identities.append({'r':r,'B_constant':B0,'D_constant':D0,'t_extra':extra,
                           'margin_lower_coefficients_b2_b_1':lower})

    parameters=[(0,0,0),(1,0,1),(0,1,0),(2,2,4),(0,3,0),(1,4,2),(0,5,1)]
    cases=[]
    for center,residue,remainder in parameters:
        N=6*center**2+2*center*residue+residue+2*remainder
        endpoint,detail=shell.construct_endpoint(N)
        k=sum(abs(v) for v in endpoint)
        assert sum(v*v for v in endpoint)==N
        assert k*k<=6*N<(k+2)**2 and k%2==N%2
        assert (detail['auxiliary_center_b'],detail['r'],detail['t'])==(center,residue,remainder)
        if detail['case']!='BALANCED':
            A,B,D=detail['A'],detail['B'],detail['D']
            assert A>0 and B>0 and A%2==B%2==1
            assert B*B<4*A and 3*A<B*B+2*B+4
            roots=detail['three_odd_squares_signed']
            assert all((x-B)%4==0 for x in roots) and sum(x*x for x in roots)==D
            four=detail['hadamard_first_four']
            assert all(x>=0 for x in four) and sum(four)==B and sum(x*x for x in four)==A
        cases.append({'b':center,'r':residue,'t':remainder,'N':N,'endpoint':endpoint,'k':k})

    signed=shell.certificate(25,signs=(1,-1,1,-1,1,-1))
    raw=tuple(signed['raw_signed_endpoint'])
    assert raw==(3,0,2,-2,2,-2)
    assert signed['native_common_depth']==min(raw)==-2
    assert tuple(h+signed['native_common_depth'] for h in signed['native_can6'])==raw
    for row in signed['joint_twenty_slices']:
        axes=row['axes']
        reconstructed=[None]*6
        for axis,visible in zip(axes,row['can3']):
            reconstructed[axis]=visible+row['visible_common_offset']
        for axis,hidden in zip((a for a in range(6) if a not in axes),row['omitted_signed_coordinates']):
            reconstructed[axis]=hidden
        assert tuple(reconstructed)==raw
    assert len(signed['joint_twenty_slices'])==20
    count=factorial(sum(abs(v) for v in raw))
    for v in raw:
        count//=factorial(abs(v))
    assert str(count)==signed['shortest_path_multiplicity']['count_decimal']=='415800'
    different=(3,3,2,1,1,1)
    assert shell.verify_endpoint(25,different)['valid'] and different!=raw
    zero=shell.certificate(0,signs=(-1,)*6,search_budget=0,brc_event_budget=0)
    assert tuple(zero['raw_signed_endpoint'])==(0,)*6
    assert zero['shortest_path_multiplicity']['count_decimal']=='1'
    assert shell.certificate(1,brc_event_budget=0)['shortest_path_multiplicity']['status']=='RESOURCE_LIMIT'
    try:
        shell.construct_endpoint(8,search_budget=0)
    except shell.ResourceLimit:
        pass
    else:
        raise AssertionError('zero search budget did not stop')

    consumed=[]
    resource_findings=[]
    def overlong():
        for i in range(100):
            consumed.append(i)
            yield 0
    assert not shell.verify_endpoint(0,overlong())['valid']
    if len(consumed)>7:
        resource_findings.append('overlong iterator consumed beyond six-coordinate validation bound')
    large_preserved=False
    try:
        large=shell.certificate(6_000_000,search_budget=0,brc_event_budget=6000)
        assert large['status']=='ENDPOINT_VERIFIED'
        assert large['shortest_path_multiplicity']['status']=='RESOURCE_LIMIT'
        assert shell.verify_endpoint(6_000_000,large['raw_signed_endpoint'])['valid']
        large_preserved=True
    except ValueError as error:
        resource_findings.append('large balanced endpoint lost to uncaught output conversion: '+str(error))
    for invalid in (True,1.0,-1):
        assert not shell.verify_endpoint(invalid,(0,)*6)['valid']
    assert not shell.verify_endpoint(0,(False,0,0,0,0,0))['valid']
    assert not shell.verify_endpoint(25,(0,)*6)['valid']

    source=Path(shell.__file__)
    output={'status':'PASS' if not resource_findings else 'RESOURCE_FINDINGS_PENDING',
            'resource_findings':resource_findings,'symbolic_six_row_identities':identities,
            'selected_parameter_boundaries':cases,'signed_joint_slices_checked':20,
            'generator_items_consumed':len(consumed),'large_decimal_limit_preserves_endpoint':large_preserved,
            'zero_shell_sign_degeneracy_preserved':True,'source_sha256':{
                str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest()
                for p in (source,Path(__file__))},
            'scope':'symbolic identities and necessary boundary examples; no N-prefix enumeration'}
    destination=ROOT/'experiments/owner_shell_length_audit_20260907.json'
    destination.write_text(json.dumps(output,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'status':output['status'],'symbolic_rows':6,'boundary_endpoints':len(cases),
                      'signed_joint_slices':20,'generator_items_consumed':len(consumed)}))


if __name__=='__main__':
    main()
