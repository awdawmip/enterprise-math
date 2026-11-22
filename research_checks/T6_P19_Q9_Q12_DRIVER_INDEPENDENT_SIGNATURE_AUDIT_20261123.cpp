// Independent nonblind re-audit of maximal-p19 mixed-digit necessary signatures.
// Authors of original p19 result: EM-X6-FB6990. Reviewer: EM-DVR-DEBB5E.
// Complete signed-side states, exact mass <=2331, 19-smooth cofactor dictionary.
// This checker uses extended-Euclid inverses and signature-image injectivity,
// not the original code's support-mask pair-join.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <unordered_map>
#include <vector>
using U=uint64_t;
constexpr int P=19, LIMIT=2331;
constexpr std::array<int,6> mods{19,361,6859,6859,6859,6859};
using Raw=std::array<int,6>;
struct Part {int mass; U sig;};
struct Atom {int q,mass;U sig;};
U encode(const Raw& x){U mul=1,ret=0;for(int i=0;i<6;i++){ret+=mul*x[i];mul*=mods[i];}return ret;}
Raw decode(U x){Raw a{};for(int k=0;k<6;k++){a[k]=x%mods[k];x/=mods[k];}return a;}
U add(U a,U b){Raw x=decode(a),y=decode(b);for(int k=0;k<6;k++)x[k]=(x[k]+y[k])%mods[k];return encode(x);}
U mul(U a,int n){Raw x=decode(a);for(int k=0;k<6;k++)x[k]=int((int64_t(x[k])*n)%mods[k]);return encode(x);}
int inv(int x,int mod){int b=x%mod,t=0,nt=1,r=mod,nr=b;while(nr){int q=r/nr;int v=t-q*nt;t=nt;nt=v;v=r-q*nr;r=nr;nr=v;}assert(r==1);return (t%mod+mod)%mod;}
U signature(int c){Raw a{};for(int k=0;k<6;k++){int y=inv(c,mods[k]);int z=1;for(int j=0;j<=k;j++)z=int((int64_t(z)*y)%mods[k]);a[k]=z;}return encode(a);}
bool smooth(int c){for(int p:{2,3,5,7,11,13,17,19})while(c%p==0)c/=p;return c==1;}
std::vector<Atom> atoms;
std::vector<Part> vertical(int order){std::vector<Part> out;auto recurse=[&](auto&& self,int idx,int q,int cost,U sig)->void{
 if(!q){out.push_back({cost,sig});return;}
 for(int i=idx;i<(int)atoms.size();i++){const auto&a=atoms[i];if(a.q<=q&&cost+a.mass<=LIMIT)self(self,i,q-a.q,cost+a.mass,add(sig,a.sig));}
};recurse(recurse,0,order,0,0);return out;}
std::vector<Part> q0parts(int cap){std::vector<Part> out;std::array<U,19> qs{};for(int j=1;j<=18;j++)qs[j]=signature(j);
 auto recurse=[&](auto&& self,int j,int mass,U sig)->void{
  if(j==19){out.push_back({mass,sig});return;}
  U curr=0;for(int times=0;mass+times*(19*j-1)<=cap;times++){
   self(self,j+1,mass+times*(19*j-1),add(sig,curr));curr=add(curr,qs[j]);
  }
 };recurse(recurse,1,0,0);
 std::sort(out.begin(),out.end(),[](const Part&a,const Part&b){return a.mass<b.mass;});return out;}
struct SideStats{U count=0,duplicates=0;};
SideStats side(const std::vector<Part>& vs,const std::vector<Part>& qs,std::unordered_map<U,int>* sigs){SideStats st;for(auto &v:vs){auto end=std::upper_bound(qs.begin(),qs.end(),LIMIT-v.mass,[](int cost,const Part& x){return cost<x.mass;});for(auto it=qs.begin();it!=end;it++){U s=add(v.sig,it->sig);st.count++;if(sigs){int &cnt=(*sigs)[s];st.duplicates+=(cnt>0);cnt++;}}}return st;}
int main(){for(int q=1;q<=6;q++)for(int r=1;r<=18;r++){int c=19*q+r;if(smooth(c))atoms.push_back({q,19*c-1,signature(c)});}assert(atoms.size()==64);
 std::array<std::vector<Part>,7> v;for(int k=3;k<=6;k++)v[k]=vertical(k);
 std::cout<<"atoms="<<atoms.size()<<" vertical3-6=";for(int k=3;k<=6;k++)std::cout<<v[k].size()<<" ";std::cout<<"\n";
 for(auto [a,b]: {std::pair{3,6}, {4,5}, {4,6}, {5,5}, {5,6}, {6,6}}){int ca=LIMIT,cb=LIMIT;for(auto &p:v[a])ca=std::min(ca,p.mass);for(auto &p:v[b])cb=std::min(cb,p.mass);int cap=std::max(LIMIT-ca,LIMIT-cb);
 auto qs=q0parts(cap);
 std::unordered_map<U,int> vals;vals.reserve(1000000);
 auto sb=side(v[b],qs,&vals); U ca_count=0,match=0;for(auto &vv:v[a]){auto end=std::upper_bound(qs.begin(),qs.end(),LIMIT-vv.mass,[](int cost,const Part& x){return cost<x.mass;});for(auto it=qs.begin();it!=end;it++){ca_count++;auto f=vals.find(add(vv.sig,it->sig));if(f!=vals.end())match+=f->second;}}
 std::cout<<a<<","<<b<<" q0="<<qs.size()<<" states="<<ca_count<<","<<sb.count<<" distinctB="<<vals.size()<<" dupB="<<sb.duplicates<<" matching_oriented="<<match<<std::endl;
 }
}
