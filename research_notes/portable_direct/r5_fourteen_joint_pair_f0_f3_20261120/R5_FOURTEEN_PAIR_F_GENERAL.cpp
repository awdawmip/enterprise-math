// Exact Bellman f>=1 on representatives from all fourteen-label priced joint support classes.
// Tested f=1,2,3 using frozen R5 scalar input. Source SHA256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b.
#define main original_census_main
#include "R5_FOURTEEN_PAIR_F0.cpp"
#undef main
struct DPF{
 const Sig& acts; unordered_map<uint64_t,int> memo; uint64_t w[K]; int f,b; size_t visits=0,cap;
 DPF(const Sig&a,int ff,size_t cp=2000000):acts(a),cap(cp),f(ff),b(ff+2){w[0]=1;for(int i=1;i<K;i++)w[i]=w[i-1]*b;memo.reserve(25000);}
 int V(uint64_t state){auto it=memo.find(state);if(it!=memo.end())return it->second;int e[K],live=0;auto s=state;for(int i=0;i<K;i++){e[i]=s%b;s/=b;if(e[i]<=f)live|=(1<<i);}if(__builtin_popcount((unsigned)live)<=1)return 0;if(++visits>cap)throw runtime_error("CAP_REACHED");int best=1000000;
 for(const auto& a:acts){bool stall=0;for(int m:a.ms)if((m&live)==live){stall=1;break;}if(stall)continue;
 int worst=0;for(int m:a.ms){uint64_t next=state;for(int i=0;i<K;i++)if(e[i]<f+1&&!(m&(1<<i)))next+=w[i];int v=V(next);worst=max(worst,v);if(a.k+worst>=best)break;}best=min(best,a.k+worst);}
 if(best==1000000)throw runtime_error("NO_PROGRESS");memo.emplace(state,best);return best;
 }
};
int main(int argc,char**argv){if(argc<4){cerr<<"USAGE adj.bin pairF0.csv output.csv [maxclasses=0(all)] [cap] [f=2]";return 2;}ifstream fi(argv[1],ios::binary);vector<uint8_t>adj((size_t)Q*N*N);fi.read((char*)adj.data(),adj.size());if(fi.gcount()!=(streamsize)adj.size())return 3;
 ifstream in(argv[2]);string line;getline(in,line);map<int,pair<int,int>> rep;size_t rows=0;while(getline(in,line)){replace(line.begin(),line.end(),',',' ');istringstream s(line);int u,v,f0,c; if(!(s>>u>>v>>f0>>c))throw runtime_error("BAD_CSV");if(f0!=735)throw runtime_error("UNEXPECTED_F0");rep.try_emplace(c,make_pair(u,v));rows++;}
 if(rows!=29646||rep.size()!=1906)throw runtime_error("BAD_CENSUS");int maxclasses=argc>4?stoi(argv[4]):0;size_t cap=argc>5?stoull(argv[5]):2000000;int f=argc>6?stoi(argv[6]):2;ofstream o(argv[3]);o<<"class,u,v,f"<<f<<",states,actions\n";int n=0;map<int,int> dist;auto t=chrono::steady_clock::now();for(auto [c,pair]:rep){auto a=signature(adj,pair.first,pair.second);DPF dp(a,f,cap);try {int v=dp.V(0);o<<c<<","<<pair.first<<","<<pair.second<<","<<v<<","<<dp.visits<<","<<a.size()<<"\n";dist[v]++;n++;}catch(exception& e){cerr<<"ERROR class="<<c<<" pair="<<pair.first<<","<<pair.second<<" "<<e.what()<<"\n";return 4;}
 if(n%100==0)cerr<<"CLASS "<<n<<" sec="<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<"\n";
 if(maxclasses&&n>=maxclasses)break;}
 o.flush();cerr<<"SOLVED="<<n<<" sec="<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<"\n";for(auto [v,k]:dist)cerr<<"V"<<f<<"="<<v<<" classes="<<k<<"\n";
}
