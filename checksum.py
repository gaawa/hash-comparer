# Python program to find SHA256 hash string of a file
import hashlib
 

def sha256(filename):
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        hash_str = sha256_hash.hexdigest()

    return hash_str