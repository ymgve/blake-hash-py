#ifndef _BLAKE_HASH_H
#define _BLAKE_HASH_H

// Max input length after which blake will ignore extra bytes
#define DECRED_MAX_LEN 180

// Output hash is 32 bytes
#define HASHED_OUTPUT_LEN 32

void blake256_hash(const char* input, char* output);

#endif
