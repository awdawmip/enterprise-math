// C71 modular certificate: two visible 23 blocks, original preparation line.
// Outputs a verified injective set of sums of the two extreme terminal ratios
// mod p, for each selected c. Equality of the exact two H observations forces
// equality of this sum. Mod p collisions would only require extra proof.
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using u64=uint64_t;
using u128=__uint128_t;
constexpr u64 P=(1ULL<<61)-1;
inline u64 add(u64 a,u64 b){u64 c=a+b;return c>=P?c-P:c;}
inline u64 sub(u64 a,u64 b){return a>=b?a-b:P+a-b;}
inline u64 mul(u64 a,u64 b){u128 t=(u128)a*b;u64 x=(u64)(t>>61)+(u64)(t&P);x=(x>>61)+(x&P);return x>=P?x-P:x;}
u64 power(u64 a,u64 e){u64 r=1;while(e){if(e&1)r=mul(r,a);a=mul(a,a);e>>=1;}return r;}
struct Mat {u64 a,b,h,d;};
Mat mm(Mat x,Mat y){return {add(mul(x.a,y.a),mul(x.b,y.h)),add(mul(x.a,y.b),mul(x.b,y.d)),add(mul(x.h,y.a),mul(x.d,y.h)),add(mul(x.h,y.b),mul(x.d,y.d))};}
struct Pair {u64 n,d;};
struct WData {u64 low,high;};
std::vector<u64> batch_inv_small(int n){
 std::vector<u64> inv(n+1);inv[1]=1;
 for(int i=2;i<=n;i++)inv[i]=mul(sub(0,P/i),inv[P%i]);
 return inv;
}
std::vector<WData> terminal(int maxc){
 auto inv=batch_inv_small(10*maxc+500);
 auto fraction=[&](u64 n,u64 d){return mul(n, inv[d]);};
 const u64 a[]={mul(3,inv[32]),fraction(3,2),6};
 const u64 b[]={fraction(15,32),fraction(15,8),3};
 std::vector<WData> R(maxc+1);u64 y=1;
 for(int w=2;w<=maxc;++w){
  if(w>=3)y=mul(y,mul(w*4+1,inv[w*4+4]));
  u64 x=mul(840,mul(inv[w+2],mul(inv[w+3],inv[w+4])));
  u64 vals[3];
  for(int j=0;j<3;j++){
   u64 num=add(mul(x,a[j]),b[j]);
   u64 den=add(1,mul(mul(x,y),a[j]));
   if(!den){std::cerr<<"zero terminal denominator: w="<<w<<"\n";std::exit(3);}
   vals[j]=mul(mul(y,num),power(den,P-2));
  }
  R[w]={vals[0],vals[w<=3?1:2]};
 }
 return R;
}
struct Rat{u64 n,d;};
int main(int argc,char**argv){
 if(argc<3){std::cerr<<"Usage: cert first_c last_c\n";return 1;}
 int first=std::atoi(argv[1]),last=std::atoi(argv[2]);
 if(first<2||last<first||last>10000){std::cerr<<"invalid range\n";return 1;}
 auto term=terminal(last);
 std::vector<Mat> first_edges(last+1);
 std::vector<Rat> ratios;
 std::vector<u64> prefix, keys;
 for(int c=first;c<=last;c++){
  u64 A1=1,B1=1,E1p=1, pow4=1;
  for(int v=c;v>=2;v--){
   A1=mul(A1,5+4*v);B1=mul(B1,5+v);E1p=mul(E1p,20+v);
   u64 E1=mul(4+v,E1p);u64 t1=mul(mul(28,4+4*v),mul(A1,B1));
   first_edges[v]={t1,mul(A1,E1),t1,mul(pow4,mul(E1,B1))};
   pow4=mul(pow4,4);
  }
  size_t N=(size_t)c*(c-1)/2;
  ratios.clear();ratios.reserve(N);
  for(int v=2;v<=c;v++){
   u64 A2=1,B2=1,E2p=1,pow4_2=1;
   for(int w=v;w>=2;w--){
    A2=mul(A2,3+4*w);B2=mul(B2,3+w);E2p=mul(E2p,12+w);
    u64 E2=mul(2+w,E2p);u64 t2=mul(mul(28,2+4*w),mul(A2,B2));
    Mat M2={t2,mul(A2,E2),t2,mul(pow4_2,mul(E2,B2))};
    Mat M=mm(first_edges[v],M2);
    auto e=term[w];
    u64 n0=add(mul(M.a,e.low),M.b), d0=add(mul(M.h,e.low),M.d);
    u64 n1=add(mul(M.a,e.high),M.b),d1=add(mul(M.h,e.high),M.d);
    u64 n=add(mul(n0,d1),mul(n1,d0)),d=mul(d0,d1);
    if(!d){std::cerr<<"zero rational denominator c="<<c<<" v="<<v<<" w="<<w<<"\n";return 4;}
    ratios.push_back({n,d});
    pow4_2=mul(pow4_2,4);
   }
  }
  if(ratios.size()!=N){std::cerr<<"wrong count\n";return 5;}
  prefix.resize(N+1);prefix[0]=1;
  for(size_t i=0;i<N;i++)prefix[i+1]=mul(prefix[i],ratios[i].d);
  if(!prefix[N]){std::cerr<<"batch zero denominator\n";return 6;}
  keys.resize(N);u64 cur=power(prefix[N],P-2);
  for(size_t i=N;i-->0;){keys[i]=mul(ratios[i].n,mul(cur,prefix[i]));cur=mul(cur,ratios[i].d);}
  if(cur!=1){std::cerr<<"batch inversion failed\n";return 7;}
  std::sort(keys.begin(),keys.end());
  size_t collisions=0;
  for(size_t i=1;i<N;i++)if(keys[i]==keys[i-1])collisions++;
  std::cout<<"c="<<c<<" words="<<N<<" duplicate_mod_endpoint_sums="<<collisions<<" min_residue="<<keys.front()<<" max_residue="<<keys.back()<<"\n";
  if(collisions)return 8;
 }
}
