// R762HR exact positive-branch BRC source census and Port-realizability check.
// C++17; g++ -O3 -std=c++17 -Wall -Wextra -pedantic R762HR_CHECK.cpp -o hr && ./hr
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

static array<int,20> triples{};
static vector<int> word;
static int length;
static uint64_t total, even_input, unsignable, connected_unsignable;

static bool overlap_connected() {
  vector<char> seen(length,0);
  seen[0]=1;
  bool change=true;
  while(change) {
    change=false;
    for(int i=0;i<length;++i) if(seen[i])
      for(int j=0;j<length;++j) if(!seen[j] &&
        __builtin_popcount((unsigned)(triples[word[i]] & triples[word[j]]))>=2) {
        seen[j]=1; change=true;
      }
  }
  for(char x:seen) if(!x)return false;
  return true;
}

static bool signable() {
  int degree[6]={};
  for(int idx:word)
    for(int i=0;i<6;++i) degree[i]+=(triples[idx]>>i)&1;
  for(int x:degree) if(x&1)return true; // ineligible: caller will not count
  ++even_input;
  for(unsigned subset=0;subset<(1u<<length);++subset) {
    if(__builtin_popcount(subset)!=length/2)continue;
    int selected[6]={};
    for(int t=0;t<length;++t) if(subset&(1u<<t))
      for(int i=0;i<6;++i) selected[i]+=(triples[word[t]]>>i)&1;
    bool exact=true;
    for(int i=0;i<6;++i) if(2*selected[i]!=degree[i]) { exact=false;break; }
    if(exact)return true;
  }
  ++unsignable;
  if(overlap_connected())++connected_unsignable;
  return false;
}

static void enumerate(int at,int low) {
  if(at==length) {++total;signable();return;}
  for(int idx=low;idx<20;++idx) {
    word[at]=idx;
    enumerate(at+1,idx);
  }
}

// A support S (a triple) gives three Port vertices (its three pairs).
// Each event chooses one of the three edges of that Port triangle.
// Closed Port walks require even degree at every chosen Port vertex.
static uint64_t even_port_edge_choices(const vector<int>& masks) {
  vector<array<array<int,2>,3>> options;
  for(int S:masks) {
    array<int,3> P{};
    int k=0;
    for(int p=0;p<64;++p)
      if(__builtin_popcount((unsigned)p)==2 && (p&S)==p)P[k++]=p;
    assert(k==3);
    options.push_back({{{P[0],P[1]},{P[0],P[2]},{P[1],P[2]}}});
  }
  uint64_t count=0;
  auto visit=[&](auto&& self,int t,uint64_t parity)->void{
    if(t==(int)options.size()) {if(parity==0)++count;return;}
    for(const auto& edge:options[t])
      self(self,t+1,parity^(1ull<<edge[0])^(1ull<<edge[1]));
  };
  visit(visit,0,0);
  return count;
}

int main() {
  int t=0;
  for(int x=0;x<64;++x)
    if(__builtin_popcount((unsigned)x)==3) triples[t++]=x;
  assert(t==20);
  constexpr array<uint64_t,5> expect_total={210,8855,177100,2220075,20030010};
  constexpr array<uint64_t,5> expect_even={20,375,6040,71435,632996};
  constexpr array<uint64_t,5> expect_bad={0,30,660,5700,29360};
  constexpr array<uint64_t,5> expect_conn_bad={0,0,0,0,240};
  for(int k=0;k<5;++k) {
    length=2*(k+1);
    word.assign(length,0);
    total=even_input=unsignable=connected_unsignable=0;
    enumerate(0,0);
    cout<<"m="<<length<<" multisets="<<total
        <<" coordinate_even="<<even_input
        <<" zero_completion="<<(even_input-unsignable)
        <<" unsignable="<<unsignable
        <<" overlap_connected_unsignable="<<connected_unsignable<<'\n';
    assert(total==expect_total[k]);
    assert(even_input==expect_even[k]);
    assert(unsignable==expect_bad[k]);
    assert(connected_unsignable==expect_conn_bad[k]);
  }
  const vector<int> witness={7,7,11,21,26,26,41,41,44,50};
  auto count=even_port_edge_choices(witness);
  cout<<"witness Port edge selections="<<59049
      <<" even_degree_selections="<<count<<'\n';
  assert(count==0);
  cout<<"PASS R762HR"<<'\n';
}
