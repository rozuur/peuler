/*
Bit of an easy one, this. 

3/7 == 428571/999999. 

Well, the d with n closer to 3/7 would probably have 3*d=1 mod 7, so
that (3/7)d would be very close to an integer. That implies d=5 mod 7,
the larger d is 999997, so I just did int((3/7)*999997), and then
checked for common factors of that and 999997 (there were none).  */
