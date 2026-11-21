"""Independent literal seven-mask joint-load countercheck of VERIFY_ALLM.

Run in the same directory: python VERIFY_DIRECT.py
Recomputes small thresholds without any max-load formulas and also tests
the threshold-recurrence at additional values 1<=m<=44.
"""
from VERIFY_ALLM import zero,mono,add,mul,factors,seq_h,phi,numerator_rows,S

def direct(m):
    hu=seq_h((216,217,218),m)
    hj=seq_h((219,220,221),m)
    products=[[mul(hu[u],hj[j]) for j in range(m)] for u in range(m)]
    shift=[[mul(mono(214*x),mono(215*y)) for y in range(m)] for x in range(m)]
    total=zero()
    for mask in range(1,8):
        indices=[i for i in (0,1,2) if mask>>i&1]
        prices=sorted(set().union(*(S[i] for i in indices)))
        xs=range(m) if 214 in prices else range(1)
        ys=range(m) if 215 in prices else range(1)
        js=range(m) if 219 in prices else range(1)
        partial=zero()
        for u in range(m):
            for x in xs:
                for y in ys:
                    for j in js:
                        loads=(x+y+u,x+j+u,y+j+u)
                        if any(loads[i]>=m for i in indices):continue
                        weight=products[u][j] if 219 in prices else hu[u]
                        partial=add(partial,mul(shift[x][y],weight))
        term=mul(factors(prices),partial)
        total=add(total,term,1 if len(indices)%2 else -1)
    return phi(total)

def verify():
    rows=[phi(v) for v in numerator_rows(120)]
    for m in (1,2,3,13,19,20,21):
        assert direct(m)==rows[m-1],m
        print('LITERAL LOAD PASS',m)
    for m in range(1,45):
        assert all(rows[m-1+76][i]-2*rows[m-1+38][i]+rows[m-1][i]==0
                   for i in range(18)),m
    print('PASS: 7 literal load checks and 44 recurrence checks')

if __name__=='__main__':verify()
