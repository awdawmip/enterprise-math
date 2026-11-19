#include <sstream>
#define main ignore_main
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
 int error=argc>1?stoi(argv[1]):8;
 ifstream f("window_adj.bin",ios::binary);vector<unsigned char> adj((size_t)QQ*NN*NN);
 f.read((char*)adj.data(),adj.size());if(!f||f.gcount()!=(streamsize)adj.size())throw runtime_error("bad adjacency");
 ifstream in("R5_TWO_MORE_REPS.csv");string line;int cls,t,u,ct,done=0;
 cout<<"class_id,representative_t,representative_u,multiplicity,f"<<error<<",states,seconds\n"<<flush;
 while(getline(in,line)){
   replace(line.begin(),line.end(),',',' ');istringstream is(line);is>>cls>>t>>u>>ct;
   auto act=build(adj,t,u);auto st=chrono::steady_clock::now();int res=-1,states=0;
   try{SolverF solver(error,7000000);res=solver.rec(0,act);states=(int)solver.mem.size();}
   catch(const exception&e){cerr<<"ERROR_CLASS "<<cls<<" "<<e.what()<<"\n";}
   double sec=chrono::duration<double>(chrono::steady_clock::now()-st).count();
   cout<<cls<<","<<t<<","<<u<<","<<ct<<","<<res<<","<<states<<","<<sec<<"\n"<<flush;
   done++;if(done%50==0)cerr<<"DONE "<<done<<" LAST "<<cls<<" SEC "<<sec<<"\n"<<flush;
 }
}
