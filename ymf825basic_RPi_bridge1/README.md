# RaspberryPi YMF825 サンプル (RaspberryPi YMF825 Sample)

[YMF825ボード](https://yamaha-webmusic.github.io/ymf825board/intro/)がRaspberryPiで動くように[YAMAHA公式サンプルコード](https://github.com/yamaha-webmusic/ymf825board)を改修したものです。
ymf825basic_RPi_bridge1はYMF825ボードを無改造で接続するボード(ymf825_bridge1)を使うバージョンです。

環境：
  - RaspberryPi ([RaspberryPi3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)で動作確認済み)
  - Python 2.7
  - pigpio (http://abyz.me.uk/rpi/pigpio/)
  - YMF825_Bridge1 (3.3V <-> 5V信号レベル変換)
  - YMF825ボードは無改造のものを使います。

<a href="https://raw.github.com/ywabiko/esp32/master/images/ESP32_YMF825_VSPI.jpg">
<img src="https://raw.github.com/ywabiko/esp32/master/images/ESP32_YMF825_VSPI.jpg"
 alt="ESP32_YMF825_VSPI" title="ESP32_YMF825_VSPI" width="300" />
</a>
<a href="https://raw.github.com/ywabiko/esp32/master/images/ESP32_YMF825_HSPI.jpg">
<img src="https://raw.github.com/ywabiko/esp32/master/images/ESP32_YMF825_HSPI.jpg"
 alt="ESP32_YMF825_HSPI" title="ESP32_YMF825_HSPI" width="300" />
</a>


接続方法： ハードウェアCSは使用しません。

      YMF825 - RPi
      --------------
      RST_N  - GPIO 23(pin#16)
      SS     - GPIO 8(pin#24)
      MOSI   - MOSI (pin#19)
      MISO   - MISO (pin#21)
      SCK    - SCLK (pin#23)
      5V     - 5V
      3.3V   - 3.3V
      GND    - GND

    Bridge1は信号レベル変換のイネーブル制御にIOを1つ使用します。

      Bridge1 - RPi
      --------------
      OE      - GPIO 24(pin#18)

信号レベル変換について、YMF825は5Vモードで動作させ、RPiとの間にダイオードを挟むことで「5V->3.3Vの変換」＆「3.3VのHIGHはYMF825の許容範囲」の簡易変換でも動作するようです。しかし、データシートから5VモードのYMF825は4VでHIGHと解釈しましたので、個体によっては動作しない可能性を考慮し、確実性を取るためにレベル変換を使っています。


ライセンス：MIT


[YMF825 board](https://yamaha-webmusic.github.io/ymf825board/intro/) sample code for RPi platform.
This code is derived from 
[YAMAHA official sample code](https://github.com/yamaha-webmusic/ymf825board)
so that it works on RPi platform.
This version (ymf825basic_RPi_bridge1) is realized to use original single voltage YMF825 board.

System:
  - RaspberryPi (confirmed with [RaspberryPi3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/))
  - Python 2.7
  - pigpio (http://abyz.me.uk/rpi/pigpio/)
  - YMF825_Bridge1 (3.3V <-> 5V level converter)
  - YMF825 board single voltage support (5V).

Wiring: Hardware CS is disabled, though, as it does not work well with YMF825 at this point.

      YMF825 - RPi
      --------------
      RST_N  - GPIO 23(pin#16)
      SS     - GPIO 8(pin#24)
      MOSI   - MOSI (pin#19)
      MISO   - MISO (pin#21)
      SCK    - SCLK (pin#23)
      5V     - 5V
      3.3V   - 3.3V
      GND    - GND

    YMF825_Bridge1 requires 1 GPIO for enable pin.

      Bridge1 - ESP32
      --------------
      OE      - GPIO 17

License: MIT
