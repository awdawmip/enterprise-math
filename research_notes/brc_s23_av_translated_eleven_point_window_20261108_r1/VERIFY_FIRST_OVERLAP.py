from fractions import Fraction as F

def add(a,b):return (a[0]+b[0],a[1]+b[1])
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def mul(n,a):return (n*a[0],n*a[1])
def norm(p):return sum(p)
def ins(p,n):return min(p)>=0 and norm(p)<=n
def tri(n):return ((i,s-i) for s in range(n+1) for i in range(s+1))
def T(n):return (n+1)*(n+2)//2 if n>=0 else 0

def run(u,w,r):
  d=norm(u);M=norm(w)
  assert M>3*d and u[0]*w[1]-u[1]*w[0]==1
  e=u[0]*r-u[1];eta=w[1]-w[0]*r
  assert F(3,2)*eta<e<2*eta
  q2=add(u,mul(2,w));q3=add(u,mul(3,w));q4=add(u,mul(4,w))
  H3=2*norm(q2);H=H3+d;a=d;z=d+a;t=M+z;s=2*M+z
  old16=[mul(2,w),w,(0,0),q4,q3,q2,add(u,w),u,mul(2,q2),add(mul(2,u),mul(3,w)),add(mul(2,u),mul(2,w)),add(mul(2,u),w),mul(2,u),add(mul(3,u),mul(4,w)),add(mul(3,u),mul(3,w)),add(mul(3,u),mul(2,w))]
  true16=sorted(old16,key=lambda p:r*p[0]-p[1]); assert len(set(old16))==16
  blocks=[]
  blocks.append(('16',old16,true16))
  for x in tri(a):
    if ins(x,a-d) or ins(sub(x,u),a-d):continue
    old=[mul(2,w),w,(0,0),q4,q3,q2,add(u,w),u,mul(2,q2),add(mul(2,u),mul(3,w)),add(mul(2,u),mul(2,w))]
    new=sorted(old,key=lambda p:r*p[0]-p[1]); blocks.append(('11',[add(x,v) for v in old],[add(x,v) for v in new]))
  for x in tri(z):
    if ins(x,a) or ins(sub(x,u),a):continue
    old=[mul(2,w),w,(0,0),q4,q3,q2]
    new=[q4,mul(2,w),q3,w,q2,(0,0)]
    blocks.append(('6',[add(x,v) for v in old],[add(x,v) for v in new]))
  for x in tri(t):
    if ins(x,z) or ins(sub(x,w),z):continue
    old=[w,(0,0),q3,q2];new=[q3,w,q2,(0,0)]
    blocks.append(('4',[add(x,v) for v in old],[add(x,v) for v in new]))
  for x in tri(s):
    if ins(x,t) or ins(sub(x,w),t):continue
    blocks.append(('2',[x,add(x,q2)],[add(x,q2),x]))
  pts=[(v,j) for v in range(H+1) for j in range(H-v+1)]
  lex=sorted(pts,key=lambda p:(w[1]*p[0]-w[0]*p[1],-p[0]))
  true=sorted(pts,key=lambda p:r*p[0]-p[1]);pos={p:i for i,p in enumerate(lex)}
  counts={'16':0,'11':0,'6':0,'4':0,'2':0}; seen=set();map_={}
  for name,old,new in blocks:
    idx=[pos[p] for p in old]
    assert idx==list(range(idx[0],idx[0]+len(old))), (name,old,idx)
    assert set(old)==set(new)
    assert not (seen&set(old)),name
    seen.update(old);map_.update(zip(old,new));counts[name]+=1
  assert [map_.get(p,p) for p in lex]==true
  assert counts=={'16':1,'11':T(d)-2,'6':T(2*d)-2*T(d)+1,'4':T(M+2*d)-2*T(2*d),'2':M*M},counts
  print('PASS_FIRST_OVERLAP',u,w,'H',H,'POINTS',len(pts),'BLOCKS',counts)
  print('OLD_16',old16)
  print('TRUE_16',true16)

run((1,1),(5,6),F(46,39))
run((2,1),(7,4),F(78,139))

# Rigorous actual logarithmic ratio enclosure and exact integer endpoint counts.
def log_box(x):
    p=2*sum((x**(2*i+1)/(2*i+1) for i in range(45)),F(0))
    return p,p+2*x**91/(91*(1-x*x))
a,b=log_box(F(1,3));c,d_=log_box(F(1,15));e,f=log_box(F(3,17))
lo,hi=(3*a-d_)/f,(3*b-c)/e
assert F(545569623581288298975349314,10**26)<lo<hi<F(545569623581288298975349315,10**26)
u=(79,431);w=(380295,2074774);M=norm(w);d=norm(u)
H3=2*norm(add(u,mul(2,w)));H=H3+d
assert H==9821806
for r in (lo,hi):
    eps=r*u[0]-u[1];eta=w[1]-w[0]*r
    assert F(3,2)*eta<eps<2*eta
assert M>3*d
n16=1;n11=T(d)-2;n6=T(2*d)-2*T(d)+1;n4=T(M+2*d)-2*T(2*d);n2=M*M
assert (n11,n6,n4,n2)==(130814,260100,3016189228633,6027363794761)
assert 20*n16+13*n11+6*n6+3*n4+n2==T(2*M+2*d)+T(M+2*d)+T(2*d)+T(d)==15075934741862
print('PASS_ACTUAL_H9821806_BLOCK_COUNTS',n16,n11,n6,n4,n2,'INVERSIONS',15075934741862)
print('PASS_S23_AV_FIRST_OVERLAP_SIXTEEN_POINT_H9821806')
