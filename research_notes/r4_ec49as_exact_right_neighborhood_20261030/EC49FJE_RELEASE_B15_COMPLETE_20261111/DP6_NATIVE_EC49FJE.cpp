// EC49FJE full native-prefix Steiner DP, support as in frozen EC49FIO.
// Input trie rows: parent, original-word support mask, terminal one-hot demand mask.
// Input cases: six changed demand IDs per line. Cost cap = B+3.
#include <bits/stdc++.h>
using namespace std;
struct Node { int parent; uint32_t support; int label; };
int main(int argc,char **argv){
 if(argc<4){cerr<<"usage: dp6_native TRIE CASES B [LIMIT]\n";return 2;}
 const int B=atoi(argv[3]), CAP=B+3, LIMIT=argc>4?atoi(argv[4]):0;
 if(CAP>=255)return 2;
 ifstream in(argv[1]);vector<Node> tree;int a,b,c;
 while(in>>a>>b>>c)tree.push_back({a,(uint32_t)b,c?__builtin_ctz((unsigned)c):-1});
 vector<array<uint8_t,64>> d(tree.size());
 vector<vector<pair<int,int>>> splits(64);
 for(int s=1;s<64;s++)for(int t=s;t;t=(t-1)&s)splits[s].push_back({t,s^t});
 ifstream cases(argv[2]);string line;int tested=0,rejected=0,possible=0;map<int,int> hist;
 while(getline(cases,line)){
  if(line.empty())continue;if(LIMIT && tested>=LIMIT)break;
  istringstream ss(line);int labels[24];fill(labels,labels+24,-1);
  uint32_t Q=0;for(int j=0;j<6;j++){int i;ss>>i; if(i<0||i>=24)return 3;labels[i]=j;Q|=1u<<i;}
  for(size_t i=0;i<tree.size();i++){
   auto &r=d[i];r.fill((uint8_t)CAP);r[0]=0;
   if(tree[i].label>=0 && labels[tree[i].label]>=0)r[1<<labels[tree[i].label]]=0;
  }
  for(int v=(int)tree.size()-1;v>0;v--){
   auto &parent=d[tree[v].parent],&child=d[v];
   int cost=((tree[v].support&~Q)==0);
   for(int mask=63;mask>=1;mask--){
    int best=parent[mask];
    for(auto [sub,rest]:splits[mask])best=min(best,(int)parent[rest]+child[sub]+cost);
    parent[mask]=(uint8_t)min(best,CAP);
   }
  }
  int optimum=d[0][63];hist[optimum]++;tested++;if(optimum<=B){possible++;cout<<"POSSIBLE "<<line<<"\n";}else rejected++;
 }
 cerr<<"checked="<<tested<<" excluded="<<rejected<<" possible="<<possible<<"\n";
 for(auto [v,n]:hist)cerr<<"cost_"<<v<<"="<<n<<"\n";
}