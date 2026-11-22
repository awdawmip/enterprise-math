// Necessary six inverse-power congruences for p19 valuation-one components.
// Source scientific scope: q10..q12, j=1..18, mass<=2331, signed support-disjoint.
// Enumeration of the first congruence digit is a necessary filter, NOT a whole-collision test.
// Lower-prime completion is NOT discarded: its contribution vanishes mod 19
// after multiplying the kth reciprocal moment equality by 19^k.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <unordered_map>
#include <vector>
using u64=uint64_t;
constexpr int P=19,B=2331;using Sig=uint32_t;
int ipow[19][7];
Sig sigatom(int residue){Sig out=0,mul=1;for(int k=1;k<=6;k++){out+=mul*ipow[residue][k];mul*=19;}return out;}
Sig addsig(Sig a,Sig b){Sig out=0,mul=1;for(int k=1;k<=6;k++){int digit=((a%19)+(b%19))%19;out+=mul*digit;mul*=19;a/=19;b/=19;}return out;}
Sig timesig(Sig a,int t){Sig out=0,mul=1;for(int k=1;k<=6;k++){out+=mul*int(((a%19)*t)%19);mul*=19;a/=19;}return out;}
const int primes[]={2,3,5,7,11,13,17,19};
bool smooth(int v){for(int p:primes)while(v%p==0)v/=p;return v==1;}
struct Atom{int q,a,w;Sig sig;};
struct Part{int m,n;Sig sig;u64 mask;};
struct Target{u64 vmask;uint32_t qmask;uint32_t vi,qi;};
std::vector<Atom> atoms;std::vector<Part> vA,vB,q0;
void vert(std::vector<Part>&o,int start,int rem,int m,int n,Sig sig,u64 mask){
 if(!rem){o.push_back({m,n,sig,mask});return;}
 for(int i=start;i<(int)atoms.size();i++){auto&a=atoms[i];if(a.q>rem||m+a.w>B)continue;vert(o,i,rem-a.q,m+a.w,n+1,addsig(sig,a.sig),mask|(1ULL<<i));}
}
void qgen(int j,int cap,int m,int n,Sig sig,uint32_t mask){
 if(j==P){q0.push_back({m,n,sig,mask});return;}
 int w=P*j-1;Sig s=sigatom(j);
 for(int t=0;m+t*w<=cap;t++)qgen(j+1,cap,m+t*w,n+t,addsig(sig,timesig(s,t)),mask|(t?(1U<<(j-1)):0));
}
int main(int argc,char**argv){if(argc!=3)return 2;int qa=atoi(argv[1]),qb=atoi(argv[2]);assert(qa>=1&&qb<=6&&qa+qb>=10&&qa+qb<=12);
 for(int j=1;j<19;j++){int inv=1;while((inv*j)%19!=1)inv++;int t=1;for(int k=1;k<=6;k++){t=(t*inv)%19;ipow[j][k]=t;}}
 for(int q=1;q<=6;q++)for(int r=1;r<19;r++){int a=19*q+r;if(!smooth(a))continue;atoms.push_back({q,a,19*a-1,sigatom(r)});}
 assert(atoms.size()==64);vert(vA,0,qa,0,0,0,0);vert(vB,0,qb,0,0,0,0);
 int ma=B,mb=B;for(auto &v:vA)ma=std::min(ma,v.m);for(auto&v:vB)mb=std::min(mb,v.m);
 qgen(1,std::max(B-ma,B-mb),0,0,0,0);
 std::sort(q0.begin(),q0.end(),[](const Part&a,const Part&b){return a.m<b.m;});
 std::unordered_map<Sig,std::vector<Target>> targets;targets.reserve(70000);
 u64 sideA=0,sideB=0,match=0,disjoint=0;bool printed=false;
 for(uint32_t vi=0;vi<vB.size();vi++){auto&v=vB[vi];for(uint32_t qi=0;qi<q0.size();qi++){auto&q=q0[qi];if(v.m+q.m>B)break;sideB++;targets[addsig(v.sig,q.sig)].push_back({v.mask,(uint32_t)q.mask,vi,qi});}}
 for(uint32_t vi=0;vi<vA.size();vi++){auto&v=vA[vi];for(uint32_t qi=0;qi<q0.size();qi++){auto&q=q0[qi];if(v.m+q.m>B)break;sideA++;auto it=targets.find(addsig(v.sig,q.sig));if(it==targets.end())continue;
  for(auto&t:it->second){match++;if((v.mask&t.vmask)||(q.mask&t.qmask))continue;disjoint++;if(!printed){std::cerr<<"FIRST_DISJOINT q="<<qa<<","<<qb<<" A_vi="<<vi<<" A_qi="<<qi<<" B_vi="<<t.vi<<" B_qi="<<t.qi<<" A_mass="<<v.m+q.m<<" B_mass="<<vB[t.vi].m+q0[t.qi].m<<" signature="<<addsig(v.sig,q.sig)<<"\n";printed=true;}}
 }}
 if(qa==qb){assert(match%2==0||match>=sideA);assert(disjoint%2==0);disjoint/=2;}
 std::cout<<"{\"q_split\":["<<qa<<","<<qb<<"],\"vertical_atoms\":"<<atoms.size()<<",\"vertical_rosters\":["<<vA.size()<<","<<vB.size()<<"],\"q0_multisets\":"<<q0.size()<<",\"side_states\":["<<sideA<<","<<sideB<<"],\"matching_first_six_mod19_oriented\":"<<match<<",\"disjoint_unordered\":"<<disjoint<<"}\n";
}
