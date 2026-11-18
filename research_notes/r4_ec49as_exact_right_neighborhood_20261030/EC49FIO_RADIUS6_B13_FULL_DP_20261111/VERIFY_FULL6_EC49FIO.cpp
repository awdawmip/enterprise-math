#include <bits/stdc++.h>
using namespace std;
struct Node{int p;uint32_t support;int label;};
int main(int argc,char**argv){
 if(argc<4){cerr<<"USAGE trie cases B [limit]\n";return 2;}
 int B=atoi(argv[3]); int LIMIT=argc>4?atoi(argv[4]):0;
 int CAP=B+3;assert(CAP<255);
 ifstream in(argv[1]);vector<Node> tree;int a,b,c;
 while(in>>a>>b>>c){tree.push_back({a,(uint32_t)b,c?__builtin_ctz((unsigned)c):-1});}
 assert(tree.size()==42735);
 vector<array<uint8_t,64>> dp(tree.size());
 vector<vector<pair<int,int>>> terms(64);
 for(int s=1;s<64;s++)for(int t=s;t;t=(t-1)&s)terms[s].push_back({t,s^t});
 ifstream cases(argv[2]);string line;long long done=0,excl=0,possible=0;map<int,int>optHist;
 vector<string>possibleInputs;
 auto begin=chrono::steady_clock::now();
 while(getline(cases,line)){
  if(line.empty())continue;
  if(LIMIT>0&&done>=LIMIT)break;
  istringstream ss(line);int labels[24];fill(labels,labels+24,-1);uint32_t Q=0;
  for(int j=0;j<6;j++){int idx;ss>>idx;assert(idx>=0&&idx<24);labels[idx]=j;Q|=1u<<idx;}
  for(size_t u=0;u<tree.size();u++){
   auto &row=dp[u];row.fill((uint8_t)CAP);row[0]=0;
   if(tree[u].label>=0&&labels[tree[u].label]>=0)row[1<<labels[tree[u].label]]=0;
  }
  for(int u=(int)tree.size()-1;u>0;u--){
   auto &x=dp[tree[u].p],&y=dp[u];
   int edge=((tree[u].support&~Q)==0);
   for(int s=63;s>=1;s--){
    int best=x[s];
    for(auto [t,other]:terms[s]){
     int v=(int)x[other]+y[t]+edge;
     if(v<best)best=v;
    }
    x[s]=(uint8_t)min(best,CAP);
   }
  }
  int optimum=dp[0][63];optHist[optimum]++;
  if(optimum<=B){possible++;possibleInputs.push_back(line);}else excl++;
  done++;
  if(done%250==0)cerr<<"cases="<<done<<" possible="<<possible<<" excluded="<<excl
    <<" sec="<<chrono::duration<double>(chrono::steady_clock::now()-begin).count()<<"\n";
 }
 cout<<"{\"checked\":"<<done<<",\"excluded\":"<<excl<<",\"possible\":"<<possible
     <<",\"budget\":"<<B<<",\"optimal_new_prefix_hist\":{";
 bool first=true;for(auto [k,n]:optHist){if(!first)cout<<",";first=false;cout<<"\""<<k<<"\":"<<n;}
 cout<<"},\"elapsed_s\":"<<fixed<<setprecision(3)
     <<chrono::duration<double>(chrono::steady_clock::now()-begin).count()<<"}\n";
 for(auto &s:possibleInputs)cout<<"POSSIBLE "<<s<<"\n";
}
