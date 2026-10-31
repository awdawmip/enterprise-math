// Author-side full exact PF3 Schur-minor enumeration for signed BRC odd rows.
#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using boost::multiprecision::cpp_int;
using namespace std;
static const cpp_int zero(0);
static inline const cpp_int& c(const vector<cpp_int>& a,int h){return (h>=0 && h<(int)a.size())?a[h]:zero;}
static inline cpp_int det2(const cpp_int& a,const cpp_int& b,const cpp_int& c,const cpp_int& d){return a*d-b*c;}
static inline cpp_int det3(const cpp_int& a,const cpp_int& b,const cpp_int& c,const cpp_int& d,const cpp_int& e,const cpp_int& f,const cpp_int& g,const cpp_int& h,const cpp_int& i){return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g);}
int main(int argc,char**argv){
 if(argc!=4){cerr<<"usage INPUT START_R END_R\n";return 2;}
 ifstream f(argv[1]);if(!f){cerr<<"input_file_missing\n";return 3;}
 int lo=stoi(argv[2]),hi=stoi(argv[3]); int r,len;unsigned long long total=0;int rows=0;
 while(f>>r>>len){vector<cpp_int> a(len);for(auto &v:a)f>>v; if(r<lo||r>hi)continue;
  if(len!=r-1||r%2!=1||r<5){cerr<<"invalid r/len\n";return 4;}
  rows++;unsigned long long ns[4]={},p[4]={},z[4]={},ng[4]={};string firstneg;
  for(int j=0;j<len;j++){cpp_int D=a[j];ns[1]++;if(D>0)p[1]++;else if(D==0)z[1]++;else ng[1]++;}
  for(int j0=0;j0<len+1;j0++)for(int j1=j0+1;j1<len+1;j1++){
   cpp_int D=det2(c(a,j0),c(a,j1),c(a,j0-1),c(a,j1-1));ns[2]++;if(D>0)p[2]++;else if(D==0)z[2]++;else if(firstneg.empty()){ng[2]++;firstneg="k=2,j="+to_string(j0)+","+to_string(j1)+",det="+D.convert_to<string>();}else ng[2]++;
  }
  for(int j0=0;j0<len+2;j0++)for(int j1=j0+1;j1<len+2;j1++)for(int j2=j1+1;j2<len+2;j2++){
   cpp_int D=det3(c(a,j0),c(a,j1),c(a,j2),c(a,j0-1),c(a,j1-1),c(a,j2-1),c(a,j0-2),c(a,j1-2),c(a,j2-2));
   ns[3]++;if(D>0)p[3]++;else if(D==0)z[3]++;else{ng[3]++;if(firstneg.empty())firstneg="k=3,j="+to_string(j0)+","+to_string(j1)+","+to_string(j2)+",det="+D.convert_to<string>();}
  }
  for(int k=1;k<=3;k++){total+=ns[k];cout<<"EXACT_ROW "<<r<<" ORDER "<<k<<" pos "<<p[k]<<" zero "<<z[k]<<" neg "<<ng[k]<<" total "<<ns[k]<<"\n";}
  if(!firstneg.empty())cout<<"EXACT_FIRST_NEG "<<r<<" "<<firstneg<<"\n";
  cout.flush();
 }
 cout<<"R442_INTEGER_EXHAUST_DONE rows="<<rows<<" total="<<total<<"\n";
}
