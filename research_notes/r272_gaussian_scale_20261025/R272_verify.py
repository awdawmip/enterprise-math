"""R272 independent exact verification: raw BRC dynamic programming vs rational moments.
Stdlib only; author-side finite checks, not a native Enterprise Math integration.
"""
from collections import defaultdict
import json

TRANS={
    (0,0):(2,-1,-1),(0,1):(2,1,-1),
    (1,0):(0,-1,-1),(1,1):(0,1,-1),
    (2,0):(1,1,1),(2,1):(2,1,-1),
}

def step(state,bit):
    q,r,e,k=state
    q1,eta,b=TRANS[(q,bit)]
    r1=2 if (r==2 or (r==1 and bit==0)) else (1 if bit==0 else 0)
    return (q1,r1,eta*e,eta*k+b)

def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c

def power(a,k):
    t=[1]
    for _ in range(k):t=multiply(t,a)
    return t

def rationalseq(numer,denom,N):
    assert denom[0]==1
    out=[]
    for n in range(N+1):
        x=numer[n] if n<len(numer) else 0
        for k in range(1,min(n,len(denom)-1)+1):
            x-=denom[k]*out[n-k]
        out.append(x)
    return out

def rational_moments(N):
    zz=[0,1]
    one_minus_z=[1,-1]
    one_plus_z2=[1,0,1]
    f=[1,-1,-1]
    g=[1,1,1]
    a_den=multiply(f,one_plus_z2)
    s_den=multiply(power(one_minus_z,2),multiply(one_plus_z2,multiply(f,g)))
    t_den=multiply(one_minus_z,multiply(one_plus_z2,multiply(power(f,2),g)))
    numer_a=[1,-1]
    numer_s=[0,0,0,-1,-2,1]
    numer_t=[0,0,0,1,6,2,-1]
    return tuple(rationalseq(n,d,N) for n,d in ((numer_a,a_den),(numer_s,s_den),(numer_t,t_den)))

def exact_dp(N):
    D={(0,0,1,0):1}
    moments=[]
    check={}
    for n in range(N+1):
        terms=[(e,k,v) for (q,r,e,k),v in D.items() if (q,r)==(0,0)]
        moments.append((sum(v for e,k,v in terms),sum(k*v for e,k,v in terms),sum(k*k*v for e,k,v in terms)))
        if n in (7,30):
            if n==7:
                channels=((0,0),(0,1),(1,0),(1,1),(2,0),(2,1))
                def channel(q,r):return (q,int(r==2))
                check['seven_channel_vector']=[sum(v for (q,r,e,k),v in D.items() if channel(q,r)==c and (e,k)==(1,-3)) for c in channels]
            if n==30:check['r270_reference_coefficient']=sum(v for (q,r,e,k),v in D.items() if (q,r,e,k)==(0,0,1,-4))
        assert sum(D.values())==2**n

        if n<N:
            nd=defaultdict(int)
            for state,v in D.items():
                for bit in (0,1):nd[step(state,bit)]+=v
            D=nd
    return moments,check

def exhaustive(upto):
    D={(0,0,1,0):1}
    total=0
    for n in range(upto+1):
        words=defaultdict(int)
        for word in range(1<<n):
            state=(0,0,1,0)
            for i in range(n-1,-1,-1):state=step(state,(word>>i)&1)
            words[state]+=1
            total+=1
        assert dict(D)==dict(words),(n,D,words)
        nd=defaultdict(int)
        for state,w in D.items():
            for bit in (0,1):nd[step(state,bit)]+=w
        D=nd
    return total

def main():
    N=100
    dp,check=exact_dp(N)
    rr=rational_moments(N)
    for n in range(N+1):
        assert dp[n]==(rr[0][n],rr[1][n],rr[2][n]),(n,dp[n],tuple(x[n] for x in rr))
    assert check['seven_channel_vector']==[2,2,3,1,1,9]
    assert check['r270_reference_coefficient']==16482
    raw=exhaustive(11)
    res={
       'status':'PASS', 'model':'FORMAL_POSITIVE_AFFINE_BRC_NOT_NATIVE_X6',
       'dp_depths':'0..100', 'rational_coefficient_depths':'0..100',
       'raw_word_depths':'0..11','raw_word_count':raw,
       'checks':check,
       'moments':{str(n):{'reset_count':str(dp[n][0]),'translation_sum':str(dp[n][1]),'translation_squared_sum':str(dp[n][2])} for n in (3,7,10,30,60,80,100)},
       'mathematical_status':'AUTHOR_SIDE_PROOF; FINITE_CHECKS_NOT_UNIVERSAL_PROOF',
       'native_status':'CONTROL_QUOTA; OWNER_NOT_VERIFIED; NOT_FORMALLY_ACCEPTED'
    }
    print(json.dumps(res,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
