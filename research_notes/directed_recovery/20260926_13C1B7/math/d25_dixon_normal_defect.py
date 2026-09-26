"""Exact transverse-parameter defect at the B11 contiguous-Dixon node."""
import json
from fractions import Fraction as Q
from pathlib import Path

def poch(a,n):
    out=Q(1)
    for j in range(n): out*=a+j
    return out

def F(m,a,d):
    return sum((poch(-m,j)/poch(d,j)*a/(a+j) for j in range(m+1)),Q(0))

def partial_a(m,a,d):
    return sum((poch(-m,j)/poch(d,j)*Q(j)/(a+j)**2 for j in range(1,m+1)),Q(0))

def partial_d(m,a,d):
    return -sum((poch(-m,j)/poch(d,j)*a/(a+j)*
                 sum((Q(1)/(d+l) for l in range(j)),Q(0))
                 for j in range(1,m+1)),Q(0))

def C(m,a):
    return 1+a*sum((1/(a+2+2*r)-1/(a+1+2*r) for r in range(m)),Q(0))

def Cprime(m,a):
    return sum((1/(a+2+2*r)-1/(a+1+2*r)
                +a*(-1/(a+2+2*r)**2+1/(a+1+2*r)**2)
                for r in range(m)),Q(0))

def telescoping_certificate(m,a,j):
    Aj=poch(-m,j)/poch(m+a+1,j)
    return (j+a+m)*Aj*(m-j*(a+2*m))/((a+2*m-1)*(a+2*m))

def modq(x,p):
    return x.numerator*pow(x.denominator,-1,p)%p

def main():
    exact=[]
    telescoping_checks=0
    for m in range(1,9):
        for a in [Q(-1,3),Q(2,7),Q(3,2),Q(2)]:
            d=m+a+1
            assert F(m,a,d)==C(m,a),(m,a,"C")
            assert partial_d(m,a,d)==Cprime(m,a)-partial_a(m,a,d),(m,a,"derivative")
            for j in range(m+1):
                assert telescoping_certificate(m,a,j+1)-telescoping_certificate(m,a,j)==j*poch(-m,j)/poch(d,j),(m,a,j,"telescoping")
                telescoping_checks+=1
            exact.append({"m":m,"a":str(a),"exact_rational_identity":True})
    rows=[]
    for p in [7,13,19,31,37,43,61,67]:
        m=(p-1)//6;a=Q(-1,3);d=m+a+1
        target=F(m,a,Q(3*m+1))
        dixon=C(m,a)
        N=partial_d(m,a,d)
        delta=(target-dixon)/p
        assert modq(delta-N/3,p)==0,("normal shift",p)
        rows.append({"p":p,"m":m,"S_target":str(target),"S_Dixon":str(dixon),
                     "normal_derivative_mod_p":modq(N,p),
                     "dropped_first_digit":modq(delta,p),
                     "one_third_normal_derivative":modq(N/3,p),
                     "target_minus_dixon_mod_p2":modq(target-dixon,p*p)})
    report={"scope":"AUTHOR_LOCAL_ALGEBRA_AND_FINITE_FALSIFICATION_NOT_INDEPENDENT_REVIEW",
            "exact_telescoping_checks":telescoping_checks,
            "exact_rational_checks":len(exact),"checks":exact,"prime_witnesses":rows,
            "counterexample_to_naive_mod_p2_dixon_substitution":next(r for r in rows if r["p"]==13),
            "LIFT_status":"OPEN; this eliminates a lossy derivative shortcut, not the endpoint residual"}
    out=Path(__file__).with_name("D25_DIXON_NORMAL_DEFECT_RESULT.json")
    out.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k!="checks"},indent=2))
if __name__=="__main__":main()
