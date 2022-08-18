# samsung-modbus-mim-b19n

Example python script to read and write data to a Samsung Heat Pump or HVAC unit using a [MIM-B19N Modbus module](https://www.samsung.com/uk/support/model/MIM-B19N/)

## Tested with:

- AE050RXYDEG-EU Gen6 ASHP
- Raspberry Pi with [USB Modbus reader](https://shop.openenergymonitor.com/modbus-rs485-to-usb-adaptor/)
- Python 3


## Install python module

```
$ pip3 install minimalmodbus
```

## Run with


```
$ python3 samsung-modbus.py
```

## Example output

```
Central heating status: 0
Target indoor temp: 21.0
Indoor temp: 22.7
Target flow temp: 25.0
Flow temp: 32.7
Return temp: 33.6
DHW status: 1
DHW target temp: 55.0
DHW temp: 49.8
Away mode status: 0
```

## Control commands

Write / controll comands can be activated by un-commenting them.

## Next setps

- Integrated this into a [EmonHub](https://github.com/openenergymonitor/emonhub) interfacer module to log the data to MQTT and [Emoncms](https://github.com/emoncms/emoncms)
- Home Assistant integration? (can anyone help with this?)
- NodeRED module? (can anyone help with this?)





