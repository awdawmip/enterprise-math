"""D25 original-216 unified upper-strip mirror and signed finite probe.
Exact modular integers. The finite p^3 sign probe is not an all-prime proof.
"""
import json, math

def primes(n):
    a=bytearray([1])*(n+1);a[:2]=b'\0\0'
    for q in range(2,math.isqrt(n)+1):
        if a[q]:a[q*q:n+1:q]=bytes((n-q*q)//q+1)
    return [q for q in range(5,n+1) if a[q]]

def verify(p):
    m=p**3;h=(p-1)//2;L=2*p//3;r=L-h
    fac=[1]*p
    for i in range(1,p):fac[i]=fac[i-1]*i%m
    invfac=[1]*p;invfac[-1]=pow(fac[-1],-1,m)
    for i in range(p-1,0,-1):invfac[i-1]=invfac[i]*i%m
    inverse216=pow(216,-1,m);inv9=pow(9,-1,p)
    chi=1 if pow(6,h,p)==1 else -1
    b=1;W=1;half=1;high=0;R=0;thetaR=0;mirror=1;coef_count=0
    denominator_power=1
    independent={5,7,11,13,17,19,373}
    for k in range(p):
        if p in independent:
            direct=math.comb(2*k,k)**2*math.comb(3*k,k)*denominator_power%m
            assert b==direct,(p,k,'independent-binomial')
        if k:
            w=(6*k+1)*b%m;W=(W+w)%m
            if k<=h:half=(half+w)%m
            if h<k<=L:
                t=k-h-1;coef_count+=1
                assert b%(p*p)==0,(p,k,'valuation')
                assert (b//(p*p))%p==chi*inv9*mirror%p,(p,k,'mirror coefficient')
                high=(high+w//(p*p))%p
                R=(R+mirror)%p;thetaR=(thetaR+t*mirror)%p
                if t<r-1:
                    s=t+1
                    mirror=mirror*s*(6*s-1)*(6*s+1)*pow(9*(2*s+1)**3,-1,p)%p
        denominator_power=denominator_power*inverse216%m
        if k<p-1:
            i=k+1
            invk=invfac[i]*fac[i-1]%m
            b=b*(2*k+1)*(2*k+2)*(3*k+1)*(3*k+2)*(3*k+3)*inverse216*pow(invk,5,m)%m
    assert coef_count==r and r*(6*r-1)*(6*r+1)%p==0
    assert high==chi*inv9*(4*R+6*thetaR)%p
    assert W==(half+p*p*high)%m
    sigma=1 if p%3==1 else -1
    assert W==(p*sigma)%m,(p,'signed hypothesis',W,p*sigma%m)
    return {'p':p,'p_mod24':p%24,'sign':sigma,'chi6':chi,'r':r,
            'W_mod_p3':W,'half_W_mod_p3':half,'high_div_p2_mod_p':high,
            'R1_mod_p':R,'theta_R1_mod_p':thetaR}

def main(bound=10000):
    ps=primes(bound);samples={5,7,11,13,17,19,23,31,37,43,73,181,373,1171,3019,9967,9973}
    rows=[verify(p) for p in ps]
    out={'schema':'D25_216_UNIFIED_HIGH_MIRROR_FINITE_CHECK_V1',
         'exact_primes_p_gt3_at_most':bound,'tested_primes':len(ps),
         'mirror_coefficient_positions':sum(x['r'] for x in rows),
         'tested_residue_class_counts':{str(a):sum(x['p_mod24']==a for x in rows) for a in (1,5,7,11,13,17,19,23)},
         'proved_identity_regression':'unified high strip coefficient formula, full terminating differential upper boundary, and W-half decomposition',
         'unproved_global_hypothesis':'W216(p-1) congruent p*Legendre(-3,p) modulo p^3',
         'global_hypothesis_finite_pass':len(rows),'selected_exact_cases':[x for x in rows if x['p'] in samples],
         'note':'All computations exact modulo p^3/p; no all-prime sign proof, no native H0/B0 execution or Source admission.'}
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
