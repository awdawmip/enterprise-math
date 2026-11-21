#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <vector>
using U=uint64_t;using M=__uint128_t;using W=std::array<U,4>;
int bit(M m){return U(m)?__builtin_ctzll(U(m)):64+__builtin_ctzll(U(m>>64));}int pc(M m){return __builtin_popcountll(U(m))+__builtin_popcountll(U(m>>64));}
W obs[125][125];M bad[125][125];std::vector<M>choices[45];int g[125],n;int caps[]={0,0,0,0,0,0,0,0,581,761,951,1131,1311,1498};struct Row{M m;int c;};std::unordered_map<U,Row>seen;long long nodes=0;
int cost(M m){int v=0;for(M a=m;a;a&=a-1){W w{};int i=bit(a);for(M b=m;b;b&=b-1)for(int j=0;j<4;j++)w[j]|=obs[i][bit(b)][j];for(U a:w)v+=__builtin_popcountll(a);}return v;}
void dfs(int start,U support,M m,M ban,int s){++nodes;if(s>=8){int c=cost(m);if(c<=caps[s]){auto it=seen.find(support);if(it==seen.end()||it->second.c>c)seen[support]={m,c};}}
 for(int k=start;k<n;k++)for(M w:choices[k]){int z=s+pc(w);if(z>13||ban&w)continue;M old=m,f=ban;bool ok=true;for(M b=w;b;b&=b-1){int j=bit(b);if((f>>j)&1){ok=false;break;}for(M a=old;a;a&=a-1)f|=bad[j][bit(a)];old|=M(1)<<j;}if(ok)dfs(k+1,support|U(1)<<k,old,f,z);if(!m)break;}}
int main(int argc,char**argv){std::ifstream in(argv[1],std::ios::binary),perm(argv[2]);in.read((char*)obs,sizeof(obs));std::array<unsigned char,3>e;while(in.read((char*)e.data(),3))do{bad[e[0]][e[1]]|=M(1)<<e[2];}while(std::next_permutation(e.begin(),e.end()));for(int&i:g)perm>>i;bool indexed[125]{};for(int i=0;i<125;i++)if(!indexed[i]){std::vector<int>cy;int t=i;do{indexed[t]=true;cy.push_back(t);t=g[t];}while(t!=i);if(cy.size()%2==0){M v[2]{};for(int j=0;j<cy.size();j++)v[j%2]|=M(1)<<cy[j];choices[n]={v[0],v[1]};}n++;}dfs(0,0,0,0,0);std::cerr<<n<<' '<<nodes<<' '<<seen.size()<<'\n';for(auto [q,r]:seen)std::cout<<q<<' '<<r.c<<' '<<U(r.m)<<' '<<U(r.m>>64)<<'\n';}
