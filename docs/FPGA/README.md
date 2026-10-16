# FPGA Lab (ALINX AX7035B)

An [ALINX AX7035B](https://www.en.alinx.com/Product/FPGA-Development-Boards/Artix-7/AX7035B.html) Artix-7 board attached to **Entrypoint**, used to learn VHDL. A VM on Entrypoint runs Vivado and gets the board's USB devices through passthrough. A USB relay that Entrypoint controls switches the board's power.

> [!NOTE]
> Work in progress: the VM and the relay are not set up yet.

<img src="https://github.com/Promete04/homelab/blob/main/pictures/Setup/fgpa.jpeg" width=300>

## Board

- **FPGA**: Xilinx Artix-7 XC7A35T-2FGG484I
- **Memory**: 256MB DDR3 + 16MB QSPI Flash
- **I/O**: Gigabit Ethernet, HDMI in/out, USB 2.0, microSD, 2x 40-pin expansion ports, 7-segment display, LEDs, keys
- **Power**: DC 5V barrel jack (CN1) with on-board switch (SW1)
- **Programming**: ALINX USB JTAG cable
- **Serial**: CP2102 USB-UART (mini USB)
- [User manual](https://botland.store/img/cms/products_29038/AX7035B%20_User_Manual.pdf)

## Power control

The 5V adapter feeds the board through a 1-channel USB relay module (CH340, "LCUS-1" type) instead of plugging in directly.

The relay stays on the **Proxmox host**, not in the VM, so the board can be power-cycled even when the VM is down.

### Host setup

Files are in [`docs/Scripts/FPGA`](../Scripts/FPGA):

```bash
cp 99-fpga-relay.rules /etc/udev/rules.d/
udevadm control --reload && udevadm trigger
install -m 755 fpga-power /usr/local/bin/

fpga-power on | off | cycle
```

From inside the VM: `ssh root@entrypoint fpga-power cycle`.

## VM
- **USB passthrough** by vendor:product ID, so it survives replugs:
  ```bash
  qm set <vmid> -usb0 host=<jtag-vid:pid> -usb1 host=10c4:ea60
  ```
- Run Vivado's `install_drivers` script inside the VM so the JTAG cable is detected.
