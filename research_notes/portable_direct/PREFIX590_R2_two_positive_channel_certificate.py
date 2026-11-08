#!/usr/bin/env python3
"""PREFIX590: exact universal two-positive-channel lift for X6 BRC dual carrier."""
from pathlib import Path
from fractions import Fraction as F
import runpy,json
r=runpy.run_path(str(Path(__file__).with_name('PREFIX589_R2_dual_carrier_certificate.py')))
blocks=r['blocks'];D=r['D'];A=r['A'];weighted=r['weighted'];multiply=r['multiply']
assert len(blocks)==24
# W^-1=P-Q with P=(J-I)/3 and Q=2I/3. This nonnegative split is entrywise minimal.
P=[[F(0)]*96 for _ in range(96)]
Q=[[F(0)]*96 for _ in range(96)]
W=[[0]*96 for _ in range(96)]
for group in blocks:
 for i in group:
  Q[i][i]=F(2,3)
  for j in group:
   if i!=j:P[i][j]=F(1,3);W[i][j]=1
assert all(P[i][j]-Q[i][j]==(F(1,3) if W[i][j] else (-F(2,3) if i==j else F(0)))
           for i in range(96) for j in range(96))
assert all(x>=0 for row in P+Q for x in row)
assert all(sum(P[i][j] for i in range(96))==1 for j in range(96))
assert all(sum(Q[i][j] for i in range(96))==F(2,3) for j in range(96))
def matmul(M,v):return [sum(t*w for t,w in zip(row,v)) for row in M]
for singled in range(96):
 v=[int(i==singled) for i in range(96)]
 pos=matmul(P,v);neg=matmul(Q,v)
 assert sum(t!=0 for t in pos)==3 and sum(t!=0 for t in neg)==1
 assert all(pos[i]>=0 and neg[i]>=0 for i in range(96))
 assert all(pos[i]-neg[i]==(F(1,3)*sum(v[j] for j in blocks[r['bid'][i]])-v[i])
            for i in range(96))
# Nonuniform native input/output endpoints, and time-varying exact source weights.
for v in [[1]*96,[int(i%7==0) for i in range(96)],[int(i==5) for i in range(96)]]:
 l=[int(i%11==0) for i in range(96)]
 native=list(map(F,v));positive=matmul(P,v);negative=matmul(Q,v)
 dual_left=matmul(W,l)  # W is symmetric
 for x,z in [((1,)*6,0),((2,3,5,7,11,13),17),((0,1,0,1,0,1),2)]:
  originalA=weighted(A,x,z);dualA=weighted(D,x,z)
  native=multiply(originalA,native)
  positive=multiply(dualA,positive)
  negative=multiply(dualA,negative)
  assert all(q>=0 for q in positive+negative)
  actual=sum(l[i]*native[i] for i in range(96))
  split=sum(dual_left[i]*(positive[i]-negative[i]) for i in range(96))
  assert actual==split
out={
 'schema':'PREFIX590_R2_UNIVERSAL_POSITIVE_LINEAR_BRC_SPLIT_V1',
 'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'exact_linear_split':'W^-1=P-Q; P=W/3>=0; Q=2I/3>=0',
 'minimality':'For any Pprime,Qprime >=0 with Pprime-Qprime=W^-1, entrywise Pprime>=P and Qprime>=Q',
 'input_domain':'arbitrary original r>=0; no endpoint-specific buffers',
 'channel_semantics':'Two nonnegative BRC dual streams, final signed readout subtraction',
 'original_port_basis_vectors_tested':96,
 'nonstationary_weight_sequences_tested':3,
 'nonstationary_sequence_length':3,
 'per_positive_channel_mass':'sum(Pr)=sum(r), sum(Qr)=2/3*sum(r)',
 'sparse_direct_cost':'Up to two 576-edge dual products per step versus one original product',
 'status':'ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED'
}
Path(__file__).with_name('PREFIX590_R2_two_positive_channel_results.json').write_text(
 json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(out['status'])
