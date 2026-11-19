// Independent 4-bit-per-label exact f8 observer Bellman; action list made by Python left endpoints.
#include <vector>
#include <string>
#include <cstdint>
#include <iostream>
#include <fstream>
#include <unordered_map>
#include <algorithm>
#include <cstdlib>
using namespace std;
struct Act{int cost;vector<unsigned> masks;};
int n,f;vector<Act> acts;unordered_map<uint64_t,int> memo;
int value(uint64_t state){
 int live=0;
 for(int h=0;h<n;h++)live+=(((state>>(h*4))&15)<=f);
 if(live<=1)return 0;
 auto it=memo.find(state);if(it!=memo.end())return it->second;
 int best=INT32_MAX/2;
 for(auto&act:acts){
  if(act.cost>=best)continue;
  bool stall=false;int worst=0;
  for(unsigned mask:act.masks){
   uint64_t next=state;
   for(int h=0;h<n;h++){
    int e=(state>>(4*h))&15;
    if(e<=f&&!(mask>>h&1))next+=uint64_t(1)<<(4*h);
   }
   if(next==state){stall=true;break;}
   worst=max(worst,value(next));
   if(worst+act.cost>=best)break;
  }
  if(!stall)best=min(best,act.cost+worst);
 }
 if(best==INT32_MAX/2)throw runtime_error("NO_PROGRESS");
 memo.emplace(state,best);return best;
}
int main(int argc,char**argv){
 if(argc<3)return 2;ifstream in(argv[1]);int count;in>>n>>count;f=atoi(argv[2]);
 if(n!=14||f!=8)return 3;
 for(int i=0;i<count;i++){
  Act a;int count_masks;in>>a.cost>>count_masks;
  for(int j=0;j<count_masks;j++){unsigned m;in>>m;a.masks.push_back(m);}
  acts.push_back(move(a));
 }
 int v=value(0);
 cout<<"EXACT_NIBBLE n="<<n<<" f="<<f<<" V="<<v<<" states="<<memo.size()<<" actions="<<count<<"\n";
 return 0;
}
