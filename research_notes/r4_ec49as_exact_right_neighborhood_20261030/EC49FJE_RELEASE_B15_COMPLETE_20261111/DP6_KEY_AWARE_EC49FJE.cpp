// EC49FJE exact one-extra-full-key six-demand signed native trie DP.
// Trie input: N, then N lines (parent,terminal_label_index(-1 means none),key_id).
// Terminal key_id=-1 is a fixed old key, 0..K-1 denotes a proposed new key.
// Cases: count, then each case: profile, count fixed-prefix node IDs, IDs,
// count candidate key IDs, IDs. For each candidate, solve exact full 6-label DP.
#include <bits/stdc++.h>
using namespace std;
const int S=64,CAP=18;struct Node{int p,lab,key;};
int main(int argc,char**argv){
 if(argc!=4){cerr<<"usage keydp TRIE CASES CSV\n";return 2;}
 ifstream in(argv[1]);int N;in>>N;vector<Node> t(N);
 for(auto &v:t)in>>v.p>>v.lab>>v.key;
 ifstream cs(argv[2]);int C;cs>>C;
 ofstream out(argv[3]);out<<"case,key_id,added,status\n";
 vector<array<uint8_t,S>> d(N);vector<uint8_t> first(N),F(N);
 vector<vector<pair<int,int>>> split(S);
 for(int s=1;s<S;s++)for(int j=s;j;j=(j-1)&s)split[s].push_back({j,s^j});
 for(int i=0;i<C;i++){
  char profile;int nf,nk;cs>>profile>>nf;fill(F.begin(),F.end(),0);
  for(int j=0,id;j<nf;j++){cs>>id;F[id]=1;}
  cs>>nk;vector<int> keys(nk);for(int &k:keys)cs>>k;
  for(int key:keys){
   fill(first.begin(),first.end(),0);
   for(int v=0;v<N;v++){
    int lab=(t[v].lab>=0 && (t[v].key==-1||t[v].key==key))?1<<t[v].lab:0;
    for(int mask=0;mask<S;mask++)d[v][mask]=(mask&~lab)?CAP:0;
   }
   for(int v=N-1;v>0;v--){
    int p=t[v].p,c=!F[v];auto &x=d[p],&y=d[v];
    bool oldterminal=t[p].lab>=0&&(t[p].key==-1||t[p].key==key);
    if(!first[p]&&!oldterminal){
     for(int s=1;s<S;s++)x[s]=min(CAP,(int)y[s]+c);
    }else{
     for(int s=S-1;s>=1;s--){
      int best=x[s];
      for(auto [z,r]:split[s])best=min(best,(int)x[r]+y[z]+c);
      x[s]=min(CAP,best);
     }
    }
    first[p]=1;
   }
   int val=d[0][63];out<<profile<<i<<","<<key<<","<<val<<","<<(val<=15?"POSSIBLE":"EXCLUDED")<<"\n";
  }
 }
}