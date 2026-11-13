from fractions import Fraction as F

def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[0],x[1]-y[1]
def mul(k,x):return k*x[0],k*x[1]
def n(x):return x[0]+x[1]
def S(h):return ((i,s-i) for s in range(h+1) for i in range(s+1))
def ins(p,h):return min(p)>=0 and n(p)<=h
def T(h):return (h+1)*(h+2)//2 if h>=0 else 0

old16coef=[(0,2),(0,1),(0,0),(1,4),(1,3),(1,2),(1,1),(1,0),
           (2,4),(2,3),(2,2),(2,1),(2,0),(3,4),(3,3),(3,2)]
new16idx=[3,0,4,1,8,5,2,9,6,13,10,7,14,11,15,12]
for alpha in (F(150001,100000),F(17,10),F(199999,100000)):
    assert [old16coef.index(z) for z in sorted(old16coef,key=lambda y:alpha*y[0]-y[1])]==new16idx

def run(u,w,r):
    d=n(u);M=n(w);assert d*3<M and u[0]*w[1]-u[1]*w[0]==1
    epsilon=r*u[0]-u[1];eta=w[1]-r*w[0];assert F(3,2)*eta<epsilon<2*eta
    q2=add(u,mul(2,w));q3=add(u,mul(3,w));q4=add(u,mul(4,w))
    h3=2*n(q2)
    v16=[add(mul(A,u),mul(B,w)) for A,B in old16coef]
    p16=[v16[i] for i in new16idx]
    base11=[mul(2,w),w,(0,0),q4,q3,q2,add(u,w),u,mul(2,q2),add(mul(2,u),mul(3,w)),add(mul(2,u),mul(2,w))]
    bnew11=[base11[i] for i in [3,0,4,1,8,5,2,9,6,10,7]]
    base6=[mul(2,w),w,(0,0),q4,q3,q2]
    bnew6=[base6[i] for i in [3,0,4,1,5,2]]
    base4=[w,(0,0),q3,q2];bnew4=[q3,w,q2,(0,0)]
    for a in range(d,2*d):
        H=h3+a;z=d+a;t=M+z;s=2*M+z
        blocks=[]
        for x in S(a-d): blocks.append(('16',[add(x,p) for p in v16],[add(x,p) for p in p16]))
        for x in S(a):
            if ins(x,a-d) or ins(sub(x,u),a-d):continue
            blocks.append(('11',[add(x,p) for p in base11],[add(x,p) for p in bnew11]))
        for x in S(z):
            if ins(x,a) or ins(sub(x,u),a):continue
            blocks.append(('6',[add(x,p) for p in base6],[add(x,p) for p in bnew6]))
        for x in S(t):
            if ins(x,z) or ins(sub(x,w),z):continue
            blocks.append(('4',[add(x,p) for p in base4],[add(x,p) for p in bnew4]))
        for x in S(s):
            if ins(x,t) or ins(sub(x,w),t):continue
            blocks.append(('2',[x,add(x,q2)],[add(x,q2),x]))
        pts=list(S(H));old=sorted(pts,key=lambda p:(w[1]*p[0]-w[0]*p[1],-p[0]))
        true=sorted(pts,key=lambda p:r*p[0]-p[1]);where={p:i for i,p in enumerate(old)}
        cnt={'16':0,'11':0,'6':0,'4':0,'2':0};seen=set();mapping={}
        for k,blk,out in blocks:
            ix=[where[p] for p in blk]
            assert ix==list(range(ix[0],ix[0]+len(ix))), (a,k,ix)
            assert set(blk)==set(out)
            assert not seen.intersection(blk),(a,k)
            seen.update(blk);mapping.update(zip(blk,out));cnt[k]+=1
        assert [mapping.get(p,p) for p in old]==true
        expected={'16':T(a-d),'11':T(a)-2*T(a-d),'6':T(z)-2*T(a)+T(a-d),
                  '4':T(M+z)-2*T(z),'2':M*M}
        assert cnt==expected,(cnt,expected)
        inverted=20*cnt['16']+13*cnt['11']+6*cnt['6']+3*cnt['4']+cnt['2']
        assert inverted==T(s)+T(t)+T(z)+T(a)
        print('PASS_SCALED_SIXTEEN_WINDOW',u,w,'H',H,'POINTS',len(pts),'COUNTS',cnt,'INV',inverted)

run((1,1),(5,6),F(46,39))
run((2,1),(7,4),F(78,139))

# Exact actual unbounded-horizon theorem endpoint arithmetic, with rational r interval.
def log_box(x):
    v=2*sum((x**(2*i+1)/(2*i+1) for i in range(45)),F(0))
    return v,v+2*x**91/(91*(1-x*x))
a,b=log_box(F(1,3));c,d=log_box(F(1,15));e,f=log_box(F(3,17))
lo,hi=(3*a-d)/f,(3*b-c)/e
assert F(545569623581288298975349314,10**26)<lo<hi<F(545569623581288298975349315,10**26)
u=(79,431);w=(380295,2074774);d=n(u);M=n(w);h3=2*n(add(u,mul(2,w)))
assert (d,M,h3)==(510,2455069,9821296)
for r in (lo,hi):
    e=r*u[0]-u[1];eta=w[1]-r*w[0]
    assert F(3,2)*eta<e<2*eta
for a in (d,d+1,2*d-1):
    z=d+a;t=M+z;s=2*M+z
    c16=T(a-d);c11=T(a)-2*T(a-d);c6=T(z)-2*T(a)+T(a-d)
    c4=T(t)-2*T(z);c2=M*M
    assert min(c16,c11,c6,c4,c2)>=0
    assert 20*c16+13*c11+6*c6+3*c4+c2==T(s)+T(t)+T(z)+T(a)
    print('PASS_ACTUAL_SIXTEEN_WINDOW','H',h3+a,'SIXTEEN',c16,'ELEVEN',c11,'SIX',c6,'FOUR',c4,'PAIR',c2,'INV',T(s)+T(t)+T(z)+T(a))
print('PASS_S23_AV_TRANSLATED_SIXTEEN_POINT_WINDOW_H9821806_TO_H9822315')
