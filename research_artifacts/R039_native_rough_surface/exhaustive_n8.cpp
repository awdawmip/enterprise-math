// R039 exact N<=8 FCC/HCP connected-cluster enumerator.
// Integer/combinatorial theorem-critical path only; no metric/radius/floating point.
#include <algorithm>
#include <array>
#include <chrono>
#include <iostream>
#include <limits>
#include <tuple>
#include <unordered_set>
#include <vector>
using namespace std;

struct P {
  int x, y, z;
  bool operator==(P const& o) const { return x == o.x && y == o.y && z == o.z; }
  bool operator<(P const& o) const { return tie(x,y,z) < tie(o.x,o.y,o.z); }
};
struct PH {
  size_t operator()(P const& p) const noexcept {
    uint64_t h = (uint32_t)(p.x * 73856093u) ^ (uint32_t)(p.y * 19349663u) ^ (uint32_t)(p.z * 83492791u);
    return (size_t)h;
  }
};
using Cluster = vector<P>;
struct CH {
  size_t operator()(Cluster const& c) const noexcept {
    size_t h = 1469598103934665603ull;
    for (auto p : c) {
      for (uint32_t v : {(uint32_t)p.x, (uint32_t)p.y, (uint32_t)p.z})
        h ^= (uint64_t)v + 0x9e3779b97f4a7c15ull + (h << 6) + (h >> 2);
    }
    return h;
  }
};

vector<P> fdirs;
vector<array<int,6>> fops;

vector<P> fcc_neighbors(P p) {
  vector<P> out; out.reserve(12);
  for (auto d : fdirs) out.push_back({p.x+d.x,p.y+d.y,p.z+d.z});
  return out;
}
vector<P> hcp_neighbors(P p) {
  static const int td[6][2]={{1,0},{-1,0},{0,1},{0,-1},{1,-1},{-1,1}};
  static const int offA[3][2]={{0,0},{-1,0},{0,-1}};
  static const int offB[3][2]={{0,0},{1,0},{0,1}};
  vector<P> out; out.reserve(12);
  for (auto const& d : td) out.push_back({p.x+d[0],p.y+d[1],p.z});
  auto off = (p.z & 1) ? offB : offA;
  for (int dz : {-1,1}) for (int r=0;r<3;r++) out.push_back({p.x+off[r][0],p.y+off[r][1],p.z+dz});
  return out;
}

P r120(P p) { int e=p.z&1; return {-p.x-p.y-e,p.x,p.z}; }
P hcp_apply(P p,int r,int s,int h,int t) {
  for(int a=0;a<r;a++) p=r120(p);
  if(s) swap(p.x,p.y);
  if(h) p.z=-p.z;
  if(t){p.x=-p.x;p.y=-p.y;p.z+=1;}
  return p;
}

Cluster canon_fcc(Cluster const& c) {
  Cluster best; bool init=false;
  for(auto op:fops){
    Cluster v; v.reserve(c.size()); int perm[3]={op[0],op[1],op[2]}, sg[3]={op[3],op[4],op[5]};
    for(auto p:c){int a[3]={p.x,p.y,p.z};v.push_back({sg[0]*a[perm[0]],sg[1]*a[perm[1]],sg[2]*a[perm[2]]});}
    sort(v.begin(),v.end()); P q=v[0];
    for(auto& p:v){p.x-=q.x;p.y-=q.y;p.z-=q.z;}
    sort(v.begin(),v.end()); if(!init||v<best){best=v;init=true;}
  }
  return best;
}
Cluster canon_hcp(Cluster const& c) {
  Cluster best; bool init=false;
  for(int r=0;r<3;r++)for(int s=0;s<2;s++)for(int h=0;h<2;h++)for(int t=0;t<2;t++){
    Cluster v; v.reserve(c.size()); for(auto p:c)v.push_back(hcp_apply(p,r,s,h,t));
    int mi=numeric_limits<int>::max(),mj=mi,mk=mi;
    for(auto p:v){mi=min(mi,p.x);mj=min(mj,p.y);mk=min(mk,p.z);}
    int tz = (mk % 2 == 0) ? mk : mk - 1;
    for(auto& p:v){p.x-=mi;p.y-=mj;p.z-=tz;}
    sort(v.begin(),v.end()); if(!init||v<best){best=v;init=true;}
  }
  return best;
}

int internal_edges(Cluster const& c,bool hcp){
  unordered_set<P,PH> S(c.begin(),c.end()); long long d=0;
  for(auto p:c) for(auto q:(hcp?hcp_neighbors(p):fcc_neighbors(p))) d+=S.count(q);
  return (int)(d/2);
}
int direct_cut(Cluster const& c,bool hcp){
  unordered_set<P,PH> S(c.begin(),c.end()); int d=0;
  for(auto p:c) for(auto q:(hcp?hcp_neighbors(p):fcc_neighbors(p))) d+=!S.count(q);
  return d;
}

template<class Canon>
unordered_set<Cluster,CH> extend(unordered_set<Cluster,CH> const& cur,bool hcp,Canon canon){
  unordered_set<Cluster,CH> nxt; nxt.reserve(cur.size()*8);
  for(auto const& c:cur){
    unordered_set<P,PH> S(c.begin(),c.end()),F;
    for(auto p:c) for(auto q:(hcp?hcp_neighbors(p):fcc_neighbors(p))) if(!S.count(q))F.insert(q);
    for(auto x:F){Cluster a=c;a.push_back(x);sort(a.begin(),a.end());nxt.insert(canon(a));}
  }
  return nxt;
}

void init_fcc(){
  for(int zero=0;zero<3;zero++){
    vector<int> inds;for(int i=0;i<3;i++)if(i!=zero)inds.push_back(i);
    for(int a:{-1,1})for(int b:{-1,1}){int v[3]={0,0,0};v[inds[0]]=a;v[inds[1]]=b;fdirs.push_back({v[0],v[1],v[2]});}
  }
  array<int,3> per={0,1,2};
  do{for(int a:{-1,1})for(int b:{-1,1})for(int d:{-1,1})fops.push_back({per[0],per[1],per[2],a,b,d});}while(next_permutation(per.begin(),per.end()));
}

int main(int argc,char** argv){
  init_fcc(); bool hcp=argc>1 && string(argv[1])=="hcp"; int nmax=argc>2?stoi(argv[2]):8;
  unordered_set<Cluster,CH> cur; Cluster seed={{0,0,0}}; cur.insert(hcp?canon_hcp(seed):canon_fcc(seed));
  cout << "world,n,count,S_min,S_max,minimizer_count\n";
  for(int n=1;n<=nmax;n++){
    int smin=numeric_limits<int>::max(),smax=0,mincnt=0;
    for(auto const& c:cur){
      int E=internal_edges(c,hcp),S=12*n-2*E;
      if(direct_cut(c,hcp)!=S){cerr<<"cut/handshake mismatch\n";return 2;}
      if(S<smin){smin=S;mincnt=1;}else if(S==smin)mincnt++;
      smax=max(smax,S);
    }
    cout<<(hcp?"hcp":"fcc")<<","<<n<<","<<cur.size()<<","<<smin<<","<<smax<<","<<mincnt<<"\n";
    if(n==nmax)break;
    cur=hcp?extend(cur,true,canon_hcp):extend(cur,false,canon_fcc);
  }
}
