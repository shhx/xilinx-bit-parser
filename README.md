# Xilinx .bit Header Parser

This tool parses Xilinx .bit files to extract header metadata such as design name, part name, date, and time.

## Usage

To use this tool, run the `xilinx_bit_paser.py` script with the path to the .bit file as an argument.

```sh
python xilinx_bit_paser.py <path_to_bit_file>
```
## Example

```sh
python xilinx_bit_paser.py example.bit
```

## Output
```
Design Name: <design_name>
Part Name: <part_name>
Date: <date>
Time: <time>
```

## To Do
- Add support for checking the existence of the sync word on the bitstream data
- Add support for parsing the bitstream data
