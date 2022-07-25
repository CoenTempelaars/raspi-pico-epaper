# -----------------------------------------------------------------------------
# Author               :   Coen Tempelaars
# -----------------------------------------------------------------------------

from epd_3in7 import EPD_3in7
from writer import Writer
import freesans20

if __name__=='__main__':
    epd = EPD_3in7()
    wri = Writer(epd, freesans20)

    epd.fill(0xff)
    wri.printstring("Hello, world!", invert=True)
    epd.show()

    epd.deep_sleep()
