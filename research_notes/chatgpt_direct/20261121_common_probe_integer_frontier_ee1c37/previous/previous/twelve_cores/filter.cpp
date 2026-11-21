#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
using namespace std;using U=uint64_t;using M=__uint128_t;
struct MaskRec{U lo,hi;unsigned c,s;};
struct Rec{array<unsigned char,13> pts;unsigned char s;uint16_t c;};
int main(int argc,char**argv){
 ifstream db(argv[1],ios::binary),in(argv[2]);ofstream out(argv[3],ios::binary);
 U lo,hi;int least,high,cap[14]={};in>>lo>>hi>>least>>high;for(int s=least;s<=high;s++)in>>cap[s];
 int no_core=stoi(argv[4]);MaskRec row;while(db.read((char*)&row,sizeof(row))){
  if(row.lo&~lo||row.hi&~hi||int(row.c)>cap[row.s])continue;
  if(no_core>0&&(row.s==13||row.s==12&&row.c==1104))continue;
  if(no_core>1&&row.s==12&&row.c==1116)continue;
  if(no_core>2&&row.s>=11)continue;
  Rec r;r.pts.fill(125);r.s=row.s;r.c=row.c;int j=0;
  for(U a=row.lo;a;a&=a-1)r.pts[j++]=countr_zero(a);
  for(U b=row.hi;b;b&=b-1)r.pts[j++]=64+countr_zero(b);
  out.write((char*)&r,sizeof(r));
 }
}
