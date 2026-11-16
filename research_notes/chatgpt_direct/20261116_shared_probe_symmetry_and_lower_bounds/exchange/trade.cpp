#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
using Word=uint64_t;
using Mask=__uint128_t;
const Mask space=(Mask(1)<<125)-1;
int pos(Mask m){return Word(m)?__builtin_ctzll(Word(m)):64+__builtin_ctzll(Word(m>>64));}
int size(Mask m){return __builtin_popcountll(Word(m))+__builtin_popcountll(Word(m>>64));}
struct Row {Mask points;int type,touch;};
vector<Row> rows;int row_kind[13];Mask old[13];
unsigned long long nodes;vector<Mask> answer;
int nt;int need[24];int order[24][2];Mask slices[15];array<int,15> bounds_lo[24],bounds_hi[24];
bool search(Mask free,int labels,const vector<int>& pool){
 ++nodes;
 if(!labels)return !free;
 int low[15]{},high[15]{},qty[15];
 for(int j=0;j<15;j++){
  qty[j]=size(free&slices[j]);for(int i=0;i<nt;i++)if(need[i]){low[j]+=need[i]*bounds_lo[i][j];high[j]+=need[i]*bounds_hi[i][j];}
  if(qty[j]<low[j]||qty[j]>high[j])return false;
 }
 vector<int> choices;choices.reserve(pool.size());Mask covered=0;int avail[24]{};
 for(int id:pool){auto &r=rows[id];int t=r.type;if(!need[t] || (r.points&~free))continue;
  choices.push_back(id);++avail[t];covered|=r.points;
 }
 if(covered!=free)return false;
 int few=1000000,pivot=-1;
 for(int i=0;i<nt;i++){
  if(need[i]>avail[i])return false;
  if(need[i]==1&&avail[i]<few){few=avail[i];pivot=125+i;}
 }
 int counts[125]={};
 for(int i:choices){Mask m=rows[i].points;for(;m;m&=m-1)++counts[pos(m)];}
 for(Mask m=free;m;m&=m-1){int p=pos(m);if(counts[p]<few){pivot=p;few=counts[p];}}
 for(int i:choices){auto&r=rows[i];if(pivot<125?!(r.points>>pivot&1):r.type!=pivot-125)continue;
  --need[r.type];answer.push_back(r.points);if(search(free^r.points,labels-1,choices))return true;
  answer.pop_back();++need[r.type];}
 return false;
}
int main(int argc,char**argv){
 fill(row_kind,row_kind+13,-1);
 ifstream bank(argv[1]),pf(argv[2]),inc(argv[3]);int kmin=stoi(argv[4]),kmax=stoi(argv[5]);int start=argc>=7?stoi(argv[6]):0,step=argc>=8?stoi(argv[7]):1;
 for(int p=0;p<125;p++){slices[p/25]|=Mask(1)<<p;slices[5+(p/5%5)]|=Mask(1)<<p;slices[10+p%5]|=Mask(1)<<p;}
 for(int i=0;i<13;i++){Word l,h;inc>>l>>h;old[i]=Mask(h)<<64|l;}
 bank>>nt;
 for(int i=0;i<nt;i++){int s,c,n;bank>>s>>c>>n;order[i][0]=s;order[i][1]=c;bounds_lo[i].fill(25);bounds_hi[i].fill(0);
  while(n--){Word l,h;bank>>l>>h;Mask m=(Mask(h)<<64)|l;int touch=0,ident=-1;
   for(int j=0;j<15;j++){int v=size(m&slices[j]);bounds_lo[i][j]=min(bounds_lo[i][j],v);bounds_hi[i][j]=max(bounds_hi[i][j],v);}
   for(int j=0;j<13;j++){if(m&old[j])touch|=1<<j;if(old[j]==m)ident=j;}
   if(ident>=0)row_kind[ident]=i;else rows.push_back({m,i,touch});
  }}
 for(int t:row_kind)if(t<0)return 3;
 struct Profile{int cost;array<int,24> qty;};vector<Profile> profiles;int c;
 while(pf>>c){Profile l{c,{}};for(int t=0;t<nt;t++)pf>>l.qty[t];if(c<=8722)profiles.push_back(l);}
 vector<int> bucket[8192];for(int i=0;i<rows.size();i++)bucket[rows[i].touch].push_back(i);
 for(int k=kmin;k<=kmax;k++){
  for(int removed=1;removed<8192;removed++)if(__builtin_popcount(removed)==k && removed%step==start){
   Mask free=0;int fixed[24]{};vector<int> candidates;for(int i=0;i<13;i++){if(removed>>i&1)free|=old[i];else ++fixed[row_kind[i]];}
   for(int sub=removed;sub;sub=(sub-1)&removed)candidates.insert(candidates.end(),bucket[sub].begin(),bucket[sub].end());
   for(int n=0;n<profiles.size();n++){
    auto &p=profiles[n];bool allowed=true;for(int t=0;t<nt;t++){need[t]=p.qty[t]-fixed[t];if(need[t]<0)allowed=false;}
    if(!allowed)continue;
    nodes=0;answer.clear();bool ok=search(free,k,candidates);
    cout<<k<<" "<<removed<<" "<<n<<" "<<p.cost<<" "<<nodes<<" "<<ok<<"\n";
    if(ok){ofstream hit("found_"+to_string(p.cost)+"_"+to_string(removed)+".txt");for(int i=0;i<13;i++)if(!(removed>>i&1))answer.push_back(old[i]);
      for(Mask m:answer){for(;m;m&=m-1)hit<<pos(m)<<" ";hit<<"\n";}return 0;}
   }
   if(removed%64<4)cout<<flush;
  }
  cout<<flush;
 }
}
