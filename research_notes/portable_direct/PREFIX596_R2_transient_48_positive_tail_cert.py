#!/usr/bin/env python3
"""PREFIX596-R2: exact native 48-positive tail for all nonnegative gate weights."""
from pathlib import Path
import json,runpy
s=runpy.run_path(str(Path(__file__).with_name('PREFIX595_R2_full_chamber_positive_49_cert.py')))
A,N,G,axis=(s[k] for k in ('A','N','G','axis'))

C=[[0]*96 for _ in range(48)]
E=[[0]*48 for _ in range(96)]
for j in range(48):
    C[j][2*j]=1
    E[2*j][j]=1
    if j==G:
        E[2*j+1][j]=1
    else:
        C[j][2*j+1]=1
assert all(sum(C[i][k]*E[k][j] for k in range(96))==int(i==j)
           for i in range(48) for j in range(48))

# Gate source is not its own successor: the marked output bit pair is equal
# after each original native transition, for each of seven typed generators.
assert all(A[k][2*G][j]==A[k][2*G+1][j]
           for k in range(7) for j in range(96))

# F_k=C A_k, O_k=A_k E, Q_k=C A_k E.
F=[[[sum(C[i][h]*A[k][h][j] for h in range(96)) for j in range(96)]
      for i in range(48)] for k in range(7)]
O=[[[sum(A[k][i][h]*E[h][j] for h in range(96)) for j in range(48)]
      for i in range(96)] for k in range(7)]
Q=[[[sum(C[i][h]*O[k][h][j] for h in range(96)) for j in range(48)]
      for i in range(48)] for k in range(7)]
assert all(v>=0 for K in F+O+Q for row in K for v in row)

# Coefficientwise verification of the closed symbolic formula:
# Q=diag(x) Drow S Dcol, with Drow=(2 except 1 at g),
# Dcol=(1 except (3+z)/2 at g).
for i in range(48):
    for j in range(48):
        eta=int(G in N[i]);k=axis[i]
        for ell in range(7):
            if j==G and i!=G:
                expected=eta*((3 if ell==k else 0)+(1 if ell==6 else 0))
            elif i==G and j==G:
                expected=0
            elif i==G:
                expected=int(j in N[i] and ell==k)
            else:
                expected=2*int(j in N[i] and ell==k)
            assert Q[ell][i][j]==expected,(ell,i,j,Q[ell][i][j],expected)

def mv(M,v):
    return [sum(a*b for a,b in zip(row,v)) for row in M]

# All 49 labeled pairs and all 96 basis columns:
# A_left A_right = (A_left E)(C A_right) exactly.
checks=0
for left in range(7):
    for right in range(7):
        for source in range(96):
            a1=[A[right][i][source] for i in range(96)]
            direct=mv(A[left],a1)
            f1=[F[right][i][source] for i in range(48)]
            factor=mv(O[left],f1)
            assert direct==factor,(left,right,source)
            checks+=1
assert checks==7*7*96

weighted=s['eval_weighted'];inputs=s['inputs'];sequences=s['sequences']
original=s['step96'];assert len(inputs)==99
paths=0
for r0 in inputs:
    for seq in sequences:
        x1,z1=seq[0]
        r=original(r0,x1,z1)
        v=mv(weighted(F,x1,z1),r0)
        assert mv(C,r)==v
        for x,z in seq[1:]:
            r=original(r,x,z)
            assert mv(weighted(O,x,z),v)==r
            v=mv(weighted(Q,x,z),v)
            assert v==mv(C,r)
            assert min(v)>=0
            paths+=1
assert paths==891

# The polynomial determinant follows from det(native S)=3^12:
# det Q = 2^46 * 3^12 * (z+3) * prod_a x_a^8.
counts={name:[sum(sum(row) for row in M) for M in matrices]
        for name,matrices in [('F',F),('O',O),('Q',Q)]}
result={
 'schema':'PREFIX596_R2_POSITIVE_48_TAIL_V1',
 'scientific_input':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'native_ports':96,'phase_states':48,'gate_target_phase':G,
 'encoding':'47 ordinary bit sums and one equal gate bit, valid after first original step',
 'domain':'arbitrary x_a>=0,z>=0 varying stepwise, full original 96-port outputs t>=2',
 'rank_generic_tail':48,
 'determinant_formula':'det Q(x,z)=2^46*3^12*(z+3)*product(x_a^8)',
 'first_transition_49_if_z1_not_1':True,
 'native_tagged_gate_bit_equalities':672,
 'typed_tail_coefficients_checked':7*48*48,
 'two_step_typed_basis_checks':checks,
 'nonstationary_tail_full_port_checks':paths,
 'typed_nonzero_by_label':counts,
 'status':'ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED'}
Path(__file__).with_name('PREFIX596_R2_transient_48_positive_tail_results.json').write_text(
    json.dumps(result,indent=2)+'\n')
print(result['status'],'two-step',checks,'tail',paths)
