// Independent integer certification of Schur-reduced PF3 minors, all contiguous rows, all column sets.
#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;using boost::multiprecision::cpp_int;
static const cpp_int Z=0;
static inline const cpp_int &a_at(const vector<cpp_int>&v,int i){return i<0||i>=int(v.size())?Z:v[i];}
static cpp_int det3(const cpp_int&a,const cpp_int&b,const cpp_int&c,const cpp_int&d,const cpp_int&e,const cpp_int&f,const cpp_int&g,const cpp_int&h,const cpp_int&i){return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g);}
int main(int argc,char**argv){
 if(argc!=2){cerr<<"usage R443_INTEGER_EXHAUST R443_INPUTS.txt\n";return 2;}
 ifstream in(argv[1]); if(!in){cerr<<"cannot read input\n";return 3;}
 int r,len,rows=0; unsigned long long global[4]={};
 while(in>>r>>len){
   if(r%2!=1||len!=r-1||r<5){cerr<<"bad row\n";return 4;}
   vector<cpp_int>v(len);for(auto&z:v)in>>z;
   unsigned long long n[4]={},pos[4]={},zero[4]={},neg[4]={};
   auto audit=[&](int m,const cpp_int&d,const string&js){n[m]++;if(d>0)pos[m]++;else if(d==0)zero[m]++;else{neg[m]++;if(neg[m]==1)cout<<"FIRST_NEG r="<<r<<" k="<<m<<" cols="<<js<<" det="<<d<<"\n";}};
   for(int x=0;x<len;x++)audit(1,v[x],to_string(x));
   for(int x=0;x<=len;x++)for(int y=x+1;y<=len;y++)audit(2,a_at(v,x)*a_at(v,y-1)-a_at(v,y)*a_at(v,x-1),to_string(x)+","+to_string(y));
   for(int x=0;x<len+2;x++)for(int y=x+1;y<len+2;y++)for(int z=y+1;z<len+2;z++){
     auto d=det3(a_at(v,x),a_at(v,y),a_at(v,z),a_at(v,x-1),a_at(v,y-1),a_at(v,z-1),a_at(v,x-2),a_at(v,y-2),a_at(v,z-2));
     audit(3,d,to_string(x)+","+to_string(y)+","+to_string(z));
   }
   for(int m=1;m<=3;m++){global[m]+=n[m];cout<<"EXACT_ROW "<<r<<" ORDER "<<m<<" pos "<<pos[m]<<" zero "<<zero[m]<<" neg "<<neg[m]<<" total "<<n[m]<<"\n";}
   cout.flush();rows++;
   if(neg[1]||neg[2]||neg[3]){cerr<<"NEGATIVE_FOUND row "<<r<<"\n";return 5;}
 }
 cout<<"R443_INTEGER_EXHAUST_DONE rows="<<rows<<" total="<<global[1]+global[2]+global[3]<<" order1="<<global[1]<<" order2="<<global[2]<<" order3="<<global[3]<<"\n";
}
