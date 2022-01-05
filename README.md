# Gentoo-aarch64_be
A big endian Gentoo port developed on a Pine64.org RockPro64

The endian wars are over... little endian won. As a result, it is increasingly difficult to find systems that allow you to test for endian cleanliness...
I developed this port to facilitate testing of device drivers and general software on a big endian system. QEMU is another approach for big endian testing, however performance suffers greatly and many race conditions are harder to find. The RockPro64 platform is affordable and unlike other small ARM systems, it supports a PCIe slot for testing hardware add in cards! DISCLAIMER: I am not associated with Pine64 in any way other than as a satisfied customer.

This port has only been tested on the RockPro64 4GB board, however it likely will run on any ARM based system that can boot the Gentoo Arm64 installation CD image.

This repository will be populated over the next few weeks - there are several cleanup activities that I would like to complete before publishing.
