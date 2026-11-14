#include <bits/stdc++.h>
using namespace std;
// EC49FFW: exact original nine-state observer and signed native X6 microsteps.
constexpr int T[9][6]={{1,2,3,1,4,5},{1,6,7,1,1,1},{2,2,8,2,2,2},{3,8,3,3,3,3},{4,2,7,4,4,4},{5,6,3,5,5,5},{6,6,8,6,6,6},{7,8,7,7,7,7},{8,8,8,8,8,8}};
constexpr int SIG[9]={0,0,4,1,16,32,8,2,0};
constexpr int LEN[6]={2,4,4,4,2,2};
constexpr char O[]="acdefg";
constexpr int INF=32767;
using Row=array<int16_t,16>;
struct Node {uint32_t c[6]{};uint8_t end=0,baseline=0;uint8_t pad[2]{};};
static_assert(sizeof(Node)==28);
vector<Node> nodes;
vector<Row> dp;
vector<uint8_t> opword;
uint64_t word_count=0,validkeys=0;
uint32_t new_child(uint32_t v,int j){uint32_t ch=nodes[v].c[j];if(!ch){ch=nodes.size(); nodes[v].c[j]=ch;nodes.emplace_back();} return ch;}
void baseline(const string& w){uint32_t v=0;for(char a:w){int j=strchr(O,a)-O; nodes[v].baseline|=1u<<j;v=new_child(v,j);}}
void terminal(int q){int s=SIG[q];int j=s==1?0:s==2?1:s==4?2:s==8?3:-1;if(j<0)return;
 uint32_t v=0;for(int k:opword) v=new_child(v,k);
 nodes[v].end|=1u<<j;word_count++;
}
void recurse(int n[6],int q){bool has=false;for(int j=0;j<6;j++)if(n[j]){has=true;n[j]--;opword.push_back(j);recurse(n,T[q][j]);opword.pop_back();n[j]++;}
 if(!has)terminal(q);
}
void gen(int h){for(int z=1;z<=h/2+1;z++)for(int x=1;x<=h+1;x++)for(int y=1;y<=h+1;y++){
  int a=z-1,e=z,d=x+y-h-1,f=h+1-y-2*z,g=h+1-x;
  if(min({a,e,d,f,g})<0)continue;validkeys++;
  int n[6]={a,0,0,e,f,g};for(int c=0;c<=d;c++){n[1]=c;n[2]=d-c;recurse(n,0);}
 }}
inline void merge(Row &left,const Row &right){
 Row out=left;
 for(int a=0;a<16;a++) if(left[a]!=INF) for(int b=1;b<16;b++) if(!(a&b)&&right[b]!=INF) {
  int m=a|b,val=left[a]+right[b];if(val<out[m])out[m]=val;
 }
 left=out;
}
void single(Row &state,uint32_t v,int j){auto child=nodes[v].c[j];if(!child)return;
 Row sub=dp[child];int fee=(nodes[v].baseline&(1u<<j))?0:LEN[j];
 for(int m=1;m<16;m++)if(sub[m]!=INF)sub[m]+=fee;
 merge(state,sub);
}
void pair_group(Row &state,uint32_t v,int p,int q){
 auto P=nodes[v].c[p],Q=nodes[v].c[q];
 if(!P&&!Q)return;
 auto bp=(nodes[v].baseline>>p)&1, bq=(nodes[v].baseline>>q)&1;
 auto pair_cost=[&](int x,int y){return LEN[p]*x+LEN[q]*y-(x&&y);};
 int basefee=pair_cost(bp,bq);
 Row sub;sub.fill(INF);sub[0]=0;
 if(P)for(int a=1;a<16;a++)if(dp[P][a]!=INF){int fee=pair_cost(1,bq)-basefee;sub[a]=min<int>(sub[a],dp[P][a]+fee);}
 if(Q)for(int b=1;b<16;b++)if(dp[Q][b]!=INF){int fee=pair_cost(bp,1)-basefee;sub[b]=min<int>(sub[b],dp[Q][b]+fee);}
 if(P&&Q)for(int a=1;a<16;a++)if(dp[P][a]!=INF)for(int b=1;b<16;b++)if(!(a&b)&&dp[Q][b]!=INF){
 int fee=pair_cost(1,1)-basefee;int m=a|b,val=dp[P][a]+dp[Q][b]+fee;if(val<sub[m])sub[m]=val;
 }
 merge(state,sub);
}
void run(){ dp.resize(nodes.size());
 for(size_t i=nodes.size();i-->0;){
  Row row;row.fill(INF);row[0]=0;int end=nodes[i].end;
  for(int m=end;m;m=(m-1)&end)row[m]=0;
  single(row,i,0);pair_group(row,i,1,4);pair_group(row,i,2,5);single(row,i,3);
  dp[i]=row;
 }
}
int main(int argc,char **argv){int h=argc>1?atoi(argv[1]):8;
 nodes.reserve(h>=10?6000000:1000000);nodes.emplace_back();
 for(auto w:{"ce","ec","ed","de"})baseline(w);
 auto start=chrono::steady_clock::now();gen(h);auto generated=chrono::steady_clock::now();run();auto solved=chrono::steady_clock::now();
 auto secs=[](auto a,auto b){return chrono::duration<double>(b-a).count();};
 cout<<"{\"h\":"<<h<<",\"candidate_words\":"<<word_count<<",\"valid_keys\":"<<validkeys<<",\"operation_nodes\":"<<nodes.size()<<",\"cost\":"<<28+dp[0][15]<<",\"generation_seconds\":"<<fixed<<setprecision(3)<<secs(start,generated)<<",\"solve_seconds\":"<<secs(generated,solved)<<"}\n";
}
