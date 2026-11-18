// Exact minimax for full 256-state R5 fifth chamber, f=4, five physical budgets.
// Input: response-family bitmasks generated from frozen exact counts at tau=U-1.
#include <bits/stdc++.h>
using namespace std;
using Word = uint64_t;
struct Mask {array<Word,4> x{};};
struct State {array<Word,20> x{}; bool operator==(State const& o) const noexcept{return x==o.x;}};
struct Hash {size_t operator()(State const& s)const noexcept {
  uint64_t h=0x9e3779b97f4a7c15ULL;
  for(auto x:s.x){x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;x*=0x94d049bb133111ebULL;x^=x>>31;h ^=x+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);}
  return (size_t)h;
}};
struct Act{int k; vector<Mask> answers,comp;};
vector<Act> actions;
unordered_map<State,uint16_t,Hash> memo;
uint64_t calls=0; chrono::steady_clock::time_point t0;
inline bool terminal(State const& s){ int cnt=0; for(int j=0;j<4;j++){
  Word u=0;for(int layer=0;layer<5;layer++)u|=s.x[layer*4+j];
  cnt+=__builtin_popcountll(u); if(cnt>1)return false;
}return true;}
int solve(State const& s){
 if(terminal(s))return 0;
 auto it=memo.find(s);if(it!=memo.end())return it->second;
 uint32_t best=0x7ffffff;
 for(Act const&a:actions){
  int worst=0;
  bool ok=true;
  for(size_t r=0;r<a.answers.size();r++){
   State z{};
   for(int j=0;j<4;j++){
    Word v=a.answers[r].x[j],nv=a.comp[r].x[j];
    z.x[j] = s.x[j]&v;
    for(int layer=1;layer<5;layer++)z.x[layer*4+j] = (s.x[layer*4+j]&v) | (s.x[(layer-1)*4+j]&nv);
   }
   if(z==s){ok=false;break;}
   int q=solve(z);if(q>worst)worst=q;
   if(a.k+worst>=best){ok=false;break;}
  }
  if(ok && a.k+worst<best)best=a.k+worst;
 }
 if(best>1000000){cerr<<"invalid cycle"<<endl;exit(9);}
 memo.emplace(s,(uint16_t)best);
 calls++;
 if(calls%1000000==0){auto sec=chrono::duration_cast<chrono::seconds>(chrono::steady_clock::now()-t0).count();cerr<<"state_count="<<calls<<" time="<<sec<<"s"<<"\n";}
 return best;
}
int main(int argc,char**argv){
 if(argc<2){cerr<<"usage: cpp f4_actions.txt";return 2;}
 ifstream f(argv[1]);int n;f>>n;
 for(int i=0;i<n;i++){
  Act a;int nr;f>>a.k>>nr;
  for(int z=0;z<nr;z++){
   Mask m{},c{};for(int q=0;q<4;q++){f>>m.x[q];c.x[q]=~m.x[q];}a.answers.push_back(m);a.comp.push_back(c);
  }
  actions.push_back(std::move(a));
 }
 State initial{};for(int j=0;j<4;j++)initial.x[j]=ULLONG_MAX;
 t0=chrono::steady_clock::now();
 memo.reserve(11000000);
 int val=solve(initial);
 cout<<"EXACT_F4_COST="<<val<<" MEMO_STATES="<<memo.size()<<" ACTION_COUNT="<<actions.size()<<"\n";
}
