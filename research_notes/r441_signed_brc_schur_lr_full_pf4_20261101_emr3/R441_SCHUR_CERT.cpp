#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <array>
#include <cmath>
#include <cfenv>
#include <cfloat>
#include <fstream>
#include <iostream>
#include <limits>
#include <string>
#include <vector>
using boost::multiprecision::cpp_int;
using namespace std;
static vector<vector<int>> perms[5];static vector<int> signp[5];
static void init(){for(int k=1;k<=4;k++){vector<int> p(k);for(int i=0;i<k;i++)p[i]=i;do{perms[k].push_back(p);int z=0;for(int i=0;i<k;i++)for(int j=i+1;j<k;j++)z+=p[i]>p[j];signp[k].push_back((z&1)?-1:1);}while(next_permutation(p.begin(),p.end()));}}
static cpp_int exact_det(const vector<cpp_int>& a,const int *j,int k){
 cpp_int m[4][4];int n=(int)a.size();
 for(int s=0;s<k;s++)for(int t=0;t<k;t++){int h=j[t]-s;m[s][t]=(h>=0&&h<n)?a[h]:cpp_int(0);}
 cpp_int v=0;for(size_t z=0;z<perms[k].size();z++){cpp_int t=signp[k][z];for(int s=0;s<k;s++)t*=m[s][perms[k][z][s]];v+=t;}return v;
}
static int certified(const vector<long double>& a,const int *j,int k){
 long double mat[4][4]{};int n=(int)a.size();
 for(int s=0;s<k;s++)for(int t=0;t<k;t++){int h=j[t]-s;if(h>=0&&h<n)mat[s][t]=a[h];}
 long double d=0,S=0;
 for(size_t z=0;z<perms[k].size();z++){
  const auto &p=perms[k][z];long double x=1;
  for(int s=0;s<k;s++)x*=mat[s][p[s]];
  d+=(signp[k][z]>0)?x:-x;S+=fabsl(x);
 }
 if(d>1.0e-12L*S)return +1;
 if(d<-1.0e-12L*S)return -1;
 return 0;
}
static unsigned long long choose(int n,int k){unsigned long long x=1;for(int i=1;i<=k;i++)x=x*(n+1-i)/i;return x;}
static unsigned long long counts[5][3];
static int n,k,r;static vector<long double> approx;static vector<cpp_int> exact;static int col[4];static unsigned long long fallback;static string firstneg;
static void visit(int z,int next){
 if(z==k){
  int v=certified(approx,col,k);
  if(v==0){fallback++;cpp_int d=exact_det(exact,col,k);v=(d>0)-(d<0);}
  counts[k][v+1]++;
  if(v<0&&firstneg.empty()){
   cpp_int d=exact_det(exact,col,k);firstneg="r="+to_string(r)+" k="+to_string(k)+" j=";
   for(int i=0;i<k;i++)firstneg+=to_string(col[i])+(i+1<k?",":"");
   firstneg+=" det="+d.convert_to<string>();
  }
  return;
 }
 for(int j=next;j<=n+k-1-(k-z-1);j++){col[z]=j;visit(z+1,j+1);}
}
int main(int argc,char**argv){
 if(LDBL_MANT_DIG<64||!numeric_limits<long double>::is_iec559||fegetround()!=FE_TONEAREST){cerr<<"UNSUPPORTED_FLOAT\n";return 9;}
 if(argc<2){cerr<<"usage input_file [start_r] [end_r]\n";return 2;}
 int rb=(argc>2)?stoi(argv[2]):5,re=(argc>3)?stoi(argv[3]):99;
 ifstream f(argv[1]);if(!f){cerr<<"cannot open\n";return 3;}
 init();int len;unsigned long long total=0,falls=0;int rows=0;
 while(f>>r>>len){exact.resize(len);for(int i=0;i<len;i++)f>>exact[i];if(r<rb||r>re)continue;
  approx.resize(len);
  for(int i=0;i<len;i++){
   int bits=(exact[i]==0)?0:(int)boost::multiprecision::msb(exact[i])+1;
   int shift=max(0,bits-60);cpp_int high=exact[i]>>shift;
   uint64_t hi=high.convert_to<uint64_t>();approx[i]=ldexpl((long double)hi,shift);
   if(!isfinite(approx[i])){cerr<<"input overflow";return 8;}
  }
  n=len-1;fallback=0;firstneg.clear();rows++;
  for(k=1;k<=4;k++){
   for(int s=0;s<3;s++)counts[k][s]=0;
   visit(0,0);
   unsigned long long count=counts[k][0]+counts[k][1]+counts[k][2];
   if(count!=choose(n+k,k)){cerr<<"count mismatch "<<r<<" "<<k<<"\n";return 11;}
   total+=count;
   cout<<"ROW "<<r<<" ORDER "<<k<<" pos "<<counts[k][2]<<" zero "<<counts[k][1]<<" neg "<<counts[k][0]<<" total "<<count<<" fallback "<<fallback<<"\n";
   if(counts[k][0]||counts[k][1])break;
  }
  falls+=fallback;
  if(!firstneg.empty())cout<<"FIRST_NEG "<<firstneg<<"\n";
 }
 cout<<"R441_CERTIFICATE_DONE rows="<<rows<<" total="<<total<<" exact_fallback="<<falls<<" mant="<<LDBL_MANT_DIG<<" cutoff=1e-12\n";
}
