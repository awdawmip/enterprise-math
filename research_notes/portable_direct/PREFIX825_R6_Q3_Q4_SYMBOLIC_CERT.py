#!/usr/bin/env python3
"""Optional SymPy exact symbolic certificates for PREFIX825.

Checks TQ=M T, W T=C, and nonzero symbolic observability minors.
Run: python PREFIX825_R6_Q3_Q4_SYMBOLIC_CERT.py (requires sympy).
"""
from sympy import Matrix, symbols, factor, simplify
from PREFIX825_R6_Q3_Q4_POSITIVE_MINIMAL_CHECK import (
    labels, q3_rows, q4_rows, model_operator, output_operator,
    rows_to_matrix, q3_update, q4_update, output, CERT)
import json


def check(q):
    a,b=symbols('a b', positive=True, integer=True)
    L=labels(q)
    T=Matrix(rows_to_matrix(q3_rows(a,b) if q==3 else q4_rows(a,b),L))
    Q=Matrix(model_operator(q,a,b,L))
    C=Matrix(output_operator(q,L))
    M=Matrix.hstack(*[Matrix(q3_update(T[:,j],a,b) if q==3 else q4_update(T[:,j],a,b))
                        for j in range(T.cols)])
    W=Matrix.hstack(*[Matrix(output(T[:,j],q)) for j in range(T.cols)])
    assert T*Q==M, 'symbolic intertwining fails'
    assert W==C, 'symbolic outputs fail'
    O=Matrix.vstack(*[C*Q**j for j in range(10)])
    rows,cols=CERT[q]['rows'],CERT[q]['cols']
    minor=O.extract(rows,cols)
    det=factor(minor.det(method='domain-ge'))
    assert simplify(det-CERT[q]['det'](a,b))==0,(q,det)
    return {'capacity':q,'moment_dimension':T.cols,
            'quotient_dimension':T.rows,'minor_determinant':str(det),
            'symbolic_intertwining':'PASS','symbolic_observer':'PASS'}


if __name__=='__main__':
    items=[check(3),check(4)]
    print(json.dumps({'result':'ALL_SYMBOLIC_CERTIFICATES_PASSED','cases':items},indent=2))
