// Independent exact positive BRC branch-count check for R253. No native import.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <tuple>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
using U=uint64_t;
using Key=tuple<int,int,int>; // terminal control, linear sign, offset on e1
struct Edge {int target,sgn,shift;};
static const Edge edges[3][2] = {{{2,-1,-1},{2,1,-1}},{{0,-1,-1},{0,1,-1}},{{1,1,1},{2,1,-1}}};
using Hist=map<Key,U>;
Hist step(const Hist &h){ Hist out;
 for(auto &[key,count]:h){auto [q,eps,k]=key;
   for(const auto &edge:edges[q]) out[{edge.target,edge.sgn*eps,edge.sgn*k+edge.shift}]+=count;
 } return out; }
map<int,U> anchors(const Hist &h){map<int,U> a;
 for(const auto &[key,c]:h){auto [q,e,k]=key;a[-e*k]+=c;}return a;}
map<pair<int,int>,U> holonomy_anchor(const Hist &h){map<pair<int,int>,U> a;
 for(const auto &[key,c]:h){auto [q,e,k]=key;a[{-e*k,e}]+=c;}return a;}
U binom(unsigned n,unsigned k){if(k>n)return 0; if(k>n-k)k=n-k;__uint128_t z=1;for(unsigned i=1;i<=k;++i){z=z*(n-i+1)/i;}return static_cast<U>(z);}
vector<string> collide_three(){struct Path{int q,e,k;string word;};vector<Path> v={{0,1,0,""}};
 for(int m=0;m<3;++m){vector<Path> nxt;
  for(const auto &p:v)for(int i=0;i<2;++i){auto g=edges[p.q][i];nxt.push_back({g.target,g.sgn*p.e,g.sgn*p.k+g.shift,p.word+to_string(i)});}
  v=std::move(nxt);
 }
 map<Key,vector<string>> groups;for(const auto &p:v)groups[{p.q,p.e,p.k}].push_back(p.word);
 vector<string> got;for(const auto &[k,w]:groups)if(w.size()>1){auto sorted=w;sort(sorted.begin(),sorted.end());got.push_back(sorted[0]+"|"+sorted[1]);}
 sort(got.begin(),got.end());return got;
}
int main(){Hist a={{{0,1,0},1}}, b={{{1,1,0},1}};
 int first_joint=-1,first_collision=-1;
 for(int m=0;m<=48;++m){
   U n=0,maxfiber=0;for(auto &[k,c]:a){n+=c;maxfiber=max(maxfiber,c);auto [q,e,v]=k;assert(e==1 || e==-1);assert(abs(v)<=m);assert(((v-m)%2)==0);int p=-e*v; assert(v==-e*p);}
   assert(n==(U(1)<<m));
   auto aa=anchors(a),bb=anchors(b);assert(aa==bb);
   assert(aa.size()==size_t(m+1));
   for(int j=0;j<=m;++j)assert(aa[m-2*j]==binom(m,j));
   if(first_joint<0 && holonomy_anchor(a)!=holonomy_anchor(b))first_joint=m;
   if(maxfiber>1 && first_collision<0)first_collision=m;
   if(m==3){assert(maxfiber==2); auto cs=collide_three(); assert(cs==vector<string>({"000|101","001|100"}));}
   if(m==12 || m==24 || m==48)cout<<"m="<<m<<" paths="<<n<<" support="<<a.size()<<" maxfiber="<<maxfiber<<"\n";
   a=step(a);b=step(b);
 }
 assert(first_joint==3 && first_collision==3);
 cout<<"first_joint_difference="<<first_joint<<" first_ordered_path_collision="<<first_collision<<" status=PASS\n";
}
