// Independent C++17 exact-integer replication for R4-EC9.
// Derives 12th-order Laurent operator from four displayed factors;
// advances original 14-state BRC directly; does not read Python/JSON outputs.
#include <boost/multiprecision/cpp_int.hpp>
#include <cassert>
#include <iostream>
#include <map>
#include <tuple>
#include <vector>
using boost::multiprecision::cpp_int;
using Key=std::tuple<int,int,int,int>; // q,r,epsilon,t
using Obs=std::tuple<int,int,int,int>; // q,clean=0/dirty=1,epsilon,t
using Hist=std::map<Key,cpp_int>;
using OH=std::map<Obs,cpp_int>;
using Poly=std::map<std::pair<int,int>,long long>; // x-degree, z-degree

Hist update(const Hist& old){
 Hist ans;
 for(const auto& [key,v]:old){
  const auto [q,r,e,t]=key;
  for(int bit=0;bit<=1;++bit){
    int nq=0,eta=1,b=-1;
    if(q==0){nq=2;eta=(bit==0?-1:1);b=-1;}
    else if(q==1){nq=0;eta=(bit==0?-1:1);b=-1;}
    else {nq=(bit==0?1:2);eta=1;b=(bit==0?1:-1);}
    int nr=r==2?2:bit==1?0:r==0?1:2;
    ans[{nq,nr,e*eta,t+e*eta*b}]+=v;
  }
 }
 return ans;
}
OH observe(const Hist& h){ OH ans;for(const auto& [k,v]:h){const auto [q,r,e,t]=k;ans[{q,r==2?1:0,e,t}]+=v;}return ans;}
void plus(Poly& p,int n,int t,long long c){p[{n,t}]+=c;if(!p[{n,t}])p.erase({n,t});}
Poly mul(const Poly&a,const Poly&b){Poly o;for(const auto& [i,u]:a)for(const auto& [j,v]:b)plus(o,i.first+j.first,i.second+j.second,u*v);return o;}
Poly factorS(){Poly p;plus(p,0,0,1);plus(p,1,1,-1);plus(p,1,-1,-1);return p;}
Poly factor1(){Poly p;plus(p,0,0,1);plus(p,2,0,1);return p;}
Poly factorD(){Poly p=factorS();plus(p,4,0,2);plus(p,6,0,-1);return p;}
Poly factorQ(){Poly p=factor1();plus(p,3,1,-1);plus(p,3,-1,-1);return p;}
Hist enumerate_depth(int n){Hist ans;for(unsigned word=0;word<(1u<<n);++word){int q=0,r=0,e=1,t=0;
 for(int j=n-1;j>=0;--j){int bit=(word>>j)&1;
  int nq,eta,b;
  if(q==0||q==1){nq=(q==0?2:0);eta=bit==0?-1:1;b=-1;}
  else {nq=bit==0?1:2;eta=1;b=bit==0?1:-1;}
  r=r==2?2:bit==1?0:r==0?1:2; q=nq;t+=e*eta*b;e*=eta;
 }
 ans[{q,r,e,t}]+=1;
}return ans;}
int main(int argc,char**argv){
 int maxdepth=argc>1?std::stoi(argv[1]):70;
 Poly P=mul(mul(factor1(),factorD()),mul(factorS(),factorQ()));
 int deg=0;for(const auto& [k,v]:P)deg=std::max(deg,k.first);
 assert(deg==12);
 Hist h;h[{0,0,1,0}]=1;
 std::vector<OH> obs;obs.reserve(maxdepth+1);
 cpp_int total=1;long long checks=0;
 for(int n=0;n<=maxdepth;n++){
  cpp_int sum=0;for(const auto& [k,v]:h)sum+=v;assert(sum==total);
  if(n<=12)assert(h==enumerate_depth(n));
  obs.push_back(observe(h));
  // The numerator P*F has x-degree <=12: homogeneous for n>=13.
  if(n>=13){std::map<Obs,cpp_int> lhs;
   for(const auto& [jt,c]:P){const int j=jt.first,delta=jt.second;if(j>n)continue;
     for(const auto& [key,v]:obs[n-j]){auto[q,r,e,t]=key;lhs[{q,r,e,t+delta}]+=c*v;}
   }
   for(const auto& [key,v]:lhs){assert(v==0);checks++;}
  }
  if(n==10){assert(obs[n].at({2,1,1,0})==49);assert(obs[n].at({2,0,1,0})==5);}
  if(n==20){assert(obs[n].at({2,1,1,0})==43307);assert(obs[n].at({2,0,1,0})==463);}
  if(n<maxdepth){h=update(h);total*=2;}
 }
 std::cout<<"PASS depth="<<maxdepth<<" full_original_words_0_12=8191 recurrence_homogeneous_from=13 checks="<<checks<<" polynomial_degree="<<deg<<"\n";
}
