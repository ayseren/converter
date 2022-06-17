from email import message
import hashlib
from secp256k1 import PrivateKey
import os

class Crypto:
  def __init__(self):
    print("Crypto")

  def ripemd160(self, value): 
    ripemd160 = hashlib.new('ripemd160',value.encode('utf-8')).hexdigest()
    print(ripemd160) 


  def sha1(self, value):
    sha1_value = hashlib.sha1(value.encode('utf-8')).hexdigest()
    print(sha1_value)


  def sha256(self, value):
    sha256_value = hashlib.sha256(value.encode('utf-8')).hexdigest()
    print(sha256_value)


#farkli sonuc cikti
  def hash160(self, value):
    sha256_value = hashlib.sha256(value.encode('utf-8')).hexdigest()
    hash160_value = hashlib.new('ripemd160', sha256_value.encode('utf-8')).hexdigest()
    print(hash160_value)


#farkli sonuc cikti
  def hash256(self, value):
    sha256_value = hashlib.sha256(value.encode('utf-8')).hexdigest()
    hash256_value = hashlib.sha256(sha256_value.encode('utf-8')).hexdigest()
    print(hash256_value)


  def secp256k1_key_generator(self, private_key=None):
    if private_key:
      privkey = PrivateKey(bytes(bytearray.fromhex(private_key)), raw=True)
      pubkey_compressed = privkey.pubkey.serialize().hex()
      pubkey_uncompressed = privkey.pubkey.serialize(compressed=False).hex()

      print({
        "private_key": private_key, 
        "compressed_public_key": pubkey_compressed, 
        "uncompressed_public_key": pubkey_uncompressed
      })

    # privkey none deger  
    if not private_key:
      privkey = PrivateKey()
      pubkey_compressed = privkey.pubkey.serialize().hex()
      pubkey_uncompressed = privkey.pubkey.serialize(compressed=False).hex()

      print({
        "private_key": private_key, 
        "compressed_public_key": pubkey_compressed, 
        "uncompressed_public_key": pubkey_uncompressed
      })

  def secp256k1_sign(self, message, private_key=None):
    #if not private_key:
    private_key = os.urandom(32)
    # private_key = PrivateKey(private_key, raw=False)
    #private_key = PrivateKey(bytes(bytearray.fromhex(private_key)), raw=True)
    private_key = PrivateKey(privkey=private_key, raw=True)
    sign =  private_key.ecdsa_sign(message.encode('utf-8'), raw=False)
    print(sign)


asdf = Crypto()
asdf.secp256k1_sign(message="hi", private_key="71d432da4caa0cb28a42867d8d88c6da0c2d3f05fc554cab9e36e3b530fb6807")
