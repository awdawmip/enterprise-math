#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
using ll=long long;
constexpr ll L=262145,H=524287,CN=131072,K=21,K2=23;
struct S {int i,j,sgn,c;};
int main(){
 vector<S> first,second;
 for(int i=0;i<=18;i++)for(int j=0;j<=18;j++)for(int s : {-1,1}){
  int c=(1<<i)-s*(1<<j);
  first.push_back({i,j,s,c}); second.push_back({i,j,s,c});
 }
 vector<int64_t> ids, resonance_ids, nonres_ids;
 unsigned long long candidates=0, nonres_witnesses=0, res_pattern_compatible=0, res_witnesses=0;
 int nonzero_res_patterns=0;
 unsigned long long gap_witnesses[7]={};
 vector<int64_t> gap_ids[7];
 // D=0: 2*t=21*m, t<=42, T<=46 => only (t,m)=(21,2),(42,4).
 for(int t=1;t<=42;t++)for(int m=0;m<=6;m++){
  int T=t+m;if(T>46)continue;
  ll d=2LL*t-K*m;
  if(d==0){
   for(const auto &u:first)for(const auto &v:second){
    if(K*v.c != K2*u.c)continue;
    res_pattern_compatible++;
    if(u.c!=0) nonzero_res_patterns++;
    if(u.c%K) continue;
    ll r=t/K, h=u.c/K;
    // full Q candidate b, exact bit sign checks
    for(ll b=L;b<=H;b+=2){
     ll a=r*b+h;
     if(a<L||a>H||(a&1)==0)continue;
     ll ka=K*a,k2a=K2*a;
     if(((ka>>u.j)&1)!=(u.sgn<0))continue;
     if(((k2a>>v.j)&1)!=(v.sgn<0))continue;
     assert((ka^(1LL<<u.j))-(1LL<<u.i)==t*b);
     assert((k2a^(1LL<<v.j))-(1LL<<v.i)==T*b);
     res_witnesses++;
     resonance_ids.push_back(((a-L)/2)*CN+(b-L)/2);
    }
   }
   continue;
  }
  for(const auto &u:first){
   for(const auto &v:second){
    candidates++;
    ll num_a=ll(t)*v.c-ll(T)*u.c;
    if(num_a%d)continue;
    ll a=num_a/d;
    if(a<L||a>H||(a&1)==0) continue;
    ll num_b=K*v.c-K2*u.c;
    if(num_b%d)continue;
    ll b=num_b/d;
    if(b<L||b>H||(b&1)==0) continue;
    ll ka=K*a,k2a=K2*a;
    if(((ka>>u.j)&1)!=(u.sgn<0))continue;
    if(((k2a>>v.j)&1)!=(v.sgn<0))continue;
    assert((ka^(1LL<<u.j))-(1LL<<u.i)==t*b);
    assert((k2a^(1LL<<v.j))-(1LL<<v.i)==T*b);
    nonres_witnesses++;
    gap_witnesses[m]++;
    gap_ids[m].push_back(((a-L)/2)*CN+(b-L)/2);
    nonres_ids.push_back(((a-L)/2)*CN+(b-L)/2);
   }
  }
 }
 auto unique_sort=[](vector<int64_t> &v){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());};
 unique_sort(resonance_ids);unique_sort(nonres_ids);for(auto &v:gap_ids)unique_sort(v);
 set_union(resonance_ids.begin(),resonance_ids.end(),nonres_ids.begin(),nonres_ids.end(),back_inserter(ids));
 long long nondiag=0, diagonal=0, overlap_res_nonres=0;
 for(auto id:ids){ if(id/CN==id%CN)diagonal++;else nondiag++; }
 for(auto id:nonres_ids)if(binary_search(resonance_ids.begin(),resonance_ids.end(),id))overlap_res_nonres++;
 ofstream out("PREFIX948_W21_W23_INTERSECTION_IDS.bin",ios::binary);
 for(auto id:ids){uint64_t x=(uint64_t)id;out.write(reinterpret_cast<const char*>(&x),8);}
 out.close();
 cout<<"{\"schema\":\"PREFIX948_R6_DETERMINANT_INDEPENDENT_INTERSECTION_V1\",\"source_k\":21,\"target_k\":23,\"range\":[262145,524287],\"source_bits\":[0,18],\"t_max\":42,\"T_max\":46,\"m_range\":[0,6],\"nonres_candidates_examined\":"<<candidates<<",\"nonres_valid_witness_patterns\":"<<nonres_witnesses<<",\"nonres_unique_pairs\":"<<nonres_ids.size()<<",\"res_compatible_patterns\":"<<res_pattern_compatible<<",\"res_nonzero_patterns\":"<<nonzero_res_patterns<<",\"res_valid_witness_patterns\":"<<res_witnesses<<",\"res_unique_pairs\":"<<resonance_ids.size()<<",\"both_subsets_pair_overlap\":"<<overlap_res_nonres<<",\"distinct_diagonal\":"<<diagonal<<",\"distinct_offdiagonal\":"<<nondiag<<",\"intersection_unique_pairs\":"<<ids.size()<<",\"computed_full_domain\":true,\"nonres_gap_witnesses\":[";
 for(int m=0;m<=6;m++){if(m)cout<<",";cout<<gap_witnesses[m];}
 cout<<"],\"nonres_gap_unique_pairs\":[";
 for(int m=0;m<=6;m++){if(m)cout<<",";cout<<gap_ids[m].size();}
 cout<<"],\"nonres_diagonal_ids\":[";
 bool firstd=true;
 for(auto id:nonres_ids)if(id/CN==id%CN){if(!firstd)cout<<",";firstd=false;cout<<(L+2*(id/CN));}
 cout<<"]}"<<endl;
}
