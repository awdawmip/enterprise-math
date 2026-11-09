"""Exact finite cubic Hasse boundary regression for original D25 low bands.

Author-side verifier: 80 primes p=6m+1 in [7,1000], both W and V.
The parameters are the finite deformation of the ORIGINAL 216/2304 models,
not native H0/B0 divided-power coefficients.
"""
from d25_AF4_low_grade_hasse_micro_20261109 import prime,jets_and_terminal

def predicted_J(p,kind):
    H=[0]
    for k in range(1,p):
        H.append((H[-1]+pow(k,-1,p))%p)
    inv=lambda x: pow(x%p,-1,p)
    if kind=="W":
        m=(p-1)//6
        return (-inv(2)*H[3*m]
                +inv(3)*(H[m-1]-H[2*m])
                -2*inv(3)*(H[4*m]-H[m])
                -inv(3*m))%p
    if p%4==1:
        t=(p-1)//4
        return (-3*inv(4*t)-inv(2)*H[2*t]
                -3*inv(4)*(H[3*t]-H[t]))%p
    t=(p-3)//4
    return (-inv(2*(t+1))-inv(2)*H[2*t+1]
            -3*inv(4)*(H[3*t+2]-H[t+1]))%p

def check(p,kind):
    _,_,b=jets_and_terminal(p,kind)
    b2,b3=b[2]%p,b[3]%p
    J=predicted_J(p,kind)
    assert b2!=0 and b3==b2*J%p,(p,kind,b2,b3,J)
    return b2,b3,J

if __name__=="__main__":
    expected={
      13:((2,2,1),(6,10,6)),
      19:((5,5,1),(6,5,4)),
      37:((18,17,3),(14,19,4)),
      43:((40,20,22),(10,2,26)),
      73:((1,21,21),(55,33,59)),
      373:((57,163,173),(79,314,207))
    }
    for p,(W,V) in expected.items():
        assert check(p,"W")==W
        assert check(p,"V")==V
        print(p,W,V)
    count=0
    for p in range(7,1001):
        if prime(p) and p%6==1:
            check(p,"W")
            check(p,"V")
            count+=1
    assert count==80,count
    print("PASS",count,"primes, two original models, cubic harmonic coefficient")
