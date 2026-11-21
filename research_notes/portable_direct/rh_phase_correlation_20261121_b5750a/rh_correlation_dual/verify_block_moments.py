#!/usr/bin/env python3
"""New local-moment bounds for the inverse-Dirichlet cone.

Same three finite complete-road inputs; prior suites are not rerun.
80-digit floating point, not interval arithmetic. Every source and factor layer
is retained. Green applications and block condensation use linear passes.
"""
from pathlib import Path
from math import comb
import hashlib
import json
import mpmath as mp

mp.mp.dps=80
ROOT=Path(__file__).resolve().parent


def fmt(x):
    return mp.nstr(x,35)


def prime_data(nmax):
    primes=[]
    omega=[0]*(nmax+1)
    for p in range(2,nmax+1):
        if not omega[p]:
            primes.append(p)
            for n in range(p,nmax+1,p): omega[n]+=1
    return primes,omega


def family(row):
    Y,theta,lam=map(mp.mpf,(row['Y'],row['theta'],row['lambda']))
    m=row['node_count']
    if row['label']=='chebyshev':
        upper=mp.mpf(row['maximum_thickness'])
        lower=upper*mp.tanh(mp.acosh(3)/(2*(m-1)))**2
        nodes=[(upper+lower)/2-(upper-lower)/2*mp.cos(mp.pi*j/(m-1)) for j in range(m)]
        weights=[mp.fprod(-nodes[k]/(nodes[j]-nodes[k]) for k in range(m) if k!=j) for j in range(m)]
    else:
        h=(mp.mpf(m+1)/2)**(mp.mpf(1)/m)*Y**(-lam*(1-theta)/m)/(lam*mp.log(Y))**(1+mp.mpf(2)/m)
        nodes=[j*h for j in range(1,m+1)]
        weights=[mp.mpf((-1)**(j+1)*comb(m,j)) for j in range(1,m+1)]
    return Y,theta,lam,nodes,weights


def roads_and_q(nodes,weights,nmax,primes):
    D=[mp.mpf(0)]*(nmax+1)
    for a,nu in zip(nodes,weights):
        road=[mp.mpf(0)]+[mp.mpf(1)]*nmax
        for p in primes:
            factor=-mp.expm1(-a*mp.log(p))
            for n in range(p,nmax+1,p): road[n]*=factor
        for n in range(2,nmax+1): D[n]+=nu*road[n]/a
    q=[mp.mpf(0)]*(nmax+1)
    total=reciprocal=mp.mpf(0)
    for n in range(1,nmax+1):
        total+=D[n]
        reciprocal+=D[n]/n
        q[n]=n*(1+mp.euler+reciprocal-mp.log(n))-total
    return D,q


def green(rhs):
    M=len(rhs)-1
    p=[mp.mpf(0)]*(M+1)
    s=[mp.mpf(0)]*(M+1)
    for i in range(1,M): p[i]=p[i-1]+i*rhs[i]
    for i in range(M-1,0,-1): s[i]=s[i+1]+(M-i)*rhs[i]
    return [mp.mpf(0)]+[((M-i)*p[i]+i*s[i+1])/M for i in range(1,M)]+[mp.mpf(0)]


def cone_envelope(w):
    M=len(w)-1
    p=[mp.mpf(0)]*(M+1)
    s=[mp.mpf(0)]*(M+1)
    for i in range(1,M): p[i]=p[i-1]+i*i*w[i]
    for i in range(M-1,0,-1): s[i]=s[i+1]+(M-i)**2*w[i]
    return [mp.mpf(0)]+[mp.sqrt(((M-i)**2*p[i]+i*i*s[i+1])/M**2) for i in range(1,M)]+[mp.mpf(0)]


def partition(A,B,beta):
    cuts=[A]
    while cuts[-1]<B:
        L=cuts[-1]
        cuts.append(min(B,L+max(2,int(mp.floor(mp.mpf(L)**beta)))))
    return cuts


def norm_positive(x,w):
    return mp.sqrt(mp.fsum(wi*max(xi,0)**2 for xi,wi in zip(x[1:-1],w[1:-1])))


def one_partition(A,B,theta,f,q,w,K,z,h,omega,eta,beta):
    M=B-A
    cuts=partition(A,B,beta)
    cut_indices=[x-A for x in cuts]
    coarse=[mp.mpf(0)]*(M+1)
    strata=[[mp.mpf(0)]*(M+1) for _ in range(max(omega)+1)]
    for x in cuts[1:-1]:
        i=x-A
        coarse[i]=f[i]
        strata[omega[x]][i]=f[i]
    remainder=[mp.mpf(0)]*(M+1)
    gap_bound2=mp.mpf(0)
    negative_only_blocks=0
    block_records=[]
    max_port_error=mp.mpf(0)
    for L,R in zip(cuts[:-1],cuts[1:]):
        H=R-L
        ia,ib=L-A,R-A
        fs=[mp.mpf(0)]+f[ia+1:ib]+[mp.mpf(0)]
        P=green(fs)
        total=mp.fsum(fs[1:-1])
        first=mp.fsum((L+j)*fs[j] for j in range(1,H))
        alpha=(R*total-first)/H
        betaval=(first-L*total)/H
        alpha_direct=mp.fsum((H-j)*fs[j]/H for j in range(1,H))
        beta_direct=mp.fsum(j*fs[j]/H for j in range(1,H))
        max_port_error=max(max_port_error,abs(alpha-alpha_direct),abs(betaval-beta_direct))
        coarse[ia]+=alpha
        coarse[ib]+=betaval
        for j in range(1,H):
            n=L+j
            r=omega[n]
            strata[r][ia]+=(H-j)*fs[j]/H
            strata[r][ib]+=j*fs[j]/H
            remainder[ia+j]=P[j]
        C=1+1/(6*(mp.mpf(L)**2-1))+eta
        local_gap=C*C*(mp.mpf(H)**5-H)/(120*mp.mpf(L)**(2*theta+3))
        gap_bound2+=local_gap
        if max(P[1:-1],default=mp.mpf(0))<=0: negative_only_blocks+=1
        if len(block_records)<4 or R==B:
            block_records.append({'L':L,'R':R,'zeroth_source_moment':fmt(total),'first_source_moment':fmt(first),
                                  'left_affine_mass':fmt(alpha),'right_affine_mass':fmt(betaval),
                                  'local_positive_potential_max':fmt(max(P))})
    # End coarse masses are retained as ports but their test values are exactly zero.
    coarse_at_endpoints=[coarse[0],coarse[M]]
    coarse[0]=coarse[M]=mp.mpf(0)
    harmonic=[((M-i)*q[A]+i*q[B])/M for i in range(M+1)]
    coarse_potential=green(coarse)
    b=[x+y for x,y in zip(harmonic,coarse_potential)]
    reconstruction_error=max(abs(b[i]+remainder[i]-q[A+i]) for i in range(M+1))
    assert reconstruction_error<mp.mpf('1e-64')
    assert max_port_error<mp.mpf('1e-65')
    Ractual=norm_positive(remainder,w)
    Rgap=mp.sqrt(gap_bound2)
    assert Ractual<=Rgap+mp.mpf('1e-60')
    rootS=mp.sqrt(mp.fsum(w[i]*max(q[A+i],0)**2 for i in range(1,M)))
    Bmain=norm_positive(b,w)
    Bends=norm_positive(harmonic,w)
    cpositive=[max(x,0) for x in coarse]
    positive_coarse_potential=green(cpositive)
    M2=mp.sqrt(mp.fsum(w[i]*positive_coarse_potential[i]**2 for i in range(1,M)))
    M1=mp.fsum(max(coarse[i],0)*K[i] for i in cut_indices[1:-1])
    M_layers=mp.fsum(max(strata[r][i],0)*K[i] for i in cut_indices[1:-1] for r in range(1,len(strata)))
    assert M2<=M1+mp.mpf('1e-60')
    assert M1<=M_layers+mp.mpf('1e-60')
    assert rootS<=Bmain+Ractual+mp.mpf('1e-60')
    assert rootS<=Bends+M2+Rgap+mp.mpf('1e-60')
    source_pair=mp.fsum(f[i]*z[i] for i in range(1,M))
    coarse_pair=mp.fsum(coarse[i]*z[i] for i in cut_indices[1:-1])
    remainder_pair=mp.fsum(h[i]*remainder[i] for i in range(1,M))
    pair_error=abs(source_pair-coarse_pair-remainder_pair)
    assert pair_error<mp.mpf('1e-65')
    assert max(abs(coarse[i]-mp.fsum(strata[r][i] for r in range(1,len(strata)))) for i in cut_indices[1:-1])<mp.mpf('1e-65')
    moment_ratios=[]
    coarse_records=[]
    for j in range(1,len(cuts)-1):
        x=cuts[j]
        span=cuts[j+1]-cuts[j-1]
        i=x-A
        ratio=max(coarse[i],0)*x/mp.sqrt(span)
        moment_ratios.append(ratio)
        if len(coarse_records)<4 or j==len(cuts)-2:
            coarse_records.append({'node':x,'support_length':span,'signed_tent_source':fmt(coarse[i]),
                                   'sqrt_length_normalized_positive_source':fmt(ratio),
                                   'factor_layer_tent_sources':{str(r):fmt(strata[r][i]) for r in range(1,len(strata))}})
    return {'beta':fmt(beta),'blocks':len(cuts)-1,'interior_coarse_nodes':len(cuts)-2,
            'source_nodes':M-1,'cuts':cuts,'negative_only_local_potential_blocks':negative_only_blocks,
            'root_actual_square_sum':fmt(rootS),'signed_coarse_main_positive_norm':fmt(Bmain),
            'actual_local_positive_remainder_norm':fmt(Ractual),'proved_local_curvature_gap_bound':fmt(Rgap),
            'true_endpoint_harmonic_positive_norm':fmt(Bends),
            'coarse_positive_Gram_budget':fmt(M2),'coarse_positive_pointwise_budget':fmt(M1),
            'factor_layers_separately_positivized_budget':fmt(M_layers),
            'factor_layer_loss_ratio':fmt(M_layers/M1) if M1 else None,
            'signed_coarse_plus_actual_remainder_upper_ratio':fmt((Bmain+Ractual)**2/rootS**2),
            'moment_Gram_plus_gap_upper_ratio':fmt((Bends+M2+Rgap)**2/rootS**2),
            'simple_moment_plus_gap_upper_ratio':fmt((Bends+M1+Rgap)**2/rootS**2),
            'largest_sqrt_length_normalized_positive_tent_source':fmt(max(moment_ratios)),
            'coarse_positive_nodes':sum(coarse[i]>0 for i in cut_indices[1:-1]),
            'coarse_negative_nodes':sum(coarse[i]<0 for i in cut_indices[1:-1]),
            'actual_kernel_source_pairing':fmt(source_pair),'actual_kernel_coarse_pairing':fmt(coarse_pair),
            'actual_kernel_local_curvature_pairing':fmt(remainder_pair),
            'endpoint_coarse_masses_with_zero_test_value':[fmt(x) for x in coarse_at_endpoints],
            'maximum_reconstruction_error':fmt(reconstruction_error),'maximum_moment_identity_error':fmt(max_port_error),
            'source_pairing_identity_error':fmt(pair_error),'sample_blocks':block_records,'sample_coarse_sources':coarse_records}


def main():
    path=ROOT/'inputs.json'
    inputs=json.loads(path.read_text())
    nmax=max(int(mp.floor(mp.mpf(c['Y'])**mp.mpf(c['lambda']))) for c in inputs['cases'])
    primes,omega=prime_data(nmax)
    rows=[]
    for row in inputs['cases']:
        Y,theta,lam,nodes,weights=family(row)
        Z=Y**lam
        A,B=int(mp.ceil(Y)),int(mp.floor(Z))
        M=B-A
        D,q=roads_and_q(nodes,weights,B,primes)
        eta=mp.fprod(nodes)*(mp.log(Z)**(len(nodes)+1))/mp.factorial(len(nodes)+1)
        assert eta<mp.mpf('0.5')
        f=[mp.mpf(0)]*(M+1)
        for i in range(1,M):
            n=A+i
            kappa=n*((n+1)*mp.log(n+1)-2*n*mp.log(n)+(n-1)*mp.log(n-1))
            f[i]=(kappa-D[n])/n
        w=[mp.mpf(A+i)**(-2*theta-1) for i in range(M+1)]
        K=cone_envelope(w)
        h=[mp.mpf(0)]+[w[i]*max(q[A+i],0) for i in range(1,M)]+[mp.mpf(0)]
        z=green(h)
        configs=[]
        for beta in (mp.mpf('0.5'),mp.mpf('0.8')):
            result=one_partition(A,B,theta,f,q,w,K,z,h,omega,eta,beta)
            result['signed_coarse_plus_proved_gap_upper_ratio']=mp.nstr(
                (mp.mpf(result['signed_coarse_main_positive_norm'])+
                 mp.mpf(result['proved_local_curvature_gap_bound']))**2/
                mp.mpf(result['root_actual_square_sum'])**2,30)
            configs.append(result)
            print(json.dumps({'label':row['label'],'theta':fmt(theta),**{k:result[k] for k in ('beta','blocks','actual_local_positive_remainder_norm',
                  'proved_local_curvature_gap_bound','signed_coarse_plus_actual_remainder_upper_ratio','moment_Gram_plus_gap_upper_ratio',
                  'factor_layer_loss_ratio','largest_sqrt_length_normalized_positive_tent_source')}},ensure_ascii=False),flush=True)
        rows.append({'label':row['label'],'Y':fmt(Y),'Z':fmt(Z),'theta':fmt(theta),'pointwise_matching_error_bound':fmt(eta),
                     'node_count':len(nodes),'partitions':configs})
    out={'status':'ALL_LOCAL_MOMENT_AND_CONCAVE_CONE_CHECKS_PASSED','precision_decimal_digits':80,'interval_arithmetic':False,
         'scientific_source_commit':inputs['scientific_source_commit'],'source_continuation_commit':inputs['source_continuation_commit'],
         'inputs_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'proof':'BLOCK_MOMENT_CORRELATION.md','cases':rows,
         'limitations':'Finite true-road decompositions only; the tent-source square-root discrepancy hypothesis and endpoint budget are not proved at unbounded scales.'}
    target=ROOT/'block_moment_results.json'
    target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'cases':len(rows),'partitions':sum(len(c['partitions']) for c in rows),'path':str(target)}),flush=True)


if __name__=='__main__': main()
