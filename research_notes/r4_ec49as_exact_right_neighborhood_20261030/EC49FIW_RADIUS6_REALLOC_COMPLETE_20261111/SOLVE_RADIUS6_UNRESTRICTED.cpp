// Exact signed-native-prefix Steiner coverage for six frozen BRC observation demands.
// Input: manifest generated from pinned legal-word grammar. Objective: minimum
// number of distinct new full signed microstep prefixes, unrestricted cache keys.
// Compile: g++ -std=c++17 -O3 SOLVE_RADIUS6_UNRESTRICTED.cpp -o solve_all
#include <bits/stdc++.h>
using namespace std;
constexpr int D = 6, K = 1 << D, INF = 30000;
struct Node {
    int child[8]={};
    unsigned char labels=0;
};
using V = array<short,K>;
vector<Node> tr;
int digit(char c){ if(c>='0'&&c<='9') return c-'0'; if(c>='a'&&c<='f')return c-'a'+10; throw runtime_error("bad hex digit");}
int descend(const string& h, bool create){
 int v=0;
 for(size_t i=0;i<h.size();i+=2){
  int code = digit(h[i])*16+digit(h[i+1]);
  if(code<1||code>7)throw runtime_error("bad signed microstep");
  if(!tr[v].child[code]){
   if(!create)return -1;
   int u=int(tr.size()); tr[v].child[code]=u;tr.emplace_back();
  }
  v=tr[v].child[code];
 }
 return v;
}
void init(){tr.clear();tr.emplace_back();}
int solve(const vector<string>& F,long long& branching,long long& nodevis){
 vector<uint8_t> freeprefix(tr.size(),0);
 for(auto&s:F){int v=descend(s,false);if(v>=0)freeprefix[v]=1;}
 vector<V> dp(tr.size());
 branching=0;nodevis=0;
 for(int v=(int)tr.size()-1;v>=0;--v){
  ++nodevis;
  auto& cur=dp[v];
  unsigned char L=tr[v].labels;
  for(int m=0;m<K;++m)cur[m]=(m & (~int(L)))?INF:0;
  for(int a=1;a<=7;++a){
   int u=tr[v].child[a]; if(!u)continue;
   auto& sub=dp[u];
   short edgecost = freeprefix[u] ? 0 : 1;
   if(L==0 && cur[0]==0 && all_of(cur.begin()+1,cur.end(),[](short x){return x==INF;})){
     for(int m=1;m<K;++m) cur[m]=(sub[m]==INF?INF:sub[m]+edgecost);
   } else {
     ++branching;
     V next;
     for(int m=0;m<K;++m){
       int best=cur[m];
       for(int s=m;s;s=(s-1)&m){
         int x=cur[m^s],y=sub[s];
         if(x < INF && y < INF && x+y+edgecost < best) best=x+y+edgecost;
       }
       next[m]=short(best);
     }
     cur=next;
   }
   L=0;
  }
 }
 return dp[0][K-1];
}
int main(int argc,char** argv){
 if(argc!=2){cerr<<"usage: solve_all input.txt\n";return 2;}
 ifstream in(argv[1]);if(!in){cerr<<"cannot open input\n";return 2;}
 int groups;in>>groups;if(groups!=D)throw runtime_error("wrong group count");
 init();
 for(int j=0;j<D;++j){
  int n;in>>n;
  for(int t=0;t<n;++t){string word;in>>word; int v=descend(word,true);tr[v].labels |= (1 << j);}
 }
 cout<<"TREE_NODES "<<tr.size()<<"\n";
 for(int prof=0;prof<2;++prof){
  string id;int n;in>>id>>n;
  if(n<=0 || n>94 || (id!="A"&&id!="B"))throw runtime_error("background count or profile mismatch");
  vector<string> F(n);for(string& x:F)in>>x;
  long long branch,processed;
  auto start=chrono::steady_clock::now();
  int m=solve(F,branch,processed);
  double seconds=chrono::duration<double>(chrono::steady_clock::now()-start).count();
  cout<<"B11_EXACT "<<id<<" "<<m<<" "<<processed<<" "<<branch<<" "<<fixed<<setprecision(3)<<seconds<<"\n";
 }
}
