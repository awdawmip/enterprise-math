"""Prepared local verifier for portable D25 Beta/parameter-jet evidence.
No network, Source write, session access, or theorem admission.
Run only after root has completed its own research-mode registration.
"""
import argparse, json, math
from fractions import Fraction as Q
from pathlib import Path

def H(n, order=1):
    return sum((Q(1, k**order) for k in range(1, n+1)), Q(0))

def jet_mul(a,b):
    return [sum((a[i]*b[k-i] for i in range(k+1)),Q(0)) for k in range(3)]

def jet_inv(a):
    assert a[0]
    out=[1/a[0],Q(0),Q(0)]
    for n in range(1,3):
        out[n]=-sum((a[k]*out[n-k] for k in range(1,n+1)),Q(0))/a[0]
    return out

def anchored_ratio(m,n):
    # R_n(t)= (-m+t/2)_n(-2m+t/3)_n(-4m+2t/3)_n /
    #         [n! 2^n (-4m+t)_n(-2m+t)_n].
    # Cancel exact powers of t before forming its rational Taylor series.
    numerator=[Q(1,math.factorial(n)*2**n),Q(0),Q(0)]
    denominator=[Q(1),Q(0),Q(0)]
    valuation=0
    for base,slope in [(-m,Q(1,2)),(-2*m,Q(1,3)),(-4*m,Q(2,3))]:
        for i in range(n):
            if base+i==0:
                valuation+=1
                numerator=jet_mul(numerator,[slope,Q(0),Q(0)])
            else: numerator=jet_mul(numerator,[Q(base+i),slope,Q(0)])
    for base,slope in [(-4*m,Q(1)),(-2*m,Q(1))]:
        for i in range(n):
            if base+i==0:
                valuation-=1
                denominator=jet_mul(denominator,[slope,Q(0),Q(0)])
            else: denominator=jet_mul(denominator,[Q(base+i),slope,Q(0)])
    return valuation,jet_mul(numerator,jet_inv(denominator))

def data(m):
    low=[]
    for n in range(m+1):
        aa=[H(m,k)-H(m-n,k) for k in (1,2)]
        bb=[H(2*m,k)-H(2*m-n,k) for k in (1,2)]
        cc=[H(4*m,k)-H(4*m-n,k) for k in (1,2)]
        L=-aa[0]/2+Q(2,3)*bb[0]+cc[0]/3
        K=-aa[1]/8+Q(4,9)*bb[1]+Q(5,18)*cc[1]
        M=K+L*L/2
        b=Q((-1)**n*math.comb(m,n),2**n)
        low.append((b,L,M))
    high=[]
    for r in range(1,3*m+1):
        eps=Q(1) if r<=m else Q(1,3)
        h=Q((-1)**m*math.factorial(m)*math.factorial(r-1)*(3*r-1),
            2**(m+r)*math.factorial(m+r))*eps
        d=m-r if r<=m else r-m-1
        J=(H(r-1)-H(m))/2+Q(2,3)*(H(2*m)-H(d))
        J+=(H(4*m)-H(3*m-r))/3+Q(3,2*(3*r-1))
        high.append((h,J))
    return low,high

def rr(m,n,values):
    j=m-n
    return sum((values[r-1]*(Q(1) if r<=m else Q(1,3))/
                ((r+j)*2**(r+j)) for r in range(1,3*m+1)),Q(0))

def verify_jets_and_beta(m):
    low,high=data(m)
    checks=0
    for n,(b,L,M) in enumerate(low):
        v,jet=anchored_ratio(m,n)
        assert v==0 and jet==[b,b*L,b*M],("low",m,n,jet,b,L,M)
        checks+=1
    for r,(h,J) in enumerate(high,1):
        v,jet=anchored_ratio(m,m+r)
        # At t=p=6m+1, original weight equals 6r-2+3t.
        # This is an endpoint-preserving anchored family; it is not the
        # unmodified original weight for arbitrary t.
        weighted=jet_mul(jet,[Q(6*r-2),Q(3),Q(0)])
        assert v==1 and weighted[:2]==[h,h*J],("high",m,r,weighted,h,J)
        checks+=1
        # Test every coordinate F=e_r: this verifies the finite linear map,
        # not just a sample F or an observer-total fit.
        coefficient=-sum((b*(3*(m-n)+1)/
                  ((r+m-n)*2**(r+m-n)) for n,(b,_,_) in enumerate(low)),Q(0))
        coefficient*=Q(1) if r<=m else Q(1,3)
        assert coefficient==h,("BA",m,r,coefficient,h)
        checks+=1
    return checks

def endpoint(m):
    # Direct positive-parameter endpoint, independent of its harmonic jets.
    p=6*m+1
    A=Q(math.factorial(p-1),3**(p-1)*math.factorial(2*m)**3)
    term=Q(1)
    total=Q(0)
    for n in range(4*m+1):
        total+=term*(6*n+2*p-1)
        if n<4*m:
            term*=((Q(2*m)+Q(1,2)+n)*(Q(1,3)+n)*(Q(2,3)+n)/
                    ((n+1)*(2*m+1+n)*(4*m+1+n)*2))
    return A*total,A

def modq(x,modulus):
    return (x.numerator*pow(x.denominator,-1,modulus))%modulus

def prime(p):
    return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))

def verify_low(p):
    assert prime(p) and p%6==1
    m=(p-1)//6
    low,high=data(m)
    ones=[Q(1)]*(3*m)
    js=[J for _,J in high]
    R1=[rr(m,n,ones) for n in range(m+1)]
    RJ=[rr(m,n,js) for n in range(m+1)]
    X=Q(1,2**m)+sum(((6*n-1)*b*L for n,(b,L,M) in enumerate(low)),Q(0))+sum((h for h,J in high),Q(0))
    Y=sum((b*(2*L+(6*n-1)*M) for n,(b,L,M) in enumerate(low)),Q(0))+sum((h*J for h,J in high),Q(0))
    X0=Q(1,2**m)+sum((b*(6*n-1)*(L+R1[n]/2) for n,(b,L,M) in enumerate(low)),Q(0))
    Z=sum((b*(2*L-R1[n]/2+(6*n-1)*(M+RJ[n]/2)) for n,(b,L,M) in enumerate(low)),Q(0))
    Qm=sum((b*R1[n] for n,(b,L,M) in enumerate(low)),Q(0))
    assert X==X0-p*Qm/2,("X",p)
    assert modq(Y-Z-Qm/2,p)==0,("Z",p)
    direct,A=endpoint(m)
    assert modq(direct-p*A*(X+p*Y),p**3)==0,("jet endpoint",p)
    chi=2*((2**(p-1)-1)//p)-((3**(p-1)-1)//p)
    low_observer=(A*X0-1)/p+A*Z
    return {"p":p,"LOW_residual_mod_p":modq(low_observer-chi,p),
            "direct_EP_residual_mod_p3":modq(direct-p-p*p*chi,p**3),
            "reconstruction_passed":True}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--max-m",type=int,default=7)
    ap.add_argument("--primes",default="7,13,19,31,37,43,61,67")
    ap.add_argument("--output",type=Path,default=Path(__file__).with_name("PREPARED_CHECKER_RESULT.json"))
    a=ap.parse_args()
    checks=sum(verify_jets_and_beta(m) for m in range(1,a.max_m+1))
    results=[verify_low(int(p)) for p in a.primes.split(",") if p.strip()]
    report={"status":"FINITE_LOCAL_CHECK_ONLY_NOT_A_PROOF_OR_ADMISSION",
            "parameter_jet_and_beta_basis_checks":checks,"max_m":a.max_m,
            "source_messages":["fb9aba8a-6fb9-411b-920b-9bb376d16cd5","f48dfe9d-4144-4e56-9948-00a764fb3035"],
            "results":results,"failures":[x for x in results if x["LOW_residual_mod_p"] or x["direct_EP_residual_mod_p3"]],
            "next_open_unit":"All-prime evaluation of combined LOW observer through terminating-family parameter derivatives; B11 already archived, do not reprove it."}
    a.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))
    if report["failures"]: raise SystemExit(1)
if __name__=="__main__":
    main()

