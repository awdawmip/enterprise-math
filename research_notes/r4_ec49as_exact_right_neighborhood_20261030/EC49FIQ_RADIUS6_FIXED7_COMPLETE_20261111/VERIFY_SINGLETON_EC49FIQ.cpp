#include <bits/stdc++.h>
using namespace std;
// EC49FIQ exact singleton signed-prefix cost: use trie from EC49FIO.
// Input rows: parent_id, 24-bit original-prefix-support, terminal 24-bit label.
// Usage: ./ec49fiq_singleton TRIE_A.txt QS_A_3.txt 3
struct Node{int parent; uint32_t sup; int label;};
int main(int argc,char **argv){
  if(argc!=4)return 2;
  int B=atoi(argv[3]);ifstream fi(argv[1]);vector<Node> v;int a,b,c;
  while(fi>>a>>b>>c)v.push_back({a,(uint32_t)b,c?__builtin_ctz((unsigned)c):-1});
  assert(v.size()==42735);
  vector<unsigned short> dist(v.size());ifstream in(argv[2]);string line;
  long long count=0,excluded=0,survived=0;
  while(getline(in,line)){
    if(line.empty())continue;
    istringstream ss(line);array<int,24> local;local.fill(-1);
    int q[6];uint32_t mask=0;
    for(int j=0;j<6;j++){if(!(ss>>q[j]))return 3;assert(q[j]>=0&&q[j]<24);local[q[j]]=j;mask|=1u<<q[j];}
    int best[6]={1000000,1000000,1000000,1000000,1000000,1000000};dist[0]=0;
    for(int u=1;u<(int)v.size();u++){
      dist[u]=dist[v[u].parent]+((v[u].sup&~mask)==0);
      int lab=v[u].label;
      if(lab>=0&&local[lab]>=0)best[local[lab]]=min(best[local[lab]],(int)dist[u]);
    }
    bool fail=false;for(int j=0;j<6;j++)if(best[j]>B)fail=true;
    if(fail)excluded++;else{survived++;cout<<"SURV "<<line<<"\n";}
    count++;
  }
  cerr<<"{\"checked\":"<<count<<",\"singleton_excluded\":"<<excluded
      <<",\"survivors\":"<<survived<<",\"B\":"<<B<<"}\n";
}
