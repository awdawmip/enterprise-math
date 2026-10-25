// D25 original-summand exhaustive integer scan, author-side, NOT native CM benchmark.
// Compile: g++ -O3 -std=c++17 this.cpp -o scan
// Execute: ./scan 100000 /tmp/d25_W_100k.csv
#include <bits/stdc++.h>
using namespace std;
using u64=unsigned long long; using u128=__uint128_t;
static inline u64 mul(u64 a,u64 b,u64 q){return static_cast<u64>((u128)a*b%q);}
static u64 inv_euclid(u64 a,u64 q){
    long long b=q,s0=1,s1=0; long long aa=a;
    while(b){long long t=aa/b;long long r=aa-t*b;aa=b;b=r;long long s=s0-t*s1;s0=s1;s1=s;}
    if(aa!=1)throw runtime_error("nonunit denominator");
    long long ans=s0%(long long)q;return ans<0?ans+q:ans;
}
static bool prime(int p){if(p<2)return false;for(int d=2;d*d<=p;++d)if(p%d==0)return false;return true;}
static u64 original_W_mod_p3(int p){
    u64 q=(u64)p*p*p;
    vector<u64> inv(p);inv[1]=1;
    for(int i=2;i<p;++i)inv[i]=(q-mul(q/i,inv[q%i],q))%q;
    u64 inv36=inv_euclid(36,q),t=1,w=0;
    for(int n=0;n<p;++n){
        w=(w+mul(6ULL*n+1,t,q))%q;
        if(n+1==p)break;
        auto numer=mul(mul(2ULL*n+1,3ULL*n+1,q),3ULL*n+2,q);
        u64 de=mul(mul(mul(inv[n+1],inv[n+1],q),inv[n+1],q),inv36,q);
        t=mul(t,mul(numer,de,q),q);
    }
    return w;
}
int main(int argc,char**argv){
    const int maxp=argc>1?stoi(argv[1]):12000;
    ofstream csv;
    if(argc>2){csv.open(argv[2]); if(!csv)throw runtime_error("cannot write CSV");
        csv<<"p,p_mod_24,W_mod_p3,expected_mod_p3,difference_mod_p3\n";}
    size_t counts[6]={};int failures=0,last=0;
    for(int p=5;p<=maxp;++p){if(!prime(p))continue;
        u64 q=(u64)p*p*p, got=original_W_mod_p3(p);
        u64 expected=(p%6==1)?(u64)p:(q-p);
        if(csv)csv<<p<<","<<(p%24)<<","<<got<<","<<expected<<","<<((got+q-expected)%q)<<"\n";
        if(got!=expected){cerr<<"FAIL prime="<<p<<" W="<<got<<" expected="<<expected<<"\n";++failures;}
        ++counts[p%6];last=p;
        if(p==5||p==7||p==11||p==13||p==19||p==37||p==101||p==19963)
            cout<<"SAMPLE p="<<p<<" Wmodp3="<<got<<" expected="<<expected<<"\n";
    }
    cout<<"SUMMARY checked="<<counts[1]+counts[5]<<" class_1="<<counts[1]<<" class_5="<<counts[5]
        <<" last_prime="<<last<<" mismatches="<<failures<<"\n";
    return failures?1:0;
}
