#!/usr/bin/env python3
"""Exploratory compensation comparison; IEEE doubles, not interval evidence."""
from array import array
from math import isqrt,log,fsum,sqrt
from pathlib import Path
import argparse,json


def pav(A,L,R):
    pools=[]
    for n in range(L,R):
        w=1/(n*(n+1))
        pools.append([n,n+1,w,w*A[n]])
        while len(pools)>1 and pools[-2][3]/pools[-2][2]>pools[-1][3]/pools[-1][2]:
            u,v=pools[-2:]
            pools[-2:]=[[u[0],v[1],u[2]+v[2],u[3]+v[3]]]
    return pools


def delta(n):
    # Integral expansion sum (-1)^j/((j+1)(j+2)n^j), at n>=1024 here.
    return fsum((-1)**j/((j+1)*(j+2)*n**j) for j in range(8))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-power',type=int,default=20)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('native_compensation_exploration.json'))
    args=parser.parse_args(); B=2**args.max_power
    sieve=bytearray(b'\x01')*(B+1);sieve[:2]=b'\0\0'
    for p in range(2,isqrt(B)+1):
        if sieve[p]:sieve[p*p::p]=b'\0'*((B-p*p)//p+1)
    prime_logs=array('d',[0.0])*(B+1)
    pp_logs=array('d',[0.0])*(B+1)
    primes=[]
    for p in range(2,B+1):
        if not sieve[p]:continue
        primes.append(p); lp=log(p);prime_logs[p]=lp
        q=p*p
        while q<=B:pp_logs[q]=lp;q*=p
    theta=array('d',[0.0])*(B+1);psi=array('d',[0.0])*(B+1);native=array('d',[0.0])*(B+1)
    s0=s1=c0=c1=0.0
    for n in range(1,B+1):
        y=prime_logs[n]-c0;t=s0+y;c0=(t-s0)-y;s0=t
        y=prime_logs[n]+pp_logs[n]-c1;t=s1+y;c1=(t-s1)-y;s1=t
        theta[n]=s0-n;psi[n]=s1-n
        if n>=1024:native[n]=psi[n]-delta(n)
    packets=[]
    for j in range(10,args.max_power):
        L=2**j;packets.append(('midpoint',L,3*L//2,2*L))
    for j in range(9,args.max_power):
        L,x,R=3*2**j,4*2**j,6*2**j
        if R<=B:packets.append(('seam',L,x,R))
    rows=[]
    for kind,L,x,R in packets:
        a,b,h=x-L,R-x,R-L; factor=h**1.5/L
        row={'kind':kind,'L':L,'x':x,'R':R,'fields':{}}
        for label,A in [('theta',theta),('psi',psi),('native',native)]:
            pools=pav(A,L,R)
            crossing=next((p for p in pools if p[0]<x<p[1]),None)
            if crossing:
                u,v,w,s=crossing;mean=s/w
                S=fsum((A[n]-mean)/(n*(n+1)) for n in range(u,x))
                residual=h*x*S/(a*b)
            else:u=v=x;residual=0.0
            mean_left=fsum(A[n]/(n*(n+1)) for n in range(L,x))/(1/L-1/x)
            mean_right=fsum(A[n]/(n*(n+1)) for n in range(x,R))/(1/x-1/R)
            contrast=(mean_left-mean_right)/x
            row['fields'][label]={'pool_count':len(pools),'crossing_pool':[u,v],'G_over_H':(v-u)/h,
                'residual_root':residual*factor,'true_positive_root':max(contrast,0)*factor,
                'signed_contrast_root':contrast*factor}
        row['Q_root']=row['fields']['theta']['signed_contrast_root']-row['fields']['psi']['signed_contrast_root']
        row['K_root']=row['fields']['native']['signed_contrast_root']-row['fields']['psi']['signed_contrast_root']
        rows.append(row)
    result={'schema':'RH_NATIVE_COMPENSATION_EXPLORATION_V1','status':'EXPLORATORY_DOUBLE_PRECISION','certified':False,
        'sieve_limit':B,'prime_count':len(primes),'packets':len(packets),'fields':['theta(n)-n','psi(n)-n','psi(n)-n-delta(n)'],
        'delta_definition':'delta(n)=n(n+1)log(1+1/n)-n; evaluated by eight terms at n>=1024',
        'rows':rows}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'packets':len(rows),'last_rows':rows[-5:]},ensure_ascii=False))


if __name__=='__main__':main()
