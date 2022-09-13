E=True
B=NotImplementedError
A=None
F=1
G='PiicoDev could not communicate with module at address 0x{:02X}, check wiring'
from machine import I2C,Pin
class C:
	def writeto_mem(A,addr,memaddr,buf,*,addrsize=8):raise B('writeto_mem')
	def readfrom_mem(A,addr,memaddr,nbytes,*,addrsize=8):raise B('readfrom_mem')
	def write8(A,addr,buf,stop=E):raise B('write')
	def read16(A,addr,nbytes,stop=E):raise B('read')
	def __init__(A,bus=A,freq=A,sda=A,scl=A):raise B('__init__')
class D(C):
	def __init__(A):A.i2c=I2C(freq=100000,sda=Pin(4),scl=Pin(5));A.writeto_mem=A.i2c.writeto_mem;A.readfrom_mem=A.i2c.readfrom_mem
	def write8(B,addr,reg,data):
		if reg is A:B.i2c.writeto(addr,data)
		else:B.i2c.writeto(addr,reg+data)
	def read16(A,addr,reg):A.i2c.writeto(addr,reg,False);return A.i2c.readfrom(addr,2)
def H(bus=A,freq=A,sda=A,scl=A):A=D();return A
