// Exact T6 two-v5-atom rigidity: final three odd-prime modular obstructions.
// Requires only C++17. No floating point or external libraries.
#include <bits/stdc++.h>
using namespace std;
using u64=uint64_t;
using Sig=array<uint32_t,4>;
const array<int,4> KS={2,3,4,6};
int P,R;
array<uint32_t,4> MOD{};
vector<pair<int,Sig>> steps;
vector<u64> A,B;
Sig high{};
size_t generated=0;

int64_t inv(int64_t a,int64_t m) {
    int64_t b=m,u=1,v=0;
    while(b) {
        int64_t t=a/b;
        a-=t*b;swap(a,b);
        u-=t*v;swap(u,v);
    }
    if(a!=1)throw runtime_error("no modular inverse");
    return(u%m+m)%m;
}
u64 key(const Sig &s) {
    u64 x=0;
    for(int i=0;i<4;i++)x=x*MOD[i]+s[i];
    return x;
}
Sig add(Sig a,const Sig &b) {
    for(int i=0;i<4;i++) {
        a[i]+=b[i];
        if(a[i]>=MOD[i])a[i]-=MOD[i];
    }
    return a;
}
void enumerate(int i,int cost,Sig s) {
    if(i==(int)steps.size()) {
        A.push_back(key(s));
        B.push_back(key(add(s,high)));
        generated++;
        return;
    }
    auto [w,g]=steps[i];
    for(;cost<=R;cost+=w) {
        enumerate(i+1,cost,s);
        s=add(s,g);
    }
}
void radix(vector<u64> &arr) {
    vector<u64> tmp(arr.size());
    vector<size_t> cnt(65536);
    for(int shift=0;shift<64;shift+=16) {
        fill(cnt.begin(),cnt.end(),0);
        for(u64 v:arr)cnt[(v>>shift)&65535]++;
        size_t cumulative=0;
        for(auto &n:cnt) {
            size_t old=n;
            n=cumulative;
            cumulative+=old;
        }
        for(u64 v:arr)tmp[cnt[(v>>shift)&65535]++]=v;
        arr.swap(tmp);
    }
}
void run(int id,int p,int r,int multiplicity,size_t expected) {
    P=p;R=r;
    steps.clear();A.clear();B.clear();generated=0;
    __uint128_t product=1;
    for(int i=0;i<4;i++) {
        uint32_t m=1;
        for(int j=0;j<KS[i];j++)m*=P;
        MOD[i]=m;
        product*=m;
    }
    assert(product<=(__uint128_t)UINT64_MAX);
    for(int u=1;u<=(R+1)/P;u++)if(u%P&&u%32) {
        Sig g{};
        for(int i=0;i<4;i++) {
            u64 z=inv(u,MOD[i]),v=1;
            for(int j=0;j<KS[i];j++)v=v*z%MOD[i];
            g[i]=(uint32_t)v;
        }
        steps.push_back({P*u-1,g});
    }
    for(int i=0;i<4;i++) {
        u64 z=inv(32,MOD[i]),v=1;
        for(int j=0;j<KS[i];j++)v=v*z%MOD[i];
        high[i]=(multiplicity*v)%MOD[i];
    }
    A.reserve(expected);B.reserve(expected);
    enumerate(0,0,Sig{});
    assert(generated==expected);
    radix(A);radix(B);
    size_t i=0,j=0;
    while(i<A.size()&&j<B.size()) {
        if(A[i]==B[j]) {
            cout<<"COLLISION pair="<<id<<" key="<<A[i]<<"\n";
            exit(3);
        }
        if(A[i]<B[j])i++;
        else j++;
    }
    cout<<"PASS pair="<<id<<" p="<<p<<" remaining_mass="<<r
        <<" profiles="<<generated<<" modular_projection=DISJOINT\n"<<flush;
}
int main() {
    // A has no p-primary v5 atom; B has 1 or 2 copies of d=32*p.
    // The p^2 residual layer cancels independently by S1,...,St
    // and modular Vandermonde over its t admissible denominators.
    run(7,17,733,1,386589);
    run(11,19,1117,2,5559120);
    run(1,17,1245,2,47972912);
    cout<<"PASS: all final three profile pairs excluded\n";
}
