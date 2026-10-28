#!/usr/bin/env python3
"""Optional second-formula SymPy rational-matrix check for global maximizer witnesses.
The main complete integer-corner proof is verify_prefix309.py; this only crosschecks two witnesses.
"""
import json,sys
from pathlib import Path
import sympy as sp
SOURCE_DIR=Path(__file__).resolve().parent
sys.path.insert(0,str(SOURCE_DIR))
from verify_prefix309 import ORBIT_DATA

def cmp(family,orbit,qpart,budget):
 out=json.loads((SOURCE_DIR/'RESULTS_PREFIX309.json').read_text(encoding='utf-8'))['results']
 record=next(r for r in out if r['family']==family and r['orbit']==orbit and r['q']==qpart)
 M=ORBIT_DATA[family][orbit-1]
 q=sp.Integer(qpart[0])+sp.I*sp.Integer(qpart[1]);q2=q*q
 rows=[[4,4*q,0],[0,-4,4*q]]
 for row in M:
  rows.append([(sp.Integer(z[0])+sp.I*sp.Integer(z[1]))*t for z,t in zip(row,[1,q,q2])])
 if budget==8:
  omit=record['eight_ref']['optimal_omissions'][0]
  rows.pop(int(omit[1])+1)
  record=next(z for z in record['eight_ref']['options'] if z['omit_port']==omit)
 else:
  record=record['ten_ref']
 U=sp.Matrix(rows)/8
 noise=[(sp.Integer(p1)-p0+sp.I*(sp.Integer(pi)-p0))/2
        for p0,p1,pi in record['signed_error_witness']]
 delta=(U.conjugate().T*U).inv()*U.conjugate().T*sp.Matrix(noise)
 norm=sp.factor((delta.conjugate().T*delta)[0])
 expected=sp.Rational(record['gain_squared'] if budget==8 else record['squared_gain'])
 assert norm==expected,(norm,expected)
 return str(norm)

if __name__=='__main__':
 print('8=',cmp('S7',5,[0,1],8))
 print('10=',cmp('S4',3,[1,0],10))
 print('PASS 2 exact independent symbolic witnesses')
