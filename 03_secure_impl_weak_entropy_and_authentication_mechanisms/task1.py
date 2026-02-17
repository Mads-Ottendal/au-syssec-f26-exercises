import sys
import random
import time
from Crypto.Cipher import AES

def brute_force_decrypt(ciphertext_file, output_file):
    # Read the ciphertext file
    with open(ciphertext_file, 'rb') as f:
        nonce = f.read(16)
        tag = f.read(16)
        encrypted = f.read()
    
    print(f"Nonce length: {len(nonce)}, Tag length: {len(tag)}, Data length: {len(encrypted)}")
    
    # Friday Feb 14, 2026
    start_time = int(time.mktime((2026, 2, 17, 0, 0, 0, 0, 0, 0)))
    end_time = start_time + 86400
    
    print(f"Trying timestamps from {start_time} to {end_time}")
    
    for timestamp in range(start_time, end_time):
        random.seed(timestamp)
        key = random.randbytes(16)
        aes = AES.new(key, AES.MODE_GCM, nonce=nonce)
        
        try:
            plaintext = aes.decrypt_and_verify(encrypted, tag)
            with open(output_file, 'wb') as f:
                f.write(plaintext)
            print(f"✓ Found key! Timestamp: {timestamp}")
            return
        except ValueError:
            continue
    
    print("BOOOO Could not recover the key")

if __name__ == '__main__':
    brute_force_decrypt(sys.argv[1], sys.argv[2])