// R87 full-lattice exact tie certificate for paired BRC precision.
// g++ -O3 -std=c++17 x6_r87_full_lattice_ties_verify.cpp -o r87_verify && ./r87_verify
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  constexpr int P=234;
  constexpr int pairs[6][2]={{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
  // Neighbor classes: low open, low wall, low middle, t=1, high middle,
  // high wall, high open. Alternating: t<1, t=1, t>1.
  long long counts[6][7]{};
  vector<array<int,3>> matches[6][7];
  long long checked=0;
  for (int x=0;x<=P;++x) for (int y=-P;y<=P;++y) for (int z=-P;z<=P;++z) {
    if (x==0 && y<0) continue;
    if (x==0 && y==0 && z<=0) continue;
    const int q=max(x+max(y,0)+max(z,0),max(-y,0)+max(-z,0));
    if(q>P)continue;
    ++checked;
    const int v[4]={0,2*x+6*y+12*z,6*x+24*y+60*z,14*x+78*y+252*z};
    int gap[4][4]{};
    for(int i=0;i<4;++i)for(int j=i+1;j<4;++j)
      gap[i][j]=gap[j][i]=abs(v[j]-v[i])/2;
    for(int k=0;k<6;++k) {
      const int i=pairs[k][0],j=pairs[k][1];
      int a=-1,b=-1;
      for(int e=0;e<4;++e)if(e!=i && e!=j) {if(a<0)a=e;else b=e;}
      const int h=gap[i][j],ell=gap[a][b],
                m=max({gap[i][a],gap[i][b],gap[j][a],gap[j][b]});
      bool take[7]{};
      if(k==1 || k==4) {
        take[0]=(h==0 && m<=1 && ell<=1);
        take[1]=(h<=1 && m<=1 && ell<=1);
        take[2]=(ell==0 && m<=1 && h<=1);
      } else {
        take[0]=(h==0 && m==6 && ell<=11);
        take[1]=(h<=1 && m<=6 && ell<=11);
        take[2]=(h<=1 && m<=5 && ell<=10);
        take[3]=(h<=1 && m<=1 && ell<=1);
        take[4]=(h<=10 && m<=5 && ell<=1);
        take[5]=(h<=11 && m<=6 && ell<=1);
        take[6]=(ell==0 && m==6 && h<=11);
      }
      for(int t=0;t<7;++t)if(take[t]) {
        ++counts[k][t];
        matches[k][t].push_back({x,y,z});
      }
    }
  }
  assert(checked==21492159LL);
  for(int k=0;k<6;++k) {
    const bool alternate=(k==1 || k==4);
    const int expected[7]={3,7,1,1,1,7,3};
    for(int t=0;t<(alternate?3:7);++t)
      assert(counts[k][t]==(alternate?1:expected[t]));
    for(int t=0;t<(alternate?3:7);++t)for(auto v:matches[k][t]) {
      const int x=v[0],y=v[1],z=v[2];
      const int q=max(x+max(y,0)+max(z,0),max(-y,0)+max(-z,0));
      assert(q<=82);
    }
  }
  cout<<"R87_FULL_LATTICE_EXACT PASS checked="<<checked<<" max_q=234\n";
  for(int k=0;k<6;++k) {
    const bool alternate=(k==1 || k==4);
    cout<<"H="<<pairs[k][0]+1<<pairs[k][1]+1
        <<" type="<<(alternate?"alternating":"neighboring")<<"\n";
    for(int t=0;t<(alternate?3:7);++t) {
      cout<<"  class="<<t<<" count="<<counts[k][t]<<" vectors=";
      for(auto v:matches[k][t])
        cout<<"("<<v[0]<<","<<v[1]<<","<<v[2]<<")";
      cout<<"\n";
    }
  }
}
