"""
3n^2 - n = 2H
             _
6n = 1 +/- \/  1 + 24*H

issqrt()
http://stackoverflow.com/questions/295579/fastest-way-to-determine-if-an-integers-square-root-is-an-integer

Working from John's suggestion, I investigated properties of the last
n bits of a perfect square. By analyzing the last 6 bits, I found that
only 12 out of 64 values are possible for the last 6 bits. This means
81% of values can be eliminated without using any math. Implementing
this solution gave an additional 8% reduction in runtime (compared to
my original algorithm). Analyzing more than 6 bits results in a list
of possible ending bits which is too large to be practical.

      //John Carmack hack, converted to Java.
      // See: http://www.codemaestro.com/reviews/9
      int i;
      float x2, y;

      x2 = n * 0.5F;
      y  = n;
      i  = Float.floatToRawIntBits(y);
      i  = 0x5f3759df - ( i >> 1 );
      y  = Float.intBitsToFloat(i);
      y  = y * ( 1.5F - ( x2 * y * y ) );

      sqrt = (long)(1.0F/y);
"""
from math import sqrt

def issquare(n,LSB):
    if (n&0x3F) not in LSB:
        return False
    sn = int(sqrt(n))
    return sn*sn == n

def main():
    LSB = [0x00,0x01,0x04,0x09,0x10,0x11,0x19,0x21,0x24,0x29,0x31,0x39]
    i = 144
    H = i*(i + i - 1)
    D = 1+H*24
    while 1:
        if issquare(D,LSB) == False or (sqrt(D) + 1)%6 !=0:
            i += 1
            H = i*(i + i -1)
            D = 1+H*24
        else:
            break
    print i,H

if __name__ == "__main__":
    main()
