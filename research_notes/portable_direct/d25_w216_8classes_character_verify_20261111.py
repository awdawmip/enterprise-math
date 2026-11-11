#!/usr/bin/env python3
"""D25 original signed W216: exact finite character test. Author-side; not native H0/B0."""
import json
import hashlib
from pathlib import Path

def primes_upto(n):
    s=bytearray(b'\x01')*(n+1);s[:2]=b'\0\0'
    for p in range(2,int(n**0.5)+1):
        if s[p]:s[p*p:n+1:p]=b'\0'*(1+(n-p*p)//p)
    return [p for p in range(5,n+1) if s[p]]

def w216(p, digits=4):
    q=p**digits; a=1;total=1;inv36=pow(36,-1,q)
    for k in range(1,p):
        j=k-1
        a=a*(2*j+1)*(3*j+1)*(3*j+2)*inv36*pow(k,-3,q)%q
        total=(total+(6*k+1)*a)%q
    return total

def independent_stripped_factorials(p):
    q=p**3
    f=[1]*(3*(p-1)+1)
    for n in range(1,len(f)):
        f[n]=f[n-1]*(n//p if n%p==0 else n)%q
    total=0;d=1;inv216=pow(216,-1,q)
    for k in range(p):
        v=2*k//p+3*k//p
        a=pow(p,v,q)*f[2*k]*f[3*k]*pow(f[k],-5,q)*d%q
        total=(total+(6*k+1)*a)%q;d=d*inv216%q
    return total

def main():
    targets={5,7,11,13,17,19,23,31,37,43,73,109,139,157,373,997,1009,1997,3001,4001,4999}
    records=[];cross=[]
    for p in primes_upto(5000):
        chi=1 if p%3==1 else -1
        v=w216(p,4)
        assert (v-chi*p)%p**3==0,(p,v)
        if p in targets:
            assert independent_stripped_factorials(p)==v%p**3,p
            cross.append(p)
        records.append({'p':p,'class_mod_24':p%24,'chi_minus_3':chi,'w_mod_p3':v%p**3,
                        'epsilon_mod_p':((v-chi*p)%p**4)//p**3})
    assert len(records)==667
    data={'schema':'EM_D25_W216_CHARACTER_FINITE_CERT_V1',
          'scope':'AUTHOR_SIDE_FINITE_EXACT_UNREVIEWED_NOT_ADMITTED',
          'frozen_scientific_source_pin':'c47e13e4aba0e006366f989d6334d443f6333ae3',
          'identity':'chatgpt-research-onhour-enterprise-math-20260923',
          'definition':'W_p=sum_{k=0}^{p-1}(6k+1)*(2k)!*(3k)!/(216^k*(k!)^5)',
          'claim_checked':'W_p == (Legendre(-3,p)*p) mod p^3 for all primes 5<=p<=5000',
          'range':[5,5000],'prime_count':len(records),
          'class_counts':{str(r):sum(x['class_mod_24']==r for x in records) for r in (1,5,7,11,13,17,19,23)},
          'independent_algorithm_primes':cross,'exceptions':[],'rows':records}
    # Compact separators use reproducible source-controlled canonical JSON bytes.
    path=Path(__file__).with_name('d25_w216_character_5_5000_records_20261111.json')
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'tested':len(records),'crosschecked':cross,
        'p4_zero_primes':[x['p'] for x in records if x['epsilon_mod_p']==0],
        'sha256':hashlib.sha256(path.read_bytes()).hexdigest()},indent=2))
if __name__=='__main__':main()
