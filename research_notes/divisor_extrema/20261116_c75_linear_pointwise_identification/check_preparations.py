"""Exact consecutive initial minors for arbitrary input pairs in the two-block model."""
from check_calibration import determinant, forward_coefficients
from hashlib import sha256
import json

TERMS = ((0,3),(0,2),(1,3),(1,2),(1,1),(2,3),(2,2),(2,1),(2,0))


def raw_rows(x, size, terms):
    rows=[]
    A=B=C=1
    for step in range(size):
        rows.append([A**j*C**i*4**(step*(5-j))*B**(5-i-j) for i,j in terms[:size]])
        A *= 4*x+9+4*step
        B *= x+6+step
        C *= x+21+step
    return rows


def certificate():
    result=[]
    # These are the two unsigned cofactors at the third and fifth positions.
    for omit in (2,4):
        terms=TERMS[:omit]+TERMS[omit+1:]
        for size in range(1,len(terms)+1):
            degree=5*size*(size-1)//2
            coefficients=forward_coefficients([determinant(raw_rows(x,size,terms))
                                              for x in range(2,3+degree)])
            assert coefficients[0]>0 and min(coefficients)>=0
            result.append(dict(omitted_column=omit+1,size=size,degree_bound=degree,
                               positive_coefficients=sum(v>0 for v in coefficients),
                               sha256_newton=sha256((','.join(map(str,coefficients))+'\n').encode('ascii')).hexdigest()))
    return dict(K=5,c_start=2,terms=TERMS,initial_minors=result)

if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
