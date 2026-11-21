#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <sstream>
#include <string>
#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <unordered_map>
using U=uint64_t;using M=__uint128_t;using Map=std::array<int,125>;
int ix(M m){return U(m)?__builtin_ctzll(U(m)):64+__builtin_ctzll(U(m>>64));}
struct Row{U m;M seed;int c;};
Map g;int qi[125],inds[63];U all=(U(1)<<63)-1;
std::vector<Map>cent;std::vector<std::array<int,63>>acts;
U quot(M seed){U z=0;for(;seed;seed&=seed-1)z|=U(1)<<qi[ix(seed)];return z;}
U image(U x,const std::array<int,63>&t){U z=0;for(;x;x&=x-1)z|=U(1)<<t[__builtin_ctzll(x)];return z;}
std::array<std::vector<Row>,2000>v;std::array<std::vector<int>,2000>reps;std::array<std::unordered_map<U,int>,2000>bank;
struct Slot{int t,amt,first;};std::vector<Slot>slots;
int cap;long long nodes,lookups,solution;int ctype[2000]{};std::vector<std::pair<int,int>>path;std::ofstream witness;
int upper(int t,int c){auto&w=v[t];return std::upper_bound(w.begin(),w.end(),c,[](int x,const Row&r){return x<r.c;})-w.begin();}
void found(int spent){
 solution++;cap=spent-1;witness<<"cost "<<spent<<"\n";for(auto[t,j]:path){const auto&x=v[t][j];witness<<ctype[t]<<" "<<x.c<<" "<<U(x.seed)<<" "<<U(x.seed>>64)<<"\n";}witness<<std::flush;
}
void cover(U free,int spent,int left){
 nodes++;
 int lb=0,nt=0,active=-1;int minc[13]{},last=-1;
 for(int k=0;k<(int)slots.size();k++){auto [t,a,f]=slots[k];if(!a)continue;nt++;last=k;
 if(f+a>(int)v[t].size())return;
 // Recover geometric individual floor from a bounded prefix. Leaving unseen cases at the prefix floor is safe.
 int count=0,mc=0,j=f;for(;count<a && j<(int)v[t].size() && j<f+70;j++)if(!(v[t][j].m&~free)){mc+=v[t][j].c;count++;}
 if(count<a && j==(int)v[t].size())return;
 if(count<a)mc+=(a-count)*v[t][j].c;
 minc[k]=mc;lb+=mc;
 }
 if(spent+lb>cap)return;
 if(left==1){
 auto [t,a,f]=slots[last];assert(a==1);lookups++;auto it=bank[t].find(free);if(it!=bank[t].end() && it->second>=f && spent+v[t][it->second].c<=cap){
 path.push_back({t,it->second});found(spent+v[t][it->second].c);path.pop_back();}return;
 }
 int smallest=100000000,shortslot=-1,mx=0;bool root=path.empty();std::vector<int>selected;
 for(int k=0;k<(int)slots.size();k++){
 auto [t,a,f]=slots[k];if(!a)continue;
 int maxp=(cap-spent-lb+minc[k])/a;int to=upper(t,maxp);if(to<=f)return;
 if(root){
  auto&rr=reps[t];auto end=std::lower_bound(rr.begin(),rr.end(),to);int n=end-rr.begin();if(!n)return;
  if(n<smallest){selected.assign(rr.begin(),end);smallest=n;shortslot=k;mx=to;}
 }else{
  if(to-f>std::max(1000LL,smallest*4LL))continue;
  std::vector<int>usable;for(int j=f;j<to;j++)if(!(v[t][j].m&~free))usable.push_back(j);
  if(usable.empty())return;
  if((int)usable.size()<smallest){selected=std::move(usable);smallest=selected.size();shortslot=k;mx=to;}
 }
 }
 assert(shortslot>=0);auto&ch=slots[shortslot];int t=ch.t,oldf=ch.first;ch.amt--;
 for(int j:selected){auto&r=v[t][j];ch.first=root?upper(t,r.c-1):j+1;path.push_back({t,j});cover(free^r.m,spent+r.c,left-1);path.pop_back();}
 ch.amt++;ch.first=oldf;
}
// Two disjoint rows can be normalized by sending the first support to its
// least centralizer image. For each pair of signatures retain the best
// possible sum; this bound can be added over vertex-disjoint pairs of slots.
int cost2[1200][1200];
int disjoint_price(int a,int b){
 auto &cost=cost2[a][b];if(cost)return cost;
 if(reps[a].size()*v[b].size()>reps[b].size()*v[a].size())std::swap(a,b);
 int best=200000;for(int j:reps[a]){auto &x=v[a][j];if(x.c+v[b][0].c>=best)break;
 for(auto&y:v[b]){if(x.c+y.c>=best)break;if(!(x.m&y.m)){best=x.c+y.c;break;}}
 }
 cost2[b][a]=cost2[a][b]=best;return best;
}
bool pairbound(int &read){
 int types[12],nn=0;read=0;
 for(auto &s:slots){if(v[s.t].empty())return true;for(int j=0;j<s.amt;j++)types[nn++]=s.t;read+=s.amt*v[s.t][0].c;}
 struct Edge{int weight;int mask;};Edge e[72];int total=0;
 for(int i=0;i<nn;i++)for(int j=i+1;j<nn;j++){int a=types[i],b=types[j];int w=disjoint_price(a,b)-v[a][0].c-v[b][0].c;
 if(read+w>cap)return true;if(w>0)e[total++]={w,(1<<i)|(1<<j)};}
 std::sort(e,e+total,[](auto a,auto b){return a.weight>b.weight;});int mask=0;for(int i=0;i<total;i++)if(!(mask&e[i].mask)){mask|=e[i].mask;read+=e[i].weight;if(read>cap)return true;}return false;
}
int main(int ac,char**av){
 if(ac!=10)return 2;
 std::ifstream mp(av[1]);for(int&x:g)mp>>x;int count=0;for(int i=0;i<125;i++)if(i<=g[i]){qi[i]=qi[g[i]]=count;inds[count++]=i;}assert(count==63);
 Map l;while(mp>>l[0]){for(int i=1;i<125;i++)mp>>l[i];std::array<int,63>a;for(int i=0;i<63;i++)a[i]=qi[l[inds[i]]];acts.push_back(a);}
 std::ifstream sigs(av[9]);std::array<int,6> total;for(int&x:total)sigs>>x;
 std::map<std::array<int,7>,int> shapeid;int cls=0,rr;
 while(sigs>>rr){std::array<int,7> q;q[0]=rr;int c;for(int i=1;i<7;i++)sigs>>q[i];sigs>>c;ctype[cls]=rr;shapeid[q]=cls++;}
 int col[63];std::fill(col,col+63,-1);int coln=0;for(int i=0;i<63;i++)if(col[i]<0){for(auto&l:acts)col[l[i]]=coln;coln++;}assert(coln==6);
 for(int m:{1,2}){std::ifstream in(av[1+m]);int s,h,c;U a,b;while(in>>s>>h>>c>>a>>b){M seed=(M(b)<<64)|a;
 std::array<int,7> q{};q[0]=m;for(M z=seed;z;z&=z-1)q[1+col[qi[ix(z)]]]+=m;int t=shapeid.at(q);v[t].push_back({quot(seed),seed,c*m});}}
 for(int t=0;t<cls;t++)if(!v[t].empty()){
 auto&w=v[t];std::sort(w.begin(),w.end(),[](const Row&a,const Row&b){return a.c!=b.c?a.c<b.c:a.m<b.m;});for(int j=0;j<int(w.size());j++)bank[t][w[j].m]=j;
 std::set<U> normalized;for(int j=0;j<int(w.size());j++){
 bool smallest=true;for(auto&a:acts)if(image(w[j].m,a)<w[j].m){smallest=false;break;}
 if(smallest)reps[t].push_back(j);
 }
 }
 std::ifstream profile(av[4]);cap=std::stoi(av[5]);witness.open(av[6]);int lo=std::stoi(av[7]),hi=std::stoi(av[8]),n,id=0;
 std::string line;while(std::getline(profile,line)){if(id>=hi)break;if(id<lo){id++;continue;}std::istringstream ss(line);int orig,t;
 ss>>orig;std::map<int,int>ct;n=0;while(ss>>t){ct[t]++;n++;}
 slots.clear();for(auto[t,z]:ct)slots.push_back({t,z,0});nodes=lookups=0;int relax;if(!pairbound(relax))cover(all,0,n);
 std::cout<<id<<" "<<cap<<" "<<solution<<" "<<nodes<<" "<<lookups<<"\n";if(id%250==0)std::cout.flush();id++;
 }
}
