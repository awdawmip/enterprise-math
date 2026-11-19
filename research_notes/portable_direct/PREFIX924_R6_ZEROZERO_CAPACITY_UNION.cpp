// PREFIX-924 C++17 independent exact census; g++ -O2 -std=c++17 this.cpp -o check
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
constexpr int L=262145,U=524287,C=33;
constexpr uint64_t N=1ULL<<32;
uint64_t ceildiv(uint64_t x,uint64_t y){return (x+y-1)/y;}
vector<vector<int>> divs;
vector<int> mu;
void init(){
 divs.resize(U+1);mu.assign(U+1,1);
 for(int d=1;d<=U;d+=2)for(int a=d;a<=U;a+=2*d)divs[a].push_back(d);
 vector<int> primes,low(U+1);
 mu[0]=0;
 for(int n=2;n<=U;n++){
  if(!low[n]){low[n]=n;primes.push_back(n);mu[n]=-1;}
  for(int p:primes){
   if(p>low[n]||int64_t(n)*p>U)break;
   low[n*p]=p;
   if(n%p==0){mu[n*p]=0;break;}
   mu[n*p]=-mu[n];
  }
 }
}
uint64_t count_row(int a,int lower){
 if(lower>U)return 0;
 uint64_t ans=0;
 for(int g:divs[a]){
  int q=a/g,lo=ceildiv(lower,g),hi=min(U/g,int((N-1)/a));
  if(lo>hi)continue;
  int64_t count=0;
  for(int d:divs[q])if(mu[d]!=0)
   count+=mu[d]*((hi/d+1)/2-((lo-1)/d+1)/2); // ONLY ODD t
  if(count<0)exit(2);
  ans+=count;
 }
 return ans;
}
int threshold(int a){return max({L,int(C*ceildiv(N,a)),int(ceildiv(N,a/C))});}
uint64_t brute(int a,int lower){
 uint64_t c=0;
 for(int b=L;b<=U;b+=2)
  if(b>=lower&&(uint64_t(a)/gcd(a,b))*b<N)c++;
 return c;
}
int main(){
 init();uint64_t all=0,extra=0,safe=0,diag=0,checks=0;
 for(int a=L;a<=U;a+=2){
  int t=threshold(a);auto z=count_row(a,L),w=count_row(a,t);
  all+=z;extra+=w;diag+=(a>=t);
  int begin=t+(t%2==0);
  if(begin<=U)safe+=(U-begin)/2+1;
  if((a-L)/2%1024==0){
   if(brute(a,L)!=z||brute(a,t)!=w)return 2;
   checks++;
  }
 }
 constexpr uint64_t total=131072ULL*131072;
 if(all!=209050784ULL||extra!=95349218ULL||safe!=9814322940ULL||diag!=73900||checks!=128)return 3;
 cout<<"zerozero_all="<<all<<"\nzerozero_outside_capacity="<<extra
     <<"\ncapacity_violations="<<(total-safe)
     <<"\nunion="<<(total-safe+extra)<<"\nremaining="<<(safe-extra)
     <<"\ndiagonal_outside_capacity="<<diag<<"\ndirect_gcd_rows_verified="<<checks<<"\n";
}
