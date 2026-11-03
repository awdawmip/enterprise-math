from fractions import Fraction as Q
from itertools import product
A=(0,0,0,1,1,1);B=(2,2,3,2,2,4);C=(5,6,7,8,9,10)
M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
   (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
PAIRS=((3,31),(7,27),(11,23),(15,19))
BETAS=((Q(0),Q(0)),(Q(1,2),Q(1,3)),(Q(3,4),Q(4,5)))
def obs(z,m,b):
    v=tuple(b if m>>k&1 else z[k] for k in range(5))+z[5:]
    s=tuple((v[A[i]],(1-v[A[i]])*v[B[i]],
             (1-v[A[i]])*(1-v[B[i]])*v[C[i]],
             (1-v[A[i]])*(1-v[B[i]])*(1-v[C[i]])) for i in range(6))
    return tuple(tuple(sum((Q(M[j][i],20)*s[i][t] for i in range(6)),Q(0))
                       for t in range(4)) for j in range(6))
def ne(pair):return next(m for m in pair if not m&4),next(m for m in pair if m&4)
def red(z,pair,bn,be,j):
    n,e=ne(pair)
    return tuple(tuple(x for i,x in enumerate(obs(z,m,b)) if i!=j)
                 for m,b in ((n,bn),(e,be)))
def measurement(z,pair,bn,be,j):
    n,e=ne(pair)
    if j in (0,1,3,4):return (obs(z,e,be)[j][2],)
    g=3 if j==2 else 4
    if n>>g&1: nc=(e,be);c=(n,bn)
    else:nc=(n,bn);c=(e,be)
    return (obs(z,*nc)[j][1],obs(z,*c)[j][2])
def constant(pair,bn,be,j):
    if j in (0,1,3,4):return Q({0:11,1:10,3:Q(9,4),4:Q(5,4)}[j])/(1-be)**2
    n,e=ne(pair);g=3 if j==2 else 4
    nc,c=(be,bn) if n>>g&1 else (bn,be)
    return max(1/(1-nc),1/(1-c)**2)
def pair_states(j):
    z=[Q(1,2)]*11;w=z[:];h=Q(1,200)
    for k,v in {0:{5:11,6:-9},1:{5:-1,6:1},2:{3:1,7:1},
                3:{8:9,9:-1},4:{8:-1,9:1},5:{4:1,10:1}}[j].items():w[k]+=v*h
    return tuple(z),tuple(w)
def recover(z,pair,bn,be,j,r):
    if j in (0,1):
        a=(z[5]+z[6])/2;b=(9*z[5]+11*z[6])/20
        if j==0:a=r[0]/(1-be)**2
        else:b=r[0]/(1-be)**2
        return (11*a-10*b,-9*a+10*b)
    if j in (3,4):
        a=(z[8]+z[9])/2;b=(z[8]+9*z[9])/10
        if j==3:a=r[0]/(1-be)**2
        else:b=r[0]/(1-be)**2
        return (Q(9,4)*a-Q(5,4)*b,-a/4+Q(5,4)*b)
    n,e=ne(pair);g=3 if j==2 else 4
    nc,c=(be,bn) if n>>g&1 else (bn,be)
    return (r[0]/(1-nc),r[1]/(1-c)**2)
def check():
    count=0
    indices={0:(5,6),1:(5,6),2:(3,7),3:(8,9),4:(8,9),5:(4,10)}
    for pair,(bn,be),j in product(PAIRS,BETAS,range(6)):
        z,w=pair_states(j)
        assert red(z,pair,bn,be,j)==red(w,pair,bn,be,j)
        mz,mw=measurement(z,pair,bn,be,j),measurement(w,pair,bn,be,j)
        dz=max(abs(w[k]-z[k]) for k in range(2,11))
        dm=max(abs(x-y) for x,y in zip(mz,mw))
        assert dm>0 and dz<=constant(pair,bn,be,j)*dm
        assert recover(z,pair,bn,be,j,mw)==tuple(w[k] for k in indices[j])
        if j in (0,1,3,4):assert dz==constant(pair,bn,be,j)*dm
        for mask,beta in product(range(32),(Q(0),Q(1,3),Q(1))):
            x,y=obs(z,mask,beta),obs(w,mask,beta)
            assert all(x[i]==y[i] for i in range(6) if i!=j)
            count+=1
    print('schemes=4 beta_pairs=3 deleted_labels=6')
    print('exact_fiber_recoveries=72 universal_upstream_mask_checks='+str(count))
    print('PASS_BRC_S23_MINIMAL_SCALAR_SOURCE_REPAIR_20261103')
if __name__=='__main__':check()
