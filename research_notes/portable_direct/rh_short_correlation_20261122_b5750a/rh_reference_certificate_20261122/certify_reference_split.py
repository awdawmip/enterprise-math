#!/usr/bin/env python3
"""Separate finite thickness error from the actual arithmetic triangle source.

The original complete road is reused. Lambda is an explicitly auxiliary
comparison readout, not a replacement for the native road or ontology.
All certified arithmetic uses the existing 10**60 outward integer intervals.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import pickle
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT/'rh_joint_certificate'))
sys.path.insert(0, str(ROOT/'rh_triangle_certificate_20261122'))
from certify_joint_energy import (A, B, H, SCALE, DIGITS, ZERO, ONE,
    Elementary, add, sub, neg, scale, mul, rat, square, positive,
    sqrt_interval, isum, record, energy, intersects, linear_sieve,
    interval_from_record, green_apply)
from certify_dyadic_triangles import phi, T, interpolate, charges_at, abs_interval


def ipow(v, k):
    out=ONE
    for _ in range(k):
        out=mul(out,v)
    return out


def pairwise_intersection(values):
    return max(v[0] for v in values)<=min(v[1] for v in values)


def scalar_max(values):
    return max(v[0] for v in values),max(v[1] for v in values)


def main():
    started=time.perf_counter()
    cache=ROOT/'rh_joint_certificate/_scratch_arrays.pkl'
    road_recomputed=False
    if not cache.exists():
        subprocess.run([sys.executable,str(ROOT/'rh_joint_certificate/certify_joint_energy.py')],check=True)
        road_recomputed=True
    data=pickle.loads(cache.read_bytes())
    assert (data['A'],data['B'],data['H'],data['DIGITS'])==(A,B,H,DIGITS)
    tree_path=ROOT/'rh_triangle_certificate_20261122/dyadic_triangle_certificate.json'
    fixed_path=ROOT/'rh_correlation_rational/rational_window_certificate.json'
    tree=json.loads(tree_path.read_bytes())
    fixed=json.loads(fixed_path.read_bytes())
    cuts=tree['partition']['fine_nodes']
    backbone=tree['partition']['backbone']
    el=Elementary()
    spf,mu=linear_sieve(B)
    primes=[n for n in range(2,B+1) if spf[n]==n]
    prime_logs={p:el.log_integer(p) for p in primes}
    logs=[ZERO]*(B+1)
    Lambda=[ZERO]*(B+1)
    prime_power_count=0
    for n in range(2,B+1):
        logs[n]=add(logs[n//spf[n]],prime_logs[spf[n]])
    for p in primes:
        n=p
        while n<=B:
            Lambda[n]=prime_logs[p]
            prime_power_count+=1
            n*=p
    e=[sub(data['D'][n],Lambda[n]) for n in range(B+1)]
    coeff=F(fixed['node_certificate']['derivative_error_coefficient_exact'])
    m=len(data['nodes'])
    eta={n:scale(ipow(logs[n],m+1),coeff) for n in sorted(set(backbone+[H,B]))}
    eta_B=eta[B]
    assert eta_B[1] <= rat(F(fixed['node_certificate']['pointwise_eta_uniform_n_le_Z']['upper']))[1]
    eabs=[abs_interval(v) for v in e[1:]]
    max_e=scalar_max(eabs)
    max_e_n=max(range(1,B+1),key=lambda n:abs_interval(e[n])[1])
    assert max_e[1] <= eta_B[1]

    # Full prefix, including the original n=1 port and gamma-containing affine
    # history. Only the arithmetic summand changes in this auxiliary comparison.
    E=[ZERO]*(B+1)
    sum_e=sum_e_over_n=ZERO
    qstar=[ZERO]*(B+1)
    for n in range(1,B+1):
        sum_e=add(sum_e,e[n])
        sum_e_over_n=add(sum_e_over_n,scale(e[n],F(1,n)))
        E[n]=sub(scale(sum_e_over_n,n),sum_e)
        qstar[n]=sub(data['q'][n],E[n])
    fstar=[ZERO]+[scale(sub(data['kappa'][n],Lambda[n]),F(1,n)) for n in range(1,B+1)]
    assert all(intersects(sub(scale(qstar[n],2),add(qstar[n-1],qstar[n+1])),fstar[n])
               for n in range(2,B))

    # The full Mobius convolution is evaluated, not a prime-only restriction.
    c_actual=[ZERO]*(B+1)
    mu_kappa=[ZERO]*(B+1)
    dc=[ZERO]*(B+1)
    mu_Lambda=[ZERO]*(B+1)
    Dmk=[sub(data['D'][n],data['kappa'][n]) for n in range(B+1)]
    for d in range(1,B+1):
        if not mu[d]:
            continue
        for n in range(d,B+1,d):
            k=n//d
            c_actual[n]=add(c_actual[n],scale(Dmk[k],mu[d]))
            mu_kappa[n]=add(mu_kappa[n],scale(data['kappa'][k],mu[d]))
            dc[n]=add(dc[n],scale(e[k],mu[d]))
            mu_Lambda[n]=add(mu_Lambda[n],scale(Lambda[k],mu[d]))
    cstar=[ZERO]+[sub(scale(logs[n],-mu[n]),mu_kappa[n]) for n in range(1,B+1)]
    assert all(intersects(mu_Lambda[n],scale(logs[n],-mu[n])) for n in range(1,B+1))
    assert all(intersects(sub(c_actual[n],cstar[n]),dc[n]) for n in range(1,B+1))
    assert all(intersects(c_actual[n],data['c'][n]) for n in range(1,H+1))
    nonsf=[n for n in range(1,B+1) if mu[n]==0]
    assert all(dc[n][0]<=0<=dc[n][1] for n in nonsf)
    assert all(scale(dc[n],mu[n])[0]>0 for n in range(2,B+1) if mu[n])
    max_dc=scalar_max([abs_interval(v) for v in dc[1:]])
    max_dc_n=max(range(1,B+1),key=lambda n:abs_interval(dc[n])[1])
    assert all(abs_interval(dc[n])[1]<=scale(ipow(logs[n],m+1),coeff)[1]
               for n in range(2,B+1) if mu[n])
    signed_error_samples=[]
    for n in [2,3,6,30,210,2310,30030,32767]:
        Psi=isum(scale(sub(ONE,el.exp_negative(scale(logs[n],a))),weight/a)
                 for a,weight in zip(data['nodes'],data['weights']))
        I=sub(logs[n],Psi)
        prediction=scale(I,mu[n])
        assert pairwise_intersection([dc[n],sub(c_actual[n],cstar[n]),prediction])
        assert I[0]>0 and I[1]<=scale(ipow(logs[n],m+1),coeff)[1]
        signed_error_samples.append({'n':n,'mu':mu[n],'delta_c':record(dc[n]),'I_log_n':record(I),
                                     'mu_I_prediction':record(prediction)})

    harmonic=[ZERO]
    for n in range(1,B+1):
        harmonic.append(add(harmonic[-1],rat(F(1,n))))
    sigma_actual=isum(scale(c_actual[d],F(1,d)) for d in range(1,H+1))
    sigma_star=isum(scale(cstar[d],F(1,d)) for d in range(1,H+1))
    dsigma=isum(scale(dc[d],F(1,d)) for d in range(1,H+1))
    assert intersects(dsigma,sub(sigma_actual,sigma_star))

    def phase_endpoint(coeffs,n):
        terms=[]
        for d in range(2,H+1):
            Pd=add(scale(sub(sub(harmonic[n],harmonic[n//d]),logs[d]),F(n,d)),
                   rat(F(d-1-2*(n%d),2*d)))
            terms.append(mul(coeffs[d],Pd))
        return isum(terms)

    dmean=isum(scale(dc[d],F(1,d)) for d in range(2,H+1))
    dcorr_num=[neg(dmean)]*(B+1)
    for d in range(2,H+1):
        for n in range(d,B+1,d):
            dcorr_num[n]=add(dcorr_num[n],dc[d])
    dcorr=[ZERO]+[scale(dcorr_num[n],F(1,n)) for n in range(1,B+1)]
    dP=green_apply(dcorr,A,B,phase_endpoint(dc,A),phase_endpoint(dc,B))
    Pstar=[ZERO]*(B+1)
    Qstar=[ZERO]*(B+1)
    for n in range(A,B+1):
        Pstar[n]=sub(data['P'][n],dP[n])
        Qstar[n]=add(qstar[n],Pstar[n])
    fQstar=[sub(data['corrected_source'][n],add(scale(neg(e[n]),F(1,n)),dcorr[n]))
             if n else ZERO for n in range(B+1)]
    tail_a=[ZERO]*(B+1);tail_s=[ZERO]*(B+1)
    for d in range(H+1,B+1):
        for n in range(d,B+1,d):
            tail_a[n]=add(tail_a[n],c_actual[d])
            tail_s[n]=add(tail_s[n],cstar[d])
    assert all(intersects(fQstar[n],scale(neg(add(sigma_star,tail_s[n])),F(1,n)))
               for n in range(A+1,B))
    assert all(intersects(sub(scale(Qstar[n],2),add(Qstar[n-1],Qstar[n+1])),fQstar[n])
               for n in range(A+1,B))

    epsilon_checks=[]
    for N in [1,2,H,A,8192,B]:
        direct=isum(sub(data['kappa'][n],ONE) for n in range(1,N+1))
        closed=sub(scale(el.log_unit(rat(F(N+1,N))),N*(N+1)),rat(N))
        assert intersects(direct,closed)
        remainder=sub(rat(F(1,2)),closed)
        assert remainder[0]>0
        epsilon_checks.append({'N':N,'epsilon_mass_direct':record(direct),'epsilon_mass_closed':record(closed),
                               'epsilon_mass_infinite_tail':record(remainder)})

    results={'schema':'EM_ACTUAL_REFERENCE_SPLIT_V1','status':'PASS',
        'scope':'One actual complete matched road and an auxiliary Lambda comparison; no replacement of native semantics and no unbounded arithmetic claim.',
        'window':{'A':A,'B':B,'H':H,'theta':'1/2','full_prefix_n':B,'closed_integer_count':B-A+1},
        'arithmetic':{'denominator_power_of_10':DIGITS,'method':'outward integer intervals; rational coefficients exact'},
        'inputs':[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
                  for p in [tree_path,fixed_path,ROOT/'rh_joint_certificate/certify_joint_energy.py',ROOT/'rh_triangle_certificate_20261122/certify_dyadic_triangles.py',ROOT/'rh_correlation_rational/certify_matched_nodes.py']],
        'cache':{'path':str(cache.relative_to(ROOT)),'sha256':hashlib.sha256(cache.read_bytes()).hexdigest(),'full_road_recomputed_this_run':road_recomputed},
        'reference_definition':{'Lambda':'Lambda(p^k)=log p; zero at all other integers including 1',
            'q_star':'q-E, E(y)=sum_(2<=n<=y)(D_n-Lambda_n)(y/n-1); same complete prefix and affine history',
            'c_star':'-mu(n) log n-(mu*kappa)(n)=-mu(n)log n-delta_1(n)-(mu*epsilon)(n)',
            'delta_c':'mu*(D-Lambda)=mu(n) I(log n); exact zero for nonsquarefree n',
            'delta_c_proof':'R_a=1*(mu n^(-a)); D=sum(nu/a)R_a-K delta_1, K=sum(nu/a); hence mu*D=-mu Psi(log n), and mu*Lambda=-mu log n. Numerical interval containment is a consistency check, not the proof of exact zero.',
            'prime_count':len(primes),'prime_power_count':prime_power_count},
        'pointwise_matching':{'eta_B':record(eta_B),'max_abs_D_minus_Lambda':record(max_e),'max_at_n':max_e_n,
            'max_abs_delta_c':record(max_dc),'max_delta_c_at_n':max_dc_n,
            'eta_to_actual_max_ratio':record((eta_B[0]*SCALE//max_e[1],(eta_B[1]*SCALE+max_e[0]-1)//max_e[0])),
            'nonsquarefree_exact_zero_error_supported_by_identity_count':len(nonsf),
            'every_nonsquarefree_delta_c_interval_contains_zero':True,
            'every_squarefree_n_ge_2_delta_c_has_mu_sign':True,
            'every_squarefree_delta_c_within_eta_log_n':True,
            'direct_Psi_identity_samples':len(signed_error_samples),
            'signed_error_samples':signed_error_samples},
        'epsilon_checks':epsilon_checks,
        'sigma':{'actual':record(sigma_actual),'reference':record(sigma_star),'difference':record(dsigma)},
        'prefix_error':{'energy_closed':record(energy(E)),'max_abs_over_sqrt_n':record(scalar_max([
            (abs_interval(E[n])[0]*SCALE//sqrt_interval(rat(n))[1],
             (abs_interval(E[n])[1]*SCALE+sqrt_interval(rat(n))[0]-1)//sqrt_interval(rat(n))[0]) for n in range(A,B+1)])),
            'true_dyadic_samples':[{'n':n,'q':record(data['q'][n]),'q_star':record(qstar[n]),'difference_E':record(E[n]),
                'eta_n_n_log_n_upper':record(scale(mul(eta[n],logs[n]),n))} for n in backbone]},
        'phase_error':{'dP_energy_closed':record(energy(dP)),'dP_at_A':record(dP[A]),'dP_at_B':record(dP[B])},
        'energies':{'q':record(energy(data['q'],mode='positive')),'q_star':record(energy(qstar,mode='positive')),
                    'Q':record(energy(data['Q'],mode='positive')),'Q_star':record(energy(Qstar,mode='positive'))},
        'blocks':[], 'negative_packet_retention':{},
    }
    packet_rows=[]
    for bidx,block in enumerate(tree['roads']['q']['dyadic_blocks']):
        X,Y=block['X'],block['Y']; outblock={'X':X,'Y':Y,'layers':[]}
        for lidx,layer in enumerate(block['levels']):
            delta=layer['delta_max_support_length']
            sq_a=sq_s=sqerr=ZERO
            sig_a=tail_sq_a=cross_a=sig_s=tail_sq_s=cross_s=ZERO
            q_signed_sq_a=q_signed_sq_s=ZERO
            outlayer={'level':layer['level'],'delta':delta,'packets':[]}
            for pidx,packet in enumerate(layer['packets']):
                L,x,R=[packet[k] for k in ('L','x','R')];h=R-L
                K1=isum(rat(phi(L,x,R,n)/n) for n in range(L+1,R))
                t_actual=interval_from_record(packet['signed_charge'])
                t_star=isum(scale(fstar[n],phi(L,x,R,n)) for n in range(L+1,R))
                dt=isum(scale(neg(e[n]),phi(L,x,R,n)/n) for n in range(L+1,R))
                assert pairwise_intersection([dt,sub(t_actual,t_star),
                    sub(scale(sub(E[x],E[L]),F(1,x-L)),scale(sub(E[R],E[x]),F(1,R-x)))])
                eta_R=scale(ipow(logs[R],m+1),coeff)
                bound=mul(eta_R,K1)
                assert abs_interval(dt)[1] <= bound[1]
                sq_a=add(sq_a,scale(square(positive(t_actual)),F(h**3,X**2)))
                sq_s=add(sq_s,scale(square(positive(t_star)),F(h**3,X**2)))
                sqerr=add(sqerr,scale(square(dt),F(h**3,X**2)))
                sa=neg(mul(sigma_actual,K1));ss=neg(mul(sigma_star,K1))
                ra=isum(scale(neg(tail_a[n]),phi(L,x,R,n)/n) for n in range(L+1,R))
                rs=isum(scale(neg(tail_s[n]),phi(L,x,R,n)/n) for n in range(L+1,R))
                tQa=interval_from_record(tree['roads']['Q']['dyadic_blocks'][bidx]['levels'][lidx]['packets'][pidx]['signed_charge'])
                tQs=isum(scale(fQstar[n],phi(L,x,R,n)) for n in range(L+1,R))
                assert intersects(add(sa,ra),tQa) and intersects(add(ss,rs),tQs)
                delta_sigma_term=neg(mul(dsigma,K1))
                delta_tail_term=isum(scale(neg(sub(tail_a[n],tail_s[n])),phi(L,x,R,n)/n)
                                    for n in range(L+1,R))
                assert pairwise_intersection([sub(tQa,tQs),add(delta_sigma_term,delta_tail_term),
                                              add(sub(sa,ss),sub(ra,rs))])
                sig_a=add(sig_a,square(sa));tail_sq_a=add(tail_sq_a,square(ra));cross_a=add(cross_a,scale(mul(sa,ra),2))
                sig_s=add(sig_s,square(ss));tail_sq_s=add(tail_sq_s,square(rs));cross_s=add(cross_s,scale(mul(ss,rs),2))
                q_signed_sq_a=add(q_signed_sq_a,square(tQa));q_signed_sq_s=add(q_signed_sq_s,square(tQs))
                row={'L':L,'x':x,'R':R,'h':h,'level':layer['level'],'X':X,
                    'q_triangle_actual':record(t_actual),'q_triangle_reference':record(t_star),'q_triangle_error':record(dt),
                    'error_eta_R_K1_bound':record(bound),'K1':record(K1),
                    'Q_triangle_actual':record(tQa),'Q_triangle_reference':record(tQs),
                    'actual_sigma_term':record(sa),'reference_sigma_term':record(ss),
                    'actual_tail_term':record(ra),'reference_tail_term':record(rs),
                    'sigma_term_actual_minus_reference':record(delta_sigma_term),
                    'tail_term_actual_minus_reference':record(delta_tail_term),
                    'Q_triangle_error':record(sub(tQa,tQs)),
                    'original_and_reference_sign_same':(t_actual[0]>0 and t_star[0]>0) or (t_actual[1]<0 and t_star[1]<0)}
                outlayer['packets'].append(row);packet_rows.append(row)
            norm_a,norm_s,norm_err=map(sqrt_interval,(sq_a,sq_s,sqerr))
            change=abs_interval(sub(norm_a,norm_s))
            # The stable sufficient bound uses the layer's actual packet lengths.
            sharp_bound_sq=isum(scale(square(interval_from_record(p['error_eta_R_K1_bound'])),F(p['h']**3,X**2)) for p in outlayer['packets'])
            assert change[0]<=norm_err[1] and norm_err[1]<=sqrt_interval(sharp_bound_sq)[1]
            outlayer.update({'weighted_positive_coefficient_square_actual':record(sq_a),
                'weighted_positive_coefficient_square_reference':record(sq_s),
                'weighted_coefficient_error_square':record(sqerr),
                'positive_root_diagnostic_change':record(change),
                'error_root_eta_bound':record(sqrt_interval(sharp_bound_sq)),
                'Q_signed_charge_square_actual':record(q_signed_sq_a),
                'Q_signed_charge_square_reference':record(q_signed_sq_s),
                'Q_actual_cross':{'sigma_sq':record(sig_a),'tail_sq':record(tail_sq_a),'twice_cross':record(cross_a)},
                'Q_reference_cross':{'sigma_sq':record(sig_s),'tail_sq':record(tail_sq_s),'twice_cross':record(cross_s)},
                'Q_paired_cross_difference':{'sigma_sq':record(sub(sig_a,sig_s)),
                    'tail_sq':record(sub(tail_sq_a,tail_sq_s)),'twice_cross':record(sub(cross_a,cross_s))}})
            assert intersects(add(add(sig_a,tail_sq_a),cross_a),q_signed_sq_a)
            assert intersects(add(add(sig_s,tail_sq_s),cross_s),q_signed_sq_s)
            outblock['layers'].append(outlayer)
        results['blocks'].append(outblock)

    # Retain selected already-known negative packets directly, without a new
    # phase correction. These are monotone finite envelopes on the fixed tree.
    J=interpolate(data['q'],backbone)
    Jstar=interpolate(qstar,backbone)
    qcharges=charges_at(data['q'],backbone); scharges=charges_at(qstar,backbone)
    Qcharges=charges_at(data['Q'],backbone); SQcharges=charges_at(Qstar,backbone)
    Echarges=charges_at(E,backbone)
    deltaQ=[add(E[n],dP[n]) for n in range(B+1)]
    deltaQcharges=charges_at(deltaQ,backbone)
    skeleton_rows=[]
    for L,x,R in zip(backbone,backbone[1:],backbone[2:]):
        source_difference=isum(scale(neg(e[n]),phi(L,x,R,n)/n) for n in range(L+1,R))
        Q_source_difference=isum(scale(sub(data['corrected_source'][n],fQstar[n]),phi(L,x,R,n))
                                for n in range(L+1,R))
        assert pairwise_intersection([sub(qcharges[x],scharges[x]),Echarges[x],source_difference])
        assert pairwise_intersection([sub(Qcharges[x],SQcharges[x]),deltaQcharges[x],Q_source_difference])
        skeleton_rows.append({'L':L,'x':x,'R':R,'q_charge':record(qcharges[x]),'q_reference_charge':record(scharges[x]),
            'q_charge_difference':record(source_difference),'Q_charge':record(Qcharges[x]),
            'Q_reference_charge':record(SQcharges[x]),'Q_charge_difference':record(Q_source_difference)})
    results['skeleton']={'nodes':backbone,'charges':skeleton_rows,
        'J_positive_energy_closed':record(energy(J,mode='positive')),
        'J_reference_positive_energy_closed':record(energy(Jstar,mode='positive')),
        'J_difference_energy_closed':record(energy([sub(J[n],Jstar[n]) for n in range(B+1)])),
        'all_slope_jump_differences_equal_full_source_hat_moments':True}
    I=interpolate(data['q'],cuts)
    P=[sub(data['q'][n],I[n]) if A<=n<=B else ZERO for n in range(B+1)]
    fine_energy=energy(P,A+1,B-1,'positive')
    endpoint_energy=add(scale(square(positive(data['q'][A])),F(1,A*A)),scale(square(positive(data['q'][B])),F(1,B*B)))
    U=[ZERO]*(B+1)
    neg_by_layer={l:[ZERO]*(B+1) for l in sorted({p['level'] for p in packet_rows})}
    for p in packet_rows:
        t=interval_from_record(p['q_triangle_actual']);L,x,R=p['L'],p['x'],p['R']
        for n in range(L+1,R):
            kernel=T(L,x,R,n)
            U[n]=add(U[n],scale(positive(t),kernel))
            neg_by_layer[p['level']][n]=add(neg_by_layer[p['level']][n],scale(positive(neg(t)),kernel))
    retention=[]
    max_level=max(neg_by_layer)
    for threshold in range(max_level+1,0,-1):
        kept=[p for p in packet_rows if p['level']>=threshold and interval_from_record(p['q_triangle_actual'])[1]<0]
        envelope=[ZERO]*(B+1)
        for n in range(A,B+1):
            envelope[n]=sub(add(J[n],U[n]),isum(neg_by_layer[l][n] for l in neg_by_layer if l>=threshold))
        env_energy=energy(envelope,A+1,B-1,'positive')
        budget=add(square(add(sqrt_interval(env_energy),sqrt_interval(fine_energy))),endpoint_energy)
        if threshold==1:
            assert all(intersects(envelope[n],I[n]) for n in range(A,B+1))
        retention.append({'retain_negative_levels_at_least':threshold,'negative_packets_retained':len(kept),
                          'interpretation':'complete fine interpolant finite benchmark, not a new tree compression' if threshold==1 else 'partial negative-packet retention finite envelope',
                          'envelope_positive_energy_interior':record(env_energy),'closed_squared_budget':record(budget)})
    results['negative_packet_retention']={'rule':'retain negative packets on all local levels >= threshold; original positive packets retained; no phase change',
        'fine_positive_remainder_energy':record(fine_energy),'true_endpoint_positive_energy':record(endpoint_energy),'rows':retention,
        'scope':'Finite envelopes, not uniform arithmetic estimates or a claim of new asymptotic bounds.'}
    results['checks']={'all_prefix_reference_equations':True,'all_c_convolution_differences':True,
        'every_nonsquarefree_error_contains_exact_zero':True,'all_38_q_triangle_difference_identities':True,
        'all_38_reference_Q_sigma_tail_identities':True,'all_38_packet_signs_unchanged':all(p['original_and_reference_sign_same'] for p in packet_rows),
        'all_38_Q_sigma_tail_differences_paired_on_same_packet':True,
        'all_4_actual_reference_skeleton_charge_differences':True,
        'all_retained_negative_packets_returns_exact_fine_interpolant':True}
    results['summary']={'packet_count':len(packet_rows),'max_abs_triangle_error':record(scalar_max([abs_interval(interval_from_record(p['q_triangle_error'])) for p in packet_rows])),
        'max_abs_corrected_triangle_error':record(scalar_max([abs_interval(interval_from_record(p['Q_triangle_error'])) for p in packet_rows])),
        'max_layer_root_error':record(scalar_max([sqrt_interval(interval_from_record(l['weighted_coefficient_error_square'])) for b in results['blocks'] for l in b['layers']]))}
    output=OUT/'reference_split_certificate.json'
    output.write_text(json.dumps(results,ensure_ascii=False,separators=(',',':'))+'\n')
    print(json.dumps({'status':'PASS','seconds':round(time.perf_counter()-started,3),'output_bytes':output.stat().st_size,
        'max_abs_D_minus_Lambda':record(max_e)['upper'],
        'summary':{k:(v['upper'] if isinstance(v,dict) and 'upper' in v else v) for k,v in results['summary'].items()},
        'energies':{k:v['upper'] for k,v in results['energies'].items()},
        'retention':[(r['negative_packets_retained'],r['closed_squared_budget']['upper']) for r in retention]},ensure_ascii=False))


if __name__=='__main__':
    main()
