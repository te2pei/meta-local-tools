SRC_URI += "git://github.com/te2pei/qemu-5.2.0.git;protocol=https;branch=main;destsuffix=${BPN}-${PV}"
SRC_URI_remove = "https://download.qemu.org/${BPN}-${PV}.tar.xz"
SRCREV = "${AUTOREV}"
