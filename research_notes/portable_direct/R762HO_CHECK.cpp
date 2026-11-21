// R762HO independent checks: repeated Port word rank and odd-repetition BRC count.
// g++ -std=c++17 -O3 -Wall -Wextra R762HO_CHECK.cpp -o r762ho && ./r762ho
#include <bits/stdc++.h>
using namespace std;
using u64=uint64_t;
constexpr u64 ORIGIN=0x808080808080ULL;

u64 choose(int n,int k){u64 r=1;for(int j=1;j<=k;j++)r=r*(n-j+1)/j;return r;}

vector<u64> port_steps(const vector<string>& ports){
  vector<u64> steps;
  for(size_t i=0;i+1<ports.size();i++){
    int a=0,b=0;
    for(char v:ports[i])a|=1<<(v-'0');
    for(char v:ports[i+1])b|=1<<(v-'0');
    if(__builtin_popcount((unsigned)(a&b))!=1||__builtin_popcount((unsigned)(a|b))!=3) throw runtime_error("Port step invalid");
    u64 step=0;
    for(int d=0;d<6;d++)if((a|b)&(1<<d))step+=u64(1)<<(8*d);
    steps.push_back(step);
  }
  if(ports.front()!=ports.back())throw runtime_error("Port cycle not closed");
  return steps;
}

u64 direct(const vector<u64>& steps,int k){
  unordered_map<u64,u64> a,b;
  a.reserve(700000);b.reserve(700000);a[ORIGIN]=1;
  for(int t=0;t<k*(int)steps.size();t++){
    const u64 d=steps[t%steps.size()];b.clear();
    for(const auto &v:a){b[v.first+d]+=v.second;b[v.first-d]+=v.second;}
    a.swap(b);
  }
  return a[ORIGIN];
}

u64 grouped(const vector<u64>& steps,int k){
  map<u64,int> occurrences;
  for(u64 s:steps) occurrences[s]++;
  unordered_map<u64,u64> a,b;
  a.reserve(700000);b.reserve(700000);a[ORIGIN]=1;
  for(auto [h,count]:occurrences){
    const int N=count*k;b.clear();
    vector<pair<int,u64>> choices;
    for(int j=0;j<=N;j++)choices.push_back({2*j-N,choose(N,j)});
    for(const auto &v:a)for(const auto &[signed_steps,mult]:choices)
      b[v.first+static_cast<u64>(signed_steps)*h]+=v.second*mult;
    a.swap(b);
  }
  return a[ORIGIN];
}

int main(){
  const vector<string> w1={"01","02","01"};
  const vector<string> w2={"01","02","03","02","01"};
  const vector<string> w3={"01","02","03","01"};
  const vector<string> w14={"01","15","12","25","24","04","05","03","04","24","23","25","35","05","01"};
  const auto a=port_steps(w1),b=port_steps(w2),c=port_steps(w3),d=port_steps(w14);
  for(int k=1;k<=4;k++){
    u64 x=direct(a,k),y=choose(2*k,k);
    u64 xx=direct(b,k),yy=y*y;
    u64 xxx=direct(c,k),yyy=(k%2==0)?choose(k,k/2)*choose(k,k/2)*choose(k,k/2):0;
    if(x!=y||xx!=yy||xxx!=yyy)return 1;
    cout<<"k="<<k<<" rank1="<<x<<" rank2="<<xx<<" rank3="<<xxx<<"\n";
  }
  for(int k=1;k<=3;k++){
    u64 x=direct(d,k),y=grouped(d,k);
    const u64 expected[]={0,104ULL,313080ULL,1700835440ULL};
    if(x!=y||x!=expected[k]) return 2;
    cout<<"14-word k="<<k<<" direct="<<x<<" grouped="<<y<<"\n";
  }
  cout<<"PASS\n";
}
