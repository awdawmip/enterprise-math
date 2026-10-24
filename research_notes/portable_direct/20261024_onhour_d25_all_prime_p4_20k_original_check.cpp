// Finite author-side arithmetic diagnostic: NOT a Source-native benchmark.
// All p <= 20000 with p = 1 (mod 6), original S_m at n <=4m,
// comparing p-free factorial terms against original exact recurrence terms.
// Use local command: c++ -O2 -std=c++17 FILE.cpp -o check && ./check
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <stdexcept>
#include <vector>
using u64=uint64_t; using u128=unsigned __int128; using i64=int64_t;
inline u64 mul(u64 a,u64 b,u64 mod){return (u64)((u128)a*b%mod);}
u64 powm(u64 a,u64 e,u64 mod){u64 b=1;for(;e;e>>=1,a=mul(a,a,mod))if(e&1)b=mul(b,a,mod);return b;}
u64 inverse(u64 a,u64 n){
    i64 b=(i64)n, old=(i64)(a%n),x0=1,x1=0;
    while(b){i64 q=old/b; i64 t=old-q*b;old=b;b=t;t=x0-q*x1;x0=x1;x1=t;}
    if(old!=1)throw std::runtime_error("non-unit inverse");
    return (u64)((x0%(i64)n+(i64)n)%(i64)n);
}
std::vector<int> primes(int N){std::vector<bool> isp(N+1,true);isp[0]=isp[1]=false;for(int k=2;k*k<=N;++k)if(isp[k])for(int n=k*k;n<=N;n+=k)isp[n]=false;std::vector<int>res;for(int p=7;p<=N;++p)if(isp[p]&&p%6==1)res.push_back(p);return res;}
struct Result{u64 sf,sr,target;};
Result check(int p){
    int m=(p-1)/6, N=2*p-2;
    u64 mod=(u64)p*p*p*p;
    std::vector<u64> ff(N+1,1),ii(N+1,1);
    for(int t=1;t<=N;t++)ff[t]=mul(ff[t-1],(t%p? t:t/p),mod);
    ii[N]=inverse(ff[N],mod);
    for(int t=N;t>0;--t)ii[t-1]=mul(ii[t],(t%p?t:t/p),mod);
    if(mul(ff[N],ii[N],mod)!=1)throw std::runtime_error("inverse factorial error");
    u64 inv3=inverse(3,mod),inv216=inverse(216,mod),inv36=inverse(36,mod);
    u64 common=mul(mul(ff[6*m],ii[2*m],mod),powm(inv3,6*m,mod),mod);
    u64 A=mul(mul(mul(ff[6*m],ii[2*m],mod),ii[2*m],mod),mul(ii[2*m],powm(inv3,6*m,mod),mod),mod);
    u64 sf=0,sr=0,Runit=1,power216=1;int v=0;
    for(int n=0;n<=4*m;++n){
        int vfac=(4*m+2*n)/p+(3*n)/p-(4*m+n)/p;
        if(vfac!=(n>m)||v!=vfac)throw std::runtime_error("valuation mismatch p="+std::to_string(p));
        u64 q=mul(common,ff[4*m+2*n],mod);
        q=mul(q,ff[3*n],mod);
        q=mul(q,ii[2*m+n],mod);q=mul(q,ii[2*m+n],mod);
        q=mul(q,ii[4*m+n],mod);q=mul(q,ii[n],mod);q=mul(q,ii[n],mod);
        q=mul(q,power216,mod);q=mul(q,6*n+2*p-1,mod);
        if(vfac)q=mul(q,p,mod);
        sf=(sf+q)%mod;
        q=mul(mul(A,Runit,mod),(u64)(6*n+2*p-1),mod);
        if(v)q=mul(q,p,mod);
        sr=(sr+q)%mod;
        if(n==4*m)break;
        u64 num=(u64)(4*m+2*n+1)*(3*n+1)*(3*n+2);
        u64 den=(u64)36*(n+1)*(2*m+n+1)*(4*m+n+1);
        while(num%p==0){num/=p;v++;}
        while(den%p==0){den/=p;v--;}
        u64 q1=mul(ii[n+1],ff[n],mod);
        u64 q2=mul(ii[2*m+n+1],ff[2*m+n],mod);
        u64 q3=mul(ii[4*m+n+1],ff[4*m+n],mod);
        u64 id=mul(mul(mul(inv36,q1,mod),q2,mod),q3,mod);
        if(mul(id,den%mod,mod)!=1) throw std::runtime_error("denom inverse mismatch");
        Runit=mul(mul(Runit,num%mod,mod),id,mod);
        power216=mul(power216,inv216,mod);
    }
    u64 target=mul(p,powm(mul(4,inv3,mod),p-1,mod),mod);
    if(sf!=sr)throw std::runtime_error("two algorithm mismatch p="+std::to_string(p));
    return {sf,sr,target};
}
int main(){
    std::map<int,int> classes;int total=0,failures=0,new_nontarget=0,sharpness_exceptions=0;
    std::ofstream out("d25_all_classes_p4_20k_records.csv");
    if(!out)throw std::runtime_error("cannot write CSV");
    out<<"p,m,p_mod24,S_factorial,S_recurrence,target,difference_mod_p4,third_digit_coefficient_mod_p\n";
    for(int p:primes(20000)){
        Result r=check(p);u64 mod=(u64)p*p*p*p;u64 delta=(r.sf+mod-r.target)%mod;
        ++total;++classes[p%24];
        if(delta%((u64)p*p*p)!=0){++failures;std::cout<<"FAIL "<<p<<" residue "<<delta<<"\n";}
        if(p%24==1||p%24==7)++new_nontarget;
        if(delta==0)++sharpness_exceptions;
        out<<p<<","<<(p-1)/6<<","<<p%24<<","<<r.sf<<","<<r.sr<<","<<r.target<<","<<delta<<","<<(delta/((u64)p*p*p))<<"\n";
    }
    std::cout<<"total="<<total<<" new_non_target="<<new_nontarget<<" failures_p3="<<failures<<" v_p_ge_4="<<sharpness_exceptions<<"\n";
    for(auto [k,v]:classes)std::cout<<"p%24="<<k<<": "<<v<<"\n";
    return (failures||sharpness_exceptions)?1:0;
}
