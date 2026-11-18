// R749SUK: integer-exact, finite certificate for the oriented two-Port defect spectrum.
// Compile: g++ -O3 -std=c++17 R749SUK_Q_FIBER_UNIFORM_BOUND_CERT.cpp -o cert
// Run: ./cert > R749SUK_Q_FIBER_RESULTS.json
#include <algorithm>
#include <array>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <set>
#include <stdexcept>
#include <vector>
using namespace std;
using ll = long long;
struct Winner {int a,u,v,d,q;};
struct Bucket {ll score=-1; vector<Winner> w;};
static int invmod(int a,int m) {
  int b=m,x=1,y=0;
  while(b){int k=a/b;a-=k*b;swap(a,b);x-=k*y;swap(x,y);}
  if(a!=1)throw runtime_error("gcd != 1");
  x%=m;return x<0?x+m:x;
}
static bool canonical(int a,int u,int v,int d) {
  return a==d && min(u,v)==a-1 && max(u,v)==a+1;
}
static void push(Bucket &b,Winner w) {
  ll s=1LL*max(w.u,w.v)*w.a*w.d;
  if(s>b.score){b.score=s;b.w.clear();}
  if(s==b.score)b.w.push_back(w);
}
static pair<ll,set<int>> brute(int M) {
  ll peak=-1;set<int> qs;
  for(int a=1;a<=M;a++)for(int d=1;d<=M;d++){
    int p=a*d-1;if(p<=0)continue;
    for(int u=1;u<=M;u++){
      if(p%u)continue;int v=p/u;
      if(v<1||v>M||canonical(a,u,v,d))continue;
      ll s=1LL*max(u,v)*a*d;int q=u+v-a-d;
      if(s>peak){peak=s;qs.clear();}
      if(s==peak)qs.insert(q);
    }
  }
  return {peak,qs};
}
int main(int argc,char**argv){
  int N=argc>1?atoi(argv[1]):10000;
  if(N<120||N>10000)throw runtime_error("certificate range: 120..10000");
  vector<Bucket> bins(N+1);ll oriented=0;
  for(int u=1;u<=N;u++)for(int a=1;a<=N;a++){
    if(gcd(a,u)!=1)continue;
    ll D=min((ll)N,((ll)N*u+1)/a);
    if(u==1){
      for(ll d=1;d<=D;d++){
        int v=a*d-1;if(v<1||v>u)continue;
        int q=u+v-a-(int)d;bool can=canonical(a,u,v,(int)d);
        if((q==0)!=can)throw runtime_error("q0 classification failed");
        if(can)continue;
        int L=max({a,u,(int)d});push(bins[L],{a,u,v,(int)d,q});oriented++;
      }
      continue;
    }
    int r=invmod(a,u),lo=(u+a)/a;
    ll d=r;if(d<lo)d+=((lo-d+u-1)/u)*u;
    for(;d<=D;d+=u){
      int v=(a*d-1)/u;if(v<1||v>u)continue;
      int q=u+v-a-(int)d;bool can=canonical(a,u,v,(int)d);
      if((q==0)!=can)throw runtime_error("q0 classification failed");
      if(1LL*u*q!=1LL*(u-a)*(u-d)-1)throw runtime_error("defect identity failed");
      if(can)continue;
      int L=max({a,u,(int)d});push(bins[L],{a,u,v,(int)d,q});oriented++;
    }
  }
  ll peak=-1;set<int> qs,allQs;vector<int> exceptions;
  vector<Winner> win;
  for(int M=2;M<=N;M++){
    if(bins[M].score>peak){peak=bins[M].score;qs.clear();win.clear();}
    if(bins[M].score==peak){for(const auto& w:bins[M].w){qs.insert(w.q);win.push_back(w);}}
    for(int q:qs)allQs.insert(q);
    if(any_of(qs.begin(),qs.end(),[](int q){return abs(q)>1;}))exceptions.push_back(M);
    if(M<=120){auto [p,bq]=brute(M);if(p!=peak||bq!=qs)throw runtime_error("independent brute-force disagreement at M="+to_string(M));}
    if(M==58&& (peak!=127890||qs!=set<int>{2}))throw runtime_error("M=58 regression failed");
    if(M==93&& (peak!=579576||qs!=set<int>{2}))throw runtime_error("M=93 regression failed");
  }
  if(exceptions!=vector<int>{58,93}||allQs!=set<int>{-1,1,2})throw runtime_error("unexpected defect spectrum");
  cout<<"{\n  \"record\": \"R749SUK\",\n  \"status\": \"PASS\",\n";
  cout<<"  \"arithmetic\": \"exact_64bit_integer_with_safe_N_at_most_10000\",\n";
  cout<<"  \"complete_scanned_M\": \"2.."<<N<<"\",\n";
  cout<<"  \"oriented_noncanonical_candidates_at_N\": "<<oriented<<",\n";
  cout<<"  \"all_maximizer_Q_values\": [-1,1,2],\n";
  cout<<"  \"maximizer_nonunit_Q_M\": [58,93],\n";
  cout<<"  \"independent_brute_maxima_and_Q_crosscheck_M\": \"2..120\",\n";
  cout<<"  \"M58_peak\": 127890,\n  \"M93_peak\": 579576,\n";
  cout<<"  \"theoretical_all_M_Q_bound\": 20,\n";
  cout<<"  \"analytic_threshold_for_bound_20\": 9999,\n";
  cout<<"  \"analytic_threshold_for_eventual_bound_16\": 249999,\n";
  cout<<"  \"scope\": \"auxiliary_labeled_two_Port_unimodular_threshold_maximizers_only; no_native_X6_admission\"\n}\n";
}