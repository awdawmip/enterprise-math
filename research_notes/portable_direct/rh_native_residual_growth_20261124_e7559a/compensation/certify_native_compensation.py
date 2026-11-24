#!/usr/bin/env python3
"""Certify the original 38 packets using psi and exact cumulative kappa.

All admissions use exact rationals and outward fixed-denominator intervals.
Saved ordinary-prime and actual-road certificates are immutable comparison data.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
from math import isqrt
import argparse,hashlib,importlib.util,json


def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def mass(u,v):return F(v-u,u*v)


def exact_pav(A,L):
    pools=[]
    for n,a in enumerate(A,L):
        pools.append([n,n+1,F(a)*mass(n,n+1)])
        while len(pools)>1 and pools[-2][2]/mass(*pools[-2][:2])>pools[-1][2]/mass(*pools[-1][:2]):
            u,v=pools[-2:];pools[-2:]=[[u[0],v[1],u[2]+v[2]]]
    return pools


def exact_R(A,L,x):
    R=L+len(A);a,b=x-L,R-x;h=R-L;pools=exact_pav(A,L)
    crossing=next((p for p in pools if p[0]<x<p[1]),None)
    if crossing is None:return F(0),pools
    u,v,s=crossing;mean=s/mass(u,v)
    S=sum((mass(n,n+1)*(A[n-L]-mean) for n in range(u,x)),F(0))
    return F(h*x,a*b)*S,pools


def stability_checks():
    cases=split_checks=changed_partitions=0
    for h in range(2,7):
        L,R=2,2+h
        bases=([F(0)]*h,[F(n) for n in range(h)],[F(-n) for n in range(h)],
               [F((-1)**n*(n+1)) for n in range(h)])
        eps=[F(1+n%2) for n in range(h-1)]
        for choices in product((-1,0,1),repeat=h-1):
            error=[F(7)] # Deliberately nonzero complete-prefix constant.
            for choice,e in zip(choices,eps):error.append(error[-1]+choice*e)
            for A in bases:
                altered=[u+v for u,v in zip(A,error)]
                old_pav=exact_pav(A,L);new_pav=exact_pav(altered,L)
                changed_partitions+=([p[:2] for p in old_pav]!=[p[:2] for p in new_pav])
                for x in range(L+1,R):
                    old,_=exact_R(A,L,x);new,_=exact_R(altered,L,x)
                    rho=sum(((F(n-L,x-L) if n<=x else F(R-n,R-x))*eps[n-L-1]/n
                             for n in range(L+1,R)),F(0))
                    assert abs(new-old)<=rho
                    split_checks+=1
                cases+=1
    return {'arithmetic':'Exact fractions','lengths':list(range(2,7)),
        'base_sequences':'zero; increasing integers; decreasing integers; alternating signed magnitude',
        'error_increments':'Each independently -epsilon,0,+epsilon; epsilon alternates1,2; prefix constant7',
        'cases':cases,'split_checks':split_checks,'changed_pool_partitions':changed_partitions,'all_passed':True}


def delta_interval(m,n):
    if n<32:return m.sub(m.qmul(m.sub(m.log_int(n+1),m.log_int(n)),n*(n+1)),m.rat(n))
    # Even truncation is above the integral; next odd term is below.
    upper=sum((F((-1)**j,(j+1)*(j+2)*n**j) for j in range(13)),F(0))
    lower=upper-F(1,14*15*n**13)
    return m.rat(lower)[0],m.rat(upper)[1]


def run(previous):
    prior=previous/'prior/riemann_directed_local_20261124'
    m=load_module('compensation_intervals',prior/'prior/riemann_cumulative_haar_20261123/dependencies/certify_fast_harmonic_energy.py')
    geometry=json.loads((prior/'directed_arithmetic/fixed_triangle_geometry.json').read_text())
    arithmetic=json.loads((prior/'directed_arithmetic/local_arithmetic_certificate.json').read_text())
    old=json.loads((previous/'deficit/isotonic_certificate.json').read_text())
    B=max(block['Y'] for block in geometry['blocks'])
    sieve=bytearray(b'\x01')*(B+1);sieve[:2]=b'\0\0'
    for p in range(2,isqrt(B)+1):
        if sieve[p]:sieve[p*p::p]=b'\0'*((B-p*p)//p+1)
    events=[m.ZERO]*(B+1);pp_events=[False]*(B+1);prime_count=pp_count=0
    for p in range(2,B+1):
        if not sieve[p]:continue
        prime_count+=1;lp=m.log_int(p);q=p
        while q<=B:
            events[q]=lp
            if q!=p:pp_events[q]=True;pp_count+=1
            q*=p
    Apsi=[m.ZERO]*(B+1);native=[m.ZERO]*(B+1);deltas=[m.ZERO]*(B+1)
    ps=m.ZERO
    for n in range(1,B+1):
        ps=m.add(ps,events[n]);Apsi[n]=m.sub(ps,m.rat(n))
        deltas[n]=delta_interval(m,n)
        native[n]=m.sub(Apsi[n],deltas[n])
        assert deltas[n][0]>0 and deltas[n][1]<m.rat(F(1,2))[0]
        if n>1:assert deltas[n-1][1]<deltas[n][0]
    assert m.overlap(native[1],m.qmul(m.log_int(2),-2))
    cumulative=m.ZERO
    for n in range(1,101):
        g=lambda k:m.ZERO if k==0 else m.qmul(m.log_int(k),k)
        kappa=m.qmul(m.add(m.sub(g(n+1),m.qmul(g(n),2)),g(n-1)),n)
        cumulative=m.add(cumulative,kappa)
        assert m.overlap(cumulative,m.add(m.rat(n),deltas[n]))
        if n>=2:
            assert kappa[0]>m.S
            assert kappa[1]-m.S<=m.rat(F(1,6*n*(n-1)))[0]
    prefixes={}
    min_L=min(p['L'] for block in geometry['blocks'] for layer in block['levels'] for p in layer['packets'])
    for label,A in [('psi',Apsi),('native',native)]:
        pref=[m.ZERO]*(B+1)
        # Common weighted-prefix constants cancel from every mean difference.
        # Start at the first actual edge to avoid importing irrelevant interval width.
        for n in range(min_L,B):pref[n+1]=m.add(pref[n],m.qmul(A[n],mass(n,n+1)))
        prefixes[label]=pref
    def stats(label,L,x,R):
        pref=prefixes[label]
        def summ(u,v):return m.sub(pref[v],pref[u])
        def mean(u,v):return m.qmul(summ(u,v),1/mass(u,v))
        pools=[]
        for n in range(L,R):
            pools.append([n,n+1,mean(n,n+1)])
            while len(pools)>1:
                u,v=pools[-2:]
                if u[2][1]<=v[2][0]:break
                assert u[2][0]>v[2][1],('ambiguous',label,L,x,R,u,v)
                pools[-2:]=[[u[0],v[1],mean(u[0],v[1])]]
        kkt=0
        for u,v,mm in pools:
            for z in range(u+1,v):
                s=m.sub(summ(u,z),m.qmul(summ(u,v),mass(u,z)/mass(u,v)))
                assert s[0]>=0,('KKT',label,L,x,R,u,z,v,s)
                kkt+=1
        crossing=next((p for p in pools if p[0]<x<p[1]),None)
        if crossing:
            u,v,mm=crossing
            S=m.sub(summ(u,x),m.qmul(summ(u,v),mass(u,x)/mass(u,v)))
            residual=m.qmul(S,F((R-L)*x,(x-L)*(R-x)))
            assert residual[0]>=0
            crossing_out={'u':u,'v':v,'prefix_residual':m.record(S)}
        else:
            residual=m.ZERO;crossing_out=None
        direct=m.qmul(m.sub(mean(L,x),mean(x,R)),1,x)
        assert direct[0]<=residual[1]
        return {'pool_intervals':[[u,v] for u,v,_ in pools],
                'crossing_pool':crossing_out,'residual':m.record(residual),
                'contrast':m.record(direct),'kkt_prefixes':kkt},residual,direct
    blocks=[]
    counts={'packets':0,'psi_pools':0,'native_pools':0,'psi_kkt_prefixes':0,'native_kkt_prefixes':0,
            'theta_boundaries_preserved_in_psi':0,'native_boundaries_preserved_in_psi':0,
            'strict_native_residual_improvement_over_theta':0,'strict_psi_residual_improvement_over_theta':0,
            'native_reference_sign_positive':0,'native_reference_sign_negative':0}
    for block,ob,arith in zip(geometry['blocks'],old['blocks'],arithmetic['blocks']):
        X=block['X'];layers=[]
        for layer,ol,al in zip(block['levels'],ob['levels'],arith['levels']):
            packets=[]
            totals={k:m.ZERO for k in ['theta_residual_square','psi_residual_square','native_residual_square',
                                     'native_reference_positive_square','native_residual_plus_matching_square',
                                     'theta_residual_plus_kappa_square','psi_residual_plus_kappa_square',
                                     'psi_residual_plus_pp_square']}
            for p,op,ap in zip(layer['packets'],ol['packets'],al['packets']):
                L,x,R=p['L'],p['x'],p['R'];a,b,h=x-L,R-x,R-L;factor=F(h**3,X**2)
                sp,rp,tp=stats('psi',L,x,R);sk,rk,tk=stats('native',L,x,R)
                rt=m.ZERO if op['crossing_pool'] is None else m.qmul(m.decode(op['crossing_pool']['prefix_residual']),F(h*x,a*b))
                K=m.decode(ap['kappa_minus_one_tent_mass']);Q=m.decode(ap['higher_prime_power_tent_mass'])
                rho=m.decode(ap['local_matching_radius'])
                assert m.overlap(tk,m.decode(ap['reference']))
                assert m.overlap(m.add(tp,K),tk)
                assert m.overlap(m.add(tp,Q),m.decode(ap['prime_only_tent_deficit']))
                assert K[1]<=m.rat(F(h,12*L*(L+1)**2))[0]
                theta_boundaries={v for _,v in op['pool_intervals'][:-1]}
                psi_boundaries={v for _,v in sp['pool_intervals'][:-1]}
                native_boundaries={v for _,v in sk['pool_intervals'][:-1]}
                assert theta_boundaries<=psi_boundaries and native_boundaries<=psi_boundaries
                # Analytic comparison is (3.1). These checks also exclude a separated numerical contradiction.
                assert rp[0]<=rt[1] and rt[0]<=m.add(rp,Q)[1]
                assert rp[0]<=rk[1] and rk[0]<=m.add(rp,K)[1]
                assert m.decode(ap['actual_enclosure'])[0]<=m.add(rk,rho)[1]
                counts['strict_native_residual_improvement_over_theta']+=rk[1]<rt[0]
                counts['strict_psi_residual_improvement_over_theta']+=rp[1]<rt[0]
                counts['native_reference_sign_positive']+=tk[0]>0
                counts['native_reference_sign_negative']+=tk[1]<0
                counts['packets']+=1
                for label,s in [('psi',sp),('native',sk)]:
                    counts[label+'_pools']+=len(s['pool_intervals'])
                    counts[label+'_kkt_prefixes']+=s['kkt_prefixes']
                counts['theta_boundaries_preserved_in_psi']+=len(theta_boundaries)
                counts['native_boundaries_preserved_in_psi']+=len(native_boundaries)
                vals={'theta_residual_square':rt,'psi_residual_square':rp,'native_residual_square':rk,
                      'native_reference_positive_square':m.positive(tk),
                      'native_residual_plus_matching_square':m.add(rk,rho),
                      'theta_residual_plus_kappa_square':m.add(rt,K),
                      'psi_residual_plus_kappa_square':m.add(rp,K),
                      'psi_residual_plus_pp_square':m.add(rp,Q)}
                for key,value in vals.items():totals[key]=m.add(totals[key],m.qmul(m.square(value),factor))
                packets.append({**p,'theta_residual':m.record(rt),'psi':sp,'native':sk,
                    'K':m.record(K),'Q_pp':m.record(Q),'local_matching_radius':m.record(rho),
                    'background_upper_rational':str(F(h,12*L*(L+1)**2)),
                    'exact_compensation_theorem_applied':True,'strict_native_residual_improvement':rk[1]<rt[0]})
            layers.append({'level':layer['level'],'squared_budgets':{k:m.record(v) for k,v in totals.items()},'packets':packets})
        blocks.append({'X':X,'Y':block['Y'],'levels':layers})
    return {'schema':'RH_NATIVE_CUMULATIVE_COMPENSATION_V1','status':'PASS',
            'scope':'Author exact/interval validation on the unchanged original38 packets; no unbounded arithmetic theorem.',
            'arithmetic':{'decimal_digits':m.DIGITS,'prime_sieve_limit':B,'ordinary_primes':prime_count,
                'higher_prime_power_events':pp_count,'delta_method':'Exact logs for n<32; rational alternating integral series through degree12 plus next-term enclosure thereafter',
                'new_D_queries':0,'new_q_queries':0,'admission':'Exact rationals and outward integer intervals; no floating decisions'},
            'native_identity_checks':{'cumulative_kappa_identities':100,'background_increment_bounds':99,
                'delta_positivity_and_upper_half':B,'delta_strict_increase':B-1,'unit_value':'E*_1=-2log2'},
            'matching_stability_checks':stability_checks(),'counts':counts,'blocks':blocks}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=Path,required=True)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('native_compensation_certificate.json'))
    args=parser.parse_args();result=run(args.previous)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    summary=[{'X':b['X'],'level':l['level'],**{k:v['upper'] for k,v in l['squared_budgets'].items()}}
             for b in result['blocks'] for l in b['levels']]
    print(json.dumps({'status':result['status'],'counts':result['counts'],
                     'matching_stability_checks':result['matching_stability_checks'],'layers':summary},ensure_ascii=False))


if __name__=='__main__':main()
