#!/usr/bin/env python3
"""PREFIX-923 reproducible bucket-capacity and 1024 high-band collision census.

Requires Python 3, g++ C++17 and the pinned
PREFIX921_R6_DISTINCT_START_ROW.cpp in the same directory.
The PREFIX-921 scan and direct endpoint verifier remain byte-for-byte intact:
only its output/reporting main is replaced for a bounded high-a census.
"""
from __future__ import annotations
import bisect, csv, hashlib, json, subprocess, sys, tempfile
from pathlib import Path

N=1<<32
P=32
L=(1<<18)+1
H=(1<<19)-1
M=1<<17
A=range(L,H+1,2)
assert len(A)==M

def capacity_count():
    caps=[bisect.bisect_left(A,(P+1)*((N+a-1)//a)) for a in A]
    directional=sum(caps)
    j=M-1
    both=union=0
    for i in range(M):
        while j>=0 and caps[j]<=i: j-=1
        union+=max(caps[i],j+1)
        both+=min(caps[i],j+1)
    prior_global=sum(bisect.bisect_left(A,((P+1)*N+a-1)//a) for a in A)
    assert 2*directional-both==union
    assert prior_global==7364142398
    assert directional==7365158936
    assert union==7365546244
    return {'global_capacity':prior_global,'direction_bucket':directional,
            'union_bucket':union,'beyond_global':union-prior_global,
            'total_pairs':M*M}

def compile_checker(source,dest):
    s=source.read_text(encoding='utf-8')
    start=s.index('int main(int argc,char** argv){')
    assert 'static Witness scan(int a,int b)' in s[:start]
    assert 'verify(a,b,w)' in s[:start]
    main=r"""
int main(int argc,char** argv){
 if(argc!=4)return 7;
 int b=std::stoi(argv[1]),low=std::stoi(argv[2]),high=std::stoi(argv[3]);
 if(b<262145||b>524287||!(b&1)||low<262145||high>524287||!(low&1)||!(high&1)||low>high)return 8;
 int count=0,raw_misses=0,first=0;
 for(int a=low;a<=high;a+=2){
  Witness w=scan(a,b);++count;
  if(w.type==0){if(raw_misses==0)first=a; ++raw_misses;}
 }
 std::cout<<b<<","<<count<<","<<raw_misses<<","<<first<<"\n";
}
"""
    with tempfile.TemporaryDirectory(prefix='prefix923c_') as d:
        cp=Path(d)/'witness.cpp'
        cp.write_text(s[:start]+main,encoding='utf-8')
        subprocess.run(['g++','-O3','-std=c++17',str(cp),'-o',str(dest)],check=True)

def screen_rows(source,result_path):
    with tempfile.TemporaryDirectory(prefix='prefix923run_') as d:
        binary=Path(d)/'row'
        compile_checker(source,binary)
        rows=[]
        for t in range(1024):
            b=L+2*((77081*t+12345)%M)
            raw=subprocess.check_output([str(binary),str(b),'500001','524287'],text=True)
            bb,n,missing,first=map(int,raw.strip().split(','))
            assert bb==b and n==12144 and missing==first==0
            rows.append((bb,n,missing,first))
    with result_path.open('w',newline='',encoding='ascii') as f:
        w=csv.writer(f,lineterminator='\n')
        w.writerow(('b','rows','raw_zero','first_zero'))
        w.writerows(rows)
    sha=hashlib.sha256(result_path.read_bytes()).hexdigest()
    assert sha=='831e4092915dfa3f2d7c06aaea90fbc40240fdd2f1bd7abce7878e7e5068e385'
    return {'rows':len(rows),'tested_pairs':sum(r[1] for r in rows),
            'raw_zero':sum(r[2] for r in rows),'csv_sha256':sha,
            'first_b':rows[0][0],'last_b':rows[-1][0]}

if __name__=='__main__':
    src=Path(sys.argv[1]) if len(sys.argv)>1 else Path('PREFIX921_R6_DISTINCT_START_ROW.cpp')
    out=Path(sys.argv[2]) if len(sys.argv)>2 else Path('PREFIX923_R6_1024_HIGHBAND_COUNTS.csv')
    print(json.dumps({'capacity':capacity_count(),'high_band':screen_rows(src,out)},indent=2))
