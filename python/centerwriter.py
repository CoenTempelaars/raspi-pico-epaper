# -----------------------------------------------------------------------------
# Author               :   Coen Tempelaars
# -----------------------------------------------------------------------------

from writer import Writer

class CenterWriter():
    def __init__(self, device, font, verbose=True):
        self.device = device
        self.writer = Writer(device, font, verbose)
        self.writer.set_clip(row_clip=True, col_clip=True, wrap=False)
        self.spacing = 0
        self.shift = 0

    def set_vertical_spacing(self, spacing):
        self.spacing = spacing

    def set_vertical_shift(self, shift):
        self.shift = shift

    def write_lines(self, lines):
        total_height = (self.writer.height + self.spacing) * len(lines) - self.spacing
        row = (self.device.height - total_height) // 2 + self.shift

        if row < 0 or (row + total_height) >= self.device.height:
            raise ValueError('Text position exceeds display limit (vertical)')

        for line in lines:
            length = self.writer.stringlen(line)
            col = (self.device.width - length) // 2 if length < self.device.width else 0

            self.writer.set_textpos(self.device, row, col)
            self.writer.printstring(line, invert=True)

            row += (self.writer.height + self.spacing)
            if row >= self.device.height:
                break
