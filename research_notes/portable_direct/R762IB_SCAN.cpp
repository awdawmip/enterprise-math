// R762IB independent C++17 exhaustive support-mask checker.
// Compile: g++ -O3 -std=c++17 R762IB_SCAN.cpp -o r762ib_scan
// Run: ./r762ib_scan
// Uses six 5-bit incidence fields; no field reaches 32 for m<=20.
#include <bits/stdc++.h>
using namespace std;
int main() {
  vector<int> triple;
  vector<uint64_t> w;
  for (int a=0; a<6; ++a) for (int b=a+1; b<6; ++b)
    for (int c=b+1; c<6; ++c) {
      int s=(1<<a)|(1<<b)|(1<<c);
      triple.push_back(s);
      uint64_t v=0;
      for (int k=0; k<6; ++k)
        if ((s>>k)&1) v += 1ULL<<(5*k);
      w.push_back(v);
    }
  assert(triple.size()==20);
  long core[21]={}, bad[21]={}, connected[21]={}, bad_connected[21]={};
  for (uint32_t mask=1; mask<(1U<<20); ++mask) {
    int m=__builtin_popcount(mask);
    if (m&1) continue;
    int degree[6]={};
    vector<int> ids;
    for (int j=0; j<20; ++j) if ((mask>>j)&1) {
      ids.push_back(j);
      for (int k=0; k<6; ++k) degree[k] += (triple[j]>>k)&1;
    }
    bool even=true;
    for (int d:degree) if (d&1) even=false;
    if (!even) continue;
    ++core[m];
    uint64_t target=0;
    for (int k=0; k<6; ++k) target += uint64_t(degree[k]/2)<<(5*k);
    int left_count=m/2, right_count=m-left_count;
    vector<uint64_t> left(1U<<left_count), right(1U<<right_count);
    for (unsigned b=1; b<left.size(); ++b) {
      int j=__builtin_ctz(b);
      left[b]=left[b&(b-1)]+w[ids[j]];
    }
    for (unsigned b=1; b<right.size(); ++b) {
      int j=__builtin_ctz(b);
      right[b]=right[b&(b-1)]+w[ids[left_count+j]];
    }
    sort(right.begin(),right.end());
    bool signable=false;
    for (uint64_t x:left)
      if (x<=target &&
          binary_search(right.begin(),right.end(),target-x)) {
        signable=true; break;
      }
    if (!signable) ++bad[m];
    unsigned seen=1;
    vector<int> todo={0};
    while (!todo.empty()) {
      int j=todo.back();todo.pop_back();
      for (int k=0; k<m; ++k)
        if (!((seen>>k)&1) &&
            __builtin_popcount(unsigned(triple[ids[j]]&triple[ids[k]]))==2) {
          seen|=1U<<k;
          todo.push_back(k);
        }
    }
    if (__builtin_popcount(seen)==m) {
      ++connected[m];
      if (!signable) ++bad_connected[m];
    }
  }
  long expected[21][4]={};
  expected[4][0]=165; expected[4][1]=30; expected[4][2]=90;
  expected[6][0]=1200;expected[6][1]=180;expected[6][2]=1020;
  expected[8][0]=3930;expected[8][2]=3915;
  expected[10][0]=5792;expected[10][1]=20;expected[10][2]=5772;
  expected[12][0]=3930;expected[12][2]=3930;
  expected[14][0]=1200;expected[14][2]=1200;
  expected[16][0]=165;expected[16][2]=165;
  expected[20][0]=1;expected[20][2]=1;
  for (int m=2; m<=20; m+=2) {
    assert(core[m]==expected[m][0] && bad[m]==expected[m][1]);
    assert(connected[m]==expected[m][2] &&
           bad_connected[m]==expected[m][3]);
    cout<<m<<","<<core[m]<<","<<bad[m]<<","
        <<connected[m]<<","<<bad_connected[m]<<"\n";
  }
  cout<<"PASS R762IB C++: all 2^20 masks checked\n";
}
