#!/usr/bin/env python3
"""Exact interface checks for the P11 infinite-family proof, not a census/proof by sampling."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from functools import reduce
from math import gcd, lcm
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parent
SEEDS = (((11,8), (176,57,185,105,208,56)),
         ((17,16), (2720,165,2725,1533,2444,2044)))


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def load_sources():
    manifest = json.loads((ROOT / 'REUSED_SOURCES.json').read_text())
    loaded = []
    for index, item in enumerate(manifest['files']):
        path = ROOT / item['filename']
        data = path.read_bytes()
        require(hashlib.sha256(data).hexdigest() == item['sha256'], 'source SHA256 mismatch')
        require(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest() == item['git_blob'],
                'source Git blob mismatch')
        spec = importlib.util.spec_from_file_location('p11_frozen_'+str(index), path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        loaded.append(module)
    return manifest, loaded[0], loaded[1]


def core_values(core, spinor):
    r,s = core
    require(r>s>0 and gcd(r,s)==1 and (r-s)%2==1, 'invalid primitive Euclidean core')
    A,B,C = spinor.rotation_triple(core)
    require(A*A+B*B==C*C and gcd(gcd(A,B),C)==1, 'core interface mismatch')
    return A,B,C,A+B,abs(A-B)


def on_curve(point, P, Q):
    if point is None:
        return True
    x,y = point
    return y*y==x*(x-P*P)*(x-Q*Q)


def add(left, right, P, Q):
    if left is None: return right
    if right is None: return left
    x,y = left; u,v = right
    S = P*P+Q*Q
    if x==u and y==-v:
        return None
    if x==u:
        require(y==v and y!=0, 'invalid doubling input')
        slope=(3*x*x-2*S*x+P*P*Q*Q)/(2*y)
    else:
        slope=(v-y)/(u-x)
    xx=slope*slope+S-x-u
    answer=(xx,-y+slope*(x-xx))
    require(on_curve(answer,P,Q), 'group law output off curve')
    return answer


def to_curve(triple, P, Q):
    D,U,V = triple
    require(D*D+U*U==P*P and D*D+V*V==Q*Q, 'fiber equations failed')
    T=U+V; Y=2*T*D; a=P+Q; R=P*Q
    require(T!=0 and a!=T, 'outside affine birational domain')
    require(Y*Y==(a*a-T*T)*(T*T-(P-Q)**2), 'quartic identity failed')
    point=(R*(a+T)/(a-T),a*R*Y/(a-T)**2)
    require(on_curve(point,P,Q), 'birational forward map failed')
    return point


def from_curve(point, P, Q):
    require(point is not None and on_curve(point,P,Q), 'invalid affine curve point')
    x,y=point; a=P+Q; R=P*Q
    require(x+R!=0, 'inverse denominator is zero')
    T=a*(x-R)/(x+R); Y=4*a*R*y/(x+R)**2
    require(T!=0, 'inverse T is zero')
    triple=(Y/(2*T),(T+F(P*P-Q*Q,1)/T)/2,(T-F(P*P-Q*Q,1)/T)/2)
    D,U,V=triple
    require(D*D+U*U==P*P and D*D+V*V==Q*Q, 'inverse fiber equations failed')
    require(to_curve(triple,P,Q)==point, 'exact round trip failed')
    return triple


def encode(value):
    if isinstance(value,F): return f'{value.numerator}/{value.denominator}'
    if isinstance(value,tuple) or isinstance(value,list): return [encode(x) for x in value]
    if isinstance(value,dict): return {str(k):encode(v) for k,v in value.items()}
    return value


def primitive_reconstruct(core, triple, parent, spinor):
    A,B,C,P,Q=core_values(core,spinor)
    D,U,V=triple
    positive=tuple(abs(t) for t in triple)
    dbar,ubar,vbar=positive
    require(0<dbar<Q and ubar>0 and vbar>0, 'not in strict positive task chamber')
    denominators=[x.denominator for x in positive]
    L=lcm(*denominators); clearing_scale=2*L
    raw=(clearing_scale*max(A,B),clearing_scale*min(A,B),clearing_scale*C,
         clearing_scale*dbar,clearing_scale*ubar,clearing_scale*vbar)
    require(all(F(v).denominator==1 for v in raw), 'denominator clearing failed')
    raw=tuple(int(v) for v in raw)
    parent.verify_point(raw)
    raw_roots=parent.fixed_outer_roots(raw)
    divisor=parent.root_gcd(raw)
    require(clearing_scale%divisor==0, 'root gcd does not divide core scale')
    require(all(v%divisor==0 for v in raw), 'primitive division not integral')
    final=tuple(v//divisor for v in raw)
    parent.verify_point(final)
    require(parent.root_gcd(final)==1, 'result is not outer-root primitive')
    roots=parent.fixed_outer_roots(final)
    require(roots==[r//divisor for r in raw_roots], 'root scaling does not commute')
    k=clearing_scale//divisor
    recovered=(F(final[3],k),F(final[4],k),F(final[5],k))
    require(recovered==positive, 'normalized rational triple was erased')
    require(F(final[0],max(A,B))==F(final[1],min(A,B))==F(final[2],C)==k,
            'core/scale readback failed')
    return {'core':core,'A_B_C':(A,B,C),'P_Q':(P,Q),'raw_signed_triple':triple,
            'signs':tuple(1 if x>0 else -1 for x in triple),'denominators':denominators,
            'initial_clearing_scale':clearing_scale,'outer_root_gcd_before':divisor,
            'final_scale':k,'primitive_sextuple':final,'outer_roots':roots,
            'outer_root_gcd_after':1,'recovered_positive_normalized_triple':recovered}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'RUN.json')
    args=parser.parse_args()
    manifest,parent,spinor=load_sources()
    seed_records=[]
    for core,datum in SEEDS:
        A,B,C,P,Q=core_values(core,spinor)
        parent.verify_point(datum)
        require(parent.root_gcd(datum)==1, 'known witness is not primitive')
        k=F(datum[2],C)
        require(k.denominator==1, 'seed scale is nonintegral')
        triple=tuple(F(value,1)/k for value in datum[3:])
        point=to_curve(triple,P,Q)
        require(from_curve(point,P,Q)==triple, 'known witness round trip failed')
        rec=primitive_reconstruct(core,triple,parent,spinor)
        require(rec['primitive_sextuple']==datum, 'known witness primitive normalization changed')
        rec['elliptic_point']=point
        seed_records.append(rec)

    core=(11,8); A,B,C,P,Q=core_values(core,spinor)
    seed=to_curve((F(105),F(208),F(56)),P,Q)
    require(seed==(F(194089),F(69872040)), 'explicit seed mismatch')
    cubic_disc=P**4*Q**4*(P*P-Q*Q)**2
    require(seed[1]!=0 and seed[1].denominator==1 and seed[1].numerator%5==0,
            'Nagell-Lutz numerator condition failed')
    require(cubic_disc%5!=0, 'Nagell-Lutz cubic discriminant not a 5-unit')
    R=P*Q; S=P*P+Q*Q
    short_A=27*(3*R*R-S*S); short_B=27*(9*R*R*S-2*S**3)
    X=9*seed[0]-3*S; Y=27*seed[1]
    short_disc=-16*(4*short_A**3+27*short_B**2)
    require(Y*Y==X**3+short_A*X+short_B, 'short-form seed transform failed')
    require(short_disc==3**12*16*cubic_disc and short_disc%5!=0,
            'short discriminant scaling failed')
    fp5_affine=[(x,y) for x in range(5) for y in range(5)
                if (y*y-x*(x-P*P)*(x-Q*Q))%5==0]
    require(len(fp5_affine)+1==8, 'exact good-reduction F5 point count failed')

    samples=[];current=None
    for n in (1,2,3):
        current=add(current,seed,P,Q)
        require(current is not None and current[1]!=0, 'unexpected torsion/boundary sample')
        triple=from_curve(current,P,Q)
        rec=primitive_reconstruct(core,triple,parent,spinor)
        rec['n']=n;rec['elliptic_point']=current;samples.append(rec)
    require(len({r['primitive_sextuple'] for r in samples})==3, 'sample outputs collided')

    # Precisely targeted bad-interface checks, not a broader search.
    wrong_eta=(seed[0],seed[1]/2)
    require(not on_curve(wrong_eta,P,Q), 'wrong eta normalization was not detected')
    rejected_boundary=False
    try:
        primitive_reconstruct(core,(F(0),F(P),F(Q)),parent,spinor)
    except AssertionError:
        rejected_boundary=True
    require(rejected_boundary, 'D=0 elliptic origin entered strict P11 family')
    second=samples[1]
    naive_gcd=reduce(gcd,second['primitive_sextuple'])
    require(naive_gcd==2 and second['outer_root_gcd_after']==1,
            'expected six-coordinate-gcd distinction disappeared')
    naive_rejected=False
    try:
        parent.verify_point(tuple(v//naive_gcd for v in second['primitive_sextuple']))
    except AssertionError:
        naive_rejected=True
    require(naive_rejected, 'naive coordinate-gcd quotient was falsely admitted')
    d,mu,nu=second['primitive_sextuple'][3:]
    scale_erasure_detected=(d*d+mu*mu!=P*P or d*d+nu*nu!=Q*Q)
    require(scale_erasure_detected, 'dropping retained scale was invisible')
    sign_erasure_detected=(to_curve(tuple(abs(t) for t in second['raw_signed_triple']),P,Q)
                           !=second['elliptic_point'])
    require(sign_erasure_detected, 'dropping raw sign provenance was invisible')

    result={'status':'PASS','scope':'FINITE_INTERFACE_VALIDATION_NOT_PROOF_BY_SAMPLING',
            'source_commit':manifest['source_commit'],'known_witnesses':seed_records,
            'multipliers_checked':[1,2,3],'family_samples':samples,
            'nontorsion_certificate':{'seed':seed,'prime':5,'eta_mod_5':0,
                                     'cubic_discriminant_mod_5':cubic_disc%5,
                                     'short_A':short_A,'short_B':short_B,'short_seed':(X,Y),
                                     'short_discriminant_mod_5':short_disc%5,
                                     'theorem_required':'Classical (generalized or integral-short) Nagell-Lutz'},
            'good_reduction_F5':{'prime':5,'cubic_discriminant_mod_5':cubic_disc%5,
                                 'affine_points':fp5_affine,'point_at_infinity_count':1,
                                 'group_order':len(fp5_affine)+1,'finite_domain':'all 25 ordered pairs in F5^2'},
            'reuse_resolution':'REUSE_EXECUTED',
            'reused_functions':['fixed_outer_roots','root_gcd','verify_point','rotation_triple'],
            'prior_census_executed':False,'negative_controls':{'wrong_eta_factor_detected':True,
                                                             'zero_D_boundary_rejected':True,
                                                             'six_coordinate_gcd':naive_gcd,
                                                             'actual_outer_root_gcd':1,
                                                             'naive_gcd_quotient_rejected':naive_rejected,
                                                             'dropping_scale_detected':scale_erasure_detected,
                                                             'dropping_raw_signs_detected':sign_erasure_detected},
            'proof_boundary':'Infinitude and all-n strict reconstruction follow from FAMILY.md, not three examples.'}
    args.output.write_text(json.dumps(encode(result),indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','known_witnesses':2,'family_multipliers':[1,2,3],
                      'outer_root_primitive':True,'finite_validation_only':True,'output':str(args.output)}))


if __name__=='__main__':main()
