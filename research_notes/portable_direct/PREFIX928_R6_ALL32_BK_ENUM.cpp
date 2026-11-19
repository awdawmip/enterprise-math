// PREFIX-928 independent enumerator B: (b,k) inverse-k method and pair bit masks.
// g++ -std=c++17 -O3 file.cpp -o checker; checker sorted-pair-ids.bin
#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <unordered_map>
#include <vector>
using namespace std;
static constexpr uint64_t N=1ULL<<32;static constexpr int LOW=262145,HIGH=524287,M=131072;
int64_t xgcd(int64_t a,int64_t b,int64_t&x,int64_t&y){if(!b){x=1;y=0;return a;}int64_t u,v;int64_t g=xgcd(b,a%b,u,v);x=v;y=u-(a/b)*v;return g;}
int inverse(int a,int b){int64_t x,y;return xgcd(a,b,x,y)==1?int((x%b+b)%b):-1;}
uint64_t id(int a,int b){return uint64_t((a-LOW)/2)*M+(b-LOW)/2;}
int main(int argc,char**argv){if(argc!=2)return 1;
vector<char> sp(HIGH+1,0);
for(int b=LOW;b<=HIGH;b+=2){uint64_t r=2;for(int i=1;i<=31;++i){if(r==1||r==b-1){sp[b]=1;break;}r=r*2%b;}}
auto outside=[&](int a,int b){return uint64_t(b)>=33*((N+a-1)/a)&&uint64_t(a)>=33*((N+b-1)/b)&&uint64_t(a/gcd(a,b))*b>=N&&!sp[b];};
unordered_map<uint64_t,uint32_t> masks;masks.reserve(6000000);
uint64_t witnesses[32]={0};
for(int b=400001;b<=400127;b+=2){
 for(int k=1;k<=int((N-1)/LOW);++k){
  int ik=inverse(k,b);if(ik<0)continue;
  uint64_t pos=ik;
  for(int i=0;i<32;++i){
   uint64_t h=1ULL<<i;
   for(int s=-1;s<=1;s+=2){
    uint64_t r=s==-1?pos:((b-pos)%b);
    if(r<LOW)r+=b;
    if(r<LOW||r>HIGH||(r&1)==0)continue;
    int a=int(r);uint64_t A=uint64_t(k)*a;
    if(A+h*(s==1)>=N)continue;
    if((int64_t(A)+s*int64_t(h))%b!=0){fprintf(stderr,"bad modulo\n");return 2;}
    uint64_t x=s==1?h:0,y=A+x;
    if(y>=N||(y-x)%a!=0||(int64_t(y)-int64_t(x^h))%b!=0){fprintf(stderr,"bad witness\n");return 3;}
    witnesses[i]++;
    if(outside(a,b))masks[id(a,b)] |= uint32_t(1)<<i;
    if(outside(b,a))masks[id(b,a)] |= uint32_t(1)<<i;
   }
   pos=2*pos%b;
  }
 }
}
uint64_t firstkey[32];for(int i=0;i<32;++i)firstkey[i]=UINT64_MAX;
for(auto &kv:masks){int bit=__builtin_ctz(kv.second);if(kv.first<firstkey[bit])firstkey[bit]=kv.first;}
for(int i=0;i<32;++i)if(firstkey[i]!=UINT64_MAX){int a=LOW+2*(firstkey[i]/M);int b=LOW+2*(firstkey[i]%M);fprintf(stderr,"FIRST bit=%d a=%d b=%d\n",i,a,b);}
vector<uint64_t> ids;ids.reserve(masks.size());for(auto &v:masks)ids.push_back(v.first);sort(ids.begin(),ids.end());
uint64_t single[32]={0},newcount[32]={0};
for(auto &v:masks){uint32_t mask=v.second;for(int i=0;i<32;++i)if(mask>>i&1)single[i]++;newcount[__builtin_ctz(mask)]++;}
uint64_t total=0;
for(int i=0;i<32;++i){total+=newcount[i];printf("bit=%d witness=%llu outside=%llu cumulative=%llu\n",i,(unsigned long long)witnesses[i],(unsigned long long)single[i],(unsigned long long)total);}
FILE*f=fopen(argv[1],"wb");if(!f)return 2;
for(uint64_t key:ids){unsigned char bytes[8];for(int i=0;i<8;++i)bytes[i]=(key>>(8*i))&255;if(fwrite(bytes,1,8,f)!=8)return 3;}
return fclose(f);
}
