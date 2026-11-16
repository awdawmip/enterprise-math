// Certified finite PF3 exhaustion using 50-bit downward dyadic interval and exact integer fallback.
// Requires standard IEEE binary extended 80-bit long double, round-to-nearest; check at runtime.
#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <cmath>
#include <cfloat>
#include <cfenv>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <vector>
using namespace std;using boost::multiprecision::cpp_int;
static const cpp_int Z=0;
static inline const cpp_int &at(const vector<cpp_int>&v,int i){return (i<0||i>=(int)v.size())?Z:v[i];}
static inline long double atf(const vector<long double>&v,int i){return (i<0||i>=(int)v.size())?0.0L:v[i];}
static cpp_int det3(const cpp_int&a,const cpp_int&b,const cpp_int&c,const cpp_int&d,const cpp_int&e,const cpp_int&f,const cpp_int&g,const cpp_int&h,const cpp_int&i){return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g);}
static long double trunc50(const cpp_int&v){
 if(v==0)return 0.0L;
 unsigned bits=boost::multiprecision::msb(v)+1u;
 unsigned shift=bits>50u?bits-50u:0u;
 cpp_int head=v>>shift;
 uint64_t hi=head.convert_to<uint64_t>();
 return ldexpl((long double)hi,(int)shift);
}
int main(int argc,char**argv){
 if(argc!=2)return 2;
 if(numeric_limits<long double>::radix!=2 || numeric_limits<long double>::digits<64 ||
    numeric_limits<long double>::max_exponent<4000 || !numeric_limits<long double>::is_iec559 ||
    numeric_limits<long double>::round_style != round_to_nearest ||
    std::fegetround() != FE_TONEAREST){cerr<<"unsupported FP environment\n";return 3;}
 ifstream in(argv[1]); if(!in)return 4;
 int r,len; unsigned long long totals[4]={},certs=0,backs=0,samples=0,rows=0;
 long double minmargin=1;
 cout<<setprecision(12);
 while(in>>r>>len){
    if(r%2!=1 || len!=r-1 || r<5)return 5;
    vector<cpp_int>v(len);for(auto&x:v)in>>x;
    vector<long double>w(len);
    for(int i=0;i<len;i++){if(v[i]<=0){cerr<<"bad input sign\n";return 6;}w[i]=trunc50(v[i]);if(!isfinite(w[i]))return 7;}
    unsigned long long counts[4]={},pos[4]={},neg[4]={},zero[4]={};
    for(int j=0;j<len;j++){counts[1]++;pos[1]++;}
    for(int j0=0;j0<len+1;j0++)for(int j1=j0+1;j1<len+1;j1++){
       cpp_int d=at(v,j0)*at(v,j1-1)-at(v,j1)*at(v,j0-1);
       counts[2]++;if(d>0)pos[2]++;else if(d==0)zero[2]++;else neg[2]++;
    }
    for(int j0=0;j0<len+2;j0++)for(int j1=j0+1;j1<len+2;j1++)for(int j2=j1+1;j2<len+2;j2++){
       long double a=atf(w,j0),b=atf(w,j1),c=atf(w,j2),
        d=atf(w,j0-1),e=atf(w,j1-1),f=atf(w,j2-1),
        g=atf(w,j0-2),h=atf(w,j1-2),i=atf(w,j2-2);
       long double t1=a*e*i, t2=b*f*g, t3=c*d*h, t4=-c*e*g, t5=-b*d*i, t6=-a*f*h;
       long double sumabs=fabsl(t1)+fabsl(t2)+fabsl(t3)+fabsl(t4)+fabsl(t5)+fabsl(t6);
       long double det=t1+t2+t3+t4+t5+t6;
       if(!isfinite(det) || !isfinite(sumabs))return 8;
       counts[3]++;
       bool cert=(det>0.0L && det>sumabs*1e-12L);
       if(cert){certs++;pos[3]++; minmargin=min(minmargin,det/sumabs);}
       else{
         backs++;
         cpp_int exact=det3(at(v,j0),at(v,j1),at(v,j2),at(v,j0-1),at(v,j1-1),at(v,j2-1),at(v,j0-2),at(v,j1-2),at(v,j2-2));
         if(exact>0)pos[3]++;else if(exact==0)zero[3]++;else {neg[3]++;if(neg[3]==1)cout<<"EXACT_NEG row="<<r<<" cols="<<j0<<","<<j1<<","<<j2<<" det="<<exact<<"\n";}
       }
       // Extra arbitrary precision independent check on deterministic sub-sample, including negative-cert bug detection.
       if((counts[3]%4096)==0 && cert){
          cpp_int exact=det3(at(v,j0),at(v,j1),at(v,j2),at(v,j0-1),at(v,j1-1),at(v,j2-1),at(v,j0-2),at(v,j1-2),at(v,j2-2));
          if(exact<=0){cerr<<"exact spotcheck mismatch\n";return 9;}samples++;
       }
    }
    for(int k=1;k<=3;k++){totals[k]+=counts[k];cout<<"R443_ROW "<<r<<" K "<<k<<" pos "<<pos[k]<<" zero "<<zero[k]<<" neg "<<neg[k]<<" count "<<counts[k]<<"\n";}
    rows++;cout.flush();
    if(neg[1]||neg[2]||neg[3]||zero[1]||zero[2]||zero[3]){cerr<<"nonpositive minor\n";return 10;}
 }
 cout<<"R443_CERTIFIED_PASS rows="<<rows<<" total="<<totals[1]+totals[2]+totals[3]<<" k1="<<totals[1]<<" k2="<<totals[2]<<" k3="<<totals[3]<<" interval_cert3="<<certs<<" integer_fallback3="<<backs<<" integer_spotchecks3="<<samples<<" min_relative_margin="<<minmargin<<"\n";
}
