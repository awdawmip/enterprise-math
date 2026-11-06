"""Exact modular validation of the p-adic low-cutoff Picard defect and jet; no native benchmark."""
from math import comb

def ps(n):
    s = bytearray(b'\x01')*(n+1); s[:2]=b'\x00\x00'
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i] = b'\x00'*((n-i*i)//i+1)
    return [p for p in range(7,n+1) if s[p] and p%6==1]

def verify(p):
    m=(p-1)//6; q=p*p
    d=[1]
    for i in range(m):
        d.append(d[-1]*(6*i+1)*(3*i+1)*pow(36*(i+1)**2,-1,q)%q)
    e=[0, pow(10,-1,q)]
    for r in range(1,m):
        e.append(e[-1]*36*r*r*pow((6*r+5)*(3*r+2),-1,q)%q)
    low_source=-(6*m+1)*(3*m+1)*d[m]%q
    assert low_source%p==0 and low_source//p!=0
    assert ((low_source//p)+(3*m+1)*d[m])%p==0
    for i in range(m+2):
        D=36*i*i*(d[i] if i<=m else 0)-(6*i-5)*(3*i-2)*(d[i-1] if 1<=i<=m+1 else 0)
        expect=low_source if i==m+1 else 0
        assert (D-expect)%q==0,(p,i,'D')
        E=(6*i-1)*(3*i-1)*(e[i] if i<=m else 0)-36*(i-1)**2*(e[i-1] if 1<=i<=m+1 else 0)
        exp=(1 if i==1 else -36*m*m*e[m] if i==m+1 else 0)
        assert (E-exp)%q==0,(p,i,'E')
    # Consumed first-order parameter-jet, checked against original d_i.
    H=0
    for i in range(m+1):
        b=comb(m,i)*comb(2*m,i)*pow(pow(2,i,q),-1,q)%q
        assert (d[i]-b*(1+p*H))%q==0,(p,i,'jet')
        if i<m:
            H+=pow(6*i+1,-1,q)+pow(3*i+1,-1,q)
            H%=q
    return {'p':p,'m':m,'low_endpoint_divided_by_p_mod_p':low_source//p,
            'complementary_endpoint_mod_p':(-36*m*m*e[m])%p}

if __name__=='__main__':
    v=[verify(p) for p in ps(997)]
    print('ALL_CHECKS_PASS',len(v),'p<=997 p=1 mod6; mod p^2 exact operator coefficients and d-to-binomial jet')
    for x in v:
        if x['p'] in (13,19,67,373):print(x)
