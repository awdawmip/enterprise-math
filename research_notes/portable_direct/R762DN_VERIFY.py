#!/usr/bin/env python3
"""R762DN: exact BRC positive-branch and Eisenstein-character verification.
No floating point, pi, trig, or external dependencies. Author evidence only.
"""
import json, math, hashlib
from collections import defaultdict, Counter

B = ((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))
ZETA = ((1,0),(0,1),(-1,-1))  # a+b*zeta, zeta^2+zeta+1=0

def mul(v, w):
    a,b=v; c,d=w
    return (a*c-b*d, a*d+b*c-b*d)

def pow_pair(v,n):
    y=(1,0)
    for _ in range(n): y=mul(y,v)
    return y

def spectrum():
    table={}
    for i in range(3):
        for j in range(3):
            for k in range(3):
                a=b=0
                for x,y,z in B:
                    u,v=ZETA[(i*x+j*y+k*z)%3]
                    a+=u; b+=v
                assert a%3==0 and b%3==0
                table[(i,j,k)]=(a//3,b//3)
    expected=Counter({(0,0):12,(2,0):1,(1,0):4,(0,-1):4,(1,1):4,(0,1):1,(-1,-1):1})
    assert Counter(table.values())==expected
    return table

def ttable(sp):
    out={}
    for r in range(6):
        c=Counter()
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    a=b=0
                    for (i,j,k),v in sp.items():
                        if (i,j,k)==(0,0,0) or v==(0,0): continue
                        w=mul(pow_pair(v,r),ZETA[(-i*x-j*y-k*z)%3])
                        a+=w[0];b+=w[1]
                    assert b==0,(r,x,y,z,(a,b))
                    c[a]+=1
        expected=(Counter({-4:8,-1:6,2:12,14:1}) if r%2==0
                  else Counter({-2:21,7:6}))
        assert c==expected,(r,c,expected)
        out[str(r)]={str(k):v for k,v in sorted(c.items())}
    return out

def convolution(Q,nmax):
    d={(0,0,0):1}
    records=[]
    for n in range(1,nmax+1):
        o=defaultdict(int)
        for (x,y,z),v in d.items():
            for i,j,k in B:
                o[((x+i)%Q,(y+j)%Q,(z+k)%Q)]+=v
        d=dict(o)
        assert sum(d.values())==6**n
        g=math.gcd(*d.values())
        c=g; e=0
        while c%3==0:
            c//=3;e+=1
        assert c==1,(Q,n,g,'non-three prime factor')
        if Q==3:
            expected=0 if n<=2 else n-1 if n%6==1 else n-2
            assert e==expected,(Q,n,e,expected)
        elif Q in (9,27):
            predicted=max(0,n//(Q//3)-2)
            assert e>=predicted,(Q,n,e,predicted,'theorem B')
            assert e==predicted,(Q,n,e,predicted,'finite conjecture test')
            if Q<=n< Q+2*(Q//3):
                assert e==(1 if n<Q+Q//3 else 2),(Q,n,e,'plateau theorem')
        if n in (2,3,4,6,7,8,9,12,18,27,36,45,54,81,120,180):
            records.append({'n':n,'gcd':str(g),'v3':e,'support':len(d)})
    return records

def main():
    sp=spectrum()
    tbl=ttable(sp)
    cases=((3,48),(9,180),(27,120))
    samples={str(q):convolution(q,max_n) for q,max_n in cases}
    evidence={
       'schema':'R762DN_AUTHOR_BRC_EXACT_EVIDENCE_V1',
       'task_id':'RS-X6-TRIADIC-CLOSURE-DYNAMICS',
       'claim_scope':'positive six-named-branch candidate endpoint group-ring law',
       'result':'PASS',
       'arithmetic':'unbounded Python integers; exact C_Q^3 convolution; formal Z[zeta] pairs',
       'spectrum_counts':{str(k):v for k,v in sorted(Counter(sp.values()).items())},
       't_residue_multisets':tbl,
       'cases':[{'Q':q,'n_min':1,'n_max':n} for q,n in cases],
       'configuration_count':sum(n for q,n in cases),
       'character_checks':27,
       't_state_checks':6*27,
       'samples':samples,
       'universal_proved':'Q=3 exact all n; any Q=3^a v3>=max(0,floor(n/3^(a-1))-2); first two plateaux exact',
       'conjecture_tested':'For Q=9 and Q=27, the stronger all-n sharpness formula holds on specified finite ranges; universal extension unproved',
       'source_pins':{
          'taskbook':'e3f42efac29a2da2d95be391f3231a664e2fade0',
          'p000':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
          'predecessor_r762dm':'abd4abb36cd82ff3a56b05b7f2ba41ac142e643e'
       },
       'native_event_admission':'NOT_ESTABLISHED',
       'independent_mathematical_review':'NOT_REVIEWED'
    }
    path='R762DN_EVIDENCE.json'
    with open(path,'w',encoding='utf-8') as f:
        json.dump(evidence,f,ensure_ascii=False,sort_keys=True,indent=2)
        f.write('\n')
    print('PASS',evidence['configuration_count'],'convolution configurations; 27 characters; 162 t-state checks')
    print('3-adic sample Q=3,n=7:', next(x for x in samples['3'] if x['n']==7))
    print('evidence_sha256',hashlib.sha256(open(path,'rb').read()).hexdigest())

if __name__=='__main__':main()
