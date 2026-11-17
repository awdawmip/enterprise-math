// PREFIX-864 exact fixed ordered odd-modulus full-transition optimization.
// C++17: g++ -O3 -std=c++17 PREFIX864_R6_EXACT_ODD_TRANSITION_OPTIMIZER.cpp -o prefix864 && ./prefix864
// Inputs are exhaustive within the specified peak-width bound, not samples.
#include <algorithm>
#include <iostream>
#include <numeric>
#include <set>
#include <utility>
#include <vector>
using namespace std;
struct Result { int p, B, tested, survivors; vector<pair<int,int>> first; };

// Exact injectivity: every old/new ordered legal transition has a distinct transcript.
static bool direct_verify(int p, int q1, int q2) {
  int N=1<<p;
  set<pair<int,int>> seen;
  for (int u=0; u<N; ++u) {
    for (int j=-1; j<p; ++j) {
      int v = j<0 ? u : (u^(1<<j));
      if (!seen.insert({u%q1, v%q2}).second) return false;
    }
  }
  return int(seen.size())==N*(p+1);
}

// For each old-residue bucket r, enumerate the multiset of legal new states v.
// Equal v values in the same bucket are an irreparable collision.
// Otherwise q2 is forbidden exactly when it divides a positive pair difference.
// Every odd divisor q2<=2^B-1 of every possible difference is preindexed.
static Result scan(int p, int B) {
  int N=1<<p, T=N*(p+1), limit=(1<<B)-1;
  vector<vector<int>> odd_divisors(N);
  for (int q=3;q<=limit;q+=2)
    for (int d=q;d<N;d+=q) odd_divisors[d].push_back(q);
  int survivors=0;
  vector<pair<int,int>> first;
  for (int q1=3;q1<=limit;q1+=2) {
    if (T>q1*limit) continue; // exact pigeonhole obstruction
    vector<unsigned char> forbidden(limit+1,0);
    int live=(limit-1)/2;
    bool repeated=false;
    for (int r=0;r<q1 && live>0;++r) {
      vector<int> next;
      for (int u=r;u<N;u+=q1) {
        next.push_back(u);
        for(int i=0;i<p;++i) next.push_back(u^(1<<i));
      }
      sort(next.begin(),next.end());
      if(adjacent_find(next.begin(),next.end())!=next.end()) {repeated=true; break;}
      for (int i=0;i<int(next.size()) && live>0;++i)
        for (int j=i+1;j<int(next.size()) && live>0;++j)
          for (int q2:odd_divisors[next[j]-next[i]])
            if(!forbidden[q2]) {forbidden[q2]=1; --live;}
    }
    if (repeated) continue;
    for(int q2=3;q2<=limit;q2+=2) if(!forbidden[q2]) {
      ++survivors;
      if (int(first.size())<8) first.push_back({q1,q2});
    }
  }
  return {p,B,((limit-1)/2)*((limit-1)/2),survivors,first};
}

static int half_period(int g) {
  int x=2%g;
  for(int d=1;d<=g;++d) {
    if(x==1||x==g-1) return d;
    x=(x*2)%g;
  }
  return -1;
}
static int width(int q) {int b=0;for(int x=q;x;x>>=1)++b;return b;}
int main(){
  const vector<pair<int,int>> probes={{10,7},{10,8},{11,8},{12,8},{12,9},{13,9},{14,9},{15,10}};
  const vector<int> expected={0,56,2,0,54,0,0,0};
  struct CRT {int p,g,a,b,B;};
  const vector<CRT> crt={
    {10,23,5,9,8},{11,23,9,11,8},{12,29,9,17,9},
    {13,29,9,35,10},{14,29,17,35,10},{15,37,17,53,11},
    {16,37,35,51,11},{18,37,65,109,12}};
  vector<Result> all;
  for (int k=0;k<int(probes.size());++k) {
    auto [p,B]=probes[k]; Result r=scan(p,B);
    if(r.survivors!=expected[k]) {cerr<<"MISMATCH p="<<p<<", B="<<B<<"\n";return 1;}
    all.push_back(r);
  }
  for(auto c:crt) {
    int q1=c.g*c.a,q2=c.g*c.b;
    if(half_period(c.g)<c.p || gcd(c.a,c.b)!=1 ||
       1LL*c.g*c.a*c.b < (1LL<<c.p) ||
       max(width(q1),width(q2))!=c.B) {
      cerr<<"CRT CONDITION FAIL at p="<<c.p<<"\n"; return 2;
    }
  }
  if(!direct_verify(10,115,207) || !direct_verify(11,207,253) || !direct_verify(12,261,493)){
    cerr<<"DIRECT WITNESS COLLISION\n"; return 3;
  }
  cout<<"{\"schema\":\"PREFIX864_EXACT_ODD_TWO_READ_V2\",\"status\":\"ALL_EXACT_ASSERTIONS_PASSED\",\"scans\":[";
  for(size_t i=0;i<all.size();++i){
    auto &r=all[i]; if(i)cout<<",";
    cout<<"{\"p\":"<<r.p<<",\"B\":"<<r.B<<",\"candidate_pairs\":"<<r.tested<<",\"injective_pairs\":"<<r.survivors<<",\"first_pairs\":[";
    for(size_t j=0;j<r.first.size();++j){if(j)cout<<",";cout<<"["<<r.first[j].first<<","<<r.first[j].second<<"]";}
    cout<<"]}";
  }
  cout<<"],\"crt_witnesses\":[";
  for(size_t i=0;i<crt.size();++i){auto c=crt[i];if(i)cout<<",";
    cout<<"{\"p\":"<<c.p<<",\"g\":"<<c.g<<",\"h_g\":"<<half_period(c.g)
        <<",\"a\":"<<c.a<<",\"b\":"<<c.b<<",\"q1\":"<<c.g*c.a
        <<",\"q2\":"<<c.g*c.b<<",\"lcm\":"<<1LL*c.g*c.a*c.b
        <<",\"peak_B\":"<<c.B<<"}";
  }
  cout<<"],\"optima\":[{\"p\":10,\"B\":8},{\"p\":11,\"B\":8},{\"p\":12,\"B\":9},{\"p\":13,\"B\":10},{\"p\":14,\"B\":10},{\"p\":15,\"B\":11},{\"p\":16,\"B\":11},{\"p\":18,\"B\":12}]}\n";
}
