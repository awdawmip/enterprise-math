# Exact independent checker for PREFIX-956, Python 3 standard library.
def formula(x,d,p):
    if d == 0: return p-(x&((1<<p)-1)).bit_count()
    z=abs(d); u=(z&-z).bit_length()-1; q=z>>u
    is_mersenne=(q&(q+1))==0
    if d<0:
        j=u+q.bit_length()
        return int(is_mersenne and j<p and not ((x>>j)&1))
    n=0
    if is_mersenne and u+q.bit_length()<p and not ((x>>u)&1): n+=1
    if z.bit_count()==1:
        h=z.bit_length()-1
        if 1<=h<=p and ((x>>(h-1))&1): n+=1
    elif z.bit_count()==2:
        v=(z^(1<<u)).bit_length()-1
        if v<p: n+=((x>>u)&1)+((x>>v)&1)
    return n

def direct(x,d,p):
    return sum((x^(1<<j))-(1<<i)==x-d for i in range(p) for j in range(p))

def verify():
    for p in range(3,10):
        H=1<<(p-1); c=[0,0,0]; o=[0,0,0]
        for x in range(1<<p):
            for d in range(1-H,2*H+1):
                n=formula(x,d,p)
                assert n==direct(x,d,p), (p,x,d,n)
                if d:
                    assert 0<=n<=2
                    c[n]+=1
                    if x&1:o[n]+=1
        assert c[1]==2**(p-2)*(3*p*p-5*p+8)
        assert c[2]==2**(p-3)*(p*p+3*p-8)
        assert o[1]==2**(p-3)*(3*p*p-7*p+12)
        assert o[2]==2**(p-3)*(p*p+5*p-10)//2
        print(p,sum(c)+(1<<p),c,o)
    assert formula(13,2,4)==direct(13,2,4)==2
if __name__=='__main__': verify()
