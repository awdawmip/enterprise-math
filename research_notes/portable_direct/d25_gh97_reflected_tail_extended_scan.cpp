#include <cstdint>
#include <iostream>
#include <vector>
using i64 = std::int64_t;

i64 mod_pow(i64 a, int e, int p) {
    i64 v=1;
    for(;e;e>>=1,a=a*a%p) if(e&1) v=v*a%p;
    return v;
}
int r_tail_mod_p(int p) {
    const int d=(p-3)/4;
    std::vector<int> inv(p);
    inv[1]=1;
    for(int k=2;k<p;++k) inv[k]=p-(i64)(p/k)*inv[p%k]%p;
    i64 h=1, zpow=mod_pow(9,d+1,p), r=0;
    for(int j=0;j<=d;++j) {
        r=(r+(i64)((8*j+5)%p)*h%p*inv[d+1+j]%p*zpow%p)%p;
        if(j<d) {
            i64 x=(4*j+3)%p;
            i64 num=x*x%p*x%p;
            h=h*num%p*inv[4*j+4]%p*inv[4*j+5]%p*inv[4*j+6]%p;
            zpow=zpow*9%p;
        }
    }
    return (int)r;
}
int main() {
    const int bound=100000;
    std::vector<char> prime(bound,true);
    prime[0]=prime[1]=false;
    for(int q=2;q*q<bound;++q) if(prime[q])
        for(int j=q*q;j<bound;j+=q) prime[j]=false;
    int n0=0,n1=0;
    std::vector<int> zero0,zero1;
    for(int p=7;p<bound;++p) if(prime[p] && p%4==3) {
        auto r=r_tail_mod_p(p);
        if(p<30000) {++n0; if(!r) zero0.push_back(p);}
        else {++n1; if(!r) zero1.push_back(p);}
    }
    std::cout<<"SOURCE_REFLECTED_TAIL_EXACT_PRIME_SCAN p<"<<bound<<"\n";
    std::cout<<"old_range_count "<<n0<<" zeros";
    for(int p:zero0) std::cout<<" "<<p;
    std::cout<<"\nnew_range_count "<<n1<<" zeros";
    for(int p:zero1) std::cout<<" "<<p;
    std::cout<<"\n";
    for(int p: {7,3347,30011,40031,65519,99991})
        std::cout<<"sample "<<p<<" residue "<<r_tail_mod_p(p)<<"\n";
}
