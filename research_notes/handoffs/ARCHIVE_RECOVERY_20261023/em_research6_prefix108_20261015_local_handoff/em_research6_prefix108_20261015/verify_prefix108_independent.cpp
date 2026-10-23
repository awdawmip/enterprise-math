// Independent C++17 integer-check of PREFIX-108 a=3 local fifth-to-sixth flow.
// Uses eight typed elementary ports, 36 unordered pairs, integer compositions.
// No source-level dependency on Python checker or previous certificate.
#include <array>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <cassert>
#include <cstdint>
using namespace std;
struct Pair {int i,j;};
struct Row {array<int,36> m{}; uint64_t mask=0;};
static vector<Pair> pairs;
static array<int,8> needs[6];
static int count_in[6]={3,13,16,3,13,16};
static vector<Row> outcomes[6];
// indices: 0Z,0O,0I,0U,1Z,1O,1I,1U.
void recurse_row(int r,int pid,array<int,8> rem,int remaining, Row state){
  if(pid==36){
    if(remaining!=0)return;
    for(auto v:rem)if(v!=0)return;
    outcomes[r].push_back(state); return;
  }
  const auto q=pairs[pid];
  int cap=remaining;
  if(q.i==q.j)cap=min(cap,rem[q.i]/2);
  else cap=min(cap,min(rem[q.i],rem[q.j]));
  for(int x=0;x<=cap;++x){
    auto nxt=rem; Row row=state;
    nxt[q.i]-=x; nxt[q.j]-=x;
    row.m[pid]=x;
    if(x)row.mask |= (uint64_t(1)<<pid);
    recurse_row(r,pid+1,nxt,remaining-x,row);
  }
}
int popcnt(uint64_t x){return __builtin_popcountll(x);}
struct Counts{long long total=0;long long seven=0;long long with_x=0;map<int,long long>by_size;set<uint64_t>seven_masks;};
void recurse_all(int row,uint64_t mask,vector<Row> const&selected,Counts&ret){
 if(row==6){
   int n=popcnt(mask);++ret.total;++ret.by_size[n];
   if(n==7){
     ++ret.seven;ret.seven_masks.insert(mask);
     int xID=-1,rID=-1;for(int i=0;i<36;++i){
       if(pairs[i].i==4&&pairs[i].j==4)xID=i;  // 1Z + 1Z
       if(pairs[i].i==5&&pairs[i].j==5)rID=i;  // 1O + 1O
     }
     assert(xID>=0&&rID>=0);
     if(mask&(uint64_t(1)<<xID)){
       ++ret.with_x;
       assert(selected[5].m[xID]==4&&selected[5].m[rID]==12);
       assert(selected[1].m[xID]==2&&selected[1].m[rID]==10);
     }else{
       assert(selected[5].m[rID]==8);
     }
   }
   return;
 }
 for(auto const&v:outcomes[row]){
   auto picks=selected;picks.push_back(v);
   recurse_all(row+1,mask|v.mask,picks,ret);
 }
}
void fill(int b){
 for(auto &a:needs)a.fill(0);
 needs[0][0]=1;needs[0][6]=2+b;needs[0][7]=3-b;
 needs[1][2]=1-b;needs[1][3]=b;needs[1][5]=21;needs[1][4]=4;
 needs[2][6]=32;
 needs[3][2]=1;needs[3][5]=5;
 needs[4][1]=1;needs[4][6]=25;
 needs[5][5]=24;needs[5][4]=8;
 for(int r=0;r<6;++r){
  int sum=0;for(int j:needs[r])sum+=j;
  assert(sum==2*count_in[r]);outcomes[r].clear();
  recurse_row(r,0,needs[r],count_in[r],Row{});
  assert(!outcomes[r].empty());
 }
}
int main(){
 for(int i=0;i<8;++i)for(int j=i;j<8;++j)pairs.push_back({i,j});
 assert(pairs.size()==36);
 long long seven_total=0,x_total=0;
 for(int b=0;b<=1;++b){
    fill(b);Counts ans;recurse_all(0,0,vector<Row>{},ans);
    assert(ans.total==75);
    if(b==0){assert(ans.by_size.at(7)==4&&ans.by_size.at(8)==30&&ans.by_size.at(9)==32&&ans.by_size.at(10)==9);assert(ans.with_x==2);}
    if(b==1){assert(ans.by_size.count(7)==0&&ans.by_size.at(8)==9&&ans.by_size.at(9)==66);}
    seven_total+=ans.seven;x_total+=ans.with_x;
    cout<<"b="<<b<<" total="<<ans.total<<" min="<<ans.by_size.begin()->first<<" sizes:";
    for(auto [n,k]:ans.by_size)cout<<" "<<n<<":"<<k;
    cout<<" seven="<<ans.seven<<" seven_X="<<ans.with_x<<" distinct7="<<ans.seven_masks.size()<<"\n";
 }
 assert(seven_total==4&&x_total==2);
 cout<<"PREFIX108 C++17 INDEPENDENT EXACT PASS\n";
}
