SUMMARY = "bitbake-layers recipe"
DESCRIPTION = "Hard key dummy"
LICENSE = "MIT"
LIC_FILES_CHKSUM="file:///${THISDIR}/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"
FILESEXTRAPATHS_prepend := '${THISDIR}:'
TARGET_CC_ARCH += "${LDFLAGS}"
SRC_URI += "file://hardkey.py \
	file://hardkey.c \
	file://hardkeytikinter.py \
	file://gpio.c \
	file://gpioset.c \
	file://sample.wav \
"

S = "${WORKDIR}"

do_compile() {
	${CC} hardkey.c -o hardkey
	${CC} gpio.c -o gpio
	${CC} gpioset.c -lgpiod -o gpioset
}


do_install() {
	install -m 755 -d "${D}/usr/local/bin"
	install -d "${D}/usr/local/bin"
	install -m 644 "${WORKDIR}/hardkey.py" "${D}/usr/local/bin"
	install -m 644 "${WORKDIR}/hardkeytikinter.py" "${D}/usr/local/bin"
	install -m 744 "${WORKDIR}/hardkey" "${D}/usr/local/bin"
	install -m 744 "${WORKDIR}/gpio" "${D}/usr/local/bin"
	install -m 744 "${WORKDIR}/gpioset" "${D}/usr/local/bin"
	install -m 744 "${WORKDIR}/sample.wav" "${D}/usr/local/bin"
}
DEPENDS = " libgpiod"
CFLAGS_append_  = " -lgpiod"
FILES_${PN} += "/usr/local/bin"



