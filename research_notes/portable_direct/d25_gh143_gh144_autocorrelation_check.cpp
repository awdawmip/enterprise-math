// GH143/GH144: 3347^2 exhaustive independent quartic/cubic/fibre certificates.
// All arithmetic is exact modulo 3347; F_3347^2 = F_3347[rho]/(rho^2-2).
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
constexpr int p=3347;
struct Elem {int a,b;};
int mod(long long v){v%=p;return v<0?int(v+p):int(v);}
Elem add(Elem x,Elem y){return {mod(x.a+y.a),mod(x.b+y.b)};}
Elem sub(Elem x,Elem y){return {mod(x.a-y.a),mod(x.b-y.b)};}
Elem mul(Elem x,Elem y){return {mod(1LL*x.a*y.a+2LL*x.b*y.b),mod(1LL*x.a*y.b+1LL*x.b*y.a)};}
Elem square(Elem x){return {mod(1LL*x.a*x.a+2LL*x.b*x.b),mod(2LL*x.a*x.b)};}
int norm(Elem x){return mod(1LL*x.a*x.a-2LL*x.b*x.b);}
int main(){
 const long long q=1LL*p*p;
 vector<int> chi(p,-1);chi[0]=0;
 for(int a=1;a<p;a++)chi[1LL*a*a%p]=1;
 Elem h={1370,685},B={2092,279};
 Elem h2=square(h),fourh2={mod(4LL*h2.a),mod(4LL*h2.b)};
 if(fourh2.a!=B.a||fourh2.b!=B.b){cerr<<"BAD_MARK_SQUARE\n";return 2;}
 vector<int8_t> fibre(q,0);
 long long cq=0,cc=0;
 array<long long,3> quartic_hist{},cubic_hist{};
 for(int a=0;a<p;a++)for(int b=0;b<p;b++){
  Elem u={a,b},u2=square(u);
  int wq=chi[norm(sub(square(sub(h,u)),square(u2)))];
  int wc=chi[norm(mul(u,add(add(u2,u),B)))];
  cq+=wq;cc+=wc;quartic_hist[wq+1]++;cubic_hist[wc+1]++;
  Elem t=sub(Elem{0,0},add(u2,u));
  fibre[t.a*p+t.b]+=chi[norm(u)];
 }
 array<long long,5> fh{};
 long long c0=0,ma=0,mb=0;
 for(int a=0;a<p;a++)for(int b=0;b<p;b++){
  int f=fibre[a*p+b];
  if(f< -2||f>2){cerr<<"BAD_FIBRE\n";return 3;}
  fh[f+2]++;c0+=f*f;
  Elem y=sub(B,Elem{a,b});ma+=1LL*y.a*f*f;mb+=1LL*y.b*f*f;
 }
 int m_a=mod(ma),m_b=mod(mb);
 int inv_minus3=1,base=p-3,e=p-2;
 while(e){if(e&1)inv_minus3=mod(1LL*inv_minus3*base);base=mod(1LL*base*base);e>>=1;}
 Elem recovered={mod(2092LL+1LL*m_a*inv_minus3),mod(1LL*m_b*inv_minus3)};
 long long corr=cq-1,trace=-cc;
 bool ok=cq==6105&&cc==6106&&corr==6104&&trace==-6106
   &&quartic_hist[0]==5598152&&quartic_hist[1]==0&&quartic_hist[2]==5604257
   &&cubic_hist[0]==5598150&&cubic_hist[1]==3&&cubic_hist[2]==5604256
   &&fh[0]==1400301&&fh[1]==0&&fh[2]==8401806&&fh[3]==2&&fh[4]==1400300
   &&c0==q-3&&m_a==0&&m_b==2510&&recovered.a==B.a&&recovered.b==B.b;
 cout<<"p="<<p<<" q="<<q<<" h=("<<h.a<<","<<h.b<<") B0=("<<B.a<<","<<B.b<<")\n";
 cout<<"quartic_sum="<<cq<<" quartic_chi(-1,0,+1)=("<<quartic_hist[0]<<","<<quartic_hist[1]<<","<<quartic_hist[2]<<")\n";
 cout<<"cubic_sum="<<cc<<" cubic_chi(-1,0,+1)=("<<cubic_hist[0]<<","<<cubic_hist[1]<<","<<cubic_hist[2]<<")\n";
 cout<<"C(h)="<<corr<<" E_B0_trace="<<trace<<" point_count="<<(q+1-trace)<<"\n";
 cout<<"fibre_hist(-2,-1,0,+1,+2)=("<<fh[0]<<","<<fh[1]<<","<<fh[2]<<","<<fh[3]<<","<<fh[4]<<")\n";
 cout<<"C(0)="<<c0<<" M_B0(0)=("<<m_a<<","<<m_b<<") recovered_B0=("<<recovered.a<<","<<recovered.b<<")\n";
 cout<<(ok?"PASS_GH143_GH144_P3347_EXACT":"FAIL_GH143_GH144_P3347")<<'\n';
 return ok?0:1;
}
