# UPDATED to latest GRUB EFI and kernel 5.16.5

**This image REQUIRES a serial console.**

**<s>Due to big endian errors in RK3399 driver, some systems will not boot with monitors attached.</s> FIXED**

Due to Github size limits, I have posted a link to the bootable image on my Google Drive folder

The Rockchip 3399 video driver is NOT endian clean so there is no video support for now.
This bootable image was created for a RockPro64 board, but it really should work on
just about any Arm SBC that can boot the Gentoo Arm64 installation CD. The only issue
I anticipate is that you may have to change device names in /etc/fstab and /etc/inittab 
within the root partition of the bootable image and then making the corresponding 
in GRUB by pressing 'e' to edit the GRUB configuration during the 5 second boot delay.

There will be a delay in releasing the rest of the sources as I clean them up.
There are minor changes to the kernel, and pretty big changes to GRUB.
