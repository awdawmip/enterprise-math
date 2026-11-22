// Exact finite certificate for cancellation of all 17^2 denominator terms
// in any T6 shape-moment collision of side mass <=2331.
// Scientific contributor: RESEARCH_DRIVER EM-DVR-DEBB5E; no native Result admission.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <tuple>
#include <vector>
using Profile = std::array<int,8>;
using Sig = std::array<int,3>;
int main() {
  constexpr int mass_limit=2331, p=17;
  std::array<int,8> weights{}, inverse{};
  for (int j=1;j<=8;j++) {
    weights[j-1]=289*j-1;
    for(int x=1;x<p;x++) if ((x*j)%p==1) inverse[j-1]=x;
    assert(inverse[j-1]>0);
  }
  std::vector<Profile> profiles;
  Profile m{};
  auto enumerate=[&](auto&& self,int j,int cost)->void {
    if(j==8){profiles.push_back(m);return;}
    for(int cnt=0;cost+cnt*weights[j]<=mass_limit;cnt++) {
      m[j]=cnt;
      self(self,j+1,cost+cnt*weights[j]);
    }
    m[j]=0;
  };
  enumerate(enumerate,0,0);
  assert(profiles.size()==67);
  std::map<std::tuple<int>,int> one;
  std::map<std::tuple<int,int>,int> two;
  std::map<std::tuple<int,int,int>,int> three;
  for(const auto& v:profiles){
    Sig s{};
    for (int j=0;j<8;j++) {
      int t=1;
      for(int k=0;k<3;k++) {
        t=(t*inverse[j])%p;
        s[k]=(s[k]+v[j]*t)%p;
      }
    }
    one[{s[0]}]++;
    two[{s[0],s[1]}]++;
    three[{s[0],s[1],s[2]}]++;
  }
  int one_pairs=0,two_pairs=0,three_pairs=0;
  for(const auto& [s,c]:one)one_pairs+=c*(c-1)/2;
  for(const auto& [s,c]:two)two_pairs+=c*(c-1)/2;
  for(const auto& [s,c]:three)three_pairs+=c*(c-1)/2;
  assert(one.size()==17 && one_pairs==101);
  assert(two.size()==63 && two_pairs==4);
  assert(three.size()==67 && three_pairs==0);
  // Independent scalar generating-function count of feasible profiles.
  std::vector<std::int64_t> dp(mass_limit+1);
  dp[0]=1;
  for (int w:weights) for(int t=w;t<=mass_limit;t++) dp[t]+=dp[t-w];
  std::int64_t dp_total=0;for(auto x:dp)dp_total+=x;
  assert(dp_total==67);
  std::cout<<"p=17; mass_limit="<<mass_limit
           <<"; profiles="<<profiles.size()<<"; dp_profiles="<<dp_total<<"\n"
           <<"k1_signatures="<<one.size()<<"; k1_colliding_pairs="<<one_pairs<<"\n"
           <<"k12_signatures="<<two.size()<<"; k12_colliding_pairs="<<two_pairs<<"\n"
           <<"k123_signatures="<<three.size()<<"; k123_colliding_pairs="<<three_pairs<<"\n";
}
