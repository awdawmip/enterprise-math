from math import prod
T=1<<96
def scale(x,a,b=1):return (x[0]*a//b,-(-x[1]*a//b))
def mul(x,y):return(x[0]*y[0],x[1]*y[1])
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def obs(q,d,exact):
    u=q+d;n=2*q+d;J=2*u*(2*u+1);L=4*n+2
    if exact:
        def pref(v):
            r=[(T,T)]
            for i in range(d):r.append(scale(r[-1],v-i,v+i+3))
            return r
        U,N=pref(u),pref(n);V=Q=A=(0,0)
        for k in range(d+1):
            l=d-k;a=scale(mul(U[k],N[l]),(k+1)*(l+1));b=scale(mul(U[k],N[l-1]),(k+1)*l) if l else (0,0)
            V=add(V,a);Q=add(Q,b);A=add(A,scale(add(a,b),(u-k)*(u+k+2),J))
        E=scale(U[d],T*q*(2*d+3)*(n+2),2*(2*u+1)*L);W=add(A,E);Z=add(scale(A,q),add(V,Q))
        P=scale(mul(W,Q),3*q*(4*q+3*d+1)**2);M=scale(mul(Z,Z),32*(3*q+d+1))
        return P[0]-M[1],P[1]-M[0]
    def pref(v):
        r=[1.]
        for i in range(d):r.append(r[-1]*(v-i)/(v+i+3))
        return r
    U,N=pref(u),pref(n);V=Q=A=0.
    for k in range(d+1):
        l=d-k;a=(k+1)*(l+1)*U[k]*N[l];b=(k+1)*l*U[k]*N[l-1] if l else 0.
        V+=a;Q+=b;A+=(u-k)*(u+k+2)*(a+b)/J
    E=U[d]*q*(2*d+3)*(n+2)/(2*(2*u+1)*L);Z=q*A+Q+V
    return 3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*Z*Z
for d in range(3101,3201):
    lo=4*d*d//5;hi=(4*d*d+2)//3
    while hi-lo>1:
        mid=(lo+hi)//2
        if obs(mid,d,False)>0:lo=mid
        else:hi=mid
    x=obs(lo,d,True);y=obs(hi,d,True)
    assert hi==lo+1 and lo>=64 and d*d<=4*lo and x[0]>0 and y[1]<0,(d,lo,hi,x,y)
    print(d,lo,hi,x[0],y[1])
print('PASS all 100 d=3101..3200 exact adjacent brackets')
