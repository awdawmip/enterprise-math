#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <vector>
using namespace std;
using U=uint64_t; using M=__uint128_t;
constexpr M one=1;
int at(M x){return U(x)?__builtin_ctzll(U(x)):64+__builtin_ctzll(U(x>>64));}
int pop(M x){return __builtin_popcountll(U(x))+__builtin_popcountll(U(x>>64));}
struct Hash{size_t operator()(M x)const{return U(x)^(U(x>>64)*0x9e3779b97f4a7c15ULL);}};
using R=array<U,4>; using F=array<M,125>;
R obs[125][125]; M bad[125][125];
int mn[]={0,0,12,36,72,120,201,292,419,557,744,936,1104,1296};
int dp[13][126],cap[14];
struct C{M m;int s,c;};
vector<C> cls; vector<int> bypt[125]; int selected[14];
long long enum_nodes=0,search_nodes=0;
vector<int> solution,chosen;
vector<unordered_map<M,int,Hash>> failed(13);
int maxfuture[15];
void enumerate(int size,M cand,const F& forbidden,const R*masks,int cost,M mask){
 ++enum_nodes;
 if(size && cost<=cap[size])cls.push_back({mask,size,cost});
 if(size==13||cost>maxfuture[size+1])return;
 while(cand){int v=at(cand);cand&=cand-1;
  R next[14],newrow{};int nc=cost;
  for(int j=0;j<size;j++)for(int h=0;h<4;h++){
   U pair=obs[v][selected[j]][h],old=masks[j][h];
   next[j][h]=old|pair;nc+=__builtin_popcountll(pair&~old);newrow[h]|=pair;
  }
  for(U w:newrow)nc+=__builtin_popcountll(w);
  if(nc>maxfuture[size+1])continue;
  next[size]=newrow;selected[size]=v;
  M rem=cand&~forbidden[v]; F nf{};
  for(M todo=rem;todo;todo&=todo-1){int j=at(todo);nf[j]=forbidden[j]|bad[j][v];}
  enumerate(size+1,rem,nf,next,nc,mask|(one<<v));
 }
}
bool dfs(M rem,int k,int budget){
 ++search_nodes;
 int n=pop(rem);
 if(!k){if(!n){solution=chosen;return true;}return false;}
 if(n<k||n>13*k||budget<dp[k][n])return false;
 auto it=failed[k].find(rem);if(it!=failed[k].end()&&it->second>=budget)return false;
 int pivot=-1;size_t few=numeric_limits<size_t>::max();vector<int> opts;
 for(M todo=rem;todo;todo&=todo-1){int p=at(todo);vector<int> can;
  for(int j:bypt[p]){auto&c=cls[j];
   if(c.s>n||n-c.s<k-1||n-c.s>13*(k-1)||c.c+dp[k-1][n-c.s]>budget||(c.m&rem)!=c.m)continue;
   can.push_back(j);if(can.size()>=few)break;
  }
  if(can.size()<few){pivot=p;few=can.size();opts=move(can);if(!few)break;}
 }
 if(few){
  sort(opts.begin(),opts.end(),[&](int i,int j){auto&a=cls[i];auto&b=cls[j];
   int da=a.c+dp[k-1][n-a.s],db=b.c+dp[k-1][n-b.s];return da!=db?da<db:a.m<b.m;});
  for(int j:opts){auto&c=cls[j];chosen.push_back(j);if(dfs(rem^c.m,k-1,budget-c.c))return true;chosen.pop_back();}
 }
 failed[k][rem]=max(failed[k][rem],budget);
 return false;
}
int main(int argc,char**argv){
 if(argc!=3&&argc!=4)return 2;
 ifstream f(argv[1],ios::binary);f.read((char*)obs,sizeof(obs));array<unsigned char,3> edge;int edges=0;
 while(f.read((char*)edge.data(),3)){edges++;do{bad[edge[0]][edge[1]]|=one<<edge[2];}while(next_permutation(edge.begin(),edge.end()));}assert(edges==47000);
 fill(&dp[0][0],&dp[0][0]+13*126,1000000);dp[0][0]=0;
 for(int k=1;k<=12;k++)for(int n=1;n<=125;n++)for(int s=1;s<=13&&s<=n;s++)dp[k][n]=min(dp[k][n],dp[k-1][n-s]+mn[s]);
 ifstream jobs(argv[2]);int job,k,budget,n;
 while(jobs>>job>>k>>budget>>n){
  M region=0;for(int i=0,v;i<n;i++){jobs>>v;region|=one<<v;}assert(n==pop(region));
  cls.clear();for(auto&v:bypt)v.clear();for(auto&v:failed)v.clear();chosen.clear();solution.clear();enum_nodes=search_nodes=0;
  fill(cap,cap+14,-1);maxfuture[14]=-1;
  for(int s=1;s<=13&&s<=n;s++)if(n-s>=k-1&&n-s<=13*(k-1))cap[s]=budget-dp[k-1][n-s];
  for(int s=13;s>=0;s--)maxfuture[s]=max(cap[s],maxfuture[s+1]);
  auto start=chrono::steady_clock::now();
  F forbidden{};R masks[14]{};enumerate(0,region,forbidden,masks,0,0);
  for(int j=0;j<(int)cls.size();j++)for(M m=cls[j].m;m;m&=m-1)bypt[at(m)].push_back(j);
  auto generated=chrono::steady_clock::now();
  if(argc==4){
   struct Rec{U lo,hi;unsigned c,s;};ofstream out(string(argv[3])+"/bank_"+to_string(job),ios::binary);
   for(auto&r:cls){Rec rec{U(r.m),U(r.m>>64),unsigned(r.c),unsigned(r.s)};out.write((char*)&rec,sizeof(rec));}
   cout<<"{\"job\":"<<job<<",\"scope\":\"candidate_generation_only\",\"classes\":"<<cls.size()<<",\"enum_nodes\":"<<enum_nodes<<",\"enum_seconds\":"<<chrono::duration<double>(generated-start).count()<<"}"<<endl;
   continue;
  }
  bool found=dfs(region,k,budget);
  auto end=chrono::steady_clock::now();
  cout<<"{\"job\":"<<job<<",\"k\":"<<k<<",\"budget\":"<<budget<<",\"points\":"<<n<<",\"classes\":"<<cls.size()<<",\"enum_nodes\":"<<enum_nodes<<",\"search_nodes\":"<<search_nodes<<",\"enum_seconds\":"<<chrono::duration<double>(generated-start).count()<<",\"search_seconds\":"<<chrono::duration<double>(end-generated).count()<<",\"found\":"<<(found?"true":"false");
  if(found){int c=0;cout<<",\"groups\":[";for(int j=0;j<(int)solution.size();j++){if(j)cout<<',';auto&r=cls[solution[j]];c+=r.c;cout<<'[';bool first=true;for(M t=r.m;t;t&=t-1){if(!first)cout<<',';cout<<at(t);first=false;}cout<<']';}cout<<"],\"cost\":"<<c;}
  cout<<"}"<<endl;
 }
}
