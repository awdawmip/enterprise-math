// PREFIX911_R6_MULTIPLIERS_9_12_EXACT.cpp
// Self-contained exact C++17 census of the PREFIX911 16 new families.
// Compile: g++ -std=c++17 -O3 FILE.cpp -o prefix911 && ./prefix911
#include <bits/stdc++.h>
using namespace std;
using I=long long; using U=uint64_t;
constexpr int L=262145,H=524287,Q=131072;
constexpr I N=1LL<<32, T=33*N;
U enc(int a,int b){return U((a-L)/2)*Q+U((b-L)/2);}
U tr(U z){return U(z%Q)*Q+z/Q;}
int aa(U z){return L+2*int(z/Q);}
int bb(U z){return L+2*int(z%Q);}
unordered_set<int> gaps,base,mid,hi,u,p,d907,d908;
void init(){
 for(int h=1;h<18;++h)base.insert(1<<h);
 for(int i=2;i<18;++i)for(int j=1;j<i;++j){
  base.insert((1<<i)+(1<<j));base.insert((1<<i)-(1<<j));
 }
 for(int m=3;m<8192;m+=2)for(int i=2;i<18;++i)for(int j=1;j<i;++j)
  for(int v:{(1<<i)+(1<<j),(1<<i)-(1<<j)})if(v%m==0){
   int d=v/m;if(d>0&&d<=H-L&&d%2==0&&!base.count(d))mid.insert(d);
  }
 for(int m=1;m<8192;m+=2)for(int i=18;i<31;++i)for(int j=1;j<18;++j)
  for(I v:{(1LL<<i)+(1LL<<j),(1LL<<i)-(1LL<<j)})if(v%m==0){
   I d=v/m;if(d>0&&d<=H-L&&d%2==0&&!base.count(int(d))&&!mid.count(int(d)))hi.insert(int(d));
  }
 gaps=base;gaps.insert(mid.begin(),mid.end());gaps.insert(hi.begin(),hi.end());
 for(int q:{262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285})u.insert(q);
 for(int q=400011;q<400522;q+=2)u.insert(q);
 for(int q=480011;q<480522;q+=2)u.insert(q);
 for(int q=L;q<=H;q+=2)for(int h=1;h<32;++h)
  if(((1LL<<h)-1)%q==0||((1LL<<h)+1)%q==0){u.insert(q);break;}
 for(int j=0;j<64;++j)for(int z:{1,3,5})p.insert(510000+z+194*j);
 for(int i=18;i<23;++i)for(int j=1;j<18;++j)for(int s:{-1,1})d907.insert((1<<i)+s*(1<<j));
 for(int i=1;i<20;++i)for(int s:{-1,1})d908.insert((1<<i)+s);
 cerr<<"BASE_COUNTS "<<base.size()<<" "<<mid.size()<<" "<<hi.size()<<" "<<u.size()<<" "<<p.size()<<" "<<d907.size()<<" "<<d908.size()<<"\n";
 if(tuple(base.size(),mid.size(),hi.size(),u.size(),p.size(),d907.size(),d908.size())!=tuple<size_t,size_t,size_t,size_t,size_t,size_t,size_t>(258,276,857,552,192,169,37))exit(2);
}
bool covered(int a,int b){
 return I(a)*b<T||u.count(a)||u.count(b)||I(a/gcd(a,b))*b<N
  ||33*((N+a-1)/a)>b||33*((N+b-1)/b)>a||p.count(a)||p.count(b)
  ||gaps.count(abs(a-b))||d907.count(3*a-b)||d907.count(3*b-a)
  ||d908.count(2*a-b)||d908.count(2*b-a);
}
struct Stats{int k,l;long long witnesses=0;unordered_set<U> vals;};
Stats enumerate(int k,int ell){
 Stats o;o.k=k;o.l=ell;
 if(gcd(k,ell)!=1||(k-ell)%2!=1||k<=ell)exit(2);
 for(int i=1;i<=22;++i)for(int s:{-1,1}){
  int d=(1<<i)+s;
  for(int a=L;a<=H;a+=2){
   int num=k*a-d;if(num%ell)continue;int b=num/ell;
   if(b<L||b>H||b%2==0)continue;
   int x=s==1?(1-k%2):(k%2),y=x+k*a;
   if(!(0<=x&&x<N&&0<=y&&y<N&&x+(1<<i)<N&&0<=y-s&&y-s<N
        &&((x^(1<<i))==x+(1<<i))&&((y^1)==y-s)
        &&y-x==k*a&&(y-s)-(x+(1<<i))==ell*b))exit(3);
   ++o.witnesses;o.vals.insert(enc(a,b));
  }
 }
 return o;
}
int main(){
 ios::sync_with_stdio(false);init();
 unordered_set<U> known;known.reserve(5500000);
 unordered_set<U> r909;
 for(auto [k,l]:vector<pair<int,int>>{{3,2},{4,1},{4,3}}){
  auto x=enumerate(k,l);r909.insert(x.vals.begin(),x.vals.end());
 }
 if(r909.size()!=1900472)exit(4);
 for(U z:r909){known.insert(z);known.insert(tr(z));}
 unordered_set<U> fresh910;fresh910.reserve(2500000);
 for(auto [k,l]:vector<pair<int,int>>{{5,2},{5,4},{6,1},{6,5},
  {7,2},{7,4},{7,6},{8,1},{8,3},{8,5},{8,7}}){
  auto x=enumerate(k,l);
  for(U z:x.vals)if(!known.count(z)&&!covered(aa(z),bb(z)))fresh910.insert(z);
 }
 size_t o910=0;
 for(U z:fresh910)if(fresh910.count(tr(z)))++o910;
 cerr<<"RECONSTRUCT_C910_NEW "<<fresh910.size()<<" "<<o910<<" "<<2*fresh910.size()-o910<<"\n";
 if(fresh910.size()!=1785732||o910!=8)exit(5);
 for(U z:fresh910){known.insert(z);known.insert(tr(z));}
 unordered_set<U> fresh;fresh.reserve(3000000);
 int families=0;
 for(int k=9;k<=12;++k)for(int ell=1;ell<k;++ell)
 if((k-ell)%2==1&&gcd(k,ell)==1){
  auto x=enumerate(k,ell);size_t c=0;
  for(U z:x.vals)if(!known.count(z)&&!covered(aa(z),bb(z))){++c;fresh.insert(z);}
  ++families;
  cout<<"FAMILY "<<k<<" "<<ell<<" "<<x.witnesses<<" "<<x.vals.size()<<" "<<c<<"\n";
 }
 size_t overlap=0;for(U z:fresh)if(fresh.count(tr(z)))++overlap;
 U added=2*fresh.size()-overlap;
 U C911=7784240442ULL+added;
 cout<<"TOTAL "<<families<<" "<<fresh.size()<<" "<<overlap<<" "<<added<<" "<<C911<<" "<<U(Q)*Q-C911<<"\n";
 if(families!=16||fresh.size()!=1562215||overlap!=34||added!=3124396||C911!=7787364838ULL)exit(6);
 U first=*min_element(fresh.begin(),fresh.end());
 cout<<"MIN_NEW_PAIR "<<aa(first)<<" "<<bb(first)<<"\n";
 return 0;
}
