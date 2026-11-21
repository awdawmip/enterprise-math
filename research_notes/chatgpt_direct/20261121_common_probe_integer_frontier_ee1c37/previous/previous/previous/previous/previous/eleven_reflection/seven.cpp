#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <map>
using namespace std;using U=uint64_t;using M=__uint128_t;
M all=(M(1)<<125)-1;int p(M v){return U(v)?__builtin_ctzll(U(v)):64+__builtin_ctzll(U(v>>64));}int sz(M v){return __builtin_popcountll(U(v))+__builtin_popcountll(U(v>>64));}
struct Row{M m;int c;};vector<Row>fixed_rows,pairs;M plane=(M(1)<<25)-1;int bd=11327;long long hits,nodes;vector<Row> ans;
int lower[8][26];int sizegroup[8][26];M refl(M m){M z=0;for(;m;m&=m-1){int q=p(m);z|=M(1)<<(((5-q/25)%5)*25+q%25);}return z;}
void solve(M rem,int k,int price,const vector<int>&pool){
 ++nodes;if(!k){if(!rem && price<=bd){hits++;ofstream f("k7winner.txt");for(auto&r:ans){for(M m=r.m;m;m&=m-1)f<<p(m)<<" ";f<<"\n";}cerr<<"hit "<<price<<endl;exit(0);}return;}
 if(price+lower[k][sz(rem&plane)]>bd)return;
 vector<int> opts;M cover=0;int c[125]{};for(int j:pool){auto&r=fixed_rows[j];if((r.m&~rem)||price+r.c+lower[k-1][sz((rem^r.m)&plane)]>bd)continue;opts.push_back(j);cover|=r.m;}
 if(cover!=rem)return;
 for(int j:opts)for(M m=fixed_rows[j].m;m;m&=m-1)c[p(m)]++;int one=-1,least=1000000;
 for(M a=rem;a;a&=a-1){int j=p(a);if(c[j]<least){least=c[j];one=j;}}
 for(int j:opts)if(fixed_rows[j].m&(M(1)<<one)){auto &r=fixed_rows[j];ans.push_back(r);solve(rem^r.m,k-1,price+r.c,opts);ans.pop_back();}
}
int main(int argc,char**argv){ifstream f(argv[1]);int n,h,c;U l,r;int cheap[8];fill(cheap,cheap+8,100000);
 while(f>>n>>h>>c>>l>>r){int caps[]={671,863,1031,1199,1367,1535};if(n==h+8 && h<=5&&c<=caps[h]){fixed_rows.push_back({(M(r)<<64)|l,c});cheap[h]=min(cheap[h],c);}}
 for(auto&row:lower)fill(row,row+26,1000000);lower[0][0]=0;for(int k=1;k<=7;k++)for(int j=0;j<=25;j++)for(int i=0;i<=min(j,5);i++)lower[k][j]=min(lower[k][j],lower[k-1][j-i]+cheap[i]);
 ifstream g(argv[2]);map<M,Row> compressed;while(g>>c>>l>>r){M m=(M(r)<<64)|l;M b=refl(m);if(m&b)exit(3);M u=m|b;if(!compressed.contains(u)||compressed[u].c>c)compressed[u]={m,c};}
 for(auto &[u,v]:compressed)pairs.push_back(v);
 cerr<<fixed_rows.size()<<" "<<pairs.size()<<" "<<lower[7][25]<<endl;
 ifstream jr(argv[3]);int ix=0;while(jr>>l>>r){M seed=(M(r)<<64)|l;M u=seed|refl(seed);int c=compressed.at(u).c;long long ac=0;nodes=0;
 for(int j=0;j<pairs.size();j++){auto&r=pairs[j];M t=r.m|refl(r.m);if((u&t)||2*(c+r.c)+lower[7][25]>bd)continue;M rem=all^u^t;ans={{seed,c},{refl(seed),c},r,{refl(r.m),r.c}};vector<int> pool;for(int k=0;k<fixed_rows.size();k++)if(!(fixed_rows[k].m&~rem))pool.push_back(k);++ac;solve(rem,7,2*(c+r.c),pool);}
 cout<<ix++<<" "<<ac<<" "<<nodes<<" "<<hits<<endl;}
}
