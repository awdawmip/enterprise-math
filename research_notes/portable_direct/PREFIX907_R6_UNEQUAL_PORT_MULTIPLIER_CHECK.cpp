// PREFIX907 exact named-XOR checker (independent C++17 integer path).
// g++ -std=c++17 -O3 PREFIX907_R6_UNEQUAL_PORT_MULTIPLIER_CHECK.cpp -o prefix907 && ./prefix907
#include <bits/stdc++.h>
using namespace std;
using ll=long long;
constexpr ll N=1LL<<32,T=33*N;
constexpr int L=262145,H=524287,QN=131072;
static uint64_t code(int a,int b){return ((uint64_t)((a-L)/2)<<17)|(uint64_t)((b-L)/2);}
static pair<int,int> decode(uint64_t v){return {L+2*(int)(v>>17),L+2*(int)(v&((1<<17)-1))};}
int main(){
 set<int> old;for(int h=1;h<=17;h++)old.insert(1<<h);
 for(int i=2;i<=17;i++)for(int j=1;j<i;j++){old.insert((1<<i)+(1<<j));old.insert((1<<i)-(1<<j));}
 set<int> g905;
 for(int m=3;m<=8191;m+=2)for(int i=2;i<=17;i++)for(int j=1;j<i;j++)for(int s:{-1,1}){
  int v=(1<<i)+s*(1<<j);if(v%m)continue;int d=v/m;
  if(d>0&&d<=H-L&&!(d&1)&&!old.count(d))g905.insert(d);
 }
 set<int> g906;
 for(int m=1;m<=8191;m+=2)for(int i=18;i<=30;i++)for(int j=1;j<=17;j++)for(int s:{-1,1}){
  ll v=(1LL<<i)+s*(1LL<<j);if(v%m)continue;ll d=v/m;
  if(d>0&&d<=H-L&&d%2==0&&!old.count(d)&&!g905.count(d))g906.insert((int)d);
 }
 assert(old.size()==258&&g905.size()==276&&g906.size()==857);
 set<int> U={262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285};
 for(int x=400011;x<=400521;x+=2)U.insert(x);
 for(int x=480011;x<=480521;x+=2)U.insert(x);
 for(int q=L;q<=H;q+=2)for(int j=1;j<32;j++)if(((1LL<<j)-1)%q==0||((1LL<<j)+1)%q==0){U.insert(q);break;}
 set<int>P;for(int j=0;j<64;j++)for(int k:{1,3,5})P.insert(510000+k+194*j);
 assert(U.size()==552&&P.size()==192);
 auto previously=[&](int a,int b){
  if(1LL*a*b<T||U.count(a)||U.count(b)||1LL*(a/std::gcd(a,b))*b<N||33*((N+a-1)/a)>b||33*((N+b-1)/b)>a)return true;
  if(P.count(a)||P.count(b))return true;
  int d=abs(a-b);return old.count(d)||g905.count(d)||g906.count(d);
 };
 unordered_set<uint64_t> candidates;
 for(int i=18;i<=22;i++)for(int j=1;j<=17;j++)for(int s:{-1,1}){
  ll big=1LL<<i,h=1LL<<j,D=big+s*h;
  for(ll a=L;a<=H;a+=2){
   ll b=3*a-D; if(b<L||b>H||!(b&1))continue;
   ll A=3*a,per=2*h,x=s==1?((h-A%per+per)%per):((per-A%per)%per),y=x+A,v=y-s*h;
   if(!(x>=0&&x<big&&x+big<N&&y<N&&v>=0&&v<N&&(x^big)==x+big&&(y^h)==v&&x%a==y%a&&(x+big)%b==v%b&&3*a-b==D)){
    cerr<<"invalid witness a="<<a<<" b="<<b<<"\n";return 3;
   }
   candidates.insert(code((int)a,(int)b));
  }
 }
 unordered_set<uint64_t> novel;
 for(uint64_t v:candidates){auto [a,b]=decode(v);if(!previously(a,b))novel.insert(v);}
 size_t intersect=0;
 for(uint64_t v:novel){auto [a,b]=decode(v);if(novel.count(code(b,a)))intersect++;}
 ll union_new=(ll)novel.size()*2-intersect;
 cout<<"candidate="<<candidates.size()<<" novel_oriented="<<novel.size()<<" reverse_overlap="<<intersect<<" new_union="<<union_new<<"\n";
 if(candidates.size()!=2905419||novel.size()!=1576800||intersect!=188||union_new!=3153412)return 4;
 cout<<"PASS total_union="<<(7775271676LL+union_new)<<" remaining="<<(QN*1LL*QN-7775271676LL-union_new)<<"\n";
}
