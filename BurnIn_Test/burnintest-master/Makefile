
#CC	= arm-linux-gnueabi-gcc
CC	= gcc
#C89	= c89
#GCC	= gcc
#CCS	= /usr/ccs/bin/cc
#NACC	= /opt/ansic/bin/cc
CFLAGS	= -g -m64
S10GCCFLAGS    = -m64
S10CCFLAGS     = -m64
FLAG64BIT      = -m64
LDFLAGS	= -static

burnintest:burnintest.c
	$(CC) -DDEBUG -O3 -g $(LDFLAGS) $< -o $@

clean:
	rm -f burnintest
	rm -f *.o
