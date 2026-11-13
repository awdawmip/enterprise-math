#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#include <gmpxx.h>

using Z = mpz_class;
using U = std::uint64_t;
constexpr U prime=(U{1}<<61)-1;
constexpr int bits=192;
constexpr int key_limit=120000;
constexpr int scan_limit=180;
const Z grid=Z(1)<<bits;
U add(U a,U b){U s=a+b;return s>=prime?s-prime:s;}
U sub(U a,U b){return a>=b?a-b:a+prime-b;}
U mul(U a,U b){__uint128_t s=__uint128_t(a)*b;return add(U(s)&prime,U(s>>61));}
U inv(U a){if(!a)throw std::runtime_error("zero modular denominator");U ans=1;for(U e=prime-2;e;e>>=1){if(e&1)ans=mul(ans,a);a=mul(a,a);}return ans;}
U mod(const Z& x){return mpz_fdiv_ui(x.get_mpz_t(),prime);}
Z down(const Z&a,const Z&b){Z x;mpz_fdiv_q(x.get_mpz_t(),a.get_mpz_t(),b.get_mpz_t());return x;}
Z up(const Z&a,const Z&b){Z x;mpz_cdiv_q(x.get_mpz_t(),a.get_mpz_t(),b.get_mpz_t());return x;}
struct Span{Z lo,hi;};
struct Matrix{Z a,b,h,d;bool up;};
struct Edge{Matrix M;Span span;};
struct Cell{std::vector<Edge> edges;Span span;std::vector<U> sigs;std::array<mpq_class,3> terminal;U bound=0;};
struct Stats{U split=0,modular=0,scanned=0,exact=0;};
// table[r][c] represents the exact three tail columns at depth zero;
// higher cells carry a certified enclosure and optionally their full finite-field image.
std::vector<std::vector<Cell>> table;
Span image(const Matrix& m,const Span& s){
 const Z& l=m.up?s.lo:s.hi;const Z& h=m.up?s.hi:s.lo;
 return {down((m.a*l+m.b*grid)*grid,m.h*l+m.d*grid),up((m.a*h+m.b*grid)*grid,m.h*h+m.d*grid)};
}
// Equality of the competing projective values is the vanishing of
// A*x*y+B*x+C*y+D on local, unnormalised rational x,y.
struct Equation{Z A,B,C,D;bool xup,yup;};
Equation root(const Matrix& m,const Matrix& n){
 return {m.a*n.h-m.h*n.a,m.a*n.d-m.h*n.b,m.b*n.h-m.d*n.a,m.b*n.d-m.d*n.b,m.up,n.up};
}
Equation left_child(const Equation& q,const Matrix& m){
 return {q.A*m.a+q.C*m.h,q.B*m.a+q.D*m.h,q.A*m.b+q.C*m.d,q.B*m.b+q.D*m.d,q.xup==m.up,q.yup};
}
Equation swap_sides(const Equation& q){return {-q.A,-q.C,-q.B,-q.D,q.yup,q.xup};}
Z corner(const Equation&q,const Z&x,const Z&y){return (q.A*y+q.B*grid)*x+(q.C*y+q.D*grid)*grid;}
struct Slice{Z A,B,C,D;bool xup;};
Slice slice(const Equation&q,const Span& s){
 const Z &yl=q.yup?s.lo:s.hi,&yh=q.yup?s.hi:s.lo;
 return {q.A*yh+q.B*grid,(q.C*yh+q.D*grid)*grid,q.A*yl+q.B*grid,(q.C*yl+q.D*grid)*grid,q.xup};
}
// Denominators of both original real maps are strictly positive. The corner
// signs below test the minimum/maximum of M(x)-N(y), not the extrema of Q.
bool separated(const Slice&s,const Span& x){
 const Z& l=s.xup?x.lo:x.hi; const Z& h=s.xup?x.hi:x.lo;
 return (s.A*l+s.B>0)||(s.C*h+s.D<0);
}
struct ModularEquation{U A,B,C,D;};
bool hit(const ModularEquation&q,const std::vector<U>& small,const std::vector<U>& large,Stats& s){
 // Solve the bilinear equation for y for every candidate x with one batch inversion.
 std::vector<U> numer(small.size()),den(small.size()),products(small.size()+1,1);
 for(size_t i=0;i<small.size();++i){
  U x=small[i],n=add(mul(q.B,x),q.D),d=add(mul(q.A,x),q.C);
  if(d==0&&n==0)return true;
  numer[i]=n;den[i]=d;
  products[i+1]=mul(products[i],d?d:1);
 }
 U acc=inv(products.back());
 for(size_t i=small.size();i-->0;){
  ++s.scanned;
  if(!den[i])continue;
  U y=sub(0,mul(numer[i],mul(products[i],acc)));
  if(std::binary_search(large.begin(),large.end(),y))return true;
  acc=mul(acc,den[i]);
 }
 return false;
}
bool exact_hit(const Equation&q,const Cell& x,const Cell& y){
 for(const auto& a:x.terminal) for(const auto& b:y.terminal)
  if(q.A*a*b+q.B*a+q.C*b+q.D==0)return true;
 return false;
}
void search(int rx,int cx,int ry,int cy,const Equation& q,Stats&s){
 const auto& x=table[rx][cx];const auto& y=table[ry][cy];
 auto cut=slice(q,y.span);
 if(separated(cut,x.span))return;
 if(!x.sigs.empty()&&!y.sigs.empty()&&std::min(x.sigs.size(),y.sigs.size())<=scan_limit){
  auto a=mod(q.A),b=mod(q.B),c=mod(q.C),d=mod(q.D);
  ++s.modular;
  bool potential=x.sigs.size()<=y.sigs.size()?hit({a,b,c,d},x.sigs,y.sigs,s):hit({a,c,b,d},y.sigs,x.sigs,s);
  if(!potential)return;
 }
 if(!rx&&!ry){
  ++s.exact;
  if(exact_hit(q,x,y))throw std::runtime_error("A pair of different words shares a true column ratio");
  return;
 }
 // Splitting the wider image first only changes order and runtime. Compare
 // matched endpoints via Q, so neither prefix needs numerical normalisation.
 bool choose_y=!rx;
 if(rx&&ry){
  const Z& xl=q.xup?x.span.lo:x.span.hi; const Z& xh=q.xup?x.span.hi:x.span.lo;
  const Z& yl=q.yup?y.span.lo:y.span.hi; const Z& yh=q.yup?y.span.hi:y.span.lo;
  Z low=corner(q,xl,yl),high=corner(q,xh,yh);
  if(low>=0&&high<=0)choose_y=true;
  else if(!(low<=0&&high>=0))choose_y=high<low;
 }
 ++s.split;
 if(choose_y){
  auto rev=swap_sides(q);auto other=slice(rev,x.span);
  for(size_t m=0;m<y.edges.size();++m){const auto&e=y.edges[m];if(!separated(other,e.span))search(ry-1,cy-int(m),rx,cx,left_child(rev,e.M),s);}
 }else{
  for(size_t m=0;m<x.edges.size();++m){const auto&e=x.edges[m];if(!separated(cut,e.span))search(rx-1,cx-int(m),ry,cy,left_child(q,e.M),s);}
 }
}
U rational_mod(const mpq_class& z){return mul(mod(z.get_num()),inv(mod(z.get_den())));}
void init(int R,int C){
 table.resize(R+1,std::vector<Cell>(C+1));
 for(int r=0;r<=R;r++)for(int c=2;c<=C;c++){
  auto& n=table[r][c];
  if(!r){
   for(auto& z:n.terminal){std::cin>>z;n.sigs.push_back(rational_mod(z));}
   auto [lo,hi]=std::minmax_element(n.terminal.begin(),n.terminal.end());
   n.span={down(lo->get_num()*grid,lo->get_den()),up(hi->get_num()*grid,hi->get_den())};n.bound=3;
  }else{
   n.bound=0;
   for(int v=2;v<=c;v++)n.bound=std::min<U>(key_limit+1,n.bound+table[r-1][v].bound);
   for(int m=0;m<=c-2;m++){
    Matrix M; std::cin>>M.a>>M.b>>M.h>>M.d;Z det=M.a*M.d-M.b*M.h;
    if(!std::cin||det==0)throw std::runtime_error("invalid likelihood matrix");
    M.up=det>0; const auto& ch=table[r-1][c-m]; auto s=image(M,ch.span);
    if(m==0)n.span=s;else{n.span.lo=std::min(n.span.lo,s.lo);n.span.hi=std::max(n.span.hi,s.hi);}
    if(n.bound<=key_limit){
     U a=mod(M.a),b=mod(M.b),h=mod(M.h),d=mod(M.d);std::vector<U> den,nums,products(1,1);
     for(U z:ch.sigs){U y=add(mul(h,z),d);den.push_back(y);nums.push_back(add(mul(a,z),b));products.push_back(mul(products.back(),y));}
     U acc=inv(products.back());
     for(size_t i=den.size();i-->0;){n.sigs.push_back(mul(nums[i],mul(acc,products[i])));acc=mul(acc,den[i]);}
    }
    n.edges.push_back({std::move(M),std::move(s)});
   }
  }
  std::sort(n.sigs.begin(),n.sigs.end());n.sigs.erase(std::unique(n.sigs.begin(),n.sigs.end()),n.sigs.end());
 }
}
void controls() {
 // A true prescribed meeting must survive both corner pruning and modular inversion.
 Stats stats;
 for (int a=1;a<=9;++a) for (int b=1;b<=9;++b) {
  const bool inc=a%2;
  // Increasing x and y or decreasing x and y; equality at (a,b).
  Equation q{0,inc?b:-b,inc?-a:a,0,inc,inc};
  Span x{a*grid-1,a*grid+1}, y{b*grid-1,b*grid+1};
  if(separated(slice(q,y),x)) throw std::runtime_error("planted interval rejected");
  if(!hit({mod(q.A),mod(q.B),mod(q.C),mod(q.D)}, {U(a)}, {U(b)},stats))throw std::runtime_error("planted modular point rejected");
 }
 // Local modular equation y*x+y-2*x-2=(x+1)(y-2), zero coefficient branch.
 if(!hit({1,prime-2,1,prime-2},{prime-1},{3},stats))throw std::runtime_error("all-y solution rejected");
 if(hit({1,0,1,1},{prime-1},{3},stats))throw std::runtime_error("impossible denominator accepted");
}
int main(){
 controls();
 int R,C;
 if(!(std::cin>>R>>C) || R<1 || C<3 || R>C-2)return 3;
 init(R,C);
 int r,c;
 while(std::cin>>r>>c){
  Stats s;const auto& roots=table[r][c].edges;
  for(int m=0;m<=c-2;m++)for(int n=0;n<m;n++)search(r-1,c-m,r-1,c-n,root(roots[m].M,roots[n].M),s);
  std::cout<<r<<" "<<c<<" "<<s.split<<" "<<s.modular<<" "<<s.scanned<<" "<<s.exact<<std::endl;
 }
}
