#include <bits/stdc++.h>
using namespace std;
struct Step{int q; unsigned mask; uint64_t code;};
static uint64_t rngstate=0xa50c37b8aa221901ULL;
uint64_t rng(){rngstate^=rngstate<<7;rngstate^=rngstate>>9;rngstate^=rngstate<<8;return rngstate;}
int main(int argc,char**argv){
  int num=argc>1?atoi(argv[1]):250000;
  vector<int> port;for(int a=0;a<6;++a)for(int b=a+1;b<6;++b)port.push_back((1<<a)|(1<<b));
  vector<Step> nxt[15];
  for(int i=0;i<15;++i)for(int j=0;j<15;++j)if(__builtin_popcount((unsigned)(port[i]&port[j]))==1){unsigned mask=port[i]|port[j];uint64_t code=0;for(int t=0;t<6;++t)if(mask>>t&1)code+=1ULL<<(5*t);nxt[i].push_back({j,mask,code});}
  for(int m: {14,16,18,20,22}){
    vector<Step> h(m);long long closed=0,even=0,fail=0;
    int k=m/2,sz=1<<k,st=1<<(m-k);
    vector<uint64_t> aa(sz),bb(st);
    for(int it=0;it<num;++it){
      int p=0;unsigned maskxor=0;uint64_t H=0;
      for(int t=0;t<m-1;++t){auto &s=nxt[p][rng()%8]; h[t]=s;p=s.q;maskxor^=s.mask;H+=s.code;}
      if(__builtin_popcount((unsigned)(port[p]&port[0]))!=1)continue;
      ++closed;
      for(const auto &s:nxt[p]) if(s.q==0){h[m-1]=s;break;}
      maskxor^=h[m-1].mask;H+=h[m-1].code;
      if(maskxor)continue;
      ++even;
      uint64_t target=H/2;
      aa[0]=0;for(int i=1;i<sz;++i){int b=__builtin_ctz((unsigned)i);aa[i]=aa[i^(1<<b)]+h[b].code;}
      sort(aa.begin(),aa.end());
      bb[0]=0;bool found=binary_search(aa.begin(),aa.end(),target);
      for(int i=1;i<st&&!found;++i){int b=__builtin_ctz((unsigned)i);bb[i]=bb[i^(1<<b)]+h[k+b].code;found=binary_search(aa.begin(),aa.end(),target-bb[i]);}
      if(!found){++fail;cout<<"COUNTEREXAMPLE m="<<m<<" iteration="<<it<<" masks:";for(const auto &s:h)cout<<" "<<s.mask;cout<<"\nports: 0";for(const auto &s:h)cout<<" "<<s.q;cout<<"\n";return 0;}
    }
    cout<<"PASS sampled m="<<m<<" trials="<<num<<" closed="<<closed<<" axis_even="<<even<<" unsupported="<<fail<<"\n";
  }
}
