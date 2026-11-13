#!/usr/bin/env python3
"""R32 fully self-contained exact S23/AV Stern-Brocot block compiler.
Produces the complete 298-row trillion-horizon risk table without event rows.
"""
import csv, hashlib, io
from pathlib import Path

D=10**24
LO=262204504569236716045286
HI=262204504569236716045287
M=128
N=10**12+M

def val(ab,T):return ab[0]*D+ab[1]*T

def risk(n):
    all_max=[]
    for T in (LO,HI):
        z=sorted(range(n),key=lambda t:t*T%D)
        h=[k for k,t in enumerate(z) if t<M]
        mx=[]
        for i,p in enumerate(h):
            e=h[(i+1)%M]
            if e<=p:e+=n
            gaps=[]
            for k in range(p,e):
                a,b=z[k%n],z[(k+1)%n]
                gaps.append((a*T//D-b*T//D+int(b*T%D<a*T%D),b-a))
            mx.append(max(gaps,key=lambda ab:val(ab,T)))
        all_max.append(mx)
    assert all_max[0]==all_max[1]
    return (1-sum(a for a,b in all_max[0]),-sum(b for a,b in all_max[0]))

def below(p,q):
    if p*D<q*LO:return True
    if p*D>q*HI:return False
    raise ArithmeticError('Farey mediant crosses frozen theta interval')

def stages():
    a,q,c,j=0,1,1,1
    while q+j<=M:
        if below(a+c,q+j):a,q=a+c,q+j
        else:c,j=a+c,q+j
    assert (a,q,c,j)==(27,103,16,61)
    n0=M
    while n0<=N:
        n1=min(q+j,N)
        assert c*q-a*j==1 and a*D<q*LO and c*D>j*HI
        yield n0,n1,a,q,c,j
        if n1==N:break
        if below(a+c,q+j):a,q=a+c,q+j
        else:c,j=a+c,q+j
        n0=n1+1

def push(s,l,r,amp):
    if l>r:return
    if s and s[-1][1]+1==l and s[-1][2]==amp:s[-1]=(s[-1][0],r,amp)
    else:s.append((l,r,amp))

def compile_runs():
    ss=list(stages())
    assert len(ss)==78
    seg=[];last=risk(M)
    assert last==(0,0)
    for n in range(M+1,390):
        now=risk(n)
        push(seg,n,n,(now[0]-last[0],now[1]-last[1]))
        last=now
    event_blocks=0;event_stages=0
    for n0,n1,a,q,c,j in ss[3:]:
        assert n0==seg[-1][1]+1 and q>=164 and j>=292
        assert 0<c*D-j*HI and c*D-j*LO<59*D-225*HI
        t=q+j
        blocks=[]
        for x,y in ((t-163,t-97),(t-60,t)):
            x=max(x,n0);y=min(y,n1)
            if x<=y:blocks.append((x,y))
        if blocks:
            event_stages+=1
            event_blocks+=len(blocks)
            if q*HI-a*D<c*D-j*HI:amp=(-a,q)
            elif c*D-j*LO<q*LO-a*D:amp=(c,-j)
            else:raise ArithmeticError('ambiguous event amplitude')
        else:amp=(0,0)
        p=n0
        for x,y in blocks:
            push(seg,p,x-1,(0,0));push(seg,x,y,amp);p=y+1
        push(seg,p,n1,(0,0))
    assert (event_stages,event_blocks)==(74,148)
    A=B=0;out=[]
    for l,r,(dA,dB) in seg:
        out.append((l-1,r,A,B,dA,dB))
        A+=(r-l+1)*dA;B+=(r-l+1)*dB
    assert len(out)==298 and (A,B)==(-4017401528447,15321634290944)
    f=io.StringIO(newline='');w=csv.writer(f,delimiter='\t',lineterminator='\n')
    w.writerow(('n0','n1','A0','B0','dA','dB'));w.writerows(out)
    data=f.getvalue().encode()
    digest=hashlib.sha256(data).hexdigest()
    assert digest=='2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6'
    Path('AFFINE_RUNS_R32.tsv').write_bytes(data)
    print('PASS_R32',len(ss),'Farey stages',event_blocks,'bulk blocks',len(out),'maximal runs')
    print('trillion-horizon risk:',A,B,'SHA256:',digest)

if __name__=='__main__':compile_runs()
