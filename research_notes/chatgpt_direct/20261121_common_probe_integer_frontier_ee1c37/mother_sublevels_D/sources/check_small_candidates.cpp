#include <set>
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
int biasQ=0;array<int,14> minProperWeight{};
int difference(M m){int d=0;constexpr W lo61=(W(1)<<61)-1;for(M a=m;a;a&=a-1){auto&row=obs[at(a)];W h[4]{};for(M b=m;b;b&=b-1)for(int j=0;j<4;j++)h[j]|=row[at(b)][j];d+=popcount(h[0])+popcount(h[1]&lo61)-popcount(h[1]&~lo61)-popcount(h[2])-popcount(h[3]);}return d;}
int price(M m){int c=0;for(M a=m;a;a&=a-1){auto&row=obs[at(a)];W h[4]{};for(M b=m;b;b&=b-1)for(int j=0;j<4;j++)h[j]|=row[at(b)][j];for(W x:h)c+=popcount(x);}return c;}
array<vector<Row>,14> globalBank;array<vector<M>,125> containing;
long long nodes=0,settlements=0,done=0,leaves=0,possible=0;
M marginal_fibers[15]{};long long marginal_tests=0,marginal_prunes=0;

int defect_budget=0;
array<vector<pair<int,int>>,14> defect_options;
unordered_map<unsigned,vector<int>> defect_memo;
long long capacity_tests=0,capacity_prunes=0;
void load_defect_options(const string& path,int budget){
  defect_budget=budget;defect_memo.clear();for(auto&v:defect_options)v.clear();
  ifstream file(path);if(!file)throw logic_error("missing complete cost-defect options");
  int size,cost,bound;
  while(file>>size>>cost>>bound){
    if(size<8||size>12||cost<excMin[size]||bound<0||bound>3*(size-2))throw logic_error("bad cost-defect option");
    int extra=cost-excMin[size];if(extra<=budget)defect_options[size].push_back({extra,bound});
  }
}
const vector<int>& defect_capacity(unsigned key){
  auto known=defect_memo.find(key);if(known!=defect_memo.end())return known->second;
  vector<int> result(defect_budget+1,key?-100000:0);
  if(key){int axis=0;while(((key>>(4*axis))&15)==0)++axis;
    const auto& previous=defect_capacity(key-(1u<<(4*axis)));
    for(auto [extra,bound]:defect_options[axis+8])for(int budget=extra;budget<=defect_budget;budget++)
      result[budget]=max(result[budget],previous[budget-extra]+bound);
  }
  return defect_memo.emplace(key,move(result)).first->second;
}


constexpr int small_cap[14]={0,0,0,0,0,0,0,0,443,598,780,0,0,0};
array<vector<Row>,14> small_bank;
array<array<vector<int>,125>,14> small_at;
long long small_visits=0,small_candidates=0;
void load_small(const string& path){
  ifstream input(path,ios::binary);if(!input)throw logic_error("missing complete small bank");
  struct Record{W lo,hi;unsigned cost,size;} raw;
  while(input.read((char*)&raw,sizeof(raw))){
    int s=raw.size;M m=M(raw.hi)<<64|raw.lo;
    if((s<8||s>10)||card(m)!=s||int(raw.cost)>small_cap[s])throw logic_error("bad small bank row");
    int id=small_bank[s].size();small_bank[s].push_back({m,int(raw.cost),abs(difference(m))});
    for(M bits=m;bits;bits&=bits-1)small_at[s][at(bits)].push_back(id);
  }
}

ofstream small_progress;

set<M> debug_candidates;
struct Search{
 array<vector<Row>,14> small_region;array<array<vector<int>,125>,14> region_at;
 vector<int> E,P;int k,budget,minE,caseNo,weightedE;
 array<M,7> mothers{};M u=0;
 vector<pair<M,int>> hall;vector<M> picked;vector<M> win;array<vector<Row>,14> region;
 bool assign(int it,const vector<int>&pts,array<M,7>&parts){
   if(it==(int)pts.size()){
     vector<int> sizes;int c=0;for(int j=0;j<k;j++){sizes.push_back(card(parts[j]));}sort(sizes.begin(),sizes.end());if(sizes!=E)return false;
     for(int j=0;j<k;j++)c+=price(parts[j]);for(M m:picked)c+=price(m);if(c>budget)return false;
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
     int c=price(m);if(c>slack+excMin[s])return false;
     debug_candidates.insert(m);return false;
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
   if(small_progress&&nodes%1000000==0)small_progress<<nodes<<" "<<leaves<<" "<<marginal_prunes<<" "<<capacity_prunes<<endl;
   // For every remaining proper class of size8..12, c>=a_s+3*delta,
   // with a=(419,557,744,993,1226). The original minima exceed a only
   // at size11 (by15) and size12 (by18). Obliged outside points give a
   // lower bound on the actual remaining proper union's fiber defect.
   if(!biasQ && kLeft){
     bool covered_sizes=true;for(int s=1;s<=13;s++)if(counts[s] && (s<8 || s>12))covered_sizes=false;
     if(covered_sizes){++marginal_tests;int defect=0;
       for(M fiber:marginal_fibers)defect+=max(0,card(free&fiber)-2*kLeft);
       int allowance=slack+15*counts[11]+18*counts[12];
       if(3*defect>allowance){++marginal_prunes;return false;}
       ++capacity_tests;unsigned key=0;for(int s=8;s<=12;s++)key|=unsigned(counts[s])<<(4*(s-8));
       if(slack<0||slack>defect_budget)throw logic_error("cost-defect slack outside certified range");
       if(defect>defect_capacity(key)[slack]){++capacity_prunes;return false;}

     }
   }

   if(biasQ){int lower=weight+weightedE;for(int i=1;i<=13;i++)lower+=counts[i]*minProperWeight[i];if(lower>biasQ*11292-108)return false;}
   if(!kLeft)return settle(used);
   int need=card(free),d=space-need;if(d<0||!capacity(used))return false;
   if(!free){throw logic_error("no obliged outside point with unfilled proper label");}
   int rare=-1;array<vector<Row>,14> choices;
   for(int s=11;s<=12;s++)if(counts[s]){
     auto &c=choices[s];for(auto&r:region[s])if(r.c<=excMin[s]+slack && !(r.m&used) && card(r.m&~free)<=d)c.push_back(r);
     if(c.size()<(size_t)counts[s])return false;
     if(rare<0||c.size()<choices[rare].size())rare=s;
   }
   if(rare!=-1){
     --counts[rare];for(auto&r:choices[rare]){
       picked.push_back(r.m);++leaves;bool ok=solve(free&~r.m,used|r.m,counts,kLeft-1,space-rare,slack-r.c+excMin[rare],weight+biasQ*r.c-r.diff);picked.pop_back();
       if(ok){++counts[rare];return true;}
     }
     ++counts[rare];return false;
   }

   int x=-1;bool all_small=true;
   for(int s=1;s<=13;s++)if(counts[s]&&(!small_cap[s]||slack+excMin[s]>small_cap[s]))all_small=false;
   if(all_small){
     array<int,125>frequency{};
     for(int s=8;s<=10;s++)if(counts[s])for(const Row&r:small_region[s]){
       if(r.c>slack+excMin[s]||(r.m&used)||card(r.m&~free)>d)continue;
       for(M points=r.m&free;points;points&=points-1)++frequency[at(points)];
     }
     int smallest=1000000000;
     for(M points=free;points;points&=points-1){int at_point=at(points);if(frequency[at_point]<smallest){smallest=frequency[at_point];x=at_point;}}
     if(!smallest)return false;
   }else x=point(free);
   M b=M(1)<<x;
   for(int s=10;s>=1;s--)if(counts[s]){

     --counts[s];
     if(!biasQ && small_cap[s] && slack+excMin[s]<=small_cap[s]){
       ++small_visits;
       for(int id:region_at[s][x]){
         const Row&r=small_region[s][id];
         if(r.c>slack+excMin[s]||(r.m&used)||card(r.m&~free)>d)continue;
         ++small_candidates;++leaves;picked.push_back(r.m);
         bool yes=solve(free&~r.m,used|r.m,counts,kLeft-1,space-s,slack-r.c+excMin[s],weight-r.diff);
         picked.pop_back();if(yes){++counts[s];return true;}
       }
       ++counts[s];continue;
     }
     Extend e{*this,free,used,counts,kLeft,space,slack,s,s-d,x,weight};
     bool yes=e.native(b,1,free^b,domain&~(free|used));++counts[s];if(yes)return true;
   }
   return false;
 }
 bool run(){
   u=0;for(int j=0;j<k;j++)u|=mothers[j];int space=0,base=minE;array<int,14>counts{};
   hall.clear();array<M,128> subsets{};array<int,8> required{};for(int j=0;j<k;j++)required[j+1]=required[j]+E[j];
   for(int sub=1;sub<(1<<k);sub++){int j=countr_zero((unsigned)sub),r=popcount((unsigned)sub);subsets[sub]=subsets[sub&(sub-1)]|mothers[j];if(card(subsets[sub])<required[r])return false;if(r>=2)hall.push_back({subsets[sub],required[r]});}
   sort(hall.begin(),hall.end(),[](auto a,auto b){return card(a.first)-a.second<card(b.first)-b.second;});
   for(int s:P){space+=s;base+=excMin[s];++counts[s];}
   int d=space-card(domain^u);
   for(int s=8;s<=10;s++)if(counts[s]){
     small_region[s].clear();for(auto&v:region_at[s])v.clear();
     for(const Row&r:small_bank[s])if(r.c<=budget-base+excMin[s]&&card(r.m&u)<=d){
       int id=small_region[s].size();small_region[s].push_back(r);
       for(M points=r.m;points;points&=points-1)region_at[s][at(points)].push_back(id);
     }
   }

   for(int s=12;s>=11;s--)if(counts[s]){
     region[s].clear();for(auto&r:globalBank[s])if(card(r.m&u)<=d)region[s].push_back(r);
     if(region[s].size()<(size_t)counts[s])return false;
   }
   return solve(domain^u,0,counts,P.size(),space,budget-base,0);
 }
};
vector<int> parse(string s){replace(s.begin(),s.end(),',',' ');istringstream f(s);vector<int> w;int v;while(f>>v)w.push_back(v);return w;}
int inherited_main(int argc,char**av){
  if(argc>11)biasQ=stoi(av[11]);
  for(int p=0;p<125;p++){M bit=M(1)<<p;marginal_fibers[p/25]|=bit;marginal_fibers[5+p/5%5]|=bit;marginal_fibers[10+p%5]|=bit;}
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
  int slack=job.budget-job.minE;for(int s:job.P)slack-=excMin[s];if(argc<16)return 20;load_small(av[15]);if(argc>16)small_progress.open(av[16]);if(argc<15)return 19;load_defect_options(av[14],slack);int first=stoi(av[9]),end=stoi(av[10]);
  for(int s=11;s<=12;s++)if(find(job.P.begin(),job.P.end(),s)!=job.P.end()){
    ifstream f(string(av[3])+to_string(s),ios::binary);if(!f)return 4;W raw[3];
    while(f.read((char*)raw,24))if(int(raw[2])<=excMin[s]+slack){
      M root=(M(raw[1])<<64)|raw[0];int cost=raw[2],delta=abs(difference(root));
      for(int x=0;x<125;x++){M m=move(root,plusMap[x]);if(at(m)==x)globalBank[s].push_back({m,cost,delta});}
    }
  }
  ifstream frames(av[4]);string line;int id=0;
  while(getline(frames,line)){
    if(id++<first)continue;if(id>end)break;istringstream st(line);for(int j=0,m;j<job.k;j++){if(!(st>>m))return 8;job.mothers[j]=parents[m];}
    ++done;if(job.run()){++possible;cout<<"hit "<<id<<" ";for(M r:job.win)cout<<W(r)<<":"<<W(r>>64)<<" ";cout<<endl;break;}
  }
  cerr<<done<<" "<<nodes<<" "<<leaves<<" "<<settlements<<" "<<possible<<"\n";
  cerr<<"marginal "<<marginal_tests<<" "<<marginal_prunes<<"\n";
  cerr<<"capacity "<<capacity_tests<<" "<<capacity_prunes<<"\n";
  cerr<<"smallbank "<<small_visits<<" "<<small_candidates<<"\n";
}

int main(int argc,char**argv){
  ifstream ob(argv[1],ios::binary),pp(argv[2]);ob.read((char*)obs,sizeof(obs));array<unsigned char,3>tr;
  while(ob.read((char*)tr.data(),3))do{bad[tr[0]][tr[1]]|=M(1)<<tr[2];}while(next_permutation(tr.begin(),tr.end()));
  array<M,250> parents;for(auto&m:parents){W lo,hi;pp>>lo>>hi;m=M(hi)<<64|lo;for(M q=m;q;q&=q-1)containing[at(q)].push_back(m);}
  load_small(argv[3]);vector<array<int,4>>cases;
  for(int j=4;j<=5;j++){ifstream frames(argv[j]);int a,b;frames>>a>>b;int size=j==4?10:9;int d=j==4?0:1;
    cases.push_back({a,b,size,d});}
  cases.push_back({cases[1][0],cases[1][1],10,1});cases.push_back({cases[0][0],cases[0][1],8,0});
  for(auto [a,b,size,d]:cases){
    Search game;M union_m=parents[a]|parents[b],free=domain^union_m,used=0;
    int x=game.point(free),slack=small_cap[size]-excMin[size];array<int,14>counts{};
    Search::Extend extension{game,free,used,counts,10,card(free)+d,slack,size,size-d,x,0};
    debug_candidates.clear();extension.native(M(1)<<x,1,free^(M(1)<<x),domain&~(free|used));
    set<M>expected;
    for(int id:small_at[size][x]){const Row&r=small_bank[size][id];if(!(r.m&used)&&card(r.m&~free)<=d)expected.insert(r.m);}
    if(expected!=debug_candidates)return 31;
    cout<<a<<" "<<b<<" "<<size<<" "<<d<<" "<<expected.size()<<"\n";
  }
}
