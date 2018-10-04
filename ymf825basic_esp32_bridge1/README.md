# ESP32 YMF825 サンプル (ESP32 YMF825 Sample)

[YMF825ボード](https://yamaha-webmusic.github.io/ymf825board/intro/)がESP32で動くように[YAMAHA公式サンプルコード](https://github.com/yamaha-webmusic/ymf825board)を改修したものです。
ymf825basic_esp32_bridge1はYMF825ボードを無改造で接続するボード(ymf825_bridge1)を使うバージョンです。

環境：
  - ESP32 ([WEMOS Lolin32](https://wiki.wemos.cc/products:lolin32:lolin32)で動作確認済み)
  - arduino-esp32 (Arudino IDE)
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


接続方法： ハードウェアSPI である VSPI または HSPI を利用します。ただしハードウェアCSは使用しません。（使用すると動作しません）

    VSPIの場合

      YMF825 - ESP32
      --------------
      RST_N  - GPIO 32   
      SS     - GPIO 5
      MOSI   - GPIO 23
      MISO   - GPIO 19
      SCK    - GPIO 18
      5V     - 5V
      3.3V   - 3.3V
      GND    - GND

    HSPIの場合

      YMF825 - ESP32
      --------------
      RST_N  - GPIO 32   
      SS     - GPIO 15
      MOSI   - GPIO 13
      MISO   - GPIO 12
      SCK    - GPIO 14
      5V     - 5V
      3.3V   - 3.3V
      GND    - GND

    Bridge1は信号レベル変換のイネーブル制御にIOを1つ使用します。

      Bridge1 - ESP32
      --------------
      OE      - GPIO 17

信号レベル変換について、YMF825は5Vモードで動作させ、ESP32との間にダイオードを挟むことで「5V->3.3Vの変換」＆「3.3VのHIGHはYMF825の許容範囲」の簡易変換でも動作するようです。しかし、データシートから5VモードのYMF825は4VでHIGHと解釈しましたので、個体によっては動作しない可能性を考慮し、確実性を取るためにレベル変換を使っています。


ライセンス：MIT


[YMF825 board](https://yamaha-webmusic.github.io/ymf825board/intro/) sample code for ESP32 platform.
This code is derived from 
[YAMAHA official sample code](https://github.com/yamaha-webmusic/ymf825board)
so that it works on ESP32 platform.
This version (ymf825basic_esp32_bridge1) is realized to use original single voltage YMF825 board.

System:
  - ESP32 (confirmed with [WEMOS Lolin32](https://wiki.wemos.cc/products:lolin32:lolin32))
  - arduino-esp32 (Arudino IDE)
  - YMF825_Bridge1 (3.3V <-> 5V level converter)
  - YMF825 board single voltage support (5V).

Wiring: This code uses VSPI or HSPI here (i.e. hardware SPI). Hardware CS is disabled, though, as it does not work well with YMF825 at this point.

    VSPI case

      YMF825 - ESP32
      --------------
      RST_N  - GPIO 32   
      SS     - GPIO 5
      MOSI   - GPIO 23
      MISO   - GPIO 19
      SCK    - GPIO 18
      5V     - 5V
      3.3V   - 3.3V
      GND    - GND

    HSPI case

      YMF825 - ESP32
      --------------
      RST_N  - GPIO 32   
      SS     - GPIO 15
      MOSI   - GPIO 13
      MISO   - GPIO 12
      SCK    - GPIO 14
      5V     - 5V
      3.3V   - 3.3V
      GND    - GND

    YMF825_Bridge1 requires 1 GPIO for enable pin.

      Bridge1 - ESP32
      --------------
      OE      - GPIO 17

License: MIT
