"""Exact D25 local-transport barrier certificate, Python 3 stdlib only."""
import json
def primes(n):
    s=bytearray(b'\x01')*(n+1);s[:2]=b'\x00\x00'
    for q in range(2,int(n**.5)+1):
        if s[q]:s[q*q::q]=b'\x00'*len(s[q*q::q])
    return [p for p in range(n+1) if s[p]]
def vf(n,p):
    a=0
    while n:n//=p;a+=n
    return a
def verify(p):
    assert p>3 and p%6==1
    m=(p-1)//6;mod=p**3;a=b=1
    for n in range(4*m+1):
        expected=0 if n<=2*m else 1 if n<=3*m else 2
        assert vf(2*n,p)+vf(3*n,p)-5*vf(n,p)==expected
        assert a%p**expected==0 and (a//p**expected)%p!=0
        if n>2*m:assert b==0
        if n==4*m:return (6*n+1)*a//p**2%p,4*m+1
        a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,mod)%mod
        b=-b*(3*n+1)**3*pow(27*(n+1)**3,-1,mod)%mod
def full(p):
    mod=p**3;W=V=0;a=b=1
    for n in range(p):
        W=(W+(6*n+1)*a)%mod;V=(V+(6*n+1)*b)%mod
        if n<p-1:
            a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,mod)%mod
            b=-b*(3*n+1)**3*pow(27*(n+1)**3,-1,mod)%mod
    return W,V
if __name__=='__main__':
    ps=primes(1999);case=[p for p in ps if p%6==1];assert len(case)==148
    witnesses={p:verify(p)[0] for p in case};checks=sum(verify(p)[1] for p in case)
    assert checks==91956 and witnesses[19]==13 and witnesses[373]==203
    target=sum(p%24 in (13,19) for p in case);assert target==77
    split={1:0,5:0}
    for p in ps:
        if p<=3:continue
        W,V=full(p)
        if p%6==1:assert W==V==p
        else:assert W==p**3-p and V==p**3-2*p
        split[p%6]+=1
    assert split=={1:148,5:153}
    print(json.dumps({'p1mod6':len(case),'target':target,'index_checks':checks,
        'p5mod6':split[5],'w4m_over_p2_modp':{19:witnesses[19],373:witnesses[373]},
        'failures':0},sort_keys=True))
