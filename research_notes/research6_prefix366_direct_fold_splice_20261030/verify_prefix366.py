#!/usr/bin/env python3
from fractions import Fraction as Q
from pathlib import Path
import json
Z=Q(0);one=Q(1)
qa=list(map(Q,[34000,3200,58250,46600,31525]));qb=list(map(Q,[204144,56336,1286,12936,28011]))
forms=[(Z,[Q(1),Z,Z,Z],Z,[Z,Q(1),Z,Z]),(Z,[Z,Z,Q(1),Z],Z,[Z,Z,Z,Q(1)]),(Q(5,2),[Q(3,2),Q(-7,2),Z,Q(-4)],Q(9,2),[Q(7,2),Q(3,2),Q(4),Z]),(Q(11,4),[Q(11,4),Q(-15,8),Q(5,4),Q(-9,4)],Q(15,8),[Q(15,8),Q(11,4),Q(9,4),Q(5,4)])]
Hs=[[[2*(a[j]*a[l]+b[j]*b[l]) for l in range(4)]for j in range(4)]for c,a,d,b in forms]
def hgj(x):
 H=[];G=[]
 for c,a,d,b in forms:
  re=c+sum(a[j]*x[j]for j in range(4));im=d+sum(b[j]*x[j]for j in range(4))
  H.append(re*re+im*im);G.append([2*(re*a[j]+im*b[j]) for j in range(4)])
 return H,G

def fm(y,s):
 x=[*y[:3],s];t=y[3];H,G=hgj(x); q1=qa[0]+qb[0]*t
 F=[q1*H[k]-qa[k+1]-qb[k+1]*t for k in range(4)]
 E=[[q1*G[k][j] for j in range(3)]+[qb[0]*H[k]-qb[k+1]]for k in range(4)]
 FS=[q1*G[k][3]for k in range(4)]
 return F,E,FS,H,G

def inv(A):
 N=len(A);T=[list(map(Q,A[i]))+[Q(int(i==j))for j in range(N)]for i in range(N)]
 for j in range(N):
  k=next((i for i in range(j,N)if T[i][j]),None)
  if k is None:raise ValueError('singular')
  T[k],T[j]=T[j],T[k]; w=T[j][j];T[j]=[v/w for v in T[j]]
  for i in range(N):
   if i==j:continue
   w=T[i][j];T[i]=[T[i][h]-w*T[j][h]for h in range(2*N)]
 return [r[N:]for r in T]

def dot(a,b):return sum((x*y for x,y in zip(a,b)),Z)
def matvec(A,v):return [dot(row,v)for row in A]
def roundq(x,N=10**18):return Q((x*N+Q(1,2)).numerator//(x*N+Q(1,2)).denominator,N)
def proposal(y,s,steps=1):
 yy=list(y)
 for _ in range(steps):
  f,e,_,_,_=fm(yy,s)
  d=matvec(inv(e),f)
  yy=[roundq(yy[i]-d[i])for i in range(4)]
 return yy

class Iv:
 def __init__(self,a,b=None):self.lo=Q(a);self.hi=Q(a if b is None else b);assert self.lo<=self.hi
 def __add__(self,o):o=conv(o);return Iv(self.lo+o.lo,self.hi+o.hi)
 __radd__=__add__
 def __neg__(self):return Iv(-self.hi,-self.lo)
 def __sub__(self,o):return self+-conv(o)
 def __rsub__(self,o):return conv(o)+-self
 def __mul__(self,o):
  o=conv(o);p=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi];return Iv(min(p),max(p))
 __rmul__=__mul__
 def absup(self):return max(abs(self.lo),abs(self.hi))
 def __str__(self):return '[%.9g,%.9g]'%(float(self.lo),float(self.hi))
def conv(x):return x if isinstance(x,Iv) else Iv(x)

def check(a,b,y,r,concave=True):
 mid=(a+b)/2;ds=(b-a)/2;x=[*y[:3],mid];tt=y[3]
 F,E,Fs,H,g=fm(y,mid);M=inv(E)
 q=qa[0]+qb[0]*tt;qhi=q+qb[0]*r
 dx=[r,r,r,ds]
 de=[[Z]*4 for _ in range(4)]
 for k in range(4):
  for j in range(3):
   gs=sum(abs(Hs[k][j][l])*dx[l]for l in range(4))
   de[k][j]=qhi*gs+qb[0]*r*abs(g[k][j])
  deltaH=sum(abs(g[k][l])*dx[l]for l in range(4))+ Q(1,2)*sum(abs(Hs[k][l][m])*dx[l]*dx[m]for l in range(4)for m in range(4))
  de[k][3]=qb[0]*deltaH
 L=[[sum(abs(M[i][k])*de[k][j]for k in range(4))for j in range(4)]for i in range(4)]
 K=max(map(sum,L))
 fss=[q*Hs[k][3][3]for k in range(4)]
 mc=matvec(M,F);ms=matvec(M,Fs);mss=matvec(M,fss)
 R=max(abs(mc[i])+ds*abs(ms[i])+ds*ds*abs(mss[i])/2 for i in range(4))
 assert K<1 and R+K*r<r,('normcert',float(a),float(b),float(K),float(R),float(r),float(R+K*r-r))
 if not concave:return K,R,r-R-K*r
 b0=[-v for v in ms]
 dfs=[qhi*sum(abs(Hs[k][3][l])*dx[l]for l in range(4))+qb[0]*r*abs(g[k][3])for k in range(4)]
 beta=[sum(abs(M[i][k])*dfs[k]for k in range(4))for i in range(4)]
 e=matvec(inv([[Q(int(i==j))-L[i][j]for j in range(4)]for i in range(4)]),[beta[i]+dot(L[i],[abs(v)for v in b0])for i in range(4)])
 p=[Iv(b0[i]-e[i],b0[i]+e[i])for i in range(3)]+[Iv(1)]
 pt=Iv(b0[3]-e[3],b0[3]+e[3])
 qi=Iv(q-qb[0]*r,q+qb[0]*r)
 gi=[[Iv(g[k][i]-sum(abs(Hs[k][i][l])*dx[l]for l in range(4)),g[k][i]+sum(abs(Hs[k][i][l])*dx[l]for l in range(4)))for i in range(4)]for k in range(4)]
 W=[]
 for k in range(4):
  Hdir=sum((Hs[k][i][j]*p[i]*p[j]for i in range(4)for j in range(4)),Iv(0))
  gt=sum((gi[k][i]*p[i]for i in range(4)),Iv(0))
  W.append(qi*Hdir+2*qb[0]*gt*pt)
 # t'' = -row3(M) W - correction with ||ME-I||
 main=-sum((M[3][k]*W[k] for k in range(4)),Iv(0))
 B=[sum(abs(M[i][k])*W[k].absup() for k in range(4)) for i in range(4)]
 correction=matvec(inv([[Q(int(i==j))-L[i][j] for j in range(4)]for i in range(4)]),matvec(L,B))
 gap=correction[3]
 assert main.hi+gap<0,('concavity',float(a),float(b),float(main.lo),float(main.hi),float(gap),float(K),[float(v)for v in e])
 return K,R,r-R-K*r,main.hi+gap,main.lo-gap


# Formal input: the 62+-digit rational trial center from PREFIX-361, provided
# inline so that this file is independently executable without a checkout.
FOLD_CENTER = list(map(Q,[
'-0.373142042340452907175027641211875750534155477909222485673943462979448485422037',
'-0.0837445473545578199827813837006670780233159346317921776530597395806951736384667',
'-1.00089215574741813465830349283668302546824867512845484704354632234612753727647',
'0.471287741123734760043946207194095912238481474040888194561639891017377903234185',
'0.0669341021803707452694937186221682246630992822998166592940333053391841372650948',
]))
# PREFIX-364 earlier 512-step verifier's exact 10^-12 terminal rational
# witnesses at t=133/2000. They are prior labels, not new root guesses.
OLDER364_TERMINAL = {
 'R0':list(map(Q,['-0.375943629312','-0.068358624255','-1.006329183805','0.462024722284'])),
 'R1':list(map(Q,['-0.369151236831','-0.098660418999','-0.997271060697','0.481264689829']))
}

def main():
 c=FOLD_CENTER; c_y=[c[0],c[1],c[2],c[4]]; sc=c[3]
 halfspan=Q(11,1000)
 a=sc-halfspan; b=sc+halfspan
 N=600; r=Q(7,100000); witness_radius=Q(1,10**7)
 T0=Q(133,2000)
 segments=[]; nodes=[]
 k_max=Z; margin_min=None; t2_upper=None; t2_lower=None
 first_node=proposal(c_y,a,steps=5)
 check(a,a,first_node,witness_radius,concave=False)
 nodes.append(first_node)
 for k in range(N):
  lo=a+(b-a)*k/N;hi=a+(b-a)*(k+1)/N
  assert hi-lo==Q(11,300000)
  mid=(lo+hi)/2
  ym=proposal(nodes[-1],mid)
  K,R,margin,up,low=check(lo,hi,ym,r,concave=True)
  next_node=proposal(ym,hi)
  check(hi,hi,next_node,witness_radius,concave=False)
  for root_point in (nodes[-1],next_node):
   assert max(abs(root_point[j]-ym[j]) for j in range(4))+witness_radius<r, 'endpoint witness must lie strictly inside segment tube'
  nodes.append(next_node)
  segments.append((lo,hi,ym))
  k_max=max(k_max,K)
  margin_min=margin if margin_min is None else min(margin_min,margin)
  t2_upper=up if t2_upper is None else max(t2_upper,up)
  t2_lower=low if t2_lower is None else min(t2_lower,low)
  if k%200==0:print('verified segment',k+1,'of',N,flush=True)
 assert t2_upper<0
 # Prior unique augmented fold source within distance 10^-24 of c; it lies
 # inside the central graph tube: the fold coordinate is in the two adjacent
 # s-intervals, and the first three x and t coordinates belong to both y-boxes.
 eps=Q(1,10**24)
 for k in (N//2-1,N//2):
  lo,hi,ym=segments[k]
  assert lo<=sc<=hi
  assert max(abs(ym[j]-c_y[j])+eps for j in range(4))<r
 # Since the chart E=(F_x[:,0:3],F_t) is nonsingular along the fold, the
 # exact PREFIX-361 det(F_x)=0 gives t'(s_fold)=0. With t''<0, the critical
 # point is the single strict maximum of this directly certified graph.
 assert c[4]-eps>T0
 # Endpoint value of t(s) is below T0, via independent point Banach tubes.
 for s,node in ((a,nodes[0]),(b,nodes[-1])):
  assert check(s,s,node,witness_radius,concave=False)[2]>0
  assert node[3]+witness_radius<T0
 # Now match at T0 to prior R0/R1 root witness cubes. The tiny strips near
 # old s coordinates each contain a T0-crossing by exact IVT signs. Their
 # full certified graph strips lie in the old fixed-parameter 10^-7 cubes.
 labels={}
 for label,old in OLDER364_TERMINAL.items():
  s_old=old[3];ds=Q(1,10**8)
  slo=s_old-ds;shi=s_old+ds
  assert a<slo<shi<b
  assert (shi<sc-eps) if label=='R0' else (slo>sc+eps)
  ystrip=proposal([*old[:3],T0],s_old,steps=4)
  K_,R_,margin_,_,_=check(slo,shi,ystrip,Q(4,10**8),concave=True)
  # Verify the small strip is within one of the 600 exact broad Banach
  # segments, hence shares its unique analytic graph root.
  matches=[(lo,hi,ym) for lo,hi,ym in segments if lo<=slo and shi<=hi]
  assert len(matches)==1, ('strip straddles segment boundary',label)
  mainlo,mainhi,mainy=matches[0]
  assert max(abs(ystrip[j]-mainy[j])+Q(4,10**8) for j in range(4))<r
  # Prior PREFIX364 t=T0 10^-7 node witness: the crossing is inside it.
  assert all(abs(ystrip[j]-old[j])+Q(4,10**8)<Q(1,10**7) for j in range(3))
  assert abs(s_old-old[3])+ds<Q(1,10**7)
  signed=[]
  for sv in (slo,shi):
   y=proposal(ystrip,sv,steps=3)
   check(sv,sv,y,Q(1,10**12),concave=False)
   if y[3]+Q(1,10**12)<T0:signed.append(-1)
   elif y[3]-Q(1,10**12)>T0:signed.append(1)
   else:raise AssertionError('endpoint t crossing not resolved')
   # This point root lies in the strip root box and is therefore on chart.
   assert max(abs(y[j]-ystrip[j])+Q(1,10**12) for j in range(4))<Q(4,10**8)
  assert signed==([-1,1] if label=='R0' else [1,-1])
  labels[label]={
   'prior_terminal_center':[str(v) for v in old],
   's_bracket':[str(slo),str(shi)],
   'crossing_t_signs':signed,
   'narrow_strip_radius':'1/25000000',
   'predecessor_witness_radius':'1/10000000',
  }
 # The same unique fold maximum lies between both sourced root labels.
 assert OLDER364_TERMINAL['R0'][3]<sc<OLDER364_TERMINAL['R1'][3]
 def rational_outer_ceil(v,scale):return (v*scale).numerator//(v*scale).denominator+1
 def rational_outer_floor(v,scale):return (v*scale).numerator//(v*scale).denominator
 res={
  'schema':'ENTERPRISE_MATH_PREFIX366_DIRECT_FOLD_SPLICE_V1',
  'status':'AUTHOR_SIDE_EXACT_RATIONAL / UNREVIEWED / NOT_ADMITTED',
  'global_knowledge_frozen':'9c220b4dc4c8c8be04bc9a47a19a536684597ef0',
  'enterprise_math_input_frozen':'0569b09ef35af9ed18e9c026bae6ddfa14fd643b',
  'source_dependencies':['PREFIX-361 original four-real-variable unique augmented fold in radius 10^-24','PREFIX-364 512-step continuation terminal R0/R1 at t=133/2000, both Banach 10^-7 node boxes'],
  'parameter_s':'Im(v), a *real-source coordinate*, NOT native heartbeat time',
  's_interval':[str(a),str(b)],
  'interval_segments':N,
  'uniform_parameter_root_boxes':N,
  'endpoint_witnesses':N+1,
  'root_tube_radius':str(r),
  'endpoint_witness_radius':str(witness_radius),
  'max_K_strict_lt':str(Q(rational_outer_ceil(k_max,10**6),10**6)),
  'min_selfmap_margin_strict_gt':str(Q(rational_outer_floor(margin_min,10**10),10**10)),
  'uniform_t_second_derivative_strict_upper_lt':str(Q(rational_outer_ceil(t2_upper,10**3),10**3)),
  'uniform_t_second_derivative_strict_lower_gt':str(Q(rational_outer_floor(t2_lower,10**3),10**3)),
  'critical_fold_s_radius_from_PREFIX361':'1/10^24',
  'fold_branch_side':'t < t_b',
  'source_splice': 'R0 is the negative-s branch, R1 the positive-s branch, of the same strict concave fold graph, directly proved without global discriminant uniqueness',
  'labels':labels,
  'verified':'All Banach, endpoint connection, strict second derivative, fold inclusion, IVT brackets, and historic labeled-cube containment use only exact fractions; no sampled-only proof.',
  'scope_boundary':'Static auxiliary 3-complex-source/5-Port model; NOT native P000 X6, typed BRC heartbeat, full 6D layer, or physical time',
  'next':'Independent H12/H3 exhaustive review and native-X6 typed observer bridge with explicit third slice coordinate and ordered path semantics.'
 }
 out=Path(__file__).with_name('RESULTS_PREFIX366.json');out.write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
 print('PASS_PREFIX366_DIRECT_R0_R1_SECOND_H12_FOLD_SPLICE')
 print('N',N,'K<',res['max_K_strict_lt'],'margin>',res['min_selfmap_margin_strict_gt'],'uniform t"<',res['uniform_t_second_derivative_strict_upper_lt'])
 print('two exact T0 source brackets',labels)

if __name__=='__main__': main()
