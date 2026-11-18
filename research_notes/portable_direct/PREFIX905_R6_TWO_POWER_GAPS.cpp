#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
using u64 = uint64_t;
constexpr int LO=262145, HI=524287, M=131072;
constexpr u64 N=(u64(1)<<32), T=33*N;
struct Pattern {int i,j,t;}; // t=1: 2^i+2^j; t=0: 2^i-2^j
struct Line {u64 all=0,old=0,panel=0,both=0,new_pairs=0,witnesses=0;};
int main(){
  set<int> U, P;
  const vector<int> S={262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285};
  U.insert(S.begin(),S.end());
  for(int q=400011;q<=400521;q+=2)U.insert(q);
  for(int q=480011;q<=480521;q+=2)U.insert(q);
  for(int q=LO;q<=HI;q+=2) for(int h=1;h<32;h++)
    if(((u64(1)<<h)-1)%q==0 || ((u64(1)<<h)+1)%q==0) {U.insert(q);break;}
  for(int c:{510001,510003,510005,510009})for(int j=0;j<64;j++) P.insert(c+194*j);
  assert(U.size()==552 && P.size()==256);
  map<int,Pattern> patterns;
  set<int> dyadic;
  for(int h=1;h<=17;h++)dyadic.insert(1<<h);
  for(int i=2;i<=18;i++)for(int j=1;j<i;j++)for(int t:{0,1}){
    int d=(1<<i)+(t?(1<<j):-(1<<j));
    if(d>0 && d<HI-LO+2 && !(d&1) && !dyadic.count(d))
      patterns.emplace(d,Pattern{i,j,t});
  }
  assert(patterns.size()==256);
  u64 tot=0,old=0,panel=0,both=0,add=0,witnesses=0;
  cout << "gap,i,j,plus,ordered_all,ordered_old_E,ordered_panel_P4,ordered_both,ordered_new,checked_witnesses\n";
  for(const auto& [d,pattern]:patterns){
    Line l;
    for(int a=LO; a+d<=HI;a+=2){
      int b=a+d;
      // Construct opposite-directed named flips using source separation b.
      int period=1<<(pattern.j+1), s=1<<pattern.j;
      u64 x=(pattern.t*s-(b%period)+period)%period,y=x+b;
      u64 e1=x+(u64(1)<<pattern.i);
      u64 e2=y+(pattern.t?-s:s);
      assert(x<N && y<N && e1<N && e2<N);
      assert(((x>>pattern.i)&1)==0 && ((y>>pattern.j)&1)==(u64)pattern.t);
      assert(e1==(x^(u64(1)<<pattern.i)) && e2==(y^(u64(1)<<pattern.j)));
      assert((y-x)==(u64)b && (e2-e1)==(u64)a);
      assert(x%b==y%b && e1%a==e2%a);
      ++l.witnesses;
      bool e = ((u64)a*b < T || U.count(a) || U.count(b)
            || ((u64)a / gcd(a,b))*b < N
            || 33*((N+a-1)/a)> (u64)b || 33*((N+b-1)/b)>(u64)a);
      bool p=P.count(a)||P.count(b);
      l.all+=2;l.old+=2*e;l.panel+=2*p;l.both+=2*(e&&p);
      l.new_pairs+=2*(!e&&!p);
    }
    assert(l.all==2*(M-d/2));
    assert(l.new_pairs==l.all-l.old-l.panel+l.both);
    tot+=l.all;old+=l.old;panel+=l.panel;both+=l.both;add+=l.new_pairs;witnesses+=l.witnesses;
    cout<<d<<","<<pattern.i<<","<<pattern.j<<","<<pattern.t<<","<<l.all<<","<<l.old<<","<<l.panel<<","<<l.both<<","<<l.new_pairs<<","<<l.witnesses<<"\n";
  }
  assert(tot==55705582 && witnesses==tot/2);
  cerr << "GAPS="<<patterns.size()<<" ALL="<<tot<<" E="<<old<<" PANEL="<<panel<<" BOTH="<<both<<" ADDED="<<add<<" WITNESSES="<<witnesses<<" COMBINED="<<(7632945416ULL+add)<<" COMPLEMENT="<<(u64(M)*M-7632945416ULL-add)<<"\n";
}
