// PREFIX912: 12x12 opposite-parity multiplier square, exact new symmetric collision classes.
// Independent of formal shared-X6 claim; C911 certified baseline from frozen BRC auxiliary model.
// g++ -std=c++17 -O3 -Wall -Wextra -pedantic PREFIX912_R6_MIXED_12X12_CENSUS.cpp -o prefix912 && ./prefix912
#include <bits/stdc++.h>
using namespace std;
using I=long long; using U=uint64_t;
constexpr int L=262145,H=524287,Q=131072;
constexpr I N=1LL<<32, T=33*N;
U enc(int a,int b){return U((a-L)/2)*Q+U((b-L)/2);}
U tr(U z){return U(z%Q)*Q+z/Q;}
U canon(U z){return min(z,tr(z));}
int aa(U z){return L+2*int(z/Q);}
int bb(U z){return L+2*int(z%Q);}
unordered_set<int> gaps,base,mid,hi, special,panels,d907,d908;
void init(){
 for(int h=1;h<18;++h)base.insert(1<<h);
 for(int i=2;i<18;++i)for(int j=1;j<i;++j){base.insert((1<<i)+(1<<j));base.insert((1<<i)-(1<<j));}
 for(int m=3;m<8192;m+=2)for(int i=2;i<18;++i)for(int j=1;j<i;++j)
 for(int v:{(1<<i)+(1<<j),(1<<i)-(1<<j)})if(v%m==0){int d=v/m;if(d>0&&d<=H-L&&d%2==0&&!base.count(d))mid.insert(d);}
 for(int m=1;m<8192;m+=2)for(int i=18;i<31;++i)for(int j=1;j<18;++j)
 for(I v:{(1LL<<i)+(1LL<<j),(1LL<<i)-(1LL<<j)})if(v%m==0){I d=v/m;if(d>0&&d<=H-L&&d%2==0&&!base.count(int(d))&&!mid.count(int(d)))hi.insert(int(d));}
 gaps=base;gaps.insert(mid.begin(),mid.end());gaps.insert(hi.begin(),hi.end());
 for(int q:{262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285})special.insert(q);
 for(int q=400011;q<400522;q+=2)special.insert(q);
 for(int q=480011;q<480522;q+=2)special.insert(q);
 for(int q=L;q<=H;q+=2)for(int h=1;h<32;++h)
 if(((1LL<<h)-1)%q==0||((1LL<<h)+1)%q==0){special.insert(q);break;}
 for(int j=0;j<64;++j)for(int z:{1,3,5})panels.insert(510000+z+194*j);
 for(int i=18;i<23;++i)for(int j=1;j<18;++j)for(int s:{-1,1})d907.insert((1<<i)+s*(1<<j));
 for(int i=1;i<20;++i)for(int s:{-1,1})d908.insert((1<<i)+s);
 if(tuple(base.size(),mid.size(),hi.size(),special.size(),panels.size(),d907.size(),d908.size())!=tuple<size_t,size_t,size_t,size_t,size_t,size_t,size_t>(258,276,857,552,192,169,37))throw runtime_error("old family counts regression");
}
bool covered(int a,int b){return I(a)*b<T||special.count(a)||special.count(b)||I(a/gcd(a,b))*b<N
  ||33*((N+a-1)/a)>b||33*((N+b-1)/b)>a||panels.count(a)||panels.count(b)
  ||gaps.count(abs(a-b))||d907.count(3*a-b)||d907.count(3*b-a)
  ||d908.count(2*a-b)||d908.count(2*b-a);}
struct Stat {I witness=0; U novel_unique=0; U raw_unique=0;};
int inverse_mod(int a,int m){
 if(m==1)return 0;
 int u=1,v=0,b=m,aa=a;
 while(b){int q=aa/b,t=aa-q*b;aa=b;b=t;t=u-q*v;u=v;v=t;}
 if(aa!=1)throw runtime_error("inverse does not exist");
 return (u%m+m)%m;
}
int mod_pos(long long n,int m){return int((n%m+m)%m);}
template<class F> Stat family(int k,int ell,F accept){
 unordered_set<U> raw; raw.reserve(150000);
 Stat st;
 const int g=gcd(k,ell),step=ell/g,inv=inverse_mod(k/g,step);
 for(int i=1;i<=22;++i)for(int s:{-1,1}){
  const int d=(1<<i)+s;
  const long long rhs=I(d)+ell-I(k)*L;
  if(rhs%(2*g))continue;
  const int t0=step==1?0:mod_pos(rhs/(2*g)*inv,step);
  for(int t=t0;t<Q;t+=step){
   const int a=L+2*t;
   const int num=k*a-d;
   if(num%ell)abort();
   const int b=num/ell;
   if(b<L||b>H)continue;
   if((b&1)==0)abort();
   const int x=(s==1)?(1-k%2):k%2;
   const int y=x+k*a;
   if(!(x>=0&&x<N&&y>=0&&y<N&&x+(1<<i)<N&&y-s>=0&&y-s<N
       &&((x^(1<<i))==(x+(1<<i)))&&((y^1)==y-s)
       &&y-x==k*a&&(y-s)-(x+(1<<i))==ell*b
       &&(y-x)%a==0&&((y-s)-(x+(1<<i)))%b==0)){
      cerr<<"INVALID "<<k<<" "<<ell<<" "<<a<<" "<<b<<" "<<i<<" "<<s<<"\n";abort();
   }
   ++st.witness;
   U z=enc(a,b);
   if(raw.insert(z).second)accept(z);
  }
 }
 st.raw_unique=raw.size();
 return st;
}
// Independent enumeration: solve for the second-port modulus b first.
// The congruence ell*(L+2t)+d == k (mod 2*k) forces odd a.
template<class F> Stat family_via_b(int k,int ell,F accept){
 unordered_set<U> raw; raw.reserve(150000);
 Stat st;
 const int g=gcd(k,ell),step=k/g,inv=inverse_mod(ell/g,step);
 for(int i=1;i<=22;++i)for(int s:{-1,1}){
  const int d=(1<<i)+s;
  const long long rhs=I(k)-I(ell)*L-d;
  if(rhs%(2*g))continue;
  const int t0=step==1?0:mod_pos(rhs/(2*g)*inv,step);
  for(int t=t0;t<Q;t+=step){
   int b=L+2*t;
   int num=ell*b+d;
   if(num%k)abort();
   int a=num/k;
   if(a<L||a>H)continue;
   if(!(a&1))abort();
   int x=(s==1)?(1-k%2):k%2,y=x+k*a;
   if(!((x^(1<<i))==(x+(1<<i))&&(y^1)==y-s && y>=0 && y-s<N && y<N &&
      y-x==k*a && (y-s)-(x+(1<<i))==ell*b))abort();
   ++st.witness;
   U z=enc(a,b);
   if(raw.insert(z).second)accept(z);
  }
 }
 st.raw_unique=raw.size();
 return st;
}
int main(){
 ios::sync_with_stdio(false);init();
 unordered_set<U> known;known.reserve(7000000);
 unordered_set<U> r909; r909.reserve(2300000);
 for(auto [k,l]:vector<pair<int,int>>{{3,2},{4,1},{4,3}})family(k,l,[&](U z){r909.insert(z);});
 if(r909.size()!=1900472)throw runtime_error("909 raw regression");
 for(U z:r909){known.insert(canon(z));}r909.clear();r909.rehash(0);
 cerr<<"KNOWN_909 "<<known.size()<<"\n";
 unordered_set<U> fresh910;fresh910.reserve(2000000);
 for(auto [k,l]:vector<pair<int,int>>{{5,2},{5,4},{6,1},{6,5},{7,2},{7,4},{7,6},{8,1},{8,3},{8,5},{8,7}}){
  family(k,l,[&](U z){U c=canon(z);if(!known.count(c)&&!covered(aa(z),bb(z)))fresh910.insert(c);});
 }
 if(fresh910.size()!=1785728){cerr<<"ERROR 910 canonical new "<<fresh910.size()<<"\n";return 4;}
 for(U z:fresh910){known.insert(z);}fresh910.clear();fresh910.rehash(0);
 cerr<<"KNOWN_910 "<<known.size()<<"\n";
 unordered_set<U> fresh911;fresh911.reserve(1800000);
 for(int k=9;k<=12;k++)for(int l=1;l<k;l++)if(((k-l)&1)&&gcd(k,l)==1){
  family(k,l,[&](U z){U c=canon(z);if(!known.count(c)&&!covered(aa(z),bb(z)))fresh911.insert(c);});
 }
 if(fresh911.size()!=1562198){cerr<<"ERROR 911 canonical new "<<fresh911.size()<<"\n";return 5;}
 for(U z:fresh911){known.insert(z);}fresh911.clear();fresh911.rehash(0);
 cerr<<"KNOWN_911 "<<known.size()<<"\n";
 unordered_set<U> fresh; fresh.reserve(8000000);
 vector<tuple<int,int,I,U,U>> fam_rows;
 I witnesses=0,raw_total=0;int families=0;
 for(int k=1;k<=12;k++)for(int l=1;l<=12;l++){
  if(((k-l)&1)==0)continue;
  // Exclude all channels that have been certified in PREFIX909/910/911.
  if(k>l && gcd(k,l)==1 && k<=12)continue;
  U before=fresh.size();
  auto st=family(k,l,[&](U z){U c=canon(z);if(!known.count(c)&&!covered(aa(z),bb(z)))fresh.insert(c);});
  ++families;witnesses+=st.witness;raw_total+=st.raw_unique;
  fam_rows.emplace_back(k,l,st.witness,st.raw_unique,fresh.size()-before);
  cout<<"FAMILY "<<k<<" "<<l<<" "<<st.witness<<" "<<st.raw_unique<<" "<<fresh.size()-before<<"\n" <<flush;
 }
 U delta=2ULL*fresh.size();
 U current=7787364838ULL+delta;
 cout<<"TOTAL "<<families<<" "<<witnesses<<" "<<raw_total<<" "<<fresh.size()<<" "<<delta<<" "<<current<<" "<<U(Q)*Q-current<<"\n";
 // Complete independent b-first recount with set-equality check.
 unordered_set<U> alternative;alternative.reserve(fresh.size()+10000);
 size_t idx_row=0;
 for(int k=1;k<=12;k++)for(int l=1;l<=12;l++){
  if(((k-l)&1)==0)continue;
  if(k>l && gcd(k,l)==1 && k<=12)continue;
  auto [rk,rl,w,u,d]=fam_rows.at(idx_row++);
  if(rk!=k||rl!=l)abort();
  auto st=family_via_b(k,l,[&](U z){U c=canon(z);if(!known.count(c)&&!covered(aa(z),bb(z)))alternative.insert(c);});
  cerr<<"B_FIRST "<<k<<" "<<l<<" witnesses="<<st.witness<<" seen="<<alternative.size()<<"\n"<<flush;
  if(st.witness!=w||st.raw_unique!=u){
   cerr<<"B_FIRST_MISMATCH "<<k<<" "<<l<<" "<<st.witness<<" "<<st.raw_unique<<" expected "<<w<<" "<<u<<"\n";return 7;
  }
 }
 if(alternative.size()!=fresh.size()){
  cerr<<"B_FIRST_UNION_COUNT_MISMATCH "<<alternative.size()<<" "<<fresh.size()<<"\n";return 8;
 }
 for(U z:alternative)if(!fresh.count(z)){cerr<<"B_FIRST_MEMBERSHIP_MISMATCH "<<z<<"\n";return 9;}
 cout<<"INDEPENDENT_B_FIRST_PASS "<<idx_row<<" "<<alternative.size()<<" exact canonical pair IDs\n";
 U smallest=*min_element(fresh.begin(),fresh.end());
 cout<<"FIRST_NOVEL "<<aa(smallest)<<" "<<bb(smallest)<<"\n";
 // Row hash: ordered (k,l,witness,raw_unique,new canonical first hit) transcript is stable.
 return 0;
}
