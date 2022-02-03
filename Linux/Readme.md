These are the changes needed to the linux source code to build a big endian kernel. I anticipate that these can be adopted by the main line kernel since they are quite small/reasonable.

For the most part the kernel is endian clean, however the Rockchip DRM video driver is not. I will get around to this as a very low priority. This means that for the time being, you <B>MUST</B> use a serial console so that you can configure sshd and user accounts to log in.

The reason for the Kconfig change is to have the generated kernel contain an EFI/PE/COFF header so that grub will load it. This also means your big endian kernel will have an embedded big endian efistub which is totally useless... but it is a small price to pay.

When the GRUB source changes (substantial) are posted, they will contain the changes necessary to the Linux efistub for use external to the kernel. If you use my prebuilt EFIBOOT binaries you will not need anything other than the changes in this directory.
