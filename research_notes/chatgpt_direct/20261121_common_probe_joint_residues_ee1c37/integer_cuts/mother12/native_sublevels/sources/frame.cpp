#include <memory>
#include <cstdint>
#include <algorithm>
#include <array>
#include <bit>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <vector>
#include <cstring>
using namespace std;using W=uint64_t;using M=__uint128_t;
using Group=array<unsigned char,125>;using Frame=array<unsigned char,7>;
int at(M x){return W(x)?countr_zero(W(x)):64+countr_zero(W(x>>64));}
int main(int argc,char**argv){
  ifstream in(argv[1]);array<M,250> p;map<M,int> ids;for(int i=0;i<250;i++){W l,h;in>>l>>h;p[i]=(M(h)<<64)|l;ids[p[i]]=i;}
  vector<array<unsigned char,250>> rotations;array<vector<int>,250> mapsToZero;
  Group g{};ifstream f(argv[2],ios::binary);while(f.read((char*)g.data(),125)){
    array<unsigned char,250> a{};for(int i=0;i<250;i++){
      M n=0;for(M m=p[i];m;m&=m-1)n|=M(1)<<g[at(m)];a[i]=ids.at(n);if(!a[i])mapsToZero[i].push_back(rotations.size());}
    rotations.push_back(a);
  }
  // For a lexicographically least sorted image its second index is globally least
 // over all ordered pairs sent to (0,b). Only transformations attaining this
 // exact minimum can witness the least tuple.
 array<array<unsigned char,250>,250> second{};
 using Options=array<array<vector<int>,250>,250>;
 auto images=make_unique<Options>();
 for(int i=0;i<250;i++)for(int j=0;j<250;j++)if(i!=j){
   int best=255;auto& options=(*images)[i][j];
   for(int id:mapsToZero[i]){
     int b=rotations[id][j];
     if(b<best){best=b;options.clear();}
     if(b==best)options.push_back(id);
   }
   second[i][j]=best;
 }
 int k=stoi(argv[3]);if(k<2||k>7)return 2;string line;set<Frame> visited;long long all=0;
  while(getline(cin,line)){if(line.empty()||line[0]!='0')continue;++all;istringstream seq(line);Frame input{};for(int i=0,x;i<k;i++){seq>>x;input[i]=x;}
    Frame best{};best.fill(255);
    int least=255;
    for(int a=0;a<k;a++)for(int b=0;b<k;b++)if(a!=b)least=min(least,int(second[input[a]][input[b]]));
    for(int a=0;a<k;a++)for(int b=0;b<k;b++)if(a!=b && second[input[a]][input[b]]==least)
      for(int j:(*images)[input[a]][input[b]]){
      const auto& perm=rotations[j];Frame candidate{};for(int z=0;z<k;z++)candidate[z]=perm[input[z]];
      sort(candidate.begin(),candidate.begin()+k);if(candidate<best)best=candidate;
    }
    if(visited.insert(best).second){for(int i=0;i<k;i++)cout<<int(best[i])<<" ";cout<<"\n";}
  }
  cerr<<all<<" "<<visited.size()<<endl;
}
