"""PREFIX-953: exact low-bit correlation; independent direct comparisons."""
import json

def fs(n,m,a,b):
    z=0
    while True:
        z+=(n*(n-1)//2)*(a//m)+n*(b//m)
        a%=m; b%=m
        y=a*n+b
        if y<m: return z
        n,b,m,a=y//m,y%m,a,m

def formula(p,k,l):
    N=1<<(p-2); J=p-2
    same=[]
    for j in range(1,J+1):
        m=1<<(j+1); q=(l*pow(k,-1,m))%m; h=1<<(j-1)
        c=h-fs(h,1<<j,2*q,q)+2*fs(h,m,2*q,q)
        same.append(c*(N//(1<<j)))
    return N*J*(J-1)//4+sum(same),same

def direct(p,k,l):
    H=1<<(p-1); low=lt=tl=tt=zprod=wprod=0
    mask=H-2
    for a in range(H+1,2*H,2):
        x=k*a;y=l*a
        lk=p-2-(x&mask).bit_count(); ll=p-2-(y&mask).bit_count()
        tk=1-((x>>(p-1))&1); tll=1-((y>>(p-1))&1)
        low+=lk*ll;lt+=lk*tll;tl+=tk*ll;tt+=tk*tll
        zprod+=(lk+tk)*(ll+tll)
        wprod+=(lk+tk+2*(a==H+1 and k>=3))*(ll+tll+2*(a==H+1 and l>=3))
    return [low,lt,tl,tt,zprod,wprod]

if __name__=='__main__':
    count=0
    for p in range(4,9):
        for k in range(1,1<<(p-1),2):
            for l in range(1,1<<(p-1),2):
                assert formula(p,k,l)[0]==direct(p,k,l)[0]
                count+=1
    q19=direct(19,21,23)
    assert q19==[9448558,532848,530485,29848,10541739,10541801]
    assert formula(19,21,23)[0]==q19[0]
    assert formula(19,23,21)[0]==q19[0]
    print(json.dumps({'small_width_ordered_core_pairs':count,'Q19_k21_k23':q19,
                      'same_bit_buckets':formula(19,21,23)[1]},sort_keys=True))
