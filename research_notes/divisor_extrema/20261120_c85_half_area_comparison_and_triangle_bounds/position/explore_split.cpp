#include <array>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>
// Exploratory, not certified. All primitive directions inside the deterministic
// inverse-basis bound are enumerated; two integer padding is floating protection.
int main(int argc,char**argv){
  uint64_t N=argc>1?std::stoull(argv[1]):200000,seed=851903;
  bool fixed_square=argc>2 && std::string(argv[2])=="square";
  std::mt19937_64 rng(seed);std::uniform_real_distribution<double>U(0.,1.);
  constexpr double pi=3.141592653589793238462643383279502884;
  std::array<double,2> theta{.25,.5};
  std::array<double,10> cuts{.01,.025,.05,.1,.2,.3,.4,.5,.75,1.};
  std::array<long double,10> sm{},sq{};
  std::array<long double,41> fs{},fq{};
  long double total=0,total2=0;uint64_t maxbox=0;
  for(uint64_t k=0;k<N;++k){
    double e=(U(rng)-.5)*pi/3,x=std::sin(e),y=std::cos(e)/U(rng),a=pi*U(rng),c=std::cos(a),s=std::sin(a),r=std::sqrt(y);
    double b00=c/r,b01=c*x/r-s*r,b10=s/r,b11=s*x/r+c*r;
    if(fixed_square){b00=1;b01=0;b10=0;b11=1;}
    std::array<double,3> ph{U(rng),U(rng),U(rng)};
    std::array<double,2> best{};
    auto point=[&](double vx,double vy){for(int j=0;j<2;++j){
      std::array<double,3> q{vx,(1-theta[j])*vx+theta[j]*vy,vy};double plus=INFINITY,minus=INFINITY;
      for(int d=0;d<3;++d) if(q[d]!=0){double v=std::abs(q[d]);plus=std::min(plus,(q[d]>0?1-ph[d]:ph[d])/v);minus=std::min(minus,(q[d]>0?ph[d]:1-ph[d])/v);}
      best[j]=std::max(best[j],std::max(plus,minus));
    }};
    point(b00,b10);point(b01,b11);point(b00+b01,b10+b11);point(b00-b01,b10-b11);
    double R=1/std::min(best[0],best[1]);
    int mb=std::ceil(R*(std::abs(b11)+std::abs(b01)))+2,nb=std::ceil(R*(std::abs(b10)+std::abs(b00)))+2;
    maxbox=std::max(maxbox,(uint64_t)(mb+1)*(2*nb+1));
    for(int n=-nb;n<=nb;++n)for(int m=0;m<=mb;++m){if((m==0&&n<=0)||std::gcd(m,std::abs(n))!=1)continue;double vx=m*b00+n*b01,vy=m*b10+n*b11;if(std::max(std::abs(vx),std::abs(vy))<=R*(1+1e-13))point(vx,vy);}
    double z0=std::pow(best[0],.1),z1=std::pow(best[1],.1),D=z0-z1;total+=D;total2+=D*D;
    for(int j=0;j<10;++j){double v=std::pow(cuts[j],.05),d=std::min(z0,v)-std::min(z1,v);sm[j]+=d;sq[j]+=d*d;}
    for(int j=0;j<=40;++j){double covol=.025*j,d=(best[0]*best[0]<covol)-(best[1]*best[1]<covol);fs[j]+=d;fq[j]+=d*d;}
  }
  auto se=[&](long double s,long double q){return std::sqrt((q-s*s/N)/(N-1)/N);};
  std::cout<<std::setprecision(17)<<"{\"status\":\"exploratory_not_certified\",\"model\":\""<<(fixed_square?"fixed_square_lattice":"haar")<<"\",\"samples\":"<<N<<",\"seed\":"<<seed<<",\"total\":["<<total/N<<","<<se(total,total2)<<"],\"maxbox\":"<<maxbox<<",\"split\":[";
  for(int j=0;j<10;++j){if(j)std::cout<<",";std::cout<<"["<<cuts[j]<<","<<sm[j]/N<<","<<se(sm[j],sq[j])<<"]";}
  std::cout<<"],\"F_quarter_minus_mid\":[";
  for(int j=0;j<=40;++j){if(j)std::cout<<",";std::cout<<"["<<.025*j<<","<<fs[j]/N<<","<<se(fs[j],fq[j])<<"]";}
  std::cout<<"]}\n";
}
