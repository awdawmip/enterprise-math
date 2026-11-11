#!/usr/bin/env python3
"""Exact R69 auxiliary-source interval certification and benchmark; stdlib only."""
from fractions import Fraction as F
from collections import OrderedDict
from time import perf_counter_ns
from json import dumps
import argparse

P,Q=27413,65521
ANCHOR=F(P,Q)

def boundaries(m):
    bs=sorted(range(m),key=lambda a:(a*P)%Q)
    return [(bs[i],bs[i+1]) for i in range(m-1)]

def choose_arc(m):
    z=[(((b*P)%Q-(a*P)%Q),a,b) for a,b in boundaries(m)]
    return min((gap,a,b) for gap,a,b in z if gap>0)[1:]

def preconditions(t,a,b,L,U):
    ul,vl=L.numerator,L.denominator
    uu,vu=U.numerator,U.denominator
    return all((c*ul)//vl==(c*uu)//vu for c in (t,a,b)) and all(
        (a*u)%v < (b*u)%v for u,v in ((ul,vl),(uu,vu)))

def kernel_integer(t,a,b,L,U):
    """Sound I/O/? classifier on a closed rational interval."""
    ul,vl=L.numerator,L.denominator
    uu,vu=U.numerator,U.denominator
    for c in (t,a,b):
        if (c*ul)//vl != (c*uu)//vu: return '?'
    x=[]
    for u,v in ((ul,vl),(uu,vu)):
        rt,ra,rb=(t*u)%v,(a*u)%v,(b*u)%v
        if ra>=rb: return '?'
        x.append((rt,ra,rb))
    if all(rt>=ra and rt<rb for rt,ra,rb in x): return 'I'
    if all(rt<ra for rt,ra,rb in x) or all(rt>=rb for rt,ra,rb in x): return 'O'
    return '?'

def kernel_fraction(t,a,b,L,U):
    vals=[]
    for th in (L,U):
        xt,xa,xb=t*th,a*th,b*th
        kt,ka,kb=(v.numerator//v.denominator for v in (xt,xa,xb))
        vals.append((kt,ka,kb,xt-kt,xa-ka,xb-kb))
    if vals[0][:3]!=vals[1][:3]: return '?'
    if any(ra>=rb for _,_,_,rt,ra,rb in vals): return '?'
    if all(rt>=ra and rt<rb for _,_,_,rt,ra,rb in vals): return 'I'
    if all(rt<ra for _,_,_,rt,ra,rb in vals) or all(rt>=rb for _,_,_,rt,ra,rb in vals): return 'O'
    return '?'

def direct(t,a,b,th):
    rt,ra,rb=(t*th)%1,(a*th)%1,(b*th)%1
    assert ra<rb
    return ra<=rt<rb

def admissible_times(n,a,b,offset):
    out=[];t=offset+2
    while len(out)<n:
        if t%Q not in (0,a%Q,b%Q): out.append(t)
        t+=1
    return out

class Cache(OrderedDict):
    def __init__(self,limit):
        super().__init__();self.limit=limit

def query(times,a,b,L,U,kernel,cache=None):
    win=next((t for t in reversed(times) if direct(t,a,b,ANCHOR)),None)
    relevant=[t for t in reversed(times) if win is None or t>=win]
    checks=hits=unknown=0
    for t in relevant:
        expected='I' if t==win else 'O'
        hit=False
        if cache is not None and t in cache:
            cL,cU,old=cache[t]
            if cL<=L and U<=cU and old==expected:
                hits+=1;hit=True
                cache.move_to_end(t)
        if not hit:
            checks+=1
            result=kernel(t,a,b,L,U)
            if result!=expected: unknown+=1
            elif cache is not None:
                cache[t]=(L,U,result)
                cache.move_to_end(t)
                if cache.limit is not None and len(cache)>cache.limit:
                    cache.popitem(last=False)
    return unknown==0,win,len(relevant),checks,hits,unknown

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',default='')
    ns=ap.parse_args()
    rows=[]
    for m in (8,32,128):
        a,b=choose_arc(m)
        for n in (16,64,256,1024):
            for offset in (0,10**18):
                times=admissible_times(n,a,b,offset)
                D=max(80,max(times).bit_length()+40)
                base=F(1,2**D)
                for reuse in (1,4,16,64):
                    intervals=[(ANCHOR-base/(1+i%4),ANCHOR+base/(1+i%4)) for i in range(reuse)]
                    assert preconditions(times[-1],a,b,*intervals[0])
                    v={}
                    for alg in ('fraction','integer','cache64','cache8'):
                        kernel=kernel_fraction if alg=='fraction' else kernel_integer
                        cache=Cache(64 if alg=='cache64' else 8) if alg.startswith('cache') else None
                        elapsed=0; checks=hits=0
                        for L,U in intervals:
                            tic=perf_counter_ns()
                            valid,win,scope,cts,h,unknown=query(times,a,b,L,U,kernel,cache)
                            elapsed+=perf_counter_ns()-tic
                            assert valid,(m,n,offset,reuse,alg,unknown,win)
                            assert win is None or direct(win,a,b,ANCHOR)
                            checks+=cts;hits+=h
                            for test in (L,(3*L+U)/4,(L+U)/2,(L+3*U)/4,U):
                                oracle=next((t for t in reversed(times) if direct(t,a,b,test)),None)
                                assert oracle==win,(m,n,offset,reuse,alg,test,oracle,win)
                        v[alg]={'checks':checks,'hits':hits,'elapsed_ns':elapsed,
                                'cache_entries':len(cache) if cache is not None else 0,
                                'scope':scope,'winner':win}
                    assert v['fraction']['checks']==v['integer']['checks']
                    assert v['integer']['checks']==v['cache64']['checks']+v['cache64']['hits']
                    rows.append({'m':m,'n':n,'offset':offset,'query_count':reuse,
                                 'theta_q_bits':Q.bit_length(),
                                 'endpoint_denominator_bits':intervals[0][0].denominator.bit_length(),
                                 'result':v})
    by_n=[]
    for n in (16,64,256,1024):
        grp=[r for r in rows if r['n']==n and r['query_count']==64]
        def summ(alg,key):return sum(r['result'][alg][key] for r in grp)
        by_n.append({'n':n,'cases':len(grp),'queries_per_case':64,
          'integer_checks':summ('integer','checks'),
          'cache_checks':summ('cache64','checks'),
          'cache_hits':summ('cache64','hits'),
          'fraction_time_ns':summ('fraction','elapsed_ns'),
          'integer_time_ns':summ('integer','elapsed_ns'),
          'cache_time_ns':summ('cache64','elapsed_ns')})
    certificate={'model':'auxiliary exact rational circle source, fixed anchor',
       'science_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
       'theta_anchor':[P,Q],'case_count':len(rows),
       'query_executions_per_method':sum(r['query_count'] for r in rows),
       'direct_oracle_points_per_method':5*sum(r['query_count'] for r in rows),
       'all_checked':True,'by_n_q64':by_n,'rows':rows}
    output=dumps(certificate,ensure_ascii=False,indent=2)+'\n'
    if ns.output:
        with open(ns.output,'w',encoding='utf-8') as f:f.write(output)
    print(dumps({k:v for k,v in certificate.items() if k!='rows'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
