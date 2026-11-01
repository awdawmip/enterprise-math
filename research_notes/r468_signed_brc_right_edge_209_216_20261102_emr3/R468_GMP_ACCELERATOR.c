/* Optional accelerator for exact unsigned Python integer multiplication.
 * Operands and product are big-endian unsigned byte arrays; no floating point.
 * Build: gcc -O3 -shared -fPIC R468_GMP_ACCELERATOR.c -o R468_GMP_ACCELERATOR.so -lgmp
 */
#include <gmp.h>
#include <stddef.h>
#include <stdint.h>
int multiply_be(const uint8_t *a,size_t na,const uint8_t *b,size_t nb,uint8_t*out,size_t cap,size_t *nout){
  mpz_t x,y,z;
  mpz_inits(x,y,z,NULL);
  mpz_import(x,na,1,1,1,0,a);
  mpz_import(y,nb,1,1,1,0,b);
  mpz_mul(z,x,y);
  size_t expected=(mpz_sizeinbase(z,2)+7)/8;
  if(expected>cap){mpz_clears(x,y,z,NULL);return -1;}
  if(mpz_cmp_ui(z,0)==0){*nout=0;}else{mpz_export(out,nout,1,1,1,0,z);}
  mpz_clears(x,y,z,NULL);return 0;
}
