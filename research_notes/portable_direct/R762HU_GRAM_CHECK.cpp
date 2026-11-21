#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <stdexcept>
using namespace std;
using U128=unsigned __int128;
struct Edge {int q;uint64_t delta;};
array<vector<Edge>,15> adj;
string str128(U128 x){if(!x)return "0";string s;while(x){s.push_back('0'+x%10);x/=10;}reverse(s.begin(),s.end());return s;}
constexpr uint64_t LOW=(1ULL<<36)-1;
uint64_t initial(){uint64_t s=0;for(int i=0;i<6;i++)s+=24ULL<<(6*i);return s;}
uint64_t encode(int q,uint64_t vec){return ((uint64_t)q<<36)+vec;}
uint64_t vec(uint64_t key){return key&LOW;}
int port(uint64_t key){return key>>36;}
using Layer=unordered_map<uint64_t,uint64_t>;
Layer step(const Layer &prev){
 Layer next;next.reserve(prev.size()*3);
 for(auto &[key,n]:prev){int p=port(key);uint64_t x=vec(key);
  for(auto e:adj[p]){next[encode(e.q,x+e.delta)]+=n;next[encode(e.q,x-e.delta)]+=n;}
 }
 return next;
}
U128 gramsum(const Layer &d){U128 ans=0;for(auto &[k,n]:d)ans+=(U128)n*n;return ans;}
U128 sumcounts(const Layer &d){U128 ans=0;for(auto &[k,n]:d)ans+=n;return ans;}
uint64_t brute4(int p,int m,uint64_t x) {
 if(m==0)return (p==0 && x==initial())?1:0;
 uint64_t out=0;for(auto e:adj[p]) {out+=brute4(e.q,m-1,x+e.delta);out+=brute4(e.q,m-1,x-e.delta);}
 return out;
}
int main(){
 vector<pair<int,int>> ports;for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)ports.push_back({a,b});
 for(int p=0;p<15;p++)for(int q=0;q<15;q++){
  unsigned mask=(1<<ports[p].first)|(1<<ports[p].second)|(1<<ports[q].first)|(1<<ports[q].second);
  int overlap=(ports[p].first==ports[q].first)+(ports[p].first==ports[q].second)+(ports[p].second==ports[q].first)+(ports[p].second==ports[q].second);
  if(overlap==1){uint64_t d=0;for(int i=0;i<6;i++)if(mask>>i&1)d+=1ULL<<(6*i);adj[p].push_back({q,d});}
 }
 for(int p=0;p<15;p++)if(adj[p].size()!=8)throw runtime_error("port degree!=8");
 if(brute4(0,4,initial())!=624)throw runtime_error("independent depth-first m4 mismatch");
 Layer d{{encode(0,initial()),1}};
 for(int r=1;r<=9;r++) {
  d=step(d); U128 gram=gramsum(d), total=sumcounts(d);
  U128 expected=1;for(int j=0;j<r;j++)expected*=16;
  if(total!=expected)throw runtime_error("source count mismatch");
  cout<<"r="<<r<<" m="<<2*r<<" K="<<str128(gram)<<" half_states="<<d.size()<<" half_sources="<<str128(total)<<"\n";
  if(r<=4){Layer e=d;for(int j=0;j<r;j++)e=step(e);uint64_t n=e.count(encode(0,initial()))?e.at(encode(0,initial())):0;
    if((U128)n!=gram)throw runtime_error("direct-full-DP mismatch");
    cout<<" independent full transfer="<<n<<" PASS\n";
  }
 }
}
