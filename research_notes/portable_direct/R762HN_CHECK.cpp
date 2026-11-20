// R762HN: exact repeated-loop positive BRC counts and lattice certificates.
// g++ -O3 -std=c++17 -Wall -Wextra -pedantic R762HN_CHECK.cpp -o r762hn && ./r762hn
#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
using i64=long long;
using u64=uint64_t;
static constexpr u64 ORIGIN=0x808080808080ULL;
using Mat6=array<array<i64,6>,6>;

// Fraction-free Bareiss determinant, exact here (intermediates small).
i64 det6(Mat6 a){
 i64 sign=1,prev=1;
 for(int k=0;k<5;k++){
  if(a[k][k]==0){int j=k+1;while(j<6 && a[j][k]==0)++j;
   if(j==6)return 0;
   swap(a[j],a[k]);sign=-sign;}
  i64 pivot=a[k][k];
  for(int i=k+1;i<6;i++)for(int j=k+1;j<6;j++)
   a[i][j]=(a[i][j]*pivot-a[i][k]*a[k][j])/prev;
  for(int i=k+1;i<6;i++)a[i][k]=0;
  prev=pivot;
 }
 return sign*a[5][5];
}

int main(){
 vector<string> ports={"01","15","12","25","24","04","05","03","04","24","23","25","35","05","01"};
 array<array<int,6>,14> h{};
 array<u64,14> add{};
 for(int t=0;t<14;t++){
  int a=0,b=0;
  for(char ch:ports[t])a|=1<<(ch-'0');
  for(char ch:ports[t+1])b|=1<<(ch-'0');
  if(__builtin_popcount(unsigned(a&b))!=1 || __builtin_popcount(unsigned(a|b))!=3) return 10;
  for(int j=0;j<6;j++)if((a|b)&(1<<j)){h[t][j]=1;add[t]|=1ULL<<(j*8);}
 }
 Mat6 C{};
 for(int i=0;i<6;i++)for(int j=0;j<6;j++)for(int t=0;t<14;t++)C[i][j]+=h[t][i]*h[t][j];
 if(det6(C)!=3456){cerr<<"wrong covariance determinant\n";return 11;}
 int cols[6]={0,1,3,4,6,7};Mat6 minor{};
 for(int i=0;i<6;i++)for(int j=0;j<6;j++)minor[i][j]=h[cols[j]][i];
 if(det6(minor)!=-3){cerr<<"wrong lattice minor\n";return 12;}
 cout<<"lattice_index=3 covariance_det=3456 minor_det=-3\n";
 unordered_map<u64,u64> states,next;
 states[ORIGIN]=1;states.reserve(3000000);next.reserve(3000000);
 const u64 expected_z2=313080ULL,expected_z4=12464855922680ULL;
 u64 gram14=0,gram28=0,z2=0,z4=0;
 for(int t=0;t<56;t++){
  u64 delta=add[t%14];next.clear();
  for(const auto &kv:states){next[kv.first+delta]+=kv.second;next[kv.first-delta]+=kv.second;}
  states.swap(next);
  if(t==13||t==27){
   __uint128_t gram=0;for(const auto &kv:states)gram+=(__uint128_t)kv.second*kv.second;
   if(t==13)gram14=(u64)gram; else gram28=(u64)gram;
  }
  if(t==27)z2=states.at(ORIGIN);
  if(t==55)z4=states.at(ORIGIN);
 }
 cout<<"Z2_direct="<<z2<<" Z2_gram="<<gram14<<"\n";
 cout<<"Z4_direct="<<z4<<" Z4_gram="<<gram28<<"\n";
 cout<<"k4_terminal_states="<<states.size()<<"\n";
 if(z2!=expected_z2||z2!=gram14||z4!=expected_z4||z4!=gram28)return 13;
 cout<<"PASS\n";
}
