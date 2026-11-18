#include <bits/stdc++.h>
using namespace std;
// EC49FFX: exact state-quotiented signed-X6 BRC operation-trie optimization.
// Reuses EC49FBS's native codeword prefix identity and EC49FFW's 9-state observer.
// For depth k>=2 the H2 baseline no longer overlaps outgoing edges;
// each 16-mask cost row depends only on (k,#e,#a,#f,DFA state).
constexpr int T[9][6]={{1,2,3,1,4,5},{1,6,7,1,1,1},{2,2,8,2,2,2},{3,8,3,3,3,3},{4,2,7,4,4,4},{5,6,3,5,5,5},{6,6,8,6,6,6},{7,8,7,7,7,7},{8,8,8,8,8,8}};
constexpr int SIG[9]={0,0,4,1,16,32,8,2,0};
constexpr int LEN[6]={2,4,4,4,2,2};
constexpr int INF=32767;
using Row=array<int16_t,16>;
int H;
vector<int8_t> memo; vector<Row> cache; vector<uint8_t> ready;
uint64_t visited_states=0,cache_hits=0,viable_nodes=0,viable_words=0;
inline size_t idx(int k,int e,int a,int f,int q){return (((((size_t)k*(H+1)+e)*(H+1)+a)*(H+1)+f)*9+q);}
inline void advance(int j,int &e,int &a,int &f){if(j==0)a++;else if(j==3)e++;else if(j==4)f++;}
bool valid(int k,int e,int a,int f,int q){
 if(2*e+f>H || abs((e-a)-1)>H-k || e>H || a>H || f>H)return false;
 if(k==H)return e==a+1&&e>=1&&(SIG[q]==1||SIG[q]==2||SIG[q]==4||SIG[q]==8);
 auto &v=memo[idx(k,e,a,f,q)];if(v>=0)return v;
 for(int j=0;j<6;j++){int E=e,A=a,F=f;advance(j,E,A,F);
  if(valid(k+1,E,A,F,T[q][j]))return (v=1);
 }
 return (v=0);
}
inline void merge(Row &left,const Row &right){
 Row out=left;
 for(int a=0;a<16;a++)if(left[a]!=INF)for(int b=1;b<16;b++)if(!(a&b)&&right[b]!=INF){
  int m=a|b,val=left[a]+right[b];if(val<out[m])out[m]=val;
 }
 left=out;
}
void single(Row &state,const Row*child,int letter,bool base){
 if(!child)return;
 Row copy=*child;int fee=base?0:LEN[letter];
 for(int m=1;m<16;m++)if(copy[m]!=INF)copy[m]+=fee;
 merge(state,copy);
}
void pair_group(Row &state,const Row*P,const Row*Q,int p,int q,bool bp,bool bq){
 if(!P&&!Q)return;
 auto pc=[&](int x,int y){return LEN[p]*x+LEN[q]*y-(x&&y);};int basefee=pc(bp,bq);
 Row sub;sub.fill(INF);sub[0]=0;
 if(P)for(int a=1;a<16;a++)if((*P)[a]!=INF){
  int val=(*P)[a]+pc(1,bq)-basefee;if(val<sub[a])sub[a]=val;
 }
 if(Q)for(int b=1;b<16;b++)if((*Q)[b]!=INF){
  int val=(*Q)[b]+pc(bp,1)-basefee;if(val<sub[b])sub[b]=val;
 }
 if(P&&Q)for(int a=1;a<16;a++)if((*P)[a]!=INF)for(int b=1;b<16;b++)if(!(a&b)&&(*Q)[b]!=INF){
  int m=a|b,val=(*P)[a]+(*Q)[b]+pc(1,1)-basefee;if(val<sub[m])sub[m]=val;
 }
 merge(state,sub);
}
int oldmask(const string &prefix){
 if(prefix.empty())return (1<<1)|(1<<2)|(1<<3);
 if(prefix=="c"||prefix=="d")return 1<<3;
 if(prefix=="e")return (1<<1)|(1<<2);
 return 0;
}
Row eval(int k,int e,int a,int f,int q,string &prefix){
 viable_nodes++;
 size_t at=idx(k,e,a,f,q);
 if(k>=2&&ready[at]){cache_hits++;return cache[at];}
 visited_states++;
 Row row;row.fill(INF);row[0]=0;
 if(k==H){
  viable_words++;int sig=SIG[q],bit=sig==1?0:sig==2?1:sig==4?2:3;
  row[1<<bit]=0;if(k>=2){cache[at]=row;ready[at]=1;}return row;
 }
 Row kids[6];bool has[6]={};
 for(int j=0;j<6;j++){
  int E=e,A=a,F=f;advance(j,E,A,F);int Q=T[q][j];
  if(valid(k+1,E,A,F,Q)){
   prefix.push_back("acdefg"[j]);kids[j]=eval(k+1,E,A,F,Q,prefix);prefix.pop_back();has[j]=true;
  }
 }
 int b=oldmask(prefix);
 single(row,has[0]?&kids[0]:nullptr,0,(b>>0)&1);
 pair_group(row,has[1]?&kids[1]:nullptr,has[4]?&kids[4]:nullptr,1,4,(b>>1)&1,(b>>4)&1);
 pair_group(row,has[2]?&kids[2]:nullptr,has[5]?&kids[5]:nullptr,2,5,(b>>2)&1,(b>>5)&1);
 single(row,has[3]?&kids[3]:nullptr,3,(b>>3)&1);
 if(k>=2){cache[at]=row;ready[at]=1;}
 return row;
}
int main(int argc,char **argv){
 H=argc>1?atoi(argv[1]):14;
 size_t states=(size_t)(H+1)*(H+1)*(H+1)*(H+1)*9;
 memo.assign(states,-1);cache.resize(states);ready.assign(states,0);
 auto start=chrono::steady_clock::now();string p;Row result=eval(0,0,0,0,0,p);auto end=chrono::steady_clock::now();
 cout<<"{\"h\":"<<H<<",\"evaluated_terminal_states\":"<<viable_words<<",\"recursive_calls\":"<<viable_nodes<<",\"distinct_state_evaluations\":"<<visited_states<<",\"cache_hits\":"<<cache_hits<<",\"exact_cost\":"<<28+result[15]<<",\"runtime_seconds\":"<<chrono::duration<double>(end-start).count()<<"}\n";
}