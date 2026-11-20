// R762HF finite exhaustive signed-lift certificate. C++17, standard library only.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
using namespace std;
struct Edge { int to, mask; };
using LL = long long;
int bitcount(int x){int n=0;while(x){n+=x&1;x>>=1;}return n;}
array<vector<Edge>,15> adj;
array<int,8> supports;
int length_now = 0;
LL port_returns=0, parity_returns=0, liftable=0, signed_returns=0;
map<int, LL> fiber_hist;
void collect(int port, int depth) {
  if (depth < length_now) {
    for (auto e : adj[port]) {
      supports[depth]=e.mask;
      collect(e.to,depth+1);
    }
    return;
  }
  if(port != 0) return;
  ++port_returns;
  int parity=0;
  for(int i=0;i<length_now;i++) parity ^= supports[i];
  if(parity != 0) return;
  ++parity_returns;
  int fibers=0;
  for(int choice=0;choice<(1<<length_now);choice++) {
    int sums[6]={};
    for(int t=0;t<length_now;t++) {
      int sign=(choice>>t&1)?1:-1;
      for(int a=0;a<6;a++) if(supports[t]>>a&1) sums[a]+=sign;
    }
    bool zero=true;
    for(int a=0;a<6;a++) if(sums[a]) zero=false;
    fibers+=zero;
  }
  if(fibers>0) ++liftable;
  signed_returns+=fibers;
  ++fiber_hist[fibers];
}
LL port_formula(int m) {
  LL pow8=1,pow2=1,negative2=1;
  for(int i=0;i<m;i++){pow8*=8;pow2*=2;negative2*=-2;}
  return (pow8+5*pow2+9*negative2)/15;
}
int main(){
  array<int,15> p{};
  int id=0;
  for(int i=0;i<6;i++) for(int j=i+1;j<6;j++) p[id++]=(1<<i)|(1<<j);
  for(int i=0;i<15;i++) for(int j=0;j<15;j++) {
    if(bitcount(p[i]&p[j])==1)
      adj[i].push_back({j,p[i]|p[j]});
  }
  for(int m : {0,2,4,6,8}) {
    length_now=m;
    port_returns=parity_returns=liftable=signed_returns=0;
    fiber_hist.clear();
    collect(0,0);
    assert(port_returns==port_formula(m));
    const LL H[5]={1,8,168,4960,177536};
    const LL Z[5]={1,16,624,34688,2413424};
    assert(parity_returns==H[m/2]);
    assert(signed_returns==Z[m/2]);
    assert(liftable==parity_returns);
    cout << "m="<<m<<" U="<<port_returns<<" H="<<parity_returns
         <<" F="<<liftable<<" Z="<<signed_returns<<" fibers={";
    bool first=true;
    for(auto [f,c]:fiber_hist){if(!first)cout<<",";first=false;cout<<f<<":"<<c;}
    cout<<"}"<<'\n';
  }
  cerr<<"PASS: all ordered unsigned walks through length eight; full signed fibers for every parity-zero return.\n";
}
