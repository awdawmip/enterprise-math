// Exact nine-slot support-family quotient, given forward-edge binary from
// build_pair_binary.py. No floating point, no probabilistic equality.
#include <bits/stdc++.h>
using namespace std;
constexpr int M=256,N=101;
const int context_fixed[]={18,24,82,34,17,144,208};
vector<uint8_t> edges;
inline bool edge(int k,int i,int j){return edges[(size_t)k*M*M+i*M+j]!=0;}
string signature(int x,int y){
 int h[9]={18,24,82,34,17,x,144,208,y};
 string out;out.reserve(N*16);
 for(int k=0;k<N;k++){
   unsigned masks[9];int n=0;
   for(int i=0;i<9;i++){
     unsigned m=0;
     for(int j=0;j<9;j++)if(edge(k,h[i],h[j]))m|=1u<<j;
     bool dupe=false;
     for(int j=0;j<n;j++)if(masks[j]==m){dupe=true;break;}
     if(!dupe)masks[n++]=m;
   }
   unsigned maximal[9];int nm=0;
   for(int i=0;i<n;i++){
     bool proper=false;
     for(int j=0;j<n;j++)if(i!=j && masks[i]!=masks[j] &&
       (masks[i]&masks[j])==masks[i]){proper=true;break;}
     if(!proper)maximal[nm++]=masks[i];
   }
   sort(maximal,maximal+nm);
   out.push_back(char(nm));
   for(int i=0;i<nm;i++){
     out.push_back(char(maximal[i]&255));
     out.push_back(char(maximal[i]>>8));
   }
 }
 return out;
}
int main(int argc,char**argv){
 if(argc!=3){cerr<<"Usage: pair_quotient FORWARD.bin CLASSES.tsv\n";return 2;}
 ifstream f(argv[1],ios::binary);
 edges.assign(istreambuf_iterator<char>(f),{});
 if(edges.size()!=size_t(N)*M*M){cerr<<"BAD_EDGE_BYTES "<<edges.size()<<"\n";return 2;}
 bool fixed_set[M]={};
 for(int a:context_fixed)fixed_set[a]=true;
 unordered_map<string,int> keys;keys.reserve(40000);
 vector<vector<pair<int,int>>> groups;
 size_t pairs=0;
 for(int x=0;x<M;x++)if(!fixed_set[x])
  for(int y=x+1;y<M;y++)if(!fixed_set[y]){
   ++pairs;
   string key=signature(x,y);
   auto [it,inserted]=keys.emplace(move(key),int(groups.size()));
   if(inserted)groups.push_back({});
   groups[it->second].push_back({x,y});
  }
 sort(groups.begin(),groups.end(),[](const auto &a,const auto &b){return a[0]<b[0];});
 ofstream out(argv[2]);
 out<<"group\trepresentative_x\trepresentative_y\tcount\tmembers\n";
 size_t non_single=0,largest=0;
 for(size_t i=0;i<groups.size();i++){
  const auto &g=groups[i];
  non_single+=(g.size()>1);
  largest=max(largest,g.size());
  out<<i<<'\t'<<g[0].first<<'\t'<<g[0].second<<'\t'<<g.size()<<'\t';
  for(size_t j=0;j<g.size();j++){
   if(j)out<<',';
   out<<g[j].first<<':'<<g[j].second;
  }
  out<<'\n';
 }
 cout<<"PAIRS="<<pairs<<" GROUPS="<<groups.size()
     <<" NONSINGLETON_GROUPS="<<non_single
     <<" REDUNDANT="<<(pairs-groups.size())
     <<" MAX_GROUP="<<largest<<"\n";
}
