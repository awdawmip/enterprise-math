// Exact R5 fifth-chamber bounded-cost solver, f=0..7, full 256 named states.
// Four bitplanes store a mismatch count 0..7 or eliminated=8 for each hypothesis.
// Lossless wrt the declared scalar observation/update language, not native X6 state.
#include <array>
#include <vector>
#include <unordered_map>
#include <fstream>
#include <iostream>
#include <cstdint>
#include <climits>
#include <chrono>
#include <cstdlib>
using namespace std;
using Word=uint64_t;
struct State { array<Word,16> x{}; bool operator==(State const &o) const noexcept{return x==o.x;} };
struct Hash {size_t operator()(State const&s) const noexcept {uint64_t h=0x9e3779b97f4a7c15ULL;for(auto x:s.x){x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;h^=x+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);}return h;}};
struct Mask {array<Word,4> x{};};
struct Act {int k;vector<Mask> sup,comp;};
struct Rec {uint16_t win=UINT16_MAX, loss=0;uint8_t move=255;};
vector<Act> acts;
unordered_map<State,Rec,Hash> memo;
uint64_t decisions=0;
auto start_clock=chrono::steady_clock::now();
bool terminal(State const &s){
 unsigned count=0;
 for(int w=0;w<4;w++){count+=__builtin_popcountll(~s.x[12+w]); if(count>1)return false;}
 return true;
}
State successor(State const &s,Mask const &support){
 State z;
 for(int w=0;w<4;w++){
  Word a=~support.x[w] & ~s.x[12+w];
  Word p0=s.x[w], p1=s.x[4+w], p2=s.x[8+w],p3=s.x[12+w];
  z.x[w]=p0 ^ a;
  Word carry=p0 & a;
  z.x[4+w]=p1 ^ carry;
  carry&=p1;
  z.x[8+w]=p2 ^ carry;
  carry&=p2;
  z.x[12+w]=p3 ^ carry;
 }
 return z;
}
bool solve(State const&s,int bound){
 if(terminal(s))return true;
 if(bound<214)return false;
 auto it=memo.find(s);
 if(it!=memo.end()){
  if(bound>=it->second.win)return true;
  if(bound<=it->second.loss)return false;
 }
 bool yes=false;int chosen=-1;
 for(int ai=0;ai<(int)acts.size();ai++){
  Act const &a=acts[ai];if(a.k>bound)continue;
  bool okay=true;
  for(auto const &support:a.sup){
    State z=successor(s,support);
    if(z==s || !solve(z,bound-a.k)){okay=false;break;}
  }
  if(okay){yes=true;chosen=ai;break;}
 }
 Rec &r=memo[s];
 if(yes){if(bound<r.win){r.win=bound;r.move=chosen;}}
 else if(bound>r.loss)r.loss=bound;
 decisions++;
 if(decisions%1000000==0){auto dt=chrono::duration_cast<chrono::seconds>(chrono::steady_clock::now()-start_clock).count();cerr<<"states="<<memo.size()<<" decisions="<<decisions<<" time="<<dt<<"s\n";}
 return yes;
}
int main(int argc,char**argv){
 if(argc<4){cerr<<"usage: verify actions.txt budget f(0..7)\n";return 2;}
 ifstream f(argv[1]);int n; if(!(f>>n))return 2;
 for(int i=0;i<n;i++){
  Act a;int cnt;f>>a.k>>cnt;
  for(int j=0;j<cnt;j++){Mask m,c;
   for(int w=0;w<4;w++){f>>m.x[w];c.x[w]=~m.x[w];}
   a.sup.push_back(m);a.comp.push_back(c);
  } acts.push_back(move(a));
 }
 int b=atoi(argv[2]),errors=atoi(argv[3]);if(errors<0||errors>7)return 2;
 State root;int initial=7-errors;
 for(int p=0;p<4;p++) if(initial & (1<<p))
   for(int w=0;w<4;w++)root.x[p*4+w]=UINT64_MAX;
 bool yes=solve(root,b);
 cout<<"EXACT_R5_BITPLANE f="<<errors<<" feasible="<<(yes?"YES":"NO")
     <<" budget="<<b<<" memo="<<memo.size()<<" decisions="<<decisions<<"\n";
 return yes?0:1;
}
