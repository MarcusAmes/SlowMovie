from waveshare_epd import epd7in5_V2
import sys
epd = epd7in5_V2.EPD()
epd.init()
epd.Clear()
sys.exit("Done")
