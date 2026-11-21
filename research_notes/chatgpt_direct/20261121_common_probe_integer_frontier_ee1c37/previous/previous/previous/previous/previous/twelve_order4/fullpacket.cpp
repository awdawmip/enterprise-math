#include <array>
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using namespace std;using M=__uint128_t;using U=uint64_t;using S=uint64_t;
int at(M v){return U(v)?__builtin_ctzll(U(v)):64+__builtin_ctzll(U(v>>64));}
int pop(M v){return __builtin_popcountll(U(v))+__builtin_popcountll(U(v>>64));}
struct P{S q;int r,c,n;M m;};int g[125],norb,cyc[125],wgt[64],per,low[13][126],best=10131;map<pair<S,int>,P> store;vector<P> rows,ans;vector<int> by[64];long long nodes,limit;S all;string prefix;
int countp(S q){int n=0;for(;q;q&=q-1)n+=wgt[__builtin_ctzll(q)];return n;}
M moved(M m){M a=0;for(;m;m&=m-1)a|=M(1)<<g[at(m)];return a;}
void add(M a,int c){M m=a,u=0;int r=0;do{if(u&m)return;u|=m;m=moved(m);r++;if(m<a)return;}while(m!=a);if(r>12)return;
 S q=0;for(M v=u;v;v&=v-1)q|=S(1)<<cyc[at(v)];int n=pop(u);auto it=store.find({q,r});if(it==store.end() || it->second.c>c*r)store[{q,r}]={q,r,c*r,n,a};}
void save(){ofstream f(prefix+to_string(best)+".txt");for(auto&p:ans){M a=p.m;for(int j=0;j<p.r;j++){for(M v=a;v;v&=v-1)f<<at(v)<<" ";f<<"\n";a=moved(a);}}}
void dfs(S free,int left,int pts,int cost,const vector<int>& options){
 if(++nodes>limit)return;
 if(!left){if(!free&&cost<best){best=cost;save();cerr<<"found "<<best<<endl;}return;}
 vector<int> active;S united=0;int ct[64]{},bestc[64];fill(bestc,bestc+64,10000000);
 for(int j:options){auto &t=rows[j];if(t.r>left || (t.q&~free) || cost+t.c+low[left-t.r][pts-t.n]>=best)continue;active.push_back(j);united|=t.q;}
 if(united!=free)return;
 int least=10000000,p=-1;
 for(int j:active)for(S v=rows[j].q;v;v&=v-1)ct[__builtin_ctzll(v)]++;
 for(S v=free;v;v&=v-1){int i=__builtin_ctzll(v);if(ct[i]<least){p=i;least=ct[i];}}
 for(int j:active){auto &r=rows[j];if(!(r.q>>p&1))continue;ans.push_back(r);dfs(free^r.q,left-r.r,pts-r.n,cost+r.c,active);ans.pop_back();if(nodes>limit)return;}
}
int main(int argc,char**argv){ifstream gm(argv[1]);gm>>per;for(int&i:g)gm>>i;int maxsize=0;limit=stoll(argv[3]);prefix=argv[4];int cap=stoi(argv[5]);best=cap+1;
 for(int p=0;p<125;p++){if(cyc[p])continue;int q=p;do{cyc[q]=norb+1;++wgt[norb];q=g[q];}while(q!=p);norb++;}if(norb>64)return 2;for(int&i:cyc)--i;all=norb==64?~S(0):((S(1)<<norb)-1);
 array<array<int,125>,125> translate;
 for(int t=0;t<125;t++)for(int p=0;p<125;p++)translate[t][p]=((p/25+t/25)%5)*25+((p/5%5+t/5%5)%5)*5+(p%5+t%5)%5;
 ifstream db(argv[2]);int price;U l,h;while(db>>price>>l>>h){M base=(M(h)<<64)|l;for(auto &tr:translate){M z=0;for(M m=base;m;m&=m-1)z|=M(1)<<tr[at(m)];add(z,price);}}
 if(argc>=7){ifstream fixed(argv[6]);int r,c;S q;U a,b;while(fixed>>r>>q>>c>>a>>b){M m=(M(b)<<64)|a;auto it=store.find({q,r});if(it==store.end() || it->second.c>c)store[{q,r}]={q,r,c,r*pop(m),m};}}
 const int minima[14]={0,0,12,36,72,120,201,292,419,557,744,936,1104,1296};
 for(int i=0;i<=12;i++)for(int j=0;j<=125;j++)low[i][j]=10000000;low[0][0]=0;
 for(int i=1;i<=12;i++)for(int j=1;j<=125;j++)for(int n=1;n<=min(j,13);n++)low[i][j]=min(low[i][j],minima[n]+low[i-1][j-n]);
 for(auto &p:store){auto &r=p.second;if(r.c+low[12-r.r][125-r.n]<best)rows.push_back(r);}sort(rows.begin(),rows.end(),[&](auto&a,auto&b){return a.c+low[12-a.r][125-a.n]<b.c+low[12-b.r][125-b.n];});vector<int> opt;
 map<int,int> tally;for(int i=0;i<rows.size();i++)opt.push_back(i),tally[rows[i].r]++;
 for(auto x:tally)cerr<<x.first<<":"<<x.second<<" ";cerr<<endl;
 dfs(all,12,125,0,opt);cout<<best<<" "<<nodes<<endl;}
