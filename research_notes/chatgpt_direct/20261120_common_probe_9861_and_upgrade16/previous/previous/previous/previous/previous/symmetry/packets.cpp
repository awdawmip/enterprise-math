#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using Mask=__uint128_t;
using Row=std::array<std::uint64_t,4>;
Mask bad[125][125];
Row obs[125][125];
int first(Mask m) {return uint64_t(m)?std::countr_zero(uint64_t(m)):64+std::countr_zero(uint64_t(m>>64));}
int count(Mask m) {return std::popcount(uint64_t(m))+std::popcount(uint64_t(m>>64));}
Mask sets[12],forbidden[12];
int k,lowest;std::uint64_t nodes,solutions;
std::array<Mask,12> best;
int cost(Mask points) {
 int q=0;
 for(Mask m=points;m;m&=m-1){
  Row u{};
  for(Mask r=points;r;r&=r-1)for(int w=0;w<4;w++)u[w]|=obs[first(m)][first(r)][w];
  for(auto v:u)q+=std::popcount(v);
 }
 return q;
}
void solve(Mask todo,int used) {
 ++nodes;
 if(!todo){
  if(used!=k)return;
  solutions++;int sum=0;
  for(int j=0;j<k;j++)sum+=cost(sets[j]);
  if(sum<lowest){lowest=sum;std::copy_n(sets,k,best.begin());}
  return;
 }
 Mask layers[13]{todo};
 int capacity=0;
 const int rem=count(todo);
 for(int j=0;j<k;j++){
  Mask choices=todo&~forbidden[j];int limit=13-count(sets[j]);
  if(!limit)choices=0;
  capacity+=std::min(limit,count(choices));
  for(int p=j+1;p>0;p--)layers[p]|=layers[p-1]&choices;
 }
 if(layers[1]!=todo || capacity<rem)return;
 int c=1;
 while(c<k&&layers[c+1]==todo)c++;
 int v=first(layers[c]&~layers[c+1]);Mask bit=Mask(1)<<v;
 for(int j=0;j<std::min(used+1,k);j++){
  if((forbidden[j]&bit)||count(sets[j])==13)continue;
  auto before=forbidden[j];
  for(Mask m=sets[j];m;m&=m-1)forbidden[j]|=bad[v][first(m)];
  sets[j]|=bit;solve(todo^bit,std::max(used,j+1));sets[j]^=bit;forbidden[j]=before;
 }
}
int main(int argc,char**argv){
 std::ifstream f(argv[1],std::ios::binary);
 f.read(reinterpret_cast<char*>(obs),sizeof(obs));
 std::array<unsigned char,3> edge;
 while(f.read(reinterpret_cast<char*>(edge.data()),3))do{bad[edge[0]][edge[1]]|=Mask(1)<<edge[2];}while(std::next_permutation(edge.begin(),edge.end()));
 int n;
 while(std::cin>>k>>n){
  std::vector<int> labels(k+1);for(int&l:labels)std::cin>>l;
  Mask points=0;
  for(int j=0;j<n;j++){int p;std::cin>>p;points|=Mask(1)<<p;}
  nodes=solutions=0;lowest=100000;
  if(n<=13*k)solve(points,0);
  for(int l:labels)std::cout<<l<<" ";
  std::cout<<nodes<<" "<<solutions<<" "<<lowest;
  if(solutions)for(int j=0;j<k;j++)std::cout<<" "<<uint64_t(best[j])<<" "<<uint64_t(best[j]>>64);
  std::cout<<std::endl;
 }
}
