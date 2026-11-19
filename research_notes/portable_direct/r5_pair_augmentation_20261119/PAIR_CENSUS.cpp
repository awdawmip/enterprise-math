#include <bits/stdc++.h>
using namespace std;
constexpr int N=256,A=101;
int H[6]={0,16,32,48,1,64};
struct Act{int k;vector<int> masks;};
struct Item{int u,v,count;vector<Act> acts;int f0=-1;};
string family_key(const vector<int>&v){string s;s.push_back(char(v.size()));for(int x:v)s.push_back(char(x));return s;}
vector<int> maximal(vector<int> s){
 sort(s.begin(),s.end());s.erase(unique(s.begin(),s.end()),s.end());
 vector<int> z;for(int x:s){bool dominated=false;
  for(int y:s)if(x!=y&&(x&y)==x){dominated=true;break;}
  if(!dominated)z.push_back(x);}return z;
}
int f0_eval(const vector<Act>&acts){
 int memo[256];fill(memo,memo+256,-1);
 auto solve=[&](auto&&self,int live)->int{
  if(__builtin_popcount((unsigned)live)<=1)return 0;
  if(memo[live]!=-1)return memo[live];
  int best=10000000;
  for(auto&a:acts){
   bool bad=false;for(int s:a.masks)if((s&live)==live){bad=true;break;}if(bad)continue;
   int mx=0;for(int s:a.masks)mx=max(mx,self(self,live&s));
   best=min(best,a.k+mx);
  }
  if(best==10000000){cerr<<"F0 NO PROGRESS "<<live<<"\n";exit(4);}
  return memo[live]=best;
 };
 return solve(solve,255);
}
int main(){
 ifstream f("window_adj.bin",ios::binary);if(!f){cerr<<"missing window_adj.bin\n";return 2;}
 vector<unsigned char> adj(size_t(A)*N*N);
 f.read((char*)adj.data(),adj.size());
 if((size_t)f.gcount()!=adj.size()){cerr<<"bad adjacency\n";return 3;}
 vector<Item> uniq;
 unordered_map<string,int> lookup;lookup.reserve(30000);
 vector<array<int,3>> each;
 for(int u=0;u<N;u++){
  if(find(begin(H),end(H),u)!=end(H))continue;
  for(int v=u+1;v<N;v++){
   if(find(begin(H),end(H),v)!=end(H))continue;
   int labels[8]={H[0],H[1],H[2],H[3],H[4],H[5],u,v};
   map<string,Act> classes;
   for(int k=0;k<A;k++){
    vector<int> masks;
    const unsigned char*data=adj.data()+size_t(k)*N*N;
    for(int i=0;i<8;i++){
     const unsigned char*row=data+size_t(labels[i])*N;int mask=0;
     for(int j=0;j<8;j++)if(row[labels[j]])mask|=1<<j;
     masks.push_back(mask);
    }
    auto mm=maximal(masks);auto key=family_key(mm);
    if(!classes.count(key))classes.emplace(key,Act{k+214,mm});
   }
   vector<Act> reps;string signature;
   for(auto&[family,a]:classes){
    if(family.size()==2&&int(uint8_t(family[1]))==255)continue;
    reps.push_back(a);
   }
   sort(reps.begin(),reps.end(),[](auto&x,auto&y){return x.k<y.k;});
   for(auto&a:reps){signature+=char(a.k-214);signature+=family_key(a.masks);}
   auto it=lookup.find(signature);int idx;
   if(it==lookup.end()){
    idx=int(uniq.size());lookup.emplace(move(signature),idx);
    uniq.push_back(Item{u,v,0,reps,-1});
   }else idx=it->second;
   uniq[idx].count++;
   each.push_back({u,v,idx});
  }
 }
 map<int,int>dist;
 for(auto &z:uniq){z.f0=f0_eval(z.acts);dist[z.f0]+=z.count;}
 ofstream a("pair_signature_census.tsv");
 a<<"# id u v multiplicity f0 action_count actions(k:decimal_masks)\n";
 for(int i=0;i<int(uniq.size());i++){
  auto &z=uniq[i];
  a<<i<<' '<<z.u<<' '<<z.v<<' '<<z.count<<' '<<z.f0<<' '<<z.acts.size();
  for(auto&x:z.acts){a<<' '<<x.k<<":";for(int s:x.masks)a<<s<<",";}a<<"\n";
 }
 ofstream b("pair_signature_members.tsv");
 b<<"# u v signature_id\n";
 for(auto&x:each)b<<x[0]<<' '<<x[1]<<' '<<x[2]<<"\n";
 cout<<"PAIR_CENSUS pairs="<<each.size()<<" signatures="<<uniq.size();
 for(auto&[v,c]:dist)cout<<" f0_"<<v<<"="<<c;cout<<"\n";
}
