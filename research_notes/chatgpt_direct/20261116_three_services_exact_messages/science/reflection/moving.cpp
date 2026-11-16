#include <algorithm>
#include <cstdint>
#include <fstream>
#include <stdexcept>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;using M=__uint128_t;using U=uint64_t;
M bad[125][125];vector<unordered_set<U>> out(14);int mate[125],orb[125];long long visits=0;
int first(M a){return uint64_t(a)?__builtin_ctzll((uint64_t)a):64+__builtin_ctzll((uint64_t)(a>>64));}
void dfs(int sz,M remaining,M*forb,U mask){visits++;if(sz>=14)throw std::runtime_error("unexpected moving size 14");if(sz>=8)out[sz].insert(mask);while(remaining){int v=first(remaining);remaining&=remaining-1;M eligible=remaining&~forb[v]&~(M(1)<<mate[v]);if(sz+1+__builtin_popcountll((U)eligible)+__builtin_popcountll((U)(eligible>>64))<8)continue;M nx[125];for(M s=eligible;s;s&=s-1){int j=first(s);nx[j]=forb[j]|bad[v][j];}dfs(sz+1,eligible,nx,mask|(U(1)<<orb[v]));}}
int main(){ifstream f("triples.bin",ios::binary);unsigned char e[3];while(f.read((char*)e,3))do{bad[e[0]][e[1]]|=M(1)<<e[2];}while(next_permutation(e,e+3));for(int v=25;v<125;v++){mate[v]=25*((5-v/25)%5)+v%25;orb[v]=min(v,mate[v])-25;}M U0=((M(1)<<125)-1)&~((M(1)<<26)-1)&~(M(1)<<100);dfs(1,U0,bad[25],1);ofstream fo("p8_seed.txt");for(int sz=8;sz<=13;sz++){cout<<sz<<" "<<out[sz].size()<<endl;for(auto m:out[sz])fo<<sz<<" "<<m<<"\n";}cout<<"visits "<<visits<<endl;}
