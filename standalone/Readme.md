These are standalone EFI boot images that support booting either big endian or little endian kernels. The folders contain versions corresponding to the device name of the boot device (e.g. whether you are installing/booting on /dev/mmcblk1 or /dev/sda).

They assume that the root partition is the third partition of the device, and the EFI boot image <b>MUST</b> be copied to the EFI/BOOT folder of the first partition, which <b>MUST</b> be formated as a vfat filesystem.

These will have two boot options, one for normal boot and one for an optional recovery boot. They will reference a (vmlinuz initrd.img) and (vmlinuz.recover initrd.recover.img) respectively. You will be able to build and install whatever kernel and initramfs you like as long as you rename it or link them to the generic names (e.g. vmlinuz and initrd.img) in /boot. Likewise you can also put in a recovery pair into /boot as long as they are named (vmlinuz.recover, initrd.recover.img).
