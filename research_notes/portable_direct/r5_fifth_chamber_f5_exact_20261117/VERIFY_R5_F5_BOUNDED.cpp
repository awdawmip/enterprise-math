// Exact bounded-cost feasibility for full 256-state R5 fifth chamber, at most 5 arbitrary errors.
#include <bits/stdc++.h>
using namespace std;
using Word=uint64_t;
struct State { array<Word,24> x{}; bool operator==(State const&o)const noexcept{return x==o.x;} };
struct Hash {size_t operator()(State const&s) const noexcept {uint64_t h=0x9e3779b97f4a7c15ULL;for(auto x:s.x){x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;x*=0x94d049bb133111ebULL;x^=x>>31;h^=x+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);}return h;}};
struct Mask{array<Word,4>x{};};
struct Act{int k;vector<Mask> support,comp;};
vector<Act> acts;
// Cache win and loss budgets: true at min_win; false at max_loss
struct Rec{uint16_t win=UINT16_MAX, loss=0; uint8_t move=255;};
unordered_map<State,Rec,Hash> cache;
uint64_t calls=0,hits=0,checks=0; chrono::steady_clock::time_point t0;
bool term(State const&s){int cnt=0;for(int j=0;j<4;j++){Word u=0;for(int l=0;l<6;l++)u|=s.x[l*4+j];cnt+=__builtin_popcountll(u);if(cnt>1)return false;}return true;}
bool solve(State const&s,int bound){
 if(term(s))return true;
 if(bound<214)return false;
 auto it=cache.find(s);
 if(it!=cache.end()){if(bound>=it->second.win){hits++;return true;}if(bound<=it->second.loss){hits++;return false;}}
 int chosen=-1;bool yes=false;
 for(int ai=0;ai<(int)acts.size();ai++){
  auto const&a=acts[ai];if(a.k>bound)continue;
  bool okay=true;
  for(size_t ri=0;ri<a.support.size();ri++){
   State z{};for(int j=0;j<4;j++){
    Word v=a.support[ri].x[j],nv=a.comp[ri].x[j];z.x[j]=s.x[j]&v;
    for(int l=1;l<6;l++)z.x[l*4+j]=(s.x[l*4+j]&v)|(s.x[(l-1)*4+j]&nv);
   }
   if(z==s){okay=false;break;}
   if(!solve(z,bound-a.k)){okay=false;break;}
  }
  if(okay){yes=true;chosen=ai;break;}
 }
 Rec &rec=cache[s];
 if(yes){if(bound<rec.win){rec.win=bound;rec.move=chosen;}}
 else{rec.loss=max(rec.loss,(uint16_t)bound);}
 calls++;
 if(calls%1000000==0){auto sec=chrono::duration_cast<chrono::seconds>(chrono::steady_clock::now()-t0).count();cerr<<"states="<<cache.size()<<" decided="<<calls<<" checks="<<checks<<" time="<<sec<<"s\n";}
 return yes;
}
int main(int argc,char**argv){if(argc<3){cerr<<"usage: program response_actions budget\n";return 2;}ifstream f(argv[1]);int n;f>>n;for(int i=0;i<n;i++){Act a;int nr;f>>a.k>>nr;for(int z=0;z<nr;z++){Mask m{},c{};for(int q=0;q<4;q++){f>>m.x[q];c.x[q]=~m.x[q];}a.support.push_back(m);a.comp.push_back(c);}acts.push_back(move(a));}
 State root{};for(int j=0;j<4;j++)root.x[j]=ULLONG_MAX;
 t0=chrono::steady_clock::now();int b=atoi(argv[2]);bool yes=solve(root,b);cout<<"F5_FEASIBLE="<<(yes?"YES":"NO")<<" BUDGET="<<b<<" STATES="<<cache.size()<<" DECISIONS="<<calls<<"\n";return yes?0:1;}