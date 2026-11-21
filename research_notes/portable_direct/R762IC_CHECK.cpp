// R762IC exact exhaustive check: all 2^20 pair-presence masks for each bad core.
#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
static vector<array<int,3>> T;
static int portid[6][6];
static array<array<int,3>,20> edgemasks;
static array<int,20> adj;
static U D[20],CENTER;
static vector<int> core_reps[3];

static void gen(int idx,int k,U value,const vector<int>&picked,const unordered_set<U>& target,bool& found){
 if(found) return;
 if(idx==k){ if(target.count(value))found=true;return; }
 int j=picked[idx];
 gen(idx+1,k,value,picked,target,found);
 if(found)return;
 gen(idx+1,k,value+D[j],picked,target,found);
 if(found)return;
 gen(idx+1,k,value-D[j],picked,target,found);
}
static unordered_set<U> make_targets(const vector<int>&core){
 unordered_set<U> out;
 for(int mask=0;mask<(1<<(int)core.size());++mask){
   int v[6]={};
   for(int k=0;k<(int)core.size();++k){
     int eps=(mask>>k)&1 ? 1:-1;
     for(auto a:T[core[k]])v[a]+=eps;
   }
   U code=CENTER;
   for(int i=0;i<6;++i){if(v[i]%2)abort();code-=(U)(v[i]/2) << (7*i);}
   out.insert(code);
 }
 return out;
}
static vector<int> core_parities(const vector<int>&core){
 bitset<1<<15> seen;seen[0]=1;
 for(auto j:core){
  bitset<1<<15> next;
  for(int x=0;x<(1<<15);++x)if(seen[x])for(int e:edgemasks[j])next[x^e]=1;
  seen=next;
 }
 vector<int> out;for(int i=0;i<1<<15;++i)if(seen[i])out.push_back(i);
 return out;
}
static bool g2_connected(int coremask,int q){
  int nodes=coremask|q, seen=nodes&-nodes;
  while(1){
   int reach=seen;
   for(int s=seen;s;s&=s-1){int j=__builtin_ctz((unsigned)(s&-s));reach|=adj[j]&nodes;}
   if(reach==seen)break;
   seen=reach;
  }
  return seen==nodes;
}
static bool parity_possible(int q,const vector<int>&base){
 int pivots[15]={};
 for(int s=q;s;s&=s-1){
  int j=__builtin_ctz((unsigned)(s&-s));
  for(int e:edgemasks[j]){
   int v=e;
   for(int i=14;i>=0;--i) if(v>>i&1){if(pivots[i])v^=pivots[i];else {pivots[i]=v;break;}}
  }
 }
 for(int x:base){
  int v=x;
  for(int i=14;i>=0;--i)if(v>>i&1)if(pivots[i])v^=pivots[i];
  if(!v)return true;
 }
 return false;
}
int main(){
 for(int a=0;a<6;++a)for(int b=a+1;b<6;++b)for(int c=b+1;c<6;++c)T.push_back({a,b,c});
 int p=0;for(int a=0;a<6;++a)for(int b=a+1;b<6;++b)portid[a][b]=portid[b][a]=p++;
 CENTER=0;for(int i=0;i<6;++i)CENTER|=32ULL<<(7*i);
 for(int j=0;j<20;++j){
  D[j]=0;for(int a:T[j])D[j]|=1ULL<<(7*a);
  int a=T[j][0],b=T[j][1],c=T[j][2];
  int v[3]={portid[a][b],portid[a][c],portid[b][c]};
  edgemasks[j]={ (1<<v[0]) | (1<<v[1]), (1<<v[0]) | (1<<v[2]), (1<<v[1]) | (1<<v[2]) };
  for(int l=0;l<j;++l){int n=0;for(int x:T[j])for(int y:T[l])n+=(x==y);if(n==2){adj[j]|=1<<l;adj[l]|=1<<j;}}
 }
 auto parse=[&](vector<string> ss){vector<int> r;for(auto x:ss)for(int j=0;j<20;++j){string y="";for(int a:T[j])y+=char('0'+a);if(x==y)r.push_back(j);}return r;};
 core_reps[0]=parse({"024","035","125","134"});
 core_reps[1]=parse({"012","015","025","034","123","124"});
 core_reps[2]=parse({"012","013","014","025","035","045","125","135","145","234"});
 const array<uint64_t,3> exp_bad={3824,1056,1024}, exp_connected={64,0,0};
 for(int ci=0;ci<3;++ci){
  auto &core=core_reps[ci];int coremask=0;for(int j:core)coremask|=1<<j;
  auto targets=make_targets(core);auto bp=core_parities(core);
  vector<uint8_t> signable(1<<20,0);
  uint64_t bad_count=0, connected_bad=0, all3_bad=0;
  array<uint64_t,21> bad_levels{}, connected_levels{}, joint_levels{};
  for(int q=0;q<(1<<20);++q){
   bool good=false;
   if(q){
    int k=q&-q;
    good=signable[q^k];
   }
   if(!good){
    vector<int> picked;
    for(int x=q;x;x&=x-1)picked.push_back(__builtin_ctz((unsigned)(x&-x)));
    gen(0,picked.size(),CENTER,picked,targets,good);
   }
   signable[q]=good;
   if(good)continue;
   int k=__builtin_popcount((unsigned)q);
   bad_count++;bad_levels[k]++;
   bool connected=g2_connected(coremask,q);
   if(connected){
     connected_bad++;connected_levels[k]++;
     if(parity_possible(q,bp)){all3_bad++;joint_levels[k]++;}
   }
  }
  cout<<"CORE "<<core.size()<<" targets "<<targets.size()<<" base_parities "<<bp.size()<<" bad "<<bad_count<<" connected_bad "<<connected_bad<<" joint_bad "<<all3_bad<<"\n";
  cout<<"BAD_LEVELS";for(int k=0;k<=20;++k)if(bad_levels[k])cout<<" "<<k<<":"<<bad_levels[k];cout<<"\n";
  cout<<"CONNECTED_BAD_LEVELS";for(int k=0;k<=20;++k)if(connected_levels[k])cout<<" "<<k<<":"<<connected_levels[k];cout<<"\n";
  cout<<"JOINT_BAD_LEVELS";for(int k=0;k<=20;++k)if(joint_levels[k])cout<<" "<<k<<":"<<joint_levels[k];cout<<"\n";
  if(bad_count!=exp_bad[ci]||connected_bad!=exp_connected[ci]||all3_bad!=0) return 2;
 }
 cout<<"PASS R762IC: 3 * 2^20 exact source-mask checks; no joint counterexample\n";
}
