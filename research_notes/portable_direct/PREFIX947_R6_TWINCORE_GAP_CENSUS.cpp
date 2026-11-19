#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;using u64=uint64_t;
constexpr int L=262145,C=131072;
int main(){ifstream input("PREFIX947_W21_W23_INTERSECTION.bin",ios::binary);if(!input)throw runtime_error("missing complete intersection");
 u64 id=0,pairs=0,combo=0,multi=0,first=1,nonzero=0;
 array<u64,7>gap_combo{},gap_pair{};array<string,7>example{};
 for(;input.read((char*)&id,8);){
  int a=L+2*(id/C),b=L+2*(id%C);
  struct Witness {int i,j,t;}; vector<Witness>t1,t2;
  for(int i=0;i<=18;++i)for(int j=0;j<=18;++j){
   int d1=(21*a^(1<<j))-(1<<i), d2=(23*a^(1<<j))-(1<<i);
   if(d1>0&&d1%b==0)t1.push_back({i,j,d1/b});
   if(d2>0&&d2%b==0)t2.push_back({i,j,d2/b});
  }
  if(t1.empty()||t2.empty())throw runtime_error("witness missing for intersection member");
  if(t1.size()>1||t2.size()>1)multi++;
  bool seen[7]={};
  for(auto p:t1)for(auto q:t2){int m=q.t-p.t;
   if(m<0||m>6)throw runtime_error("t jump theorem violation");
   ++gap_combo[m];seen[m]=true;combo++; if(example[m].empty())example[m]="a="+to_string(a)+" b="+to_string(b)+" (i21,j21,t21)=("+to_string(p.i)+","+to_string(p.j)+","+to_string(p.t)+") (i23,j23,t23)=("+to_string(q.i)+","+to_string(q.j)+","+to_string(q.t)+")";
  }
  for(int m=0;m<=6;++m)if(seen[m])gap_pair[m]++;
  pairs++;
 }
 if(!input.eof())throw runtime_error("input truncated");
 if(pairs!=137274)throw runtime_error("total intersection mismatches previous full merge");
 cout<<"EXACT_TWINCORE_GAP_CENSUS pairs="<<pairs<<" witness_combinations="<<combo<<" multi_witness_pairs="<<multi<<"\n";
 for(int m=0;m<=6;++m)cout<<"gap_"<<m<<"_combinations="<<gap_combo[m]<<" gap_"<<m<<"_pairs="<<gap_pair[m]<<" example="<<example[m]<<"\n";
 cout<<"ALL_TWINCORE_GAP_ASSERTIONS_PASSED\n";
}
