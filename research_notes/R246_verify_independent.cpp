// R246 independent integer-affine verifier: only first X6 axis nontrivial.
// Standalone algebra checker; does not import Enterprise Math source.
#include <array>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <tuple>
#include <stdexcept>
#include <string>
using namespace std;
struct Aff { long long a, b; bool operator==(const Aff& other) const {return tie(a,b)==tie(other.a,other.b);} bool operator<(const Aff& o) const {return tie(a,b)<tie(o.a,o.b);} };
const Aff I{1,0}, N{0,0}, C{1,1}, R{-1,0};
Aff then(Aff early, Aff later) {return {later.a*early.a, later.a*early.b+later.b};}
int pi(int s) {return 4*((s>>3)&1)+2*(((s>>2)&1)^((s>>1)&1))+(s&1);}
int next(int s,int g) {return s^(g==3 ? (8*(((s>>2)&1)^((s>>1)&1))):(8*(s&1)));}
using Edges=array<array<Aff,16>,2>;
int idx(int g){return g==3?0:1;}
Edges effects(bool delayed){Edges e;for(auto& row:e)row.fill(I);for(int s:{2,4}) for(int g:{3,2}) e[idx(g)][s]=N;
 if(delayed) {for(int s:{10,12}) e[idx(2)][s]=C;}
 e[idx(3)][12]=R;
 return e;}
using State=pair<int,Aff>;
State run(int s,int depth,int encoded,const Edges &e){Aff f=I; for(int j=0;j<depth;j++){int g=(encoded&(1<<j))?2:3; f=then(f,e[idx(g)][s]); s=next(s,g);}return {pi(s),f};}
int earliest(const Edges&e,int cap){for(int depth=1;depth<=cap;depth++)for(int w=0;w<(1<<depth);w++)if(run(2,depth,w,e)!=run(4,depth,w,e)) return depth;return -1;}
vector<int> refine(const Edges&e){vector<int> labels(16);for(int s=0;s<16;s++)labels[s]=pi(s);for(int round=0;round<10;round++) {
 map<tuple<int,int,Aff,int,Aff>,int> name;vector<int> newer(16);
 for(int s=0;s<16;s++){
 auto key=make_tuple(labels[s],labels[next(s,3)],e[0][s],labels[next(s,2)],e[1][s]);
 if(!name.count(key)) name[key]=int(name.size());
 newer[s]=name[key];}
 if(newer==labels) return labels;
 labels=move(newer);}
 throw runtime_error("refinement not stabilized");}
int main(){static_assert(sizeof(int)>=4); for(int s=0;s<16;s++){
 if(pi(s)!=pi(s^6)) throw runtime_error("bad parity quotient");
 for(int g:{2,3}) if(next(s^6,g)!=(next(s,g)^6)) throw runtime_error("tau not equivariant");}
 if(!(then(N,R)==N))throw runtime_error("singular masking identity fails");
 for(int mode=0;mode<2;mode++){auto e=effects(mode==0); auto labels=refine(e); int count=0; vector<int> unique;for(auto c:labels)if(find(unique.begin(),unique.end(),c)==unique.end())unique.push_back(c); count=int(unique.size());
 auto first=earliest(e,8);if(count!=10||labels[2]==labels[4]||labels[10]==labels[12])throw runtime_error("strong partition mismatch");
 if(first!=(mode==0?3:-1)) throw runtime_error("first witness mismatch");
 cout<<(mode==0?"delayed":"masked")<<" earliest_observed_depth_1_to_8="<<first<<" strong_classes="<<count<<"\n";
 }
 cout<<"PASS: full exact 1D affine first-axis specialization; six-axis identity extension valid.\n";
}
