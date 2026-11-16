// Search partitions on the point orbits of a prime-order affine transformation.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using Mask=__uint128_t;
int first(Mask m){return std::uint64_t(m)?__builtin_ctzll(std::uint64_t(m)):64+__builtin_ctzll(std::uint64_t(m>>64));}
struct Kind{int size,cost;std::vector<Mask> masks;};
struct Tile{Mask support,seed;int type,labels;};
struct Problem{
 int prime,n=0;
 std::array<int,125> action{},index{};
 std::vector<Tile> tiles;
 std::vector<std::vector<int>> on, fixed;
 std::vector<int> left,path;
 std::uint64_t nodes=0;
 Mask image(Mask m) const{
    Mask r=0;
    while(m){int i=first(m);m&=m-1;r|=Mask(1)<<action[i];}
    return r;
 }
 void build(const std::vector<Kind>& k){
    index.fill(-1);
    for(int i=0;i<125;i++)if(index[i]<0){int j=i;do{index[j]=n;j=action[j];}while(i!=j);n++;}
    on.resize(n);fixed.resize(k.size());
    for(int t=0;t<int(k.size());t++){
      std::set<std::pair<Mask,int>> seen;
      for(Mask m:k[t].masks){
        Mask u=m,r=image(m);int l=1;
        while(r!=m&&r>=m&&!(u&r)){u|=r;r=image(r);l++;}
        if(r!=m)continue;
        Mask cover=0;
        for(Mask a=u;a;a&=a-1)cover|=Mask(1)<<index[first(a)];
        if(!seen.insert({cover,l}).second)continue;
        int id=tiles.size();tiles.push_back({cover,m,t,l});
        if(l==1)fixed[t].push_back(id);
        for(Mask a=cover;a;a&=a-1)on[first(a)].push_back(id);
      }
    }
 }
 bool search(Mask free){
    nodes++;
    if(!free)return std::all_of(left.begin(),left.end(),[](int a){return !a;});
    for(int t=0;t<int(left.size());t++)if(int need=left[t]%prime){
       for(auto j:fixed[t])if((tiles[j].support&free)==tiles[j].support&&!--need)break;
       if(need)return false;
    }
    std::vector<int> best;
    for(Mask a=free;a;a&=a-1){
      std::vector<int> choices;
      for(int j:on[first(a)]){
        const auto& row=tiles[j];
        if(left[row.type]>=row.labels&&(row.support&free)==row.support){
            choices.push_back(j);if(!best.empty()&&choices.size()>=best.size())break;
        }
      }
      if(choices.empty())return false;
      if(best.empty()||choices.size()<best.size())best.swap(choices);
    }
    for(int j:best){const auto& row=tiles[j];left[row.type]-=row.labels;path.push_back(j);
      if(search(free^row.support))return true;
      left[row.type]+=row.labels;path.pop_back();}
    return false;
 }
};
int main(int argc,char**argv){
 std::string d=argv[1];int chosen=std::stoi(argv[2]);std::ifstream input(d+"/bank"),syms(d+"/maps");
 int nt;input>>nt;std::vector<Kind> k(nt);
 for(auto& a:k){int n;input>>a.size>>a.cost>>n;while(n--){std::uint64_t lo,hi;input>>lo>>hi;a.masks.push_back((Mask(hi)<<64)|lo);}}
 for(int h=0;h<=chosen;h++){
  Problem b;syms>>b.prime;for(auto& i:b.action)syms>>i;if(h!=chosen)continue;b.build(k);
  std::ifstream ps(d+"/profiles");b.left.resize(nt);int cost,id=0;
  while(ps>>cost){for(auto& c:b.left)ps>>c;b.nodes=0;b.path.clear();bool ok=b.search((Mask(1)<<b.n)-1);
    std::cout<<id++<<" "<<cost<<" "<<b.nodes<<" "<<ok<<std::endl;
    if(ok){for(int j:b.path){const auto& tile=b.tiles[j];Mask m=tile.seed;
     for(int s=0;s<tile.labels;s++,m=b.image(m)){std::cerr<<"row ";for(Mask v=m;v;v&=v-1)std::cerr<<first(v)<<" ";std::cerr<<"\n";}}
     return 0;}
  }
 }
}
