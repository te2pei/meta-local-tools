SUMMARY = "bitbake-layers recipe"
DESCRIPTION = "Hard key dummy"
LICENSE = "MIT"
LIC_FILES_CHKSUM="file:///${THISDIR}/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"
FILESEXTRAPATHS_prepend := '${THISDIR}:'
TARGET_CC_ARCH += "${LDFLAGS}"
SRC_URI += "file://hardkey.py \
	file://hardkey.c \
	file://hardkeytikinter.py "

S = "${WORKDIR}"

python do_display_banner() {
    bb.plain("***********************************************");
    bb.plain("*                                             *");
    bb.plain("*  Example recipe created by bitbake-layers   *");
    bb.plain("*                                             *");
    bb.plain("***********************************************");
}

do_compile() {
	${CC} hardkey.c -o hardkey
}


do_install() {
	install -m 755 -d "${D}/usr/local/bin"
	install -d "${D}/usr/local/bin"
	install -m 644 "${WORKDIR}/hardkey.py" "${D}/usr/local/bin"
	install -m 644 "${WORKDIR}/hardkeytikinter.py" "${D}/usr/local/bin"
	install -m 744 "${WORKDIR}/hardkey" "${D}/usr/local/bin"
}
FILES_${PN} += "/usr/local/bin"

addtask display_banner before do_build
