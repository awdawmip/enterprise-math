// PREFIX-873: exact all-r residue-fiber capacity profile, p=32
// Source model / frozen pin: PREFIX-872 / f42f2906d77f24085c123f3ccfe9667d41caa96d
// Build: g++ -O3 -std=c++17 PREFIX873_R6_ALL_FIBER_FLOORSUM_CHECK.cpp -o prefix873
// Run: ./prefix873 > prefix873_all_46_cases.txt
#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;
// Exact Euclidean floor_sum: sum_{0<=k<n} floor((a*k+b)/m).
static inline ull fs(ull n, ull m, ull a, ull b) {
  ull ans=0;
  while (true) {
    if (a>=m) { ans+=(n-1)*n*(a/m)/2; a%=m; }
    if (b>=m) { ans+=n*(b/m); b%=m; }
    ull y=a*n+b;
    if (y<m) break;
    n=y/m; b=y%m; swap(m,a);
  }
  return ans;
}
int main() {
  const int p=32;
  const ull N=(1ULL<<32), Q=(1ULL<<19)-1;
  const vector<int> G={1,3,5,7,9,11,13,15,19,21,23,25,27,29,35,37,39,47,49,53,55,59,61};
  for (int g:G) {
    ull A=Q/g; if(!(A&1)) A--;
    for(int rev=0;rev<2;rev++) {
      ull q1=(rev?g*(A-2):g*A), q2=(rev?g*A:g*(A-2));
      vector<int> pos(p),neg(p);
      for(int i=0;i<p;i++) {pos[i]=(1ULL<<i)%g; neg[i]=(g-pos[i])%g;}
      vector<ull> cnt(g);
      ull bad=0,maxover=0,maxr=0,maxclass=0;
      for(ull r=0;r<q1;r++) {
        ull m=(N-1-r)/q1+1;
        fill(cnt.begin(),cnt.end(),0);
        cnt[0]=m; // no-change event
        ull prev=fs(m,1,q1,r);
        for(int i=0;i<p;i++) {
          ull next=fs(m,2ULL<<i,q1,r);
          ull ones=prev-2*next,zeros=m-ones;
          cnt[pos[i]]+=zeros; cnt[neg[i]]+=ones;
          prev=next;
        }
        for(int a=0;a<g;a++) {
          if(cnt[a]>q2/g) {
            bad++;
            ull over=cnt[a]-q2/g;
            if(over>maxover) {maxover=over;maxr=r;maxclass=a;}
          }
        }
      }
      cout<<"g="<<g<<",orientation="<<(rev?"low-first":"high-first")
          <<",q1="<<q1<<",q2="<<q2
          <<",violating_ra="<<bad<<",max_over="<<maxover
          <<",r="<<maxr<<",a="<<maxclass<<"\n";
    }
  }
}
