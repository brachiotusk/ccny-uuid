import hashlib
import hmac
import numpy as np
import math
import operator
class DRBG(object):
        def __init__(self, key, seed):
            self.key = key
            self.val = b'\x01' * 64
            self.reseed(seed)
            self.byte_index = 0
            self.bit_index = 0

        def hmac(self, key, val):
            return hmac.new(key, val, hashlib.sha512).digest()

        def reseed(self, data=b''):
            self.key = self.hmac(self.key, self.val + b'\x00' + data)
            self.val = self.hmac(self.key, self.val)

            if data:
                self.key = self.hmac(self.key, self.val + b'\x01' + data)
                self.val = self.hmac(self.key, self.val)

        def generate_bits(self, n):
            xs = np.zeros(n, dtype=bool)
            for i in range(0,n):
                xs[i] = (self.val[self.byte_index] >> (7 - self.bit_index)) & 1

                self.bit_index += 1
                if self.bit_index >= 8:
                    self.bit_index = 0
                    self.byte_index += 1

                if self.byte_index >= 8:
                    self.byte_index = 0
                    self.val = self.hmac(self.key, self.val)

            self.reseed()
            return xs
class Generate(object):
    def __init__ (self,key,seed):
        self.Buffer = b''
        self.counter = 0
        self.DRBG = DRBG(self,key,seed)
        self.KeyBuffer = b''
    def store(self):
        xc = b''
        l = len(self)
        closePower = 2 ** math.ceil(math.log2(l))
        HMACEncoded = self.DRBG.generate_bits(self, closePower)
        return (self.val >> self) & closePower
    def XOR(self, n):
        ll = Generate.store(self)
        final = b''
        for x in range(0,n):
            enc = operator.xor(self, self.val)
            final = final + enc
        return final

    def addBuffer(self):
        am = Generate.store(self)
        if(len(self.Buffer) > 0):
            for x in range(0, self.Buffer):
                a = self.DRBG.reseed(self, 1)
                self.DRBG.generate_bits(self, 1)
                c = bin((self.val >> x) & 1)
                xc = xc + c
                self.counter = self.counter + 1
                return xc
    def KeyXC(self)
        for y in range(0, len(self.val)):
            while(self.counter < self.Buffer)
                a = Generate.XOR(self, (Generate.addBuffer(self) >> y) & 1)
                self.val[y] = a
            b = Generate.XOR(self, self.val >> (y + self.counter) & 1)
            self.val[y+self.counter] = b

            


        
        



        

 
