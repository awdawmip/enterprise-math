"""Reproduce R5 primitive 27/31 all-m cyclotomic first-jet phase certificates.
Standard Python 3, exact integer cyclic group ring. No third-party dependencies.
Proof of rational-function recurrence is in RESEARCH.md; finite checks alone are
not the infinite-threshold argument.
"""
import hashlib, json

S=(set(range(214,219)),{214,216,217,218,219,220,221},{215,216,217,218,219,220,221})
S4=set(range(296,313))
def zero(d): return [0]*d
def unit(d): a=zero(d);a[0]=1;return a
def add(a,b): return [x+y for x,y in zip(a,b)]
def sub(a,b): return [x-y for x,y in zip(a,b)]
def scale(a,c): return [c*x for x in a]
def shift(a,p):
 d=len(a);k=p%d
 return a[:] if k==0 else a[-k:]+a[:-k]
def mul(a,b):
 d=len(a);out=zero(d)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:out[(i+j)%d]+=x*y
 return out
def factor(d,p): return sub(unit(d),shift(unit(d),p))
def series_one(d,n): return [unit(d)]+[zero(d) for _ in range(n-1)]
def series_div(A,p):
 out=[]
 for k,v in enumerate(A):
  out.append(add(v,shift(out[-1],p)) if k else v[:])
 return out
def multi_div(A,prices):
 for p in prices:A=series_div(A,p)
 return A
def series_add(A,B): return [add(a,b) for a,b in zip(A,B)]
def series_sub(A,B): return [sub(a,b) for a,b in zip(A,B)]
def t_shift(A,d,p): return [zero(d)]+[shift(A[k-1],p) for k in range(1,len(A))]
def norm(v,d):
 if d==27:return [v[i]-v[18+i%9] for i in range(18)]
 if d==31:return [v[i]-v[30] for i in range(30)]
 raise ValueError(d)
def first_jet_series(d,M):
 X,Y=214,215
 U=(216,217,218); J=(219,220,221)
 p0=216 if d==27 else 217
 p4=297 if d==27 else 310
 z=series_one(d,M)
 Jt=multi_div(z,J)
 JXYt2=[zero(d) for _ in range(M)]
 for j in range((M+1)//2):JXYt2[2*j]=shift(Jt[j],(X+Y)*j)
 Bs={}
 for Z in (X,Y):
  B=[];sj=zero(d);gz=zero(d)
  for n in range(M):
   sj=add(sj,Jt[n])
   if n:gz=add(gz,shift(unit(d),Z*(n-1)))
   B.append(add(shift(sj,Z*n),mul(Jt[n],gz)))
  Bs[Z]=B
 A={}
 A[1]=multi_div(z,(X,Y))
 A[2]=series_div(Jt,X)
 A[4]=series_div(Jt,Y)
 A[3]=series_div(Bs[Y],X)
 A[5]=series_div(Bs[X],Y)
 A[6]=series_add(multi_div(Jt,(X+Y,X)),multi_div(t_shift(Jt,d,Y),(X+Y,Y)))
 diff=series_sub(Jt,JXYt2)
 A[7]=series_add(multi_div(JXYt2,(X,Y)),series_add(multi_div(diff,(X+Y,Y)),multi_div(t_shift(diff,d,X),(X+Y,X))))
 terms=[zero(d) for _ in range(M)]
 for mask in range(1,8):
  sup=set().union(*(S[k] for k in range(3) if mask&(1<<k)))
  assert [p for p in sorted(sup) if p%d==0]==[p0]
  Q=unit(d)
  for p in sorted(sup-{p0}):Q=mul(Q,factor(d,p))
  sign=1 if mask.bit_count()%2 else -1
  for n in range(M):terms[n]=add(terms[n],scale(mul(Q,A[mask][n]),-p0*sign))
 first=multi_div(terms,U)
 Q4=unit(d)
 for p in sorted(S4-{p4}):Q4=mul(Q4,factor(d,p))
 H4=multi_div(z,sorted(S4))
 out=[];acc=zero(d)
 for n in range(M):
  acc=add(acc,sub(first[n],scale(mul(Q4,H4[n]),p4)))
  out.append(norm(acc,d))
 return out
EXPECTED_SHA={
27:["e777bf45f765b115b0ba9ec2ba884d3defa54707726a11eb535a85c3450ed028","e6e38f774ad14de676d41542a60cae60c8407bba85e1d90f1a0618310731e615","7c3b24c507e001b13cc7ecb01e6231bafde870aa062618d65b8bacb3e27c76af","d1bf098c6b0d6309916194e23df997e0e5c35facbcccf1f3a58dff4abfc06ca2","6789a1f6db7c1b9140bfd67cf48b5b732e293c133747b751855992cf20067c01"],
31:["3878ba3c95859a42fd7d0067c1a9b8f192ad95a166060bb4cf36d4c305edeb56","ccc20519bf337e1ed59eefdc51c1d1f25837b8324a40a3f2885b42c2aaeb5c86","0235b4038020bc9d18b21474dd8cca4c99b483249ae0ae0c6900a7fff31241ae","e004c907018f55d16ff2e900f2c28ab99edf7e2c9c8fab23783dfd736587b52b","234fab3608ba652f413d7c18ba1232ece5ff36aa6cedaebcf27f6c56a6a1241a"]}
def first_nonzero_minor(a,b):
 for i in range(len(a)):
  for j in range(i+1,len(a)):
   det=a[i]*b[j]-a[j]*b[i]
   if det:return {'indices_zero_based':[i,j],'determinant':str(det)}
 return None
def verify():
 report={'schema':'R5_ROOT27_31_ALLM_FIRST_JET_V2','scientific_input':'f003690c912ffc1cd923c33176155a6fe82d69ba','arithmetic':'exact_integer_cyclic_group_ring','proof_identity':'G_d(t)=P_d(t)/(1-t^(2d))^3','verification':{},'phase_certificates':[]}
 for d in (27,31):
  T=2*d;M=3*T
  vectors=first_jet_series(d,M+5)
  for m,expected in enumerate(EXPECTED_SHA[d],start=1):
   actual=hashlib.sha256(json.dumps(vectors[m-1],separators=(',',':')).encode()).hexdigest()
   assert actual==expected,(d,m,actual,expected)
  minor_count=0
  for r in range(T):
   a,b,c=vectors[r],vectors[r+T],vectors[r+2*T]
   assert all(c[i]-2*b[i]+a[i]==0 for i in range(len(a))),(d,r+1)
   witness={'d':d,'phase_r':r+1}
   minor=first_nonzero_minor(a,b)
   if r<T-5:
    assert minor is not None,(d,r+1)
    witness.update(minor);witness['type']='INDEPENDENT_PAIR';minor_count+=1
   else:
    assert b==[2*x for x in a],(d,r+1)
    i=next((i for i,x in enumerate(a) if x),None)
    assert i is not None
    witness.update({'type':'DOUBLING_NONZERO','coordinate_zero_based':i,'a_coordinate':str(a[i])})
   report['phase_certificates'].append(witness)
  for j in range(5):
   assert vectors[3*T+j]==[3*vectors[2*T+j][i]-3*vectors[T+j][i]+vectors[j][i] for i in range(len(vectors[j]))]
  report['verification'][str(d)]={'T':T,'basis_m_1_to':M,'initial_previous_complete_vector_sha_regression':5,'exact_second_difference_zero_count':T,'nonzero_independent_pairs':minor_count,'nonzero_terminal_doubling':5,'extra_recurrence_direct_checks':5,'basis_sha256':hashlib.sha256(json.dumps(vectors[:M],separators=(',',':')).encode()).hexdigest()}
  print('PASS',d,'phase certificates',T,'independent minors',minor_count,'doubling',5)
 return report
if __name__=='__main__':
 print(json.dumps(verify(),indent=2,ensure_ascii=False))
