#!/usr/bin/env python3
"""Independent 428-prime exact B2 source witness. Universal result is literature-derived."""
def primes(n):
    ok=bytearray(b'\x01')*(n+1);ok[0:2]=b'\x00\x00'
    for q in range(2,int(n**0.5)+1):
        if ok[q]:ok[q*q::q]=b'\x00'*(((n-q*q)//q)+1)
    return [p for p in range(5,n+1) if ok[p]]
def witness(p):
    f=[1]*(4*p);v=[0]*(4*p)
    for n in range(1,4*p):
        z=n;c=0
        while z%p==0:z//=p;c+=1
        v[n]=v[n-1]+c
        f[n]=f[n-1]*z%p
    H=(p-1)//2;E=(3*p-1)//4;out=0
    for b in range(H+1,E+1):
        assert v[4*b]-4*v[b]==2
        u=f[4*b]*pow(f[b],-4,p)*pow(2304,-b,p)%p
        out=(out+(8*b+1)*u)%p
    return out
if __name__=='__main__':
    ps=primes(3000);bad=[p for p in ps if witness(p)!=0]
    print({'tested':len(ps),'nonzero_B2':bad,'classes':{c:sum(p%24==c for p in ps) for c in (1,5,7,11,13,17,19,23)}})
    assert not bad
