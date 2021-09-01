import blake_hash

genesis = "0100000000000000000000000000000000000000000000000000000000000000000000000dc101dfc3c6a2eb10ca0c5374e10d28feb53f7eabcc850511ceadb99174aa66000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffff011b00c2eb0b000000000000000000000000a0d7b85600000000000000000000000000000000000000000000000000000000000000000000000000000000"
genesis = genesis.decode("hex")

# 32-byte hash returned
genesis_hash = blake_hash.getPoWHash(genesis)
genesis_blockid = genesis_hash[::-1].encode("hex")

if genesis_blockid == "298e5cc3d985bfe7f81dc135f360abe089edd4396b86d2de66b0cef42b21d980":
    print("Hash OK")
else:
    raise Exception("Hash bad")