// PREFIX906 independent exact 64-bit C++ witness, gap generation and overlap census.
// g++ -O3 -std=c++17 PREFIX906_R6_INDEPENDENT_INTEGER_CHECK.cpp -o prefix906 && ./prefix906
#include <bits/stdc++.h>
using namespace std;
using ll=long long;
constexpr ll N=1LL<<32,T=33*N;
constexpr int lo=262145,hi=524287, count_=131072;
struct R { int m,i,j,s; };
int main(){
  set<int> old; for(int h=1;h<=17;h++)old.insert(1<<h);
  for(int i=2;i<=17;i++)for(int j=1;j<i;j++){
    old.insert((1<<i)+(1<<j));old.insert((1<<i)-(1<<j));
  }
  set<int> prior;
  for(int m=3;m<=8191;m+=2)for(int i=2;i<=17;i++)for(int j=1;j<i;j++)for(int s:{-1,1}){
    int v=(1<<i)+s*(1<<j);if(v%m)continue;
    int d=v/m;if(d>0&&!(d&1)&&d<=hi-lo&&!old.count(d)) prior.insert(d);
  }
  if(prior.size()!=276){cerr<<"prior count fail\n";return 2;}
  map<int,R> g;
  for(int m=1;m<=8191;m+=2)for(int i=18;i<=30;i++)for(int j=1;j<=17;j++)for(int s:{-1,1}){
    ll v=(1LL<<i)+s*(1LL<<j);if(v%m)continue;
    ll d=v/m;if(d>0&&d<=hi-lo&&d%2==0&&!old.count(d)&&!prior.count(d))g.emplace(d,R{m,i,j,s});
  }
  if(g.size()!=857){cerr<<"new gap count fail "<<g.size()<<"\n";return 3;}
  vector<char> special(count_),panel(count_);
  set<int> S={262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285};
  for(int k=0;k<count_;k++){
    int q=lo+2*k;bool v=S.count(q)|| (q>=400011&&q<=400521) || (q>=480011&&q<=480521);
    for(int h=1;h<32&&!v;h++)v=((1LL<<h)-1)%q==0||((1LL<<h)+1)%q==0;
    special[k]=v;
  }
  for(int j=0;j<64;j++)for(int k:{1,3,5})panel[(510000+k+194*j-lo)/2]=true;
  if(count(special.begin(),special.end(),true)!=552||count(panel.begin(),panel.end(),true)!=192){cerr<<"U/P fail\n";return 4;}
  array<ll,6> totals{};
  for(auto [d,r]:g){
    int off=d/2;ll pairs=0,E=0,P=0,EP=0;
    for(int k=off;k<count_;k++){
      ll a=lo+2LL*k,b=a-d,m=r.m,h=1LL<<r.j,H=1LL<<r.i,A=m*a,period=2*h;
      ll x=(r.s==1)?((h-A%period+period)%period):((period-A%period)%period)%period;
      ll y=x+A,v=y+(r.s==1?-h:h),u=x+H;
      if(!(x>=0&&x<H&&y<N&&u<N&&v>=0&&v<N&&((x^H)==u)&&((y^h)==v)&&x%a==y%a&&u%b==v%b&&m*(a-b)==H+r.s*h)){
       cerr<<"witness fail d="<<d<<" a="<<a<<"\n";return 5;
      }
      ll L=a/std::gcd(a,b)*b;
      bool e=(a*b<T)||special[k]||special[k-off]||L<N||33*((N+a-1)/a)>b||33*((N+b-1)/b)>a;
      bool p=panel[k]||panel[k-off];pairs++;E+=e;P+=p;EP+=e&&p;
    }
    totals[0]+=pairs;totals[1]+=E;totals[2]+=P;totals[3]+=EP;totals[4]+=E+P-EP;totals[5]+=pairs-E-P+EP;
  }
  for(ll v:totals)cout<<v<<' ';
  cout<<'\n';
  array<ll,6> expected={79950454,35590676,189860,5519,35775017,44175437};
  if(totals!=expected)return 6;
  cout<<"PASS; gap_types="<<g.size()<<"; new_ordered="<<2*totals[5]<<"; total="<<7686920802+2*totals[5]<<'\n';
}
