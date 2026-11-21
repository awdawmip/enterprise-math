// Endpoint-only search: two proper (10,744,sign*60), five proper (11,1059,sign*179), embedded sizes 12,12,13,13; exact total 11595. Both signs must be searched for the full-affine canonical frame catalogue.
#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>
using namespace std;using W=uint64_t;using M=__uint128_t;
constexpr M domain=(M(1)<<125)-1;
int at(M x){return W(x)?countr_zero(W(x)):64+countr_zero(W(x>>64));}
int card(M x){return popcount(W(x))+popcount(W(x>>64));}
struct Row{M m;int c;int diff;};
constexpr int excMin[14]={0,0,12,36,72,120,201,292,419,557,744,1008,1244,99999};
array<array<array<M,256>,16>,125> plusMap,minusMap;
int shift(int x,int y,int sign){return ((x/25+sign*(y/25)+5)%5)*25+((x/5%5+sign*(y/5%5)+5)%5)*5+(x%5+sign*(y%5)+5)%5;}
M move(M m,const array<array<M,256>,16>&p){M r=0;for(int i=0;i<16;i++,m>>=8)r|=p[i][unsigned(m&255)];return r;}
W obs[125][125][4];M bad[125][125];
int direction=1;int biasQ=0;array<int,14> minProperWeight{};
int difference(M m){int d=0;constexpr W lo61=(W(1)<<61)-1;for(M a=m;a;a&=a-1){auto&row=obs[at(a)];W h[4]{};for(M b=m;b;b&=b-1)for(int j=0;j<4;j++)h[j]|=row[at(b)][j];d+=popcount(h[0])+popcount(h[1]&lo61)-popcount(h[1]&~lo61)-popcount(h[2])-popcount(h[3]);}return d;}
int price(M m){int c=0;for(M a=m;a;a&=a-1){auto&row=obs[at(a)];W h[4]{};for(M b=m;b;b&=b-1)for(int j=0;j<4;j++)h[j]|=row[at(b)][j];for(W x:h)c+=popcount(x);}return c;}
array<vector<Row>,14> globalBank;array<vector<M>,125> containing;
long long nodes=0,settlements=0,done=0,leaves=0,possible=0;
struct Search{
 vector<int> E,P;int k,budget,minE,caseNo,weightedE;
 array<M,7> mothers{};M u=0;array<M,14> lastMask{};
 vector<pair<M,int>> hall;vector<M> picked;vector<M> win;array<vector<Row>,14> region;
 bool assign(int it,const vector<int>&pts,array<M,7>&parts){
   if(it==(int)pts.size()){
     vector<int> sizes;int c=0;for(int j=0;j<k;j++){sizes.push_back(card(parts[j]));}sort(sizes.begin(),sizes.end());if(sizes!=E)return false;
     for(int j=0;j<k;j++)c+=price(parts[j]);for(M m:picked)c+=price(m);if(c!=budget)return false;int exactDelta=0;for(int j=0;j<k;j++)exactDelta+=difference(parts[j]);for(M m:picked)exactDelta+=difference(m);if(exactDelta!=direction*1015)return false;
     if(biasQ){int delta=0;for(int j=0;j<k;j++)delta+=difference(parts[j]);for(M m:picked)delta+=difference(m);if(abs(delta)<108+biasQ*(c-11292))return false;}
     win=picked;for(int j=0;j<k;j++)win.push_back(parts[j]);return true;
   }
   int x=pts[it];M b=M(1)<<x;
   for(int j=0;j<k;j++)if(mothers[j]&b && card(parts[j])<E.back()){parts[j]|=b;if(assign(it+1,pts,parts))return true;parts[j]^=b;}
   return false;
 }
 bool settle(M used){
   ++settlements;if((domain&~used)&~u)return false;
   M free=domain&~used;array<M,7> parts{};vector<int> shared;
   for(M a=free;a;a&=a-1){int x=at(a),last=-1,n=0;for(int j=0;j<k;j++)if((mothers[j]>>x)&1){last=j;n++;}if(n==1)parts[last]|=M(1)<<x;else shared.push_back(x);}
   return assign(0,shared,parts);
 }
 bool capacity(M used){
   array<int,7> slots{};for(int j=0;j<k;j++)slots[j]=card(mothers[j]&~used);sort(slots.begin(),slots.begin()+k);
   for(int j=0;j<k;j++)if(slots[j]<E[j])return false;for(auto [u,need]:hall)if(card(u&~used)<need)return false;return true;
 }
 int point(M free){
   int pivot=at(free),highest=-1;
   for(M a=free;a;a&=a-1){int x=at(a);int v=0;for(M b=free;b;b&=b-1)v+=card(bad[x][at(b)]&free);
     if(v>highest){pivot=x;highest=v;}}
   return pivot;
 }
 struct Extend {
   Search& game;M unknown,used;array<int,14>&counts;int left,space,slack,s,required,x,weight;
   bool emit(M m){
     for(M parent:containing[x])if(!(m&~parent))return false;
     int c=price(m);if(s!=10 || c!=744 || difference(m)!=direction*60)return false;if(c>slack+excMin[s])return false;
     ++leaves;game.picked.push_back(m);
     bool yes=game.solve(unknown&~m,used|m,counts,left-1,space-s,slack-c+excMin[s],weight+biasQ*c-abs(difference(m)));game.picked.pop_back();return yes;
   }
   M conflict(int next,M current){M b=0;for(M a=current;a;a&=a-1)b|=bad[next][at(a)];return b;}
   bool fill(M current,int need,M extra){
     if(!need)return emit(current);
     for(;card(extra)>=need;extra&=extra-1){
       int j=at(extra);if(fill(current|(M(1)<<j),need-1,(extra&(extra-1))&~conflict(j,current)))return true;
     }
     return false;
   }
   bool native(M current,int sz,M free,M extra){
     if(sz>=required && card(extra)>=s-sz && fill(current,s-sz,extra))return true;
     if(sz==s)return false;
     for(;free && sz+card(free)>=required;free&=free-1){
       int j=at(free);M badnew=conflict(j,current);
       if(native(current|(M(1)<<j),sz+1,(free&(free-1))&~badnew,extra&~badnew))return true;
     }
     return false;
   }
 };
 bool solve(M free,M used,array<int,14>&counts,int kLeft,int space,int slack,int weight){
   ++nodes;
   if(biasQ){int lower=weight+weightedE;for(int i=1;i<=13;i++)lower+=counts[i]*minProperWeight[i];if(lower>biasQ*11292-108)return false;}
   if(!kLeft)return settle(used);
   int need=card(free),d=space-need;if(d<0||!capacity(used))return false;
   if(!free){throw logic_error("no obliged outside point with unfilled proper label");}
   int rare=-1;array<vector<Row>,14> choices;
   for(int s=11;s<=12;s++)if(counts[s]){
     auto &c=choices[s];for(auto&r:region[s])if(r.m>lastMask[s] && r.c<=excMin[s]+slack && !(r.m&used) && card(r.m&~free)<=d)c.push_back(r);
     if(c.size()<(size_t)counts[s])return false;
     if(rare<0||c.size()<choices[rare].size())rare=s;
   }
   if(rare!=-1){
     --counts[rare];M previousMask=lastMask[rare];for(auto&r:choices[rare]){
       lastMask[rare]=r.m;
       picked.push_back(r.m);++leaves;bool ok=solve(free&~r.m,used|r.m,counts,kLeft-1,space-rare,slack-r.c+excMin[rare],weight+biasQ*r.c-r.diff);picked.pop_back();lastMask[rare]=previousMask;
       if(ok){++counts[rare];return true;}
     }
     ++counts[rare];return false;
   }
   int x=point(free);M b=M(1)<<x;
   for(int s=10;s>=1;s--)if(counts[s]){
     --counts[s];Extend e{*this,free,used,counts,kLeft,space,slack,s,s-d,x,weight};
     bool yes=e.native(b,1,free^b,domain&~(free|used));++counts[s];if(yes)return true;
   }
   return false;
 }
 bool run(){
   lastMask.fill(0);u=0;for(int j=0;j<k;j++)u|=mothers[j];int space=0,base=minE;array<int,14>counts{};
   hall.clear();array<M,128> subsets{};array<int,8> required{};for(int j=0;j<k;j++)required[j+1]=required[j]+E[j];
   for(int sub=1;sub<(1<<k);sub++){int j=countr_zero((unsigned)sub),r=popcount((unsigned)sub);subsets[sub]=subsets[sub&(sub-1)]|mothers[j];if(card(subsets[sub])<required[r])return false;if(r>=2)hall.push_back({subsets[sub],required[r]});}
   sort(hall.begin(),hall.end(),[](auto a,auto b){return card(a.first)-a.second<card(b.first)-b.second;});
   for(int s:P){space+=s;base+=excMin[s];++counts[s];}
   int d=space-card(domain^u);
   for(int s=12;s>=11;s--)if(counts[s]){
     region[s].clear();for(auto&r:globalBank[s])if(card(r.m&u)<=d)region[s].push_back(r);
     if(region[s].size()<(size_t)counts[s])return false;
   }
   return solve(domain^u,0,counts,P.size(),space,budget-base,0);
 }
};
vector<int> parse(string s){replace(s.begin(),s.end(),',',' ');istringstream f(s);vector<int> w;int v;while(f>>v)w.push_back(v);return w;}
int main(int argc,char**av){
  if(argc>14)direction=stoi(av[14]);if(direction!=1&&direction!=-1)return 18;
  if(argc>11)biasQ=stoi(av[11]);
  ifstream ob(av[1],ios::binary),pp(av[2]);ob.read((char*)obs,sizeof(obs));array<unsigned char,3>tr;
  while(ob.read((char*)tr.data(),3))do{bad[tr[0]][tr[1]]|=M(1)<<tr[2];}while(next_permutation(tr.begin(),tr.end()));
  array<M,250> parents;for(auto&m:parents){W l,h;pp>>l>>h;m=M(h)<<64|l;for(M q=m;q;q&=q-1)containing[at(q)].push_back(m);}
  for(int x=0;x<125;x++)for(int b=0;b<16;b++)for(int z=1;z<256;z++){
    int first=countr_zero((unsigned)z)+8*b;
    plusMap[x][b][z]=plusMap[x][b][z&(z-1)];minusMap[x][b][z]=minusMap[x][b][z&(z-1)];
    if(first<125){plusMap[x][b][z]|=M(1)<<shift(first,x,1);minusMap[x][b][z]|=M(1)<<shift(first,x,-1);}
  }
  Search job;job.weightedE=stoi(av[12]);{auto weights=parse(av[13]);for(int i=0;i<14;i++)minProperWeight[i]=weights.at(i);}
  job.P=parse(av[5]);job.E=parse(av[6]);job.k=job.E.size();job.minE=stoi(av[7]);job.budget=stoi(av[8]);
  int slack=job.budget-job.minE;for(int s:job.P)slack-=excMin[s];int first=stoi(av[9]),end=stoi(av[10]);
  for(int s=11;s<=12;s++)if(find(job.P.begin(),job.P.end(),s)!=job.P.end()){
    ifstream f(string(av[3])+to_string(s),ios::binary);if(!f)return 4;W raw[3];
    while(f.read((char*)raw,24))if(int(raw[2])<=excMin[s]+slack && (s!=11 || int(raw[2])==1059)){
      M root=(M(raw[1])<<64)|raw[0];if(s==11 && difference(root)!=direction*179)continue;int cost=raw[2],delta=abs(difference(root));
      for(int x=0;x<125;x++){M m=move(root,plusMap[x]);if(at(m)==x)globalBank[s].push_back({m,cost,delta});}
    }
  }
  ifstream frames(av[4]);string line;int id=0;
  while(getline(frames,line)){
    if(id++<first)continue;if(id>end)break;istringstream st(line);for(int j=0,m;j<job.k;j++){if(!(st>>m))return 8;job.mothers[j]=parents[m];}
    ++done;if(job.run()){++possible;cout<<"hit "<<id<<" ";for(M r:job.win)cout<<W(r)<<":"<<W(r>>64)<<" ";cout<<endl;break;}
  }
  cerr<<done<<" "<<nodes<<" "<<leaves<<" "<<settlements<<" "<<possible<<"\n";
}
