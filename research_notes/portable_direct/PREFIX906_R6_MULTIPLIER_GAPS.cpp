#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std; using u64=uint64_t;
constexpr int LO=262145,HI=524287,M=131072;
constexpr u64 N=1ULL<<32,T=33*N;
struct Pattern{int k,i,j,t;};
int main(){
 set<int>U,P,old;
 const vector<int>S={262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285};
 U.insert(S.begin(),S.end());
 for(int q=400011;q<=400521;q+=2)U.insert(q);
 for(int q=480011;q<=480521;q+=2)U.insert(q);
 for(int q=LO;q<=HI;q+=2)for(int h=1;h<32;h++)if(((1ULL<<h)-1)%q==0 ||((1ULL<<h)+1)%q==0){U.insert(q);break;}
 for(int c:{510001,510003,510005,510009})for(int j=0;j<64;j++)P.insert(c+194*j);
 assert(U.size()==552&&P.size()==256);
 for(int h=1;h<=17;h++)old.insert(1<<h);
 map<int,Pattern> newones;int byk[7]={};int idx=0;
 for(int k:{1,3,5,7,9,11,13}){
  map<int,Pattern> temp;
  for(int i=2;i<=22;i++)for(int j=1;j<i;j++)for(int t:{0,1}){
   int numerator=(1<<i)+(t?(1<<j):-(1<<j));
   if(numerator%k)continue;
   int d=numerator/k;
   if(d>0&&d<=HI-LO&&d%2==0&&!old.count(d))temp.emplace(d,Pattern{k,i,j,t});
  }
  byk[idx++]=temp.size();
  for(auto [d,p]:temp){old.insert(d);if(k>1)newones.emplace(d,p);}
 }
 assert(old.size()==520&&newones.size()==247);
 assert(byk[0]==256&&byk[1]==105&&byk[2]==56&&byk[3]==26&&byk[4]==30&&byk[5]==18&&byk[6]==12);
 cout<<"gap,k,i,j,plus,ordered_all,ordered_old_E,ordered_panel_P4,ordered_both,ordered_new,checked_witnesses\n";
 u64 all=0,e=0,p=0,both=0,net=0,witnesses=0;
 for(auto [d,pat]:newones){
  u64 A=0,E=0,R=0,B=0,V=0,W=0;
  for(int b=LO;b+d<=HI;b+=2){
   int a=b+d;
   int period=1<<(pat.j+1),s=1<<pat.j;
   u64 x=( (long long)pat.t*s -(long long)pat.k*a + (long long)period*(pat.k*a/period+2))%period;
   u64 y=x+(u64)pat.k*a;
   u64 e1=x+(1ULL<<pat.i),e2=y+(pat.t?-s:s);
   assert(x<N&&y<N&&e1<N&&e2<N);
   assert(((x>>pat.i)&1)==0&&((y>>pat.j)&1)==(u64)pat.t);
   assert((x^(1ULL<<pat.i))==e1&&(y^(1ULL<<pat.j))==e2);
   assert(y-x==(u64)pat.k*a&&e2-e1==(u64)pat.k*b);
   assert(x%a==y%a&&e1%b==e2%b);
   W++;
   bool v=(u64)a*b<T||U.count(a)||U.count(b)|| (u64)a/gcd(a,b)*b<N ||33*((N+a-1)/a)>(u64)b||33*((N+b-1)/b)>(u64)a;
   bool r=P.count(a)||P.count(b);
   A+=2;E+=2*v;R+=2*r;B+=2*(v&&r);V+=2*(!v&&!r);
  }
  assert(A==2*(M-d/2)&&V==A-E-R+B);
  cout<<d<<","<<pat.k<<","<<pat.i<<","<<pat.j<<","<<pat.t<<","<<A<<","<<E<<","<<R<<","<<B<<","<<V<<","<<W<<"\n";
  all+=A;e+=E;p+=R;both+=B;net+=V;witnesses+=W;
 }
 cerr<<"GAPS="<<newones.size()<<" ALL="<<all<<" E="<<e<<" PANEL="<<p<<" BOTH="<<both<<" ADDED="<<net<<" WITNESSES="<<witnesses<<" COMBINED="<<(7663771438ULL+net)<<" COMPLEMENT="<<(u64(M)*M-7663771438ULL-net)<<"\n";
}
