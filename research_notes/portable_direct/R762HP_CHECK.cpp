#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
using A6 = array<int,6>;

struct DSU {
  A6 p{};
  DSU() { for (int i=0;i<6;i++) p[i]=i; }
  int f(int x) { return p[x]==x ? x : p[x]=f(p[x]); }
  void join(int a,int b) { p[f(a)]=f(b); }
};

vector<int> ports;
vector<vector<int>> adj;
array<uint64_t,9> closed{}, evenH{}, constructed{};
vector<int> word;

void check(int m) {
  ++closed[m];
  vector<int> S(m);
  A6 H{};
  for (int t=0;t<m;t++) {
    S[t]=ports[word[t]]|ports[word[t+1]];
    assert(__builtin_popcount((unsigned)S[t])==3);
    for(int a=0;a<6;a++) if(S[t]&(1<<a)) ++H[a];
  }
  for(int a=0;a<6;a++) if(H[a]%2) return;
  ++evenH[m];
  assert(m%2==0);

  DSU g;
  for (int t=1;t<m;t++) {
    int add=S[t]&~S[t-1], del=S[t-1]&~S[t];
    assert(__builtin_popcount((unsigned)add)==__builtin_popcount((unsigned)del));
    assert(__builtin_popcount((unsigned)add)<=1);
    if(add) g.join(__builtin_ctz((unsigned)add),__builtin_ctz((unsigned)del));
  }
  A6 component_balance{};
  for (int a=0;a<6;a++)
    component_balance[g.f(a)]+=H[a]/2-(m/2)*((S[0]>>a)&1);
  for (int a=0;a<6;a++) assert(component_balance[a]==0);
  ++constructed[m];
}

void dfs(int depth,int limit) {
  if(depth==limit) { if(word.back()==0) check(limit); return; }
  for(int next:adj[word.back()]) {
    word.push_back(next);
    dfs(depth+1,limit);
    word.pop_back();
  }
}

int main() {
  for(int a=0;a<6;a++) for(int b=a+1;b<6;b++)
    ports.push_back((1<<a)|(1<<b));
  adj.resize(ports.size());
  for(size_t i=0;i<ports.size();i++) for(size_t j=0;j<ports.size();j++)
    if(__builtin_popcount((unsigned)(ports[i]&ports[j]))==1)
      adj[i].push_back(j);
  for(int m=2;m<=8;m+=2) { word={0}; dfs(0,m); }
  for(int m=2;m<=8;m+=2)
    cout<<m<<" "<<closed[m]<<" "<<evenH[m]<<" "<<constructed[m]<<"\n";
  assert(evenH[2]==8 && evenH[4]==168 && evenH[6]==4960 && evenH[8]==177536);
  const int P[][2]={{0,1},{1,5},{1,2},{2,5},{2,4},{0,4},{0,5},
                    {0,3},{0,4},{2,4},{2,3},{2,5},{3,5},{0,5},{0,1}};
  const int coeff[14]={3,4,-5,4,1,-3,2,1,0,0,0,0,0,0};
  A6 total{}, half{};
  for(int t=0;t<14;t++) {
    int h=(1<<P[t][0])|(1<<P[t][1])|(1<<P[t+1][0])|(1<<P[t+1][1]);
    assert(__builtin_popcount((unsigned)h)==3);
    for(int a=0;a<6;a++) if(h&(1<<a)) { ++total[a]; half[a]+=coeff[t]; }
  }
  for(int a=0;a<6;a++) assert(total[a]==2*half[a]);
  cout<<"14-example half=";
  for(int a:half) cout<<a<<",";
  cout<<" integer-identity PASS\nPASS\n";
}
