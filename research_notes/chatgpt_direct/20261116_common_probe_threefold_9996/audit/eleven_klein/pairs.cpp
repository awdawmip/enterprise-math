#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <vector>
using U=uint64_t;using M=__uint128_t;using W=std::array<U,4>;
int bit(M m){return U(m)?__builtin_ctzll(U(m)):64+__builtin_ctzll(U(m>>64));}int pc(M m){return __builtin_popcountll(U(m))+__builtin_popcountll(U(m>>64));}
W obs[125][125];M bad[125][125];std::vector<M>choices[125];int g[125],n;int caps[]={0,0,0,0,0,0,0,0,581,761,951,1131,1311,1498};struct Row{M m;int c;};std::unordered_map<U,Row>seen;long long nodes=0;
int cost(M m){int v=0;for(M a=m;a;a&=a-1){W w{};int i=bit(a);for(M b=m;b;b&=b-1)for(int j=0;j<4;j++)w[j]|=obs[i][bit(b)][j];for(U a:w)v+=__builtin_popcountll(a);}return v;}
void dfs(int start,U support,M m,M ban,int s){++nodes;if(s>=8){int c=cost(m);if(c<=caps[s]){auto it=seen.find(support);if(it==seen.end()||it->second.c>c)seen[support]={m,c};}}
 for(int k=start;k<n;k++)for(M w:choices[k]){int z=s+pc(w);if(z>13||ban&w)continue;M old=m,f=ban;bool ok=true;for(M b=w;b;b&=b-1){int j=bit(b);if((f>>j)&1){ok=false;break;}for(M a=old;a;a&=a-1)f|=bad[j][bit(a)];old|=M(1)<<j;}if(ok)dfs(k+1,support|U(1)<<k,old,f,z);if(!m)break;}}
int main(int argc,char**argv){std::ifstream in(argv[1],std::ios::binary),perm(argv[2]);in.read((char*)obs,sizeof(obs));std::array<unsigned char,3>e;while(in.read((char*)e.data(),3))do{bad[e[0]][e[1]]|=M(1)<<e[2];}while(std::next_permutation(e.begin(),e.end()));int gg[4][125];for(int jj=0;jj<=atoi(argv[3]);jj++)for(auto&r:gg)for(int&x:r)perm>>x;int ix=atoi(argv[4]);bool indexed[125]{};
 for(int i=0;i<125;i++)if(!indexed[i]){std::vector<int>w;for(auto&a:gg)if(!indexed[a[i]]){indexed[a[i]]=true;w.push_back(a[i]);}std::vector<M>cos;for(int k:w){M m=(M(1)<<k)|(M(1)<<gg[ix][k]);if(std::find(cos.begin(),cos.end(),m)==cos.end())cos.push_back(m);}if(cos.size()==2)choices[n]=cos;n++;}dfs(0,0,0,0,0);std::cerr<<n<<' '<<nodes<<' '<<seen.size()<<'\n';for(auto [q,r]:seen)std::cout<<q<<' '<<r.c<<' '<<U(r.m)<<' '<<U(r.m>>64)<<'\n';}
