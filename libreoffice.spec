# rhbz#465664 jar-repacking breaks help by reordering META-INF/MANIFEST.MF
%define __jar_repack %{nil}
# don't worry about whitespace for now
%define _default_patch_flags -s -l
# undef to get english only and no-langpacks for a faster smoketest build
%define langpacks 1
# whether to use stlport or gcc's stl, we're basically locked to stlport for
# i386 to support third party uno components and add-ons designed to work with
# vanilla OOo.
%ifarch %{ix86}
%define stlport_abi_lockin 1
%else
%define stlport_abi_lockin 0
%endif

%if %{stlport_abi_lockin}
%define stlflags --with-stlport
%else
%define stlflags --without-stlport
%endif

%if %{langpacks}
%define langpack_langs af ar bg bn ca cs cy da de dz el en-US es et eu fi fr ga gl gu pa-IN he hi hu hr it ja ko lt ms nb nl nn nr pl pt pt-BR ru sh sk sl sr ss st sv ta th tr ve xh zh-CN zh-TW zu ns tn ts as mr ml or te ur kn uk mai ro
%else
%define langpack_langs en-US
%endif

Summary:        Free Software Productivity Suite
Name:           libreoffice
Version:        3.2.99.1
Release:        2%{?dist}
License:        LGPLv3 and LGPLv2+ and BSD and (MPLv1.1 or GPLv2 or LGPLv2 or Netscape) and (CDDL or GPLv2) and Public Domain
Group:          Applications/Productivity
URL:            http://www.documentfoundation.org/develop
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:        http://download.documentfoundation.org/libreoffice/src/libreoffice-artwork-3.2.99.1.tar.bz2
Source1:        http://download.documentfoundation.org/libreoffice/src/libreoffice-base-3.2.99.1.tar.bz2
Source2:        http://download.documentfoundation.org/libreoffice/src/libreoffice-bootstrap-3.2.99.1.tar.bz2
Source3:        http://download.documentfoundation.org/libreoffice/src/libreoffice-calc-3.2.99.1.tar.bz2
Source4:        http://download.documentfoundation.org/libreoffice/src/libreoffice-components-3.2.99.1.tar.bz2
Source5:        http://download.documentfoundation.org/libreoffice/src/libreoffice-extensions-3.2.99.1.tar.bz2
Source6:        http://download.documentfoundation.org/libreoffice/src/libreoffice-extras-3.2.99.1.tar.bz2
Source7:        http://download.documentfoundation.org/libreoffice/src/libreoffice-filters-3.2.99.1.tar.bz2
Source8:        http://download.documentfoundation.org/libreoffice/src/libreoffice-help-3.2.99.1.tar.bz2
Source9:        http://download.documentfoundation.org/libreoffice/src/libreoffice-impress-3.2.99.1.tar.bz2
Source10:       http://download.documentfoundation.org/libreoffice/src/libreoffice-libs-core-3.2.99.1.tar.bz2
Source11:       http://download.documentfoundation.org/libreoffice/src/libreoffice-libs-extern-3.2.99.1.tar.bz2
Source12:       http://download.documentfoundation.org/libreoffice/src/libreoffice-libs-extern-sys-3.2.99.1.tar.bz2
Source13:       http://download.documentfoundation.org/libreoffice/src/libreoffice-libs-gui-3.2.99.1.tar.bz2
Source14:       http://download.documentfoundation.org/libreoffice/src/libreoffice-postprocess-3.2.99.1.tar.bz2
Source15:       http://download.documentfoundation.org/libreoffice/src/libreoffice-sdk-3.2.99.1.tar.bz2
Source16:       http://download.documentfoundation.org/libreoffice/src/libreoffice-testing-3.2.99.1.tar.bz2
Source17:       http://download.documentfoundation.org/libreoffice/src/libreoffice-ure-3.2.99.1.tar.bz2
Source18:       http://download.documentfoundation.org/libreoffice/src/libreoffice-writer-3.2.99.1.tar.bz2
Source19:       http://cgit.freedesktop.org/ooo-build/ooo-build/plain/src/evolocal.odb
Source20:       http://tools.openoffice.org/unowinreg_prebuild/680/unowinreg.dll
Source21:       redhat-registry.tar.gz
Source22:       redhat-langpacks.tar.gz
Source23:       redhat-agreement.xsl
Source24:       http://www.openoffice.org/nonav/issues/showattachment.cgi/66959/acor_lt.zip
Source25:       libreoffice-multiliblauncher.sh
Source26:       http://hg.services.openoffice.org/binaries/fdb27bfe2dbe2e7b57ae194d9bf36bab-SampleICC-1.3.2.tar.gz
Source27:       http://hg.services.openoffice.org/binaries/a7983f859eafb2677d7ff386a023bc40-xsltml_2.1.2.zip
Source28:       http://hg.services.openoffice.org/binaries/1f24ab1d39f4a51faf22244c94a6203f-xmlsec1-1.2.14.tar.gz
Source29:       http://hg.services.openoffice.org/binaries/798b2ffdc8bcfe7bca2cf92b62caf685-rhino1_5R5.zip
Source30:       http://hg.services.openoffice.org/binaries/35c94d2df8893241173de1d16b6034c0-swingExSrc.zip
Source31:       http://hg.services.openoffice.org/binaries/ada24d37d8d638b3d8a9985e80bc2978-source-9.0.0.7-bj.zip
Source32:       http://hg.services.openoffice.org/binaries/18f577b374d60b3c760a3a3350407632-STLport-4.5.tar.gz 
Source33:       description.xml
Source34:       manifest.xml
Source35:       http://download.documentfoundation.org/libreoffice/src/libreoffice-l10n-3.2.99.1.tar.bz2
BuildRequires:  zip, findutils, autoconf, flex, bison, icu, gperf, gcc-c++
BuildRequires:  binutils, java-devel >= 1.6.0, boost-devel, zlib-devel
BuildRequires:  python-devel, expat-devel, libxml2-devel, libxslt-devel, bc
BuildRequires:  neon-devel, libcurl-devel, libidn-devel, pam-devel, cups-devel
BuildRequires:  libXext-devel, libXt-devel, libICE-devel, libjpeg-devel, make
BuildRequires:  gecko-devel, libwpd-devel, hunspell-devel, unixODBC-devel
BuildRequires:  db4-devel, sane-backends-devel, libicu-devel, perl-Archive-Zip
BuildRequires:  freetype-devel, gtk2-devel, desktop-file-utils, hyphen-devel
BuildRequires:  evolution-data-server-devel, libtextcat-devel, nss-devel
BuildRequires:  gstreamer-devel, gstreamer-plugins-base-devel, openssl-devel
BuildRequires:  mdds-devel, lpsolve-devel, hsqldb, bsh, lucene, lucene-contrib
BuildRequires:  mesa-libGLU-devel, redland-devel, ant, ant-apache-regexp
BuildRequires:  jakarta-commons-codec, jakarta-commons-httpclient, cppunit-devel
BuildRequires:  jakarta-commons-lang, poppler-devel, fontpackages-devel, junit4
BuildRequires:  pentaho-reporting-flow-engine, libXinerama-devel, mythes-devel
BuildRequires:  silgraphite-devel, libwpg-devel, libwps-devel, vigra-devel

Patch1:  openoffice.org-2.0.1.rhXXXXXX.extensions.defaulttoevo2.patch
Patch2:  openoffice.org-1.9.123.ooo53397.prelinkoptimize.desktop.patch
Patch3:  openoffice.org-2.0.2.rh188467.printingdefaults.patch
Patch4:  openoffice.org-2.2.1.ooo7065.sw.titlepagedialog.patch
Patch5:  openoffice.org-2.3.0.ooo76649.httpencoding.patch
Patch6:  openoffice.org-2.4.0.ooo86080.unopkg.bodge.patch
Patch7:  openoffice.org-3.0.0.ooo88341.sc.verticalboxes.patch
Patch8:  workspace.dtardon03.patch
Patch9:  openoffice.org-2.2.0.gccXXXXX.solenv.javaregistration.patch
Patch10: openoffice.org-3.1.0.oooXXXXX.solenv.allowmissing.patch
Patch11: openoffice.org-3.1.0.ooo61927.sw.ww6.unicodefontencoding.patch
Patch12: openoffice.org-3.1.0.ooo101274.opening-a-directory.patch
Patch13: openoffice.org-3.1.0.ooo102061.sc.cellanchoring.patch
Patch14: workspace.impress195.patch
Patch15: openoffice.org-3.1.1.ooo105784.vcl.sniffscriptforsubs.patch
Patch16: workspace.srb1.patch
Patch17: openoffice.org-3.2.0.ooo106502.svx.fixspelltimer.patch
Patch18: openoffice.org-3.3.0.ooo108246.svx.hide-sql-group-when-inactive.patch
Patch19: openoffice.org-3.3.0.ooo108637.sfx2.uisavedir.patch
Patch20: openoffice.org-3.2.0.ooo108846.sfx2.qstartfixes.patch
Patch21: openoffice.org-3.2.0.ooo95369.sw.sortedobjs.patch
Patch22: openoffice.org-3.2.0.ooo110142.svx.safercolornames.patch
Patch23: openoffice.org-3.3.0.ooo111758.sd.xerror.patch
Patch24: openoffice.org-3.2.0.ooo111741.extras.malformed-xml-file.patch
Patch25: openoffice.org-3.3.0.ooo112059.sw.avoid-null-ptr-deref.patch
Patch26: openoffice.org-3.3.0.ooo107490.cppu.lifecycle.patch
Patch27: openoffice.org-3.3.0.ooo100686.wizards.types.not.mediatypes.patch
Patch28: workspace.vcl113.patch
Patch29: openoffice.org-3.3.0.ooo112384.sw.export.doc.styledoesntexist.patch
Patch30: workspace.gtk3.patch
Patch31: workspace.cmcfixes77.patch
Patch32: workspace.vcl114.patch
Patch33: openoffice.org-3.3.0.ooo113273.desktop.resolvelinks.patch
Patch34: openoffice.org-3.3.0.ooo106591.sal.tradcopy.patch
Patch35: workspace.vcl115.patch
Patch36: workspace.cmcfixes78.patch
Patch37: openoffice.org-3.3.0.ooo114012.sd.bada11ychain.patch
Patch38: workspace.cmcfixes79.patch
Patch39: openoffice.org-3.3.0.ooo114703.vcl.betterlocalize.font.patch
Patch40: openoffice.org-3.3.0.rh637738.libgcrypt.addmutex.patch
Patch41: openoffice.org-3.3.0.rh638185.editeng.cjkctlhtmlsizes.patch
Patch42: openoffice.org-3.2.0.rh632236.writerfilter.cleanup-cell-props.patch
Patch43: libreoffice-buildfix.patch

%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%define instdir %{_libdir}
%define baseinstdir %{instdir}/libreoffice
%define ureinstdir %{baseinstdir}/ure
%define basisinstdir %{baseinstdir}/basis3.3
%define sdkinstdir %{baseinstdir}/basis3.3/sdk
%define fontname opensymbol
%define OFFICEUPD 330
%define SOPOST l*

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
Requires: %{name}-%{fontname}-fonts = %{version}-%{release}
Requires: %{name}-ure = %{version}-%{release}
Requires: liberation-sans-fonts >= 1.0, liberation-serif-fonts >= 1.0, liberation-mono-fonts >= 1.0
Requires: dejavu-sans-fonts, dejavu-serif-fonts, dejavu-sans-mono-fonts
Requires: hunspell-en, hyphen-en, hyphen >= 2.4, autocorr-en
Requires: lucene
Requires(pre):    gtk2 >= 2.9.4
Requires(post):   gtk2 >= 2.9.4
Requires(preun):  gtk2 >= 2.9.4
Requires(postun): gtk2 >= 2.9.4
Obsoletes: openoffice.org-core < 1:3.3.1
Obsoletes: openoffice.org-brand < 1:3.3.1, broffice.org-brand < 1:3.3.1

%description core
The shared core libraries and support files for LibreOffice.

%package pyuno
Summary: Python support for LibreOffice
Group: Development/Libraries
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-ure = %{version}-%{release}
Requires: python
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core
Obsoletes: openoffice.org-pyuno < 1:3.3.1

%description pyuno
Python bindings for the LibreOffice UNO component model. Allows scripts both
external to LibreOffice and within the internal LibreOffice scripting framework
to be written in python.

%package base
Summary: Database front-end for LibreOffice
Group: Applications/Productivity
Requires: hsqldb, postgresql-jdbc
Requires: %{name}-ure = %{version}-%{release}
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-calc = %{version}-%{release}
Obsoletes: openoffice.org-base-core < 1:3.3.1
Obsoletes: openoffice.org-base < 1:3.3.1, broffice.org-base < 1:3.3.1

%description base
GUI database front-end for LibreOffice. Allows creation and management of 
databases through a GUI.

%package report-builder
Summary: Create database reports from LibreOffice
Group: Applications/Productivity
Requires: pentaho-reporting-flow-engine
Requires: %{name}-base = %{version}-%{release}
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core
Obsoletes: openoffice.org-report-builder < 1:3.3.1

%description report-builder
Creates database reports from LibreOffice databases. The report builder can
define group and page headers as well as group, page footers and calculation
fields to accomplish complex database reports.

%package bsh
Summary: BeanShell support for LibreOffice
Group: Development/Libraries
Requires: bsh
Requires: %{name}-core = %{version}-%{release}
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core
Obsoletes: openoffice.org-bsh < 1:3.3.1

%description bsh
Support BeanShell scripts in LibreOffice.

%package rhino
Summary: JavaScript support for LibreOffice
Group: Development/Libraries
Requires: %{name}-core = %{version}-%{release}
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core
Obsoletes: openoffice.org-rhino < 1:3.3.1

%description rhino
Support JavaScript scripts in LibreOffice.

%package wiki-publisher
Summary: Create Wiki articles on MediaWiki servers with LibreOffice
Group: Applications/Productivity
Requires: jakarta-commons-codec, jakarta-commons-httpclient
Requires: jakarta-commons-lang, jakarta-commons-logging
Requires: %{name}-writer = %{version}-%{release}
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core
Obsoletes: openoffice.org-wiki-publisher < 1:3.3.1

%description wiki-publisher
The Wiki Publisher enables you to create Wiki articles on MediaWiki servers
without having to know the syntax of the MediaWiki markup language. Publish
your new and existing documents transparently with writer to a wiki page.

%package ogltrans
Summary: 3D OpenGL slide transitions for LibreOffice
Group: Applications/Productivity
Requires: %{name}-impress = %{version}-%{release}
Requires(pre):    %{name}-core
Obsoletes: openoffice.org-ogltrans < 1:3.3.1

%description ogltrans
OpenGL Transitions enable 3D slide transitions to be used in LibreOffice.
Requires good quality 3D support for your graphics card for best experience.

%package presentation-minimizer
Summary: Shrink LibreOffice presentations
Group: Applications/Productivity
Requires: %{name}-impress = %{version}-%{release}
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core
Obsoletes: openoffice.org-presentation-minimizer < 1:3.3.1

%description presentation-minimizer
The Presentation Minimizer is used to reduce the file size of the current
presentation. Images will be compressed, and data that is no longer needed will
be removed.

%package presenter-screen
Summary: Presenter Screen for LibreOffice Presentations
Group: Applications/Productivity
Requires: %{name}-impress = %{version}-%{release}
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core
Obsoletes: openoffice.org-presenter-screen < 1:3.3.1

%description presenter-screen
The Presenter Screen is used to provides information on a second screen, that
typically is not visible to the audience when delivering a presentation. e.g.
slide notes.

%package pdfimport
Summary: PDF Importer for LibreOffice Draw
Group: Applications/Productivity
Requires: %{name}-draw = %{version}-%{release}
Requires(pre):    %{name}-core
Requires(post):   %{name}-core
Requires(preun):  %{name}-core
Requires(postun): %{name}-core
Obsoletes: openoffice.org-pdfimport < 1:3.3.1

%description pdfimport
The PDF Importer imports PDF into drawing documents to preserve layout
and enable basic editing of PDF documents.

%package %{fontname}-fonts
Summary: LibreOffice dingbats font
Group: User Interface/X
Requires: fontpackages-filesystem
Obsoletes: openoffice.org-fonts < 1:3.3.1
BuildArch: noarch

%description %{fontname}-fonts
A dingbats font, OpenSymbol, suitable for use by LibreOffice for bullets and
mathematical symbols. 

%package writer
Summary: LibreOffice Word Processor Application
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-ure = %{version}-%{release}
Obsoletes: openoffice.org-writer-core < 1:3.3.1
Obsoletes: openoffice.org-writer < 1:3.3.1, broffice.org-writer < 1:3.3.1

%description writer
The LibreOffice Word Processor application.

%package emailmerge
Summary: Email mail-merge component for LibreOffice 
Group: Applications/Productivity
Requires: %{name}-writer = %{version}-%{release}
Requires: %{name}-pyuno = %{version}-%{release}
Obsoletes: openoffice.org-emailmerge < 1:3.3.1

%description emailmerge
Enables the LibreOffice writer module to mail-merge to email.

%package calc
Summary: LibreOffice Spreadsheet Application
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-ure = %{version}-%{release}
Obsoletes: openoffice.org-calc-core < 1:3.3.1
Obsoletes: openoffice.org-calc < 1:3.3.1, broffice.org-calc < 1:3.3.1

%description calc
The LibreOffice Spreadsheet application.

%package draw
Summary: LibreOffice Drawing Application
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-ure = %{version}-%{release}
Requires: %{name}-pdfimport = %{version}-%{release}
Requires: %{name}-graphicfilter = %{version}-%{release}
Obsoletes: openoffice.org-draw-core < 1:3.3.1
Obsoletes: openoffice.org-draw < 1:3.3.1, broffice.org-draw < 1:3.3.1

%description draw
The LibreOffice Drawing Application.

%package impress
Summary: LibreOffice Presentation Application
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-ure = %{version}-%{release}
Requires: %{name}-presenter-screen = %{version}-%{release}
Obsoletes: openoffice.org-impress-core < 1:3.3.1
Obsoletes: openoffice.org-impress < 1:3.3.1, broffice.org-impress < 1:3.3.1

%description impress
The LibreOffice Presentation Application.

%package math
Summary: LibreOffice Equation Editor Application
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-ure = %{version}-%{release}
Obsoletes: openoffice.org-math-core < 1:3.3.1
Obsoletes: openoffice.org-math < 1:3.3.1, broffice.org-math < 1:3.3.1

%description math 
The LibreOffice Equation Editor Application.

%package graphicfilter
Summary: LibreOffice Extra Graphic filters
Group: Applications/Productivity
Requires: %{name}-ure = %{version}-%{release}
Requires: %{name}-core = %{version}-%{release}
Obsoletes: openoffice.org-graphicfilter < 1:3.3.1

%description graphicfilter
The graphicfilter module for LibreOffice provides graphic filters, e.g. svg and
flash filters.

%package xsltfilter
Summary: Optional xsltfilter module for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Obsoletes: openoffice.org-xsltfilter < 1:3.3.1

%description xsltfilter
The xsltfilter module for LibreOffice, provides additional docbook and
xhtml export transforms. Install this to enable docbook export.

%package javafilter
Summary: Optional javafilter module for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Obsoletes: openoffice.org-javafilter < 1:3.3.1

%description javafilter
The javafilter module for LibreOffice, provides additional AportisDoc,
Pocket Excel and Pocket Word import filters.

%post javafilter
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun javafilter
update-desktop-database %{_datadir}/applications &> /dev/null || :

%package testtools
Summary: Testtools for LibreOffice
Group: Development/Libraries
Requires: %{name}-ure = %{version}-%{release}
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-writer = %{version}-%{release}
Requires: %{name}-calc = %{version}-%{release}
Requires: %{name}-draw = %{version}-%{release}
Requires: %{name}-impress = %{version}-%{release}
Requires: %{name}-base = %{version}-%{release}
Requires: %{name}-math = %{version}-%{release}
Requires: %{name}-bsh = %{version}-%{release}
Requires: %{name}-rhino = %{version}-%{release}
Obsoletes: openoffice.org-testtools < 1:3.3.1

%description testtools
QA tools for LibreOffice, enables automated testing.

%package ure
Summary: UNO Runtime Environment
Group: Development/Libraries
Requires: unzip, jre >= 1.5.0
Obsoletes: openoffice.org-ure < 1:3.3.1

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
Requires: %{name}-ure = %{version}-%{release}
Requires: %{name}-core = %{version}-%{release}
Requires: unzip, java-devel
Obsoletes: openoffice.org-sdk < 1:3.3.1, openoffice.org-devel < 1:3.3.1

%description sdk
The LibreOffice SDK is an add-on for the LibreOffice office suite. It provides
the necessary tools for programming using the LibreOffice APIs and for creating
extensions (UNO components) for LibreOffice.  To set the build environment for
building against the sdk use %{sdkinstdir}/setsdkenv_unix.sh.

%package sdk-doc
Summary: Software Development Kit documentation for LibreOffice
Group: Documentation
Requires: %{name}-sdk = %{version}-%{release}
Obsoletes: openoffice.org-sdk-doc < 1:3.3.1

%description sdk-doc
This provides documentation for programming using the LibreOffice APIs
and examples of creating extensions (UNO components) for LibreOffice.

%package headless
Summary: LibreOffice Headless plug-in
Group: Development/Libraries
Requires: %{name}-ure = %{version}-%{release}
Requires: %{name}-core = %{version}-%{release}
Obsoletes: openoffice.org-headless < 1:3.3.1

%description headless
A plug-in for LibreOffice that enables it to function without an X server. 
It implements the -headless command line option and allows LibreOffice to be
used as a backend server for e.g. document conversion.

%package langpack-af
Summary: Afrikaans language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=af), hunspell-af, hyphen-af, autocorr-af
Obsoletes: openoffice.org-langpack-af_ZA < 1:3.3.1

%description langpack-af
Provides additional Afrikaans translations and resources for LibreOffice.

%package langpack-ar
Summary: Arabic language pack for LibreOffice
Group: Applications/Productivity
Requires: font(:lang=ar), hunspell-ar
Requires: %{name}-core = %{version}-%{release}
Obsoletes: openoffice.org-langpack-ar < 1:3.3.1

%description langpack-ar
Provides additional Arabic translations and resources for LibreOffice.

%package langpack-bg
Summary: Bulgarian language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=bg), hunspell-bg, hyphen-bg, mythes-bg, autocorr-bg
Obsoletes: openoffice.org-langpack-bg_BG < 1:3.3.1

%description langpack-bg
Provides additional Bulgarian translations and resources for LibreOffice.

%package langpack-bn
Summary: Bengali language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=bn), hunspell-bn, hyphen-bn
Obsoletes: openoffice.org-langpack-bn < 1:3.3.1

%description langpack-bn
Provides additional Bengali translations and resources for LibreOffice.

%package langpack-ca
Summary: Catalan language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=ca), hunspell-ca, hyphen-ca, mythes-ca
Obsoletes: openoffice.org-langpack-ca_ES < 1:3.3.1

%description langpack-ca
Provides additional Catalan translations and resources for LibreOffice.

%package langpack-cs
Summary: Czech language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=cs), hunspell-cs, hyphen-cs, mythes-cs, autocorr-cs
Obsoletes: openoffice.org-langpack-cs_CZ < 1:3.3.1

%description langpack-cs
Provides additional Czech translations and resources for LibreOffice.

%package langpack-cy
Summary: Welsh language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=cy), hunspell-cy, hyphen-cy
Obsoletes: openoffice.org-langpack-cy_GB < 1:3.3.1

%description langpack-cy
Provides additional Welsh translations and resources for LibreOffice.

%package langpack-da
Summary: Danish language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=da), hunspell-da, hyphen-da, mythes-da, autocorr-da
Obsoletes: openoffice.org-langpack-da_DK < 1:3.3.1

%description langpack-da
Provides additional Danish translations and resources for LibreOffice.

%package langpack-de
Summary: German language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=de), hunspell-de, hyphen-de, mythes-de, autocorr-de
Obsoletes: openoffice.org-langpack-de < 1:3.3.1

%description langpack-de
Provides additional German translations and resources for LibreOffice.

%package langpack-el
Summary: Greek language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=el), hunspell-el, hyphen-el, mythes-el
Obsoletes: openoffice.org-langpack-el_GR < 1:3.3.1

%description langpack-el
Provides additional Greek translations and resources for LibreOffice.

%package langpack-en
Summary: English language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: mythes-en
Obsoletes: openoffice.org-langpack-en < 1:3.3.1

%description langpack-en
English thesaurus for LibreOffice.

%package langpack-es
Summary: Spanish language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=es), hunspell-es, hyphen-es, mythes-es, autocorr-es
Obsoletes: openoffice.org-langpack-es < 1:3.3.1

%description langpack-es
Provides additional Spanish translations and resources for LibreOffice.

%package langpack-et
Summary: Estonian language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=et), hunspell-et, hyphen-et
Obsoletes: openoffice.org-langpack-et_EE < 1:3.3.1

%description langpack-et
Provides additional Estonian translations and resources for LibreOffice.

%package langpack-eu
Summary: Basque language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=eu), hunspell-eu, hyphen-eu, autocorr-eu
Obsoletes: openoffice.org-langpack-eu_ES < 1:3.3.1

%description langpack-eu
Provides additional Basque translations and resources for LibreOffice.

%package langpack-fi
Summary: Finnish language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=fi), openoffice.org-voikko, autocorr-fi
Obsoletes: openoffice.org-langpack-fi_FI < 1:3.3.1

%description langpack-fi
Provides additional Finnish translations and resources for LibreOffice.

%package langpack-fr
Summary: French language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=fr), hunspell-fr, hyphen-fr, mythes-fr, autocorr-fr
Obsoletes: openoffice.org-langpack-fr < 1:3.3.1

%description langpack-fr
Provides additional French translations and resources for LibreOffice.

%package langpack-ga
Summary: Irish language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=ga), hunspell-ga, hyphen-ga, mythes-ga, autocorr-ga
Obsoletes: openoffice.org-langpack-ga_IE < 1:3.3.1

%description langpack-ga
Provides additional Irish translations and resources for LibreOffice.

%package langpack-gl
Summary: Galician language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=gl), hunspell-gl, hyphen-gl
Obsoletes: openoffice.org-langpack-gl_ES < 1:3.3.1

%description langpack-gl
Provides additional Galician translations and resources for LibreOffice.

%package langpack-gu
Summary: Gujarati language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=gu), hunspell-gu, hyphen-gu
Obsoletes: openoffice.org-langpack-gu_IN < 1:3.3.1

%description langpack-gu
Provides additional Gujarati translations and resources for OpenOffice.or.

%package langpack-pa
Summary: Punjabi language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=pa), hunspell-pa, hyphen-pa
Obsoletes: openoffice.org-langpack-pa < 1:3.3.1

%description langpack-pa
Provides additional Punjabi translations and resources for LibreOffice.

%package langpack-he
Summary: Hebrew language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=he), hunspell-he
Obsoletes: openoffice.org-langpack-he_IL < 1:3.3.1

%description langpack-he
Provides additional Hebrew translations and resources for LibreOffice.

%package langpack-hi
Summary: Hindi language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=hi), hunspell-hi, hyphen-hi
Obsoletes: openoffice.org-langpack-hi_IN < 1:3.3.1

%description langpack-hi
Provides additional Hindi translations and resources for LibreOffice.

%package langpack-hu
Summary: Hungarian language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=hu), hunspell-hu, hyphen-hu, mythes-hu, autocorr-hu
Obsoletes: openoffice.org-langpack-hu_HU < 1:3.3.1

%description langpack-hu
Provides additional Hungarian translations and resources for LibreOffice.

%package langpack-hr
Summary: Croatian language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=hr), hunspell-hr, hyphen-hr
Obsoletes: openoffice.org-langpack-hr_HR < 1:3.3.1

%description langpack-hr
Provides additional Croatian translations and resources for LibreOffice.

%package langpack-it
Summary: Italian language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=it), hunspell-it, hyphen-it, mythes-it, autocorr-it
Obsoletes: openoffice.org-langpack-it < 1:3.3.1

%description langpack-it
Provides additional Italian translations and resources for LibreOffice.

%package langpack-ja
Summary: Japanese language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=ja), autocorr-ja
Obsoletes: openoffice.org-langpack-ja_JP < 1:3.3.1

%description langpack-ja
Provides additional Japanese translations and resources for LibreOffice.

%package langpack-ko
Summary: Korean language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=ko), hunspell-ko, autocorr-ko
Obsoletes: openoffice.org-langpack-ko_KR < 1:3.3.1

%description langpack-ko
Provides additional Korean translations and resources for LibreOffice.

%package langpack-lt
Summary: Lithuanian language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=lt), hunspell-lt, hyphen-lt, autocorr-lt
Obsoletes: openoffice.org-langpack-lt_LT < 1:3.3.1

%description langpack-lt
Provides additional Lithuanian translations and resources for LibreOffice.

%package langpack-ms
Summary: Malay language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=ms), hunspell-ms
Obsoletes: openoffice.org-langpack-ms_MY < 1:3.3.1

%description langpack-ms
Provides additional Malay translations and resources for LibreOffice.

%package langpack-nb
Summary: Bokmal language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=nb), hunspell-nb, hyphen-nb, mythes-nb
Obsoletes: openoffice.org-langpack-nb_NO < 1:3.3.1

%description langpack-nb
Provides additional Bokmal translations and resources for LibreOffice.

%package langpack-nl
Summary: Dutch language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=nl), hunspell-nl, hyphen-nl, mythes-nl, autocorr-nl
Obsoletes: openoffice.org-langpack-nl < 1:3.3.1

%description langpack-nl
Provides additional Dutch translations and resources for LibreOffice.

%package langpack-nn
Summary: Nynorsk language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=nn), hunspell-nn, hyphen-nn, mythes-nn
Obsoletes: openoffice.org-langpack-nn_NO < 1:3.3.1

%description langpack-nn
Provides additional Nynorsk translations and resources for LibreOffice.

%package langpack-nr
Summary: Southern Ndebele language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=nr), hunspell-nr
Obsoletes: openoffice.org-langpack-nr_ZA < 1:3.3.1

%description langpack-nr
Provides additional Southern Ndebele translations and resources for 
LibreOffice.

%package langpack-pl
Summary: Polish language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=pl), hunspell-pl, hyphen-pl, mythes-pl, autocorr-pl
Obsoletes: openoffice.org-langpack-pl_PL < 1:3.3.1

%description langpack-pl
Provides additional Polish translations and resources for LibreOffice.

%package langpack-pt-PT
Summary: Portuguese language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=pt), hunspell-pt, hyphen-pt, mythes-pt, autocorr-pt
Obsoletes: openoffice.org-langpack-pt_PT < 1:3.3.1

%description langpack-pt-PT
Provides additional Portuguese translations and resources for LibreOffice.

%package langpack-pt-BR
Summary: Brazilian Portuguese language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=pt), hunspell-pt, hyphen-pt, mythes-pt, autocorr-pt
Obsoletes: openoffice.org-langpack-pt_BR < 1:3.3.1

%description langpack-pt-BR
Provides additional Brazilian Portuguese translations and resources for 
LibreOffice.

%package langpack-ru
Summary: Russian language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=ru), hunspell-ru, hyphen-ru, mythes-ru, autocorr-ru
Obsoletes: openoffice.org-langpack-ru < 1:3.3.1

%description langpack-ru
Provides additional Russian translations and resources for LibreOffice.

%package langpack-sk
Summary: Slovak language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=sk), hunspell-sk, hyphen-sk, mythes-sk, autocorr-sk
Obsoletes: openoffice.org-langpack-sk_SK < 1:3.3.1

%description langpack-sk
Provides additional Slovak translations and resources for LibreOffice.

%package langpack-sl
Summary: Slovenian language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=sl), hunspell-sl, hyphen-sl, mythes-sl, autocorr-sl
Obsoletes: openoffice.org-langpack-sl_SI < 1:3.3.1

%description langpack-sl
Provides additional Slovenian translations and resources for LibreOffice.

%package langpack-sr
Summary: Serbian language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=sr), hunspell-sr, hyphen-sr, autocorr-sr
Obsoletes: openoffice.org-langpack-sr < 1:3.3.1

%description langpack-sr
Provides additional Serbian translations and resources for LibreOffice.

%package langpack-ss
Summary: Swati language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=ss), hunspell-ss
Obsoletes: openoffice.org-langpack-ss_ZA < 1:3.3.1

%description langpack-ss
Provides additional Swati translations and resources for LibreOffice.

%package langpack-st
Summary: Southern Sotho language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=st), hunspell-st
Obsoletes: openoffice.org-langpack-st_ZA < 1:3.3.1

%description langpack-st
Provides additional Southern Sotho translations and resources for 
LibreOffice.

%package langpack-sv
Summary: Swedish language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=sv), hunspell-sv, hyphen-sv, mythes-sv, autocorr-sv
Obsoletes: openoffice.org-langpack-sv < 1:3.3.1

%description langpack-sv
Provides additional Swedish translations and resources for LibreOffice.

%package langpack-ta
Summary: Tamil language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires:  font(:lang=ta), hunspell-ta, hyphen-ta
Obsoletes: openoffice.org-langpack-ta_IN < 1:3.3.1

%description langpack-ta
Provides additional Tamil translations and resources for LibreOffice.

%package langpack-th
Summary: Thai language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=th), hunspell-th
Obsoletes: openoffice.org-langpack-th_TH < 1:3.3.1

%description langpack-th
Provides additional Thai translations and resources for LibreOffice.

%package langpack-nso
Summary: Northern Sotho language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=nso), hunspell-nso
Obsoletes: openoffice.org-langpack-nso_ZA < 1:3.3.1

%description langpack-nso
Provides additional Northern Sotho translations and resources for 
LibreOffice.

%package langpack-tn
Summary: Tswana language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=tn), hunspell-tn
Obsoletes: openoffice.org-langpack-tn_ZA < 1:3.3.1

%description langpack-tn
Provides additional Tswana translations and resources for LibreOffice.

%package langpack-ts
Summary: Tsonga language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=ts), hunspell-ts
Obsoletes: openoffice.org-langpack-ts_ZA < 1:3.3.1

%description langpack-ts
Provides additional Tsonga translations and resources for LibreOffice.

%package langpack-tr
Summary: Turkish language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=tr), autocorr-tr
Obsoletes: openoffice.org-langpack-tr_TR < 1:3.3.1

%description langpack-tr
Provides additional Turkish translations and resources for LibreOffice.

%package langpack-ve
Summary: Venda language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=ve), hunspell-ve
Obsoletes: openoffice.org-langpack-ve_ZA < 1:3.3.1

%description langpack-ve
Provides additional Venda translations and resources for LibreOffice.

%package langpack-xh
Summary: Xhosa language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=xh), hunspell-xh
Obsoletes: openoffice.org-langpack-xh_ZA < 1:3.3.1

%description langpack-xh
Provides additional Xhosa translations and resources for LibreOffice.

%package langpack-zh-Hans
Summary: Simplified Chinese language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=zh-cn), autocorr-zh
Obsoletes: openoffice.org-langpack-zh_CN < 1:3.3.1

%description langpack-zh-Hans
Provides additional Simplified Chinese translations and resources for 
LibreOffice.

%package langpack-zh-Hant
Summary: Traditional Chinese language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=zh-tw), autocorr-zh
Obsoletes: openoffice.org-langpack-zh_TW < 1:3.3.1

%description langpack-zh-Hant
Provides additional Traditional Chinese translations and resources for 
LibreOffice.

%package langpack-zu
Summary: Zulu language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=zu), hunspell-zu, hyphen-zu
Obsoletes: openoffice.org-langpack-zu_ZA < 1:3.3.1

%description langpack-zu
Provides additional Zulu translations and resources for LibreOffice.

%package langpack-as
Summary: Assamese language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=as), hunspell-as, hyphen-as
Obsoletes: openoffice.org-langpack-as_IN < 1:3.3.1

%description langpack-as
Provides additional Assamese translations and resources for LibreOffice.

%package langpack-mr
Summary: Marathi language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=mr), hunspell-mr, hyphen-mr
Obsoletes: openoffice.org-langpack-mr_IN < 1:3.3.1

%description langpack-mr
Provides additional Marathi translations and resources for LibreOffice.

%package langpack-ml
Summary: Malayalam language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=ml), hunspell-ml, hyphen-ml
Obsoletes: openoffice.org-langpack-ml_IN < 1:3.3.1

%description langpack-ml
Provides additional Malayalam translations and resources for LibreOffice.

%package langpack-or
Summary: Oriya language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=or), hunspell-or, hyphen-or
Obsoletes: openoffice.org-langpack-or_IN < 1:3.3.1

%description langpack-or
Provides additional Oriya translations and resources for LibreOffice.

%package langpack-te
Summary: Telugu language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=te), hunspell-te, hyphen-te
Obsoletes: openoffice.org-langpack-te_IN < 1:3.3.1

%description langpack-te
Provides additional Telugu translations and resources for LibreOffice.

%package langpack-ur
Summary: Urdu language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=ur), hunspell-ur
Obsoletes: openoffice.org-langpack-ur < 1:3.3.1

%description langpack-ur
Provides additional Urdu translations and resources for LibreOffice.

%package langpack-kn
Summary: Kannada language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=kn), hunspell-kn, hyphen-kn
Obsoletes: openoffice.org-langpack-kn_IN < 1:3.3.1

%description langpack-kn
Provides additional Kannada translations and resources for LibreOffice.

%package langpack-dz
Summary: Dzongkha language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=dz)
Obsoletes: openoffice.org-langpack-dz < 1:3.3.1

%description langpack-dz
Provides additional Dzongkha translations and resources for LibreOffice.

%package langpack-uk
Summary: Ukrainian language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=uk), hunspell-uk, hyphen-uk, mythes-uk
Obsoletes: openoffice.org-langpack-uk < 1:3.3.1

%description langpack-uk
Provides additional Ukrainian translations and resources for LibreOffice.

%package langpack-mai
Summary: Maithili language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=mai)
Obsoletes: openoffice.org-langpack-mai_IN < 1:3.3.1

%description langpack-mai
Provides additional Maithili translations and resources for LibreOffice.

%package langpack-ro
Summary: Romanian language pack for LibreOffice
Group: Applications/Productivity
Requires: %{name}-core = %{version}-%{release}
Requires: font(:lang=ro), hunspell-ro, hyphen-ro, mythes-ro
Obsoletes: openoffice.org-langpack-ro < 1:3.3.1

%description langpack-ro
Provides additional Romanian translations and resources for LibreOffice.

%package -n autocorr-en
Summary: English auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-en
Rules for auto-correcting common English typing errors.

%package -n autocorr-af
Summary: Afrikaans auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-af
Rules for auto-correcting common Afrikaans typing errors.

%package -n autocorr-bg
Summary: Bulgarian auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-bg
Rules for auto-correcting common Bulgarian typing errors.

%package -n autocorr-cs
Summary: Czech auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-cs
Rules for auto-correcting common Czech typing errors.

%package -n autocorr-da
Summary: Danish auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-da
Rules for auto-correcting common Danish typing error.

%package -n autocorr-de
Summary: German auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-de
Rules for auto-correcting common German typing errors.

%package -n autocorr-es
Summary: Spanish auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-es
Rules for auto-correcting common Spanish typing errors.

%package -n autocorr-eu
Summary: Basque auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-eu
Rules for auto-correcting common Basque typing errors.

%package -n autocorr-fa
Summary: Farsi auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-fa
Rules for auto-correcting common Farsi typing errors.

%package -n autocorr-fi
Summary: Finnish auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-fi
Rules for auto-correcting common Finnish typing errors.

%package -n autocorr-fr
Summary: French auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-fr
Rules for auto-correcting common French typing errors.

%package -n autocorr-ga
Summary: Irish auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-ga
Rules for auto-correcting common Irish typing errors.

%package -n autocorr-hu
Summary: Hungarian auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-hu
Rules for auto-correcting common Hungarian typing errors.

%package -n autocorr-it
Summary: Italian auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-it
Rules for auto-correcting common Italian typing errors.

%package -n autocorr-ja
Summary: Japanese auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-ja
Rules for auto-correcting common Japanese typing errors.

%package -n autocorr-ko
Summary: Korean auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-ko
Rules for auto-correcting common Korean typing errors.

%package -n autocorr-lb
Summary: Luxembourgish auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-lb
Rules for auto-correcting common Luxembourgish typing errors.

%package -n autocorr-lt
Summary: Lithuanian auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-lt
Rules for auto-correcting common Lithuanian typing errors.

%package -n autocorr-mn
Summary: Mongolian auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-mn
Rules for auto-correcting common Mongolian typing errors.

%package -n autocorr-nl
Summary: Dutch auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-nl
Rules for auto-correcting common Dutch typing errors.

%package -n autocorr-pl
Summary: Polish auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-pl
Rules for auto-correcting common Polish typing errors.

%package -n autocorr-pt
Summary: Portuguese auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-pt
Rules for auto-correcting common Portuguese typing errors.

%package -n autocorr-ru
Summary: Russian auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-ru
Rules for auto-correcting common Russian typing errors.

%package -n autocorr-sk
Summary: Slovak auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-sk
Rules for auto-correcting common Slovak typing errors.

%package -n autocorr-sl
Summary: Slovenian auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-sl
Rules for auto-correcting common Slovenian typing errors.

%package -n autocorr-sr
Summary: Serbian auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-sr
Rules for auto-correcting common Serbian typing errors.

%package -n autocorr-sv
Summary: Swedish auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-sv
Rules for auto-correcting common Swedish typing errors.

%package -n autocorr-tr
Summary: Turkish auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-tr
Rules for auto-correcting common Turkish typing errors.

%package -n autocorr-vi
Summary: Vietnamese auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-vi
Rules for auto-correcting common Vietnamese typing errors.

%package -n autocorr-zh
Summary: Chinese auto-correction rules
Group: Applications/Text
BuildArch: noarch

%description -n autocorr-zh
Rules for auto-correcting common Chinese typing errors.

%prep
%setup -q -c -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11 -a 12 -a 13 -a 14 -a 15 -a 16 -a 17 -a 18 -a 35
for a in */*; do mv `pwd`/$a .; done
#remove "debugging" translations
rm -rf l10n/source/kid
#Customize Palette to remove Sun colours and add Red Hat colours
(head -n -1 extras/source/palettes/standard.soc && \
 echo -e ' <draw:color draw:name="Red Hat 1" draw:color="#cc0000"/>
 <draw:color draw:name="Red Hat 2" draw:color="#0093d9"/> 
 <draw:color draw:name="Red Hat 3" draw:color="#ff8d00"/>
 <draw:color draw:name="Red Hat 4" draw:color="#abb400"/>
 <draw:color draw:name="Red Hat 5" draw:color="#4e376b"/>' && \
 tail -n 1 extras/source/palettes/standard.soc) > redhat.soc
mv -f redhat.soc extras/source/palettes/standard.soc
cp -p %{SOURCE19} extras/source/database/evolocal.odb
cp -p %{SOURCE20} external/unowinreg/unowinreg.dll
%patch1  -p1 -b .rhXXXXXX.extensions.defaulttoevo2.patch
%patch2  -p1 -b .ooo53397.prelinkoptimize.desktop.patch
%patch3  -p1
%patch4  -p1 -b .ooo7065.sw.titlepagedialog.patch
%patch5  -p0 -b .ooo76649.httpencoding.patch
%patch6  -p1 -b .ooo86080.unopkg.bodge.patch
%patch7  -p1 -b .ooo88341.sc.verticalboxes.patch
%patch8  -p0 -b .workspace.dtardon03.patch
%patch9  -p0 -b .gccXXXXX.solenv.javaregistration.patch
%patch10 -p1 -b .oooXXXXX.solenv.allowmissing.patch
%patch11 -p1 -b .ooo61927.sw.ww6.unicodefontencoding.patch
%patch12 -p0 -b .ooo101274.opening-a-directory.patch
%patch13 -p0 -b .ooo102061.sc.cellanchoring.patch
%patch14 -p0 -b .workspace.impress195.patch
%patch15 -p0 -b .ooo105784.vcl.sniffscriptforsubs.patch
%patch16 -p1 -b .workspace.srb1.patch
%patch17 -p1 -b .ooo106502.svx.fixspelltimer.patch
%patch18 -p1 -b .ooo108246.svx.hide-sql-group-when-inactive.patch
%patch19 -p1 -b .ooo108637.sfx2.uisavedir.patch
%patch20 -p1 -b .ooo108846.sfx2.qstartfixes.patch
%patch21 -p1 -b .ooo95369.sw.sortedobjs.patch
%patch22 -p0 -b .ooo110142.svx.safercolornames.patch
%patch23 -p0 -b .ooo111758.sd.xerror.patch
%patch24 -p1 -b .ooo111741.extras.malformed-xml-file.patch
%patch25 -p1 -b .ooo112059.sw.avoid-null-ptr-deref.patch
%patch26 -p0 -b .ooo107490.cppu.lifecycle.patch
%patch27 -p0 -b .ooo100686.wizards.types.not.mediatypes.patch
%patch28 -p0 -b .workspace.vcl113.patch
%patch29 -p0 -b .ooo112384.sw.export.doc.styledoesntexist.patch
%patch30 -p0 -b .workspace.gtk3.patch
%patch31 -p1 -b .workspace.cmcfixes77.patch
%patch32 -p0 -b .workspace.vcl114.patch
%patch33 -p0 -b .ooo113273.desktop.resolvelinks.patch
%patch34 -p0 -b .ooo106591.sal.tradcopy.patch
%patch35 -p1 -b .workspace.vcl115.patch
%patch36 -p1 -b .workspace.cmcfixes78.patch
%patch37 -p0 -b .ooo114012.sd.bada11ychain.patch
%patch38 -p1 -b .workspace.cmcfixes79.patch
%patch39 -p1 -b .ooo114703.vcl.betterlocalize.font.patch
%patch40 -p0 -b .rh637738.libgcrypt.addmutex.patch
%patch41 -p1 -b .rh638185.editeng.cjkctlhtmlsizes.patch
%patch42 -p1 -b .rh632236.writerfilter.cleanup-cell-props.patch
%patch43 -p1 -b .libreoffice-buildfix.patch

%build
echo build start time is `date`, diskspace: `df -h . | tail -n 1`
#don't build localized helps which are poorly translated
POORHELPS=`find l10n/source -name localize.sdf -exec grep 'helpcontent2.*main.*Working With %PRODUCTNAME' {} \; | cut -f 10 | grep -v en-US | xargs`
#convert _smp_mflags to dmake equivalent
SMP_MFLAGS=%{?_smp_mflags}
SMP_MFLAGS=$[${SMP_MFLAGS/-j/}]
if [ $SMP_MFLAGS -lt 2 ]; then SMP_MFLAGS=2; fi
NDMAKES=`dc -e "$SMP_MFLAGS v p"`
NBUILDS=`dc -e "$SMP_MFLAGS $NDMAKES / p"`

autoconf
%configure \
 --with-vendor="Red Hat, Inc." --with-num-cpus=$NBUILDS --with-max-jobs=$NDMAKES \
 --with-build-version="Ver: %{version}-%{release}" --with-unix-wrapper=%{name} \
 --enable-symbols --disable-ldap --disable-epm --disable-mathmldtd \
 --disable-Xaw --disable-gnome-vfs --enable-gio --enable-symbols \
 --enable-lockdown --enable-evolution2 --enable-cairo --enable-dbus \
 --enable-opengl --enable-vba --enable-minimizer --enable-presenter-console \
 --enable-pdfimport --enable-wiki-publisher --enable-report-builder \
 --with-system-jfreereport --with-vba-package-format="builtin" \
 --with-system-libs --with-system-headers --with-system-mozilla \
 --with-system-mythes --with-system-dicts --with-system-apache-commons \
 --with-system-libtextcat --with-system-libtextcat-data --without-system-saxon \
 --with-external-dict-dir=/usr/share/myspell --without-myspell-dicts \
 --without-fonts --without-agg --without-ppds --without-afms %{stlflags} \
 --with-lang="%{langpack_langs}" --with-poor-help-localizations="$POORHELPS" \
 --with-external-tar=`pwd`/ext_sources --with-java-target-version=1.5

mkdir -p ext_sources
cp %{SOURCE20} ext_sources/185d60944ea767075d27247c3162b3bc-unowinreg.dll
cp %{SOURCE26} ext_sources
cp %{SOURCE27} ext_sources
cp %{SOURCE28} ext_sources
cp %{SOURCE29} ext_sources
cp %{SOURCE30} ext_sources
cp %{SOURCE31} ext_sources
cp %{SOURCE32} ext_sources

#use the RPM_OPT_FLAGS but remove the OOo overridden ones
for i in $RPM_OPT_FLAGS; do
        case "$i" in
                -O?|-pipe|-Wall|-g|-fexceptions) continue;;
        esac
        ARCH_FLAGS="$ARCH_FLAGS $i"
done
export ARCH_FLAGS

. ./*[Ee]nv.[Ss]et.sh
./bootstrap
cd instsetoo_native
if ! VERBOSE=false build --dlv_switch -link -P$NBUILDS --all -- -P$NDMAKES -s; then
    build --dlv_switch -link --all
fi

#generate the icons and mime type stuff
export DESTDIR=../../../output
export KDEMAINDIR=/usr
export GNOMEDIR=/usr
export GNOME_MIME_THEME=hicolor
cd ../sysui
cd unxlng*/misc/libreoffice
./create_tree.sh

echo build end time is `date`, diskspace: `df -h . | tail -n 1`

%install
rm -rf $RPM_BUILD_ROOT
source ./Linux*Env.Set.sh
#figure out the icon version
export `grep "^PRODUCTVERSIONSHORT =" sysui/desktop/productversion.mk | sed -e "s/ //g"`
export `grep "PRODUCTVERSION[ ]*=[ ]*" sysui/desktop/productversion.mk | sed -e "s/ //g"`
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
    cat ../unx*.pro/OpenOffice/installed/logging/en-US/log_*_en-US.log
    echo - ---dump log end---
    ok=false
fi
if [ $ok == "false" ]; then
    exit 1
fi
mkdir -p $RPM_BUILD_ROOT/%{baseinstdir}
mv ../unxlng*.pro/OpenOffice/installed/install/en-US/* $RPM_BUILD_ROOT/%{baseinstdir}
chmod -R +w $RPM_BUILD_ROOT/%{baseinstdir}
%if %{langpacks}
dmake ooolanguagepack
rm -rf ../unxlng*.pro/OpenOffice_languagepack/installed/install/log
for langpack in ../unxlng*.pro/OpenOffice_languagepack/installed/install/*; do
cp -rp $langpack/* $RPM_BUILD_ROOT/%{baseinstdir}
rm -rf $langpack
done
%endif
for file in swriter scalc simpress sdraw ; do
    cp -f ../../desktop/$OUTPATH.pro/bin/$file $RPM_BUILD_ROOT/%{baseinstdir}/program/$file.bin
done
rm -rf $RPM_BUILD_ROOT/%{baseinstdir}/share/prereg
#give a consistent javasettingsunopkginstall.xml
$RPM_BUILD_ROOT/%{baseinstdir}/program/unopkg list --bundled || :
export WITH_LANG="en-US"
dmake sdkoo
mv ../unxlng*.pro/OpenOffice_SDK/installed/install/en-US/*/sdk $RPM_BUILD_ROOT/%{sdkinstdir}
cd ../../

# revoke ScriptProviders and make into extensions
pushd $RPM_BUILD_ROOT/%{basisinstdir}/program

# BeanShell
../ure-link/bin/regcomp -revoke -r services.rdb -br services.rdb -c "vnd.sun.star.expand:\$OOO_BASE_DIR/program/classes/ScriptProviderForBeanShell.jar"
mkdir $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForBeanShell.oxt \
     $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForBeanShell.oxt/META-INF
mv classes/ScriptProviderForBeanShell.jar $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForBeanShell.oxt
cp %{SOURCE33} $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForBeanShell.oxt
cp %{SOURCE34} $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForBeanShell.oxt/META-INF
sed -i -e 's/@display-name@/Script provider for BeanShell/' \
    -e 's/@version@/%{version}/' \
    -e 's/@id@/com.sun.star.script.provider.ScriptProviderForBeanShell/' \
    $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForBeanShell.oxt/description.xml
sed -i -e 's/@type@/java/' -e 's/@path@/ScriptProviderForBeanShell.jar/' \
    $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForBeanShell.oxt/META-INF/manifest.xml

# JavaScript
../ure-link/bin/regcomp -revoke -r services.rdb -br services.rdb -c "vnd.sun.star.expand:\$OOO_BASE_DIR/program/classes/ScriptProviderForJavaScript.jar"
mkdir $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForJavaScript.oxt \
     $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForJavaScript.oxt/META-INF
mv classes/ScriptProviderForJavaScript.jar $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForJavaScript.oxt
cp %{SOURCE33} $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForJavaScript.oxt
cp %{SOURCE34} $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForJavaScript.oxt/META-INF
sed -i -e 's/@display-name@/Script provider for JavaScript/' \
    -e 's/@version@/%{version}/' \
    -e 's/@id@/com.sun.star.script.provider.ScriptProviderForJavaScript/' \
    $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForJavaScript.oxt/description.xml
sed -i -e 's/@type@/java/' -e 's/@path@/ScriptProviderForJavaScript.jar/' \
    $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForJavaScript.oxt/META-INF/manifest.xml

# Python
../ure-link/bin/regcomp -revoke -r services.rdb -br services.rdb -c vnd.openoffice.pymodule:pythonscript
mkdir $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForPython.oxt \
     $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForPython.oxt/META-INF
mv pythonscript.py $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForPython.oxt
cp %{SOURCE33} $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForPython.oxt
cp %{SOURCE34} $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForPython.oxt/META-INF
sed -i -e 's/@display-name@/Script provider for Python/' \
    -e 's/@version@/%{version}/' \
    -e 's/@id@/com.sun.star.script.provider.ScriptProviderForPython/' \
    $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForPython.oxt/description.xml
sed -i -e 's/@type@/python/' -e 's/@path@/pythonscript.py/' \
    $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/ScriptProviderForPython.oxt/META-INF/manifest.xml

popd

#configure sdk
pushd $RPM_BUILD_ROOT/%{sdkinstdir}
    for file in setsdkenv_unix.csh setsdkenv_unix.sh ; do
        sed -e "s,@OO_SDK_NAME@,sdk," \
            -e "s,@OO_SDK_HOME@,%{sdkinstdir}," \
            -e "s,@OFFICE_HOME@,%{baseinstdir}," \
            -e "s,@OFFICE_BASE_HOME@,%{basisinstdir}," \
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
#fix permissions
    find examples -type f -exec chmod -x {} \;
popd

#add our custom configuration options
#enable gtk file dialog as the default
rm -rf $RPM_BUILD_ROOT/%{basisinstdir}/share/registry/modules/org/openoffice/Office/Common/Common-UseOOoFileDialogs.xcu
#default autorecovery settings
#system libtextcat fingerprint location
#rhbz#484055 system autocorr location
#rhbz#451512 set better math print options
tar xzf %{SOURCE21} -C $RPM_BUILD_ROOT/%{basisinstdir}/share

#add the debugging libsalalloc_malloc.so.3 library
cp -f solver/%{OFFICEUPD}/unxlng*.pro/lib/libsalalloc_malloc.so.3 $RPM_BUILD_ROOT/%{ureinstdir}/lib
chmod -x $RPM_BUILD_ROOT/%{basisinstdir}/program/testtoolrc
chmod -x $RPM_BUILD_ROOT/%{basisinstdir}/program/hid.lst

#remove spurious exec bits
chmod -x $RPM_BUILD_ROOT/%{basisinstdir}/program/gengalrc

#We don't need to carry around all the letter templates for all the languages 
#in each langpack! In addition, all the bitmaps are the same!
pushd $RPM_BUILD_ROOT/%{basisinstdir}/share/template
mkdir -p wizard
for I in %{langpack_langs}; do
    if [ -d $I/wizard/bitmap ]; then
        cp -afl $I/wizard/bitmap wizard/
        rm -rf $I/wizard/bitmap
        ln -sf ../../wizard/bitmap $I/wizard/bitmap
    fi

    if [ -d $I/wizard/letter/$I ]; then
        mv -f $I/wizard/letter/$I ${I}_wizard_letter_${I}
        rm -rf $I/wizard/letter/*
        mv -f ${I}_wizard_letter_${I} $I/wizard/letter/$I
    else
        rm -rf $I/wizard/letter/*
    fi
done
popd

#Set some aliases to canonical autocorrect language files for locales with matching languages
pushd $RPM_BUILD_ROOT/%{basisinstdir}/share/autocorr

# ooo#108049
cp -p %{SOURCE24} acor_lt-LT.dat

#en-ZA exists and has a good autocorrect file with two or three extras that make sense for South Africa
en_GB_aliases="en-AG en-AU en-BS en-BW en-BZ en-CA en-DK en-GH en-HK en-IE en-IN en-JM en-NG en-NZ en-SG en-TT"
for lang in $en_GB_aliases; do
        ln -sf acor_en-GB.dat acor_$lang.dat
done
en_US_aliases="en-PH"
for lang in $en_US_aliases; do
        ln -sf acor_en-US.dat acor_$lang.dat
done
en_ZA_aliases="en-NA en-ZW"
for lang in $en_ZA_aliases; do
        ln -sf acor_en-ZA.dat acor_$lang.dat
done
%if %{langpacks}
af_ZA_aliases="af-NA"
for lang in $af_ZA_aliases; do
        ln -sf acor_af-ZA.dat acor_$lang.dat
done
de_DE_aliases="de-AT de-BE de-CH de-LI de-LU"
for lang in $de_DE_aliases; do
        ln -sf acor_de-DE.dat acor_$lang.dat
done
es_ES_aliases="es-AR es-BO es-CL es-CO es-CR es-CU es-DO es-EC es-GT es-HN es-MX es-NI es-PA es-PE es-PR es-PY es-SV es-US es-UY es-VE"
for lang in $es_ES_aliases; do
        ln -sf acor_es-ES.dat acor_$lang.dat
done
fr_FR_aliases="fr-BE fr-CA fr-CH fr-LU fr-MC"
for lang in $fr_FR_aliases; do
        ln -sf acor_fr-FR.dat acor_$lang.dat
done
it_IT_aliases="it-CH"
for lang in $it_IT_aliases; do
        ln -sf acor_it-IT.dat acor_$lang.dat
done
nl_NL_aliases="nl-AW nl-BE"
for lang in $nl_NL_aliases; do
        ln -s acor_nl-NL.dat acor_$lang.dat
done
sv_SE_aliases="sv-FI"
for lang in $sv_SE_aliases; do
        ln -s acor_sv-SE.dat acor_$lang.dat
done
%else
rm -f acor_[a-df-z]*.dat acor_e[su]*.dat
%endif
popd
#rhbz#484055 make these shared across multiple applications
mkdir -p $RPM_BUILD_ROOT/%{_datadir}
mv -f $RPM_BUILD_ROOT/%{basisinstdir}/share/autocorr $RPM_BUILD_ROOT/%{_datadir}/autocorr
chmod 755 $RPM_BUILD_ROOT/%{_datadir}/autocorr

%if %{langpacks}

#auto generate the langpack file lists, format is...
#langpack id, has help or not, autocorrection glob, script classification
langpackdetails=\
(\
af      help    western         ar      help    ctl     \
bg      help    western         bn      help    western \
ca      help    western         cs      help    western \
cy      nohelp  western         da      help    western \
de      help    western         el      help    western \
es      help    western         et      help    western \
eu      help    western         fi      help    western \
fr      help    western         ga      nohelp  western \
gl      help    western         gu      nohelp  ctl     \
pa-IN   help    ctl             he      nohelp  ctl     \
hi      help    ctl             hu      help    western \
hr      nohelp  western         it      help    western \
ja      help    cjk             ko      help    cjk     \
lt      help    western         ms      nohelp  western \
nb      help    western         nl      help    western \
nn      help    western         pl      help    western \
pt      help    western         pt-BR   help    western \
ru      help    western         sk      help    western \
sl      help    western         sr      help    western \
sv      help    western         ta      help    ctl     \
th      help    ctlseqcheck     tr      help    western \
zh-CN   help    cjk             zh-TW   help    cjk     \
zu      help    western         tn      help    western \
ts      help    western         as      nohelp  western \
mr      nohelp  western         ml      nohelp  western \
or      nohelp  ctl             te      nohelp  western \
ur      nohelp  western         kn      nohelp  western \
xh      help    western         ve      help    western \
st      help    western         ss      help    western \
nr      help    western         ns      help    western \
dz      help    ctl             uk      help    western \
sh      help    western         mai     help    western \
ro      nohelp  western
)

tar xzf %{SOURCE22}

i=0
while [ $i -lt ${#langpackdetails[@]} ]; do
   lang=${langpackdetails[$i]}
   sed -e "s/LANG/$lang/g" langpacks/libreoffice.langpack-common.template > $lang.filelist
   i=$[i+1]
   help=${langpackdetails[$i]}
   if [ "$help" = "help" ]; then
     sed -e "s/LANG/$lang/g" langpacks/libreoffice.langpack-help.template >> $lang.filelist
   fi
   i=$[i+1]
   type=${langpackdetails[$i]}
   if [ "$type" = "cjk" ]; then
     sed -e "s/LANG/$lang/g" langpacks/libreoffice.langpack-cjk.template >> $lang.filelist
   fi
   #rh217269 upstream made a decision to sequence check all ctl languages
   #I think this is wrong, and only Thai should be sequence checked
   if [ "$type" = "ctlseqcheck" ]; then
     sed -e "s/LANG/$lang/g" langpacks/libreoffice.langpack-ctl.template >> $lang.filelist
   fi
   if [ "$type" = "ctl" ]; then
     rm -f $RPM_BUILD_ROOT/%{basisinstdir}/share/registry/ctl_$lang.xcd
   fi
   i=$[i+1]
done

#rhbz#452379 clump serbian translations together
cat sh.filelist >> sr.filelist

%endif

#remove it in case we didn't build with gcj
rm -f $RPM_BUILD_ROOT/%{basisinstdir}/program/classes/sandbox.jar

#remove pagein stuff
rm -f $RPM_BUILD_ROOT/%{basisinstdir}/program/pagein*

#remove dummy .dat files
rm -f $RPM_BUILD_ROOT/%{basisinstdir}/program/root?.dat

#set standard permissions for rpmlint
find $RPM_BUILD_ROOT/%{baseinstdir} -exec chmod +w {} \;
find $RPM_BUILD_ROOT/%{baseinstdir} -type d -exec chmod 0755 {} \;

# move python bits into site-packages
mkdir -p $RPM_BUILD_ROOT/%{python_sitearch}
pushd $RPM_BUILD_ROOT/%{python_sitearch}
echo "import sys, os" > uno.py
echo "sys.path.append('%{basisinstdir}/program')" >> uno.py
echo "os.putenv('URE_BOOTSTRAP', 'vnd.sun.star.pathname:%{baseinstdir}/program/fundamentalrc')" >> uno.py
cat $RPM_BUILD_ROOT/%{basisinstdir}/program/uno.py >> uno.py
rm -f $RPM_BUILD_ROOT/%{basisinstdir}/program/uno.py*
mv -f $RPM_BUILD_ROOT/%{basisinstdir}/program/unohelper.py* .
popd

# rhbz#477435 package opensymbol separately
pushd $RPM_BUILD_ROOT/%{basisinstdir}/share/fonts/truetype
install -d -m 0755 %{buildroot}%{_fontdir}
install -p -m 0644 *.ttf %{buildroot}%{_fontdir}
popd
rm -rf $RPM_BUILD_ROOT/%{basisinstdir}/share/fonts

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
echo exec libreoffice -view \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/ooviewdoc
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/ooviewdoc

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oowriter
echo exec libreoffice -writer \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oowriter
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oowriter

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oocalc
echo exec libreoffice -calc \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oocalc
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oocalc

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/ooimpress
echo exec libreoffice -impress \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/ooimpress
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/ooimpress

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oodraw
echo exec libreoffice -draw \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oodraw
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oodraw

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oomath
echo exec libreoffice -math \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oomath
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oomath

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oobase
echo exec libreoffice -base \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oobase
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oobase

cp -f %{SOURCE25} $RPM_BUILD_ROOT/%{_bindir}/unopkg
sed -i -e "s/LAUNCHER/unopkg/g" $RPM_BUILD_ROOT/%{_bindir}/unopkg
sed -i -e "s/BRAND/libreoffice/g" $RPM_BUILD_ROOT/%{_bindir}/unopkg
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/unopkg

cp -f %{SOURCE25} $RPM_BUILD_ROOT/%{_bindir}/libreoffice
sed -i -e "s/LAUNCHER/soffice/g" $RPM_BUILD_ROOT/%{_bindir}/libreoffice
sed -i -e "s/BRAND/libreoffice/g" $RPM_BUILD_ROOT/%{_bindir}/libreoffice
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/libreoffice

pushd $RPM_BUILD_ROOT/%{_bindir}
# rhbz#499474 provide a /usr/bin/soffice for .recently-used.xbel
ln -s %{baseinstdir}/program/soffice soffice
# rhbz#499474 provide a /usr/bin/openoffice.org for backwards compat
ln -s %{baseinstdir}/program/libreoffice openoffice.org
popd

pushd $RPM_BUILD_ROOT/%{baseinstdir}/share/xdg/
chmod u+w *.desktop
rm -rf printeradmin.desktop
for file in *.desktop; do
    # rhbz#156677 remove the version from Name=
    sed -i -e "s/$PRODUCTVERSION //g" $file
    # rhbz#156067 don't version the icons
    sed -i -e "s/$PRODUCTVERSIONSHORT//g" $file
    # add X-GIO-NoFuse so we get url:// instead of file://~.gvfs/
    echo X-GIO-NoFuse=true >> $file
done
echo "StartupNotify=true" >> base.desktop
echo "StartupNotify=true" >> calc.desktop
echo "StartupNotify=true" >> impress.desktop
echo "StartupNotify=true" >> writer.desktop
echo "StartupNotify=true" >> math.desktop
echo "StartupNotify=true" >> draw.desktop
echo "TryExec=oobase" >> base.desktop
echo "TryExec=oocalc" >> calc.desktop
echo "TryExec=ooimpress" >> impress.desktop
echo "TryExec=oowriter" >> writer.desktop
echo "TryExec=oomath" >> math.desktop
echo "TryExec=oodraw" >> draw.desktop
# rhbz#156677# / rhbz#186515#
echo "NoDisplay=true" >> math.desktop
echo "NoDisplay=true" >> startcenter.desktop
# rhbz#491159 temporarily remove NoDisplay=true from qstart.desktop
sed -i -e "/NoDisplay=true/d" qstart.desktop
# relocate the .desktop and icon files
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
cp -p base.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/libreoffice-base.desktop
cp -p calc.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/libreoffice-calc.desktop
cp -p impress.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/libreoffice-impress.desktop
cp -p writer.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/libreoffice-writer.desktop
cp -p math.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/libreoffice-math.desktop
cp -p draw.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/libreoffice-draw.desktop
cp -p javafilter.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/libreoffice-javafilter.desktop
cp -p startcenter.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/libreoffice-startcenter.desktop
for desktop in *.desktop; do
    desktop-file-validate $desktop
done
popd

pushd sysui/output/usr/share/
#get rid of the gnome icons and other unneeded files
rm -rf icons/gnome applications application-registry
# rhbz#156067 don't version the icons
find . -name "*.desktop" -exec sed -i -e s/$PRODUCTVERSIONSHORT//g {} \;
find . -name "*libreoffice$PRODUCTVERSIONSHORT*" -print \
    | while read path; do
        mv $path `echo $path | sed s/libreoffice$PRODUCTVERSIONSHORT/libreoffice/`
    done
find . -type l -print \
    | while read path; do
        target=`readlink $path`
        new_target=`echo $target | sed -e s/$PRODUCTVERSIONSHORT//g`
        if [ "$target" != "$new_target" ]; then
            ln -sf $new_target $path
        fi
    done

sed -i -e s/libreoffice$PRODUCTVERSIONSHORT/libreoffice/g \
  ./mime-info/libreoffice.keys
#relocate the rest of them
cp -r icons $RPM_BUILD_ROOT/%{_datadir}
cp -r mime-info $RPM_BUILD_ROOT/%{_datadir}
#add our mime-types, e.g. for .oxt extensions
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mime/packages
cp -p mime/packages/libreoffice.xml $RPM_BUILD_ROOT/%{_datadir}/mime/packages
popd

rm -rf $RPM_BUILD_ROOT/%{baseinstdir}/readmes
rm -rf $RPM_BUILD_ROOT/%{baseinstdir}/licenses

mkdir -p $RPM_BUILD_ROOT/%{basisinstdir}/share/psprint/driver
cp -r psprint_config/configuration/ppds/SGENPRT.PS $RPM_BUILD_ROOT/%{basisinstdir}/share/psprint/driver/SGENPRT.PS

# rhbz#452385 to auto have postgres in classpath if subsequently installed
# rhbz#465664 to get lucene working for functional help
sed -i -e "s#URE_MORE_JAVA_CLASSPATH_URLS.*#& file:///usr/share/java/lucene.jar file:///usr/share/java/lucene-contrib/lucene-analyzers.jar file:///usr/share/java/postgresql-jdbc.jar#" $RPM_BUILD_ROOT/%{basisinstdir}/program/fundamentalbasisrc

%check
source ./Linux*Env.Set.sh
cd test
build && deliver -link
cd ../smoketestoo_native
#JFW_PLUGIN_DO_NOT_CHECK_ACCESSIBILITY="1" works around flawed accessibility check
#SAL_USE_VCLPLUGIN="svp" uses the headless plugin for these tests
JFW_PLUGIN_DO_NOT_CHECK_ACCESSIBILITY="1" SAL_USE_VCLPLUGIN="svp" timeout -k 2m 2h build.pl

%clean
rm -rf $RPM_BUILD_ROOT

%if %{langpacks}
%files langpack-af 	-f af.filelist
%defattr(-,root,root,-)

%files langpack-ar  	-f ar.filelist
%defattr(-,root,root,-)

%files langpack-bg 	-f bg.filelist
%defattr(-,root,root,-)

%files langpack-bn  	-f bn.filelist
%defattr(-,root,root,-)

%files langpack-ca 	-f ca.filelist
%defattr(-,root,root,-)

%files langpack-cs 	-f cs.filelist
%defattr(-,root,root,-)

%files langpack-cy 	-f cy.filelist
%defattr(-,root,root,-)

%files langpack-da 	-f da.filelist
%defattr(-,root,root,-)

%files langpack-de 	-f de.filelist
%defattr(-,root,root,-)

%files langpack-el 	-f el.filelist
%defattr(-,root,root,-)

%files langpack-en
%defattr(-,root,root,-)

%files langpack-es	-f es.filelist
%defattr(-,root,root,-)

%files langpack-et 	-f et.filelist
%defattr(-,root,root,-)

%files langpack-eu 	-f eu.filelist
%defattr(-,root,root,-)

%files langpack-fi 	-f fi.filelist
%defattr(-,root,root,-)

%files langpack-fr 	-f fr.filelist
%defattr(-,root,root,-)

%files langpack-ga 	-f ga.filelist
%defattr(-,root,root,-)

%files langpack-gl	-f gl.filelist
%defattr(-,root,root,-)

%files langpack-gu	-f gu.filelist
%defattr(-,root,root,-)

%files langpack-pa	-f pa-IN.filelist
%defattr(-,root,root,-)

%files langpack-he	-f he.filelist
%defattr(-,root,root,-)

%files langpack-hi	-f hi.filelist
%defattr(-,root,root,-)

%files langpack-hu	-f hu.filelist
%defattr(-,root,root,-)

%files langpack-hr	-f hr.filelist
%defattr(-,root,root,-)

%files langpack-it	-f it.filelist
%defattr(-,root,root,-)

%files langpack-ja 	-f ja.filelist
%defattr(-,root,root,-)

%files langpack-ko	-f ko.filelist
%defattr(-,root,root,-)
%{baseinstdir}/share/registry/korea.xcd

%files langpack-lt	-f lt.filelist
%defattr(-,root,root,-)

%files langpack-ms	-f ms.filelist
%defattr(-,root,root,-)

%files langpack-nb	-f nb.filelist
%defattr(-,root,root,-)

%files langpack-nl	-f nl.filelist
%defattr(-,root,root,-)

%files langpack-nn	-f nn.filelist
%defattr(-,root,root,-)

%files langpack-pl	-f pl.filelist
%defattr(-,root,root,-)

%files langpack-pt-PT	-f pt.filelist
%defattr(-,root,root,-)

%files langpack-pt-BR	-f pt-BR.filelist
%defattr(-,root,root,-)

%files langpack-ru	-f ru.filelist
%defattr(-,root,root,-)

%files langpack-sk	-f sk.filelist
%defattr(-,root,root,-)

%files langpack-sl	-f sl.filelist
%defattr(-,root,root,-)

%files langpack-sr	-f sr.filelist
%defattr(-,root,root,-)

%files langpack-sv	-f sv.filelist
%defattr(-,root,root,-)

%files langpack-ta	-f ta.filelist
%defattr(-,root,root,-)

%files langpack-th	-f th.filelist
%defattr(-,root,root,-)

%files langpack-tr	-f tr.filelist
%defattr(-,root,root,-)

%files langpack-zh-Hans	-f zh-CN.filelist
%defattr(-,root,root,-)

%files langpack-zh-Hant	-f zh-TW.filelist
%defattr(-,root,root,-)

%files langpack-zu	-f zu.filelist
%defattr(-,root,root,-)

%files langpack-tn	-f tn.filelist
%defattr(-,root,root,-)

%files langpack-ts	-f ts.filelist
%defattr(-,root,root,-)

%files langpack-nso	-f ns.filelist
%defattr(-,root,root,-)

%files langpack-nr	-f nr.filelist
%defattr(-,root,root,-)

%files langpack-ss	-f ss.filelist
%defattr(-,root,root,-)

%files langpack-st	-f st.filelist
%defattr(-,root,root,-)

%files langpack-ve	-f ve.filelist
%defattr(-,root,root,-)

%files langpack-xh	-f xh.filelist
%defattr(-,root,root,-)

%files langpack-as	-f as.filelist
%defattr(-,root,root,-)

%files langpack-mr	-f mr.filelist
%defattr(-,root,root,-)

%files langpack-ml	-f ml.filelist
%defattr(-,root,root,-)

%files langpack-or	-f or.filelist
%defattr(-,root,root,-)

%files langpack-te	-f te.filelist
%defattr(-,root,root,-)

%files langpack-ur	-f ur.filelist
%defattr(-,root,root,-)

%files langpack-kn	-f kn.filelist
%defattr(-,root,root,-)

%files langpack-dz	-f dz.filelist
%defattr(-,root,root,-)

%files langpack-uk	-f uk.filelist
%defattr(-,root,root,-)

%files langpack-mai	-f mai.filelist
%defattr(-,root,root,-)

%files langpack-ro	-f ro.filelist
%defattr(-,root,root,-)
%endif

%files core
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/help
%docdir %{basisinstdir}/help/en
%dir %{basisinstdir}/help/en
%{basisinstdir}/help/en/default.css
%{basisinstdir}/help/en/err.html
%{basisinstdir}/help/en/highcontrast1.css
%{basisinstdir}/help/en/highcontrast2.css
%{basisinstdir}/help/en/highcontrastblack.css
%{basisinstdir}/help/en/highcontrastwhite.css
%{basisinstdir}/help/en/sbasic.*
%{basisinstdir}/help/en/schart.*
%{basisinstdir}/help/en/shared.*
%{basisinstdir}/help/idxcaption.xsl
%{basisinstdir}/help/idxcontent.xsl
%{basisinstdir}/help/main_transform.xsl
%{basisinstdir}/presets
%dir %{basisinstdir}/program
%{basisinstdir}/program/addin
%{basisinstdir}/program/basprov%{SOPOST}.uno.so
%{basisinstdir}/program/canvasfactory.uno.so
%{basisinstdir}/program/cde-open-url
%dir %{basisinstdir}/program/classes
%{basisinstdir}/program/classes/agenda.jar                
%{basisinstdir}/program/classes/commonwizards.jar
%{basisinstdir}/program/classes/fax.jar
%{basisinstdir}/program/classes/form.jar
%{basisinstdir}/program/classes/query.jar          
%{basisinstdir}/program/classes/letter.jar          
%{basisinstdir}/program/classes/LuceneHelpWrapper.jar
%{basisinstdir}/program/classes/officebean.jar
%{basisinstdir}/program/classes/report.jar
%{basisinstdir}/program/classes/saxon9.jar
%{basisinstdir}/program/classes/ScriptFramework.jar
%{basisinstdir}/program/classes/ScriptProviderForJava.jar
%{basisinstdir}/program/classes/table.jar
%{basisinstdir}/program/classes/unoil.jar
%{basisinstdir}/program/classes/web.jar
%{basisinstdir}/program/classes/XMergeBridge.jar
%{basisinstdir}/program/classes/xmerge.jar
%{basisinstdir}/program/classes/XSLTFilter.jar
%{basisinstdir}/program/classes/XSLTValidate.jar
%{basisinstdir}/program/cmdmail.uno.so
%{basisinstdir}/program/deployment%{SOPOST}.uno.so
%{basisinstdir}/program/deploymentgui%{SOPOST}.uno.so
%{basisinstdir}/program/dlgprov%{SOPOST}.uno.so
%{basisinstdir}/program/fastsax.uno.so
%{basisinstdir}/program/fpicker.uno.so
%{basisinstdir}/program/fps_gnome.uno.so
%{basisinstdir}/program/fps_office.uno.so
%{basisinstdir}/program/fundamentalbasisrc
%{basisinstdir}/program/gengal*
%{basisinstdir}/program/gnome-open-url
%{basisinstdir}/program/gnome-open-url.bin
%{basisinstdir}/program/hatchwindowfactory.uno.so
%{basisinstdir}/program/i18nsearch.uno.so
%{basisinstdir}/program/kde-open-url
%{basisinstdir}/program/legacy_binfilters.rdb
%{basisinstdir}/program/libacc%{SOPOST}.so
%{basisinstdir}/program/libadabas%{SOPOST}.so
%{basisinstdir}/program/libavmedia*.so
%{basisinstdir}/program/libbasctl%{SOPOST}.so
%{basisinstdir}/program/libbf_sb%{SOPOST}.so
%{basisinstdir}/program/libbf_frm%{SOPOST}.so
%{basisinstdir}/program/libbf_go%{SOPOST}.so
%{basisinstdir}/program/libbf_migratefilter%{SOPOST}.so
%{basisinstdir}/program/libbf_ofa%{SOPOST}.so
%{basisinstdir}/program/libbf_sch%{SOPOST}.so
%{basisinstdir}/program/libbf_sd%{SOPOST}.so
%{basisinstdir}/program/libbf_so%{SOPOST}.so
%{basisinstdir}/program/libbf_svt%{SOPOST}.so
%{basisinstdir}/program/libbf_svx%{SOPOST}.so
%{basisinstdir}/program/libbf_wrapper%{SOPOST}.so
%{basisinstdir}/program/libbf_xo%{SOPOST}.so
%{basisinstdir}/program/libbib%{SOPOST}.so
%{basisinstdir}/program/libbindet%{SOPOST}.so
%{basisinstdir}/program/libcached1.so
%{basisinstdir}/program/libcanvastools%{SOPOST}.so
%{basisinstdir}/program/libchart*%{SOPOST}.so
%{basisinstdir}/program/libcollator_data.so
%{basisinstdir}/program/libcppcanvas%{SOPOST}.so
%{basisinstdir}/program/libctl%{SOPOST}.so
%{basisinstdir}/program/libcui%{SOPOST}.so
%{basisinstdir}/program/libdba%{SOPOST}.so
%{basisinstdir}/program/libdbacfg%{SOPOST}.so
%{basisinstdir}/program/libdbase%{SOPOST}.so
%{basisinstdir}/program/libdbaxml%{SOPOST}.so
%{basisinstdir}/program/libdbmm%{SOPOST}.so
%{basisinstdir}/program/libdbpool2.so
%{basisinstdir}/program/libdbtools%{SOPOST}.so
%{basisinstdir}/program/libdbu%{SOPOST}.so
%{basisinstdir}/program/libdeploymentmisc%{SOPOST}.so
%{basisinstdir}/program/libdesktop_detector%{SOPOST}.so
%{basisinstdir}/program/libdict_ja.so
%{basisinstdir}/program/libdict_zh.so
%{basisinstdir}/program/libdrawinglayer%{SOPOST}.so
%{basisinstdir}/program/libediteng%{SOPOST}.so
%{basisinstdir}/program/libeggtray%{SOPOST}.so
%{basisinstdir}/program/libembobj.so
%{basisinstdir}/program/libemboleobj.so
%{basisinstdir}/program/libevoab*.so
%{basisinstdir}/program/libevtatt.so
%{basisinstdir}/program/libegi%{SOPOST}.so    
%{basisinstdir}/program/libeme%{SOPOST}.so
%{basisinstdir}/program/libepb%{SOPOST}.so
%{basisinstdir}/program/libepg%{SOPOST}.so    
%{basisinstdir}/program/libepp%{SOPOST}.so
%{basisinstdir}/program/libeps%{SOPOST}.so    
%{basisinstdir}/program/libept%{SOPOST}.so
%{basisinstdir}/program/libera%{SOPOST}.so    
%{basisinstdir}/program/libeti%{SOPOST}.so
%{basisinstdir}/program/libexp%{SOPOST}.so    
%{basisinstdir}/program/libicd%{SOPOST}.so
%{basisinstdir}/program/libicg%{SOPOST}.so
%{basisinstdir}/program/libidx%{SOPOST}.so
%{basisinstdir}/program/libime%{SOPOST}.so
%{basisinstdir}/program/libindex_data.so
%{basisinstdir}/program/libipb%{SOPOST}.so
%{basisinstdir}/program/libipd%{SOPOST}.so
%{basisinstdir}/program/libips%{SOPOST}.so
%{basisinstdir}/program/libipt%{SOPOST}.so
%{basisinstdir}/program/libipx%{SOPOST}.so
%{basisinstdir}/program/libira%{SOPOST}.so
%{basisinstdir}/program/libitg%{SOPOST}.so
%{basisinstdir}/program/libiti%{SOPOST}.so
%{basisinstdir}/program/libofficebean.so
%{basisinstdir}/program/liboooimprovecore%{SOPOST}.so
%{basisinstdir}/program/libfile%{SOPOST}.so
%{basisinstdir}/program/libfilterconfig1.so
%{basisinstdir}/program/libflat%{SOPOST}.so
%{basisinstdir}/program/libfrm%{SOPOST}.so
%{basisinstdir}/program/libguesslang%{SOPOST}.so
%{basisinstdir}/program/libhelplinker%{SOPOST}.so
%{basisinstdir}/program/libhyphen%{SOPOST}.so
%{basisinstdir}/program/libi18nregexpgcc3.so
%{basisinstdir}/program/libjdbc%{SOPOST}.so
%{basisinstdir}/program/liblegacy_binfilters%{SOPOST}.so
%{basisinstdir}/program/liblng%{SOPOST}.so
%{basisinstdir}/program/liblog%{SOPOST}.so
%{basisinstdir}/program/liblocaledata_en.so
%{basisinstdir}/program/liblocaledata_es.so
%{basisinstdir}/program/liblocaledata_euro.so
%{basisinstdir}/program/liblocaledata_others.so
%{basisinstdir}/program/libmcnttype.so
%{basisinstdir}/program/libmozbootstrap.so
%{basisinstdir}/program/libmsfilter%{SOPOST}.so
%{basisinstdir}/program/libmsforms%{SOPOST}.uno.so
%{basisinstdir}/program/libmtfrenderer.uno.so
%{basisinstdir}/program/libmysql%{SOPOST}.so
%{basisinstdir}/program/libodbc%{SOPOST}.so
%{basisinstdir}/program/libodbcbase%{SOPOST}.so
%{basisinstdir}/program/liboffacc%{SOPOST}.so
%{basisinstdir}/program/liboox%{SOPOST}.so
%{basisinstdir}/program/libpcr%{SOPOST}.so
%{basisinstdir}/program/libpdffilter%{SOPOST}.so
%{basisinstdir}/program/libpl%{SOPOST}.so
%{basisinstdir}/program/libpreload%{SOPOST}.so
%{basisinstdir}/program/libprotocolhandler%{SOPOST}.so
%{basisinstdir}/program/libqstart_gtk%{SOPOST}.so
%{basisinstdir}/program/librecentfile.so
%{basisinstdir}/program/libres%{SOPOST}.so
%{basisinstdir}/program/libsax%{SOPOST}.so
%{basisinstdir}/program/libscn%{SOPOST}.so
%{basisinstdir}/program/libscriptframe.so
%{basisinstdir}/program/libsd%{SOPOST}.so
%{basisinstdir}/program/libsdfilt%{SOPOST}.so
%{basisinstdir}/program/libsdbc2.so
%{basisinstdir}/program/libsdbt%{SOPOST}so
%{basisinstdir}/program/libsdd%{SOPOST}.so
%{basisinstdir}/program/libsdui%{SOPOST}.so
%{basisinstdir}/program/libspa%{SOPOST}.so
%{basisinstdir}/program/libspell%{SOPOST}.so
%{basisinstdir}/program/libsrtrs1.so
%{basisinstdir}/program/libsts%{SOPOST}.so
%{basisinstdir}/program/libsvx%{SOPOST}.so
%{basisinstdir}/program/libsvxcore%{SOPOST}.so
%{basisinstdir}/program/libsw%{SOPOST}.so
%{basisinstdir}/program/libtextconv_dict.so
%{basisinstdir}/program/libtextconversiondlgs%{SOPOST}.so
%{basisinstdir}/program/libtvhlp1.so
%{basisinstdir}/program/libucbhelper4gcc3.so
%{basisinstdir}/program/libucpchelp1.so
%{basisinstdir}/program/libucpdav1.so
%{basisinstdir}/program/libucpftp1.so
%{basisinstdir}/program/libucphier1.so
%{basisinstdir}/program/libucppkg1.so
%{basisinstdir}/program/libunordf%{SOPOST}.so
%{basisinstdir}/program/libunopkgapp.so
%{basisinstdir}/program/libunoxml%{SOPOST}.so
%{basisinstdir}/program/libupdchk%{SOPOST}.so
%{basisinstdir}/program/libuui%{SOPOST}.so
%{basisinstdir}/program/libvbahelper%{SOPOST}.so
%{basisinstdir}/program/libvclplug_gen%{SOPOST}.so
%{basisinstdir}/program/libvclplug_gtk%{SOPOST}.so
%{basisinstdir}/program/libwpgimport%{SOPOST}.so
%{basisinstdir}/program/libxmlfa%{SOPOST}.so
%{basisinstdir}/program/libxmlfd%{SOPOST}.so
%{basisinstdir}/program/libxmx%{SOPOST}.so
%{basisinstdir}/program/libxof%{SOPOST}.so
%{basisinstdir}/program/libxsec_fw.so
%{basisinstdir}/program/libxsec_xmlsec.so
%{basisinstdir}/program/libxsltdlg%{SOPOST}.so
%{basisinstdir}/program/libxsltfilter%{SOPOST}.so
%{basisinstdir}/program/libxstor.so
%{basisinstdir}/program/migrationoo2.uno.so
%{basisinstdir}/program/nsplugin
%{basisinstdir}/program/open-url
%{basisinstdir}/program/offapi.rdb
%{basisinstdir}/program/passwordcontainer.uno.so
%{basisinstdir}/program/plugin
%{basisinstdir}/program/pluginapp.bin
%{basisinstdir}/program/productregistration.uno.so
%dir %{basisinstdir}/program/resource
%{basisinstdir}/program/resource/avmediaen-US.res
%{basisinstdir}/program/resource/accen-US.res
%{basisinstdir}/program/resource/basctlen-US.res
%{basisinstdir}/program/resource/bf_frmen-US.res
%{basisinstdir}/program/resource/bf_ofaen-US.res
%{basisinstdir}/program/resource/bf_schen-US.res
%{basisinstdir}/program/resource/bf_sden-US.res
%{basisinstdir}/program/resource/bf_svten-US.res
%{basisinstdir}/program/resource/bf_svxen-US.res
%{basisinstdir}/program/resource/biben-US.res
%{basisinstdir}/program/resource/calen-US.res
%{basisinstdir}/program/resource/chartcontrolleren-US.res
%{basisinstdir}/program/resource/cuien-US.res
%{basisinstdir}/program/resource/dbaen-US.res
%{basisinstdir}/program/resource/dbmmen-US.res
%{basisinstdir}/program/resource/dbuen-US.res
%{basisinstdir}/program/resource/dbwen-US.res
%{basisinstdir}/program/resource/deploymenten-US.res
%{basisinstdir}/program/resource/deploymentguien-US.res
%{basisinstdir}/program/resource/dkten-US.res
%{basisinstdir}/program/resource/editengen-US.res
%{basisinstdir}/program/resource/egien-US.res
%{basisinstdir}/program/resource/emeen-US.res
%{basisinstdir}/program/resource/epben-US.res
%{basisinstdir}/program/resource/epgen-US.res
%{basisinstdir}/program/resource/eppen-US.res
%{basisinstdir}/program/resource/epsen-US.res
%{basisinstdir}/program/resource/epten-US.res
%{basisinstdir}/program/resource/euren-US.res
%{basisinstdir}/program/resource/fps_officeen-US.res
%{basisinstdir}/program/resource/frmen-US.res
%{basisinstdir}/program/resource/fween-US.res
%{basisinstdir}/program/resource/galen-US.res
%{basisinstdir}/program/resource/impen-US.res
%{basisinstdir}/program/resource/ofaen-US.res
%{basisinstdir}/program/resource/pcren-US.res
%{basisinstdir}/program/resource/pdffilteren-US.res
%{basisinstdir}/program/resource/preloaden-US.res
%{basisinstdir}/program/resource/productregistrationen-US.res
%{basisinstdir}/program/resource/sanen-US.res
%{basisinstdir}/program/resource/sben-US.res
%{basisinstdir}/program/resource/sden-US.res
%{basisinstdir}/program/resource/sfxen-US.res
%{basisinstdir}/program/resource/spaen-US.res
%{basisinstdir}/program/resource/sdbten-US.res
%{basisinstdir}/program/resource/svsen-US.res
%{basisinstdir}/program/resource/svten-US.res
%{basisinstdir}/program/resource/svxen-US.res
%{basisinstdir}/program/resource/swen-US.res
%{basisinstdir}/program/resource/textconversiondlgsen-US.res
%{basisinstdir}/program/resource/tken-US.res
%{basisinstdir}/program/resource/tplen-US.res
%{basisinstdir}/program/resource/uuien-US.res
%{basisinstdir}/program/resource/updchken-US.res
%{basisinstdir}/program/resource/upden-US.res
%{basisinstdir}/program/resource/vclen-US.res
%{basisinstdir}/program/resource/wzien-US.res
%{basisinstdir}/program/resource/xmlsecen-US.res
%{basisinstdir}/program/resource/xsltdlgen-US.res
%{basisinstdir}/program/sax.uno.so
%{basisinstdir}/program/senddoc
%{basisinstdir}/program/services.rdb
%{basisinstdir}/program/simplecanvas.uno.so
%{basisinstdir}/program/slideshow.uno.so
%{basisinstdir}/program/libsofficeapp.so
%{basisinstdir}/program/spadmin.bin
%{basisinstdir}/program/stringresource%{SOPOST}.uno.so
%{basisinstdir}/program/syssh.uno.so
%{basisinstdir}/program/ucpexpand1.uno.so
%{basisinstdir}/program/ucpext.uno.so
%{basisinstdir}/program/ucptdoc1.uno.so
%{basisinstdir}/program/unorc
%{basisinstdir}/program/updatefeed.uno.so
%{basisinstdir}/ure-link
%{basisinstdir}/program/uri-encode
%{basisinstdir}/program/vbaevents%{SOPOST}.uno.so
%{basisinstdir}/program/vclcanvas.uno.so
%{basisinstdir}/program/versionrc
%{basisinstdir}/program/cairocanvas.uno.so
%dir %{basisinstdir}/share
%dir %{basisinstdir}/share/Scripts
%{basisinstdir}/share/Scripts/java
%{basisinstdir}/share/autotext
%{basisinstdir}/share/basic
%dir %{basisinstdir}/share/config
%{basisinstdir}/share/config/images.zip
%{basisinstdir}/share/config/images_classic.zip
%{basisinstdir}/share/config/images_crystal.zip
%{basisinstdir}/share/config/images_hicontrast.zip
%{basisinstdir}/share/config/images_oxygen.zip
%{basisinstdir}/share/config/images_tango.zip
%{basisinstdir}/share/config/javasettingsunopkginstall.xml
%{basisinstdir}/share/config/psetup.xpm
%{basisinstdir}/share/config/psetupl.xpm
%dir %{basisinstdir}/share/config/soffice.cfg
%{basisinstdir}/share/config/soffice.cfg/modules
%{basisinstdir}/share/config/symbol
%{basisinstdir}/share/config/webcast
%{basisinstdir}/share/config/wizard
%dir %{basisinstdir}/share/dtd
%{basisinstdir}/share/dtd/officedocument
%{basisinstdir}/share/gallery
%dir %{basisinstdir}/share/psprint
%config %{basisinstdir}/share/psprint/psprint.conf
%{basisinstdir}/share/psprint/driver
%dir %{basisinstdir}/share/registry
%{basisinstdir}/share/registry/binfilter.xcd
%{basisinstdir}/share/registry/gnome.xcd
%{basisinstdir}/share/registry/lingucomponent.xcd
%{basisinstdir}/share/registry/main.xcd
%{basisinstdir}/share/registry/oo-ad-ldap.xcd.sample
%{basisinstdir}/share/registry/oo-ldap.xcd.sample
%{basisinstdir}/share/registry/Langpack-en-US.xcd
%dir %{basisinstdir}/share/registry/modules
%dir %{basisinstdir}/share/registry/modules/org
%dir %{basisinstdir}/share/registry/modules/org/openoffice
%dir %{basisinstdir}/share/registry/modules/org/openoffice/Office
%dir %{basisinstdir}/share/registry/modules/org/openoffice/Office/Paths
%{basisinstdir}/share/registry/modules/org/openoffice/Office/Paths/SystemAutoCorrect.xcu
%dir %{basisinstdir}/share/registry/modules/org/openoffice/Office/Recovery
%{basisinstdir}/share/registry/modules/org/openoffice/Office/Recovery/AutoSaveRecovery.xcu
%dir %{basisinstdir}/share/registry/res
%{basisinstdir}/share/registry/res/fcfg_langpack_en-US.xcd
%dir %{basisinstdir}/share/samples
%{basisinstdir}/share/samples/en-US
%dir %{basisinstdir}/share/template
%{basisinstdir}/share/template/en-US
%{basisinstdir}/share/template/wizard
%dir %{basisinstdir}/share/wordbook
%{basisinstdir}/share/wordbook/en-US
%dir %{basisinstdir}/share/xslt
%{basisinstdir}/share/xslt/common
%dir %{basisinstdir}/share/xslt/export
%{basisinstdir}/share/xslt/export/common
%{basisinstdir}/share/xslt/export/spreadsheetml
%{basisinstdir}/share/xslt/export/wordml
%dir %{basisinstdir}/share/xslt/import
%{basisinstdir}/share/xslt/import/common
%{basisinstdir}/share/xslt/import/spreadsheetml
%{basisinstdir}/share/xslt/import/wordml
%{basisinstdir}/program/liblnth%{SOPOST}.so
%{_bindir}/unopkg
#icons and mime
%{_datadir}/icons/*/*/*/gnome*
%{_datadir}/icons/*/*/*/libreoffice*
%{_datadir}/mime-info/libreoffice.*
%{basisinstdir}/program/libxmlsecurity.so
%{_datadir}/mime/packages/libreoffice.xml
%{basisinstdir}/program/configmgr.uno.so
%{basisinstdir}/program/desktopbe1.uno.so
%{basisinstdir}/program/fsstorage.uno.so
%{basisinstdir}/program/gconfbe1.uno.so
%{basisinstdir}/program/i18npool.uno.so
%{basisinstdir}/program/libbasegfx%{SOPOST}.so
%{basisinstdir}/program/libcomphelp4gcc3.so
%{basisinstdir}/program/libfileacc.so
%{basisinstdir}/program/libfwe%{SOPOST}.so
%{basisinstdir}/program/libfwi%{SOPOST}.so
%{basisinstdir}/program/libfwk%{SOPOST}.so
%{basisinstdir}/program/libfwl%{SOPOST}.so
%{basisinstdir}/program/libfwm%{SOPOST}.so
%{basisinstdir}/program/libi18nisolang*.so
%{basisinstdir}/program/libi18npaper*.so
%{basisinstdir}/program/libi18nutilgcc3.so
%{basisinstdir}/program/libpackage2.so
%{basisinstdir}/program/libsb%{SOPOST}.so
%{basisinstdir}/program/libsfx%{SOPOST}.so
%{basisinstdir}/program/libsot%{SOPOST}.so
%{basisinstdir}/program/libspl%{SOPOST}.so
%{basisinstdir}/program/libsvl%{SOPOST}.so
%{basisinstdir}/program/libsvt%{SOPOST}.so
%{basisinstdir}/program/libtk%{SOPOST}.so
%{basisinstdir}/program/libtl%{SOPOST}.so
%{basisinstdir}/program/libucb1.so
%{basisinstdir}/program/libucpfile1.so
%{basisinstdir}/program/libutl%{SOPOST}.so
%{basisinstdir}/program/libvcl%{SOPOST}.so
%{basisinstdir}/program/libvos3gcc3.so
%{basisinstdir}/program/libxcr%{SOPOST}.so
%{basisinstdir}/program/libxo%{SOPOST}.so
%{basisinstdir}/program/localebe1.uno.so
%{basisinstdir}/program/ucpgio1.uno.so
%{basisinstdir}/program/oovbaapi.rdb
#share unopkg
%dir %{baseinstdir}
%{baseinstdir}/basis-link
%dir %{baseinstdir}/share
%dir %{baseinstdir}/share/extensions
%{baseinstdir}/share/extensions/package.txt
%dir %{baseinstdir}/program
%{baseinstdir}/program/unopkg
%{baseinstdir}/program/unopkg.bin
%{baseinstdir}/program/bootstraprc
%{baseinstdir}/program/fundamentalrc
%{baseinstdir}/program/setuprc
%{baseinstdir}/program/versionrc
%doc %{baseinstdir}/LICENSE
%doc %{baseinstdir}/LICENSE.html
%doc %{baseinstdir}/LICENSE.odt
%doc %{baseinstdir}/README
%doc %{baseinstdir}/README.html
%doc %{baseinstdir}/THIRDPARTYLICENSEREADME.html
%dir %{baseinstdir}/program
%{baseinstdir}/program/about.*
%{baseinstdir}/program/intro.*
%dir %{baseinstdir}/program/resource
%{baseinstdir}/program/resource/oooen-US.res
%{baseinstdir}/program/soffice
%{baseinstdir}/program/soffice.bin
%{baseinstdir}/program/sofficerc
%{baseinstdir}/program/spadmin
%{baseinstdir}/program/unoinfo
%{baseinstdir}/program/libnpsoplugin.so
%dir %{baseinstdir}/share
%dir %{baseinstdir}/share/config
%{baseinstdir}/share/config/images_brand.zip
%docdir %{baseinstdir}/share/readme
%dir %{baseinstdir}/share/readme
%{baseinstdir}/share/readme/LICENSE_en-US
%{baseinstdir}/share/readme/LICENSE_en-US.html
%{baseinstdir}/share/readme/README_en-US
%{baseinstdir}/share/readme/README_en-US.html
%dir %{baseinstdir}/share/registry
%{baseinstdir}/share/registry/brand.xcd
%{baseinstdir}/share/xdg/
%{baseinstdir}/program/redirectrc
%{_datadir}/applications/libreoffice-startcenter.desktop
#launchers
%{_bindir}/libreoffice
%{_bindir}/openoffice.org
%{_bindir}/soffice
%{_bindir}/ooffice
%{_bindir}/ooviewdoc

%post core
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database %{_datadir}/applications &> /dev/null || :
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  for theme in hicolor locolor; do
    if test -d "%{_datadir}/icons/$theme"; then
      if test -f "%{_datadir}/icons/$theme/index.theme"; then
        touch --no-create %{_datadir}/icons/$theme
        gtk-update-icon-cache -q %{_datadir}/icons/$theme
      fi
    fi
  done
fi

%postun core
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database %{_datadir}/applications &> /dev/null || :
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  for theme in hicolor locolor; do
    if test -d "%{_datadir}/icons/$theme"; then
      if test -f "%{_datadir}/icons/$theme/index.theme"; then
        touch --no-create %{_datadir}/icons/$theme
        gtk-update-icon-cache -q %{_datadir}/icons/$theme
      fi
    fi
  done
fi

%files base
%defattr(-,root,root,-)
%dir %{basisinstdir}
%{basisinstdir}/help/en/sdatabase.*
%dir %{basisinstdir}/program
%dir %{basisinstdir}/program/classes
%{basisinstdir}/program/classes/sdbc_hsqldb.jar
%{basisinstdir}/program/libabp%{SOPOST}.so
%{basisinstdir}/program/libadabasui%{SOPOST}.so
%{basisinstdir}/program/libdbp%{SOPOST}.so
%{basisinstdir}/program/libhsqldb.so
%{basisinstdir}/program/librpt*%{SOPOST}.so
%dir %{basisinstdir}/program/resource
%{basisinstdir}/program/resource/abpen-US.res
%{basisinstdir}/program/resource/adabasuien-US.res
%{basisinstdir}/program/resource/cnren-US.res
%{basisinstdir}/program/resource/dbpen-US.res
%{basisinstdir}/program/resource/rpten-US.res
%{basisinstdir}/program/resource/rptuien-US.res
%{basisinstdir}/program/resource/sdbclen-US.res
%{basisinstdir}/program/resource/sdberren-US.res
%{basisinstdir}/share/registry/base.xcd
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/sbase
%{_datadir}/applications/libreoffice-base.desktop
%{_bindir}/oobase

%post base
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun base
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files report-builder
%defattr(-,root,root,-)
%docdir %{baseinstdir}/share/extensions/report-builder/help
%{baseinstdir}/share/extensions/report-builder

%files bsh
%defattr(-,root,root,-)
%{basisinstdir}/share/Scripts/beanshell
%{baseinstdir}/share/extensions/ScriptProviderForBeanShell.oxt

%files rhino
%defattr(-,root,root,-)
%{basisinstdir}/program/classes/js.jar
%{basisinstdir}/share/Scripts/javascript
%{baseinstdir}/share/extensions/ScriptProviderForJavaScript.oxt

%files wiki-publisher
%defattr(-,root,root,-)
%docdir %{baseinstdir}/share/extensions/wiki-publisher/license
%{baseinstdir}/share/extensions/wiki-publisher

%files ogltrans
%defattr(-,root,root,-)
%dir %{baseinstdir}
%dir %{basisinstdir}/program
%{basisinstdir}/program/OGLTrans.uno.so
%dir %{basisinstdir}/share/config
%dir %{basisinstdir}/share/config/soffice.cfg
%dir %{basisinstdir}/share/config/soffice.cfg/simpress
%{basisinstdir}/share/config/soffice.cfg/simpress/transitions-ogl.xml
%{basisinstdir}/share/registry/ogltrans.xcd

%files presentation-minimizer
%defattr(-,root,root,-)
%docdir %{baseinstdir}/share/extensions/presentation-minimizer/help
%{baseinstdir}/share/extensions/presentation-minimizer

%files presenter-screen
%defattr(-,root,root,-)
%docdir %{baseinstdir}/share/extensions/presenter-screen/help
%{baseinstdir}/share/extensions/presenter-screen

%files pdfimport
%defattr(-,root,root,-)
%docdir %{baseinstdir}/share/extensions/pdfimport/help
%{baseinstdir}/share/extensions/pdfimport

%_font_pkg -n %{fontname} opens___.ttf
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_fontdir}

%files calc
%defattr(-,root,root,-)
%dir %{basisinstdir}
%{basisinstdir}/help/en/scalc.*
%dir %{basisinstdir}/program
%{basisinstdir}/program/libanalysis%{SOPOST}.so
%{basisinstdir}/program/libbf_sc%{SOPOST}.so
%{basisinstdir}/program/libcalc%{SOPOST}.so
%{basisinstdir}/program/libdate%{SOPOST}.so
%{basisinstdir}/program/libfor%{SOPOST}.so
%{basisinstdir}/program/libforui%{SOPOST}.so
%{basisinstdir}/program/libsc%{SOPOST}.so
%{basisinstdir}/program/libscd%{SOPOST}.so
%{basisinstdir}/program/libscfilt%{SOPOST}.so
%{basisinstdir}/program/libscui%{SOPOST}.so
%{basisinstdir}/program/libsolver%{SOPOST}.so
%dir %{basisinstdir}/program/resource
%{basisinstdir}/program/resource/analysisen-US.res
%{basisinstdir}/program/resource/bf_scen-US.res
%{basisinstdir}/program/resource/dateen-US.res
%{basisinstdir}/program/resource/foren-US.res
%{basisinstdir}/program/resource/foruien-US.res
%{basisinstdir}/program/resource/scen-US.res
%{basisinstdir}/program/resource/solveren-US.res
%{basisinstdir}/program/libvbaobj%{SOPOST}.uno.so
%{basisinstdir}/share/registry/calc.xcd
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/scalc
%{baseinstdir}/program/scalc.bin
%{_datadir}/applications/libreoffice-calc.desktop
%{_bindir}/oocalc

%post calc
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun calc
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files draw
%defattr(-,root,root,-)
%dir %{basisinstdir}
%{basisinstdir}/help/en/sdraw.*
%{basisinstdir}/share/registry/draw.xcd
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/sdraw
%{baseinstdir}/program/sdraw.bin
%{_datadir}/applications/libreoffice-draw.desktop
%{_bindir}/oodraw

%post draw
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun draw
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files emailmerge
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/program
%{basisinstdir}/program/mailmerge.py*

%files writer
%defattr(-,root,root,-)
%dir %{basisinstdir}
%{basisinstdir}/help/en/swriter.*
%dir %{basisinstdir}/program
%{basisinstdir}/program/libbf_sw%{SOPOST}.so
%{basisinstdir}/program/libhwp.so
%{basisinstdir}/program/libmsword%{SOPOST}.so
%{basisinstdir}/program/libmsworks%{SOPOST}.so
%{basisinstdir}/program/libswd%{SOPOST}.so
%{basisinstdir}/program/libswui%{SOPOST}.so
%{basisinstdir}/program/libt602filter%{SOPOST}.so
%{basisinstdir}/program/libwpft%{SOPOST}.so
%{basisinstdir}/program/libwriterfilter%{SOPOST}.so
%{basisinstdir}/program/libvbaswobj%{SOPOST}.uno.so
%dir %{basisinstdir}/program/resource
%{basisinstdir}/program/resource/bf_swen-US.res
%{basisinstdir}/program/resource/t602filteren-US.res
%dir %{basisinstdir}/share/registry/modules
%dir %{basisinstdir}/share/registry/modules/org
%dir %{basisinstdir}/share/registry/modules/org/openoffice
%dir %{basisinstdir}/share/registry/modules/org/openoffice/Office
%dir %{basisinstdir}/share/registry/modules/org/openoffice/Office/Writer
%{basisinstdir}/share/registry/modules/org/openoffice/Office/Writer/TableNumberRecognition.xcu
%{basisinstdir}/share/registry/writer.xcd
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/swriter
%{baseinstdir}/program/swriter.bin
%{_datadir}/applications/libreoffice-writer.desktop
%{_bindir}/oowriter

%post writer
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun writer
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files impress
%defattr(-,root,root,-)
%dir %{basisinstdir}
%{basisinstdir}/help/en/simpress.*
%dir %{basisinstdir}/program
%{basisinstdir}/program/libanimcore.so
%{basisinstdir}/program/libplaceware*.so
%dir %{basisinstdir}/share/config
%dir %{basisinstdir}/share/config/soffice.cfg
%dir %{basisinstdir}/share/config/soffice.cfg/simpress
%{basisinstdir}/share/config/soffice.cfg/simpress/effects.xml
%{basisinstdir}/share/config/soffice.cfg/simpress/transitions.xml
%{basisinstdir}/share/registry/impress.xcd
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/simpress
%{baseinstdir}/program/simpress.bin
%{_datadir}/applications/libreoffice-impress.desktop
%{_bindir}/ooimpress

%post impress
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun impress
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files math
%defattr(-,root,root,-)
%dir %{basisinstdir}
%{basisinstdir}/help/en/smath.*
%dir %{basisinstdir}/program
%{basisinstdir}/program/libbf_sm%{SOPOST}.so
%{basisinstdir}/program/libsm%{SOPOST}.so
%{basisinstdir}/program/libsmd%{SOPOST}.so
%dir %{basisinstdir}/program/resource
%{basisinstdir}/program/resource/bf_smen-US.res
%{basisinstdir}/program/resource/smen-US.res
%dir %{basisinstdir}/share/registry/modules
%dir %{basisinstdir}/share/registry/modules/org
%dir %{basisinstdir}/share/registry/modules/org/openoffice
%dir %{basisinstdir}/share/registry/modules/org/openoffice/Office
%dir %{basisinstdir}/share/registry/modules/org/openoffice/Office/Math
%{basisinstdir}/share/registry/modules/org/openoffice/Office/Math/MathPrintOptions.xcu
%{basisinstdir}/share/registry/math.xcd
%dir %{baseinstdir}
%dir %{baseinstdir}/program
%{baseinstdir}/program/smath
%{_datadir}/applications/libreoffice-math.desktop
%{_bindir}/oomath

%post math
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun math
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files graphicfilter
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/program
%{basisinstdir}/program/libflash%{SOPOST}.so
%{basisinstdir}/program/libsvgfilter%{SOPOST}.so
%{basisinstdir}/share/registry/graphicfilter.xcd

%files xsltfilter
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/share/xslt
%{basisinstdir}/share/xslt/docbook
%dir %{basisinstdir}/share/xslt/export
%{basisinstdir}/share/xslt/export/uof
%{basisinstdir}/share/xslt/export/xhtml
%dir %{basisinstdir}/share/xslt/import
%{basisinstdir}/share/xslt/import/uof
%{basisinstdir}/share/registry/xsltfilter.xcd

%files javafilter
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/program
%dir %{basisinstdir}/program/classes
%{basisinstdir}/program/classes/aportisdoc.jar
%{basisinstdir}/program/classes/pexcel.jar
%{basisinstdir}/program/classes/pocketword.jar
%{_datadir}/applications/libreoffice-javafilter.desktop
%{basisinstdir}/share/registry/palm.xcd
%{basisinstdir}/share/registry/pocketexcel.xcd
%{basisinstdir}/share/registry/pocketword.xcd

%files testtools
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/program
%{basisinstdir}/program/hid.lst
%{basisinstdir}/program/libcommuni%{SOPOST}.so
%{ureinstdir}/lib/libsalalloc_malloc.so.3
%{basisinstdir}/program/libsimplecm%{SOPOST}.so
%{basisinstdir}/program/testtoolrc
%{basisinstdir}/program/testtool.bin
%dir %{basisinstdir}/program/resource
%{basisinstdir}/program/resource/stten-US.res

%files ure
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{baseinstdir}
%{ureinstdir}
%exclude %{ureinstdir}/lib/libsalalloc_malloc.so.3

%files sdk
%defattr(-,root,root,-)
%{sdkinstdir}/
%exclude %{sdkinstdir}/docs/
%exclude %{sdkinstdir}/examples/

%files sdk-doc
%defattr(-,root,root,-)
%docdir %{sdkinstdir}/docs
%{sdkinstdir}/docs/
%{sdkinstdir}/examples/

%files headless
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/program
%{basisinstdir}/program/libbasebmp%{SOPOST}.so
%{basisinstdir}/program/libvclplug_svp%{SOPOST}.so

%files pyuno
%defattr(-,root,root,-)
%dir %{basisinstdir}
%dir %{basisinstdir}/program
%{basisinstdir}/program/libpyuno.so
%{basisinstdir}/program/officehelper.py*
%{basisinstdir}/program/pythonloader.py*
%{basisinstdir}/program/pythonloader.uno.so
%{basisinstdir}/program/pythonloader.unorc
%{basisinstdir}/program/pyuno.so
%dir %{basisinstdir}/share/Scripts
%{basisinstdir}/share/Scripts/python
%{python_sitearch}/uno.py*
%{python_sitearch}/unohelper.py*
%{baseinstdir}/share/extensions/ScriptProviderForPython.oxt
%{basisinstdir}/share/registry/pyuno.xcd

%files -n autocorr-en
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_en-*

%if %{langpacks}

%files -n autocorr-af
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_af-*

%files -n autocorr-bg
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_bg-*

%files -n autocorr-cs
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_cs-*

%files -n autocorr-da
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_da-*

%files -n autocorr-de
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_de-*

%files -n autocorr-es
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_es-*

%files -n autocorr-eu
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_eu.dat

%files -n autocorr-fa
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_fa-*

%files -n autocorr-fi
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_fi-*

%files -n autocorr-fr
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_fr-*

%files -n autocorr-ga
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_ga-*

%files -n autocorr-hu
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_hu-*

%files -n autocorr-it
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_it-*

%files -n autocorr-ja
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_ja-*

%files -n autocorr-ko
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_ko-*

%files -n autocorr-lb
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_lb-*

%files -n autocorr-lt
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_lt-*

%files -n autocorr-nl
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_nl-*

%files -n autocorr-mn
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_mn-*

%files -n autocorr-pl
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_pl-*

%files -n autocorr-pt
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_pt-*

%files -n autocorr-ru
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_ru-*

%files -n autocorr-sk
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_sk-*

%files -n autocorr-sl
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_sl-*

%files -n autocorr-sr
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_sr-*
%{_datadir}/autocorr/acor_sh-*

%files -n autocorr-sv
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_sv-*

%files -n autocorr-tr
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_tr-*

%files -n autocorr-vi
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_vi-*

%files -n autocorr-zh
%defattr(-,root,root,-)
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE
%dir %{_datadir}/autocorr
%{_datadir}/autocorr/acor_zh-*

%endif

%changelog
* Wed Oct 06 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.1-2
- Related: rhbz#639945 pull in review changes
  + redland build-fix
  + replace awk script
  + validate .destop files

* Wed Sep 29 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.1-1
- initial import of the leviathan
