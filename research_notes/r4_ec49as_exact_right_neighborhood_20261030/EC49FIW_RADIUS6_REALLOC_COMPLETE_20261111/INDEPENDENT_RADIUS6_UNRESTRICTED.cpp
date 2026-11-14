// Independently verify BRC six-label prefix minimum using actual attained labels.
// OR-coverage recurrence differs from requested-set subset partition solver.
#include <bits/stdc++.h>
using namespace std;
static constexpr int K=64, INF=30000;
struct Node{int ch[8]={};unsigned char labels=0;};
using A=array<short,K>;
vector<Node> tree;
int digit(char c){return c>='0'&&c<='9'?c-'0':c-'a'+10;}
int descend(const string& hex,bool add){int u=0;for(size_t i=0;i<hex.size();i+=2){int k=16*digit(hex[i])+digit(hex[i+1]);if(k<1||k>7)abort();if(!tree[u].ch[k]){if(!add)return -1;int v=tree.size();tree[u].ch[k]=v;tree.emplace_back();}u=tree[u].ch[k];}return u;}
int exact(const vector<string>& F){
 vector<unsigned char> old(tree.size());
 for(auto&p:F){auto v=descend(p,false);if(v>=0)old[v]=1;}
 vector<A> dp(tree.size());
 for(int v=int(tree.size())-1;v>=0;--v){
  A cur;cur.fill(INF);cur[tree[v].labels]=0;
  for(int k=1;k<=7;++k){
   int u=tree[v].ch[k];if(!u)continue;
   A next=cur;int edge=old[u]?0:1;
   for(int m=0;m<K;++m)if(cur[m]<INF){
     for(int s=1;s<K;++s)if(dp[u][s]<INF){
       int mm=m|s,cost=cur[m]+dp[u][s]+edge;
       if(cost<next[mm])next[mm]=cost;
     }
   }
   cur=next;
  }
  dp[v]=cur;
 }
 return dp[0][63];
}
int main(int argc,char**argv){if(argc!=2)return 2;ifstream in(argv[1]);int groups;in>>groups;if(groups!=6)abort();tree.emplace_back();for(int i=0;i<groups;++i){int n;in>>n;for(int j=0;j<n;++j){string w;in>>w;int v=descend(w,true);tree[v].labels|=1<<i;}}cout<<"INDEPENDENT_NODES "<<tree.size()<<"\n";for(int i=0;i<2;++i){string name;int n;in>>name>>n;if(n<=0 || n>94)abort();vector<string> f(n);for(auto&x:f)in>>x;auto t=chrono::steady_clock::now();int ans=exact(f);double sec=chrono::duration<double>(chrono::steady_clock::now()-t).count();cout<<"INDEPENDENT_B11 "<<name<<" "<<ans<<" sec="<<fixed<<setprecision(2)<<sec<<"\n";}}
