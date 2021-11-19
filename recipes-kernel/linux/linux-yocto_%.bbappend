FILESEXTRAPATHS_prepend := '${THISDIR}:'
SRC_URI += "file://fragment.cfg \
	file://0001-added-zynqmp-zcu102-qemu.dts.patch \
	file://defconfig \
"

KBUILD_DEFCONFIG_qemuarm64-test ?= "defconfig"
#KBUILD_DEFCONFIG ?= "defconfig"
#KCONFIG_MODE="--alldefconfig"

