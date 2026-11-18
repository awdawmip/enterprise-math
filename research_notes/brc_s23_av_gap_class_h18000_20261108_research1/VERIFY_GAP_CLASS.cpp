// Exact integer certificate for S23/AV endpoint gap-class upper bound.
// C++17, g++ -O3 -std=c++17 -o verify VERIFY_GAP_CLASS.cpp
#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <stdexcept>
#include <tuple>
#include <vector>
using namespace std;
using i128=__int128_t;
static i128 parse128(const char* s){i128 x=0;for(;*s;++s){assert(*s>='0'&&*s<='9');x=x*10+(*s-'0');}return x;}
static const i128 Q=parse128("100000000000000000000000000");
static const i128 LO=parse128("545569623581288298975349314");
static const i128 HI=LO+1;
constexpr int64_t B=1000000000000LL;
constexpr int64_t R=5455696235812LL; // floor(r * 10^12), certified by LO/Q, HI/Q.
constexpr int N=2455069;
struct Point {int64_t key;int32_t v,j;};
struct Stats {int maxv=-1,maxj=-1,minsum=INT32_MAX;int64_t count=0;};
static bool lessp(const Point& a,const Point& b){return a.key<b.key;}
static bool valid(int K,int L,int dv,int dj,const Stats& x){return K>=x.maxj && L>=x.maxv && (int64_t)K+L<=N+x.minsum && (i128)K*Q>HI*L && (i128)(K+dj)*Q<LO*(L+dv);}
static bool actual_order(const Point& a,const Point& b) {int dv=b.v-a.v,dj=b.j-a.j;return (dv>=0?LO:HI)*dv>Q*dj;}
int main(int argc,char**argv){
 if(argc!=2){cerr<<"Usage: verify H\n";return 2;}
 int H=atoi(argv[1]);if(H<5001 || H>20000){cerr<<"invalid horizon\n";return 2;}
 auto tic=chrono::steady_clock::now();
 assert((i128)R*Q<=LO*B && HI*B<(i128)(R+1)*Q);
 int64_t M=(int64_t)(H+1)*(H+2)/2;
 vector<Point> v;v.reserve(M);
 for(int a=0;a<=H;++a)for(int b=0;b<=H-a;++b)v.push_back({R*a-B*b,a,b});
 assert((int64_t)v.size()==M);
 sort(v.begin(),v.end(),lessp);
 if(v.front().v!=0||v.front().j!=H||v.back().v!=H||v.back().j!=0){cerr<<"outer order invalid\n";return 1;}
 map<pair<int,int>,Stats> classes;
 for(int64_t i=1;i<M;++i){
   const auto &a=v[i-1],&b=v[i];
   if(!actual_order(a,b)) {cerr<<"adverse order FAILED at index "<<i<<"\n";return 1;}
   int dv=b.v-a.v, dj=b.j-a.j;
   Stats &s=classes[{dv,dj}];
   s.maxv=max(s.maxv,a.v);s.maxj=max(s.maxj,a.j);s.minsum=min(s.minsum,a.v+a.j);s.count++;
 }
 cout<<"PASS_THRESHOLD_ORDER H="<<H<<" M="<<M<<" BOUNDED="<<M-1<<" CLASSES="<<classes.size()<<"\n";
 v.clear();v.shrink_to_fit();
 int maxCertified=0;
 int64_t total=0;
 for(const auto &[delta,st]: classes){
   int dv=delta.first,dj=delta.second;
   int K=0,L=0;
   if(dv==79 && dj==431){K=2074774;L=380295;}
   else {
      bool found=false;
      for(L=st.maxv;L<st.maxv+100000;++L){
         i128 low=(LO*L)/Q, high=(HI*L)/Q;
         if(low!=high){cerr<<"fraction bound ambiguity L="<<L<<"\n";return 1;}
         K=max((int)low+1,st.maxj);
         if(valid(K,L,dv,dj,st)){found=true;break;}
      }
      if(!found){cerr<<"MISSING_CLASS_WITNESS "<<dv<<" "<<dj<<" maxv="<<st.maxv<<" maxj="<<st.maxj<<" minsum="<<st.minsum<<"\n";return 1;}
   }
   if(!valid(K,L,dv,dj,st)){cerr<<"INVALID_WITNESS "<<dv<<" "<<dj<<"\n";return 1;}
   int certLength=K+L-st.minsum; maxCertified=max(maxCertified,certLength);total+=st.count;
   cout<<"CLASS "<<dv<<" "<<dj<<" COUNT="<<st.count<<" MAXV="<<st.maxv<<" MAXJ="<<st.maxj<<" MINSUM="<<st.minsum<<" WITNESS="<<K<<","<<L<<" MAXLENGTH="<<certLength<<"\n";
 }
 if(total!=M-1){cerr<<"BAD_COUNT\n";return 1;}
 int ell=(int)((i128)H*Q/LO)+1;
 int k=(int)((i128)HI*H/Q)+1;
 if(!(LO*ell>Q*H && Q*k>HI*H && ell<=N && k<=N)){cerr<<"BAD_OUTER\n";return 1;}
 double elapsed=chrono::duration<double>(chrono::steady_clock::now()-tic).count();
 cout<<"PASS_OUTER "<<ell<<" "<<k<<"\n";
 cout<<"PASS_S23_AV_GAP_CLASS_UPPER H="<<H<<" MAX_CERTIFIED_LENGTH="<<maxCertified<<" CLASSES="<<classes.size()<<" ELAPSED_SECONDS="<<elapsed<<"\n";
}
