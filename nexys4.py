#
# This file is part of LiteX-Boards.
#
# Copyright (c) 2018-2019 Florent Kermarrec <florent@enjoy-digital.fr>
# SPDX-License-Identifier: BSD-2-Clause

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform, VivadoProgrammer, Adept
from litex.build.openocd import OpenOCD

from litex.soc.cores import spi_flash

# IOs ----------------------------------------------------------------------------------------------

_io = [
    # Clk / Rst
    ("clk", 0, Pins("E3"), IOStandard("LVCMOS33")),
    ("cpu_reset", 0, Pins("C12"), IOStandard("LVCMOS33")),

    # Leds
    ("user_led",  0, Pins("T8"), IOStandard("LVCMOS33")),
    ("user_led",  1, Pins("V9"), IOStandard("LVCMOS33")),
    ("user_led",  2, Pins("R8"), IOStandard("LVCMOS33")),
    ("user_led",  3, Pins("T6"), IOStandard("LVCMOS33")),
    ("user_led",  4, Pins("T5"), IOStandard("LVCMOS33")),
    ("user_led",  5, Pins("T4"), IOStandard("LVCMOS33")),
    ("user_led",  6, Pins("U7"), IOStandard("LVCMOS33")),
    ("user_led",  7, Pins("U6"), IOStandard("LVCMOS33")),
    ("user_led",  8, Pins("V4"), IOStandard("LVCMOS33")),
    ("user_led",  9, Pins("U3"), IOStandard("LVCMOS33")),
    ("user_led", 10, Pins("V1"), IOStandard("LVCMOS33")),
    ("user_led", 11, Pins("R1"), IOStandard("LVCMOS33")),
    ("user_led", 12, Pins("P5"), IOStandard("LVCMOS33")),
    ("user_led", 13, Pins("U1"), IOStandard("LVCMOS33")),
    ("user_led", 14, Pins("R2"), IOStandard("LVCMOS33")),
    ("user_led", 15, Pins("P2"), IOStandard("LVCMOS33")),

    # Switches
    ("user_sw",  0, Pins("U9"), IOStandard("LVCMOS33")),
    ("user_sw",  1, Pins("U8"), IOStandard("LVCMOS33")),
    ("user_sw",  2, Pins("R7"), IOStandard("LVCMOS33")),
    ("user_sw",  3, Pins("R6"), IOStandard("LVCMOS33")),
    ("user_sw",  4, Pins("R5"), IOStandard("LVCMOS33")),
    ("user_sw",  5, Pins("V7"), IOStandard("LVCMOS33")),
    ("user_sw",  6, Pins("V6"), IOStandard("LVCMOS33")),
    ("user_sw",  7, Pins("V5"), IOStandard("LVCMOS33")),
    ("user_sw",  8, Pins("U4"), IOStandard("LVCMOS33")),
    ("user_sw",  9, Pins("V2"), IOStandard("LVCMOS33")),
    ("user_sw", 10, Pins("U2"), IOStandard("LVCMOS33")),
    ("user_sw", 11, Pins("T3"), IOStandard("LVCMOS33")),
    ("user_sw", 12, Pins("T1"), IOStandard("LVCMOS33")),
    ("user_sw", 13, Pins("R3"), IOStandard("LVCMOS33")),
    ("user_sw", 14, Pins("P3"), IOStandard("LVCMOS33")),
    ("user_sw", 15, Pins("P4"), IOStandard("LVCMOS33")),

    # Buttons
    ("btnc", 0, Pins("E16"), IOStandard("LVCMOS33")),# btnc
    ("btnd", 1, Pins("V10"), IOStandard("LVCMOS33")),# btnd
    ("btnl", 2, Pins("T16"), IOStandard("LVCMOS33")),# btnl
    ("btnr", 3, Pins("R10"), IOStandard("LVCMOS33")),# btnr
    ("btnu", 4, Pins("F15"), IOStandard("LVCMOS33")),# btnu

    # Serial
    ("serial", 0,
        Subsignal("tx", Pins("D4")),# uart_txd_out - RsTx 
        Subsignal("rx", Pins("C4")),# uart_txd_in - RsRx
        IOStandard("LVCMOS33"),
    ),
    
    # serial 1 (uart1)
    
    ("uart1", 0,
        Subsignal("tx", Pins("H4")),# uart_txd_out - RsTx 
        Subsignal("rx", Pins("H1")),# uart_txd_in - RsRx
        IOStandard("LVCMOS33"),
    ),
    
    ("ledRGB", 1,
        Subsignal("r", Pins("K6")),
        Subsignal("g", Pins("H6")),
        Subsignal("b", Pins("L16")),
        IOStandard("LVCMOS33"),
    ),
    ("ledRGB", 2,
        Subsignal("r", Pins("K5")),
        Subsignal("g", Pins("F13")),
        Subsignal("b", Pins("F6")),
        IOStandard("LVCMOS33"),
    ),
    
    # 7SEG DISPLAY
    ("display_digit",  0, Pins("N6"), IOStandard("LVCMOS33")),
    ("display_digit",  1, Pins("M6"), IOStandard("LVCMOS33")),
    ("display_digit",  2, Pins("M3"), IOStandard("LVCMOS33")),
    ("display_digit",  3, Pins("N5"), IOStandard("LVCMOS33")),
    ("display_digit",  4, Pins("N2"), IOStandard("LVCMOS33")),
    ("display_digit",  5, Pins("N4"), IOStandard("LVCMOS33")),
    ("display_digit",  6, Pins("L1"), IOStandard("LVCMOS33")),
    ("display_digit",  7, Pins("M1"), IOStandard("LVCMOS33")),

    ("display_segment",  0, Pins("L3"), IOStandard("LVCMOS33")),
    ("display_segment",  1, Pins("N1"), IOStandard("LVCMOS33")),
    ("display_segment",  2, Pins("L5"), IOStandard("LVCMOS33")),
    ("display_segment",  3, Pins("L4"), IOStandard("LVCMOS33")),
    ("display_segment",  4, Pins("K3"), IOStandard("LVCMOS33")),
    ("display_segment",  5, Pins("M2"), IOStandard("LVCMOS33")),
    ("display_segment",  6, Pins("L6"), IOStandard("LVCMOS33")),
    ("display_segment",  7, Pins("M4"), IOStandard("LVCMOS33")),
    
    ("adxl362_spi", 0, #Accelerometer
        Subsignal("cs_n", Pins("C15")),
        Subsignal("clk", Pins("D15")),
        Subsignal("mosi", Pins("B14")),
        Subsignal("miso", Pins("D13")),
        IOStandard("LVCMOS33")
    ),
    
    ("spiflash_4x", 0,  # clock needs to be accessed through STARTUPE2
        Subsignal("cs_n", Pins("L13")),
        Subsignal("dq", Pins("K17", "K18", "L14", "M14")),
        IOStandard("LVCMOS33")
    ),
    ("spiflash_1x", 0,  # clock needs to be accessed through STARTUPE2
        Subsignal("cs_n", Pins("L13")),
        Subsignal("mosi", Pins("K17")),
        Subsignal("miso", Pins("K18")),
        Subsignal("wp", Pins("L14")),
        Subsignal("hold", Pins("M14")),
        IOStandard("LVCMOS33")
    ),
    
    
    # SDCard - NO revisado para Nexys4
    ("spisdcard", 0,
        Subsignal("rst",  Pins("E2")), # ok
        Subsignal("clk",  Pins("B1")), # ok
        Subsignal("mosi", Pins("C1"), Misc("PULLUP True")), #
        Subsignal("cs_n", Pins("D2"), Misc("PULLUP True")), #
        Subsignal("miso", Pins("C2"), Misc("PULLUP True")), #
        Misc("SLEW=FAST"),
        IOStandard("LVCMOS33"),
    ),
    ("sdcard", 0,
        Subsignal("rst",  Pins("E2"),          Misc("PULLUP True")),
        Subsignal("data", Pins("C2 E1 F1 D2"), Misc("PULLUP True")),
        Subsignal("cmd",  Pins("C1"),          Misc("PULLUP True")),
        Subsignal("clk",  Pins("B1")),
        Subsignal("cd",   Pins("A1")),
        Misc("SLEW=FAST"),
        IOStandard("LVCMOS33"),
    ),
    
    # DDR borrada, la nexys4 posee una Celullar RAM -_-

    # RMII Ethernet - No revisado para Nexys4
    ("eth_clocks", 0,
        Subsignal("ref_clk", Pins("D5")),
        IOStandard("LVCMOS33"),
    ),

    ("eth", 0,
        Subsignal("rst_n",   Pins("B3")),# ok
        Subsignal("rx_data", Pins("C11 D10")), # ok
        Subsignal("crs_dv",  Pins("D9")), # ok
        Subsignal("tx_en",   Pins("B9")), # ok
        Subsignal("tx_data", Pins("A10 A8")), # ok, aunque verificar orden de los pines
        Subsignal("mdc",     Pins("C9")), # ok
        Subsignal("mdio",    Pins("A9")), # ok
        Subsignal("rx_er",   Pins("C10")), # ok
        Subsignal("int_n",   Pins("B8")), # D8 por B8
        IOStandard("LVCMOS33")
     ),
]

# Platform -----------------------------------------------------------------------------------------

class Platform(XilinxPlatform):
    default_clk_name   = "clk100"
    default_clk_period = 1e9/100e6
    default_clk_period = 10.0
    
    #agregado:
    
    # From https://www.xilinx.com/support/documentation/user_guides/ug470_7Series_Config.pdf
    # 17536096 bits == 2192012 == 0x21728c -- Therefore 0x220000
    gateware_size = 0x220000

    # Micron N25Q128A13ESF40 (ID 0x0018ba20)
    # FIXME: Create a "spi flash module" object in the same way we have SDRAM
    # module objects.
    # Mas info https://github.com/fupy/issues-wiki/issues/9 - https://github.com/fupy/issues-wiki/issues/9#issuecomment-369819759
    spiflash_model = "S25FL128" #"n25q128a13"
    spiflash_read_dummy_bits = 10
    spiflash_clock_div = 4
    spiflash_total_size = int((128/8)*1024*1024) # 128Mbit - 0x1000000
    spiflash_page_size = 256 #512 or 256 depending on part number
    spiflash_sector_size = 0x10000 #depending on device model and sector location this may be 4 KB, 64 KB or 256 KB

    def __init__(self):
        XilinxPlatform.__init__(self, "xc7a100t-CSG324-1", _io, toolchain="vivado")
        self.add_platform_command("set_property INTERNAL_VREF 0.750 [get_iobanks 34]")

    def create_programmer(self):
        return OpenOCD("openocd_xc7_ft2232.cfg", "bscan_spi_xc7a100t.bit")

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)
        self.add_period_constraint(self.lookup_request("clk100",             loose=True), 1e9/100e6)
        self.add_period_constraint(self.lookup_request("eth_clocks:ref_clk", loose=True), 1e9/50e6)
