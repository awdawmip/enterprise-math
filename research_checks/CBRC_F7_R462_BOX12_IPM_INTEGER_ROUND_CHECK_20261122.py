#!/usr/bin/env python3
"""B12 F7 solver-generated rational witness, followed by exact integer verification.
SciPy + NumPy are needed only to generate the candidate. The actual bound
is certified by enumerating the complete original B12 input box in integers.
This is a reproducible experimental generator, not a fixed literal certificate.
"""
import hashlib
import json
from itertools import product
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

B = 12
M = 1_000_000
coordinates = {}

def term(a, b):
    if a == b == 0:
        return None, 0
    if b == 0:
        return None, 1
    key = (abs(a), b)
    if key in ((2, 1), (1, -1)):
        return None, .5
    if key not in coordinates:
        coordinates[key] = len(coordinates)
    return coordinates[key], .5

def build_linear_inequalities():
    distinct = set()
    for a, b, c, d in product(range(-B, B + 1), repeat=4):
        k = a - 2*b - c + 2*d
        parts = [term(a+k, b+k), term(c-k, d-k), term(a,b), term(c,d)]
        coefficients = {}
        const = 0.
        for (index, value), sign in zip(parts, (1,1,-1,-1)):
            const += sign*value
            if index is not None:
                coefficients[index] = coefficients.get(index, 0) + sign
        coeff = tuple(sorted((index,value) for index,value in coefficients.items() if value))
        if not coeff:
            assert abs(const) <= .5
            continue
        if coeff[0][1] < 0:
            coeff = tuple((index,-value) for index,value in coeff)
            const = -const
        distinct.add((coeff, round(2*const)))
    rows=[]; cols=[]; data=[]; rhs=[]
    for j,(coeff,c2) in enumerate(distinct):
        for index,val in coeff:
            rows.extend((2*j,2*j+1)); cols.extend((index,index)); data.extend((val,-val))
        rhs.extend((.5-c2/2,.5+c2/2))
    return coo_matrix((np.float64(data),(rows,cols)), shape=(len(rhs),len(coordinates))).tocsr(),np.asarray(rhs)

def main():
    A,rhs=build_linear_inequalities()
    result=linprog(np.zeros(A.shape[1]),A_ub=A,b_ub=rhs,bounds=(0,None),method="highs-ipm",options={"time_limit":120})
    if not result.success:
        raise RuntimeError(f"B12 numerical candidate generation did not finish: {result.message}")
    increments={key:int(round(float(result.x[index])*M)) for key,index in coordinates.items()}
    increments={key:n for key,n in increments.items() if n!=0}
    def q(a,b):
        if a==0 and b==0:return 0
        if b==0:return M
        key=(abs(a),b)
        if key in ((2,1),(1,-1)):return M//2
        return M//2+increments.get(key,0)
    maxabs=0;checked=0;saturators=0
    for a,b,c,d in product(range(-B,B+1),repeat=4):
        k=a-2*b-c+2*d
        D=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d)
        if abs(D)>maxabs:
            maxabs=abs(D);saturators=1
        elif abs(D)==maxabs:
            saturators+=1
        checked+=1
    assert checked==25**4
    assert maxabs <= 500001, (maxabs,M)
    table=json.dumps(sorted((a,b,n) for (a,b),n in increments.items()),separators=(',',':'))
    print("EXACT B12 ROUNDED CHECK PASSED; inputs",checked,"override count",len(increments),
          "max_abs_D_numerator",maxabs,"denominator",M,"saturators",saturators,
          "table_sha256",hashlib.sha256(table.encode()).hexdigest())

if __name__ == '__main__':main()
