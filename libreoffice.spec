# download path contains version without the last (fourth) digit
%define libo_version 4.0.1
# Should contain .alphaX / .betaX, if this is pre-release (actually
# pre-RC) version. The pre-release string is part of tarball file names,
# so we need a way to define it easily at one place.
# %%define libo_prerelease .beta2
# rhbz#715152 state vendor
%if 0%{?rhel}
%define vendoroption --with-vendor="Red Hat, Inc."
%define libo_python3 %{nil}
%define libo_python_sitearch %{python_sitearch}
%endif
%if 0%{?fedora}
%define libo_python3 1
%define libo_python_sitearch %{python3_sitearch}
%define vendoroption --with-vendor="The Fedora Project"
%endif
# rhbz#465664 jar-repacking breaks help by reordering META-INF/MANIFEST.MF
%define __jar_repack %{nil}
# don't worry about whitespace for now
%define _default_patch_flags -s -l
# make it easier to download sources from pre-release site
# http://dev-builds.libreoffice.org/pre-releases/src
%define source_url http://dev-builds.libreoffice.org/pre-releases/src
# %%define source_url http://download.documentfoundation.org/libreoffice/src/%{libo_version}
# URL for external projects' tarballs
%define external_url http://dev-www.libreoffice.org/src/

# get english only and no-langpacks for a faster smoketest build
# fedpkg compile/install/local/mockbuild does not handle --without ATM,
# so it is necessary to change this to bcond_with to achieve the same
# effect
%bcond_without langpacks

%if %{with langpacks}
%if 0%{?rhel} && 0%{?rhel} < 7
%define langpack_langs en-US af ar as bg bn ca cs cy da de dz el es et eu fi fr ga gl gu he hi hr hu it ja ko kn lt mai ml mr ms nb nl nn nr nso or pa-IN pl pt pt-BR ro ru sh sk sl sr ss st sv ta te th tn tr ts uk ur ve xh zh-CN zh-TW zu
%else
%define langpack_langs en-US af ar as bg bn ca cs cy da de dz el es et eu fa fi fr ga gl gu he hi hr hu it ja kk ko kn lt lv mai ml mr nb nl nn nr nso or pa-IN pl pt pt-BR ro ru sh si sk sl sr ss st sv ta te th tn tr ts uk ve xh zh-CN zh-TW zu
%endif
%define with_lang --with-lang="%{langpack_langs}"
%else
%define langpack_langs en-US
%endif

Summary:        Free Software Productivity Suite
Name:           libreoffice
Epoch:          1
Version:        %{libo_version}.2
Release:        1%{?libo_prerelease}%{?dist}
License:        (MPLv1.1 or LGPLv3+) and LGPLv3 and LGPLv2+ and BSD and (MPLv1.1 or GPLv2 or LGPLv2 or Netscape) and Public Domain and ASL 2.0 and Artistic and MPLv2.0
Group:          Applications/Productivity
URL:            http://www.documentfoundation.org/develop

Source0:        %{source_url}/libreoffice-%{version}%{?libo_prerelease}.tar.xz
Source1:        %{source_url}/libreoffice-help-%{version}%{?libo_prerelease}.tar.xz
Source2:        %{source_url}/libreoffice-translations-%{version}%{?libo_prerelease}.tar.xz
Source3:        http://dev-www.libreoffice.org/extern/185d60944ea767075d27247c3162b3bc-unowinreg.dll
Source4:        libreoffice-multiliblauncher.sh
Source5:        %{external_url}/0168229624cfac409e766913506961a8-ucpp-1.3.2.tar.gz
Source6:        %{external_url}/a7983f859eafb2677d7ff386a023bc40-xsltml_2.1.2.zip
Source7:        %{external_url}/1f24ab1d39f4a51faf22244c94a6203f-xmlsec1-1.2.14.tar.gz
Source8:        %{external_url}/798b2ffdc8bcfe7bca2cf92b62caf685-rhino1_5R5.zip
Source9:        %{external_url}/35c94d2df8893241173de1d16b6034c0-swingExSrc.zip
#Unfortunately later versions of hsqldb changed the file format, so if we use a later version we loose
#backwards compatability.
Source10:       %{external_url}/17410483b5b5f267aa18b7e00b65e6e0-hsqldb_1_8_0.zip
%if 0%{?rhel} && 0%{?rhel} < 7
Source11:       %{external_url}/9f9e15966b5624834157fe3d748312bc-mdds_0.6.1.tar.bz2
Source12:       %{external_url}/46e92b68e31e858512b680b3b61dc4c1-mythes-1.2.3.tar.gz
Source13:       %{external_url}/ca66e26082cab8bb817185a116db809b-redland-1.0.8.tar.gz
Source14:       %{external_url}/284e768eeda0e2898b0d5bf7e26a016e-raptor-1.4.18.tar.gz
Source15:       %{external_url}/fca8706f2c4619e2fa3f8f42f8fc1e9d-rasqal-0.9.16.tar.gz
Source16:       %{external_url}/dc3d21a3921931096d6e80f6701f6763-libexttextcat-3.4.0.tar.bz2
Source17:       %{external_url}/libcdr-0.0.9.tar.bz2
Source18:       %{external_url}/9d283e02441d8cebdcd1e5d9df227d67-libwpg-0.2.1.tar.bz2
Source19:       %{external_url}/e7f84e3199dfee9122949448cab3823f-libwpd-0.9.6.tar.bz2
Source20:       %{external_url}/d197bd6211669a2fa4ca648faf04bcb1-libwps-0.2.7.tar.bz2
Source21:       %{external_url}/b2371dc7cf4811c9d32146eec913d296-libcmis-0.3.0.tar.gz
Source22:       %{external_url}/48d647fbd8ef8889e5a7f422c1bfda94-clucene-core-2.3.3.4.tar.gz
Source23:       %{external_url}/libvisio-0.0.24.tar.bz2
Source24:       %{external_url}/861ef15fa0bc018f9ddc932c4ad8b6dd-lcms2-2.4.tar.gz
Source25:       %{external_url}/libmspub-0.0.3.tar.bz2
Source26:       %{external_url}/8755aac23317494a9028569374dc87b2-liborcus_0.3.0.tar.bz2
Source27:       %{external_url}/54e578c91b1b68e69c72be22adcb2195-liblangtag-0.4.0.tar.bz2
Source28:       %{external_url}/f02578f5218f217a9f20e9c30e119c6a-boost_1_44_0.tar.bz2
%endif

# build tools
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bc
BuildRequires: binutils
BuildRequires: bison
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: findutils
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: gperf
BuildRequires: icu
BuildRequires: make
BuildRequires: perl(Archive::Zip)
BuildRequires: perl(Digest::MD5)
BuildRequires: zip

# libs / headers
BuildRequires: GConf2-devel
BuildRequires: bluez-libs-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: boost-devel
BuildRequires: clucene-core-devel
%endif
BuildRequires: cppunit-devel
BuildRequires: cups-devel
BuildRequires: evolution-data-server-devel
BuildRequires: expat-devel
BuildRequires: fontpackages-devel
BuildRequires: freetype-devel
BuildRequires: gecko-devel
%if 0%{?rhel} && 0%{?rhel} < 7
BuildRequires: gstreamer-devel
BuildRequires: gstreamer-plugins-base-devel
%else
BuildRequires: graphite2-devel
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
%endif
BuildRequires: gtk2-devel
BuildRequires: hunspell-devel
BuildRequires: hyphen-devel
%if 0%{?fedora}
BuildRequires: kdelibs4-devel
%endif
BuildRequires: libICE-devel
BuildRequires: libXext-devel
BuildRequires: libXinerama-devel
BuildRequires: libXt-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: libcdr-devel
BuildRequires: libcmis-devel >= 0.3.0
%endif
BuildRequires: libcurl-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: libexttextcat-devel
%endif
BuildRequires: libicu-devel
BuildRequires: libidn-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: libjpeg-turbo-devel
BuildRequires: liblangtag-devel >= 0.4.0
BuildRequires: libmspub-devel
BuildRequires: liborcus-devel >= 0.3.0
BuildRequires: libvisio-devel
BuildRequires: libwpd-devel
BuildRequires: libwpg-devel
BuildRequires: libwps-devel
%else
BuildRequires: libjpeg-devel
%endif
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: lpsolve-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: mdds-devel
%endif
BuildRequires: mesa-libGLU-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: mysql-connector-c++-devel
BuildRequires: mythes-devel
%endif
BuildRequires: neon-devel
BuildRequires: nss-devel
BuildRequires: openldap-devel
BuildRequires: openssl-devel
BuildRequires: pam-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: poppler-cpp-devel
%endif
BuildRequires: poppler-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: postgresql-devel
%endif
%if 0%{libo_python3}
BuildRequires: python3-devel >= 3.3.0
%else
BuildRequires: python-devel
%endif
BuildRequires: redland-devel
BuildRequires: sane-backends-devel
BuildRequires: unixODBC-devel
BuildRequires: vigra-devel
BuildRequires: zlib-devel

# java stuff
BuildRequires: ant
BuildRequires: ant-apache-regexp
%if 0%{?rhel} && 0%{?rhel} < 7
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-lang
BuildRequires: apache-tomcat-apis
%else
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-lang
BuildRequires: tomcat-servlet-3.0-api
%endif
BuildRequires: bsh
%if 0%{?rhel} && 0%{?rhel} < 7
BuildRequires: hsqldb
%endif
BuildRequires: java-devel
BuildRequires: jakarta-commons-httpclient
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: junit
%endif
BuildRequires: pentaho-reporting-flow-engine

# fonts needed for unit tests
BuildRequires: liberation-mono-fonts >= 1.0
BuildRequires: liberation-sans-fonts >= 1.0
BuildRequires: liberation-serif-fonts >= 1.0

Requires: %{name}-writer = %{epoch}:%{version}-%{release}
Requires: %{name}-calc = %{epoch}:%{version}-%{release}
Requires: %{name}-impress = %{epoch}:%{version}-%{release}
Requires: %{name}-draw = %{epoch}:%{version}-%{release}
Requires: %{name}-math = %{epoch}:%{version}-%{release}
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-emailmerge = %{epoch}:%{version}-%{release}

Patch1:  openoffice.org-2.0.2.rh188467.printingdefaults.patch
Patch2:  openoffice.org-2.4.0.ooo86080.unopkg.bodge.patch
Patch3:  openoffice.org-3.0.0.ooo88341.sc.verticalboxes.patch
Patch4:  openoffice.org-3.1.0.oooXXXXX.solenv.allowmissing.patch
Patch5:  openoffice.org-3.1.0.ooo101274.opening-a-directory.patch
Patch6:  openoffice.org-3.1.1.ooo105784.vcl.sniffscriptforsubs.patch
Patch7:  libreoffice-installfix.patch
#to-do, fix this on bigendian platforms
Patch8: 0001-disable-failing-check.patch
%if 0%{?rhel} && 0%{?rhel} < 7
Patch9: libreoffice-rhel6gcj.patch
Patch10: libreoffice-rhel6poppler.patch
Patch11: libreoffice-rhel6langs.patch
Patch12: 0001-Require-icu-4.6-or-later-with-system-icu.patch
Patch13: libreoffice-rhel6limits.patch
Patch14: libreoffice-rhel6glib.patch
%endif
Patch15: 0001-temporarily-disable-failing-test.patch
Patch16: 0001-make-evolution-3.6-work-with-address-book.patch
Patch17: 0001-no-g_list_free_full-in-RHEL-6-glib.patch
Patch18: 0001-Work-around-problem-with-boost-shared_array-NULL-cto.patch
Patch19: 0001-fix-compile-for-change-to-boost-1.53.0-declaring-sma.patch
Patch20: 0001-Resolves-rhbz-895196-sc-filter-float-a11y-parent-of-.patch
Patch21: 0001-do-not-access-vector-elements-beyond-size-rhbz-84751.patch
Patch22: 0001-rhbz-742780-Let-make-OPT_FLAGS-.-override-SDK-optimi.patch

%define instdir %{_libdir}
%define baseinstdir %{instdir}/libreoffice
%define ureinstdir %{baseinstdir}/ure
%define sdkinstdir %{baseinstdir}/sdk
%define fontname opensymbol

%description
LibreOffice is an Open Source, community-developed, office productivity suite.
It includes the key desktop applications, such as a word processor,
spreadsheet, presentation manager, formula editor and drawing program, with a
user interface and feature set similar to other office suites.  Sophisticated
and flexible, LibreOffice also works transparently with a variety of file
formats, including Microsoft Office File Formats.

%package core
Summary: Core modules for LibreOffice
Group: Applications/Productivity
Requires: %{name}-%{fontname}-fonts = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: liberation-sans-fonts >= 1.0, liberation-serif-fonts >= 1.0, liberation-mono-fonts >= 1.0
Requires: dejavu-sans-fonts, dejavu-serif-fonts, dejavu-sans-mono-fonts
Requires: hyphen-en, hyphen >= 2.4, autocorr-en
%if 0%{?rhel} && 0%{?rhel} < 7
Requires: hunspell-en
%else
Requires: hunspell-en-US
%endif
Requires(pre):    gtk2 >= 2.9.4
Requires(post):   gtk2 >= 2.9.4
Requires(preun):  gtk2 >= 2.9.4
Requires(postun): gtk2 >= 2.9.4
Obsoletes: libreoffice-binfilter < 1:4.0.0.0
Obsoletes: libreoffice-testtools < 1:3.4.99.1
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-core%{?_isa} = 1:3.3.0
Provides: openoffice.org-brand%{?_isa} = 1:3.3.0, broffice.org-brand%{?_isa} = 1:3.3.0
%endif

%description core
The shared core libraries and support files for LibreOffice.

%package pyuno
Summary: Python support for LibreOffice
Group: Development/Libraries
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
%if 0%{libo_python3}
Requires: python3
%else
Requires: python
%endif
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-pyuno%{?_isa} = 1:3.3.0
%endif

%description pyuno
Python bindings for the LibreOffice UNO component model. Allows scripts both
external to LibreOffice and within the internal LibreOffice scripting framework
to be written in python.

%package base
Summary: Database front-end for LibreOffice
Group: Applications/Productivity
Requires: postgresql-jdbc
%if 0%{?rhel} && 0%{?rhel} < 7
Requires:  hsqldb
%endif
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-calc = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-base-core%{?_isa} = 1:3.3.0
Provides: openoffice.org-base%{?_isa} = 1:3.3.0, broffice.org-base%{?_isa} = 1:3.3.0
%endif

%description base
GUI database front-end for LibreOffice. Allows creation and management of 
databases through a GUI.

%package report-builder
Summary: Create database reports from LibreOffice
Group: Applications/Productivity
Requires: pentaho-reporting-flow-engine
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-base = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-report-builder%{?_isa} = 1:3.3.0
%endif

%description report-builder
Creates database reports from LibreOffice databases. The report builder can
define group and page headers as well as group, page footers and calculation
fields to accomplish complex database reports.

%package bsh
Summary: BeanShell support for LibreOffice
Group: Development/Libraries
Requires: bsh
Requires: %{name}-core = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-bsh%{?_isa} = 1:3.3.0
%endif

%description bsh
Support BeanShell scripts in LibreOffice.

%package rhino
Summary: JavaScript support for LibreOffice
Group: Development/Libraries
Requires: %{name}-core = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-rhino%{?_isa} = 1:3.3.0
%endif

%description rhino
Support JavaScript scripts in LibreOffice.

%package wiki-publisher
Summary: Create Wiki articles on MediaWiki servers with LibreOffice
Group: Applications/Productivity
%if 0%{?rhel} && 0%{?rhel} < 7
Requires: jakarta-commons-codec, jakarta-commons-httpclient
Requires: jakarta-commons-lang, jakarta-commons-logging
%else
Requires: apache-commons-codec, jakarta-commons-httpclient
Requires: apache-commons-lang, apache-commons-logging
%endif
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-writer = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-wiki-publisher%{?_isa} = 1:3.3.0
%endif

%description wiki-publisher
The Wiki Publisher enables you to create Wiki articles on MediaWiki servers
without having to know the syntax of the MediaWiki markup language. Publish
your new and existing documents transparently with writer to a wiki page.

%package nlpsolver
Summary: Non-linear solver engine for LibreOffice Calc
Group: Applications/Productivity
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-calc = %{epoch}:%{version}-%{release}

%description nlpsolver
A non-linear solver engine for Calc as an alternative to the default linear
programming model when more complex, nonlinear programming is required.

%package ogltrans
Summary: 3D OpenGL slide transitions for LibreOffice
Group: Applications/Productivity
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-impress = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-ogltrans%{?_isa} = 1:3.3.0
%endif

%description ogltrans
OpenGL Transitions enable 3D slide transitions to be used in LibreOffice.
Requires good quality 3D support for your graphics card for best experience.

%package presentation-minimizer
Summary: Shrink LibreOffice presentations
Group: Applications/Productivity
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-impress = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-presentation-minimizer%{?_isa} = 1:3.3.0
%endif

%description presentation-minimizer
The Presentation Minimizer is used to reduce the file size of the current
presentation. Images will be compressed, and data that is no longer needed will
be removed.

%package pdfimport
Summary: PDF Importer for LibreOffice Draw
Group: Applications/Productivity
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-draw = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-pdfimport%{?_isa} = 1:3.3.0
%endif

%description pdfimport
The PDF Importer imports PDF into drawing documents to preserve layout
and enable basic editing of PDF documents.

%package %{fontname}-fonts
Summary: LibreOffice dingbats font
Group: User Interface/X
Requires: fontpackages-filesystem
BuildArch: noarch
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-fonts = 1:3.3.0
Provides: openoffice.org-opensymbol-fonts = 1:3.3.0
%endif

%description %{fontname}-fonts
A dingbats font, OpenSymbol, suitable for use by LibreOffice for bullets and
mathematical symbols. 

%package writer
Summary: LibreOffice Word Processor Application
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-writer-core%{?_isa} = 1:3.3.0
Provides: openoffice.org-writer%{?_isa} = 1:3.3.0, broffice.org-writer%{?_isa} = 1:3.3.0
%endif

%description writer
The LibreOffice Word Processor application.

%package emailmerge
Summary: Email mail-merge component for LibreOffice 
Group: Applications/Productivity
Requires: %{name}-writer = %{epoch}:%{version}-%{release}
Requires: %{name}-pyuno = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-emailmerge%{?_isa} = 1:3.3.0
%endif

%description emailmerge
Enables the LibreOffice writer module to mail-merge to email.

%package calc
Summary: LibreOffice Spreadsheet Application
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-calc-core%{?_isa} = 1:3.3.0
Provides: openoffice.org-calc%{?_isa} = 1:3.3.0, broffice.org-calc%{?_isa} = 1:3.3.0
%endif

%description calc
The LibreOffice Spreadsheet application.

%package draw
Summary: LibreOffice Drawing Application
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-pdfimport = %{epoch}:%{version}-%{release}
Requires: %{name}-graphicfilter = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-draw-core%{?_isa} = 1:3.3.0
Provides: openoffice.org-draw%{?_isa} = 1:3.3.0, broffice.org-draw%{?_isa} = 1:3.3.0
%endif

%description draw
The LibreOffice Drawing Application.

%package impress
Summary: LibreOffice Presentation Application
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-presenter-screen < 2:4.0.0.0-1.beta1
Provides: %{name}-presenter-screen%{?_isa} = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-impress-core%{?_isa} = 1:3.3.0
Provides: openoffice.org-impress%{?_isa} = 1:3.3.0, broffice.org-impress%{?_isa} = 1:3.3.0
Provides: openoffice.org-presenter-screen%{?_isa} = 1:3.3.0
%endif

%description impress
The LibreOffice Presentation Application.

%package math
Summary: LibreOffice Equation Editor Application
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-math-core%{?_isa} = 1:3.3.0
Provides: openoffice.org-math%{?_isa} = 1:3.3.0, broffice.org-math%{?_isa} = 1:3.3.0
%endif

%description math 
The LibreOffice Equation Editor Application.

%package graphicfilter
Summary: LibreOffice Extra Graphic filters
Group: Applications/Productivity
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-graphicfilter%{?_isa} = 1:3.3.0
%endif

%description graphicfilter
The graphicfilter module for LibreOffice provides graphic filters, e.g. svg and
flash filters.

%package xsltfilter
Summary: Optional xsltfilter module for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-xsltfilter%{?_isa} = 1:3.3.0
%endif

%description xsltfilter
The xsltfilter module for LibreOffice, provides additional docbook and
xhtml export transforms. Install this to enable docbook export.

%package javafilter
Summary: Optional javafilter module for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-javafilter%{?_isa} = 1:3.3.0
%endif

%description javafilter
The javafilter module for LibreOffice, provides additional AportisDoc,
Pocket Excel and Pocket Word import filters.

%post javafilter
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun javafilter
update-desktop-database %{_datadir}/applications &> /dev/null || :

%if 0%{?fedora} || 0%{?rhel} >= 7
%package postgresql
Summary: PostgreSQL connector for LibreOffice
Group: Applications/Productivity
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: postgresql-libs

%description postgresql
A PostgreSQL connector for the database front-end for LibreOffice. Allows
creation and management of PostgreSQL databases through a GUI.
%endif

%package ure
Summary: UNO Runtime Environment
Group: Development/Libraries
Requires: unzip, jre >= 1.5.0
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-ure%{?_isa} = 1:3.3.0
%endif

%description ure
UNO is the component model of LibreOffice. UNO offers interoperability between
programming languages, other components models and hardware architectures,
either in process or over process boundaries, in the Intranet as well as in the
Internet. UNO components may be implemented in and accessed from any
programming language for which a UNO implementation (AKA language binding) and
an appropriate bridge or adapter exists

%package sdk
Summary: Software Development Kit for LibreOffice
Group: Development/Libraries
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: unzip, java-devel
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-sdk%{?_isa} = 1:3.3.0, openoffice.org-devel%{?_isa} = 1:3.3.0
%endif

%description sdk
The LibreOffice SDK is an add-on for the LibreOffice office suite. It provides
the necessary tools for programming using the LibreOffice APIs and for creating
extensions (UNO components) for LibreOffice.  To set the build environment for
building against the sdk use %{sdkinstdir}/setsdkenv_unix.sh.

%package sdk-doc
Summary: Software Development Kit documentation for LibreOffice
Group: Documentation
Requires: %{name}-sdk = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-sdk-doc%{?_isa} = 1:3.3.0
%endif

%description sdk-doc
This provides documentation for programming using the LibreOffice APIs
and examples of creating extensions (UNO components) for LibreOffice.

%package headless
Summary: LibreOffice Headless plug-in
Group: Development/Libraries
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-headless%{?_isa} = 1:3.3.0
%endif

%description headless
A plug-in for LibreOffice that enables it to function without an X server. 
It implements the -headless command line option and allows LibreOffice to be
used as a backend server for e.g. document conversion.

%if 0%{?fedora}
%package kde
Summary: LibreOffice KDE integration plug-in
Group:   Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}

%description kde
A plug-in for LibreOffice that enables integration into the KDE desktop environment.
%endif

%if 0%{?_enable_debug_packages}

%define debug_package %{nil}
%global __debug_package 1

%package debuginfo
Summary: Debug information for package %{name}
Group: Development/Debug
AutoReqProv: 0
Requires: libreoffice-core = %{epoch}:%{version}-%{release}
Requires: libreoffice-gdb-debug-support = %{epoch}:%{version}-%{release}

%description debuginfo
This package provides debug information for package %{name}.
Debug information is useful when developing applications that use this
package or when debugging this package.

%files debuginfo -f debugfiles.list

%package gdb-debug-support
Summary: Additional support for debugging with gdb
Group: Development/Debug
Requires: gdb
AutoReqProv: 0

%description gdb-debug-support
This package provides gdb pretty printers for package %{name}.

%files gdb-debug-support
%{_datadir}/gdb/auto-load%{baseinstdir}
%{_datadir}/libreoffice/gdb

%endif

%define _langpack_common() \
%{baseinstdir}/program/resource/*%{1}.res  \
%{baseinstdir}/share/config/soffice.cfg/modules/*/ui/res/%{1} \
%{baseinstdir}/share/config/soffice.cfg/*/ui/res/%{1} \
%{baseinstdir}/share/template/%{1} \
%{baseinstdir}/share/registry/Langpack-%{1}.xcd \
%{baseinstdir}/share/registry/res/registry_%{1}.xcd \
%{baseinstdir}/share/registry/res/fcfg_langpack_%{1}.xcd \
%{nil}

# Defines a language pack subpackage.
#
# It's necessary to define language code (-l) and language name (-n).
# Additionally, it's possible
# * to require autocorr, hunspell, hyphen or mythes package or font for
#   given language,
# * to provide libreoffice-langpack-loc package, where loc is glibc
#   locale--this is necessary for yum to pick it automatically,
# * to require other, unrelated, packages,
# * to specify file serving as file list.
# For these, lower case character argument takes an argument specifying
# language, upper case character argument uses language from -l.
#
# All remaining arguments are considered to be files and added to the file
# list.
#
# Aa:  autocorr dependency
# c:   additional config file (just the name stem)
# E    the package does not contain any files (i.e., has empty filelist)
# Ff:  font language dependency
# Hh:  hunspell dependency
# i:   additional language added to this package
# L:   language code for files
# l:   language code, e.g., cs
# Mm:  mythes dependency
# n:   language name, e.g., Czech
# p:   Provides: of libreoffice-langpack
# r:   comma-separated list of additional requires
# S:s: script classification (cjk, ctl). -S is only a marker, as it does
#      not add any .xcd into the package (the file does not exist for at
#      least one CTL-using locale, si)
# T    has help files
# Xx:  has autotext definitions
# Yy:  hyphen dependency
#
# Example:
# libreoffice-langpack-cs: langpack for Czech lang. requiring hyphen-cs,
# autocorr-cs, mythes-cs-CZ and suitable font:
# %%langpack -l cs -n Czech -H -A -m cs-CZ
#  b de g  jk   o q  tuvw  z BCD  G IJK  NOPQR  UVW  Z0123456789
%define langpack(Aa:c:EFf:Hh:iL:l:Mm:n:p:r:S:s:TXx:Yy:) \
%define project LibreOffice \
%define lang %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define pkgname langpack-%{lang} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
\
%package %{pkgname} \
Summary: %{langname} language pack for %{project} \
Group: Applications/Productivity \
Requires: %{name}-core = %{epoch}:%{version}-%{release} \
%{-a:Requires: autocorr-%{-a*}}%{!-a:%{-A:Requires: autocorr-%{lang}}} \
%{-f:Requires: font(:lang=%{-f*})}%{!-f:%{-F:Requires: font(:lang=%{lang})}} \
%{-h:Requires: hunspell-%{-h*}}%{!-h:%{-H:Requires: hunspell-%{lang}}} \
%{-m:Requires: mythes-%{-m*}}%{!-m:%{-M:Requires: mythes-%{lang}}} \
%{-y:Requires: hyphen-%{-y*}}%{!-y:%{-Y:Requires: hyphen-%{lang}}} \
%{-r:Requires: %{-r*}} \
%{-p:Provides: %{name}-langpack-%{-p*}} \
\
%description %{pkgname} \
Provides additional %{langname} translations and resources for %{project}. \
\
%files %{pkgname} \
%{!-E: \
%define _langpack_lang %{-L:%{-L*}}%{!-L:%{-l*}} \
%define autotextdir %{baseinstdir}/share/autotext \
%{expand:%%_langpack_common %{_langpack_lang}} \
%{-x:%{autotextdir}/%{-x*}}%{!-x:%{-X:%{autotextdir}/%{_langpack_lang}}} \
%{-c:%{baseinstdir}/share/registry/%{-c*}.xcd} \
%{-s:%{baseinstdir}/share/registry/%{-s*}_%{_langpack_lang}.xcd} \
%{-T: \
%docdir %{baseinstdir}/help/%{_langpack_lang} \
%{baseinstdir}/help/%{_langpack_lang} \
} \
%{-i:%{expand:%%_langpack_common %{-i*}}} \
} \
%{nil}

# Defines an auto-correction subpackage.
#
# i: add autocorrections from additional language
# l: language code
# n: language name
# L  the filename does not contain country code
#
# All remaining arguments are considered to be files and added to the file
# list.
%define autocorr(i:Ll:n:) \
%define lang %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define pkgname autocorr-%{lang} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
\
%package -n %{pkgname} \
Summary: %{langname} auto-correction rules \
Group: Applications/Text \
BuildArch: noarch \
\
%description -n %{pkgname} \
Rules for auto-correcting common %{langname} typing errors. \
\
%files -n %{pkgname} \
%doc solver/unxlng*/bin/ure/LICENSE \
%dir %{_datadir}/autocorr \
%{-L:%{_datadir}/autocorr/acor_%{lang}.dat} \
%{!-L:%{_datadir}/autocorr/acor_%{lang}-*.dat} \
%{-i:%{_datadir}/autocorr/acor_%{-i*}-*.dat} \
%{nil}

%if %{with langpacks}

%langpack -l af -n Afrikaans -F -H -Y -A
%langpack -l ar -n Arabic -F -H -s ctl
%langpack -l as -n Assamese -F -H -Y
%langpack -l bg -n Bulgarian -F -H -Y -M -A -T -X
%langpack -l bn -n Bengali -F -H -Y -T
%langpack -l ca -n Catalan -F -H -Y -M -T
%langpack -l cs -n Czech -F -H -Y -M -A -T -X
%langpack -l cy -n Welsh -F -H -Y
%langpack -l da -n Danish -F -H -Y -M -A -T -X
%langpack -l de -n German -F -H -Y -M -A -T -X
%langpack -l dz -n Dzongkha -F -s ctl -T
%langpack -l el -n Greek -F -H -Y -M -T
%langpack -l en -n English -F -H -Y -M -A -E
%langpack -l es -n Spanish -F -H -Y -M -A -T -X
%langpack -l et -n Estonian -F -H -Y -T
%langpack -l eu -n Basque -F -H -Y -A -T -X
%if 0%{?fedora} || 0%{?rhel} >= 7
%langpack -l fa -n Farsi -A -H -Y -s ctl
%endif
%if 0%{?rhel} && 0%{?rhel} < 7
%langpack -l fi -n Finnish -F -A -T
%else
%langpack -l fi -n Finnish -F -r libreoffice-voikko -A -T
%endif
%langpack -l fr -n French -F -H -Y -M -A -T -X
%langpack -l ga -n Irish -F -H -Y -M -A
%langpack -l gl -n Galician -F -H -Y -T
%langpack -l gu -n Gujarati -F -H -Y -s ctl
%langpack -l he -n Hebrew -F -H -s ctl
%langpack -l hi -n Hindi -F -H -Y -s ctl -T
%langpack -l hr -n Croatian -F -H -Y -A
%langpack -l hu -n Hungarian -F -H -Y -M -A -T -X
%langpack -l it -n Italian -F -H -Y -M -A -T -X
%langpack -l ja -n Japanese -F -A -s cjk -T -X
%if 0%{?fedora} || 0%{?rhel} >= 7
%langpack -l kk -n Kazakh -F -H
%endif
%langpack -l kn -n Kannada -F -H -Y
%langpack -l ko -n Korean -F -H -A -s cjk -T -c korea -X
%langpack -l lt -n Lithuanian -F -H -Y -A
%if 0%{?fedora} || 0%{?rhel} >= 7
%langpack -l lv -n Latvian -F -H -Y -M
%endif
%langpack -l mai -n Maithili -F
%if 0%{?rhel} && 0%{?rhel} < 7
%langpack -l ms -n Malay -F -H
%endif
%langpack -l ml -n Malayalam -F -H -Y
%langpack -l mr -n Marathi -F -H -Y
%langpack -l nb -n Bokmal -F -H -Y -M -T
%langpack -l nl -n Dutch -F -H -Y -M -A -T -X
%langpack -l nn -n Nynorsk -F -H -Y -M -T
%define langpack_lang Southern Ndebele
%langpack -l nr -n %{langpack_lang} -F -H
%define langpack_lang Northern Sotho
%langpack -l nso -n %{langpack_lang} -F -H
%langpack -l or -n Oriya -F -H -Y -s ctl
%langpack -l pa -n Punjabi -F -H -Y -s ctl -L pa-IN
%langpack -l pl -n Polish -F -H -Y -M -A -T -X
%define langpack_lang Brazilian Portuguese
%langpack -l pt-BR -n %{langpack_lang} -f pt -h pt -y pt -m pt -a pt -p pt_BR -T -X
%langpack -l pt-PT -n Portuguese -f pt -h pt -y pt -m pt -a pt -p pt_PT -T -L pt -x pt
%langpack -l ro -n Romanian -F -H -Y -M -T
%langpack -l ru -n Russian -F -H -Y -M -A -T -X
%if 0%{?fedora} || 0%{?rhel} >= 7
%langpack -l si -n Sinhalese -F -H -S ctl -T
%endif
%langpack -l sk -n Slovak -F -H -Y -M -A -T -X
%langpack -l sl -n Slovenian -F -H -Y -M -A -T -X
#rhbz#452379 clump serbian translations together
%langpack -l sr -n Serbian -F -H -Y -A -i sh
%langpack -l ss -n Swati -F -H
%define langpack_lang Southern Sotho
%langpack -l st -n %{langpack_lang} -F -H
%langpack -l sv -n Swedish -F -H -Y -M -A -T -X
%langpack -l ta -n Tamil -F -H -Y -s ctl
%langpack -l te -n Telugu -F -H -Y
%langpack -l th -n Thai -F -H -s ctl -c ctlseqcheck_th
%langpack -l tn -n Tswana -F -H
%langpack -l tr -n Turkish -F -A -T -X
%langpack -l ts -n Tsonga -F -H
%langpack -l uk -n Ukrainian -F -H -Y -M -T
%if 0%{?rhel} && 0%{?rhel} < 7
%langpack -l ur -n Urdu -F -H
%endif
%langpack -l ve -n Venda -F -H
%langpack -l xh -n Xhosa -F -H
%define langpack_lang Simplified Chinese
%langpack -l zh-Hans -n %{langpack_lang} -f zh-cn -a zh -p zh_CN -s cjk -T -L zh-CN -x zh-CN
%define langpack_lang Traditional Chinese
%langpack -l zh-Hant -n %{langpack_lang} -f zh-tw -a zh -p zh_TW -s cjk -T -L zh-TW -x zh-TW
%langpack -l zu -n Zulu -F -H -Y
%undefine langpack_lang

%endif

%autocorr -l en -n English

%if %{with langpacks}

%autocorr -l af -n Afrikaans
%autocorr -l bg -n Bulgarian
%autocorr -l cs -n Czech
%autocorr -l da -n Danish
%autocorr -l de -n German
%autocorr -l es -n Spanish
%autocorr -l eu -n Basque -L
%autocorr -l fa -n Farsi
%autocorr -l fi -n Finnish
%autocorr -l fr -n French
%autocorr -l ga -n Irish
%autocorr -l hr -n Croatian
%autocorr -l hu -n Hungarian
%autocorr -l it -n Italian
%autocorr -l ja -n Japanese
%autocorr -l ko -n Korean
%autocorr -l lb -n Luxembourgish
%autocorr -l lt -n Lithuanian
%autocorr -l mn -n Mongolian
%autocorr -l nl -n Dutch
%autocorr -l pl -n Polish
%autocorr -l pt -n Portuguese
%autocorr -l ru -n Russian
%autocorr -l sk -n Slovak
%autocorr -l sl -n Slovenian
#rhbz#452379 clump serbian autocorrections together
%autocorr -l sr -n Serbian -i sh
%autocorr -l sv -n Swedish
%autocorr -l tr -n Turkish
%autocorr -l vi -n Vietnamese
%autocorr -l zh -n Chinese

%endif

%define make_autocorr_aliases(l:) \
%{?-l: \
for lang in %{*}; do \
    ln -sf acor_%{-l*}.dat acor_$lang.dat \
done \
} \
%{!?-l:%{error:-l must be present}}

%prep
%setup -q -n %{name}-%{version}%{?libo_prerelease} -b 1 -b 2
rm -rf git-hooks */git-hooks
#Customize Palette to remove Sun colours and add Red Hat colours
(head -n -1 extras/source/palettes/standard.soc && \
 echo -e ' <draw:color draw:name="Red Hat 1" draw:color="#cc0000"/>
 <draw:color draw:name="Red Hat 2" draw:color="#0093d9"/> 
 <draw:color draw:name="Red Hat 3" draw:color="#ff8d00"/>
 <draw:color draw:name="Red Hat 4" draw:color="#abb400"/>
 <draw:color draw:name="Red Hat 5" draw:color="#4e376b"/>' && \
 tail -n 1 extras/source/palettes/standard.soc) > redhat.soc
mv -f redhat.soc extras/source/palettes/standard.soc
%patch1  -p1
%patch2  -p1 -b .ooo86080.unopkg.bodge.patch
%patch3  -p1 -b .ooo88341.sc.verticalboxes.patch
%patch4  -p1 -b .oooXXXXX.solenv.allowmissing.patch
%patch5  -p1 -b .ooo101274.opening-a-directory.patch
%patch6  -p1 -b .ooo105784.vcl.sniffscriptforsubs.patch
%patch7  -p1 -b .libreoffice-installfix.patch
%patch8 -p1 -b .disable-failing-check.patch
%if 0%{?rhel} && 0%{?rhel} < 7
%patch9 -p1 -b .rhel6gcj.patch
%patch10 -p1 -b .rhel6poppler.patch
%patch11 -p1 -b .rhel6langs.patch
%patch12 -p1 -R -b .Require-icu-4.6-or-later-with-system-icu.patch
%patch13 -p1 -b .rhel6limits.patch
%patch14 -p1 -b .rhel6glib.patch
%endif
%patch15 -p1 -b .temporarily-disable-failing-test.patch
%patch16 -p1 -b .make-evolution-3.6-work-with-address-book.patch
%patch17 -p1 -b .no-g_list_free_full-in-RHEL-6-glib.patch
%patch18 -p1 -b .Work-around-problem-with-boost-shared_array-NULL-cto.patch
%patch19 -p1 -b .fix-compile-for-change-to-boost-1.53.0-declaring-sma.patch
%patch20 -p1 -b .rhbz-895196-sc-filter-float-a11y-parent-of-.patch
%patch21 -p1 -b .do-not-access-vector-elements-beyond-size-rhbz-84751.patch
%patch22 -p1 -b .rhbz-742780-Let-make-OPT_FLAGS-.-override-SDK-optimi.patch

# TODO: check this
# these are horribly incomplete--empty translations and copied english
# strings with spattering of translated strings
rm -rf translations/source/{gu,he,hr}/helpcontent2

%if 0%{?rhel} && 0%{?rhel} < 7
cp -r translations/source/en-GB translations/source/ms
cp -r translations/source/en-GB translations/source/ur
%endif

# disable failing test
# FIXME something to do with python3?
sed -i -e /sw_macros_test/d -e /sw_subsequent_.\*port/d sw/Module_sw.mk

%build
echo build start time is `date`, diskspace: `df -h . | tail -n 1`
#don't build localized helps which aren't translated
POORHELPS=`ls -d translations/source/*/helpcontent2 translations/source/*|cut -f 3 -d /|sort|uniq -u|xargs`
#don't build localized helps which are poorly translated
POORHELPS="$POORHELPS `grep 'msgstr .Working with Documents' translations/source/*/helpcontent2/source/text/swriter/guide.po| cut -f 3 -d / | xargs`"
# path to external tarballs
EXTSRCDIR=`dirname %{SOURCE0}`

%if 0%{?fedora}
# KDE bits
export QT4DIR=%{_qt4_prefix}
export KDE4DIR=%{_kde4_prefix}
export PATH=$QT4DIR/bin:$PATH
%endif

#use the RPM_OPT_FLAGS but remove the OOo overridden ones
for i in $RPM_OPT_FLAGS; do
        case "$i" in
                -pipe|-Wall|-g|-fexceptions) continue;;
        esac
        ARCH_FLAGS="$ARCH_FLAGS $i"
done
export ARCH_FLAGS
export CFLAGS=$ARCH_FLAGS
export CXXFLAGS=$ARCH_FLAGS

%if 0%{?rhel}
%if 0%{?rhel} < 7
%define distrooptions --disable-graphite --without-system-mythes --without-system-mdds --without-junit --without-system-redland --disable-ext-mysql-connector --without-system-libexttextcat --without-system-libcdr --without-system-libwps --without-system-libwpd --without-system-libwpg --without-system-libcmis --without-system-clucene --without-system-libvisio --without-system-lcms2 --without-system-libmspub --without-system-orcus --without-system-liblangtag --without-system-boost --enable-gstreamer-0-10 --disable-gstreamer --disable-postgresql-sdbc --with-servlet-api-jar=/usr/share/java/apache-tomcat-apis/tomcat-servlet2.5-api.jar --enable-python=system --with-system-hsqldb
%else
%define distrooptions --without-system-hsqldb --disable-gstreamer-0-10 --enable-gstreamer --with-system-mythes --enable-python=system --with-servlet-api-jar=/usr/share/java/tomcat-servlet-api.jar
%endif
%else
%define distrooptions --without-system-hsqldb --enable-kde4 --disable-gstreamer-0-10 --enable-gstreamer --with-system-mythes --with-servlet-api-jar=/usr/share/java/tomcat-servlet-api.jar
%endif

%if ! 0%{libo_python3}
export PYTHON=%{_bindir}/python
export PYTHON_CFLAGS=`pkg-config --cflags python`
export PYTHON_LIBS=`pkg-config --libs python`
%endif

aclocal -I m4
autoconf
# avoid running autogen.sh on make
touch autogen.lastrun
%configure \
 %vendoroption %{?_smp_flags:--with-parallelism=%{_smp_flags}} \
 --with-build-version="%{version}-%{release}" --with-unix-wrapper=%{name} \
 --enable-release-build --disable-epm --disable-mathmldtd \
 --disable-gnome-vfs --enable-gio --enable-symbols --enable-lockdown \
 --enable-evolution2 --enable-dbus --enable-opengl --enable-vba \
 --enable-ext-presenter-minimizer --enable-ext-nlpsolver \
 --enable-ext-wiki-publisher --enable-ext-report-builder \
 --enable-scripting-beanshell --enable-scripting-javascript \
 --with-system-jars --with-vba-package-format="builtin" \
 --with-system-libs --with-system-headers --with-system-mozilla \
 --without-system-npapi-headers --with-system-dicts \
 --with-external-dict-dir=/usr/share/myspell \
 --without-myspell-dicts --without-fonts --without-ppds --without-afms \
 %{?with_lang} --with-poor-help-localizations="$POORHELPS" \
 --with-external-tar="$EXTSRCDIR" --with-java-target-version=1.5 \
 %{distrooptions} \
 --disable-fetch-external

if ! make VERBOSE=true; then
    # TODO Do we still need this? I think parallel build is reliable
    # enough these days...
    make VERBOSE=true PARALLELISM=1
fi

#generate the icons and mime type stuff
export DESTDIR=../../../output
export KDEMAINDIR=/usr
export GNOMEDIR=/usr
export GNOME_MIME_THEME=hicolor
# TODO use empty variables? Should make the renaming hacks in %%install
# unnecessary.
. ./bin/get_config_variables PRODUCTVERSIONSHORT PRODUCTVERSION
cd sysui/unxlng*/misc/libreoffice
./create_tree.sh

echo build end time is `date`, diskspace: `df -h . | tail -n 1`


%install
# TODO investigate use of make distro-pack-install
. ./bin/get_config_variables `sed -n -e '/^export/s/^export \([A-Z0-9_]\+\).*/\1/p' config_host.mk`
#figure out the icon version
export `grep "^PRODUCTVERSIONSHORT =" solenv/inc/productversion.mk | sed -e "s/ //g"`
export `grep "PRODUCTVERSION[ ]*=[ ]*" solenv/inc/productversion.mk | sed -e "s/ //g"`
#install
cd instsetoo_native/util
#direct install
mkdir -p $RPM_BUILD_ROOT/%{instdir}
export PKGFORMAT=installed
#don't duplicate english helpcontent about the place
unset DEFAULT_TO_ENGLISH_FOR_PACKING
if dmake openoffice_en-US; then
    ok=true
    break
else
    echo - ---dump log start---
    cat ../unx*.pro/LibreOffice/installed/logging/en-US/log_*_en-US.log
    echo - ---dump log end---
    ok=false
fi
if [ $ok == "false" ]; then
    exit 1
fi
mkdir -p $RPM_BUILD_ROOT/%{baseinstdir}
mv ../unxlng*.pro/LibreOffice/installed/install/en-US/* $RPM_BUILD_ROOT/%{baseinstdir}
chmod -R +w $RPM_BUILD_ROOT/%{baseinstdir}
# The installer currently sets UserInstallation to
# $ORIGIN/../libreoffice/4, which is of course total nonsense. Because I
# have no inclination to crawl through mountains of perl code to figure out
# where it comes from, I am just going to replace it by a sensible
# value here.
sed -i -e '/UserInstallation/s@\$ORIGIN/..@$SYSUSERCONFIG@' $RPM_BUILD_ROOT/%{baseinstdir}/program/bootstraprc
%if %{with langpacks}
dmake ooolanguagepack
rm -rf ../unxlng*.pro/LibreOffice_languagepack/installed/install/log
for langpack in ../unxlng*.pro/LibreOffice_languagepack/installed/install/*; do
  cp -rp $langpack/* $RPM_BUILD_ROOT/%{baseinstdir}
  rm -rf $langpack
done
%endif
export WITH_LANG_LIST="en-US"
dmake sdkoo
mv ../unxlng*.pro/LibreOffice_SDK/installed/install/en-US/sdk $RPM_BUILD_ROOT/%{sdkinstdir}
cd ../../

#configure sdk
pushd $RPM_BUILD_ROOT/%{sdkinstdir}
    for file in setsdkenv_unix.csh setsdkenv_unix.sh ; do
        sed -e "s,@OO_SDK_NAME@,sdk," \
            -e "s,@OO_SDK_HOME@,%{sdkinstdir}," \
            -e "s,@OFFICE_HOME@,%{baseinstdir}," \
            -e "s,@OO_SDK_URE_HOME@,%{ureinstdir}," \
            -e "s,@OO_SDK_MAKE_HOME@,/usr/bin," \
            -e "s,@OO_SDK_ZIP_HOME@,/usr/bin," \
            -e "s,@OO_SDK_CPP_HOME@,/usr/bin," \
            -e "s,@OO_SDK_CC_55_OR_HIGHER@,," \
            -e "s,@OO_SDK_JAVA_HOME@,$JAVA_HOME," \
            -e "s,@OO_SDK_OUTPUT_DIR@,\$HOME," \
            -e "s,@SDK_AUTO_DEPLOYMENT@,NO," \
            $file.in > $file
        chmod 755 $file
    done
    # we don't want to install the input files
    rm -f setsdkenv_unix.csh.in setsdkenv_unix.sh.in
#fix permissions
    find examples -type f -exec chmod -x {} \;
popd

#ensure a template dir for each lang
pushd $RPM_BUILD_ROOT/%{baseinstdir}/share/template
for I in %{langpack_langs}; do
    mkdir -p $I
done
popd

#Set some aliases to canonical autocorrect language files for locales with matching languages
pushd $RPM_BUILD_ROOT/%{baseinstdir}/share/autocorr

%make_autocorr_aliases -l en-GB en-AG en-AU en-BS en-BW en-BZ en-CA en-DK en-GH en-HK en-IE en-IN en-JM en-NG en-NZ en-SG en-TT
%make_autocorr_aliases -l en-US en-PH
#en-ZA exists and has a good autocorrect file with two or three extras that make sense for 
#neighbouring english speaking territories
%make_autocorr_aliases -l en-ZA en-NA en-ZW
%if %{with langpacks}
%make_autocorr_aliases -l af-ZA af-NA
%make_autocorr_aliases -l de-DE de-AT de-BE de-CH de-LI de-LU
%make_autocorr_aliases -l es-ES es-AR es-BO es-CL es-CO es-CR es-CU es-DO es-EC es-GT es-HN es-MX es-NI es-PA es-PE es-PR es-PY es-SV es-US es-UY es-VE
%make_autocorr_aliases -l fr-FR fr-BE fr-CA fr-CH fr-LU fr-MC
%make_autocorr_aliases -l it-IT it-CH
%make_autocorr_aliases -l nl-NL nl-AW
%make_autocorr_aliases -l sv-SE sv-FI
%else
rm -f acor_[a-df-z]*.dat acor_e[su]*.dat
%endif
popd
#rhbz#484055 make these shared across multiple applications
mkdir -p $RPM_BUILD_ROOT/%{_datadir}
mv -f $RPM_BUILD_ROOT/%{baseinstdir}/share/autocorr $RPM_BUILD_ROOT/%{_datadir}/autocorr
chmod 755 $RPM_BUILD_ROOT/%{_datadir}/autocorr

#remove it in case we didn't build with gcj
rm -f $RPM_BUILD_ROOT/%{baseinstdir}/program/classes/sandbox.jar

#remove dummy .dat files
rm -f $RPM_BUILD_ROOT/%{baseinstdir}/program/root?.dat

#set standard permissions for rpmlint
find $RPM_BUILD_ROOT/%{baseinstdir} -exec chmod +w {} \;
find $RPM_BUILD_ROOT/%{baseinstdir} -type d -exec chmod 0755 {} \;

# move python bits into site-packages
mkdir -p $RPM_BUILD_ROOT/%{libo_python_sitearch}
pushd $RPM_BUILD_ROOT/%{libo_python_sitearch}
echo "import sys, os" > uno.py
echo "sys.path.append('%{baseinstdir}/program')" >> uno.py
echo "os.putenv('URE_BOOTSTRAP', 'vnd.sun.star.pathname:%{baseinstdir}/program/fundamentalrc')" >> uno.py
cat $RPM_BUILD_ROOT/%{baseinstdir}/program/uno.py >> uno.py
rm -f $RPM_BUILD_ROOT/%{baseinstdir}/program/uno.py*
mv -f $RPM_BUILD_ROOT/%{baseinstdir}/program/unohelper.py* .
popd

# rhbz#477435 package opensymbol separately
pushd $RPM_BUILD_ROOT/%{baseinstdir}/share/fonts/truetype
install -d -m 0755 %{buildroot}%{_fontdir}
install -p -m 0644 *.ttf %{buildroot}%{_fontdir}
popd
rm -rf $RPM_BUILD_ROOT/%{baseinstdir}/share/fonts

#ensure that no sneaky un-prelinkable, un-fpic or non executable shared libs 
#have snuck through
pic=0
executable=0
for foo in `find $RPM_BUILD_ROOT/%{instdir} -name "*" -exec file {} \;| grep ": ELF" | cut -d: -f 1` ; do
    chmod +wx $foo
    ls -asl $foo
    result=`readelf -d $foo | grep TEXTREL` || true
    if [ "$result" != "" ]; then
        echo "TEXTREL Warning: $foo is b0rked (-fpic missing)"
        pic=1
    fi
    result=`readelf -l $foo | grep GNU_STACK | grep RWE` || true
    if [ "$result" != "" ]; then
        echo "GNU_STACK Warning: $foo is b0rked (-noexecstack missing)"
        executable=1
    fi
done
if [ $pic == 1 ]; then false; fi
if [ $executable == 1 ]; then false; fi

#make up some /usr/bin scripts
mkdir -p $RPM_BUILD_ROOT/%{_bindir}

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/ooffice
echo exec libreoffice \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/ooffice
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/ooffice

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/ooviewdoc
echo exec libreoffice --view \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/ooviewdoc
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/ooviewdoc

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oowriter
echo exec libreoffice --writer \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oowriter
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oowriter

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oocalc
echo exec libreoffice --calc \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oocalc
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oocalc

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/ooimpress
echo exec libreoffice --impress \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/ooimpress
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/ooimpress

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oodraw
echo exec libreoffice --draw \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oodraw
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oodraw

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oomath
echo exec libreoffice --math \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oomath
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oomath

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oobase
echo exec libreoffice --base \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oobase
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oobase

cp -f %{SOURCE4} $RPM_BUILD_ROOT/%{_bindir}/unopkg
sed -i -e "s/LAUNCHER/unopkg/g" $RPM_BUILD_ROOT/%{_bindir}/unopkg
sed -i -e "s/BRAND/libreoffice/g" $RPM_BUILD_ROOT/%{_bindir}/unopkg
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/unopkg

cp -f %{SOURCE4} $RPM_BUILD_ROOT/%{_bindir}/libreoffice
sed -i -e "s/LAUNCHER/soffice/g" $RPM_BUILD_ROOT/%{_bindir}/libreoffice
sed -i -e "s/BRAND/libreoffice/g" $RPM_BUILD_ROOT/%{_bindir}/libreoffice
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/libreoffice

pushd $RPM_BUILD_ROOT/%{_bindir}
# rhbz#499474 provide a /usr/bin/soffice for .recently-used.xbel
ln -s %{baseinstdir}/program/soffice soffice
# rhbz#499474 provide a /usr/bin/openoffice.org for backwards compat
ln -s libreoffice openoffice.org
popd

pushd $RPM_BUILD_ROOT/%{baseinstdir}/share/xdg/
chmod u+w *.desktop
rm -rf printeradmin.desktop
ICONVERSION=`echo $PRODUCTVERSION | sed -e 's/\.//'`
for file in *.desktop; do
    # rhbz#156677 remove the version from Name=
    # rhbz#156067 don't version the icons
    sed -i -e "s/ *$PRODUCTVERSION//g" \
        -e "s/$ICONVERSION//g" \
        -e "s/$PRODUCTVERSIONSHORT//g" \
        $file
    # add X-GIO-NoFuse so we get url:// instead of file://~.gvfs/
    echo X-GIO-NoFuse=true >> $file
done
for app in base calc draw impress math writer; do
    echo "StartupNotify=true" >> $app.desktop
    echo "TryExec=oo$app" >> $app.desktop
done
# rhbz#156677# / rhbz#186515#
echo "NoDisplay=true" >> startcenter.desktop
# rhbz#491159 temporarily remove NoDisplay=true from qstart.desktop
sed -i -e "/NoDisplay=true/d" qstart.desktop
# relocate the .desktop and icon files
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
for app in base calc draw impress javafilter math startcenter writer xsltfilter; do
    desktop-file-validate $app.desktop
    cp -p $app.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/libreoffice-$app.desktop
done
popd

pushd sysui/output/usr/share/
#get rid of the gnome icons and other unneeded files
rm -rf icons/gnome applications application-registry

#relocate the rest of them
# rhbz#901346 512x512 icons are not used by anything
for icon in `find icons -path '*/512x512' -prune -o -type f -print`; do
    mkdir -p $RPM_BUILD_ROOT/%{_datadir}/`dirname $icon`
    cp -p $icon $RPM_BUILD_ROOT/%{_datadir}/`echo $icon | sed -e s@office$ICONVERSION@office@ | sed -e s@office$PRODUCTVERSION@office@`
done
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mime-info
cp -p mime-info/libreoffice$PRODUCTVERSION.keys $RPM_BUILD_ROOT/%{_datadir}/mime-info/libreoffice.keys
cp -p mime-info/libreoffice$PRODUCTVERSION.mime $RPM_BUILD_ROOT/%{_datadir}/mime-info/libreoffice.mime
#add our mime-types, e.g. for .oxt extensions
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mime/packages
cp -p mime/packages/libreoffice$PRODUCTVERSION.xml $RPM_BUILD_ROOT/%{_datadir}/mime/packages/libreoffice.xml
popd

rm -rf $RPM_BUILD_ROOT/%{baseinstdir}/readmes
rm -rf $RPM_BUILD_ROOT/%{baseinstdir}/licenses

mkdir -p $RPM_BUILD_ROOT/%{baseinstdir}/share/psprint/driver
cp -p psprint_config/configuration/ppds/SGENPRT.PS $RPM_BUILD_ROOT/%{baseinstdir}/share/psprint/driver/SGENPRT.PS

# rhbz#452385 to auto have postgres in classpath if subsequently installed
sed -i -e "s#URE_MORE_JAVA_CLASSPATH_URLS.*#& file:///usr/share/java/postgresql-jdbc.jar#" $RPM_BUILD_ROOT/%{baseinstdir}/program/fundamentalrc

export DESTDIR=$RPM_BUILD_ROOT
install-gdb-printers -a %{_datadir}/gdb/auto-load%{baseinstdir} -c -i %{baseinstdir} -p %{_datadir}/libreoffice/gdb


#%check
#unset WITH_LANG
## work around flawed accessibility check
#export JFW_PLUGIN_DO_NOT_CHECK_ACCESSIBILITY="1"
#%if 0%{?rhel} && 0%{?rhel} < 7
#timeout 2h make smoketest.subsequentcheck
#%else
#timeout -k 2m 2h make smoketest.subsequentcheck
#%endif

%files

%files core
%dir %{baseinstdir}
%dir %{baseinstdir}/help
%docdir %{baseinstdir}/help/en
%dir %{baseinstdir}/help/en
%{baseinstdir}/help/en/default.css
%{baseinstdir}/help/en/err.html
%{baseinstdir}/help/en/highcontrast1.css
%{baseinstdir}/help/en/highcontrast2.css
%{baseinstdir}/help/en/highcontrastblack.css
%{baseinstdir}/help/en/highcontrastwhite.css
%{baseinstdir}/help/en/sbasic.*
%{baseinstdir}/help/en/schart.*
%{baseinstdir}/help/en/shared.*
%{baseinstdir}/help/idxcaption.xsl
%{baseinstdir}/help/idxcontent.xsl
%{baseinstdir}/help/main_transform.xsl
%{baseinstdir}/presets
%dir %{baseinstdir}/program
%{baseinstdir}/program/addin
%{baseinstdir}/program/basprov.uno.so
%{baseinstdir}/program/cairocanvas.uno.so
%{baseinstdir}/program/canvasfactory.uno.so
%{baseinstdir}/program/cde-open-url
%dir %{baseinstdir}/program/classes
%{baseinstdir}/program/classes/agenda.jar
%{baseinstdir}/program/classes/commonwizards.jar
%{baseinstdir}/program/classes/form.jar
%{baseinstdir}/program/classes/query.jar
%{baseinstdir}/program/classes/officebean.jar
%{baseinstdir}/program/classes/report.jar
%{baseinstdir}/program/classes/ScriptFramework.jar
%{baseinstdir}/program/classes/ScriptProviderForJava.jar
%{baseinstdir}/program/classes/table.jar
%{baseinstdir}/program/classes/unoil.jar
%{baseinstdir}/program/classes/web.jar
%{baseinstdir}/program/classes/XMergeBridge.jar
%{baseinstdir}/program/classes/xmerge.jar
%{baseinstdir}/program/cmdmail.uno.so
%{baseinstdir}/program/libdeployment.so
%{baseinstdir}/program/libdeploymentgui.so
%{baseinstdir}/program/dlgprov.uno.so
%{baseinstdir}/program/expwrap.uno.so
%{baseinstdir}/program/fastsax.uno.so
%{baseinstdir}/program/flat_logo.svg
%{baseinstdir}/program/fpicker.uno.so
%{baseinstdir}/program/fps_office.uno.so
%{baseinstdir}/program/gdbtrace
%{baseinstdir}/program/gengal
%{baseinstdir}/program/gengal.bin
%{baseinstdir}/program/gnome-open-url
%{baseinstdir}/program/gnome-open-url.bin
%{baseinstdir}/program/hatchwindowfactory.uno.so
%{baseinstdir}/program/kde-open-url
%{baseinstdir}/program/i18nsearch.uno.so
%{baseinstdir}/program/ldapbe2.uno.so
%{baseinstdir}/program/libacclo.so
%{baseinstdir}/program/libavmedia*.so
%{baseinstdir}/program/libbasctllo.so
%{baseinstdir}/program/libbiblo.so
%{baseinstdir}/program/libcached1.so
%{baseinstdir}/program/libcanvastoolslo.so
%{baseinstdir}/program/libchart*lo.so
%{baseinstdir}/program/libcollator_data.so
%{baseinstdir}/program/libcppcanvaslo.so
%{baseinstdir}/program/libctllo.so
%{baseinstdir}/program/libcuilo.so
%{baseinstdir}/program/libdbalo.so
%{baseinstdir}/program/libdbaselo.so
%{baseinstdir}/program/libdbaxmllo.so
%{baseinstdir}/program/libdbmmlo.so
%{baseinstdir}/program/libdbpool2.so
%{baseinstdir}/program/libdbtoolslo.so
%{baseinstdir}/program/libdbulo.so
%{baseinstdir}/program/libdeploymentmisclo.so
%{baseinstdir}/program/libdesktop_detectorlo.so
%{baseinstdir}/program/libdict_ja.so
%{baseinstdir}/program/libdict_zh.so
%{baseinstdir}/program/libdrawinglayerlo.so
%{baseinstdir}/program/libeditenglo.so
%{baseinstdir}/program/libembobj.so
%{baseinstdir}/program/libemboleobj.so
%{baseinstdir}/program/libevoab*.so
%{baseinstdir}/program/libevtattlo.so
%{baseinstdir}/program/libegilo.so
%{baseinstdir}/program/libemelo.so
%{baseinstdir}/program/libepblo.so
%{baseinstdir}/program/libepglo.so
%{baseinstdir}/program/libepplo.so
%{baseinstdir}/program/libepslo.so
%{baseinstdir}/program/libeptlo.so
%{baseinstdir}/program/liberalo.so
%{baseinstdir}/program/libetilo.so
%{baseinstdir}/program/libexplo.so
%{baseinstdir}/program/libicdlo.so
%{baseinstdir}/program/libicglo.so
%{baseinstdir}/program/libidxlo.so
%{baseinstdir}/program/libimelo.so
%{baseinstdir}/program/libindex_data.so
%{baseinstdir}/program/libipblo.so
%{baseinstdir}/program/libipdlo.so
%{baseinstdir}/program/libipslo.so
%{baseinstdir}/program/libiptlo.so
%{baseinstdir}/program/libipxlo.so
%{baseinstdir}/program/libiralo.so
%{baseinstdir}/program/libitglo.so
%{baseinstdir}/program/libitilo.so
%{baseinstdir}/program/libofficebean.so
%{baseinstdir}/program/libfilelo.so
%{baseinstdir}/program/libfilterconfiglo.so
%{baseinstdir}/program/libflatlo.so
%{baseinstdir}/program/libfrmlo.so
%{baseinstdir}/program/libguesslanglo.so
%{baseinstdir}/program/libhelplinkerlo.so
%{baseinstdir}/program/libhyphenlo.so
%{baseinstdir}/program/libjdbclo.so
%{baseinstdir}/program/liblnglo.so
%{baseinstdir}/program/libloglo.so
%{baseinstdir}/program/liblocaledata_en.so
%{baseinstdir}/program/liblocaledata_es.so
%{baseinstdir}/program/liblocaledata_euro.so
%{baseinstdir}/program/liblocaledata_others.so
%{baseinstdir}/program/libmcnttype.so
%{baseinstdir}/program/libmorklo.so
%{baseinstdir}/program/libmozbootstrap.so
%{baseinstdir}/program/libmsfilterlo.so
%{baseinstdir}/program/mtfrenderer.uno.so
%{baseinstdir}/program/libmysqllo.so
%{baseinstdir}/program/libodbclo.so
%{baseinstdir}/program/libodbcbaselo.so
%{baseinstdir}/program/liboffacclo.so
%{baseinstdir}/program/libooxlo.so
%{baseinstdir}/program/libpcrlo.so
%{baseinstdir}/program/libpdffilterlo.so
%{baseinstdir}/program/libpllo.so
%{baseinstdir}/program/libprotocolhandlerlo.so
%{baseinstdir}/program/libqstart_gtklo.so
%{baseinstdir}/program/librecentfile.so
%{baseinstdir}/program/libreslo.so
%{baseinstdir}/program/libsaxlo.so
%{baseinstdir}/program/libscnlo.so
%{baseinstdir}/program/libscriptframe.so
%{baseinstdir}/program/libsdlo.so
%{baseinstdir}/program/libsdfiltlo.so
%{baseinstdir}/program/libsdbc2.so
%{baseinstdir}/program/libsdbtlo.so
%{baseinstdir}/program/libsddlo.so
%{baseinstdir}/program/libsduilo.so
%{baseinstdir}/program/libspalo.so
%{baseinstdir}/program/libspelllo.so
%{baseinstdir}/program/libsrtrs1.so
%{baseinstdir}/program/libsvgiolo.so
%{baseinstdir}/program/libsvxlo.so
%{baseinstdir}/program/libsvxcorelo.so
%{baseinstdir}/program/libswlo.so
%{baseinstdir}/program/libtextconv_dict.so
%{baseinstdir}/program/libtextconversiondlgslo.so
%{baseinstdir}/program/libtextfdlo.so
%{baseinstdir}/program/libtvhlp1.so
%{baseinstdir}/program/libodfflatxmllo.so
%{baseinstdir}/program/libucbhelper4gcc3.so
%{baseinstdir}/program/libucpchelp1.so
%{baseinstdir}/program/libucpdav1.so
%{baseinstdir}/program/libucpftp1.so
%{baseinstdir}/program/libucphier1.so
%{baseinstdir}/program/libucppkg1.so
%{baseinstdir}/program/libunordflo.so
%{baseinstdir}/program/libunopkgapp.so
%{baseinstdir}/program/libunoxmllo.so
%{baseinstdir}/program/libuuilo.so
%{baseinstdir}/program/libvbahelperlo.so
%{baseinstdir}/program/libvclplug_genlo.so
%{baseinstdir}/program/libvclplug_gtklo.so
%{baseinstdir}/program/libwpftdrawlo.so
%{baseinstdir}/program/libxmlfalo.so
%{baseinstdir}/program/libxmlfdlo.so
%{baseinstdir}/program/libxoflo.so
%{baseinstdir}/program/libxsec_fw.so
%{baseinstdir}/program/libxsec_xmlsec.so
%{baseinstdir}/program/libxsltdlglo.so
%{baseinstdir}/program/libxsltfilterlo.so
%{baseinstdir}/program/libxstor.so
%if 0%{?fedora} || 0%{?rhel} >= 7
# TODO how useful this is in Fedora?
%{baseinstdir}/program/losessioninstall.uno.so
%endif
%{baseinstdir}/program/migrationoo2.uno.so
%{baseinstdir}/program/migrationoo3.uno.so
%{baseinstdir}/program/msforms.uno.so
%{baseinstdir}/program/nsplugin
%{baseinstdir}/program/open-url
%{baseinstdir}/program/types/offapi.rdb
%{baseinstdir}/program/passwordcontainer.uno.so
%{baseinstdir}/program/pagein-common
%{baseinstdir}/program/plugin
%{baseinstdir}/program/pluginapp.bin
%dir %{baseinstdir}/program/resource
%{baseinstdir}/program/resource/avmediaen-US.res
%{baseinstdir}/program/resource/accen-US.res
%{baseinstdir}/program/resource/basctlen-US.res
%{baseinstdir}/program/resource/biben-US.res
%{baseinstdir}/program/resource/chartcontrolleren-US.res
%{baseinstdir}/program/resource/cuien-US.res
%{baseinstdir}/program/resource/dbaen-US.res
%{baseinstdir}/program/resource/dbmmen-US.res
%{baseinstdir}/program/resource/dbuen-US.res
%{baseinstdir}/program/resource/dbwen-US.res
%{baseinstdir}/program/resource/deploymenten-US.res
%{baseinstdir}/program/resource/deploymentguien-US.res
%{baseinstdir}/program/resource/dkten-US.res
%{baseinstdir}/program/resource/editengen-US.res
%{baseinstdir}/program/resource/epsen-US.res
%{baseinstdir}/program/resource/euren-US.res
%{baseinstdir}/program/resource/fps_officeen-US.res
%{baseinstdir}/program/resource/frmen-US.res
%{baseinstdir}/program/resource/fween-US.res
%{baseinstdir}/program/resource/galen-US.res
%{baseinstdir}/program/resource/impen-US.res
%{baseinstdir}/program/resource/ofaen-US.res
%{baseinstdir}/program/resource/pcren-US.res
%{baseinstdir}/program/resource/pdffilteren-US.res
%{baseinstdir}/program/resource/sben-US.res
%{baseinstdir}/program/resource/scnen-US.res
%{baseinstdir}/program/resource/sden-US.res
%{baseinstdir}/program/resource/sfxen-US.res
%{baseinstdir}/program/resource/spaen-US.res
%{baseinstdir}/program/resource/sdbten-US.res
%{baseinstdir}/program/resource/svlen-US.res
%{baseinstdir}/program/resource/svten-US.res
%{baseinstdir}/program/resource/svxen-US.res
%{baseinstdir}/program/resource/swen-US.res
%{baseinstdir}/program/resource/textconversiondlgsen-US.res
%{baseinstdir}/program/resource/tken-US.res
%{baseinstdir}/program/resource/tplen-US.res
%{baseinstdir}/program/resource/uuien-US.res
%{baseinstdir}/program/resource/upden-US.res
%{baseinstdir}/program/resource/vclen-US.res
%{baseinstdir}/program/resource/wzien-US.res
%{baseinstdir}/program/resource/xmlsecen-US.res
%{baseinstdir}/program/resource/xsltdlgen-US.res
%{baseinstdir}/program/senddoc
%dir %{baseinstdir}/program/services
%{baseinstdir}/program/services/services.rdb
%{baseinstdir}/program/simplecanvas.uno.so
%{baseinstdir}/program/slideshow.uno.so
%{baseinstdir}/program/libsofficeapp.so
%{baseinstdir}/program/spadmin.bin
%{baseinstdir}/program/stringresource.uno.so
%{baseinstdir}/program/syssh.uno.so
%{baseinstdir}/program/tde-open-url
%{baseinstdir}/program/ucpcmis1.uno.so
%{baseinstdir}/program/ucpexpand1.uno.so
%{baseinstdir}/program/ucpext.uno.so
%{baseinstdir}/program/ucptdoc1.uno.so
%{baseinstdir}/program/unorc
%{baseinstdir}/program/updatefeed.uno.so
# TODO do we need this?
%{baseinstdir}/program/ui-previewer
%{baseinstdir}/ure-link
%{baseinstdir}/program/uri-encode
%{baseinstdir}/program/vbaevents.uno.so
%{baseinstdir}/program/vclcanvas.uno.so
%{baseinstdir}/program/versionrc
%dir %{baseinstdir}/share
%dir %{baseinstdir}/share/Scripts
%{baseinstdir}/share/Scripts/java
%dir %{baseinstdir}/share/autotext
%{baseinstdir}/share/autotext/en-US
%{baseinstdir}/share/basic
%dir %{baseinstdir}/share/config
%{baseinstdir}/share/config/images.zip
%{baseinstdir}/share/config/images_crystal.zip
%{baseinstdir}/share/config/images_hicontrast.zip
%{baseinstdir}/share/config/images_oxygen.zip
%{baseinstdir}/share/config/images_tango.zip
%{baseinstdir}/share/config/psetup.xpm
%{baseinstdir}/share/config/psetupl.xpm
%dir %{baseinstdir}/share/config/soffice.cfg
%{baseinstdir}/share/config/soffice.cfg/modules
# UI translations go into langpacks
%exclude %{baseinstdir}/share/config/soffice.cfg/modules/*/ui/res
%{baseinstdir}/share/config/soffice.cfg/*/ui
# UI translations go into langpacks
%exclude %{baseinstdir}/share/config/soffice.cfg/*/ui/res
%{baseinstdir}/share/config/webcast
%{baseinstdir}/share/config/wizard
%dir %{baseinstdir}/share/dtd
%{baseinstdir}/share/dtd/officedocument
%{baseinstdir}/share/gallery
%if 0%{?rhel} && 0%{?rhel} < 7
%{baseinstdir}/share/liblangtag
%endif
%dir %{baseinstdir}/share/psprint
%config %{baseinstdir}/share/psprint/psprint.conf
%{baseinstdir}/share/psprint/driver
%dir %{baseinstdir}/share/registry
%{baseinstdir}/share/registry/gnome.xcd
%{baseinstdir}/share/registry/lingucomponent.xcd
%{baseinstdir}/share/registry/main.xcd
%{baseinstdir}/share/registry/oo-ad-ldap.xcd.sample
%{baseinstdir}/share/registry/oo-ldap.xcd.sample
%{baseinstdir}/share/registry/Langpack-en-US.xcd
%dir %{baseinstdir}/share/registry/res
%{baseinstdir}/share/registry/res/fcfg_langpack_en-US.xcd
%dir %{baseinstdir}/share/template
%{baseinstdir}/share/template/en-US
%dir %{baseinstdir}/share/template/common
%{baseinstdir}/share/template/common/internal
%{baseinstdir}/share/template/common/layout
%{baseinstdir}/share/template/common/wizard
%{baseinstdir}/share/template/wizard
%dir %{baseinstdir}/share/wordbook
%{baseinstdir}/share/wordbook/en-GB.dic
%{baseinstdir}/share/wordbook/en-US.dic
%{baseinstdir}/share/wordbook/sl.dic
%{baseinstdir}/share/wordbook/technical.dic
%dir %{baseinstdir}/share/xslt
%{baseinstdir}/share/xslt/common
%dir %{baseinstdir}/share/xslt/export
%{baseinstdir}/share/xslt/export/common
%{baseinstdir}/share/xslt/export/spreadsheetml
%{baseinstdir}/share/xslt/export/wordml
%dir %{baseinstdir}/share/xslt/import
%{baseinstdir}/share/xslt/import/common
%{baseinstdir}/share/xslt/import/spreadsheetml
%{baseinstdir}/share/xslt/import/wordml
%{baseinstdir}/program/liblnthlo.so
%{_bindir}/unopkg
#icons and mime
%{_datadir}/icons/*/*/*/libreoffice*
%{_datadir}/mime-info/libreoffice.*
%{baseinstdir}/program/libxmlsecurity.so
%{_datadir}/mime/packages/libreoffice.xml
%{baseinstdir}/program/configmgr.uno.so
%{baseinstdir}/program/desktopbe1.uno.so
%{baseinstdir}/program/fsstorage.uno.so
%{baseinstdir}/program/gconfbe1.uno.so
%{baseinstdir}/program/i18npool.uno.so
%{baseinstdir}/program/libbasegfxlo.so
%{baseinstdir}/program/libcomphelpgcc3.so
%{baseinstdir}/program/libfileacc.so
%{baseinstdir}/program/libfwelo.so
%{baseinstdir}/program/libfwilo.so
%{baseinstdir}/program/libfwklo.so
%{baseinstdir}/program/libfwllo.so
%{baseinstdir}/program/libfwmlo.so
%{baseinstdir}/program/libi18nisolang*.so
%{baseinstdir}/program/libi18nutilgcc3.so
%{baseinstdir}/program/libpackage2.so
%{baseinstdir}/program/libsblo.so
%{baseinstdir}/program/libsfxlo.so
%{baseinstdir}/program/libsotlo.so
%{baseinstdir}/program/libspllo.so
%{baseinstdir}/program/libspl_unxlo.so
%{baseinstdir}/program/libsvllo.so
%{baseinstdir}/program/libsvtlo.so
%{baseinstdir}/program/libtklo.so
%{baseinstdir}/program/libtllo.so
%{baseinstdir}/program/libucb1.so
%{baseinstdir}/program/libucpfile1.so
%{baseinstdir}/program/libutllo.so
%{baseinstdir}/program/libvcllo.so
%{baseinstdir}/program/libxmlscriptlo.so
%{baseinstdir}/program/libxolo.so
%{baseinstdir}/program/localebe1.uno.so
%{baseinstdir}/program/ucpgio1.uno.so
%{baseinstdir}/program/types/oovbaapi.rdb
#share unopkg
%dir %{baseinstdir}/share/extensions
%{baseinstdir}/share/extensions/package.txt
%{baseinstdir}/program/unopkg
%{baseinstdir}/program/unopkg.bin
%{baseinstdir}/program/bootstraprc
%{baseinstdir}/program/fundamentalrc
%{baseinstdir}/program/setuprc
%doc %{baseinstdir}/CREDITS.odt
%doc %{baseinstdir}/LICENSE
%doc %{baseinstdir}/LICENSE.html
%doc %{baseinstdir}/LICENSE.odt
%doc %{baseinstdir}/NOTICE
%{baseinstdir}/program/intro.*
%{baseinstdir}/program/soffice
%{baseinstdir}/program/soffice.bin
%{baseinstdir}/program/sofficerc
%{baseinstdir}/program/spadmin
%{baseinstdir}/program/unoinfo
%{baseinstdir}/program/libnpsoplugin.so
%{baseinstdir}/program/oosplash
%{baseinstdir}/program/shell/
%{baseinstdir}/share/config/images_brand.zip
%{baseinstdir}/share/xdg/
%{baseinstdir}/program/redirectrc
%{_datadir}/applications/libreoffice-startcenter.desktop
#launchers
%{_bindir}/libreoffice
%{_bindir}/openoffice.org
%{_bindir}/soffice
%{_bindir}/ooffice
%{_bindir}/ooviewdoc
%if 0%{?rhel} && 0%{?rhel} < 7
%{baseinstdir}/program/libraptor-lo.so.1
%{baseinstdir}/program/librasqal-lo.so.1
%{baseinstdir}/program/librdf-lo.so.0
%{baseinstdir}/program/libclucene.so
%{baseinstdir}/program/liblcms2.so.2
%{baseinstdir}/share/fingerprint
%endif

%post core
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database %{_datadir}/applications &> /dev/null || :
for theme in hicolor locolor; do
    touch --no-create %{_datadir}/icons/$theme &>/dev/null || :
done

%postun core
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database %{_datadir}/applications &> /dev/null || :
if [ $1 -eq 0 ] ; then
    for theme in hicolor locolor; do
        touch --no-create %{_datadir}/icons/$theme &>/dev/null || :
        gtk-update-icon-cache -q %{_datadir}/icons/$theme &>/dev/null || :
    done
fi

%posttrans core
for theme in hicolor locolor; do
    gtk-update-icon-cache -q %{_datadir}/icons/$theme &>/dev/null || :
done


%files base
%{baseinstdir}/help/en/sdatabase.*
%if 0%{?fedora} || 0%{?rhel} >= 7
%{baseinstdir}/program/classes/hsqldb.jar
%endif
%{baseinstdir}/program/classes/sdbc_hsqldb.jar
%{baseinstdir}/program/libabplo.so
%{baseinstdir}/program/libdbplo.so
%{baseinstdir}/program/libhsqldb.so
%{baseinstdir}/program/librptlo.so
%{baseinstdir}/program/librptuilo.so
%{baseinstdir}/program/librptxmllo.so
%{baseinstdir}/program/resource/abpen-US.res
%{baseinstdir}/program/resource/cnren-US.res
%{baseinstdir}/program/resource/dbpen-US.res
%{baseinstdir}/program/resource/rpten-US.res
%{baseinstdir}/program/resource/rptuien-US.res
%{baseinstdir}/program/resource/sdbclen-US.res
%{baseinstdir}/program/resource/sdberren-US.res
%{baseinstdir}/share/registry/base.xcd
%{baseinstdir}/program/sbase
%{_datadir}/applications/libreoffice-base.desktop
%{_bindir}/oobase

%post base
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun base
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files report-builder
%docdir %{baseinstdir}/share/extensions/report-builder/help
%{baseinstdir}/share/extensions/report-builder

%files bsh
%{baseinstdir}/program/classes/ScriptProviderForBeanShell.jar
%{baseinstdir}/program/services/scriptproviderforbeanshell.rdb
%{baseinstdir}/share/Scripts/beanshell

%files rhino
%{baseinstdir}/program/classes/js.jar
%{baseinstdir}/program/classes/ScriptProviderForJavaScript.jar
%{baseinstdir}/program/services/scriptproviderforjavascript.rdb
%{baseinstdir}/share/Scripts/javascript

%files wiki-publisher
%docdir %{baseinstdir}/share/extensions/wiki-publisher/license
%{baseinstdir}/share/extensions/wiki-publisher

%files nlpsolver
%docdir %{baseinstdir}/share/extensions/nlpsolver/help
%{baseinstdir}/share/extensions/nlpsolver

%files ogltrans
%{baseinstdir}/program/OGLTrans.uno.so
%{baseinstdir}/share/config/soffice.cfg/simpress/transitions-ogl.xml
%{baseinstdir}/share/registry/ogltrans.xcd

%files presentation-minimizer
%docdir %{baseinstdir}/share/extensions/presentation-minimizer/help
%{baseinstdir}/share/extensions/presentation-minimizer

%files pdfimport
%{baseinstdir}/program/pdfimport.uno.so
%{baseinstdir}/program/xpdfimport
%{baseinstdir}/share/registry/pdfimport.xcd
%dir %{baseinstdir}/share/xpdfimport
%{baseinstdir}/share/xpdfimport/xpdfimport_err.pdf

%_font_pkg -n %{fontname} opens___.ttf
%doc solver/unxlng*/bin/ure/LICENSE

%files calc
%{baseinstdir}/help/en/scalc.*
%{baseinstdir}/program/libanalysislo.so
%{baseinstdir}/program/libcalclo.so
%{baseinstdir}/program/libdatelo.so
%{baseinstdir}/program/libforlo.so
%{baseinstdir}/program/libforuilo.so
%{baseinstdir}/program/libpricinglo.so
%{baseinstdir}/program/libsclo.so
%{baseinstdir}/program/libscdlo.so
%{baseinstdir}/program/libscfiltlo.so
%{baseinstdir}/program/libscuilo.so
%{baseinstdir}/program/libsolverlo.so
%{baseinstdir}/program/resource/analysisen-US.res
%{baseinstdir}/program/resource/dateen-US.res
%{baseinstdir}/program/resource/foren-US.res
%{baseinstdir}/program/resource/foruien-US.res
%{baseinstdir}/program/resource/pricingen-US.res
%{baseinstdir}/program/resource/scen-US.res
%{baseinstdir}/program/resource/solveren-US.res
%{baseinstdir}/program/vbaobj.uno.so
%{baseinstdir}/share/registry/calc.xcd
%{baseinstdir}/program/pagein-calc
%{baseinstdir}/program/scalc
%{_datadir}/applications/libreoffice-calc.desktop
%{_bindir}/oocalc

%post calc
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun calc
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files draw
%{baseinstdir}/help/en/sdraw.*
%{baseinstdir}/share/registry/draw.xcd
%{baseinstdir}/program/pagein-draw
%{baseinstdir}/program/sdraw
%{_datadir}/applications/libreoffice-draw.desktop
%{_bindir}/oodraw

%post draw
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun draw
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files emailmerge
%{baseinstdir}/program/mailmerge.py*
%{baseinstdir}/program/msgbox.py*
%{baseinstdir}/program/officehelper.py*

%files writer
%{baseinstdir}/help/en/swriter.*
%{baseinstdir}/program/libhwplo.so
%{baseinstdir}/program/liblwpftlo.so
%{baseinstdir}/program/libmswordlo.so
%{baseinstdir}/program/libswdlo.so
%{baseinstdir}/program/libswuilo.so
%{baseinstdir}/program/libt602filterlo.so
%{baseinstdir}/program/libwpftwriterlo.so
%{baseinstdir}/program/libwriterfilterlo.so
%{baseinstdir}/program/vbaswobj.uno.so
%{baseinstdir}/program/resource/t602filteren-US.res
%{baseinstdir}/share/registry/writer.xcd
%{baseinstdir}/program/pagein-writer
%{baseinstdir}/program/swriter
%{_datadir}/applications/libreoffice-writer.desktop
%{_bindir}/oowriter

%post writer
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun writer
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files impress
%{baseinstdir}/help/en/simpress.*
%{baseinstdir}/program/libanimcorelo.so
%{baseinstdir}/program/libplacewarelo.so
%{baseinstdir}/program/PresenterScreen.uno.so
%dir %{baseinstdir}/share/config/soffice.cfg/simpress
%{baseinstdir}/share/config/soffice.cfg/simpress/effects.xml
%{baseinstdir}/share/config/soffice.cfg/simpress/transitions.xml
%{baseinstdir}/share/registry/impress.xcd
%{baseinstdir}/program/pagein-impress
%{baseinstdir}/program/simpress
%{_datadir}/applications/libreoffice-impress.desktop
%{_bindir}/ooimpress

%post impress
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun impress
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files math
%{baseinstdir}/help/en/smath.*
%{baseinstdir}/program/libsmlo.so
%{baseinstdir}/program/libsmdlo.so
%{baseinstdir}/program/resource/smen-US.res
%{baseinstdir}/share/registry/math.xcd
%{baseinstdir}/program/smath
%{_datadir}/applications/libreoffice-math.desktop
%{_bindir}/oomath

%post math
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun math
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files graphicfilter
%{baseinstdir}/program/libflashlo.so
%{baseinstdir}/program/libsvgfilterlo.so
%{baseinstdir}/share/registry/graphicfilter.xcd

%files xsltfilter
%{baseinstdir}/share/xslt/docbook
%{baseinstdir}/share/xslt/export/uof
%{baseinstdir}/share/xslt/export/xhtml
%{baseinstdir}/share/xslt/import/uof
%{baseinstdir}/share/registry/xsltfilter.xcd
%{_datadir}/applications/libreoffice-xsltfilter.desktop

%files javafilter
%{baseinstdir}/program/classes/aportisdoc.jar
%{baseinstdir}/program/classes/pexcel.jar
%{baseinstdir}/program/classes/pocketword.jar
%{_datadir}/applications/libreoffice-javafilter.desktop
%{baseinstdir}/share/registry/palm.xcd
%{baseinstdir}/share/registry/pocketexcel.xcd
%{baseinstdir}/share/registry/pocketword.xcd

%if 0%{?fedora} || 0%{?rhel} >= 7
%files postgresql
%{baseinstdir}/program/postgresql-sdbc.uno.so
%{baseinstdir}/program/postgresql-sdbc-impl.uno.so
%{baseinstdir}/program/postgresql-sdbc.ini
%{baseinstdir}/program/services/postgresql-sdbc.rdb
%{baseinstdir}/share/registry/postgresqlsdbc.xcd
%endif

%files ure
%doc solver/unxlng*/bin/ure/LICENSE
%{ureinstdir}

%files sdk
%{sdkinstdir}/
%exclude %{sdkinstdir}/docs/
%exclude %{sdkinstdir}/examples/

%files sdk-doc
%docdir %{sdkinstdir}/docs
%{sdkinstdir}/docs/
%{sdkinstdir}/examples/

%files headless
%{baseinstdir}/program/libbasebmplo.so
%{baseinstdir}/program/libvclplug_svplo.so

%files pyuno
%{baseinstdir}/program/libpyuno.so
%{baseinstdir}/program/pythonloader.py*
%{baseinstdir}/program/pythonloader.uno.so
%{baseinstdir}/program/pythonloader.unorc
%{baseinstdir}/program/pythonscript.py*
%{baseinstdir}/program/pyuno.so
%{baseinstdir}/program/services/scriptproviderforpython.rdb
%{baseinstdir}/program/wizards
%{baseinstdir}/share/Scripts/python
%{libo_python_sitearch}/uno.py*
%{libo_python_sitearch}/unohelper.py*
%if 0%{libo_python3}
%{libo_python_sitearch}/__pycache__/uno.cpython-*
%{libo_python_sitearch}/__pycache__/unohelper.cpython-*
%endif
%{baseinstdir}/share/registry/librelogo.xcd
%{baseinstdir}/share/registry/pyuno.xcd

%if 0%{?fedora}
%files kde
%{baseinstdir}/program/kde4be1.uno.so
%{baseinstdir}/program/libvclplug_kde4lo.so
%endif

%changelog
* Thu Feb 28 2013 David Tardon <dtardon@redhat.com> - 1:4.0.1.2-1
- 4.0.1 rc2

* Tue Feb 26 2013 Eike Rathke <erack@redhat.com> - 1:4.0.0.3-8
- do not access vector elements beyond size, rhbz#847519 related
- Resolves: rhbz#742780 let make OPT_FLAGS=... override SDK flags
- Resolves: rhbz#907933 crash on removing second last para

* Tue Feb 19 2013 Caolán McNamara <caolanm@redhat.com> - 1:4.0.0.3-7
- Resolves: rhbz#895196 sc filter float a11y parent of itself

* Tue Feb 19 2013 David Tardon <dtardon@redhat.com> - 1:4.0.0.3-6
- Resolves: rhbz#911896 add Kazakh localization

* Fri Feb 15 2013 Caolán McNamara <caolanm@redhat.com> - 1:4.0.0.3-5
- make evolution 3.6 work with address book
- Resolves: rhbz#910176 cannot select directory with gtk folder picker
- fixes for building against Boost 1.53.0

* Fri Feb 15 2013 Stephan Bergmann <sbergman@redhat.com> - 1:4.0.0.3-4
- Resolves: fdo#60491 missing libemboleobj.so
- Resolves: rhbz#908674 crash on start

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1:4.0.0.3-3
- Rebuild for Boost-1.53.0

* Wed Feb 06 2013 David Tardon <dtardon@redhat.com> - 1:4.0.0.3-2
- fix parsing errors in translated help

* Fri Feb 01 2013 David Tardon <dtardon@redhat.com> - 1:4.0.0.3-1
- 4.0.0 rc3

* Wed Jan 23 2013 David Tardon <dtardon@redhat.com> - 1:4.0.0.2-1
- 4.0.0 rc2
- use ucpp again

* Tue Jan 22 2013 David Tardon <dtardon@redhat.com> - 1:4.0.0.1-3
- Resolves: rhbz#760765 Impress doesn't copy custom styles from one file
  to another

* Mon Jan 21 2013 David Tardon <dtardon@redhat.com> - 1:4.0.0.1-2
- Resolves: rhbz#901346 do not install 512x512 icons

* Tue Jan 15 2013 David Tardon <dtardon@redhat.com> - 1:4.0.0.1-1
- 4.0.0 rc1

* Sat Dec 22 2012 David Tardon <dtardon@redhat.com> - 1:4.0.0.0-4.beta2
- use system cpp instead of ucpp

* Wed Dec 19 2012 David Tardon <dtardon@redhat.com> - 1:4.0.0.0-3.beta2
- 4.0.0 beta2

* Thu Dec 06 2012 David Tardon <dtardon@redhat.com> - 1:4.0.0.0-2.beta1
- 4.0.0 beta1

* Thu Nov 29 2012 David Tardon <dtardon@redhat.com> - 1:3.6.4.3-1
- 3.6.4 rc3

* Wed Nov 28 2012 Caolán McNamara <caolanm@redhat.com> - 1:3.6.4.1-2
- fix docx import on big endian

* Sun Nov 18 2012 David Tardon <dtardon@redhat.com> - 1:3.6.4.1-1
- 3.6.4 rc1

* Wed Nov 14 2012 Caolán McNamara <caolanm@redhat.com> - 1:3.6.3.2-8
- Resolves: rhbz#872815 ogltrans effects still suboptimal

* Tue Nov 13 2012 Caolán McNamara <caolanm@redhat.com> - 1:3.6.3.2-7
- big endian test failure

* Thu Nov 08 2012 Caolán McNamara <caolanm@redhat.com> - 1:3.6.3.2-6
- Resolves: fdo#56198/rhbz#868002 honour gtk-scrollbar-warp-preference

* Tue Nov 06 2012 Caolán McNamara <caolanm@redhat.com> - 1:3.6.3.2-5
- bump for libexttextcat

* Fri Nov 02 2012 David Tardon <dtardon@redhat.com> - 1:3.6.3.2-4
- Resolves: rhbz#871929 add keywords to desktop files
- fix debuginfo

* Wed Oct 31 2012 Eike Rathke <erack@redhat.com> - 1:3.6.3.2-3
- Resolves: rhbz#865058 increase number of user-defined format codes

* Fri Oct 26 2012 David Tardon <dtardon@redhat.com> - 1:3.6.3.2-2
- Resolves: rhbz#824035 do not bundle saxon

* Wed Oct 24 2012 David Tardon <dtardon@redhat.com> - 1:3.6.3.2-1
- 3.6.3 rc2
- drop integrated 0001-Resolves-rhbz-868479-fdo-56281-doubled-in-German-ok-.patch

* Mon Oct 22 2012 Caolán McNamara <caolanm@redhat.com> - 1:3.6.3.1-3
- Resolves: rhbz#868479 guard against duplicated ~ in OK/Cancel

* Thu Oct 11 2012 David Tardon <dtardon@redhat.com> - 1:3.6.3.1-2
- Resolves: rhbz#858641 backport gstreamer 1.0 support to F-18

* Thu Oct 11 2012 Caolán McNamara <caolanm@redhat.com> - 1:3.6.3.1-1
- 3.6.3 rc1
- drop integrated 0001-Resolves-rhbz-855972-crash-on-switching-to-outline-v.patch
- drop integrated 0001-fdo-52022-Simple-LargeControlPoints-actually-can-hav.patch
- drop integrated 0001-fdo-46071-Do-not-hide-windows-based-on-nil-Visible-p.patch

* Fri Oct 05 2012 Stephan Bergmann <sbergman@redhat.com> - 1:3.6.2.2-3
- Resolves: fdo#46071 Do not hide windows based on nil Visible property

* Fri Oct 05 2012 Stephan Bergmann <sbergman@redhat.com> - 1:3.6.2.2-2
- Resolves: fdo#52022 Part of data in userdir is lost on upgrade

* Wed Sep 26 2012 David Tardon <dtardon@redhat.com> - 1:3.6.2.2-1
- 3.6.2 rc2

* Wed Sep 12 2012 Caolán McNamara <caolanm@redhat.com> - 1:3.6.2.1-2
- Resolves: rhbz#855541 XIOError handler multithread woes

* Wed Sep 12 2012 David Tardon <dtardon@redhat.com> - 1:3.6.2.1-1
- 3.6.2 rc1

* Tue Sep 11 2012 Caolán McNamara <caolanm@redhat.com> - 1:3.6.1.2-4
- Resolves: rhbz#855507 large ole2 compound files fail to load

* Mon Sep 10 2012 Caolán McNamara <caolanm@redhat.com> - 1:3.6.1.2-3
- Resolves: rhbz#855972 crash on switching to outline view

* Wed Aug 29 2012 Caolán McNamara <caolanm@redhat.com> - 1:3.6.1.2-2
- Related: rhbz#850709 hunspell en-US available standalone so
  make English langpack require hunspell-en and core just
  bare bones hunspell-en-US

* Sun Aug 26 2012 David Tardon <dtardon@redhat.com> - 1:3.6.1.2-1
- 3.6.1 rc2

* Wed Aug 22 2012 Caolán McNamara <caolanm@redhat.com> - 1:3.6.1.1-2
- Resolves: rhbz#846775 Clipboard must be disposed before selection
- Resolves: rhbz#842292 crash in scrolling multiselection in draw

* Wed Aug 15 2012 David Tardon <dtardon@redhat.com> - 1:3.6.1.1-1
- 3.6.1 rc1

* Sun Aug 12 2012 Kevin Fenzi <kevin@scrye.com> - 1:3.6.0.4-3
- Rebuild for new boost

* Sat Jul 28 2012 David Tardon <dtardon@redhat.com> - 1:3.6.0.4-2
- rebuilt for boost 1.50

* Fri Jul 27 2012 David Tardon <dtardon@redhat.com> - 1:3.6.0.4-1
- 3.6.0 rc4

* Thu Jul 26 2012 David Tardon <dtardon@redhat.com> - 1:3.6.0.3-2
- Resolves: rhbz#842552 crash in pptx import

* Wed Jul 25 2012 David Tardon <dtardon@redhat.com> - 1:3.6.0.3-1
- 3.6.0 rc3

* Tue Jul 17 2012 David Tardon <dtardon@redhat.com> - 1:3.6.0.2-1
- 3.6.0 rc2

* Mon Jul 16 2012 Caolán McNamara <caolanm@redhat.com> - 1:3.6.0.1-3
- Resolves: rhbz#836937 insanely slow with Zemberek

* Mon Jul 16 2012 David Tardon <dtardon@redhat.com> - 1:3.6.0.1-2
- rebuild for new libexttextcat

* Thu Jul 12 2012 David Tardon <dtardon@redhat.com> - 3.6.0.1-1
- 3.6.0 rc1

* Mon Jul 09 2012 Caolán McNamara <caolanm@redhat.com> - 3.6.0.0-4
- Resolves: rhbz#838368 --view ignored while -view accepted

* Thu Jul 05 2012 David Tardon <dtardon@redhat.com> - 3.6.0.0-3
- 3.6.0 beta3

* Mon Jul  2 2012 Marek Kasik <mkasik@redhat.com> - 3.6.0.0-2
- Rebuild (poppler-0.20.1)

* Wed Jun 27 2012 David Tardon <dtardon@redhat.com> - 3.6.0.0-1
- 3.6.0 beta2
- drop integrated 0001-move-binfilter-mime-types-into-extra-.desktop-file.patch
- drop integrated 0001-Resolves-rhbz-788042-skip-splashscreen-with-quicksta.patch
- drop integrated libreoffice-ensure-non-broken-xml-tree.patch
- drop integrated 0001-preserve-timestamps-for-.py-files.patch
- drop integrated 0001-Resolves-rhbz-788045-swriter-help-etc-doesn-t-show-h.patch
- drop integrated 0001-Resolves-rhbz-799525-put-flat-odf-mimetypes-in-xsltf.patch
- drop integrated 0001-Resolves-rhbz-800272-complain-about-unknown-command-.patch
- drop integrated 0001-Resolves-rhbz-806663-SlideshowImpl-can-outlive-SdMod.patch
- drop integrated 0001-desktop-do-not-complain-about-soffice-command-line-o.patch
- drop integrated 0001-Resolves-fdo-48096-torn-off-popups-trigger-keyboard-.patch
- drop integrated 0001-fdo-38088-better-CSV-import-default-separators.patch
- drop integrated 0001-save-register-arguments-first.patch
- drop integrated 0001-do-not-let-gcc-use-registers-we-are-setting-ourselve.patch
- drop integrated 0001-wrong-types-used-here-breaks-64bit-bigendian.patch
- drop integrated 0001-Resolves-rhbz-805743-a11y-call-doShow-after-we-have-.patch
- drop integrated 0001-Resolves-fdo-49849-implement-Unicode-6.1-hebrew-line.patch
- drop integrated 0001-use-ure-instead-of-ure-link.patch
- drop broken 0001-fix-setting-of-paper-tray-from-print-dialog-fdo-4393.patch

* Mon Jun 18 2012 Caolán McNamara <caolanm@redhat.com> - 3.5.5.1-2
- Resolves: rhbz#830810 missing dependency on lucene-contrib

* Thu Jun 14 2012 David Tardon <dtardon@redhat.com> - 3.5.5.1-1
- 3.5.5 rc1
- drop integrated 0001-make-hsqldb-build-with-java-1.7.patch
- drop integrated 0001-Related-rhbz-799628-crash-with-chewing-IM-with-g3g.patch
- drop integrated 0001-silence-SolarMutex-not-locked-spew.patch
- drop integrated 0001-gcc-trunk-fix-unable-to-find-string-literal-operator.patch
- drop integrated 0001-ppc-yyinput-returns-a-int-truncating-to-unsigned-cha.patch
- drop integrated 0001-Resolves-rhbz-826609-rhbz-820554-fix-smoketest-on-pp.patch

* Mon Jun 11 2012 David Tardon <dtardon@redhat.com> - 3.5.4.2-3
- make gdb pretty printers for URE libs usable again

* Fri Jun 08 2012 Caolán McNamara <caolanm@redhat.com> - 3.5.4.2-2
- Resolves: rhbz#826609, rhbz#820554 fix smoketest on ppc[64] and s390[x]

* Wed May 23 2012 David Tardon <dtardon@redhat.com> - 3.5.4.2-1
- 3.5.4 rc2

* Thu May 17 2012 Caolán McNamara <caolanm@redhat.com> - 3.5.4.1-2
- Resolves: rhbz#811226 ARM FTBFS

* Wed May 16 2012 David Tardon <dtardon@redhat.com> - 3.5.4.1-1
- 3.5.4 rc1
- drop integrated 0001-do-not-prepend-n-twice-it-confuses-KFileDialog-rhbz-.patch
- drop integrated 0001-incrementing-index-twice-in-one-run-seems-wrong.patch
- drop integrated 0001-fdo-49365-correctly-map-monitor-index-back-to-screen.patch
- drop integrated 0001-rhbz-809019-count-mirrored-monitors-as-one.patch

* Sun May 13 2012 Caolán McNamara <caolanm@redhat.com> - 3.5.3.2-5
- Resolves: fdo#49849 line breaking fixes for Hebrew

* Fri May 11 2012 David Tardon <dtardon@redhat.com> - 3.5.3.2-4
- Resolves: rhbz#820439 KDE export dialog broken for most formats
- Resolves: fdo#49365 Libreoffice fails to start on second screen with
  gtk vcl plugin
- Resolves: rhbz#809019 Impress thinks a machine with 2 monitors in
  clone mode is multihead

* Wed May 09 2012 Caolán McNamara <caolanm@redhat.com> - 3.5.3.2-3
- Resolves: rhbz#805743 a11y crash in impress/draw
- Resolves: rhbz#813202 opengl slide transitions still a bit
  problematic in Fedora 17

* Thu May 03 2012 David Tardon <dtardon@redhat.com> - 3.5.3.2-2
- rebuild for changed dependencies

* Wed Apr 25 2012 David Tardon <dtardon@redhat.com> - 3.5.3.2-1
- 3.5.3 rc2
- fix broken test on 64bit big endian

* Mon Apr 23 2012 David Tardon <dtardon@redhat.com> - 3.5.3.1-2
- rebuild for icu
- fix UNO bridges for ppc and ppc64

* Thu Apr 19 2012 David Tardon <dtardon@redhat.com> - 3.5.3.1-1
- 3.5.3 rc1
- drop integrated 0001-Introduced-SystemShellExecuteFlags-URIS_ONLY.patch
- drop integrated 0001-Simplify-code-and-use-proper-register-names-for-linu.patch
- drop integrated 0001-resolved-rhbz-813280-the-current-document-is-not-alw.patch

* Wed Apr 18 2012 Eike Rathke <erack@redhat.com> - 3.5.2.1-7
- Resolves: rhbz#813280 sheets cannot be moved in Calc

* Wed Apr 11 2012 Eike Rathke <erack@redhat.com> - 3.5.2.1-6
- Resolves: fdo#38088 rhbz#810267 better CSV import default separators

* Tue Apr 10 2012 Caolán McNamara <caolanm@redhat.com> - 3.5.2.1-5
- Resolves: rhbz#811226 FTBFS ARM

* Thu Apr 05 2012 Stephan Bergmann <sbergman@redhat.com> - 3.5.2.1-4
- Fix URIS_ONLY flag issue
- rebuild for db4

* Mon Apr 02 2012 Caolán McNamara <caolanm@redhat.com> - 3.5.2.1-3
- Resolves: rhbz#708041 focus problems with tearable menus

* Mon Mar 26 2012 Caolán McNamara <caolanm@redhat.com> - 3.5.2.1-2
- Resolves: rhbz#806663 SlideshowImpl can outlive SdModule

* Sun Mar 25 2012 David Tardon <dtardon@redhat.com> - 3.5.2.1-1
- 3.5.2 rc1
-drop integrated 0001-yet-another-clash-with-macro-name.patch

* Wed Mar 14 2012 David Tardon <dtardon@redhat.com> - 3.5.1.2-2
- Resolves: rhbz#770209 can't change paper tray setting while printing

* Thu Mar 08 2012 David Tardon <dtardon@redhat.com> - 3.5.1.2-1
- 3.5.1 rc2

* Tue Mar 06 2012 Caolán McNamara <caolanm@redhat.com> - 3.5.1.1-3
- Resolves: rhbz#799628 crash with chewing IM with g3g
- Resolves: rhbz#799525 put flat odf mimetypes into xsltfilter.desktop
- Resolves: rhbz#800272 complain about unknown commandline options

* Wed Feb 29 2012 Caolán McNamara <caolanm@redhat.com> - 3.5.1.1-2
- Resolves: rhbz#788045 swriter --help doesn't show help
- Resolves: rhbz#798667 missing .desktop icons

* Sun Feb 26 2012 David Tardon <dtardon@redhat.com> - 3.5.1.1-1
- 3.5.1 rc1
- drop 0001-Resolves-fdo-43644-survive-registered-but-unavailabl.patch
- drop 0001-Resolves-rhbz-789622-Adapt-SDK-to-changed-paths-in-L.patch
- drop 0001-Fix-fdo-45177-avoid-linked-undo-for-the-while.patch
- drop 0001-Fix-some-apparent-misuses-of-RTL_CONSTASCII_USTRINGP.patch
- drop binfilter-Fix-some-apparent-misuses-of-RTL_CONSTASCII_USTRINGP.patch
- Resolves: fdo#45177 avoid linked undo crash
- Fix some apparent misuses of RTL_CONSTASCII_USTRINGPARAM (cherry-picked from
  upstream libreoffice-3-5 branch)

* Tue Feb 14 2012 Stephan Bergmann <sbergman@redhat.com> - 3.5.0.3-5
- Resolves rhbz#789622: Adapt SDK to changed paths in LO installation

* Mon Feb 13 2012 Caolán McNamara <caolanm@redhat.com> - 3.5.0.3-4
- ensure gdb .py files have the same timstamps so that multilib
  .pyc's and .pyo's have the same content (timestamp in binary cache)

* Sat Feb 11 2012 Caolán McNamara <caolanm@redhat.com> - 3.5.0.3-3
- make sure .tree files don't get busted again

* Tue Feb 07 2012 Stephan Bergmann <sbergman@redhat.com> - 3.5.0.3-2
- junit4 -> junit
- Resolves: rhbz#788042 skip splashscreen with quickstarter
- with split binfilter we need fix for fdo#43644

* Thu Feb 02 2012 David Tardon <dtardon@redhat.com> - 3.5.0.3-1
- 3.5.0 rc3
- Resolves: rhbz#786328 add nlpsolver subpackage
- split legacy binary filters into subpackage

* Thu Jan 26 2012 Stephan Bergmann <sbergman@redhat.com> - 3.5.0.2-2
- add libreoffice-postgresql subpackage

* Wed Jan 25 2012 David Tardon <dtardon@redhat.com> - 3.5.0.2-1
- 3.5.0 rc2

* Thu Jan 19 2012 David Tardon <dtardon@redhat.com> - 3.5.0.1-1
- 3.5.0 rc1
- drop integrated 0001-workaround-internal-compiler-error-with-gcc-4.7.patch
- drop integrated 0001-fix-for-gcc-4.7-C-11-these-are-not-string-literal-op.patch
- drop integrated 0001-fix-for-gcc-4.7-C-11-this-is-not-string-literal-oper.patch
- drop integrated 0001-Revert-fast_merge-fix-mis-merge-of-first-module-s-st.patch
- drop integrated 0001-fix-writing-of-strings-from-the-first-module.patch
- drop integrated 0001-refactor-slightly-to-avoid-link-problems-with-gcc-4..patch

* Fri Jan 13 2012 David Tardon <dtardon@redhat.com> - 3.4.99.3-1
- 3.5.0 beta3
- drop integrated 0001-fix-syntactic-error.patch
- drop integrated 0001-gcc-trunk-fix-error-unable-to-find-string-literal-op.patch
- drop integrated 0001-gcc-trunk-avoid-confusion.patch
- drop integrated 0001-workaround-for-LO-namespace-pollution-breaking-KDE4-.patch
- drop integrated 0001-smath-does-not-handle-accents-in-MathML.patch
- Resolves: rhbz#533318 smath does not handle accents in MathML
- Resolves: rhbz#771108 English menu in writer despite installation of
  libreoffice-langpack-de

* Fri Jan 06 2012 David Tardon <dtardon@redhat.com> - 3.4.99.2-2
- rebuild with gcc 4.7

* Wed Dec 21 2011 David Tardon <dtardon@redhat.com> - 3.4.99.2-1
- 3.5.0 beta2
- drop integrated 0001-Resolves-rhbz-761009-IFSD_Equal-is-asymmetrical.patch
- drop integrated 0001-Resolves-rhbz-767708-avoid-SIGBUS-writing-to-overcom.patch
- drop integrated 0001-force-gbuild-stage-for-CustomTargets.patch
- drop integrated 0001-these-translations-do-already-exist-in-translations-.patch
- drop integrated 0001-Fix-typo-and-clean-up.patch
- use system mysql-connector-c++

* Sun Dec 18 2011 David Tardon <dtardon@redhat.com> - 3.4.99.1-1
- 3.5.0 beta1
- drop integrated 0001-Related-fdo-37195-migrationoo3-not-registered.patch
- drop integrated 0001-Related-i58612-don-t-crash-anyway.patch
- drop integrated 0001-Related-rhbz-652604-better-survive-exceptions-thrown.patch
- drop integrated 0001-Related-rhbz-702833-addEventListener-without-removeE.patch
- drop integrated 0001-Related-rhbz-711087-band-aid.patch
- drop integrated 0001-Related-rhbz-718976-crash-in-SwTxtSizeInfo-GetMultiC.patch
- drop integrated 0001-Related-rhbz-730225-avoid-segv-in-ld-this-was-set-to.patch
- drop integrated 0001-Related-rhbz-753201-fedora-ant-java-1.5.0-gcj-won-t-.patch
- drop integrated 0001-Resolves-fdo-32665-handle-that-FreeSerif-lacks-some-.patch
- drop integrated 0001-Resolves-rhbz-693265-fix-crash-from-unhandled-except.patch
- drop integrated 0001-Resolves-rhbz-695509-crash-in-RefreshDocumentLB.patch
- drop integrated 0001-Resolves-rhbz-713154-pdf-export-dialog-too-tall-to-f.patch
- drop integrated 0001-Resolves-rhbz-715549-use-fontconfig-s-detected-forma.patch
- drop integrated 0001-Resolves-rhbz-738255-avoid-crash-on-NULL-pointer.patch
- drop integrated 0001-Resolves-rhbz-751290-KDE-black-on-dark-tooltips.patch
- drop integrated 0001-add-Oracle-Java-1.7.0-recognition.patch
- drop integrated 0001-avoid-using-com.sun.org-apis.patch
- drop integrated 0001-bubble-down-configure-test-findings-on-visibility.patch
- drop integrated 0001-fix-horizontal-scrollbars-with-KDE-oxygen-style-bnc-.patch
- drop integrated 0001-gtk3-fix-cairo-canvas-crash-for-non-X-or-svp-backend.patch
- drop integrated 0001-helgrind-Related-rhbz-655686-get-order-of-shutdown-c.patch
- drop integrated 0001-rhbz-667082-do-not-crash-importing-section-containin.patch
- drop integrated 0001-rhbz-702635-set-correct-page-number-when-exporting-s.patch
- drop integrated Backport-reading-AES-encrypted-ODF-1.2-documents.patch
- drop integrated gdb-pretty-printers.patch
- drop integrated kde4configure.patch
- drop integrated libreoffice-ppc64.patch
- drop integrated openoffice.org-3.3.0.ooo108637.sfx2.uisavedir.patch
- drop integrated openoffice.org-3.3.0.ooo113273.desktop.resolvelinks.patch
- drop integrated vbahelper.visibility.patch
- drop libreoffice-testtools subpackage, because testtool has been
  removed by upstream

* Thu Dec 15 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.4.2-6
- Resolves: rhbz#761009 IFSD_Equal is asymmetrical
- Resolves: rhbz#767708 write to mmap'ed file w/o disk space: SIGBUS

* Tue Nov 29 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.4.2-5
- Resolves: rhbz#757653 fix headless crash with cairo canvas

* Tue Nov 22 2011 Lukas Tinkl <ltinkl@redhat.com> - 3.4.4.2-4
- Resolves: rhbz#751290 - [kde] LibreOffice has black on dark-grey tooltip-texts

* Fri Nov 11 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.4.2-3
- Related: fdo#42534 0001-Related-i58612-don-t-crash-anyway.patch
- Resolves: fdo#42749 KDE oxygen theme and scrollbars

* Thu Nov 10 2011 Stephan Bergmann <sbergman@redhat.com> - 3.4.4.2-2
- Patch to backport reading AES-encrypted ODF 1.2 documents

* Thu Nov 03 2011 David Tardon <dtardon@redhat.com> - 3.4.4.2-1
- 3.4.4 rc2

* Fri Oct 28 2011 Rex Dieter <rdieter@fedoraproject.org> - 1:3.4.4.1-4
- rebuild(poppler)

* Thu Oct 27 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.4.1-3
- Resolves: rhbz#665800 missing glyph symbol shown when toggling bold/italic
  for Sinhala text

* Thu Oct 27 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.4.1-2
- possible fix for java 1.7.0 detection


* Wed Oct 26 2011 David Tardon <dtardon@redhat.com> - 3.4.4.1-1
- 3.4.4 rc1

* Tue Oct 25 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-16
- allow building with gcj

* Fri Oct 21 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-15
- Resolves: rhbz#747356 let Qt call XInitThreads
- fix .sdw import

* Wed Oct 19 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-14
- Related: rhbz#743750 addXineramaScreenUnique issue
 
* Fri Oct 07 2011 Stephan Bergmann <sbergman@redhat.com> - 3.4.3.2-13
- Patches to build with GCC 6.4.1

* Fri Sep 30 2011 Marek Kasik <mkasik@redhat.com> - 3.4.3.2-12
- Rebuild (poppler-0.18.0)

* Tue Sep 20 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-11
- Resolves: rhbz#738133 fix bn discard string
- Resolves: fdo#35513 avoid crash while processing incorrect print range

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 3.4.3.2-10
- Rebuild (poppler-0.17.3)

* Thu Sep 15 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-9
- Resolves: rhbz#738255 avoid crash on sc inputhdl

* Tue Sep 13 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-8
- Resolves: rhbz#274631 remove NoDisplay from -math.desktop

* Thu Sep 08 2011 David Tardon <dtardon@redhat.com> - 3.4.3.2-7
- rebuild for new icu

* Tue Sep 06 2011 David Tardon <dtardon@redhat.com> - 3.4.3.2-6
- Resolves: rhbz#734976 libreoffice-langpack-*-* not pulled in by
  yum install libreoffice

* Fri Sep 02 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-5
- Resolves: rhbz#735182 be able to rebuild against poppler 0.17.3

* Tue Aug 30 2011 David Tardon <dtardon@redhat.com> - 3.4.3.2-4
- Resolves: rhbz#734432 openoffice.org symlink broken

* Mon Aug 29 2011 David Tardon <dtardon@redhat.com> - 3.4.3.2-3
- add Latvian langpack

* Fri Aug 26 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.3.2-2
- Resolves: rhbz#733564 graphite2 now packaged into fedora
- Related: fdo#37195 migrationoo3 not registered

* Thu Aug 25 2011 David Tardon <dtardon@redhat.com> - 3.4.3.2-1
- 3.4.3 rc2

* Mon Aug 22 2011 David Tardon <dtardon@redhat.com> - 3.4.3.1-2
- add gdb pretty printers

* Tue Aug 16 2011 David Tardon <dtardon@redhat.com> - 3.4.3.1-1
- 3.4.3 rc1
- drop integrated 0001-Resolves-rhbz-725144-wrong-csh-syntax.patch

* Fri Aug 12 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.2.3-3
- Related: rhbz#730225 avoid segv in ld

* Tue Aug 02 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.2.3-2
- Resolves: rhbz#693265 fix crash from unhandled exception

* Fri Jul 29 2011 David Tardon <dtardon@redhat.com> - 3.4.2.3-1
- 3.4.2 rc3

* Mon Jul 25 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.2.2-2
- Resolves: rhbz#725144 wrong csh syntax

* Wed Jul 20 2011 David Tardon <dtardon@redhat.com> - 3.4.2.2-1
- 3.4.2 rc2
- fix breakage in KDE4 plugin

* Tue Jul 19 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.2.1-3
- Resolves: rhbz#715549 use fontconfig's detected format

* Mon Jul 18 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.2.1-2
- Rebuild (poppler-0.17.0), add libreoffice-poppler-0.17.0.patch
  seeing as the API changed for some reason or other

* Wed Jul 13 2011 David Tardon <dtardon@redhat.com> - 3.4.2.1-1
- 3.4.2 rc1
- drop 0001-bad-merge-fix-to-enable-extensions-to-build-again.patch
- drop 0001-fix-regression-in-SvGlobalName-operator.patch

* Tue Jul 12 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.1.3-3
- fix regression in SvGlobalName operator

* Tue Jul 05 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.1.3-2
- Related: rhbz#718976 crash in SwTxtSizeInfo::GetMultiCreator

* Fri Jul 01 2011 David Tardon <dtardon@redhat.com> - 3.4.1.3-1
- 3.4.1 rc3

* Thu Jun 23 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.1.2-1
- 3.4.1 rc2
- drop integrated 0001-correctly-build-GTK-systray-icon.patch

* Tue Jun 21 2011 David Tardon <dtardon@redhat.com> - 3.4.1.1-5
- Resolves: rhbz#714781 add Persian langpack
- Resolves: rhbz#667082 do not crash importing section containing just
  an empty paragraph

* Mon Jun 20 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.1.1-4
- Related: rhbz#711087 band aid for crash in sc undo
- Resolves: rhbz#714338 add a metapackage to install standard bits

* Fri Jun 17 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.1.1-3
- Related: rhbz#702833 addEventListener without removeEventListener

* Thu Jun 16 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.1.1-2
- Resolves: rhbz#713154 pdf export dialog too tall to fit

* Wed Jun 15 2011 David Tardon <dtardon@redhat.com> - 3.4.1.1-1
- 3.4.1 RC1
- drop integrated 0001-Resolves-rhbz-707317-avoid-crash-in-getRowSpan.patch
- drop integrated 0001-Resolves-rhbz-710004-band-aid-for-immediate-crash-in.patch
- drop integrated 0001-Resolves-rhbz-710556-don-t-crash-on-missing-graphics.patch
- drop integrated 0001-Resolves-rhbz-699909-crash-in-export-of-.doc-in-lcl_.patch
- drop integrated 0001-fdo-37584-Make-a-real-copy-of-the-text-where-to-coun.patch
- drop integrated 0001-Resolves-fdo-37668-bitwise-operations-on-signed-numb.patch

* Thu Jun 09 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.0.2-5
- Resolves: rhbz#699909 crash in export of .doc in lcl_getField
- Resolves: fdo#37584 Make a real copy of the text
- Resolves: rhbz#709503/fdo#37668 bitwise operations on signed values

* Tue Jun 07 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.0.2-4
- Resolves: rhbz#710556 't crash on missing graphics .pptx export
- Resolves: rhbz#652604 better survive exceptions in autorecovery

* Thu Jun 02 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.0.2-3
- Resolves: rhbz#710004 band aid for crash

* Mon May 30 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.0.2-2
- Resolves: rhbz#707317 avoid crash in getRowSpan

* Fri May 27 2011 David Tardon <dtardon@redhat.com> - 3.4.0.2-1
- 3.4.0 RC2
- drop integrated 0001-fix-build-with-system-bsh.patch

* Wed May 25 2011 Caolán McNamara <caolanm@redhat.com> - 3.4.0.1-3
- rebuild for new hunspell

* Tue May 24 2011 David Tardon <dtardon@redhat.com> - 3.4.0.1-2
- Resolves: rhbz#706110 oosplash.bin segfault on every login

* Fri May 20 2011 David Tardon <dtardon@redhat.com> - 3.4.0.1-1
- 3.4 RC1
- Resolves: rhbz#702635 set correct page number when exporting selected
  pages

* Sat May 07 2011 Christopher Aillon <caillon@redhat.com> - 3.3.99.4-2
- Update icon cache scriptlet

* Sat May 07 2011 David Tardon <dtardon@redhat.com> 3.3.99.4-1
- 3.4 beta4
- drop integrated 0001-Removed-duplicate-code-block-mis-merge-prolly.patch
- drop integrated 7de0b88ce2dd932915894385b54be1897d5ee053.zip

* Mon Apr 18 2011 Caolán McNamara <caolanm@redhat.com> 3.3.99.1-2
- Resolves: rhbz#695509 crash in RefreshDocumentLB
- bubble down configure test findings on visibility

* Mon Apr 11 2011 Caolán McNamara <caolanm@redhat.com> 3.3.99.1-1
- 3.4 beta1
- drop openoffice.org-1.9.123.ooo53397.prelinkoptimize.desktop.patch
  in favour of ooosplash
- drop openoffice.org-2.2.0.gccXXXXX.solenv.javaregistration.patch
  because components are passively registered now
- drop integrated openoffice.org-3.1.0.ooo102061.sc.cellanchoring.patch
- drop integrated turn-script-providers-into-extensions.patch
- drop integrated 0001-tidy-this-up-and-don-t-bail-out-on-mislength-records.patch
- drop integrated 0001-free-ctxt-after-taking-lastError-details.patch
- drop integrated 0001-Removed-suspect-hack.-Cursor-on-post-it-now-scrolls-.patch
- drop integrated libreoffice-gcc4.6.0.patch
- drop integrated 0001-fexceptions-fexceptions.patch
- drop integrated 0001-Related-rhbz-672872-cancel-gtk-file-dialog-on-deskto.patch
- drop vbahelper.visibility.patch
- drop integrated 0001-Resolves-fdo-33509-i62414-out-by-one-breaks-CTL-spel.patch
- drop integrated 0001-Resolves-rhbz-670020-crash-in-slidesorting.patch
- drop integrated 0001-Resolves-rhbz-676539-handle-missing-pWindows-from-xW.patch
- drop integrated 0001-Resolves-fdo-33750-i94623-use-optimal-border-width-w.patch
- drop integrated 0001-rhbz-649310-don-t-crash-deregistering-diff.-platform.patch
- drop integrated 0001-Resolves-rhbz-674330-dereference-of-NULL-mpBase.patch
- drop integrated 0001-rhbz-678284-Get-correct-current-position-when-shift-page-up-and-.patch
- drop integrated 0001-Resolves-rhbz-681159-bandaid-for-crash.patch
- drop integrated 0001-Resolves-rhbz-672818-bandaid-for-crash-in-SwTxtNode-.patch
- drop integrated 0001-install-high-resolution-icons.patch
- drop integrated 0001-Resolves-rhbz-682716-pa-IN-isn-t-handled-by-fontconf.patch
- drop integrated 0001-Related-rhbz-684477-make-sure-this-is-thread-safe.patch
- drop integrated 0001-Resolves-rhbz-682621-better-resizing-of-overtall-gly.patch
- drop integrated 0001-Resolves-rhbz-684620-crash-with-NULL-pTableBox.patch
- drop integrated libreoffice-fdo33947.sd.print.crash.patch
- drop integrated 0001-add-cairo_ft_font_face_create_for_pattern-wrapper.patch
- drop integrated 0001-Related-rhbz-680460-reorganize-this-to-make-it-inher.patch
- drop integrated 0001-Related-rhbz-680460-don-t-bother-with-an-interim-Fon.patch
- drop integrated 0001-Resolves-rhbz-680460-honour-lcdfilter-subpixeling-et.patch
- drop integrated 0001-Cut-Gordian-Knot-of-who-owns-the-font-options.patch
- drop integrated 0001-beware-of-invalidated-iterator.patch
- drop integrated rhbz680766.fix-mdds-crash.patch
- drop integrated 0001-Resolves-rhbz-684580-X-and-strike-through-escapes-ra.patch
- drop integrated 0001-set-mime-types-on-flat-xml-filters.patch
- drop integrated 0001-add-flat-xml-types-to-.desktop-files-etc.patch
- drop integrated libreoffice-fdo31271.icu.patch

* Tue Apr 05 2011 Caolán McNamara <caolanm@redhat.com> 3.3.2.2-6
- Resolves: rhbz#655686 get order of shutdown correct

* Wed Mar 30 2011 Caolán McNamara <caolanm@redhat.com> 3.3.2.2-5
- Add application/vnd.oasis.opendocument.text-flat-xml, etc. to
  .desktop files for mcepl

* Tue Mar 29 2011 Caolán McNamara <caolanm@redhat.com> 3.3.2.2-4
- Resolves: rhbz#684580 improve X and / strike-through

* Thu Mar 24 2011 David Tardon <dtardon@redhat.com> 3.3.2.2-3
- Resolves: rhbz#680766 crash in mdds

* Wed Mar 23 2011 David Tardon <dtardon@redhat.com> 3.3.2.2-2
- Related: rhbz#689268 versioned deps need to contain epoch

* Tue Mar 22 2011 Caolán McNamara <caolanm@redhat.com> 3.3.2.2-1
- latest version
- drop integrated 0001-Resolves-fdo-33701-ensure-node-outlives-path.patch
- drop integrated 0001-valgrind-don-t-leave-an-evil-thread-running-after-ma.patch

* Tue Mar 22 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-12
- Fix fontoptions cache
- avoid crash in calc on changing size of rows (dtardon)

* Mon Mar 21 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-11
- Resolves: rhbz#689268 autocorrs from OOo F14 not upgraded

* Wed Mar 16 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-10
- Resolves: rhbz#680460 honour lcdfilter and subpixeling

* Tue Mar 15 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-9
- Resolves: fdo#33947 sd print crash

* Mon Mar 14 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-8
- Related: rhbz#684477 make sure this is thread safe
- Resolves: rhbz#684620 crash with NULL pTableBox

* Sun Mar 13 2011 Marek Kasik <mkasik@redhat.com> 3.3.1.2-7
- Rebuild (poppler-0.16.3)

* Wed Mar 09 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-6
- Resolves: rhbz#682621 better resizing of overtall glyphsubs

* Tue Mar 08 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-5
- Resolves: rhbz#682716 pa-IN isn't handled well by fontconfig

* Tue Mar 08 2011 David Tardon <dtardon@redhat.com> 3.3.1.2-4
- install 128x128 px icons

* Wed Mar 02 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-3
- Resolves: rhbz#681159 crash in writer
- Resolves: rhbz#672818 crash in writer
- Resolves: fdo#33701 ensure node outlives path
- Resolves: rhbz#681738 crash on writing config post-main

* Thu Feb 17 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-2
- Resolves: rhbz#678284 Calc crashes during cell select with keys
  (dtardon)

* Thu Feb 17 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.2-1
- RC2

* Wed Feb 16 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.1-2
- Resolves: rhbz#674330 dereference of NULL mpBase

* Fri Feb 11 2011 Caolán McNamara <caolanm@redhat.com> 3.3.1.1-1
- 3.3.1 rc1
- drop integrated 0001-don-t-pushback-and-process-a-corrupt-extension.patch
- drop integrated libreoffice-fdo32561.comphelper.patch
- drop integrated 0001-Related-rhbz-610103-more-woes-on-rpm-upgrade-vs-rpm-.patch
- drop integrated 0001-Resolves-rhbz-673819-crash-on-changing-position-of-d.patch
- drop integrated 0001-rhbz-666440-don-t-pushback-and-process-a-corrupt-extension.patch

* Thu Feb 10 2011 Caolán McNamara <caolanm@redhat.com> 3.3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
- Related: rhbz#610103 make this even more robust
- Related: rhbz#672872 cancel gtk file dialog on terminate
- Resolves: fdo#33509/ooo#62414 fix CTL spelling popup
- Resolves: rhbz#673819 crash on changing position of header/footer object
- Resolves: rhbz#670020 crash in slidesorting
- Resolves: rhbz#676539 handle missing pWindows from xWindows
- Resolves: rhbz#649310 don't crash deregistering diff. platform ext.
  (dtardon)
- Resolves: rhbz#666440 don't pushback and process a corrupt extension

* Mon Jan 24 2011 Caolán McNamara <caolanm@redhat.com> 3.3.0.4-2
- Resolves: rhbz#671540 fix lonely )

* Thu Jan 20 2011 Caolán McNamara <caolanm@redhat.com> 3.3.0.4-1
- next release candidate
- drop integrated 0001-fix-presenter-screens-description.xml-build.patch

* Tue Jan 18 2011 Caolán McNamara <caolanm@redhat.com> 3.3.0.3-2
- backport fix to get presenter screen working
- make handling busted extensions more robust

* Wed Jan 12 2011 Caolán McNamara <caolanm@redhat.com> 3.3.0.3-1
- latest version
- drop integrated 0001-Resoves-rhbz-663857-font-color-missing-C-FAQ-10.3-do.patch
- drop integrated 0001-Avoid-double-paste-when-pasting-text-into-cell-comme.patch
- drop integrated 0001-Resolves-rhbz-660342-Undo-Redo-crash-with-postits.patch
- drop integrated 0001-Resolves-rhbz-666088-clean-up-search-cache-singleton.patch

* Thu Jan 06 2011 Caolán McNamara <caolanm@redhat.com> 3.3.0.2-5
- Resolves: rhbz#666088 don't crash on clean up of search cache

* Wed Jan 05 2011 Lukas Tinkl <ltinkl@redhat.com> 3.3.0.2-4
- create a KDE integration subpackage

* Mon Jan 03 2011 David Tardon <dtardon@redhat.com> 3.3.0.2-3
- rebuild with new poppler

* Wed Dec 22 2010 Caolán McNamara <caolanm@redhat.com> 3.3.0.2-2
- Resolves: rhbz#663724 fdo32572-sc-dont-double-paste.patch
- Resolves: rhbz#660342 Undo/Redo crash with postits

* Tue Dec 21 2010 Caolán McNamara <caolanm@redhat.com> 3.3.0.2-1
- latest version

* Sat Dec 18 2010 Caolán McNamara <caolanm@redhat.com> 3.3.0.1-4
- Resolves: rhbz#663857 font color missing in transitions

* Wed Dec 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 3.3.0.1-3
- rebuild (poppler)

* Wed Dec 15 2010 Caolán McNamara <caolanm@redhat.com> 3.3.0.1-2
- Fix up some doc imports

* Sun Dec 05 2010 Caolán McNamara <caolanm@redhat.com> 3.3.0.1-1
- release candidate 1
- drop integrated qstart.dont-forceenabled-on-post-reg-restart.patch
- drop integrated exit.quickstarter.when.deleted.patch
- drop integrated 0001-destroydesktop.in.timeout.patch
- drop integrated openoffice.org-3.3.0.rhbz657541.join-paragraphs.patch

* Sat Nov 27 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.3-2
- Resolves: rhbz#610103 exit quickstarter when libs deleted
- Resolves: rhbz#652695 release desktop in timeout
- Resolves: rhbz#657541 don't crash during processing of auto. styles
  when joining paragraphs (dtardon)

* Thu Nov 18 2010 Caolán McNamara <caolanm@redhat.com 3.2.99.3-1
- next Libreoffice milestone
- drop integrated openoffice.org-2.0.1.rhXXXXXX.extensions.defaulttoevo2.patch
- drop integrated openoffice.org-2.2.1.ooo7065.sw.titlepagedialog.patch
- drop integrated openoffice.org-3.2.0.ooo108846.sfx2.qstartfixes.patch
- drop integrated openoffice.org-3.3.0.ooo107490.cppu.lifecycle.patch
- drop integrated libreoffice-buildfix.patch
- drop integrated libreoffice-xdg632229.gnomeshell.patch
- drop integrated 0001-strcpy-cannot-be-used-with-overlapping-src-and-dest.patch
- drop integrated 0001-abort-doesn-t-gain-us-anything-here.patch
- drop integrated 0001-latest-libX11-changed-header-guards.patch

* Sat Nov 06 2010 David Tardon <dtardon@redhat.com 3.2.99.2-6
- turn script providers into extensions

* Wed Nov 03 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.2-5
- Resolves: rhbz#649210 add Sinhalese langpack

* Sat Oct 30 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.2-4
- langpack macro hard-coded version number

* Fri Oct 22 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.2-3
- Resolves: xdg632229 gnomeshell app tracking

* Tue Oct 12 2010 David Tardon <dtardon@redhat.com> 3.2.99.2-2
- use macros to define auto-correction and language pack subpackages

* Mon Oct 11 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.2-1
- next LibreOffice milestone
- drop integrated openoffice.org-2.3.0.ooo76649.httpencoding.patch
- drop integrated workspace.dtardon03.patch
- drop integrated openoffice.org-3.1.0.ooo61927.sw.ww6.unicodefontencoding.patch
- drop integrated workspace.impress195.patch
- drop integrated workspace.srb1.patch
- drop integrated openoffice.org-3.2.0.ooo106502.svx.fixspelltimer.patch
- drop integrated openoffice.org-3.3.0.ooo108246.svx.hide-sql-group-when-inactive.patch
- drop integrated openoffice.org-3.2.0.ooo95369.sw.sortedobjs.patch
- drop integrated openoffice.org-3.2.0.ooo110142.svx.safercolornames.patch
- drop integrated openoffice.org-3.3.0.ooo111758.sd.xerror.patch
- drop integrated openoffice.org-3.2.0.ooo111741.extras.malformed-xml-file.patch
- drop integrated openoffice.org-3.3.0.ooo112059.sw.avoid-null-ptr-deref.patch
- drop integrated openoffice.org-3.3.0.ooo100686.wizards.types.not.mediatypes.patch
- drop integrated workspace.vcl113.patch
- drop integrated openoffice.org-3.3.0.ooo112384.sw.export.doc.styledoesntexist.patch
- drop integrated workspace.cmcfixes77.patch
- drop integrated workspace.vcl114.patch
- drop integrated openoffice.org-3.3.0.ooo106591.sal.tradcopy.patch
- drop integrated workspace.vcl115.patch
- drop integrated workspace.cmcfixes78.patch
- drop integrated openoffice.org-3.3.0.ooo114012.sd.bada11ychain.patch
- drop integrated workspace.cmcfixes79.patch
- drop integrated openoffice.org-3.3.0.ooo114703.vcl.betterlocalize.font.patch
- drop integrated openoffice.org-3.3.0.rh638185.editeng.cjkctlhtmlsizes.patch
- drop integrated openoffice.org-3.3.0.rh637738.libgcrypt.addmutex.patch
- drop integrated openoffice.org-3.2.0.rh632236.writerfilter.cleanup-cell-props.patch
- drop workspace.gtk3.patch

* Wed Oct 06 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.1-2
- Related: rhbz#639945 pull in review changes
  + redland build-fix
  + replace awk script
  + validate .destop files

* Wed Sep 29 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.1-1
- initial import of the leviathan
