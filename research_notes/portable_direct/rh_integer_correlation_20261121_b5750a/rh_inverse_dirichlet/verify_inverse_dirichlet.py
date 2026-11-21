#!/usr/bin/env python3
"""O(B-A) inverse-Dirichlet multipliers on the same three complete-road windows.

The earlier gradient and positive-cell integrations are not rerun. Their input
parameters and recorded square sums are reused from inputs.json. Deterministic
road generation is repeated only to supply the new matrix-vector operations.
All computations use 80-digit non-interval arithmetic.
"""
from pathlib import Path
from math import comb
import hashlib
import json
import mpmath as mp

mp.mp.dps = 80
ROOT = Path(__file__).resolve().parent


def fmt(x):
    return mp.nstr(x,35)


def prime_data(nmax):
    primes=[]
    omega=[0]*(nmax+1)
    for p in range(2,nmax+1):
        if not omega[p]:
            primes.append(p)
            for n in range(p,nmax+1,p):
                omega[n]+=1
    return primes,omega


def family(row):
    Y,theta,lam=map(mp.mpf,(row['Y'],row['theta'],row['lambda']))
    if row['label']=='chebyshev':
        m=int(mp.ceil(lam*mp.log(Y)))
        A=mp.mpf(row['maximum_thickness'])
        b=A*mp.tanh(mp.acosh(3)/(2*(m-1)))**2
        nodes=[(A+b)/2-(A-b)/2*mp.cos(mp.pi*j/(m-1)) for j in range(m)]
        weights=[mp.fprod(-nodes[k]/(nodes[j]-nodes[k]) for k in range(m) if k!=j) for j in range(m)]
    else:
        m=int(row['label'][1:])
        h=(mp.mpf(m+1)/2)**(mp.mpf(1)/m)*Y**(-lam*(1-theta)/m)/(lam*mp.log(Y))**(1+mp.mpf(2)/m)
        nodes=[j*h for j in range(1,m+1)]
        weights=[mp.mpf((-1)**(j+1)*comb(m,j)) for j in range(1,m+1)]
    return Y,theta,lam,nodes,weights


def full_inputs(nodes,weights,nmax,primes):
    D=[mp.mpf(0)]*(nmax+1)
    for a,nu in zip(nodes,weights):
        road=[mp.mpf(0)]+[mp.mpf(1)]*nmax
        for p in primes:
            factor=-mp.expm1(-a*mp.log(p))
            for n in range(p,nmax+1,p):
                road[n]*=factor
        for n in range(2,nmax+1):
            D[n]+=nu*road[n]/a
    q=[mp.mpf(0)]*(nmax+1)
    P=mp.mpf(0)
    R=mp.mpf(0)
    for n in range(1,nmax+1):
        P+=D[n]
        R+=D[n]/n
        q[n]=n*(1+mp.euler+R-mp.log(n))-P
    return D,q


def inverse_dirichlet(rhs):
    """rhs has local indices 0..M; endpoints are ignored, outputs vanish there.

    Two positive triangular prefix/suffix contributions; no dense matrix.
    Three linear scans, O(M) arithmetic operations and O(M) storage.
    """
    M=len(rhs)-1
    prefix=[mp.mpf(0)]*(M+1)
    suffix=[mp.mpf(0)]*(M+1)
    for i in range(1,M):
        prefix[i]=prefix[i-1]+i*rhs[i]
    for i in range(M-1,0,-1):
        suffix[i]=suffix[i+1]+(M-i)*rhs[i]
    out=[mp.mpf(0)]*(M+1)
    for i in range(1,M):
        out[i]=((M-i)*prefix[i]+i*suffix[i+1])/M
    return out


def compute(row,primes,omega):
    Y,theta,lam,nodes,weights=family(row)
    Z=Y**lam
    A,B=int(mp.ceil(Y)),int(mp.floor(Z))
    M=B-A
    D,q=full_inputs(nodes,weights,B,primes)
    w=[mp.mpf(A+i)**(-2*theta-1) for i in range(M+1)]
    u=[max(q[A+i],0) for i in range(M+1)]
    h=[mp.mpf(0)]+[w[i]*u[i] for i in range(1,M)]+[mp.mpf(0)]
    f=[mp.mpf(0)]*(M+1)
    kappa=[mp.mpf(0)]*(M+1)
    for i in range(1,M):
        n=A+i
        kappa[i]=n*((n+1)*mp.log(n+1)-2*n*mp.log(n)+(n-1)*mp.log(n-1))
        f[i]=(kappa[i]-D[n])/n
    z=inverse_dirichlet(h)
    forced=inverse_dirichlet(f)
    forced_positive=inverse_dirichlet([max(x,0) for x in f])
    harmonic=[((M-i)*q[A]+i*q[B])/M for i in range(M+1)]
    harmonic_positive_endpoints=[((M-i)*max(q[A],0)+i*max(q[B],0))/M for i in range(M+1)]
    S=mp.fsum(w[i]*u[i]**2 for i in range(1,M))
    expected=mp.mpf(row['expected_interior_positive_square_sum'])
    assert abs(S-expected)<mp.mpf('1e-36')
    poisson_error=max(abs(2*z[i]-z[i-1]-z[i+1]-h[i]) for i in range(1,M))
    reconstruction_error=max(abs(forced[i]+harmonic[i]-q[A+i]) for i in range(1,M))
    assert poisson_error<mp.mpf('1e-65')
    assert reconstruction_error<mp.mpf('1e-65')
    assert z[0]==z[M]==0
    assert min(z[1:M])>=0
    background_work=mp.fsum(kappa[i]*z[i]/(A+i) for i in range(1,M))
    road_work=mp.fsum(D[A+i]*z[i]/(A+i) for i in range(1,M))
    source=mp.fsum(f[i]*z[i] for i in range(1,M))
    source_positive=mp.fsum(max(f[i],0)*z[i] for i in range(1,M))
    source_negative=mp.fsum(max(-f[i],0)*z[i] for i in range(1,M))
    left_boundary=q[A]*z[1]
    right_boundary=q[B]*z[M-1]
    boundary=left_boundary+right_boundary
    rhs=source+boundary
    identity_error=abs(S-rhs)
    assert identity_error<mp.mpf('1e-65')
    assert abs(source-(background_work-road_work))<mp.mpf('1e-65')
    assert abs(source-mp.fsum(h[i]*forced[i] for i in range(1,M)))<mp.mpf('1e-65')
    assert abs(boundary-mp.fsum(h[i]*harmonic[i] for i in range(1,M)))<mp.mpf('1e-65')
    if S:
        root=mp.sqrt(S)
        dual_norm2=mp.fsum((h[i]/root)**2/w[i] for i in range(1,M))
        dual_value=rhs/root
        assert abs(dual_norm2-1)<mp.mpf('1e-70')
        assert abs(dual_value-root)<mp.mpf('1e-60')
    else:
        root=dual_norm2=dual_value=mp.mpf(0)
        assert all(t==0 for t in z)
    harmonic_positive_energy=mp.fsum(w[i]*max(harmonic[i],0)**2 for i in range(1,M))
    forced_positive_energy=mp.fsum(w[i]*max(forced[i],0)**2 for i in range(1,M))
    split_upper=(mp.sqrt(harmonic_positive_energy)+mp.sqrt(forced_positive_energy))**2
    source_sign_discard_upper=mp.fsum(w[i]*(forced_positive[i]+harmonic_positive_endpoints[i])**2 for i in range(1,M))
    assert S<=split_upper+mp.mpf('1e-60')
    assert S<=source_sign_discard_upper+mp.mpf('1e-60')
    strata=[]
    for r in range(1,max(omega)+1):
        indices=[i for i in range(1,M) if omega[A+i]==r]
        hb=mp.fsum(kappa[i]*z[i]/(A+i) for i in indices)
        hd=mp.fsum(D[A+i]*z[i]/(A+i) for i in indices)
        strata.append({'omega':r,'source_nodes':len(indices),
                       'source_nodes_with_nonpositive_q':sum(q[A+i]<=0 for i in indices),
                       'background_pairing':fmt(hb),'road_pairing':fmt(hd),
                       'signed_source_pairing':fmt(hb-hd)})
    absolute_budget=source_positive+source_negative+abs(left_boundary)+abs(right_boundary)
    result={'label':row['label'],'Y':fmt(Y),'Z':fmt(Z),'theta':fmt(theta),
            'A':A,'B':B,'interior_nodes':M-1,'node_count':len(nodes),
            'positive_curvature_support':sum(h[i]>0 for i in range(1,M)),
            'strictly_positive_kernel_nodes':sum(z[i]>0 for i in range(1,M)),
            'positive_square_sum':fmt(S),'positive_square_root':fmt(root),
            'source_work':fmt(source),'background_work':fmt(background_work),'road_work':fmt(road_work),
            'positive_source_pairing':fmt(source_positive),'negative_source_pairing':fmt(source_negative),
            'q_A':fmt(q[A]),'q_B':fmt(q[B]),'z_A_plus_1':fmt(z[1]),'z_B_minus_1':fmt(z[M-1]),
            'left_boundary_work':fmt(left_boundary),'right_boundary_work':fmt(right_boundary),
            'boundary_work':fmt(boundary),'source_plus_boundary':fmt(rhs),
            'net_source_and_boundary_absolute_over_square_sum':fmt((abs(source)+abs(left_boundary)+abs(right_boundary))/S) if S else None,
            'uncombined_source_and_boundary_absolute_over_square_sum':fmt(absolute_budget/S) if S else None,
            'harmonic_positive_energy':fmt(harmonic_positive_energy),
            'forced_positive_energy':fmt(forced_positive_energy),
            'source_boundary_separated_positive_upper_ratio':fmt(split_upper/S) if S else None,
            'source_and_endpoint_negative_parts_discarded_upper_ratio':fmt(source_sign_discard_upper/S) if S else None,
            'maximum_z':fmt(max(z)),'dual_optimizer_norm_squared':fmt(dual_norm2),
            'functional_at_dual_optimizer':fmt(dual_value),'prior_gradient_discard_upper_ratio':row['prior_gradient_discard_upper_ratio'],
            'maximum_poisson_residual':fmt(poisson_error),'maximum_harmonic_source_reconstruction_error':fmt(reconstruction_error),
            'raw_energy_identity_error':fmt(identity_error),
            'dual_optimizer_identity_error':fmt(abs(dual_value-root)),
            'factor_strata':strata,
            'scope':'Exact identities proved analytically; this finite run is non-interval, and no uniform arithmetic estimate is inferred.'}
    return result


def main():
    path=ROOT/'inputs.json'
    inputs=json.loads(path.read_text())
    nmax=max(int(mp.floor(mp.mpf(c['Y'])**mp.mpf(c['lambda']))) for c in inputs['cases'])
    primes,omega=prime_data(nmax)
    rows=[]
    for row in inputs['cases']:
        result=compute(row,primes,omega)
        rows.append(result)
        print(json.dumps({k:result[k] for k in ('label','theta','positive_square_sum','source_work','left_boundary_work','right_boundary_work',
                                               'net_source_and_boundary_absolute_over_square_sum','uncombined_source_and_boundary_absolute_over_square_sum',
                                               'source_boundary_separated_positive_upper_ratio','raw_energy_identity_error')},ensure_ascii=False),flush=True)
    out={'status':'ALL_INVERSE_DIRICHLET_AND_DUALITY_CHECKS_PASSED','precision_decimal_digits':80,'interval_arithmetic':False,
         'scientific_source_commit':inputs['scientific_source_commit'],'previous_artifact_commit':inputs['previous_artifact_commit'],
         'inputs_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'proof':'INVERSE_DIRICHLET_INTERFACE.md',
         'operator_cost':'Each Green application uses two cumulative arrays and three O(B-A) scans. Input road generation is accounted for separately.',
         'cases':rows,'limitations':'The supremum formula is an equivalence, not an already established bound on its signed arithmetic functional. Previous energy suites are not rerun.'}
    target=ROOT/'inverse_dirichlet_results.json'
    target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'cases':len(rows),'path':str(target)}),flush=True)


if __name__=='__main__':
    main()
