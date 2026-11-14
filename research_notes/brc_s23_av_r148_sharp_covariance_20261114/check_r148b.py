"""R148B: exact infinite alternating-sign family, verified at finite r."""
from fractions import Fraction as F
from math import gcd

def support(word):
    s = [0]
    for v in word:
        s.append(s[-1] + int(v))
    m = len(word)
    a, b = F(0), F(1)
    for i in range(m):
        for j in range(i+1, m+1):
            a = max(a, F(s[j]-s[i]-1, j-i))
            b = min(b, F(s[j]-s[i]+1, j-i))
    A,B = a.numerator,a.denominator
    C,D = b.numerator,b.denominator
    U = min(B*(s[j]+1)-j*A for j in range(m+1))
    V = max(D*s[j]-j*C for j in range(m+1))
    return (A,B,C,D,U,V)

def covariance(a,b,c,d,U,V):
    g = gcd(b,d)
    q = F(g-1,2)
    return sum(((F((a*t-U)%g)-q)*(F((V-c*t)%g)-q)
                for t in range(g)),F(0))/(g*b*d)

for r in range(1,51):
    word = '0'*r+'1'+'0'*r+'1'+'0'*r
    a,b,c,d,U,V = support(word)
    assert (a,b,c,d,U,V)==(1,r+2,3,3*r+2,2,0), (r,(a,b,c,d,U,V))
    gamma = covariance(a,b,c,d,U,V)
    if r%2:
        expected = F(0)
    elif r%4==0:
        expected = F(1,4*b*d)
    else:
        expected = F(-3,4*b*d)
    assert gamma==expected,(r,gamma,expected)
print('R148B_INFINITE_SIGN_FAMILY_FINITE_RECHECK_PASS',
      'r=1..50','positive',12,'negative',13,'zero',25)
