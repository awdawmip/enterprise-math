// PREFIX-177 second implementation: independent exact <=11 covering decision.
// Compile: c++ -O3 -std=c++17 -Wall -Wextra verify_family_171_independent.cpp -o verify_family_171_independent
// Usage: ./verify_family_171_independent <prefix165_all10.bin>
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <set>
#include <stdexcept>
#include <unordered_set>
#include <vector>
using namespace std;
typedef array<unsigned short,4> Vec;
typedef uint64_t Mask;
static vector<Vec> d8,d16,edges,three,four;
static inline Vec plus2(const Vec&a,const Vec&b){return {static_cast<unsigned short>(a[0]+b[0]),static_cast<unsigned short>(a[1]+b[1]),static_cast<unsigned short>(a[2]+b[2]),static_cast<unsigned short>(a[3]+b[3])};}
static inline int enc(const Vec&v){return int(((v[0]*17+v[1])*17+v[2])*17+v[3]);}
static int card(const Vec&x){int n=0;for(auto v:x)if(v)n++;return n;}
static int pop(Mask x){return __builtin_popcountll(x);}
static void init(){
 for(int n:{8,16}){vector<Vec>&out=n==8?d8:d16;for(int a=0;a<=n;a++)for(int b=0;b<=n-a;b++)for(int c=0;c<=n-a-b;c++)out.push_back(Vec{(unsigned short)a,(unsigned short)b,(unsigned short)c,(unsigned short)(n-a-b-c)});}
 for(auto v:d8){int s=card(v);if(s==1||s==2){if(v!=Vec{4,4,0,0})edges.push_back(v);} else if(s==3)three.push_back(v);else if(s==4)four.push_back(v);}
 if(d8.size()!=165 || d16.size()!=969 || edges.size()!=45 || three.size()!=84 || four.size()!=35)throw runtime_error("domain size mismatch");
}
// Each clause is a disjunction of singleton or doubleton W-witnesses.
class Exact {
public:
 vector<vector<Mask>> clauses;
 unordered_set<Mask> explored;
 uint64_t calls=0;
 Mask solution=0;
 explicit Exact(const array<unsigned char,9>&ids){
  vector<Vec> U=edges;
  for(unsigned char id:ids)U.push_back(three.at(id));
  bool base[83521]={};int target_of[83521];fill(target_of,target_of+83521,-1);
  for(size_t i=0;i<U.size();i++)for(size_t j=i;j<U.size();j++)base[enc(plus2(U[i],U[j]))]=true;
  for(auto y:d16)if(!base[enc(y)]){target_of[enc(y)]=(int)clauses.size();clauses.emplace_back();}
  for(int i=0;i<35;i++){
   for(auto u:U){int t=target_of[enc(plus2(four[i],u))];if(t!=-1)clauses[t].push_back(Mask(1)<<i);}
   for(int j=i;j<35;j++){int t=target_of[enc(plus2(four[i],four[j]))];if(t!=-1)clauses[t].push_back((Mask(1)<<i)|(Mask(1)<<j));}
  }
  for(auto &cl:clauses){sort(cl.begin(),cl.end());cl.erase(unique(cl.begin(),cl.end()),cl.end());/* Empty clause is an exact impossibility certificate. */}
 }
 bool try_cover(Mask mask,int space){
   ++calls;
   if(space<0)return false;
   if(explored.find(mask)!=explored.end())return false;
   vector<Mask> pool; vector<Mask> chosen_options; size_t smallest=999;
   for(const vector<Mask>&cl:clauses){
     bool met=false;Mask union_missing=0;vector<Mask>choices;
     for(Mask producer:cl){
       Mask addition=producer&~mask;
       if(!addition){met=true;break;}
       if(pop(addition)<=space){choices.push_back(addition);union_missing|=addition;}
     }
     if(met)continue;
     if(choices.empty()){explored.insert(mask);return false;}
     pool.push_back(union_missing);
     if(choices.size()<smallest){smallest=choices.size();chosen_options=move(choices);}
   }
   if(pool.empty()){solution=mask;return true;}
   // Packing distinct candidate unions gives an admissible lower bound.
   sort(pool.begin(),pool.end(),[](Mask a,Mask b){return pop(a)<pop(b);});
   Mask already=0;int required=0;
   for(Mask alternatives:pool){if((alternatives&already)==0){required++;already|=alternatives;}}
   if(required>space){explored.insert(mask);return false;}
   sort(chosen_options.begin(),chosen_options.end(),[](Mask a,Mask b){if(pop(a)!=pop(b))return pop(a)<pop(b);return a>b;});
   chosen_options.erase(unique(chosen_options.begin(),chosen_options.end()),chosen_options.end());
   for(Mask addition:chosen_options)if(try_cover(mask|addition,space-pop(addition)))return true;
   explored.insert(mask);return false;
 }
};
int main(int argc,char **argv){
 if(argc!=2)return 2;
 try{init();ifstream is(argv[1],ios::binary);if(!is)throw runtime_error("cannot open input");
    set<array<unsigned char,9>> seen;int total=0,yes=0,no=0;uint64_t nodes=0, max_nodes=0;
    while(true){unsigned char record[27];is.read((char*)record,sizeof record);if(is.gcount()==0)break;if(is.gcount()!=27)throw runtime_error("truncated record");
      array<unsigned char,9> ids;copy(record,record+9,ids.begin());
      if(!is_sorted(ids.begin(),ids.end()) || adjacent_find(ids.begin(),ids.end())!=ids.end() || ids[8]>=84)throw runtime_error("invalid Q");
      if(!seen.insert(ids).second)throw runtime_error("duplicate Q");
      Exact s(ids);bool cover=s.try_cover(0,11);
      total++;nodes+=s.calls;max_nodes=max(max_nodes,s.calls);if(cover){yes++;cout<<"YES Qindex="<<total-1<<" W=";for(int i=0;i<35;i++)if(s.solution>>i&1)cout<<i<<",";cout<<"\n";}else no++;
    }
    cout<<"INDEPENDENT_PREFIX178_DONE rows="<<total<<" feasible11="<<yes<<" impossible11="<<no<<" total_nodes="<<nodes<<" max_nodes="<<max_nodes<<" distinctQ="<<seen.size()<<"\n";
    if(total==0)return 5;
    return 0;
 }catch(const exception&e){cerr<<"INDEPENDENT_PREFIX178_ERROR: "<<e.what()<<"\n";return 3;}
}
