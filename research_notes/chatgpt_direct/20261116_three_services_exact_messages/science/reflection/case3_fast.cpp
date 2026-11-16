#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;using U=uint64_t;using M=__uint128_t;
constexpr U full25=(U(1)<<25)-1,full50=(U(1)<<50)-1;int shape[5];
struct Row{U f,p;};
vector<Row> classes[220],reps[220],selected;
unordered_map<U,vector<U>> byfixed[220];
vector<U> moving[14];unordered_set<U> legal[14];unordered_set<U> tried;long long examined=0,compatible=0,allfixed=0,countshape=0;
int pop(U n){return __builtin_popcountll(n);}
U orbit_transform(U m,int e,int dy,int dz){
 U output=0;
 while(m){int j=__builtin_ctzll(m);m&=m-1;int x=(j/25+1)*e%5,y=(j/5%5*e+dy)%5,z=(j%5*e+dz)%5;x=min(x,5-x)-1;output|=U(1)<<(25*x+5*y+z);}
 return output;
}
void load(){ifstream f("fixed_all_masks.txt");U hi,lo;int a,b;
 while(f>>hi>>lo>>a>>b){U fixed=lo&full25,pairs=(lo>>25)|(hi<<39);int id=16*a+b;classes[id].push_back({fixed,pairs});byfixed[id][fixed].push_back(pairs);}
 ifstream g("rare.txt");while(g>>a>>b>>hi>>lo){reps[16*a+b].push_back({lo&full25,(lo>>25)|(hi<<39)});}
 ifstream seed("p8_seed.txt");U x;
 while(seed>>a>>x){
  if(a<=9){legal[a].insert(x);continue;}
  for(int e=1;e<=2;e++)for(int y=0;y<5;y++)for(int z=0;z<5;z++)
   legal[a].insert(orbit_transform(x,e,y,z));}
 for(int k=10;k<=11;k++){moving[k]=vector<U>(legal[k].begin(),legal[k].end());cout<<"swapped representatives "<<k<<" "<<moving[k].size()<<endl;}
}
bool contains(int k,U t){if(k>=10)return legal[k].count(t);int j=__builtin_ctzll(t), e=j<25?1:2;return legal[k].count(orbit_transform(t,e,5-(j/5%5*e)%5,5-(j%5*e)%5));}
bool split(U rem){
 if(!tried.insert(rem).second)return false;
 int n=pop(rem);for(int i=11;i>=8;i--)for(int j=i;j>=8;j--){
  int k=n-i-j;if(k>j||k<8)continue;
  // At least 30 transposed-pair orbits remain. If j < 10 then i+j+k <= 11+9+9=29.
  if (j<10) throw std::runtime_error("impossible second moving size");
  // Enumerate two large representatives that lie in the remainder, then look up the last mask.
  vector<U> second;
  for(U p:moving[i])if((p&rem)==p){
   if(second.empty())for(U q:moving[j])if((q&rem)==q)second.push_back(q);
   for(U q:second){if((i==j&&q<=p)||(q&p))continue;U t=rem^p^q;
    if(contains(k,t)){cout<<"MOVE "<<p<<" "<<q<<" "<<t<<endl;return true;}}
  }
 }
 return false;
}
bool dfs(U usedF,U usedP,int pos){examined++;
 if(pos==4){
  auto f=full25^usedF;auto it=byfixed[shape[pos]].find(f);if(it==byfixed[shape[pos]].end())return false;
  for(U p:it->second)if(!(p&usedP)){allfixed++;if(split(full50^(p|usedP))){cout<<"FIX "<<f<<" "<<p<<endl;return true;}}return false;}
 auto &source=(pos==0)?reps[shape[pos]]:classes[shape[pos]];
 for(auto &r:source)if(!(r.f&usedF)&&!(r.p&usedP)){
  if(pos>1&&shape[pos-1]==shape[pos]&&r.f<selected.back().f)continue;
  selected.push_back(r);
  if(dfs(usedF|r.f,usedP|r.p,pos+1)){cout<<"FIX "<<r.f<<" "<<r.p<<endl;return true;}
  selected.pop_back();}
 return false;
}
int main(int argc,char**argv){load();ifstream s("shapes.txt");while(s>>shape[0]>>shape[1]>>shape[2]>>shape[3]>>shape[4]){int no=countshape++;if(argc>1 && stoi(argv[1])!=no)continue;bool ok=dfs(0,0,0);cout<<"CASE "<<no<<" "<<examined<<" "<<allfixed<<" "<<tried.size()<<" "<<ok<<endl;if(ok)return 0;}cout<<"CLOSED "<<countshape<<endl;}
