These are standalone EFI boot images that support booting either big endian or little endian kernels.

They assume that the root partition is the third partition of the device, and the EFI boot loader <b>MUST</b> be copied to the EFI/BOOT folder of the first partition, which <b>MUST</b> be formated as a vfat filesystem.
