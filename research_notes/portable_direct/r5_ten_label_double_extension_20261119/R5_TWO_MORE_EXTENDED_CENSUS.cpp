#define main hidden_f01_main
#include "R5_TWO_MORE_F01_CENSUS.cpp"
#undef main
#include <chrono>

struct SolverF {
 int f,base; uint64_t pw[KK];
 unordered_map<uint64_t,int> mem;
 size_t calls=0,maxstates;
 explicit SolverF(int F,size_t maxs):f(F),base(F+2),maxstates(maxs){pw[0]=1;for(int i=1;i<KK;i++)pw[i]=pw[i-1]*base;mem.reserve(20000);}
 int rec(uint64_t idx,const Signature& a){
  if(auto it=mem.find(idx);it!=mem.end())return it->second;
  uint64_t tmp=idx;int e[KK],live=0;
  for(int i=0;i<KK;i++){e[i]=tmp%base;tmp/=base;if(e[i]<=f)live|=1<<i;}
  if(__builtin_popcount((unsigned)live)<=1)return 0;
  if(++calls>maxstates)throw runtime_error("STATE_CAP_REACHED");
  int best=INT32_MAX/8;
  for(auto&act:a){
    bool skip=false;for(int m:act.masks)if((m&live)==live){skip=true;break;}
    if(skip)continue;
    int worst=0;
    for(int m:act.masks){uint64_t nxt=idx;for(int i=0;i<KK;i++)if(!(m&(1<<i))&&e[i]<f+1)nxt+=pw[i];
      worst=max(worst,rec(nxt,a));if(act.cost+worst>=best)break;}
    best=min(best,act.cost+worst);
  }
  if(best==INT32_MAX/8)throw runtime_error("NO_PROGRESS");
  mem[idx]=best;return best;
 }
};

int main(int argc,char**argv){
 int maxF=argc>1?stoi(argv[1]):2;
 if(maxF<2||maxF>8)throw runtime_error("maxF 2..8");
 ifstream f("window_adj.bin",ios::binary);vector<unsigned char> adj((size_t)QQ*NN*NN);
 f.read((char*)adj.data(),adj.size());if(!f||f.gcount()!=(streamsize)adj.size())throw runtime_error("bad adjacency");
 vector<int> pool;for(int t=0;t<NN;t++)if(find(seed.begin(),seed.end(),t)==seed.end())pool.push_back(t);
 map<string,int> ids;vector<Signature> unique;vector<int> counts;vector<vector<int>> scores;
 vector<vector<pair<int,int>>> members;
 for(int i=0;i<(int)pool.size();i++)for(int j=i+1;j<(int)pool.size();j++){
  int t=pool[i],u=pool[j];auto act=build(adj,t,u);string s=key(act);auto it=ids.find(s);int id;
  if(it==ids.end()){
   id=unique.size();ids.emplace(move(s),id);unique.push_back(move(act));
   counts.push_back(0);members.push_back({});
   vector<int> r={solve_f0(unique.back()),Solver1().root(unique.back()).first};
   scores.push_back(r);
  }else id=it->second;
  counts[id]++;members[id].push_back({t,u});
 }
 cerr<<"TOTAL "<<pool.size()*(pool.size()-1)/2<<" CLASS "<<unique.size()<<"\n"<<flush;
 for(int ff=2;ff<=maxF;ff++){
  auto st=chrono::steady_clock::now();long long totalStates=0;int omitted=0;
  map<int,int> distribution;
  for(int id=0;id<(int)unique.size();id++){
   try{
    SolverF s(ff,5000000);
    int val=s.rec(0,unique[id]);
    scores[id].push_back(val);distribution[val]+=counts[id];totalStates+=s.mem.size();
   }catch(const exception&e){scores[id].push_back(-1);omitted+=counts[id];}
   if(id%250==0)cerr<<"f="<<ff<<" id="<<id<<" seconds="<<chrono::duration<double>(chrono::steady_clock::now()-st).count()<<"\n"<<flush;
  }
  cerr<<"STAGE "<<ff<<" SECONDS "<<chrono::duration<double>(chrono::steady_clock::now()-st).count()<<" STATES "<<totalStates<<" OMITTED "<<omitted<<"\n";
  for(auto [v,n]:distribution)cerr<<"V"<<ff<<"="<<v<<" COUNT="<<n<<"\n";
 }
 cout<<"#t,u,class_id";for(int ff=0;ff<=maxF;ff++)cout<<",f"<<ff;cout<<"\n";
 for(int id=0;id<(int)unique.size();id++)for(auto [t,u]:members[id]){
  cout<<t<<","<<u<<","<<id;for(int x:scores[id])cout<<","<<x;cout<<"\n";
 }
}
