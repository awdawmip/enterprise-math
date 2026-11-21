// Exact regional cover with an independently checked integer dual change of cost.
#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <vector>
using namespace std;using U=uint64_t;using M=__uint128_t;using L=long long;
constexpr L INF=numeric_limits<L>::max()/8;
int at(M x){return U(x)?__builtin_ctzll(U(x)):64+__builtin_ctzll(U(x>>64));}
int pop(M x){return __builtin_popcountll(U(x))+__builtin_popcountll(U(x>>64));}
struct Hash{size_t operator()(M x)const{return U(x)^(U(x>>64)*0x9e3779b97f4a7c15ULL);}};
struct Rec{U lo,hi;unsigned c,s;};struct C{M m;L rc;int s,c;};
vector<C> cls;vector<int> bypt[125];vector<unordered_map<M,L,Hash>> failed(13);
L dp[13][126];long long nodes=0,limit=0;bool interrupted=false;vector<int> selected,solution;
bool dfs(M rem,int k,L budget){
 if(limit&&nodes++>=limit){interrupted=true;return false;}
 if(!limit)nodes++;
 int n=pop(rem);if(!k){if(!n){solution=selected;return true;}return false;}
 if(n<k||n>13*k||budget<dp[k][n])return false;
 auto it=failed[k].find(rem);if(it!=failed[k].end()&&it->second>=budget)return false;
 size_t few=numeric_limits<size_t>::max();vector<int> opts;
 for(M t=rem;t;t&=t-1){int p=at(t);vector<int> can;
  for(int j:bypt[p]){auto&c=cls[j];if(c.s>n||n-c.s<k-1||n-c.s>13*(k-1)||c.rc+dp[k-1][n-c.s]>budget||(c.m&rem)!=c.m)continue;
   can.push_back(j);if(can.size()>=few)break;
  }
  if(can.size()<few){few=can.size();opts=move(can);if(!few)break;}
 }
 if(few){sort(opts.begin(),opts.end(),[&](int i,int j){auto&a=cls[i];auto&b=cls[j];L da=a.rc+dp[k-1][n-a.s],db=b.rc+dp[k-1][n-b.s];return da!=db?da<db:a.m<b.m;});
  for(int j:opts){auto&c=cls[j];selected.push_back(j);if(dfs(rem^c.m,k-1,budget-c.rc))return true;selected.pop_back();if(interrupted)return false;}
 }
 auto [fit,inserted]=failed[k].emplace(rem,budget);if(!inserted)fit->second=max(fit->second,budget);
 return false;
}
int main(int argc,char**argv){
 if(argc!=5&&argc!=6)return 2;
 ifstream job(argv[1]);int jid,k,budget,n;job>>jid>>k>>budget>>n;M region=0;for(int i=0,v;i<n;i++){job>>v;region|=M(1)<<v;}assert(pop(region)==n);
 ifstream weights(argv[3]);L q,v,w[125];weights>>q>>v;for(L&a:w)weights>>a;assert(q>0);
 if(argc==6)limit=atoll(argv[5]);
 L rb=q*budget-k*v;for(M m=region;m;m&=m-1)rb-=w[at(m)];
 ifstream bank(argv[2],ios::binary);Rec r;L mins[14];fill(mins,mins+14,INF);
 while(bank.read((char*)&r,sizeof(r))){M m=M(r.lo)|(M(r.hi)<<64);assert((m&region)==m&&pop(m)==int(r.s));L c=q*r.c-v;for(M t=m;t;t&=t-1)c-=w[at(t)];assert(c>=0);
  int j=cls.size();cls.push_back({m,c,int(r.s),int(r.c)});mins[r.s]=min(mins[r.s],c);for(M t=m;t;t&=t-1)bypt[at(t)].push_back(j);
 }
 fill(&dp[0][0],&dp[0][0]+13*126,INF);dp[0][0]=0;for(int a=1;a<=k;a++)for(int b=1;b<=n;b++)for(int s=1;s<=13&&s<=b;s++)dp[a][b]=min(dp[a][b],dp[a-1][b-s]+mins[s]);
 auto start=chrono::steady_clock::now();bool found=dfs(region,k,rb);double secs=chrono::duration<double>(chrono::steady_clock::now()-start).count();
 ofstream out(argv[4]);out<<"{\"job\":"<<jid<<",\"method\":\"dual_exact_cover\",\"search_nodes\":"<<nodes<<",\"search_seconds\":"<<secs<<",\"complete\":"<<(interrupted?"false":"true")<<",\"found\":"<<(found?"true":"false")<<",\"reduced_budget\":"<<rb;
 if(found){int c=0;out<<",\"groups\":[";for(int i=0;i<(int)solution.size();i++){if(i)out<<',';auto&r=cls[solution[i]];c+=r.c;out<<'[';bool first=true;for(M m=r.m;m;m&=m-1){if(!first)out<<',';first=false;out<<at(m);}out<<']';}out<<"],\"cost\":"<<c;}out<<"}"<<endl;
}
