#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using namespace std;using U=uint64_t;using M=__uint128_t;using W=array<U,4>;
int first(M m){return U(m)?__builtin_ctzll(U(m)):64+__builtin_ctzll(U(m>>64));}
int pop(M m){return __builtin_popcountll(U(m))+__builtin_popcountll(U(m>>64));}
M bad[125][125];W obs[125][125];int g[125],costs[14][26];long long counts[14][26];long long nodes;
M banned(M used,M add,M forbidden){for(;add;add&=add-1){int i=first(add);if(forbidden&(M(1)<<i))return ~M(0);for(M b=used;b;b&=b-1)forbidden|=bad[i][first(b)];used|=M(1)<<i;}return forbidden;}
int cost(M used){int c=0;for(M a=used;a;a&=a-1){int p=first(a);W w{};for(M b=used;b;b&=b-1){auto&o=obs[p][first(b)];for(int l=0;l<4;l++)w[l]|=o[l];}for(U v:w)c+=__builtin_popcountll(v);}return c;}
vector<M> groups;vector<int> amt,par;ofstream dump;
void solve(M used,M forbidden,int n,int h,int start){
 ++nodes;counts[n][h]++;if(n>=1){int c=cost(used);costs[n][h]=min(costs[n][h],c);if(n>=7)dump<<n<<" "<<h<<" "<<c<<" "<<U(used)<<" "<<U(used>>64)<<"\n";}
 for(int j=start;j<groups.size();j++){M add=groups[j];if(n+amt[j]>13 || (add&forbidden))continue;
  M f=banned(used,add,forbidden);if(f==~M(0))continue;solve(used|add,f,n+amt[j],h+par[j],j+1);}
}
int main(int argc,char**argv){ifstream f(argv[1],ios::binary);f.read((char*)obs,sizeof(obs));array<unsigned char,3>e;while(f.read((char*)e.data(),3))do{bad[e[0]][e[1]]|=M(1)<<e[2];}while(next_permutation(e.begin(),e.end()));
 for(auto&r:costs)fill(r,r+26,1000000);
 for(int i=0;i<125;i++){int x=i/25;g[i]=25*((5-x)%5)+i%25;}
 for(int i=0;i<125;i++)if(i<=g[i]){groups.push_back((M(1)<<i)|(M(1)<<g[i]));amt.push_back(i==g[i]?1:2);par.push_back(i==g[i]);}
 dump.open(argv[2]);solve(0,0,0,0,0);cerr<<nodes<<endl;
 for(int n=1;n<=13;n++)for(int h=0;h<=25;h++)if(counts[n][h])cout<<n<<" "<<h<<" "<<counts[n][h]<<" "<<costs[n][h]<<endl;
}
