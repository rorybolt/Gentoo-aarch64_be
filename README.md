# Gentoo-aarch64_be
A big endian Gentoo port developed on a Pine64.org RockPro64

The endian wars are over... little endian won. As a result, it is increasingly difficult to find systems that allow you to test for endian cleanliness...
I developed this port to facilitate testing of device drivers and general software on a big endian system. QEMU is another approach for big endian testing, however performance suffers greatly and many race conditions are harder to find. The RockPro64 platform is affordable and unlike other small ARM systems, it supports a PCIe slot for testing hardware add in cards! DISCLAIMER: I am not associated with Pine64 in any way other than as a satisfied customer.

This port has only been tested on the RockPro64 4GB board, however it likely will run on any ARM based system that can boot the Gentoo Arm64 installation CD image.

This repository will be populated over the next few weeks - there are several cleanup activities that I would like to complete before publishing.

Stage3 tarball is now available.
Bootable image is now available.
Kernel runtime patches are now available.

Upcoming releases (in probable order)

  1) Stand alone GRUB EFI modules for mmcblk1 and sda
  2) Updated bootable images (all known grub issues now fixed!)
  3) GRUB patches (quite a lot)
  4) Big endian video support for RK3399

Since the GRUB changes are substantial and non-trivial, I will also release GRUB binaries preconfigured to boot from SDHC (mmcblk1) and sda. These will have two boot options, one for normal boot and one for an optional recovery boot. They will reference a (vmlinuz initrd.img) and (vmlinuz.recover initrd.recover.img) respectively. You will be able to build and install whatever kernel and initramfs you like as long as you rename it or link them to the generic names (e.g. vmlinuz and initrd.img) in /boot. Likewise you can also put in a recovery pair into /boot as long as they are named (vmlinuz.recover, initrd.recover.img).

