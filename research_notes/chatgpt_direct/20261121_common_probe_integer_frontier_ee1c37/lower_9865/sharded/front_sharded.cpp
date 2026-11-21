#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <bit>
#include <map>
#include <set>
#include <string>
#include <tuple>
using namespace std;
using M=__uint128_t;
const M FULL=(M(1)<<125)-1;
int pos(M b){return (uint64_t)b?__builtin_ctzll((uint64_t)b):64+__builtin_ctzll((uint64_t)(b>>64));}
struct Type{int sz,price;vector<M> all,reps;};
vector<Type> types;
using Pools=vector<vector<M>>;
uint64_t nodes;
vector<M> solution;
M slices[15];
vector<array<int,15>> abs_lo,abs_hi;
#include "marginals.hpp"
#include "exact_margins.hpp"
bool solve(M free,int left,vector<int>&cnt,const Pools&pool){
 ++nodes;if(!exact_margins(free,cnt))return false;
 for(int e=0;e<15;++e){
   int lo=0,hi=0;
   for(int j=0;j<cnt.size();j++)if(cnt[j]) {lo+=cnt[j]*abs_lo[j][e];hi+=cnt[j]*abs_hi[j][e];}
   M m=free&slices[e];
   int v=popcount(uint64_t(m))+popcount(uint64_t(m>>64));
   if(v<lo||v>hi)return false;
 }
 int choice=-1,best=2147483647;vector<int> count(cnt.size());
 for(int j=0;j<cnt.size();j++)if(cnt[j]){
   int n=0;for(M m:pool[j])if((m&free)==m)++n;
   if(n<cnt[j])return false;
   if(n<best){best=n;choice=j;}count[j]=n;
 }
 if(left==1){if(choice>=0&&count[choice]){solution.push_back(free);return true;}return false;}
 if(choice<0)return !free;
 Pools options(cnt.size());M united=0;
 for(int j=0;j<cnt.size();j++)if(cnt[j]){
  auto& dest=options[j];dest.reserve(count[j]);
  for(M m:pool[j])if((m&free)==m){dest.push_back(m);united|=m;}
 }
 if(united!=free)return false;
 int pivot=-1;
 if(best>10){
   array<int,125>freq{};for(int j=0;j<cnt.size();j++)if(cnt[j])for(M m:options[j])for(M q=m;q;q&=q-1)++freq[pos(q)];
   for(M q=free;q;q&=q-1)if(freq[pos(q)]<best){best=freq[pos(q)];pivot=pos(q);choice=-1;}
 }
 for(int j=0;j<cnt.size();j++)if(cnt[j]&&(choice<0||choice==j)){
   --cnt[j];for(int q=0;q<125;q++)bound_at[left-1][q]=bound_at[left][q]-level_bound[0][j][q];
   auto all=std::move(options[j]);
   if(choice>=0&&cnt[j]){
     for(int i=0;i+cnt[j]<all.size();i++){
       options[j].assign(all.begin()+i+1,all.end());
       if(solve(free^all[i],left-1,cnt,options)){solution.push_back(all[i]);return true;}
     }
   }else{
     if(cnt[j])options[j]=all;
     for(M m:all)if((pivot<0||((m>>pivot)&1))&&solve(free^m,left-1,cnt,options)){solution.push_back(m);return true;}
   }
   options[j]=std::move(all);++cnt[j];
 }
 return false;
}

using Action=array<unsigned char,125>;
vector<Action> affine_actions;
bool root_symmetry=false;
M image(M mask,const Action& a){M result=0;for(M v=mask;v;v&=v-1)result|=M(1)<<a[pos(v)];return result;}
void init_actions(const string& root){
 ifstream f(root+"/linear");vector<Action> lin(96);for(auto&a:lin)for(auto&v:a){int x;f>>x;v=x;}
 for(const auto&a:lin)for(int d=0;d<125;d++){Action result;
  for(int i=0;i<125;i++){int j=a[i];result[i]=25*((j/25+d/25)%5)+5*((j/5%5+d/5%5)%5)+(j%5+d%5)%5;}
  affine_actions.push_back(result);
 }
}
bool normalized_solve(M free,int left,vector<int>&cnt,const Pools&pool){
 if(!root_symmetry)return solve(free,left,cnt,pool);
 M holes=FULL^free;
 if((popcount(uint64_t(holes))+popcount(uint64_t(holes>>64)))>26)return solve(free,left,cnt,pool);
 if(!exact_margins(free,cnt))return false;
 vector<const Action*> stab;for(const auto& a:affine_actions)if(image(holes,a)==holes)stab.push_back(&a);
 int j=-1;Pools filtered(cnt.size());
 for(int i=0;i<cnt.size();i++)if(cnt[i]){
  for(M m:pool[i])if((m&free)==m)filtered[i].push_back(m);
  if(filtered[i].size()<cnt[i])return false;
  if(j<0||filtered[i].size()<filtered[j].size())j=i;
 }
 if(j<0)return free==0;
 if(stab.size()<=1)return solve(free,left,cnt,filtered);
 vector<M> representatives,orbit_minimum;
 for(M m:filtered[j]){M minimum=m;for(const auto*a:stab)minimum=min(minimum,image(m,*a));orbit_minimum.push_back(minimum);if(minimum==m)representatives.push_back(m);}
 
 ++nodes;--cnt[j];
 auto all=move(filtered[j]);
 for(M m:representatives){
  filtered[j].clear();if(cnt[j])for(int z=0;z<all.size();z++)if(all[z]>m&&orbit_minimum[z]>=m)filtered[j].push_back(all[z]);
  if(solve(free^m,left-1,cnt,filtered)){solution.push_back(m);++cnt[j];return true;}
 }
 ++cnt[j];return false;
}

long long geometric_nodes,leaf_nodes;
bool add_big(M free,int left,int punct,int start,vector<int>&cnt,const Pools&pool,const vector<M>&large){
 ++geometric_nodes;
 if(!exact_margins(free,cnt))return false;
 if(punct<0||cnt[punct]==0){++leaf_nodes;return normalized_solve(free,left,cnt,pool);}
 int num=cnt[punct]--;for(int j=start;j+num<=large.size();j++){M m=large[j];if(m&~free)continue;
 if(add_big(free^m,left-1,punct,j+1,cnt,pool,large)){solution.push_back(m);return true;}}
 ++cnt[punct];return false;
}

bool finish_witness(M free,vector<int>&rem){
 int chosen=-1,best=2147483647;
 for(int j=0;j<types.size();j++)if(rem[j]){
  int count=0;for(M m:types[j].all)if((m&free)==m)++count;
  if(count<rem[j])return false;
  if(count<best){best=count;chosen=j;}
 }
 if(chosen<0)return !free;
 --rem[chosen];
 for(M m:types[chosen].all)if((m&free)==m&&finish_witness(free^m,rem)){solution.push_back(m);return true;}
 ++rem[chosen];return false;
}
void save_witness(const string&dir,int cost,const vector<int>&orig){
 map<M,int> kind;
 for(int j=0;j<types.size();j++)for(M m:types[j].all)kind[m]=j;
 vector<int>rem=orig;M free=FULL;
 for(M m:solution){
  if(!kind.count(m)||!(rem[kind[m]]--)||(m&free)!=m)throw runtime_error("invalid partial witness");
  free^=m;
 }
 if(!finish_witness(free,rem))throw runtime_error("missing anchored/core decomposition");
 free=FULL;long long check=0;vector<int>verify(types.size());
 for(M m:solution){
  if(!kind.count(m)||(m&free)!=m)throw runtime_error("invalid complete witness");
  free^=m;check+=types[kind[m]].price;++verify[kind[m]];
 }
 if(free||check!=cost||verify!=orig)throw runtime_error("witness verification failure");
 sort(solution.begin(),solution.end());
 ofstream out(dir+"/found_"+to_string(cost)+".json");
 out<<"{\"cost\":"<<cost<<",\"classes\":[";
 for(int i=0;i<solution.size();i++){
  M m=solution[i];int j=kind[m];if(i)out<<",";
  out<<"{\"size\":"<<types[j].sz<<",\"cost\":"<<types[j].price<<",\"points\":[";
  bool sep=false;for(M q=m;q;q&=q-1){if(sep)out<<",";out<<pos(q);sep=true;}out<<"]}";
 }out<<"]}\n";
}

int main(int argc,char**argv){
 ifstream db(argv[1],ios::binary);struct BR{uint64_t lo,hi;unsigned c,s;};BR rr;map<pair<int,int>,Type> all_types;
 while(db.read((char*)&rr,sizeof(rr))){int size=rr.s&255;auto& t=all_types[{size,rr.c}];t.sz=size;t.price=rr.c;M m=M(rr.lo)|(M(rr.hi)<<64);t.all.push_back(m);if(rr.s>=256)t.reps.push_back(m);}
 for(auto& [k,t]:all_types)types.push_back(move(t));int n=types.size();
 map<pair<int,int>,vector<M>> spaces;
 for(int k=1;k<=6;k++){
  ifstream f(string(argv[2])+"/cores"+to_string(k)+".txt");
  uint64_t a,b;set<pair<int,M>> unique;
  while(f>>a>>b){vector<int> centers(k);for(int&i:centers)f>>i;
   for(int h=0;h<(1<<k);h++){
    M m=M(a)|(M(b)<<64);bool ok=true;
    for(int i=0;i<k;i++)if(h>>i&1){M bit=M(1)<<centers[i];if(!(bit&m)){ok=false;break;}m^=bit;}
    if(ok)unique.emplace(popcount((unsigned)h),m);
   }
  }
  for(auto [h,m]:unique)spaces[{k,h}].push_back(m);
 }
 for(int i=0;i<125;i++){M bit=M(1)<<i;slices[i/25]|=bit;slices[5+i/5%5]|=bit;slices[10+i%5]|=bit;}
 init_actions(argv[3]);prepare_bounds();init_shapes();multi_id[{}]=0;multis.push_back({});reachable.push_back({0});
 struct Frame{M f; vector<M>rows;};
 map<tuple<int,int,int>,vector<Frame>> prec;
 auto frames=[&](int k,int h,int a)->const vector<Frame>&{
  auto key=make_tuple(k,h,a);if(prec.count(key))return prec[key];
  string nm=string(argv[3])+"/"+(a==2?"pair":"anchored")+to_string(k)+"_"+to_string(h);
  ifstream ds(nm);uint64_t lo,hi;int n;if(!ds)throw runtime_error(nm);
  auto &frames=prec[key];while(ds>>lo>>hi>>n){Frame r{M(lo)|(M(hi)<<64),{}};for(int j=0;j<n;j++){ds>>lo>>hi;r.rows.push_back(M(lo)|(M(hi)<<64));}
  frames.push_back(move(r));}return frames;};
 int val,begin_frame,end_frame;while(cin>>val>>begin_frame>>end_frame){
  if(begin_frame<0||end_frame<begin_frame)throw runtime_error("bad prefix interval");
  vector<int> orig(n);for(int& x:orig)cin>>x;
  vector<int> ids,cnt;int k=0,h=0,left=0;
  for(int j=0;j<n;j++)if(orig[j]){
   if(types[j].sz==13||types[j].sz==12&&types[j].price==1104){k+=orig[j];if(types[j].sz==13)h+=orig[j];}
   else{ids.push_back(j);cnt.push_back(orig[j]);left+=orig[j];}
  }
  Pools pool;for(int i:ids)pool.push_back(types[i].all);
  abs_lo.resize(pool.size());abs_hi.resize(pool.size());
  for(int j=0;j<pool.size();j++){
   abs_lo[j].fill(13);abs_hi[j].fill(0);
   for(int e=0;e<15;e++)for(M s:pool[j]){
    M m=s&slices[e];int v=popcount(uint64_t(m))+popcount(uint64_t(m>>64));
    abs_lo[j][e]=min(abs_lo[j][e],v);abs_hi[j][e]=max(abs_hi[j][e],v);
   }
  }
  actual_ids=ids;table.clear();bound_at[left].fill(0);level_bound[0].clear();
  for(int j=0;j<ids.size();j++){level_bound[0].push_back(shape_max[ids[j]]);for(int t=0;t<125;t++)bound_at[left][t]+=cnt[j]*shape_max[ids[j]][t];}
  bool found=false;nodes=0;solution.clear();
  int punct=-1;for(int j=0;j<ids.size();j++)if(types[ids[j]].sz==12&&types[ids[j]].price==1116)punct=j;
  geometric_nodes=leaf_nodes=0;
  int count_p=punct<0?0:cnt[punct],pre=min(count_p,k<=1?2:1);
  root_symmetry=k>0&&count_p==0;
  int total_frames=0;
  if(pre){
   auto &sub=frames(k,h,pre);cnt[punct]-=pre;total_frames=sub.size();
   for(int index=begin_frame;index<end_frame&&index<total_frames;index++){
    const auto&r=sub[index];
    if(add_big(r.f,left-pre,punct,0,cnt,pool,r.rows)){found=true;break;}
   }
  }else if(k){
   const auto&sub=spaces[{k,h}];total_frames=sub.size();
   for(int index=begin_frame;index<end_frame&&index<total_frames;index++)
    if(add_big(sub[index],left,punct,0,cnt,pool,{})){found=true;break;}
  }else{
   int a=0;for(int j=1;j<ids.size();j++)if(types[ids[j]].all.size()<types[ids[a]].all.size())a=j;
   --cnt[a];const auto&sub=types[ids[a]].reps;total_frames=sub.size();
   for(int index=begin_frame;index<end_frame&&index<total_frames;index++){
    M m=sub[index];
    if(add_big(FULL^m,left-1,punct,0,cnt,pool,{})){solution.push_back(m);found=true;break;}
   }
  }
  if(found)save_witness(argv[3],val,orig);
  cout<<val<<" "<<geometric_nodes<<" "<<leaf_nodes<<" "<<nodes<<" "<<found<<" "<<total_frames<<endl;
 }
}
