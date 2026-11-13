"""Independent signed BRC Newton replay; integers only; source R340/R341."""
import hashlib,json
from math import comb

def C(n,k):return comb(n,k) if 0<=k<=n else 0
def add(A,B):
 Z=A.copy()
 for j,v in B.items():
  Z[j]=Z.get(j,0)+v
  if not Z[j]:del Z[j]
 return Z
def mul(A,B):
 Z={}
 for i,v in A.items():
  for j,w in B.items():Z[i+j]=Z.get(i+j,0)+v*w
 return {i:v for i,v in Z.items() if v}
def t(n,v,s):return {s+j:v*C(n,j) for j in range(n+1)} if n>=0 and v else {}
def K(i):
 d=(-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3));z={}
 for h,v in enumerate(d,1):z=add(z,t(i+1-h,-v,i-1))
 return z
def J(s):
 z={}
 for v,n in ((-C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2)):z=add(z,t(n,v,s))
 return z
def solve(n=320):
 B=[{0:1,1:1}];ks={i:K(i) for i in range(1,13)}
 for s in range(1,2*n+5):
  z=J(s) if s<=10 else {}
  for i in range(1,min(12,s)+1):z=add(z,mul(ks[i],B[s-i]))
  B.append(z)
 assert all(B[s].get(j,0)>0 for s in range(len(B)) for j in range(s+1))
 D=[]
 for q in range(n+3):
  a=[2**(q-v)*B[q+v].get(q,0) for v in range(q+1)];row=[]
  direct=[sum((-1)**(k-v)*C(k,v)*a[v] for v in range(k+1)) for k in range(q+1)]
  while a:
   row.append(a[0]);a=[a[j+1]-a[j] for j in range(len(a)-1)]
  assert row==direct and all(x>0 for x in row) and row[-1]==5**q
  D.append(row)
 assert [D[5][0],D[5][1],D[6][0],D[6][1]]==[7008,43600,80512,414400]
 h=hashlib.sha256();edge=hashlib.sha256();h3=hashlib.sha256();neg3=[];edge_bad=[]
 for q in range(1,n+1):
  for k in range(q):
   m=D[q][k]*D[q+1][k+1]-D[q][k+1]*D[q+1][k]
   assert m!=0
   if k:assert m>0;h.update(f'{q},{k}:{m}\n'.encode())
   else:
    edge.update(f'{q}:{m}\n'.encode())
    if m<0:edge_bad.append(q)
  if q>=3:
   for k in range(1,q-1):
    A=[[D[q+i][k+j] for j in range(3)] for i in range(3)]
    a,b,c=A[0];d,e,f=A[1];g,hv,j=A[2]
    x=a*(e*j-f*hv)-b*(d*j-f*g)+c*(d*hv-e*g)
    h3.update(f'{q},{k}:{x}\n'.encode())
    if x<0:neg3.append((q,k,str(x)))
 assert edge_bad==list(range(5,n+1))
 if n==320:
  assert h.hexdigest()=='f7ab9b1cdb8edb82e8c0d29b604cd1129748faaf9449fbe711fe8f3acb6b63ff'
  assert edge.hexdigest()=='5d7e481d4bd9eb9f698376406b28fe2fc5dc85f85a1cd0be06c98e5f6d7c7c83'
 assert neg3[:1]==[(8,1,'-11584498914207849250816')]
 A=[[D[8+i][1+j] for j in range(3)] for i in range(3)]
 assert A==[[43805312,78344512,91806720],[469858304,857183744,1074865856],[5090189312,9447016960,12488498560]]
 from itertools import combinations
 minors=[A[r][c]*A[s][d]-A[r][d]*A[s][c] for r,s in combinations(range(3),2) for c,d in combinations(range(3),2)]
 assert len(minors)==9 and min(minors)==738381811220480 and all(x>0 for x in minors)
 L=A[0][0]*A[1][1]-A[0][1]*A[1][0];R=A[1][1]*A[2][2]-A[1][2]*A[2][1]
 U=A[0][1]*A[1][2]-A[0][2]*A[1][1];V=A[1][0]*A[2][1]-A[1][1]*A[2][0]
 assert L*R-U*V==A[1][1]*int(neg3[0][2])
 return dict(status='PASS',q_max=n,interior_TP2_positive=n*(n-1)//2,R340_TP2_sha256=h.hexdigest(),R340_edge_sha256=edge.hexdigest(),TP3_tested=sum(q-2 for q in range(3,n+1)),TP3_negative=neg3,TP3_sha256=h3.hexdigest(),TP3_positive=sum(q-2 for q in range(3,n+1))-len(neg3),TP3_zeros=0,first_block=A,minor2_min=min(minors),negative_det=neg3[0][2],dodgson_diff=str(L*R-U*V),signed_external_negative=sum(v<0 for s,x in enumerate(B) for degree,v in x.items() if degree>s))
if __name__=='__main__':
 r=solve();open('R342_RECEIPT.json','w').write(json.dumps(r,sort_keys=True,ensure_ascii=False,indent=2)+'\n');print(r['status'],r['TP3_tested'],len(r['TP3_negative']))
