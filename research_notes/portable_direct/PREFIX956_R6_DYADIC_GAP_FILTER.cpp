#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
struct Term {int v,i,j,s;};
struct Hit {uint64_t id;unsigned m;};
int main(){
 const int H=1<<18,L=H+1,U=2*H-1,M=H/2;
 vector<Term> terms;
 for(int i=0;i<19;i++)for(int j=0;j<19;j++)for(int s:{-1,1})terms.push_back({(1<<i)-s*(1<<j),i,j,s});
 array<uint64_t,7> total{},after_mod4{},after_2adic{},after_integer{},inrange{},sourcelaw{};
 vector<Hit> hits; hits.reserve(12000);
 for(int m=0;m<=6;m++)for(int t=1;t<=42;t++){
  const int T=t+m; if(T>46)continue;
  const int d=2*t-21*m; if(d==0)continue;
  unsigned vd=__builtin_ctz((unsigned)(d<0?-d:d));
  const int64_t mod2=(int64_t)2<<vd, bit=(int64_t)1<<vd;
  for(const auto &x:terms)for(const auto &y:terms){
   total[m]++;
   int delta=y.v-x.v;
   if(m&1){if(!(delta&1))continue;}else if((delta&3)!=((m&2)?0:2))continue;
   after_mod4[m]++;
   int64_t na=int64_t(t)*y.v-int64_t(T)*x.v;
   int64_t nb=21LL*y.v-23LL*x.v;
   if(((na%mod2)+mod2)%mod2!=bit || ((nb%mod2)+mod2)%mod2!=bit)continue;
   after_2adic[m]++;
   if(na%d || nb%d)continue;
   after_integer[m]++;
   int64_t a=na/d,b=nb/d;
   if(a<L || a>U || b<L || b>U || !(a&1) || !(b&1))continue;
   inrange[m]++;
   int64_t ka=21*a, la=23*a;
   if((1-2*((ka>>x.j)&1))!=x.s || (1-2*((la>>y.j)&1))!=y.s)continue;
   int64_t left1=(ka^(1LL<<x.j))-(1LL<<x.i);
   int64_t left2=(la^(1LL<<y.j))-(1LL<<y.i);
   if(left1!=t*b || left2!=T*b || left1<=0 || left2<=0 || left1>=(1LL<<32) || left2>=(1LL<<32))continue;
   sourcelaw[m]++;
   uint64_t id=uint64_t((a-L)/2)*M+(b-L)/2;
   hits.push_back({id,unsigned(m)});
  }
 }
 sort(hits.begin(),hits.end(),[](const Hit&a,const Hit&b){return a.id<b.id || (a.id==b.id && a.m<b.m);});
 array<uint64_t,7> member{}; map<unsigned,int> maskhist;
 vector<uint64_t> off; off.reserve(6203);
 int multiple=0, diag=0;
 for(size_t i=0;i<hits.size();){size_t j=i;unsigned mask=0;uint64_t id=hits[i].id;
  while(j<hits.size()&&hits[j].id==id){mask|=1U<<hits[j].m;j++;}
  maskhist[mask]++;if(mask&(mask-1))multiple++;
  int a=L+2*(id/M), b=L+2*(id%M);
  if(a!=b)off.push_back(id);else diag++;
  for(int m=0;m<=6;m++)if(mask>>m&1)member[m]++;
  i=j;
 }
 ofstream out("PREFIX956_NONDIAGONAL_IDS.bin",ios::binary);
 for(uint64_t id:off)out.write(reinterpret_cast<const char*>(&id),8);
 out.close();
 auto print=[&](const char*name,const array<uint64_t,7>&a){cout<<name<<": ";for(auto x:a)cout<<x<<" ";cout<<"\n";};
 print("TOTAL",total);print("AFTER_MOD4",after_mod4);print("AFTER_2ADIC",after_2adic);
 print("AFTER_INTEGER_DIV",after_integer);print("IN_RANGE",inrange);print("SOURCE_VALID",sourcelaw);print("PAIR_MEMBERS",member);
 cout<<"TOTAL_PAIRS="<<off.size()+diag<<" OFF="<<off.size()<<" DIAG="<<diag<<" MULTI="<<multiple<<"\nMASKS:";
 for(auto [m,n]:maskhist){cout<<" "<<m<<":"<<n;}cout<<"\n";
}
