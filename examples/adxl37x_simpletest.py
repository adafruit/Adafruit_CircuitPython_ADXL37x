# SPDX-FileCopyrightText: Copyright (c) 2022 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time

import board

import adafruit_adxl37x

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
accelerometer = adafruit_adxl37x.ADXL375(i2c)

while True:
    print(
        f"{accelerometer.acceleration[0]} {accelerometer.acceleration[1]} {accelerometer.acceleration[2]} m/s^2"  # noqa: E501
    )
    time.sleep(0.2)
