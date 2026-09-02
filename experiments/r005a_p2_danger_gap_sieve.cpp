// Exact dangerous prime-gap enumerator for R005-A p=2.
// Usage:
//   g++ -O3 r005a_p2_danger_gap_sieve.cpp -o danger_gap_sieve
//   ./danger_gap_sieve 387096200 > R005A_P2_DANGER_GAPS_UPTO_387096200.json
#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){
 long long N=argc>1?stoll(argv[1]):387096200LL;
 int root=(int)sqrt((long double)N)+1;
 vector<bool> small(root+1,true); small[0]=small[1]=false; vector<int> base;
 for(int i=2;i<=root;i++) if(small[i]){base.push_back(i); if(1LL*i*i<=root) for(long long j=1LL*i*i;j<=root;j+=i) small[(size_t)j]=false;}
 const long long SEG=1LL<<20; long long prev=0,pc=0,dc=0,maxg=0; bool first=true;
 cout<<"{\n  \"limit\": "<<N<<",\n  \"dangerous_gaps\": [\n";
 for(long long L=2;L<=N;L+=SEG){
  long long R=min(N,L+SEG-1); vector<char> isp((size_t)(R-L+1),true);
  for(int p:base){if(1LL*p*p>R)break; long long s=max(1LL*p*p,((L+p-1)/p)*1LL*p); for(long long x=s;x<=R;x+=p) isp[(size_t)(x-L)]=false;}
  for(long long x=L;x<=R;x++) if(isp[(size_t)(x-L)]){
   ++pc;
   if(prev){long long g=x-prev; maxg=max(maxg,g); __int128 lhs=(__int128)g*g*g*g*(prev+g),rhs=(__int128)16*prev*prev;
    if(lhs>rhs){if(!first)cout<<",\n";first=false;cout<<"    {\"p\": "<<prev<<", \"r\": "<<x<<", \"g\": "<<g<<"}";++dc;}}
   prev=x;
  }
 }
 cout<<"\n  ],\n  \"prime_count\": "<<pc<<",\n  \"dangerous_count\": "<<dc<<",\n  \"max_gap\": "<<maxg<<"\n}\n";
}