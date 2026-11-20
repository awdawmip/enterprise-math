// Exact cover of the histories outside an anchored orbit of five message classes.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
using Mask=__uint128_t;
constexpr Mask all=(Mask(1)<<125)-1;
int bit(Mask m){return std::uint64_t(m)?__builtin_ctzll(std::uint64_t(m)):64+__builtin_ctzll(std::uint64_t(m>>64));}
struct Table{int size,cost;std::vector<Mask> rows;};
struct Search{
 std::vector<Table> db;std::vector<std::vector<Mask>> anchor;
 std::vector<int> remaining;std::vector<Mask> path;
 std::uint64_t nodes=0;
 bool cover(Mask free,int labels,const std::vector<std::vector<Mask>>& possible){
  ++nodes;if(labels==1){for(int t=0;t<int(db.size());t++)if(remaining[t]){
    if(!std::binary_search(possible[t].begin(),possible[t].end(),free))return false;
    path.push_back(free);return true;}return false;}
  std::vector<std::vector<Mask>> pool(db.size());std::array<int,125> freq{};
  int best=1000000,choice=-1,point=-1;
  for(int t=0;t<int(db.size());t++)if(remaining[t]){
    auto& a=pool[t];for(Mask m:possible[t])if((free&m)==m)a.push_back(m);
    if(int(a.size())<remaining[t])return false;
    if(int(a.size())<best){best=a.size();choice=t;}
  }
  for(auto& a:pool)for(Mask m:a)for(Mask v=m;v;v&=v-1)freq[bit(v)]++;
  for(Mask v=free;v;v&=v-1){int i=bit(v);if(!freq[i])return false;
    if(freq[i]<best){best=freq[i];point=i;choice=-1;}}
  for(int t=0;t<int(db.size());t++)if(remaining[t]&&(choice<0||choice==t)){
    const auto a=pool[t];--remaining[t];
    for(int j=0;j<int(a.size());j++){
       Mask m=a[j];if(point>=0&&!(m&(Mask(1)<<point)))continue;
       if(point<0 && remaining[t])pool[t].assign(a.begin()+j+1,a.end());
       path.push_back(m);
       if(cover(free^m,labels-1,pool))return true;
       path.pop_back();
    }
    ++remaining[t];pool[t]=a;
  }return false;
 }
};
int main(int argc,char**argv){
 std::string folder=argv[1];int orbit=std::stoi(argv[2]),cap=std::stoi(argv[3]);
 int multiplicity=argc>4?std::stoi(argv[4]):5; bool neighbor=argc>5; std::string name=neighbor?"neighbor"+std::to_string(multiplicity):argc>4?"partial"+std::to_string(multiplicity):"single";
 std::ifstream bank(folder+"/bank"),sig(folder+"/"+name),pr(folder+"/profiles");
 Search S;int nt;bank>>nt;S.db.resize(nt);
 for(auto&t:S.db){int n;bank>>t.size>>t.cost>>n;for(int i=0;i<n;i++){std::uint64_t l,h;bank>>l>>h;t.rows.push_back((Mask(h)<<64)|l);}}
 int k;std::uint64_t l,h;std::vector<Mask> bundle(multiplicity);
 std::vector<int> kinds(multiplicity);
 for(int i=0;i<=orbit;i++){sig>>k>>l>>h;for(auto&m:bundle){std::uint64_t a,b;sig>>a>>b;m=(Mask(b)<<64)|a;} if(neighbor){for(int& t:kinds)sig>>t;}else std::fill(kinds.begin(),kinds.end(),k); }
 Mask free=all^((Mask(h)<<64)|l);S.anchor.resize(nt);
 for(int t=0;t<nt;t++)for(Mask m:S.db[t].rows)if((m&free)==m)S.anchor[t].push_back(m);
 S.remaining.resize(nt);int cost,id=0;
 while(pr>>cost){for(auto&n:S.remaining)pr>>n;int j=id++;
  if(cost>cap)continue;for(int t:kinds)--S.remaining[t]; if(*std::min_element(S.remaining.begin(),S.remaining.end())<0)continue;S.nodes=0;S.path.clear();
  bool yes=S.cover(free,13-multiplicity,S.anchor);std::cout<<j<<" "<<cost<<" "<<S.nodes<<" "<<yes<<std::endl;
  if(yes){auto print=[](Mask m){for(;m;m&=m-1)std::cerr<<bit(m)<<" ";std::cerr<<"\n";};for(Mask m:bundle)print(m);for(Mask m:S.path)print(m);break;}
 }
}
