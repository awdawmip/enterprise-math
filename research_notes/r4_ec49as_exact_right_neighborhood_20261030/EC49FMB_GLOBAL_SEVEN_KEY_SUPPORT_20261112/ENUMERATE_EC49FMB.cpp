#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false); cin.tie(nullptr);
  int n; unsigned full; cin>>n>>full; assert(n==92);
  vector<unsigned> m(n); vector<int> seed(n);
  for(int i=0;i<n;++i) cin>>m[i]>>seed[i];
  unsigned long long total[6]={}, cover[6]={};
  for(int a=0;a<n-4;++a) for(int b=a+1;b<n-3;++b) {
    unsigned ab=m[a]|m[b]; int bs=seed[a]+seed[b];
    for(int c=b+1;c<n-2;++c) {
      unsigned abc=ab|m[c]; int cs=bs+seed[c];
      for(int d=c+1;d<n-1;++d) {
        unsigned abcd=abc|m[d]; int ds=cs+seed[d];
        for(int e=d+1;e<n;++e) {
          int r=5-ds-seed[e]; ++total[r];
          if((abcd|m[e])==full) ++cover[r];
        }
      }
    }
  }
  unsigned long long all=0, feasible=0;
  for(int r=0;r<=5;++r) {
    all+=total[r]; feasible+=cover[r];
    cout<<r<<" "<<total[r]<<" "<<cover[r]<<"\n";
  }
  assert(all==49177128ULL && feasible==108434ULL);
  cout<<"GLOBAL_ENUMERATION_EXACT_PASS "<<all<<" "<<feasible<<"\n";
}
