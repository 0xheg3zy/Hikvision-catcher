A simple Hikvision detector to know the details of camera exists on your lan.

## Usage :
Just run 
```bash
kali@kali~$ python main.py
```
Output :
```
Searching for Hikvision devices...

Found device:
  IP: 192.168.1.200
  Model: DS-7204*****
  Serial: DS-7204**********38159WCVU
  Firmware: V4.30.301build 210423
  DSP: V5.0, build 210412
----------------------------------------
```

If you want to know more details, uncommit L55 to print more data
