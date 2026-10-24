// R265 independent exact finite-field implementation; no native P000 execution.
#include <iostream>
#include <map>
#include <tuple>
#include <vector>
#include <array>
#include <cassert>
using namespace std;
using ll=long long;
constexpr ll P=1000003;
ll powmod(ll a,ll n){ll r=1;for(;n;n>>=1,a=a*a%P)if(n&1)r=r*a%P;return r;}
struct Edge {int target, eta, b;};
const Edge edges[3][2]={{{2,-1,-1},{2,+1,-1}},{{0,-1,-1},{0,+1,-1}},{{1,+1,+1},{2,+1,-1}}};
const int delta[3][2]={{1,0},{2,0},{2,2}};
int main(){
  using Key=tuple<int,int,int,int>; // q,r,eps,k
  map<Key,ll> d; d[{0,0,+1,0}]=1;
  vector<ll> s;
  for(int m=0;m<=24;m++){
    ll v=0, sum=0;
    for(auto const& kv:d){
      auto [q,r,eps,k]=kv.first;
      sum=(sum+kv.second)%P;
      if(q==0&&r==2&&eps==1){
        ll x=(k>=0)?powmod(2,k):powmod(powmod(2,P-2),-k);
        v=(v+kv.second*x)%P;
      }
    }
    assert(sum==powmod(2,m)); s.push_back(v);
    if(m==24)break;
    map<Key,ll> next;
    for(auto const& kv:d){
      auto [q,r,eps,k]=kv.first;
      for(int a=0;a<2;a++){
        auto e=edges[q][a];
        Key key{e.target,delta[r][a],e.eta*eps,e.eta*k+e.b};
        next[key]=(next[key]+kv.second)%P;
      }
    }
    d.swap(next);
  }
  ll h[13][13]{};
  for(int i=0;i<13;i++)for(int j=0;j<13;j++)h[i][j]=s[i+j];
  ll det=1;
  for(int i=0;i<13;i++){
    int row=i;
    while(row<13 && h[row][i]==0)row++;
    assert(row<13);
    if(row!=i){for(int j=0;j<13;j++)swap(h[i][j],h[row][j]);det=(P-det)%P;}
    ll pivot=h[i][i];det=det*pivot%P;
    ll inv=powmod(pivot,P-2);
    for(int r=i+1;r<13;r++){
      ll scale=h[r][i]*inv%P;
      for(int c=i;c<13;c++)h[r][c]=(h[r][c]-scale*h[i][c]%P+P)%P;
    }
  }
  assert(det==206678);
  cout<<"{\"schema\":\"R265_INDEPENDENT_CPP17_V1\",\"prime\":"<<P<<",\"hankel_det_mod_p\":"<<det<<",\"depths_checked\":25,\"status\":\"PASS\"}\n";
}
