// R749SUL: exact integer certificate for forced positive unit Q windows.
// C++17: g++ -O2 -std=c++17 R749SUL_NEAR_SQUARE_Q_CERT.cpp -o cert && ./cert
#include <algorithm>
#include <cmath>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
using i64=long long;
struct Bucket {i64 best=-1;set<int> q;};
static void add(Bucket &b,i64 score,int q){
  if(score>b.best){b.best=score;b.q.clear();}
  if(score==b.best)b.q.insert(q);
}
static i64 gcd_ext(i64 a,i64 b,i64 &x,i64 &y){
  if(b==0){x=1;y=0;return a;}
  i64 p,z;auto g=gcd_ext(b,a%b,p,z);x=z;y=p-(a/b)*z;return g;
}
int main(){
  constexpr int N=5000;
  vector<Bucket> at(N+1);
  add(at[2],2,-1); // u=v=1 and (a,d)=(1,2), modulo swapping a,d
  i64 oriented=2; // the two u=1 configurations
  for(int u=2;u<=N;++u){
    for(int a=1;a<=N;++a){
      i64 x,y;
      if(gcd_ext(a,u,x,y)!=1)continue;
      int d0=int((x%u+u)%u);if(d0==0)d0=u;
      int dmax=int(min<i64>(N,((i64)u*u+1)/a));
      for(int d=d0;d<=dmax;d+=u){
        i64 z=((i64)a*d-1)/u;
        if(z<1||z>u)continue;
        ++oriented;
        if(a==d&&abs(u-z)==2)continue; // exactly Q=0 canonical
        int L=max({u,a,d,int(z)});
        add(at[L],(i64)u*a*d,int(u+z-a-d));
      }
    }
  }
  Bucket prefix;
  int checked=0,levels=0;
  bool pass=true;
  vector<int> samples={58,93,1023,1027,1599,1604,4095,4103,4899,4907};
  cout<<"{\"model\":\"positive_determinant_one_oriented_noncanonical\",\"max_entry\":"<<N;
  cout<<",\"oriented_candidates_including_canonical\":"<<oriented<<",\"samples\":[";
  bool first=true;
  for(int M=2;M<=N;++M){
    if(at[M].best>prefix.best)prefix=at[M];
    else if(at[M].best==prefix.best)prefix.q.insert(at[M].q.begin(),at[M].q.end());
    int t=int(sqrt((double)M+1));while((t+1)*(t+1)<=M+1)++t;while(t*t>M+1)--t;
    if(t>=32 && M>=t*t-1 && M<=t*t-1+t/8){
      ++checked;
      if(M==t*t-1)++levels;
      if(prefix.q!=set<int>{1})pass=false;
    }
    if(find(samples.begin(),samples.end(),M)!=samples.end()){
      if(!first)cout<<",";first=false;
      cout<<"{\"M\":"<<M<<",\"tau\":"<<prefix.best<<",\"q\":[";
      bool f=true;for(int q:prefix.q){if(!f)cout<<",";f=false;cout<<q;}
      cout<<"]}";
    }
  }
  cout<<"],\"near_square_t_min\":32,\"near_square_t_max\":70";
  cout<<",\"checked_window_scales\":"<<checked<<",\"checked_window_levels\":"<<levels;
  cout<<",\"all_window_maximizers_q_equals_1\":"<<(pass?"true":"false")<<"}\n";
  return pass?0:1;
}
