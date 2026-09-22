// Deterministic exhaustive finite check. Not a formal proof-producing SAT solver.
// Input optional: max H (1..40, default34), per-cardinality node budget (default1e8).
// Modes:0 high-band;1 complete ruler;2 high-band after any one INTERNAL deletion
// with both endpoints protected (mode2 emitted only for 3<=H<=20).
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;
int H,K,mode; uint64_t wanted,visited,budget; vector<int> support,answer; bool exhausted;

bool admissible(uint64_t covered){
 if ((covered&wanted)!=wanted)return false;
 if (mode==2) {
  for (int erase=2;erase<K;++erase) {
   uint64_t remaining=0;
   for(int i=0;i<K;++i)if(i!=erase)
    for(int j=0;j<i;++j)if(j!=erase)
     remaining|=uint64_t(1)<<abs(support[i]-support[j]);
   if((remaining&wanted)!=wanted)return false;
  }
 }
 return true;
}
bool enumerate(int next,uint64_t covered){
 if(++visited>budget){exhausted=true;return false;}
 if(int(support.size())==K){if(admissible(covered)){answer=support;return true;}return false;}
 const int need=K-int(support.size());
 for(int x=next;x<=H-need;++x){
  uint64_t after=covered;
  for(int y:support)after|=uint64_t(1)<<abs(x-y);
  support.push_back(x);
  if(enumerate(x+1,after))return true;
  support.pop_back();if(exhausted)return false;
 }
 return false;
}
int main(int argc,char**argv){
 try{
  int maximum=argc>1?stoi(argv[1]):34;
  budget=argc>2?stoull(argv[2]):100000000ULL;
  if(maximum<1||maximum>40||budget<1)throw invalid_argument("invalid bound");
  cout<<"[\n";bool first=true;
  for(H=1;H<=maximum;++H)for(mode=0;mode<3;++mode){
   if(mode==2&&(H<3||H>20))continue;
   wanted=0;for(int d=mode==1?1:H/3+1;d<=H;++d)wanted|=uint64_t(1)<<d;
   if(!first)cout<<",\n";first=false;
   cout<<"{\"H\":"<<H<<",\"mode\":"<<mode<<",\"trials\":[";
   bool first_trial=true;
   for(K=2;K<=H+1;++K){
    // Necessary pair count and cross-half pair count. They may be weak.
    if(K*(K-1)/2<(mode==1?H:H-H/3)||(K*K)/4<(H+1)/2)continue;
    support={0,H};answer.clear();visited=0;exhausted=false;
    bool found=enumerate(1,uint64_t(1)<<H);
    if(!first_trial)cout<<",";first_trial=false;
    cout<<"{\"k\":"<<K<<",\"nodes\":"<<visited<<",\"verdict\":\""
        <<(found?"FOUND":exhausted?"BUDGET_EXHAUSTED":"EXCLUDED_EXHAUSTIVELY")<<"\"}";
    if(found||exhausted){
     sort(answer.begin(),answer.end());
     cout<<"],\"status\":\""<<(found?"MINIMUM_FOUND":"BUDGET_EXHAUSTED")<<"\",\"minimum\":";
     if(found)cout<<K;else cout<<"null";
     cout<<",\"support\":[";for(size_t i=0;i<answer.size();++i){if(i)cout<<",";cout<<answer[i];}
     cout<<"]}";break;
    }
   }
  }
  cout<<"\n]\n";return 0;
 }catch(const exception&e){cerr<<e.what()<<"\n";return 2;}
}
