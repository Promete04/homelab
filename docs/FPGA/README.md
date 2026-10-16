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

The 5V adapter feeds the board through a 1-channel USB relay module (CH340, "LCUS-1" type) instead of plugging in directly:

```
5V adapter (+) ──► relay COM ──► relay NO ──► board (+)
5V adapter (−) ─────────────────────────────► board (−)
```

- The relay switches only the **low-voltage 5V side**. No mains wiring.
- **NO** (normally open) means the board stays off if Entrypoint reboots or the relay loses USB.
- **SW1 stays on** permanently, so the relay is the only power switch.

The relay stays on the **Proxmox host**, not in the VM, so the board can be power-cycled even when the VM is down.

| Device | USB ID | Goes to |
|---|---|---|
| ALINX JTAG cable | check with `lsusb` | FPGA VM (passthrough) |
| CP2102 UART | `10c4:ea60` | FPGA VM (passthrough) |
| CH340 relay | `1a86:7523` | Proxmox host |

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

- **Software**: Vivado ML Standard (free, supports the XC7A35T). Install only Artix-7 support (~40-60GB). Skip Vitis for now; it's only needed for C on a MicroBlaze soft-core.
- **Resources**: ~6-8GB RAM. Entrypoint's 16GB is shared with Home Assistant and the LXCs.
- **USB passthrough** by vendor:product ID, so it survives replugs:
  ```bash
  qm set <vmid> -usb0 host=<jtag-vid:pid> -usb1 host=10c4:ea60
  ```
- Run Vivado's `install_drivers` script inside the VM so the JTAG cable is detected.
