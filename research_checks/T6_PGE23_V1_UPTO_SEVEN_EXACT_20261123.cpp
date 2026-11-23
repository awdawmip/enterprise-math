// Exhaustive, exact p-adic six-moment signatures for valuation-one denominators
// in the original T6 per-side mass cap 2331. No floating arithmetic.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;
using U128 = unsigned __int128;
constexpr int CAP=2331, NMAX=7, K=6;
struct Atom {int u, cost; array<uint64_t,K> sig;};
int prime;
array<uint64_t,K> moduli{};
vector<Atom> atoms;
array<uint64_t,NMAX+1> counts{};
vector<U128> keys;
uint64_t modular_inverse(uint64_t a, uint64_t m) {
    int64_t x=0,y=1,r=(int64_t)m,s=(int64_t)a;
    while(s){auto q=r/s; auto t=x-q*y; x=y; y=t; t=r-q*s;r=s;s=t;}
    if(r!=1){fprintf(stderr,"non-unit inverse\n");exit(2);}
    return (x%(int64_t)m+(int64_t)m)%(int64_t)m;
}
uint64_t mulmod(uint64_t a,uint64_t b,uint64_t m){return (uint64_t)(((U128)a*b)%m);}
U128 encode(const array<uint64_t,K>&s){
    U128 k=0,place=1;
    for(int j=0;j<K;j++){k+=(U128)s[j]*place;place*=moduli[j];}
    return k;
}
void rec(size_t index,int n,int mass,const array<uint64_t,K>&s){
    counts[n]++;
    keys.push_back(encode(s));
    if(n==NMAX)return;
    for(size_t i=index;i<atoms.size();i++){
        const Atom&a=atoms[i];
        if(mass+a.cost>CAP)break;
        array<uint64_t,K> next;
        for(int j=0;j<K;j++) next[j]=(s[j]+a.sig[j])%moduli[j];
        rec(i,n+1,mass+a.cost,next);
    }
}
array<uint64_t,NMAX+1> count_dp(){
    static uint64_t dp[NMAX+1][CAP+1];
    for(auto &row:dp)for(auto &v:row)v=0;
    dp[0][0]=1;
    for(const auto&a:atoms){
        for(int n=1;n<=NMAX;n++)
            for(int m=a.cost;m<=CAP;m++)dp[n][m]+=dp[n-1][m-a.cost];
    }
    array<uint64_t,NMAX+1> ret{};
    for(int n=0;n<=NMAX;n++)for(int m=0;m<=CAP;m++)ret[n]+=dp[n][m];
    return ret;
}
void run(int p){
    prime=p;
    atoms.clear(); counts={}; keys.clear();
    uint64_t current=1;
    for(int k=0;k<K;k++){current*=p;moduli[k]=current;}
    for(int u=1;u<=2332/p;u++){
        if(u%p==0)continue;
        Atom a{u,p*u-1,{}};
        for(int k=1;k<=K;k++){
            uint64_t m=moduli[k-1], inv=modular_inverse(u,m), v=1;
            for(int t=0;t<k;t++)v=mulmod(v,inv,m);
            a.sig[k-1]=v;
        }
        atoms.push_back(a);
    }
    auto dp=count_dp();
    uint64_t total=0;
    for(int n=0;n<=NMAX;n++)total+=dp[n];
    keys.reserve((size_t)total);
    rec(0,0,0,{});
    uint64_t sum=0;
    for(int n=0;n<=NMAX;n++){
        sum+=counts[n];
        if(counts[n]!=dp[n]){fprintf(stderr,"count/DP mismatch p=%d n=%d\n",p,n);exit(3);}
    }
    if(sum!=total||keys.size()!=total){fprintf(stderr,"total mismatch\n");exit(4);}
    sort(keys.begin(),keys.end());
    uint64_t collision=0;
    U128 first=0;
    for(size_t i=1;i<keys.size();i++)if(keys[i]==keys[i-1]){if(collision==0)first=keys[i];collision++;}
    printf("p=%d atoms=%zu total=%llu counts=",p,atoms.size(),(unsigned long long)total);
    for(int n=0;n<=NMAX;n++)printf("%s%llu",n?",":"",(unsigned long long)counts[n]);
    printf(" dup_adjacent=%llu",(unsigned long long)collision);
    if(collision){
        char buf[64];int len=0;do{buf[len++]='0'+first%10;first/=10;}while(first);
        printf(" first_key=");while(len)putchar(buf[--len]);
    }
    puts("");fflush(stdout);
}
int main(){for(int p:{23,29,31,37,41,43,47})run(p);}
