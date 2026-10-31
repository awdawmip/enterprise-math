// R444: exact-integer Schur/LR complete PF3 test for finitely supported signed BRC rows.
// Based on the R443 author-side integer checker; caches exact 2x2 cofactors.
#include <boost/multiprecision/cpp_int.hpp>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
using namespace std;
using boost::multiprecision::cpp_int;
static const cpp_int ZERO=0;
static const cpp_int& A(const vector<cpp_int>&v,int i){return (i<0 || i>=int(v.size()))?ZERO:v[i];}
static unsigned long long choose2(unsigned long long n){return n*(n-1)/2;}
static unsigned long long choose3(unsigned long long n){return n*(n-1)*(n-2)/6;}
int main(int argc,char**argv){
 if(argc!=2){cerr<<"usage: R444_PF3_INTEGER INPUT.txt\n";return 2;}
 ifstream f(argv[1]);if(!f){cerr<<"cannot open input\n";return 3;}
 unsigned long long totals[4]={},negs[4]={},zeros[4]={};int rows=0,r,len;
 while(f>>r>>len){
  if(r%2!=1 || r<5 || len!=r-1){cerr<<"invalid row header\n";return 4;}
  vector<cpp_int> a(len);for(auto &x:a){if(!(f>>x)){cerr<<"missing coefficient\n";return 4;}}
  const int N=len+2;
  vector<cpp_int> D(size_t(N)*N);
  auto d2=[&](int x,int y)->cpp_int&{return D[size_t(x)*N+y];};
  unsigned long long c[4]={},p[4]={},n[4]={},z[4]={};
  auto audit=[&](int m,const cpp_int &v,int x,int y,int zidx){
   c[m]++;if(v>0){p[m]++;return;}if(v==0)z[m]++;else n[m]++;
   if(n[m]+z[m]==1)cout<<"FIRST_NONPOS r="<<r<<" order="<<m<<" col="<<x<<","<<y<<","<<zidx<<" det="<<v<<"\n";
  };
  for(int x=0;x<len;x++)audit(1,a[x],x,-1,-1);
  for(int x=0;x<N;x++)for(int y=x+1;y<N;y++){
    d2(x,y)=A(a,x)*A(a,y-1)-A(a,y)*A(a,x-1);
    if(y<=len)audit(2,d2(x,y),x,y,-1);
  }
  for(int x=0;x<N;x++)for(int y=x+1;y<N;y++){
   const cpp_int &dxy=d2(x,y),&ax2=A(a,x-2),&ay2=A(a,y-2);
   for(int zidx=y+1;zidx<N;zidx++){
    cpp_int det=dxy*A(a,zidx-2)-d2(x,zidx)*ay2+d2(y,zidx)*ax2;
    audit(3,det,x,y,zidx);
   }
  }
  if(c[1]!=unsigned(len)||c[2]!=choose2(len+1)||c[3]!=choose3(len+2)){
    cerr<<"incomplete exhaustive domain\n";return 6;
  }
  for(int m=1;m<=3;m++){
   totals[m]+=c[m];negs[m]+=n[m];zeros[m]+=z[m];
   cout<<"R444_EXACT_ROW r="<<r<<" order="<<m<<" checked="<<c[m]<<" positive="<<p[m]<<" zero="<<z[m]<<" negative="<<n[m]<<"\n";
  }
  cout.flush();rows++;
 }
 cout<<"R444_EXACT_DONE rows="<<rows<<" checked="<<totals[1]+totals[2]+totals[3]<<" k1="<<totals[1]<<" k2="<<totals[2]<<" k3="<<totals[3]<<" nonpositive="<<negs[1]+negs[2]+negs[3]+zeros[1]+zeros[2]+zeros[3]<<"\n";
 if(rows==0||negs[1]+negs[2]+negs[3]+zeros[1]+zeros[2]+zeros[3])return 5;
 cout<<"R444_PF3_EXACT_PASS\n";
}
