// T6 exact p17-valuation-one, at most eight atoms per side.
// C++17; full integer recursion and independent generating-function count.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

constexpr int CAP=2331, P=17, NMAX=8;
constexpr array<int,5> MOD={17,289,4913,83521,1419857};
constexpr array<uint64_t,9> EXPECTED={
  1,129,4220,62225,531399,3017496,12469599,39974384,104260287
};
array<array<int,5>,138> ATOM{};
array<uint64_t,9> counted{};
vector<uint64_t> keys;

int inverse(int a,int m) {
  int t=0,nt=1,r=m,nr=a;
  while(nr){int q=r/nr,x=t-q*nt;t=nt;nt=x;x=r-q*nr;r=nr;nr=x;}
  assert(r==1);
  return t<0?t+m:t;
}
uint64_t encode(const array<int,5>& sig) {
  uint64_t key=0,place=1;
  for(int k=0;k<5;k++){key+=(uint64_t)sig[k]*place;place*=MOD[k];}
  assert(place==2862423051509815793ULL); // product 17^(1+...+5)
  return key;
}
void enumerate(int start,int n,int cost,const array<int,5>& sig){
  ++counted[n];
  keys.push_back(encode(sig));
  if(n==NMAX)return;
  for(int u=start;u<=137;u++){
    if(u%P==0)continue;
    int c=P*u-1;
    if(cost+c>CAP)break;
    array<int,5> next{};
    for(int k=0;k<5;k++)next[k]=(sig[k]+ATOM[u][k])%MOD[k];
    enumerate(u,n+1,cost+c,next);
  }
}
array<uint64_t,9> independent_counts(){
  array<array<uint64_t,CAP+1>,NMAX+1> dp{};
  dp[0][0]=1;
  for(int u=1;u<=137;u++){
    if(u%P==0)continue;
    int c=P*u-1;
    for(int n=1;n<=NMAX;n++)
      for(int mass=c;mass<=CAP;mass++)dp[n][mass]+=dp[n-1][mass-c];
  }
  array<uint64_t,9> out{};
  for(int n=0;n<=NMAX;n++)
    for(int mass=0;mass<=CAP;mass++)out[n]+=dp[n][mass];
  return out;
}
int main(){
  for(int u=1;u<=137;u++){
    if(u%P==0)continue;
    for(int k=0;k<5;k++){
      uint64_t pw=1;int inv=inverse(u,MOD[k]);
      for(int j=0;j<=k;j++)pw=pw*inv%MOD[k];
      ATOM[u][k]=(int)pw;
    }
  }
  keys.reserve(160319740);
  enumerate(1,0,0,{});
  assert(independent_counts()==counted);
  assert(counted==EXPECTED);
  sort(keys.begin(),keys.end());
  for(size_t i=1;i<keys.size();i++)assert(keys[i]!=keys[i-1]);
  cout<<"by_size:";
  for(int n=0;n<=NMAX;n++)cout<<" "<<n<<":"<<counted[n];
  cout<<"\ntotal="<<keys.size()<<" unique="<<keys.size()
      <<" collisions=0\nPASS: up-to-eight p17-v1 profiles injective for k=1..5\n";
}
