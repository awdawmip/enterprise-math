#include <bits/stdc++.h>
using namespace std;
using U=unsigned __int128;
struct Hasher { size_t operator()(U x)const noexcept{uint64_t a=(uint64_t)x,b=(uint64_t)(x>>64);auto mix=[](uint64_t x){x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;x*=0x94d049bb133111ebULL;return x^(x>>31);};return mix(a)^mix(b+0x9e3779b97f4a7c15ULL);}};
struct Act {int k;vector<uint32_t> m;};
int n,f;vector<Act> acts;
unordered_map<U,int,Hasher> memo;
unsigned long long visits=0,decisions=0,progress_step=5000000;
int V(U st){
  visits++;int alive=0;
  for(int h=0;h<n;h++)alive+=((st>>(h*4)&15)<=f);
  if(alive<=1)return 0;
  if(auto it=memo.find(st);it!=memo.end())return it->second;
  int best=INT_MAX/4;
  for(auto &act:acts){
    if(act.k>=best)continue;
    bool loop=false;int worst=0;
    for(auto mask:act.m){
      U next=st;
      for(int h=0;h<n;h++){
        int e=(st>>(h*4))&15;
        if(e<=f && !((mask>>h)&1)) next+=U(1)<<(4*h);
      }
      if(next==st){loop=true;break;}
      ++decisions;
      int c=V(next);
      if(c>worst)worst=c;
      if(worst+act.k>=best)break;
    }
    if(!loop)best=min(best,act.k+worst);
  }
  memo.emplace(st,best);
  if(memo.size()%progress_step==0)cerr<<"memo="<<memo.size()<<" calls="<<visits<<" transitions="<<decisions<<"\n";
  return best;
}
int main(int argc,char**argv){if(argc<3)return 2;ifstream is(argv[1]);int ac;is>>n>>ac;f=atoi(argv[2]);if(n>32||f>14)return 2;
for(int i=0;i<ac;i++){Act x;int m;is>>x.k>>m;for(int j=0;j<m;j++){uint32_t z;is>>z;x.m.push_back(z);}acts.push_back(move(x));}
cout<<"START n="<<n<<" f="<<f<<" actions="<<ac<<flush;
auto t=chrono::steady_clock::now();int res=V(0);auto s=chrono::duration<double>(chrono::steady_clock::now()-t).count();cout<<"\nEXACT_RESTRICTED n="<<n<<" f="<<f<<" V="<<res<<" memo="<<memo.size()<<" calls="<<visits<<" transitions="<<decisions<<" seconds="<<s<<"\n";
}
