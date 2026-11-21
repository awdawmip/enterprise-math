#include <algorithm>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <utility>
#include <vector>
using namespace std;
struct Node{map<int,int>children;vector<int>leaves;int maxSlack=0;};
struct Profile{int floor,first;};
int main(int argc,char**argv){
 if(argc!=2)return 2;ifstream in(argv[1]);int nt,np,cap;in>>nt>>np>>cap;vector<pair<int,int>>types[42];
 for(int i=0;i<nt;i++){int id,base,n;in>>id>>base>>n;if(id<0||id>=42)return 3;for(int j=0;j<n;j++){int c,d;in>>c>>d;types[id].push_back({c-base,d});}}
 vector<Node>trie(1);vector<Profile>profiles;int maxSlack=0;
 for(int i=0;i<np;i++){int floor,first;in>>floor>>first;profiles.push_back({floor,first});int slack=cap-floor;maxSlack=max(maxSlack,slack);int node=0;trie[node].maxSlack=max(trie[node].maxSlack,slack);for(int j=0;j<11;j++){int type;in>>type;int next;auto it=trie[node].children.find(type);if(it==trie[node].children.end()){next=trie.size();trie[node].children[type]=next;trie.emplace_back();}else next=it->second;node=next;trie[node].maxSlack=max(trie[node].maxSlack,slack);}trie[node].leaves.push_back(i);}
 vector<int>bounds(cap+1,-1),attainer(cap+1,-1);uint64_t updates=0,states=0;size_t held=0,peak=0;
 function<void(int,const vector<int16_t>&)>visit=[&](int node,const vector<int16_t>&dp){
  held+=dp.size()*sizeof(int16_t);peak=max(peak,held);
  for(int p:trie[node].leaves){auto [floor,first]=profiles[p];int q2=-1,q3=-1;for(int c=first;c<=cap;c++){int v=dp[c-floor];if(v<0)continue;if(v>1611)throw logic_error("global difference cap exceeded");if(v>bounds[c]){bounds[c]=v;attainer[c]=p;}if(v>=108+2*(c-11292))q2=c;if(v>=108+3*(c-11292))q3=c;}cout<<"profile "<<p<<" "<<q2<<" "<<q3<<"\n";if(first<=11594&&11594-floor<(int)dp.size()&&dp[11594-floor]>=1012)cout<<"boundary "<<p<<" "<<dp[11594-floor]<<"\n";}
  for(auto [type,next]:trie[node].children){int slack=trie[next].maxSlack;vector<int16_t>ndp(slack+1,-1);for(int i=0;i<=slack;i++)if(dp[i]>=0){states++;for(auto [spent,diff]:types[type]){if(i+spent>slack)break;int v=dp[i]+diff;if(v>32767)throw logic_error("difference overflow");auto&target=ndp[i+spent];if(v>target){target=v;updates++;}}}visit(next,ndp);}
  held-=dp.size()*sizeof(int16_t);
 };
 vector<int16_t>start(maxSlack+1,-1);start[0]=0;visit(0,start);
 for(int c=11301;c<=cap;c++)if(bounds[c]>=0)cout<<"bound "<<c<<" "<<bounds[c]<<" "<<attainer[c]<<"\n";
 cerr<<"profiles "<<np<<" trie_nodes "<<trie.size()<<" states "<<states<<" updates "<<updates<<" peak_dp_bytes "<<peak<<" max_slack "<<maxSlack<<"\n";
}
