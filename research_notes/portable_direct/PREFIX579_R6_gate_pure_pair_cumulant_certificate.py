#!/usr/bin/env python3
"""PREFIX-579-R6: exact third-order cross-axis gate-residual certificate.
Model pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Runs the previously published 96-port BRC third-cumulant certificate and
checks a new rank-four, zero-diagonal gate-residual interaction form.
Requires published PREFIX565_positive_marginal_certificate.py,
PREFIX578_R6_compact_third_cumulant_certificate.py and
PREFIX577_R6_PUBLISHED_RESULTS.json alongside this file.
"""
import json
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'
NAME=('R1','R2','R3','R4','R5','R6','K')


def certify():
    p=subprocess.run([sys.executable,str(HERE/'PREFIX578_R6_compact_third_cumulant_certificate.py')],
                     cwd=HERE,capture_output=True,text=True,check=True)
    prev=json.loads(p.stdout)
    assert prev['status']=='ALL_CHECKS_PASS' and prev['science_pin']==PIN
    assert prev['finite_states']==96 and prev['primitive_labeled_edges']==576
    assert prev['independent_third_entries']==56 and prev['full_seven_dimensional_entries']==84
    tensor={tuple(k.split(',')):F(v) for k,v in prev['full_tensor'].items()}
    assert len(tensor)==84
    def third(a,b,c):
        return tensor[tuple(sorted((a,b,c),key=NAME.index))]
    # Y = K - (5R1-R2+5R3-R4-4R5-4R6)/192.
    # Equivalently Y = K -(3R1+R2+3R3+R4)/64 + n/48 at zero root.
    y={NAME[i]:-F(b,192) for i,b in enumerate((5,-1,5,-1,-4,-4))}
    y['K']=F(1)
    cov_data=json.loads((HERE/'PREFIX577_R6_PUBLISHED_RESULTS.json').read_text())
    assert cov_data['status']=='ALL_CHECKS_PASS'
    cov=[[F(v) for v in row] for row in cov_data['covariance_rate']]
    w=[y[k] for k in NAME]
    assert all(sum(w[a]*cov[a][j] for a in range(7))==0 for j in range(6))
    assert sum(w[a]*w[b]*cov[a][b] for a in range(7) for b in range(7))==F(367,73728)
    B=[[sum(coeff*third(j,'R'+str(i+1),'R'+str(k+1))
             for j,coeff in y.items()) for k in range(6)] for i in range(6)]
    M=[[int(v*73728) for v in row] for row in B]
    assert all(F(M[i][j],73728)==B[i][j] for i in range(6) for j in range(6))
    expected=[[0,0,34,-24,-5,-5],
              [0,0,-24,14,5,5],
              [34,-24,0,0,-5,-5],
              [-24,14,0,0,5,5],
              [-5,5,-5,5,0,0],
              [-5,5,-5,5,0,0]]
    assert M==expected and all(M[i][j]==M[j][i] for i in range(6) for j in range(6))
    assert all(M[i][i]==0 for i in range(6))
    assert all(sum(row)==0 for row in M)
    assert all(row[4]==row[5] for row in M)
    assert (34*14-24*24)**2==10000
    D={'R5':F(1),'R6':F(-1)}
    def mixed(c,a,b):
        return sum(x*y*z*third(i,j,k) for i,x in c.items()
                   for j,y in a.items() for k,z in b.items())
    assert mixed(y,D,D)==0
    assert all(mixed(y,D,{'R'+str(j+1):F(1)})==0 for j in range(6))
    assert mixed(y,{'R1':F(1),'R3':F(1)},
                    {'R1':F(1),'R3':F(1)})==F(17,18432)
    assert mixed(y,{'R1':F(1),'R4':F(1)},
                    {'R1':F(1),'R4':F(1)})==-F(1,1536)
    assert all(third(*key)==third(*tuple('R6' if x=='R5' else 'R5' if x=='R6' else x
                                for x in key)) for key in tensor)
    assert all(sum(third('R'+str(i+1),NAME[j],NAME[k]) for i in range(6))==0
               for j in range(7) for k in range(7))
    return {'status':'ALL_CHECKS_PASS','science_pin':PIN,
            'parent_source':'PREFIX578_R6_compact_third_cumulant_certificate.py',
            'model_states':96,'labeled_actions':576,'parent_tensor_entries':84,
            'observable':'Y=K-(5R1-R2+5R3-R4-4R5-4R6)/192',
            'matrix_B_equals_M_over':73728,'matrix_M':M,'matrix_rank':4,
            'nullspace_basis':[[1,1,1,1,1,1],[0,0,0,0,1,-1]],
            'leading_principal_minor_M4':10000,
            'axis_diagonal_zero_checks':6,'second_order_orthogonality_checks':6,
            'gate_residual_variance_rate':'367/73728',
            'conservation_null_checks':6,'axis_swap_null_checks':6,
            'full_tensor_axis_swap_checks':84,'full_tensor_conservation_checks':49,
            'mixed_Y_R1plusR3_squared':'17/18432',
            'mixed_Y_R1plusR4_squared':'-1/1536',
            'scope':'n->infinity third joint cumulant rates of uniform 6-action native walk; author exact rational proof',
            'review_status':'UNREVIEWED / NOT_ADMITTED'}

if __name__=='__main__':
    print(json.dumps(certify(),indent=2,ensure_ascii=False))
