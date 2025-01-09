import argparse
import struct


class XilinxHeaderParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.result = {}
        self._parse_file()

    def _parse_file(self):
        with open(self.file_path, "rb") as f:
            # Field 1: Header
            header_length = struct.unpack(">H", f.read(2))[0]  # Big-endian 2 bytes
            f.read(header_length) # Skip header bytes
            key_length = struct.unpack(">H", f.read(2))[0]  # ??
            # Parse key-length-value fields
            while True:
                key_data = f.read(1)  # 1 byte key
                if not key_data:
                    # End of file
                    break
                key = key_data[0]
                length = struct.unpack(">H", f.read(2))[0]  # Big-endian 2 bytes
                value = f.read(length)
                if key == ord("a"):  # Design name
                    self.result["design_name"] = value.decode("ascii").strip("\0")
                elif key == ord("b"):  # Part name
                    self.result["part_name"] = value.decode("ascii").strip("\0")
                elif key == ord("c"):  # Date
                    self.result["date"] = value.decode("ascii").strip("\0")
                elif key == ord("d"):  # Time
                    self.result["time"] = value.decode("ascii").strip("\0")
                elif key == ord("e"):  # Configuration bitstream
                    # Not implemented
                    break

    def get_design_name(self):
        return self.result.get("design_name")

    def get_part_name(self):
        return self.result.get("part_name")

    def get_date(self):
        return self.result.get("date")

    def get_time(self):
        return self.result.get("time")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse a Xilinx .bit file.")
    parser.add_argument("file_path", type=str, help="Path to the .bit file")
    args = parser.parse_args()

    parser = XilinxHeaderParser(args.file_path)
    print("Design Name:", parser.get_design_name())
    print("Part Name:", parser.get_part_name())
    print("Date:", parser.get_date())
    print("Time:", parser.get_time())
