// Exhaust possible normalized planar sections of a three-colouring; independent of the global extension checker.
// Compile e.g. c++ -O3 -std=c++17 seeds.cpp -o seeds ; ./seeds > seeds.txt .
#include <array>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;
using U=unsigned long long;using Row=array<int,5>;using Mat=array<int,5>;
Row word[243];int deficiency[243],tr[243][720];vector<int> eligible,pt[243];set<U> out;
int enc(Row r){int z=0;for(int c:r)z=z*3+c;return z;}
U key(Mat r){sort(r.begin(),r.end());U z=0;for(int v:r)z=z*243+v;return z;}
int canonical_calls=0,pre=0;
U canonical(Mat m,Mat trans){U best=~0ULL;
  for(auto a:{m,trans})for(int r:a)for(int j:pt[r]){
    Mat s;for(int i=0;i<5;i++)s[i]=tr[a[i]][j];best=min(best,key(s));}
  return best;
}
void evaluate(Mat m,int d){
  Mat trans;int overlap=0;
  for(int j=0;j<5;j++){Row col;for(int i=0;i<5;i++)col[i]=word[m[i]][j];trans[j]=enc(col);d+=deficiency[trans[j]];}
  if(d>3)return;
  for(int j=0;j<5;j++)for(int i=0;i<5;i++){int c=word[m[i]][j];
    overlap+=(count(word[m[i]].begin(),word[m[i]].end(),c)==1 && count(word[trans[j]].begin(),word[trans[j]].end(),c)==1);}
  if(2*d+overlap>6)return;
  canonical_calls++;out.insert(canonical(m,trans));
}
void visit(Mat m,int k,int lo,int d){if(k==5){++pre;evaluate(m,d);return;}
  for(int j=lo;j<(int)eligible.size();j++){int r=eligible[j];if(d+deficiency[r]>1)continue;m[k]=r;visit(m,k+1,j,d+deficiency[r]);}}
int main(){
  for(int i=0;i<243;i++){int z=i,cnt[3]={};for(int k=4;k>=0;k--){word[i][k]=z%3;cnt[z%3]++;z/=3;}
    deficiency[i]=2-count(cnt,cnt+3,1);if(deficiency[i]<=1)eligible.push_back(i);}
  Row pp{0,1,2,3,4};int j=0;do{array<int,3>p{0,1,2};do{
    for(int r=0;r<243;r++){Row s;for(int k=0;k<5;k++)s[k]=p[word[r][pp[k]]];tr[r][j]=enc(s);if(tr[r][j]==5)pt[r].push_back(j);}j++;
  }while(next_permutation(p.begin(),p.end()));}while(next_permutation(pp.begin(),pp.end()));
  // Row 00012 has ternary code 5. The remaining four rows are in increasing order.
  Mat m{}; m[0]=5;visit(m,1,0,0);
  for(U s:out)printf("%llu\n",s);
  fprintf(stderr,"row_sets=%d accepted_before_orbit=%d planar_orbits=%zu\n",pre,canonical_calls,out.size());
  return 0;
}
