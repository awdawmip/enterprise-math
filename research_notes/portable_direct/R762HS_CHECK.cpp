// R762HS: exact Port-degree character projection and 10-source closed-Port sieve.
// g++ -std=c++17 -O3 -Wall -Wextra -pedantic R762HS_CHECK.cpp -o hs && ./hs
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

array<int, 20> triple{};
array<array<int,3>,64> tri_port{};
array<int,64> port_id{};
array<int,10> word{};
uint64_t total=0, parity_even=0, unsignable=0, overlap_connected_bad=0, port_parity_good=0;

bool overlap_connected() {
  int seen=1;
  bool changed=true;
  while(changed) {
    changed=false;
    for(int i=0;i<10;++i) if(seen&(1<<i))
      for(int j=0;j<10;++j) if(!(seen&(1<<j)) &&
          __builtin_popcount(unsigned(triple[word[i]]&triple[word[j]]))>=2) {
        seen|=1<<j; changed=true;
      }
  }
  return seen==(1<<10)-1;
}

bool has_zero_signing(const array<int,6>& degree) {
  for(int s=0;s<(1<<10);++s) if(__builtin_popcount(unsigned(s))==5) {
    array<int,6> d{};
    for(int t=0;t<10;++t) if(s&(1<<t))
      for(int a=0;a<6;++a) d[a]+=(triple[word[t]]>>a)&1;
    bool matched=true;
    for(int a=0;a<6;++a) if(2*d[a]!=degree[a]) { matched=false; break; }
    if(matched) return true;
  }
  return false;
}

// Fix the bit of the first Port to zero: the global flip of all 15 bits
// preserves each character; hence the denominator is 2^14, not 2^15.
int64_t even_degree_choices(const vector<int>& masks) {
  int64_t numerator=0;
  for(int x=0;x<(1<<14);++x) {
    int64_t product=1;
    for(int S:masks) {
      const auto& p=tri_port[S];
      auto bit=[&](int q){return q==0 ? 0 : ((x>>(q-1))&1);};
      int a=bit(p[0]),b=bit(p[1]),c=bit(p[2]);
      product*= (a==b && a==c) ? 3 : -1;
    }
    numerator+=product;
  }
  assert(numerator%(1<<14)==0);
  return numerator/(1<<14);
}

void visit() {
  ++total;
  array<int,6> H{};
  for(int t=0;t<10;++t)
    for(int a=0;a<6;++a) H[a]+=(triple[word[t]]>>a)&1;
  for(int h:H) if(h&1) return;
  ++parity_even;
  if(has_zero_signing(H)) return;
  ++unsignable;
  if(!overlap_connected()) return;
  ++overlap_connected_bad;
  vector<int> masks;
  for(int t=0;t<10;++t)masks.push_back(triple[word[t]]);
  if(even_degree_choices(masks)>0) ++port_parity_good;
}
void scan(int pos,int low) {
  if(pos==10) {visit();return;}
  for(int i=low;i<20;++i) {word[pos]=i;scan(pos+1,i);}
}
int main() {
  int port_count=0,type_count=0;
  for(int p=0;p<64;++p) if(__builtin_popcount(unsigned(p))==2) port_id[p]=port_count++;
  for(int S=0;S<64;++S) if(__builtin_popcount(unsigned(S))==3) {
    triple[type_count++]=S;
    int k=0;
    for(int p=0;p<64;++p) if(__builtin_popcount(unsigned(p))==2 && (p&S)==p)
      tri_port[S][k++]=port_id[p];
    assert(k==3);
  }
  assert(port_count==15 && type_count==20);
  scan(0,0);
  cout << "m10 total="<<total<<" coordinate_even="<<parity_even
       <<" unsignable="<<unsignable<<" connected_unsignable="<<overlap_connected_bad
       <<" Port_even_degree_possible="<<port_parity_good<<"\n";
  assert(total==20030010 && parity_even==632996 && unsignable==29360);
  assert(overlap_connected_bad==240 && port_parity_good==0);
  vector<int> pasch12={7,7,7,25,25,25,42,42,42,52,52,52};
  vector<int> pasch14={7,7,7,7,7,25,25,25,42,42,42,52,52,52};
  auto c12=even_degree_choices(pasch12),c14=even_degree_choices(pasch14);
  cout<<"Pasch multiplicity (3,3,3,3): "<<c12<<"; (5,3,3,3): "<<c14<<"\n";
  assert(c12==1296 && c14==12960);
  cout<<"PASS R762HS\n";
}
