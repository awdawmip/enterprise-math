"""Independent targeted audit of C87's integrated-kernel certificate.

Checks full interval coverage, exact chamber continuity, axis coefficients,
all saved bindings/margins, and selected full-box recomputations. This does
not rerun the triangle kappa mesh or the full adaptive kernel search.
"""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import hashlib,importlib.util,json,sys,time

ROOT=Path(__file__).resolve().parent

def import_file(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

def audit():
    start=time.time()
    main=import_file('c87_integrated_kernel_audited',ROOT/'certify_integrated_kernel.py')
    base=main.base;Q=base.Q
    cert=json.loads((ROOT/'integrated_kernel_certificate.json').read_text())
    terms,source_hash=base.terms_from_json()
    assert cert['chamber_source_sha256']==source_hash
    for name,digest in cert['source_sha256'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,name
    axis_source=ROOT/'positions/mellin_chambers.json'
    assert hashlib.sha256(axis_source.read_bytes()).hexdigest()==source_hash
    assert (ROOT/'positions/c84_interval_kernel.py').read_bytes()==(
        ROOT/'inputs/c86/triangle/c84_interval_kernel.py').read_bytes()

    def restricted(ts,kind,v):
        out=defaultdict(F)
        for a,b,c,w in ts:
            aa,bb=(a,b+c*v)if kind=='r' else(a+c*v,b)
            if not aa and not bb:continue
            if aa<0 or(aa==0 and bb<0):aa,bb=-aa,-bb
            out[aa,bb]+=w
        return{k:v for k,v in out.items()if v}
    edge_checks=0
    for j in range(1,4):
        for si in range(j):
            assert restricted(terms[j-1,si],'r',base.CUTS[j])==restricted(terms[j,si],'r',base.CUTS[j])
            edge_checks+=1
        for ri in range(j,4):
            assert restricted(terms[ri,j-1],'s',base.CUTS[j])==restricted(terms[ri,j],'s',base.CUTS[j])
            edge_checks+=1
    assert edge_checks==12

    rows=cert['intervals'];n=cert['r_grid']
    assert len(rows)==cert['accepted_x_intervals']==60
    assert F(rows[0]['x_interval'][0])==F(1,8)
    assert F(rows[-1]['x_interval'][1])==1
    assert all((c*n).denominator==1 for c in base.CUTS)
    ratios=[];radial_cells=boundary_cells=0
    for j,row in enumerate(rows):
        l,h=map(F,row['x_interval']);assert l<h
        if j:assert F(rows[j-1]['x_interval'][1])==l
        lo=int(row['A_interval']['lower_numerator'])
        hi=int(row['A_interval']['upper_numerator'])
        center=row['center'];error=row['error']
        e=int(error['upper_numerator'])
        assert lo==int(center['lower_numerator'])-e
        assert hi==int(center['upper_numerator'])+e
        ratio=F(lo,Q)/(h*h);ratios.append(ratio)
        assert ratio>F(1,200)
        interior=boundary=0
        for i in range(n):
            a,b=F(i,n),F(i+1,n);ri=base.index((a+b)/2)
            possible=[k for k in range(ri+1)
                      if b*h>base.CUTS[k] and a*l<base.CUTS[k+1]]
            assert possible
            if len(possible)==1:interior+=1
            else:boundary+=1
        assert interior==row['interior_r_cells']
        assert boundary==row['boundary_r_cells']
        radial_cells+=interior+boundary;boundary_cells+=boundary
    minimum=min(ratios)
    assert minimum==F(cert['actual_minimum_certified_ratio'])
    assert minimum>F(1,200)

    # Complete-box recomputations cover the first/last box, the strict-margin
    # bottleneck, the most chamber-crossing box, and the box containing x=1/3.
    selected={0,len(rows)-1,ratios.index(minimum),
              max(range(len(rows)),key=lambda j:rows[j]['boundary_r_cells'])}
    selected.add(next(j for j,r in enumerate(rows)
                      if F(r['x_interval'][0])<=F(1,3)<=F(r['x_interval'][1])))
    rerun=[]
    for j in sorted(selected):
        row=rows[j];l,h=map(F,row['x_interval'])
        bound,detail=main.interval_box(terms,n,l,h)
        assert bound.lo==int(row['A_interval']['lower_numerator'])
        assert bound.hi==int(row['A_interval']['upper_numerator'])
        for key,value in detail.items():assert value==row[key],(j,key)
        rerun.append(row['x_interval'])

    # Independent coefficient collection of the complete x-axis expansion.
    p=F(41,20);g=F(1,20);remainder=F(0)
    a2terms=defaultdict(F)
    for ri in range(4):
        a,b=base.CUTS[ri:ri+2]
        constant=defaultdict(F);linear=defaultdict(lambda:[F(0),F(0)])
        quad=defaultdict(lambda:[F(0),F(0),F(0)])
        for z,v,w,c in terms[ri,0]:
            assert z in (0,F(1,2),1)
            if not z:continue
            constant[z]+=c*z*z
            linear[z][0]+=p*c*z*v;linear[z][1]+=p*c*z*w
            for j,item in enumerate((v*v,2*v*w,w*w)):
                quad[z][j]+=p*(p-1)*c*item/2
            m=max(abs(v+w*a),abs(v+w*b))
            assert m<=z
            ell=z-m/8;assert 0<ell<=1
            remainder+=abs(c)*p*(p-1)*g*m**3*(b-a)/(6*ell)
        assert all(v==0 for v in constant.values())
        assert all(v==[0,0]for v in linear.values())
        if ri<2:
            expected={F(1,2):[0,0,0],F(1):[0,0,F(861,200)]}
        else:
            expected={F(1,2):[F(861,200),-F(2583,200),F(861,100)],
                      F(1):[-F(861,400),F(861,80),-F(861,100)]}
        for radical in (F(1,2),F(1)):assert quad[radical]==expected[radical]
        for radical,poly in quad.items():
            for j,c in enumerate(poly):
                a2terms[radical*b]+=c*b**(j+1)/(g+j+1)
                if a:a2terms[radical*a]-=c*a**(j+1)/(g+j+1)
    a2terms={a:c for a,c in a2terms.items()if c}
    assert a2terms=={F(1,2):F(211,244),F(1,4):-F(101,122),F(1):F(23,61)}
    assert remainder==F(9318931,47520000)
    axis=import_file('c87_axis_audited',ROOT/'positions/certify_axis_midpoint.py')
    axis_cert=json.loads((ROOT/'positions/axis_midpoint_certificate.json').read_text())
    axis_terms,axis_hash=axis.terms_from_json();assert axis_hash==source_hash
    families={
        'b2':{ri:[(b,c,w)for a,b,c,w in axis_terms[ri,0]if not a]for ri in range(4)},
        'A_at_one':{ri:[(a+b,c,w)for a,b,c,w in axis_terms[ri,ri]]for ri in range(4)}}
    for name,data in families.items():
        value=axis.integrate_rows(data,axis_cert['n'])
        for key,interval in value.items():assert interval.json()==axis_cert[name][key]
    a2=base.I.rat(0)
    for a,c in a2terms.items():a2+=c*base.root20(a)
    assert a2.json()==axis_cert['a2']
    axis_lower=a2-F(433,1000)*base.root20(F(1,8))-remainder/8
    assert axis_lower.json()==axis_cert['axis_lower_bound']
    assert F(axis_lower.lo,Q)>F(1,40)
    assert F(int(axis_cert['b2']['integral']['lower_numerator']),Q)>-F(433,1000)
    assert int(axis_cert['b2']['integral']['upper_numerator'])<0
    result={
        'status':'PASS',
        'whole_chamber_interface_exact_identities':edge_checks,
        'accepted_x_intervals':len(rows),
        'closed_interval_cover':['1/8','1'],
        'classified_radial_cells':radial_cells,
        'chamber_crossing_radial_cells':boundary_cells,
        'strict_minimum_A_over_x_squared':str(minimum),
        'strict_minimum_decimal_display':float(minimum),
        'strict_target':'1/200',
        'selected_complete_x_boxes_recomputed':rerun,
        'axis_constant_linear_and_quadratic_coefficients':'PASS',
        'axis_remainder_exact':str(remainder),
        'axis_integrals_recomputed':['b2','A(1)'],
        'axis_lower_strictly_above':'1/40',
        'kernel_certificate_source_bindings':len(cert['source_sha256']),
        'triangle_kappa_grid_recomputed':False,
        'full_adaptive_kernel_search_recomputed':False,
        'seconds':time.time()-start,
        'source_sha256':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
            for name in ['certify_integrated_kernel.py','inputs/c86/certify_mellin_integral.py',
                         'positions/certify_axis_midpoint.py','inputs/c86/smallarea/mellin_chambers.json']}}
    (ROOT/'integrated_kernel_independent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':audit()
