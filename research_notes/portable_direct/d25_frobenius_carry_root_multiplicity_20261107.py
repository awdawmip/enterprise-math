"""D25 exact F_p carrier roots and second/third jets (author-side, no native run)."""
from math import isqrt


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n)+1))


def jet(p):
    assert is_prime(p) and p % 8 == 5
    k = (p-5)//8
    z = pow(9, -1, p)
    c, h, d, d2, x = 1, 1, 0, 0, 1
    for j in range(1, k+1):
        c = c*(k-j+1)*(3*k+2-j)*pow(j*j, -1, p) % p
        xprev, x = x, x*z % p
        h = (h+c*x) % p
        d = (d+j*c*xprev) % p
        if j >= 2:
            d2 = (d2+j*(j-1)*c*xprev*pow(z,-1,p)) % p
    assert (z*(1-z)*d2+(1+4*k*z)*d-k*(3*k+1)*h)%p == 0
    q = (1-z)*h*h % p
    dq = (-h*h+2*(1-z)*h*d) % p
    ddq = (-4*h*d+2*(1-z)*(d*d+h*d2)) % p
    C, Cp, Cpp = -z*q%p, -z*dq%p, -z*ddq%p
    Cppp = -z*6*((1-z)*d*d2-d*d) % p if h == 0 else None
    if h == 0:
        assert d and C == Cp == 0
        assert Cpp == -16*pow(81,-1,p)*d*d%p and Cpp
        assert (16*d2+117*d)%p == 0
        assert Cppp == 5*d*d%p and Cppp
        assert (8*z*z*Cpp)%p != 0
    return p, k, h, d, C, Cp, Cpp, Cppp


if __name__ == "__main__":
    data = [jet(p) for p in range(5,30000) if p%8==5 and is_prime(p)]
    a = [r for r in data if r[0]%24==13]
    b = [r for r in data if r[0]%24==5]
    assert (len(data),len(a),len(b)) == (815,407,408)
    assert all(r[2]==0 for r in a)
    assert all(r[2]!=0 for r in b)
    print("EXACT_Fp_JETS_PASS",len(data),"class13_root",len(a),"class5_nonroot",len(b))
    for p,k,h,d,c,cp,cpp,cppp in data:
        if p in (13,29,37,61,109,181,373):
            print(p,k,h,d,c,cp,cpp,cppp,8*pow(9,-2,p)*cpp%p if h==0 else "not-root")
