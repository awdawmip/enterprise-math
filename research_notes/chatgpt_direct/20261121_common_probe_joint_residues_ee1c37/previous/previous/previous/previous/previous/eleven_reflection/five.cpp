#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;using U=uint64_t;using M=__uint128_t;int at(M m){return U(m)?__builtin_ctzll(U(m)):64+__builtin_ctzll(U(m>>64));}
int sz(M m){return __builtin_popcountll(U(m))+__builtin_popcountll(U(m>>64));}
struct Row {M m;int c;};vector<Row>fixedrows[14],pairseeds;map<M,Row> bank;map<M,int> pairidx;int g[800][125],H[125];M universe=(M(1)<<125)-1;int limit=11327;int minp[14]={0,0,0,0,0,0,0,0,423,569,792,960};int minf[14]={0,0,0,0,0,0,0,0,0,660,0,960,0,1296};vector<Row> path;vector<int> fixedn,pairn;long long frames,term,solutions;set<vector<int>>seen;int jobid=0;
M move(M m,const int *p){M o=0;for(;m;m&=m-1)o|=M(1)<<p[at(m)];return o;}
int ix(int x,int y,int z){return ((x%5+5)%5)*25+((y%5+5)%5)*5+(z%5+5)%5;}
M support(Row r){return r.m|move(r.m,H);}
void completed(){++solutions;ofstream f("reflection_winner.txt");for(int i=0;i<path.size();i++){M m=path[i].m;for(M v=m;v;v&=v-1)f<<at(v)<<" ";f<<"\n";if(i>=5){m=move(m,H);for(;m;m&=m-1)f<<at(m)<<" ";f<<"\n";}}int cost=0;for(int i=0;i<path.size();i++)cost+=path[i].c*(i>=5?2:1);cerr<<"HIT "<<cost<<endl;exit(0);}
void completion(M free,int price){
 ++frames;if(price+2*(minp[pairn[0]]+minp[pairn[1]]+minp[pairn[2]])>limit)return;
 vector<int> choices[3];for(int z=0;z<3;z++){
 int s=pairn[z],other=minp[pairn[(z+1)%3]]+minp[pairn[(z+2)%3]];
 for(int j=0;j<pairseeds.size();j++){auto&r=pairseeds[j];if(sz(r.m)!=s||price+2*(r.c+other)>limit)continue;M t=support(r);if(!(t&~free))choices[z].push_back(j);}
 if(choices[z].empty())return;
 }
 int a[3]={0,1,2};sort(a,a+3,[&](int x,int y){return choices[x].size()<choices[y].size();});
 for(int i:choices[a[0]]){auto&r=pairseeds[i];M f=free^support(r);for(int j:choices[a[1]]){auto&t=pairseeds[j];M u=support(t);if(u&~f)continue;auto it=bank.find(f^u);if(it==bank.end()||price+2*(r.c+t.c+it->second.c)>limit)continue;path.push_back(r);path.push_back(t);path.push_back(it->second);completed();}}
}
void fix(M free,int k,int price,int first){
 if(k==5){completion(free,price);return;}
 int type=fixedn[k],lb=0;for(int j=k+1;j<5;j++)lb+=minf[fixedn[j]];for(int n:pairn)lb+=2*minp[n];
 auto &v=fixedrows[type];for(int j=first;j<v.size();j++){auto&r=v[j];if((r.m&~free)||price+r.c+lb>limit)continue;path.push_back(r);fix(free^r.m,k+1,price+r.c,(k+1<5&&fixedn[k+1]==type)?j+1:0);path.pop_back();}
}
void start(const vector<int>&f,const vector<int>&p){
 fixedn=f;pairn=p;sort(fixedn.begin(),fixedn.end(),greater<int>());sort(pairn.begin(),pairn.end());
 int lb=0;for(int n:f)lb+=minf[n];for(int n:p)lb+=2*minp[n];if(lb>limit)return;
 // The 13-point fixed rows form a single known orbit. A preselected representative suffices.
 if(fixedn[0]!=13 || fixedn[1]!=13)exit(4);auto&r=fixedrows[13][0];path={r};frames=term=0;fix(universe^r.m,1,r.c,1);cout<<jobid++<<" "<<frames<<" "<<solutions<<endl;
}
int main(int argc,char**argv){
 int k=0;for(int d:{1,2})for(int v=0;v<8;v++)for(int swap=0;swap<2;swap++)for(int a=0;a<5;a++)for(int b=0;b<5;b++){for(int i=0;i<125;i++){int x=i/25,y=i/5%5,z=i%5;if(swap)std::swap(y,z);g[k][i]=ix(d*((v&1)?-x:x),d*((v&2)?-y:y)+a,d*((v&4)?-z:z)+b);}k++;}
 for(int i=0;i<125;i++)H[i]=ix(-i/25,i/5%5,i%5);
 ifstream fr(argv[1]);int n,h,c;U a,b;while(fr>>n>>h>>c>>a>>b){if(h!=5 ||(n!=9&&n!=11&&n!=13))continue;int cap=n==9?719:n==11?1165:1501;if(c<=cap)fixedrows[n].push_back({(M(b)<<64)|a,c});}
 set<M> org;for(int u=0;u<800;u++)org.insert(move(fixedrows[13][0].m,g[u]));if(org.size()!=fixedrows[13].size())return 3;
 ifstream fs(argv[2]);while(fs>>n){M m=0;for(int j=0;j<n;j++){int q;fs>>q;m|=M(1)<<q;}fs>>c;if(n==11&&c>1062)continue;
  M u=m|move(m,H);auto zz=bank.find(u);if(zz!=bank.end()&&zz->second.c<=c)continue;
  for(int j=0;j<800;j++){M q=move(u,g[j]),v=move(m,g[j]);auto it=bank.find(q);if(it==bank.end()||c<it->second.c)bank[q]={v,c};}
 }
 for(auto&[m,r]:bank)pairseeds.push_back(r);
 for(int a=0;a<=5;a++)for(int b=0;b<=5-a;b++){vector<int>f(5-a-b,13);f.insert(f.end(),a,9);f.insert(f.end(),b,11);int n=0;for(int v:f)n+=v;
 for(int x=8;x<=11;x++)for(int y=x;y<=11;y++)for(int z=y;z<=11;z++)if(n+2*(x+y+z)==125)start(f,{x,y,z});}
}
