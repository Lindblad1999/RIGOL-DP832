# RIGOL-DP832
Connection and data-logging from 2 RIGOL DP832 Power supplies

## Requirements

```bash
pip install pyvisa-py
```
```bash
pip install schedule
```
```bash
sudo apt-get -y install python3-usb
```

## pyvisa problems
```python
rm = pyvisa.ResourceManager()
print(rm.list_resources())
```
If device is connected, but no device is found, or if an error occurs that says no device found, do the following:

Become root:
```bash
sudo -i
```

Open the following file:
```bash
nano /etc/udev/rules.d/99-com.rules
```
And enter the following, and save:
```bash
SUBSYSTEM=="usb", MODE="0666", GROUP="usbusers"
```

Run the following command:
```bash
cp  /etc/udev/rules.d/99-com.rules  /etc/udev/rules.d/99-com.rules.BAK
```

And restart udev:
```bash
/etc/init.d/udev  restart
```

Create the 'usbusers' group:
```bash
sudo groupadd usbusers
```
And add yourself to the group:
```bash
sudo usermod -a -G usbusers USERNAME
```

Finally reboot PC...

Solution found [here](https://stackoverflow.com/questions/52256123/unable-to-get-full-visa-address-that-includes-the-serial-number)
