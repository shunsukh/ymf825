#!/usr/bin/python

import time
import pigpio

#CS0    24PIN
#MOSI   19PIN
#MISO   21PIN
#SCLK   23PIN
#RST_N  16PIN(GPIO23)
GPIO_RST_N = 23
#OE     18PIN(GPIO24)
GPIO_OE  = 24
GPIO_CS0 = 8

HIGH = 1
LOW  = 0

#0:5V 1:3.3V
OUTPUT_POWER = 0


pi = pigpio.pi()
pi.set_mode(GPIO_RST_N, pigpio.OUTPUT)
pi.set_mode(GPIO_OE,  pigpio.OUTPUT)

pi.write(GPIO_OE, HIGH)
time.sleep(0.001)
pi.write(GPIO_RST_N, HIGH)
print("RST_N", pi.read(GPIO_RST_N))
#pi.write(GPIO_OE, LOW)
time.sleep(0.001)

h = pi.spi_open(1, 100000, 0)
if h < 0:
    print("Failed to open SPI")
else:
    print("SPI opened")

pi.set_mode(GPIO_CS0, pigpio.OUTPUT)

#Initialize
def spi_m_write(addr, datas, num):
    print("spi_write:")
    print "(" + str(addr)+":"+(','.join([str(item) for item in datas]))+")"
    pi.write(GPIO_CS0, LOW)
    pi.spi_write(h, [addr])
    for cnt in range(0,num):
        pi.spi_write(h, [datas[cnt]])
    pi.write(GPIO_CS0, HIGH)

def spi_s_write(addr, data):
    print("spi_s_write:0x%02x, 0x%02x" % (addr, data))
    spi_m_write(addr, [data], 1)

def init_ymf825():
    print("initialize ymf825:")
    pi.write(GPIO_RST_N, LOW)
    time.sleep(0.001)
    pi.write(GPIO_RST_N, HIGH)
    time.sleep(0.001)
    spi_s_write(0x1d, OUTPUT_POWER)
    spi_s_write(0x02, 0x0e)
    time.sleep(0.0001)
    spi_s_write(0x00, 0x01) #CLKEN
    spi_s_write(0x01, 0x00) #AKRST
    spi_s_write(0x1a, 0xa3)
    time.sleep(0.0001)
    spi_s_write(0x1a, 0x00)
    time.sleep(0.03)
    spi_s_write(0x02, 0x04) #AP1, AP3
    time.sleep(0.0001)
    spi_s_write(0x02, 0x00)
    ##add
    spi_s_write(0x19, 0xf0) #Master Vol
    spi_s_write(0x1b, 0x3f) #interpolation
    spi_s_write(0x14, 0x00) #interpolation
    spi_s_write(0x03, 0x01) #Analog Gain
    #
    spi_s_write(0x08, 0xf6)
    time.sleep(0.021)
    spi_s_write(0x08, 0x00)
    spi_s_write(0x09, 0xf8)
    spi_s_write(0x0a, 0x00)
    #
    spi_s_write(0x17, 0x40) #MS_S
    spi_s_write(0x18, 0x00)


def set_tone():
    tone_data = ( 0x81, #header
                  #T_ADR 0
                  0x01, 0x85,
                  0x00, 0x7f, 0xf4, 0xbb, 0x00, 0x10, 0x40,
                  0x00, 0xaf, 0xa0, 0x0e, 0x03, 0x10, 0x40,
                  0x00, 0x2f, 0xf3, 0x9b, 0x00, 0x20, 0x41,
                  0x00, 0xaf, 0xa0, 0x0e, 0x01, 0x10, 0x40,
                  0x80, 0x03, 0x81, 0x80 )
    spi_s_write(0x08, 0xf6)
    time.sleep(0.0001)
    spi_s_write(0x08, 0x00)
    spi_m_write(0x07, tone_data, 35)

def set_ch():
    spi_s_write(0x0f, 0x30) #keyon = 0
    spi_s_write(0x10, 0x71) #chvol
    spi_s_write(0x11, 0x00) #xvb
    spi_s_write(0x12, 0x08) #frac
    spi_s_write(0x13, 0x00) #frac

def keyon(fnumh, fnuml):
    spi_s_write(0x0b, 0x00) #voice num
    spi_s_write(0x0c, 0x54) #vovol
    spi_s_write(0x0d, fnumh) #fnum
    spi_s_write(0x0e, fnuml) #fnum
    spi_s_write(0x0f, 0x40) #keyon = 1

def keyoff():
    spi_s_write(0x0f, 0x00) #keyon = 0


# setup ---------------
init_ymf825()
set_tone()
set_ch()

# test play -----------
for cnt in range(1,5):
    keyon(0x14, 0x65)
    time.sleep(0.5)
    keyoff()
    time.sleep(0.2)
    keyon(0x1c, 0x11)
    time.sleep(0.5)
    keyoff()
    time.sleep(0.2)
    keyon(0x1c, 0x42)
    time.sleep(0.5)
    keyoff()
    time.sleep(0.2)
    keyon(0x1c, 0x5d)
    time.sleep(0.5)
    keyoff()
    time.sleep(0.2)
    keyon(0x24, 0x17)
    time.sleep(0.5)
    keyoff()
    time.sleep(0.2)


pi.spi_close(h)
print("SPI closed")
