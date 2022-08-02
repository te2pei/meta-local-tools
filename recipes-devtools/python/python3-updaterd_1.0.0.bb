SUMMARY = "Python Updater"
SECTION = "devel/python"
HOMEPAGE = ""
LICENSE = "MIT"
LIC_FILES_CHKSUM="file:///${COMMON_LICENSE_DIR}/eCos-2.0;md5=8c3ea41d02fa9c9253c692351e5940e7"

DEPENDS = "dbus"

FILESEXTRAPATHS_prepend := "${THISDIR}:"
SRC_URI_append += " file://updaterd-1.0.0.tar.gz \
                    file://updaterd.service \
                    file://updaterd.conf \
 "

S = "${WORKDIR}/updaterd-${PV}"

PYPI_PACKAGE = "updaterd"
#inherit distutils3-base autotools pkgconfig

# documentation needs python3-sphinx, which is not in oe-core or meta-python for now
# change to use PACKAGECONFIG when python3-sphinx is added to oe-core
#EXTRA_OECONF += "--disable-documentation"

RDEPENDS_${PN} += " python3-pydbus python3-logging python3-xml \
    sqlite3 \
"

SYSTEMD_SERVICE_${PN} = "updaterd.service"

do_install () {
    install -d ${D}${libdir}/${PYTHON_DIR}site-packages/${PYPI_PACKAGE}
    install -m 644 ${S}/${PYPI_PACKAGE}/* ${D}${libdir}/${PYTHON_DIR}site-packages/${PYPI_PACKAGE}/


    install -d ${D}${sysconfdir}/${PYPI_PACKAGE}/
    install -d ${D}${systemd_system_unitdir}

    install -m 0644 ${WORKDIR}/updaterd.conf ${D}${sysconfdir}/${PYPI_PACKAGE}/
    install -m 0644 ${WORKDIR}/updaterd.service ${D}${systemd_system_unitdir}

}

FILES_${PN} += " \
    /usr/* \
    /lib/* \
"
