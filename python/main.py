# -----------------------------------------------------------------------------
# Author               :   Coen Tempelaars
# -----------------------------------------------------------------------------

from epd_3in7 import EPD_3in7
from centerwriter import CenterWriter
import freesans20

if __name__=='__main__':
    epd = EPD_3in7()
    cw = CenterWriter(epd, freesans20)

    epd.fill(0xff)
    cw.set_vertical_spacing(10)
    cw.write_lines(["Hello", "World"])
    epd.show()

    epd.deep_sleep()
