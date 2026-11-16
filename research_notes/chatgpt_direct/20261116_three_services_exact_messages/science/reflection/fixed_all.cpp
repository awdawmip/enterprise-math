#include <algorithm>
#include <array>
#include <cstdio>
#include <cstdint>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;using M=__uint128_t;
M bad[125][125],orbit[75];uint64_t count_[25][26];M witness_[25][26];
int first(M a){return uint64_t(a)?__builtin_ctzll((uint64_t)a):64+__builtin_ctzll((uint64_t)(a>>64));}
bool compatible(M s,M o){ M full=s|o;
 for(M z=o;z;z&=z-1){int a=first(z);for(M q=full;q;q&=q-1){int b=first(q);if(bad[a][b]&full)return false;}}
 return true;}
int maxp[26];ofstream frontier;
void dfs(M occupied,M mask,int a,int b,int start,M candidates){
 count_[a][b]++;witness_[a][b]=mask;
 if(a+2*b>=1)frontier<<(uint64_t)(mask>>64)<<" "<<(uint64_t)mask<<" "<<a<<" "<<b<<"\n";
 while(candidates){
  int i=first(candidates);candidates&=candidates-1;
  M s=occupied|orbit[i],cand=0;
  for(M z=candidates;z;z&=z-1){int j=first(z);if(compatible(s,orbit[j]))cand|=M(1)<<j;}
  dfs(s,mask|(M(1)<<i),a+(i<25),b+(i>=25),i+1,cand);
 }
}
int main(){ifstream fin("triples.bin",ios::binary);unsigned char e[3];while(fin.read((char*)e,3))do{bad[e[0]][e[1]]|=M(1)<<e[2];}while(next_permutation(e,e+3));int k=0;for(int i=0;i<125;i++){int j=25*((5-i/25)%5)+i%25;if(i<=j)orbit[k++]=M(1)<<i|M(1)<<j;}frontier.open("fixed_all_masks.txt");dfs(0,0,0,0,0,(M(1)<<75)-1);for(int a=0;a<=20;a++)for(int b=0;b<=25;b++)if(count_[a][b])cout<<a<<" "<<b<<" "<<count_[a][b]<<endl;}
