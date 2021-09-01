#ifndef _BLAKE_HASH_H
#define _BLAKE_HASH_H

// Output hash is 32 bytes
#define HASHED_OUTPUT_LEN 32

void blake256_hash(const char* input, int inputsize, char* output);

#endif
