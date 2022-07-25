# -----------------------------------------------------------------------------
# Author               :   Coen Tempelaars
# -----------------------------------------------------------------------------

from epd_3in7 import EPD_3in7

if __name__=='__main__':
    epd = EPD_3in7()

    epd.fill(0xff)
    epd.text("Hello, world!", 5, 10, epd.black)
    epd.show()

    epd.deep_sleep()
