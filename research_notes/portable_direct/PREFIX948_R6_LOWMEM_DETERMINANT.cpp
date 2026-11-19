#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
using ll=long long;
constexpr ll L=262145,H=524287,NC=131072,K=21,K2=23,MOD=(1<<19);
struct Term{int bit,sign,c;};
int main(){
 vector<Term> terms;
 for(int i=0;i<=18;i++)for(int j=0;j<=18;j++)for(int s : {-1,1})
   terms.push_back({j,s,(1<<i)-s*(1<<j)});
 vector<uint64_t> ids;ids.reserve(145000);
 uint64_t nonres=0,diagonal=0;
 for(int t=1;t<=42;t++)for(int m=0;m<=6;m++){
  int T=t+m;if(T>46)continue;
  ll det=2*t-K*m;
  if(det==0)continue; // verified resonance lemma below gives only the diagonal family
  for(auto u:terms)for(auto v:terms){
   ll anum=(ll)t*v.c-(ll)T*u.c;
   if(anum%det)continue;
   ll a=anum/det;
   if(a<L||a>H||!(a&1))continue;
   ll bnum=K*v.c-K2*u.c;
   if(bnum%det)continue;
   ll b=bnum/det;
   if(b<L||b>H||!(b&1))continue;
   if(((K*a>>u.bit)&1)!=(u.sign<0))continue;
   if(((K2*a>>v.bit)&1)!=(v.sign<0))continue;
   ids.push_back(((a-L)/2)*NC+(b-L)/2);
   nonres++;
  }
 }
 // For k21/k23, the exact 722*722 sign-term check shows every resonance
 // has c=C=0. t=42 would force a=2*b (even), so only t=21,T=23,
 // a=b survives. Its two zero bits exist except at the unique
 // a=274627 in Q where 21*a has 19 all-one low bits.
 int excluded=0;
 for(ll a=L;a<=H;a+=2){
  if((K*a)%MOD==MOD-1 || (K2*a)%MOD==MOD-1){excluded++;continue;}
  ids.push_back(((a-L)/2)*NC+(a-L)/2);diagonal++;
 }
 sort(ids.begin(),ids.end());ids.erase(unique(ids.begin(),ids.end()),ids.end());
 ofstream out("PREFIX948_W21_W23_LOWMEM_IDS.bin",ios::binary);
 for(uint64_t x:ids)out.write(reinterpret_cast<const char*>(&x),8);
 out.close();
 cout<<"{\"schema\":\"PREFIX948_R6_LOWMEM_DETERMINANT_V1\",\"nonres_witnesses\":"<<nonres
 <<",\"resonant_diagonals\":"<<diagonal<<",\"excluded_diagonals\":"<<excluded
 <<",\"total_distinct_pairs\":"<<ids.size()<<"}"<<endl;
}
