#include <bits/stdc++.h>
using namespace std;
constexpr int T[9][6]={{1,2,3,1,4,5},{1,6,7,1,1,1},{2,2,8,2,2,2},{3,8,3,3,3,3},{4,2,7,4,4,4},{5,6,3,5,5,5},{6,6,8,6,6,6},{7,8,7,7,7,7},{8,8,8,8,8,8}};
constexpr int S[9]={0,0,4,1,16,32,8,2,0};
const vector<vector<int>> A={{-1,-1},{1,2,-1,-2},{2,1,-2,-1},{3,1,1,-3},{1,-1},{2,-2}};
constexpr char O[]="acdefg";
inline int di(int a){return 2*(abs(a)-1)+(a<0);}
struct Node { uint32_t c[6]{}; uint8_t end=0,cost=1; uint8_t pad[2]{}; };
static_assert(sizeof(Node)==28);
vector<Node> tr,bt;
uint64_t candidate=0,legalkeys=0,usedkeys=0,states=0;
vector<int> path;
void addbase(string w){uint32_t v=0;for(char x:w)for(int s:A[strchr(O,x)-O]){int d=di(s);if(!bt[v].c[d]){bt[v].c[d]=bt.size();bt.emplace_back();}v=bt[v].c[d];}}
void addword(int q){int sig=S[q];if(sig!=1&&sig!=2&&sig!=4&&sig!=8)return;candidate++;
  uint32_t v=0,b=0;
  for(int a:path){int d=di(a);
    uint32_t nb=(b!=UINT32_MAX&&bt[b].c[d])?bt[b].c[d]:UINT32_MAX;
    if(!tr[v].c[d]){uint32_t t=tr.size();tr[v].c[d]=t;Node n;n.cost=(nb==UINT32_MAX);tr.push_back(n);}
    v=tr[v].c[d];b=nb;
  }
  tr[v].end|=1<<(sig==1?0:sig==2?1:sig==4?2:3);
}
void rec(int n[6],int q){bool empty=true;for(int j=0;j<6;j++)if(n[j]){empty=false;break;}
 if(empty){addword(q);return;}
 for(int j=0;j<6;j++)if(n[j]){n[j]--;for(int a:A[j])path.push_back(a);rec(n,T[q][j]);for(size_t i=0;i<A[j].size();i++)path.pop_back();n[j]++;}
}
using Row=array<uint16_t,16>;
vector<Row> dp;
constexpr uint16_t INF=65535;
void solve(){
 dp.resize(tr.size());
 for(size_t ii=tr.size();ii-->0;){
   auto &d=dp[ii];d.fill(INF);d[0]=0;int e=tr[ii].end;
   for(int s=e;s;s=(s-1)&e)d[s]=0;
   for(int j=0;j<6;j++){uint32_t ch=tr[ii].c[j];if(!ch)continue;
     Row nxt=d;auto &child=dp[ch];int edge=tr[ch].cost;
     for(int a=0;a<16;a++)if(d[a]!=INF)for(int b=1;b<16;b++)if(!(a&b)&&child[b]!=INF){
       int m=a|b;int val=d[a]+child[b]+edge;if(val<nxt[m])nxt[m]=val;
     }
     d=nxt;
   }
   for(int s=0;s<16;s++)if(d[s]!=INF)states++;
 }
}
vector<pair<string,int>> witness;
void trace(uint32_t v,int want,vector<int>& steps){
 vector<pair<uint32_t,int>> kids;for(int j=0;j<6;j++)if(tr[v].c[j])kids.push_back({tr[v].c[j],j});
 int nc=kids.size(),e=tr[v].end;
 vector<Row> layer(nc+1);vector<array<uint8_t,16>> fromS(nc+1),fromT(nc+1);
 layer[0].fill(INF);layer[0][0]=0;for(int s=e;s;s=(s-1)&e)layer[0][s]=0;
 for(int i=0;i<nc;i++){
   layer[i+1]=layer[i];for(int s=0;s<16;s++){fromS[i+1][s]=s;fromT[i+1][s]=0;}
   uint32_t ch=kids[i].first;int edge=tr[ch].cost;
   for(int a=0;a<16;a++)if(layer[i][a]!=INF)for(int b=1;b<16;b++)if(!(a&b)&&dp[ch][b]!=INF){
     int m=a|b,val=layer[i][a]+dp[ch][b]+edge;
     if(val<layer[i+1][m]){layer[i+1][m]=val;fromS[i+1][m]=a;fromT[i+1][m]=b;}
   }
 }
 if(layer[nc][want]!=dp[v][want])abort();
 int mask=want;
 for(int i=nc;i>=1;i--){
   int b=fromT[i][mask],a=fromS[i][mask];
   if(b){int d=kids[i-1].second;steps.push_back((d%2?-1:1)*(d/2+1));trace(kids[i-1].first,b,steps);steps.pop_back();}
   mask=a;
 }
 if(mask){
   vector<int> z=steps;string w;
   for(size_t i=0;i<z.size();){bool found=false;for(int j=0;j<6;j++)if(i+A[j].size()<=z.size()&&equal(A[j].begin(),A[j].end(),z.begin()+i)){w+=O[j];i+=A[j].size();found=true;break;}if(!found)abort();}
   witness.push_back({w,mask==1?1:mask==2?2:mask==4?4:8});
 }
}
int main(int argc,char**argv){
 int h=argc>1?atoi(argv[1]):9;
 tr.reserve(6000000);bt.reserve(40);tr.emplace_back();bt.emplace_back();
 for(string w:{"ce","ec","ed","de"})addbase(w);
 for(int z=1;z<=h/2+1;z++)for(int x=1;x<=h+1;x++)for(int y=1;y<=h+1;y++){
   int a=z-1,e=z,d=x+y-h-1,f=h+1-y-2*z,g=h+1-x;
   if(min({a,e,d,f,g})<0)continue;
   legalkeys++;uint64_t old=candidate;int n[6]={a,0,0,e,f,g};
   for(int c=0;c<=d;c++){n[1]=c;n[2]=d-c;rec(n,0);}
   if(candidate!=old)usedkeys++;
 }
 solve();vector<int> steps;trace(0,15,steps);
 sort(witness.begin(),witness.end(),[](auto &a,auto &b){return a.second<b.second;});
 cout<<"{\n\"h\":"<<h<<",\"keys\":"<<legalkeys<<",\"keys_with_low\":"<<usedkeys
     <<",\"candidate_words\":"<<candidate<<",\"trie_nodes\":"<<tr.size()
     <<",\"reachable_states\":"<<states<<",\"minimum_cost\":"<<28+dp[0][15]<<",\"witness\":[";
 for(size_t i=0;i<witness.size();i++){if(i)cout<<",";cout<<"{\"signature\":"<<witness[i].second<<",\"word\":\""<<witness[i].first<<"\"}";}
 cout<<"]}\n";
}