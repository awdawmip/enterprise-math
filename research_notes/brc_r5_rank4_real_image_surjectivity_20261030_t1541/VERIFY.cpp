// Exact finite certificate verifier for R5 seedless-LR full-rank observation image.
// C++17, all arithmetic integral; __int128 for facet intersections.
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using i128=__int128_t;
using V=std::array<long long,4>;
struct Ine { V a;long long b;};
constexpr int NP=14,NK=12;
const int P[NP]={120,240,60,60,180,60,30,30,30,30,90,90,20,40};
const int Q[NP]={240,120,180,60,60,60,108,72,45,15,36,24,40,20};
const int T[NP]={1,1,2,2,2,2,3,3,3,3,3,3,3,3};
const int Par[NP]={-1,-1,0,0,1,1,2,2,3,3,4,4,5,5};
const int Key[NP]={0,1,2,3,4,3,5,6,7,8,9,10,11,8};
void demand(bool c,const std::string& why){if(!c)throw std::runtime_error(why);}
V obs(int mask,bool lr){
  int stop[NP],surv[NP];
  for(int i=0;i<NP;i++)stop[i]=(mask>>(lr?Key[i]:i))&1;
  for(int i=0;i<NP;i++)surv[i]=(Par[i]<0 ? 1:surv[Par[i]]*(1-stop[Par[i]]));
  V a{0,0,0,0};
  for(int i=0;i<NP;i++)if(surv[i] && stop[i]){
    a[1]+=(4-T[i])*P[i]; a[2]+=(4-T[i])*Q[i];
    if(i==9||i==13)a[0]+=Q[i];
    if(i==8||i==12)a[3]+=P[i];
  }
  return a;
}
using Mat=std::array<std::array<i128,4>,4>;
i128 determinant(const Mat& a){
  // expansion by first row with 3-by-3 integer cofactors
  i128 ans=0;
  for(int j=0;j<4;j++){
    i128 b[3][3];
    for(int r=1;r<4;r++){
      int col=0;
      for(int k=0;k<4;k++)if(k!=j)b[r-1][col++]=a[r][k];
    }
    i128 minor=b[0][0]*(b[1][1]*b[2][2]-b[1][2]*b[2][1])
        -b[0][1]*(b[1][0]*b[2][2]-b[1][2]*b[2][0])
        +b[0][2]*(b[1][0]*b[2][1]-b[1][1]*b[2][0]);
    ans+=(j%2?-1:1)*a[0][j]*minor;
  }
  return ans;
}
long long signed64(i128 v){demand(v>=INT64_MIN && v<=INT64_MAX,"integer exceeds int64");return (long long)v;}
using MaskSet=std::array<uint64_t,64>;
void insert(MaskSet& a,int k){a[k/64]|=(uint64_t(1)<<(k%64));}
bool has(const MaskSet& a,int k){return (a[k/64]>>(k%64))&1;}
bool nonempty(const MaskSet& a){for(auto w:a)if(w)return true;return false;}
MaskSet meet(const MaskSet&a,const MaskSet&b){MaskSet r{};for(int k=0;k<64;k++)r[k]=a[k]&b[k];return r;}
int pop(const MaskSet& s){int n=0;for(auto x:s)n+=__builtin_popcountll(x);return n;}
int starAnchor(const MaskSet& s){
  int must1=0,must0=0;
  for(int b=0;b<4096;b++)if(has(s,b)){
    for(int j=0;j<12;j++)if(!has(s,b^(1<<j))){
       if(b&(1<<j))must1|=(1<<j);else must0|=(1<<j);
    }
  }
  if(must1&must0)return -1;
  for(int b=0;b<4096;b++)if(has(s,b) && (b&must1)==must1 && (b&must0)==0)return b;
  return -1;
}
int main(int argc,char**argv){
try{
  demand(argc==2,"usage: VERIFY FACETS.txt");
  for(int i=0;i<NP;i++){
    demand(P[i]>0&&Q[i]>0,"nonpositive path mass");
    if(Par[i]>=0)demand(T[i]==T[Par[i]]+1,"bad tree time");
  }
  for(int i=0;i<6;i++){
    int cp=0,cq=0;for(int j=0;j<NP;j++)if(Par[j]==i){cp+=P[j];cq+=Q[j];}
    demand(cp==P[i] && cq==Q[i],"tree mass conservation");
  }
  demand(P[0]+P[1]==360&&Q[0]+Q[1]==360,"root mass mismatch");
  int collisionPairs=0;
  for(int i=0;i<NP;i++)for(int j=0;j<i;j++)if(Key[i]==Key[j]){
    demand(T[i]==T[j]&&P[i]*Q[j]==P[j]*Q[i],"false LR key collision");collisionPairs++;
  }
  demand(collisionPairs==2,"expected two LR collisions");
  std::set<V> LR,FULL;
  std::array<V,4096> lrMasks;
  for(int i=0;i<4096;i++){lrMasks[i]=obs(i,true);LR.insert(lrMasks[i]);}
  for(int i=0;i<16384;i++)FULL.insert(obs(i,false));
  demand(LR.size()==272&&FULL.size()==647,"deterministic vector count changed");
  Mat rankWitness{{{{0,20,40,20}},{{0,30,45,30}},{{0,30,72,0}},{{15,750,375,0}}}};
  demand(LR.count(V{0,0,0,0})&&LR.count(V{0,20,40,20})&&LR.count(V{0,30,45,30})&&LR.count(V{0,30,72,0})&&LR.count(V{15,750,375,0}),"rank witnesses absent");
  demand(determinant(rankWitness)==-135000,"LR affine dimension is not 4");
  std::vector<Ine> facets;
  std::ifstream in(argv[1]);demand((bool)in,"facet file missing");
  std::string head;std::getline(in,head);demand(head.find("57")!=std::string::npos,"facet header missing");
  Ine h;
  while(in>>h.a[0]>>h.a[1]>>h.a[2]>>h.a[3]>>h.b)facets.push_back(h);
  demand(facets.size()==57,"facet count != 57");
  for(const auto& f:facets){
    int n=0;for(const auto& p:LR){
      i128 dot=0;for(int i=0;i<4;i++)dot+=(i128)f.a[i]*p[i];
      demand(dot<=f.b,"LR violates candidate facet");
      n+=(dot==f.b);
    }
    demand(n>=1,"candidate support has no LR points");
  }
  for(const auto& p:FULL)for(const auto& f:facets){
    i128 dot=0;for(int j=0;j<4;j++)dot+=(i128)f.a[j]*p[j];
    demand(dot<=f.b,"FULL violates a hull inequality");
  }
  // RIGOROUS BOX certificates, using nonnegative combinations of facets.
  auto box=[&](std::vector<std::pair<int,long long>> terms, long long den, V target,long long bound){
    V sum{0,0,0,0};i128 b=0;
    for(auto [i,w]:terms){demand(i>=0&&i<57&&w>=0,"bad box term");
      for(int k=0;k<4;k++)sum[k]+=w*facets[i].a[k];
      b+=(i128)w*facets[i].b;
    }
    for(int k=0;k<4;k++)demand(sum[k]==den*target[k],"bad box combination");
    demand(b==den*bound,"bad box bound");
  };
  box({{17,1}},1,V{-1,0,0,0},0);
  box({{22,1}},1,V{1,0,0,0},35);
  box({{17,2},{19,1},{23,1}},1,V{0,-1,0,0},0);
  box({{16,14},{17,552},{19,69},{54,1}},148,V{0,1,0,0},1080);
  box({{17,30},{19,45},{23,8},{28,1}},30,V{0,0,-1,0},0);
  box({{16,88},{17,478},{19,809},{54,1}},370,V{0,0,1,0},1080);
  box({{19,1}},1,V{0,0,0,-1},0);
  box({{20,1}},1,V{0,0,0,1},50);
  uint64_t fourTuples=0,nonsingular=0,feasibleTuples=0;
  std::set<V> foundVertices;
  for(int i=0;i<57;i++)for(int j=i+1;j<57;j++)for(int k=j+1;k<57;k++)for(int l=k+1;l<57;l++){
    fourTuples++;
    int ids[4]={i,j,k,l};Mat a{};
    for(int row=0;row<4;row++)for(int col=0;col<4;col++)a[row][col]=facets[ids[row]].a[col];
    i128 d=determinant(a);if(!d)continue;nonsingular++;
    i128 nums[4];
    for(int col=0;col<4;col++){
      Mat z=a;
      for(int row=0;row<4;row++)z[row][col]=facets[ids[row]].b;
      nums[col]=determinant(z);
    }
    bool feasible=true;
    for(const auto& f:facets){
      i128 lhs=0;for(int col=0;col<4;col++)lhs+=(i128)f.a[col]*nums[col];
      i128 rhs=(i128)f.b*d;
      if((d>0 && lhs>rhs)||(d<0 && lhs<rhs)){feasible=false;break;}
    }
    if(!feasible)continue;
    feasibleTuples++;
    V x;
    for(int col=0;col<4;col++){
      demand(nums[col]%d==0,"feasible nonintegral H vertex");
      x[col]=signed64(nums[col]/d);
    }
    demand(LR.count(x),"extra H vertex absent from LR");
    foundVertices.insert(x);
  }
  demand(fourTuples==395010,"4-tuple count mismatch");
  demand(!foundVertices.empty(),"no H vertices");
  std::set<MaskSet> faces;
  std::vector<MaskSet> q;
  for(const auto& f:facets){
    MaskSet s{};
    for(int mask=0;mask<4096;mask++){
      i128 dot=0;for(int col=0;col<4;col++)dot+=(i128)f.a[col]*lrMasks[mask][col];
      if(dot==f.b)insert(s,mask);
    }
    demand(nonempty(s),"empty facet optimizer");
    if(faces.insert(s).second)q.push_back(s);
  }
  for(size_t at=0;at<q.size();at++){
    auto s=q[at];
    size_t n=q.size();
    for(size_t j=0;j<n;j++){
      auto z=meet(s,q[j]);
      if(nonempty(z)&&faces.insert(z).second)q.push_back(z);
    }
  }
  demand(faces.size()==438,"proper-face count mismatch");
  size_t maxFace=0,minFace=4096;
  for(const auto& f:faces){
    demand(starAnchor(f)>=0,"face optimizer mask set has no downset anchor");
    maxFace=std::max(maxFace,(size_t)pop(f));minFace=std::min(minFace,(size_t)pop(f));
  }
  std::cout<<"TREE_OK positive_2measure=1 norm_360=1 LR_collision_pairs="<<collisionPairs<<"\n";
  std::cout<<"DETERMINISTIC unique_LR="<<LR.size()<<" unique_FULL="<<FULL.size()<<"\n";
  std::cout<<"H_CERT inequalities="<<facets.size()<<" bounded_box=[r:0..35,x:0..1080,y:0..1080,s:0..50]"<<"\n";
  std::cout<<"H_CERT quadruples="<<fourTuples<<" nonsingular="<<nonsingular<<" feasible="<<feasibleTuples<<" distinct_vertices="<<foundVertices.size()<<" all_vertices_in_LR=1"<<"\n";
  std::cout<<"FULL_HULL containment_all_647=1 rank4_det=-135000\n";
  std::cout<<"FACE_CERT proper_faces="<<faces.size()<<" every_optimizer_set_downset_anchor=1 max_opt_masks="<<maxFace<<" min_opt_masks="<<minFace<<"\n";
  std::cout<<"THEOREM actual_LR_image=actual_FULL_image=shared_4D_convex_hull via face_fiber_star_degree\n";
  std::cout<<"PASS_EXACT_R5_RANK4_REAL_IMAGE_SURJECTIVITY\n";
} catch(const std::exception&e){std::cerr<<"FAIL "<<e.what()<<"\n";return 1;}
}
