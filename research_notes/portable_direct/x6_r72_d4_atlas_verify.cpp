// R72 independent full-cube verification, C++17 exact integer arithmetic.
// Verify every nonzero q<=234 difference modulo overall sign against the fixed 28 witnesses.
// Compile: g++ -O3 -std=c++17 x6_r72_d4_atlas_verify.cpp -o verify && ./verify
#include <bits/stdc++.h>
using namespace std;
struct Entry {int q,a,b,c;int g[6];};
static const int coords[28][3]={
 {1,0,0},{0,2,-1},{1,-3,1},{2,-3,1},{3,-1,0},{1,3,-1},
 {3,-4,1},{4,-1,0},{3,2,-1},{4,-4,1},{5,-1,0},{5,-4,1},
 {6,-1,0},{3,-7,2},{6,-4,1},{7,-1,0},{7,2,-1},{9,-5,1},
 {10,-5,1},{15,-6,1},{21,-7,1},{24,-14,3},{36,-16,3},
 {39,-20,4},{42,-24,5},{45,-21,4},{66,-28,5},{114,-56,11}
};
int qval(int a,int b,int c){
 return max(max(a,0)+max(b,0)+max(c,0),max(-a,0)+max(-b,0)+max(-c,0));
}
void gval(int a,int b,int c,int g[6]){
 int z[4]={0,2*a+6*b+12*c,6*a+24*b+60*c,14*a+78*b+252*c};
 int k=0;
 for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)g[k++]=abs(z[i]-z[j]);
}
int main(){
 vector<Entry> lib;
 for(auto v:coords){
  Entry e; e.a=v[0];e.b=v[1];e.c=v[2];
  e.q=qval(e.a,e.b,e.c);gval(e.a,e.b,e.c,e.g);
  lib.push_back(e);
 }
 long long count=0,covered=0;
 int maxq=0,failures=0;
 for(int a=-234;a<=234;a++)for(int b=-234;b<=234;b++)for(int c=-234;c<=234;c++){
  if((a==0&&b==0&&c==0)||a<0||(a==0&&b<0)||(a==0&&b==0&&c<0))continue;
  int q=qval(a,b,c);if(q>234)continue;
  ++count;
  int g[6];gval(a,b,c,g);
  bool found=false;
  for(auto &e:lib){
   if(e.q>q)continue;
   bool ok=true;
   for(int i=0;i<6;i++)if(e.g[i]>g[i]){ok=false;break;}
   if(ok){found=true;break;}
  }
  if(found)++covered;
  else if(failures++<4)cerr<<"MISS "<<a<<","<<b<<","<<c<<" q="<<q<<"\n";
 }
 for(auto &e:lib)maxq=max(maxq,e.q);
 cout<<"{\"status\":\""<<(failures?"FAIL":"PASS")
     <<"\",\"tested_unoriented\":"<<count
     <<",\"covered\":"<<covered
     <<",\"failures\":"<<failures
     <<",\"atlas_size\":"<<lib.size()
     <<",\"atlas_max_q\":"<<maxq<<"}\n";
 return failures?1:0;
}
