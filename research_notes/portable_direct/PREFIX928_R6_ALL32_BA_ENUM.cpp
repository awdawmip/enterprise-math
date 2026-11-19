// PREFIX-928 enumerator A: (b,a) inverse-a method. g++ -O3 -std=c++17 file.cpp -o checker
// Usage: checker output-sorted-pair-ids.bin
#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <iterator>
#include <numeric>
#include <vector>
using namespace std;
static constexpr uint64_t N=1ULL<<32;
static constexpr int QMIN=262145,QMAX=524287,M=131072;
int64_t egcd(int64_t a,int64_t b,int64_t &x,int64_t &y){if(!b){x=1;y=0;return a;}int64_t u,v;int64_t g=egcd(b,a%b,u,v);x=v;y=u-(a/b)*v;return g;}
int inv(int a,int b){int64_t x,y;int64_t g=egcd(a,b,x,y);if(g!=1)return -1;return int((x%b+b)%b);}
uint64_t code(int a,int b){return uint64_t((a-QMIN)/2)*M+((b-QMIN)/2);}
int main(int argc,char**argv){if(argc!=2){fprintf(stderr,"need output filename\n");return 1;}
vector<unsigned char> special(QMAX+1,0);
for(int b=QMIN;b<=QMAX;b+=2){int64_t r=2;for(int d=1;d<32;++d){if(r==1||r==b-1){special[b]=1;break;}r=r*2%b;}}
auto outside=[&](int a,int b){
 if(uint64_t(b)<33*((N+a-1)/a)||uint64_t(a)<33*((N+b-1)/b))return false;
 if(uint64_t(a/gcd(a,b))*b<N)return false;
 return special[b]==0;
};
vector<uint64_t> union_keys;union_keys.reserve(6000000);
vector<vector<uint64_t>> perbit(32);
uint64_t witness[32]={0};
for(int b=400001;b<=400127;b+=2){
 for(int a=QMIN;a<=QMAX;a+=2){
  int ia=inv(a,b);if(ia<0)continue;
  uint64_t cap=(N-1)/a;
  uint64_t v=ia;
  bool normal=outside(a,b),reverse=outside(b,a);
  for(int i=0;i<32;++i){
   uint64_t h=1ULL<<i;
   for(int s=-1;s<=1;s+=2){
    uint64_t k=(s==-1?v:(b-v)%b);
    if(k==0||k>cap)continue;
    uint64_t A=k*uint64_t(a);
    if(A+(s==1?h:0)>=N)continue;
    if((int64_t(A)+s*int64_t(h))%b!=0){fprintf(stderr,"congruence bug\n");return 2;}
    uint64_t x=(s==1?h:0),y=A+x;
    if(!(y<N&&(y-x)%a==0&&(int64_t(y)-int64_t(x^h))%b==0)){fprintf(stderr,"witness bug\n");return 2;}
    ++witness[i];
    if(normal)perbit[i].push_back(code(a,b));
    if(reverse)perbit[i].push_back(code(b,a));
   }
   v=2*v%b;
  }
 }
}
for(int i=0;i<32;++i){
 auto &v=perbit[i];
 sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());
 size_t individual=v.size();
 vector<uint64_t> merge;merge.reserve(union_keys.size()+v.size());
 set_union(union_keys.begin(),union_keys.end(),v.begin(),v.end(),back_inserter(merge));
 union_keys.swap(merge);
 printf("bit=%d witness=%llu outside=%zu cumulative=%zu\n",i,(unsigned long long)witness[i],individual,union_keys.size());
}
FILE*f=fopen(argv[1],"wb");if(!f)return 2;
for(uint64_t key:union_keys){unsigned char b[8];for(int j=0;j<8;++j)b[j]=((key>>(8*j))&255);if(fwrite(b,1,8,f)!=8)return 3;}
return fclose(f);
}
