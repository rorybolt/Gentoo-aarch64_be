<B>This image REQUIRES a serial console.</B>

Due to Github size limits, I have posted a link to the bootable image on my Google Drive folder

The Rockchip 3399 video driver is NOT endian clean so there is no video support for now.
This bootable image was created for a RockPro64 board, but it really should work on
just about any Arm SBC that can boot the Gentoo Arm64 installation CD. The only issue
I anticipate is that you may have to change device names in /etc/fstab and by pressing 
'e' to edit the GRUB configuration during the 5 second boot delay.

There will be a delay in releasing the rest of the sources as I clean them up.
There are minor changes to the kernel, and pretty big changes to GRUB.
