// R72 q-shell discovery. C++17, exact signed integers. Executed on 2026-11-21.
#include <bits/stdc++.h>
using namespace std;
struct Candidate {int a,b,c,q; array<int,6> gap;};
array<int,6> gaps(int a,int b,int c){
 int z2=2*a+6*b+12*c,z3=6*a+24*b+60*c,z4=14*a+78*b+252*c;
 return {abs(z2),abs(z3),abs(z4),abs(z3-z2),abs(z4-z2),abs(z4-z3)};
}
int main(int argc,char**argv){
 int Q=argc>1?atoi(argv[1]):234;
 vector<Candidate> keep;
 unsigned long long tested=0,dominated=0;
 for(int q=1;q<=Q;++q){
  for(int a=0;a<=q;++a){
   for(int b=-q;b<=q;++b){
    if(a==0&&b<0)continue;
    int pos=max(a,0)+max(b,0),neg=max(-a,0)+max(-b,0);
    if(max(pos,neg)>q)continue;
    int lo=-(q-neg),hi=q-pos;
    auto process=[&](int c){
      if(a==0&&b==0&&c<=0)return;
      ++tested;auto gg=gaps(a,b,c);
      bool isdom=false;
      for(const auto& k:keep){
       bool dom=true;for(int j=0;j<6;++j)if(k.gap[j]>gg[j]){dom=false;break;}
       if(dom){isdom=true;break;}
      }
      if(isdom){++dominated;return;}
      for(int i=(int)keep.size()-1;i>=0;--i)if(keep[i].q==q){
       bool dom=true;for(int j=0;j<6;++j)if(gg[j]>keep[i].gap[j]){dom=false;break;}
       if(dom)keep.erase(keep.begin()+i);
      }
      keep.push_back({a,b,c,q,gg});
    };
    if(max(pos,neg)==q){for(int c=lo;c<=hi;++c)process(c);}
    else{process(lo);if(lo!=hi)process(hi);}
   }
  }
 }
 cout<<"atlas_size "<<keep.size()<<" checked "<<tested<<" dominated "<<dominated<<"\n";
 for(auto &k:keep){
  cout<<k.q<<","<<k.a<<","<<k.b<<","<<k.c;
  for(int z:k.gap)cout<<","<<z;
  cout<<"\n";
 }
}
