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
%define langpack_langs af ar bg bn ca cs cy da de dz el en-US es et eu fi fr ga gl gu pa-IN he hi hu hr it ja ko lt ms nb nl nn nr pl pt pt-BR ru sh sk sl sr ss st sv ta th tr ve xh zh-CN zh-TW zu ns tn ts as mr ml or te ur kn uk mai ro si
%else
%define langpack_langs en-US
%endif

Summary:        Free Software Productivity Suite
Name:           libreoffice
Version:        3.2.99.3
Release:        1%{?dist}
License:        LGPLv3 and LGPLv2+ and BSD and (MPLv1.1 or GPLv2 or LGPLv2 or Netscape) and (CDDL or GPLv2) and Public Domain
Group:          Applications/Productivity
URL:            http://www.documentfoundation.org/develop
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:        http://download.documentfoundation.org/libreoffice/src/libreoffice-artwork-3.2.99.3.tar.bz2
Source1:        http://download.documentfoundation.org/libreoffice/src/libreoffice-base-3.2.99.3.tar.bz2
Source2:        http://download.documentfoundation.org/libreoffice/src/libreoffice-bootstrap-3.2.99.3.tar.bz2
Source3:        http://download.documentfoundation.org/libreoffice/src/libreoffice-calc-3.2.99.3.tar.bz2
Source4:        http://download.documentfoundation.org/libreoffice/src/libreoffice-components-3.2.99.3.tar.bz2
Source5:        http://download.documentfoundation.org/libreoffice/src/libreoffice-extensions-3.2.99.3.tar.bz2
Source6:        http://download.documentfoundation.org/libreoffice/src/libreoffice-extras-3.2.99.3.tar.bz2
Source7:        http://download.documentfoundation.org/libreoffice/src/libreoffice-filters-3.2.99.3.tar.bz2
Source8:        http://download.documentfoundation.org/libreoffice/src/libreoffice-help-3.2.99.3.tar.bz2
Source9:        http://download.documentfoundation.org/libreoffice/src/libreoffice-impress-3.2.99.3.tar.bz2
Source10:       http://download.documentfoundation.org/libreoffice/src/libreoffice-libs-core-3.2.99.3.tar.bz2
Source11:       http://download.documentfoundation.org/libreoffice/src/libreoffice-libs-extern-3.2.99.3.tar.bz2
Source12:       http://download.documentfoundation.org/libreoffice/src/libreoffice-libs-extern-sys-3.2.99.3.tar.bz2
Source13:       http://download.documentfoundation.org/libreoffice/src/libreoffice-libs-gui-3.2.99.3.tar.bz2
Source14:       http://download.documentfoundation.org/libreoffice/src/libreoffice-postprocess-3.2.99.3.tar.bz2
Source15:       http://download.documentfoundation.org/libreoffice/src/libreoffice-sdk-3.2.99.3.tar.bz2
Source16:       http://download.documentfoundation.org/libreoffice/src/libreoffice-testing-3.2.99.3.tar.bz2
Source17:       http://download.documentfoundation.org/libreoffice/src/libreoffice-ure-3.2.99.3.tar.bz2
Source18:       http://download.documentfoundation.org/libreoffice/src/libreoffice-writer-3.2.99.3.tar.bz2
Source19:       http://cgit.freedesktop.org/ooo-build/ooo-build/plain/src/evolocal.odb
Source20:       http://tools.openoffice.org/unowinreg_prebuild/680/unowinreg.dll
Source21:       redhat-langpacks.tar.gz
Source23:       libreoffice-multiliblauncher.sh
Source26:       http://hg.services.openoffice.org/binaries/fdb27bfe2dbe2e7b57ae194d9bf36bab-SampleICC-1.3.2.tar.gz
Source27:       http://hg.services.openoffice.org/binaries/a7983f859eafb2677d7ff386a023bc40-xsltml_2.1.2.zip
Source28:       http://hg.services.openoffice.org/binaries/1f24ab1d39f4a51faf22244c94a6203f-xmlsec1-1.2.14.tar.gz
Source29:       http://hg.services.openoffice.org/binaries/798b2ffdc8bcfe7bca2cf92b62caf685-rhino1_5R5.zip
Source30:       http://hg.services.openoffice.org/binaries/35c94d2df8893241173de1d16b6034c0-swingExSrc.zip
Source31:       http://hg.services.openoffice.org/binaries/ada24d37d8d638b3d8a9985e80bc2978-source-9.0.0.7-bj.zip
Source32:       http://hg.services.openoffice.org/binaries/18f577b374d60b3c760a3a3350407632-STLport-4.5.tar.gz 
Source33:       http://download.documentfoundation.org/libreoffice/src/libreoffice-l10n-3.2.99.3.tar.bz2
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

Patch1:  openoffice.org-1.9.123.ooo53397.prelinkoptimize.desktop.patch
Patch2:  openoffice.org-2.0.2.rh188467.printingdefaults.patch
Patch3:  openoffice.org-2.4.0.ooo86080.unopkg.bodge.patch
Patch4:  openoffice.org-3.0.0.ooo88341.sc.verticalboxes.patch
Patch5:  openoffice.org-2.2.0.gccXXXXX.solenv.javaregistration.patch
Patch6:  openoffice.org-3.1.0.oooXXXXX.solenv.allowmissing.patch
Patch7:  openoffice.org-3.1.0.ooo101274.opening-a-directory.patch
Patch8:  openoffice.org-3.1.0.ooo102061.sc.cellanchoring.patch
Patch9:  openoffice.org-3.1.1.ooo105784.vcl.sniffscriptforsubs.patch
Patch10: openoffice.org-3.3.0.ooo108637.sfx2.uisavedir.patch
Patch11: openoffice.org-3.3.0.ooo113273.desktop.resolvelinks.patch
Patch12: turn-script-providers-into-extensions.patch

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
Obsoletes: openoffice.org-opensymbol-fonts < 1:3.3.1
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


# Defines a language pack subpackage.
#
# It's necessary to define language code (-l) and language name (-n).
# Additionally, it's possible
# * to require autocorr, hunspell, hyphen or mythes package or font for
#   given language,
# * to obsolete openoffice.org-langpack package,
# * to require other, unrelated, packages,
# * to specify file serving as file list.
# For these, lower case character argument takes an argument specifying
# language, upper case character argument uses language from -l.
#
# All remaining arguments are considered to be files and added to the file
# list.
#
# Aa: autocorr dependency
# Ff: font language dependency
# Hh: hunspell dependency
# l:  language code, e.g., cs
# Mm: mythes dependency
# n:  language name, e.g., Czech
# Oo: Obsoletes: of openoffice.org-langpack
# r:  comma-separated list of additional requires
# Ss: filelist
# Yy: hyphen dependency
#
# Example:
# libreoffice-langpack-cs: langpack for Czech lang. requiring hyphen-cs,
# autocorr-cs, mythes-cs-CZ and suitable font, obsoleting
# openoffice.org-langpack-cs_CZ, and taking the files from cs.filelist:
# %langpack -l cs -n Czech -H -A -m cs-CZ -o cs_CZ -S
%define langpack(Aa:Ff:Hh:l:Mm:n:Oo:r:Ss:Yy:) \
%define project LibreOffice \
%define lang %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define pkgname langpack-%{lang} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
\
%package %{pkgname} \
Summary: %{langname} language pack for %{project} \
Group: Applications/Productivity \
Requires: %{name}-core = %{version}-%{release} \
%{-a:Requires: autocorr-%{-a*}}%{!-a:%{-A:Requires: autocorr-%{lang}}} \
%{-f:Requires: font(:lang=%{-f*})}%{!-f:%{-F:Requires: font(:lang=%{lang})}} \
%{-h:Requires: hunspell-%{-h*}}%{!-h:%{-H:Requires: hunspell-%{lang}}} \
%{-m:Requires: mythes-%{-m*}}%{!-m:%{-M:Requires: mythes-%{lang}}} \
%{-y:Requires: hyphen-%{-y*}}%{!-y:%{-Y:Requires: hyphen-%{lang}}} \
%{-r:Requires: %{-r*}} \
%define obs openoffice.org-langpack \
%define obsv 1:3.3.1 \
%{-o:Obsoletes: %{obs}-%{-o*} < %{obsv}}%{!-o:%{-O:Obsoletes: %{obs}-%{lang} < %{obsv}}} \
\
%description %{pkgname} \
Provides additional %{langname} translations and resources for %{project}. \
\
%define filelist %{-s:-f %{-s*}.filelist}%{!-s:%{-S:-f %{lang}.filelist}} \
%files %{pkgname} %{filelist} \
%defattr(-,root,root,-) \
%*


# Defines an auto-correction subpackage.
#
# l: language code
# n: language name
# X  do not use default file match on %{_datadir}/autocorr/acor_%{lang}-*
#    in file list
#
# All remaining arguments are considered to be files and added to the file
# list.
%define autocorr(l:n:X) \
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
%defattr(-,root,root,-) \
%doc solver/%{OFFICEUPD}/unxlng*/bin/ure/LICENSE \
%dir %{_datadir}/autocorr \
%{!-X:%{_datadir}/autocorr/acor_%{lang}-*} \
%*


%if %{langpacks}

%langpack -l af -n Afrikaans -F -H -Y -A -o af_ZA -S
%langpack -l ar -n Arabic -F -H -O -S
%langpack -l as -n Assamese -F -H -Y -o as_IN -S
%langpack -l bg -n Bulgarian -F -H -Y -M -A -o bg_BG -S
%langpack -l bn -n Bengali -F -H -Y -O -S
%langpack -l ca -n Catalan -F -H -Y -M -o ca_ES -S
%langpack -l cs -n Czech -F -H -Y -M -A -o cs_CZ -S
%langpack -l cy -n Welsh -F -H -Y -o cy_GB -S
%langpack -l da -n Danish -F -H -Y -M -A -o da_DK -S
%langpack -l de -n German -F -H -Y -M -A -O -S
%langpack -l dz -n Dzongkha -F -O -S
%langpack -l el -n Greek -F -H -Y -M -o el_GR -S
%langpack -l en -n English -M -O
%langpack -l es -n Spanish -F -H -Y -M -A -O -S
%langpack -l et -n Estonian -F -H -Y -o et_EE -S
%langpack -l eu -n Basque -F -H -Y -A -o eu_ES -S
%langpack -l fi -n Finnish -F -r openoffice.org-voikko -A -o fi_FI -S
%langpack -l fr -n French -F -H -Y -M -A -O -S
%langpack -l ga -n Irish -F -H -Y -M -A -o ga_IE -S
%langpack -l gl -n Galician -F -H -Y -o gl_ES -S
%langpack -l gu -n Gujarati -F -H -Y -o gu_IN -S
%langpack -l he -n Hebrew -F -H -o he_IL -S
%langpack -l hi -n Hindi -F -H -Y -o hi_IN -S
%langpack -l hr -n Croatian -F -H -Y -A -o hr_HR -S
%langpack -l hu -n Hungarian -F -H -Y -M -A -o hu_HU -S
%langpack -l it -n Italian -F -H -Y -M -A -O -S
%langpack -l ja -n Japanese -F -A -o ja_JP -S
%langpack -l kn -n Kannada -F -H -Y -o kn_IN -S
%langpack -l ko -n Korean -F -H -A -o ko_KR -S
%{baseinstdir}/share/registry/korea.xcd

%langpack -l lt -n Lithuanian -F -H -Y -A -o lt_LT -S
%langpack -l mai -n Maithili -F -o mai_IN -S
%langpack -l ml -n Malayalam -F -H -Y -o ml_IN -S
%langpack -l mr -n Marathi -F -H -Y -o mr_IN -S
%langpack -l ms -n Malay -F -H -o ms_MY -S
%langpack -l nb -n Bokmal -F -H -Y -M -o nb_NO -S
%langpack -l nl -n Dutch -F -H -Y -M -A -O -S
%langpack -l nn -n Nynorsk -F -H -Y -M -o nn_NO -S
%define langpack_lang Southern Ndebele
%langpack -l nr -n %{langpack_lang} -F -H -o nr_ZA -S
%define langpack_lang Northern Sotho
%langpack -l nso -n %{langpack_lang} -F -H -o nso_ZA -s ns
%langpack -l or -n Oriya -F -H -Y -o or_IN -S
%langpack -l pa -n Punjabi -F -H -Y -O -s pa-IN
%langpack -l pl -n Polish -F -H -Y -M -A -o pl_PL -S
%define langpack_lang Brazilian Portuguese
%langpack -l pt-BR -n %{langpack_lang} -f pt -h pt -y pt -m pt -a pt -o pt_BR -S
%langpack -l pt-PT -n Portuguese -f pt -h pt -y pt -m pt -a pt -o pt_PT -s pt
%langpack -l ro -n Romanian -F -H -Y -M -O -S
%langpack -l ru -n Russian -F -H -Y -M -A -O -S
%langpack -l si -n Sinhalese -F -H -O -S
%langpack -l sk -n Slovak -F -H -Y -M -A -o sk_SK -S
%langpack -l sl -n Slovenian -F -H -Y -M -A -o sl_SI -S
%langpack -l sr -n Serbian -F -H -Y -A -O -S
%langpack -l ss -n Swati -F -H -o ss_ZA -S
%define langpack_lang Southern Sotho
%langpack -l st -n %{langpack_lang} -F -H -o st_ZA -S
%langpack -l sv -n Swedish -F -H -Y -M -A -O -S
%langpack -l ta -n Tamil -F -H -Y -o ta_IN -S
%langpack -l te -n Telugu -F -H -Y -o te_IN -S
%langpack -l th -n Thai -F -H -o th_TH -S
%langpack -l tn -n Tswana -F -H -o tn_ZA -S
%langpack -l tr -n Turkish -F -A -o tr_TR -S
%langpack -l ts -n Tsonga -F -H -o ts_ZA -S
%langpack -l uk -n Ukrainian -F -H -Y -M -O -S
%langpack -l ur -n Urdu -F -H -O -S
%langpack -l ve -n Venda -F -H -o ve_ZA -S
%langpack -l xh -n Xhosa -F -H -o xh_ZA -S
%define langpack_lang Simplified Chinese
%langpack -l zh-Hans -n %{langpack_lang} -f zh-cn -a zh -o zh_CN -s zh-CN
%define langpack_lang Traditional Chinese
%langpack -l zh-Hant -n %{langpack_lang} -f zh-tw -a zh -o zh_TW -s zh-TW
%langpack -l zu -n Zulu -F -H -Y -o zu_ZA -S
%undefine langpack_lang

%endif

%autocorr -l en -n English

%if %{langpacks}

%autocorr -l af -n Afrikaans
%autocorr -l bg -n Bulgarian
%autocorr -l cs -n Czech
%autocorr -l da -n Danish
%autocorr -l de -n German
%autocorr -l es -n Spanish
%autocorr -l eu -n Basque -X
%{_datadir}/autocorr/acor_eu.dat

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
%autocorr -l sr -n Serbian
%{_datadir}/autocorr/acor_sh-*

%autocorr -l sv -n Swedish
%autocorr -l tr -n Turkish
%autocorr -l vi -n Vietnamese
%autocorr -l zh -n Chinese

%endif

%prep
%setup -q -c -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11 -a 12 -a 13 -a 14 -a 15 -a 16 -a 17 -a 18 -a 33
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
%patch1  -p1 -b .ooo53397.prelinkoptimize.desktop.patch
%patch2  -p1
%patch3  -p1 -b .ooo86080.unopkg.bodge.patch
%patch4  -p1 -b .ooo88341.sc.verticalboxes.patch
%patch5  -p0 -b .gccXXXXX.solenv.javaregistration.patch
%patch6  -p1 -b .oooXXXXX.solenv.allowmissing.patch
%patch7  -p0 -b .ooo101274.opening-a-directory.patch
%patch8  -p0 -b .ooo102061.sc.cellanchoring.patch
%patch9  -p0 -b .ooo105784.vcl.sniffscriptforsubs.patch
%patch10 -p1 -b .ooo108637.sfx2.uisavedir.patch
%patch11 -p0 -b .ooo113273.desktop.resolvelinks.patch
%patch12 -p1 -b .turn-script-providers-into-extensions.patch
touch scripting/source/pyprov/delzip
touch scripting/util/provider/beanshell/delzip
touch scripting/util/provider/javascript/delzip

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

NDMAKES=1
NBUILDS=1

autoconf
%configure \
 --with-vendor="Red Hat, Inc." --with-num-cpus=$NBUILDS --with-max-jobs=$NDMAKES \
 --with-build-version="Ver: %{version}-%{release}" --with-unix-wrapper=%{name} \
 --disable-ldap --disable-epm --disable-mathmldtd \
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
if ! VERBOSE=true build --dlv_switch -link -P$NBUILDS --all -- -P$NDMAKES -s; then
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


%define install_bundled_extension(n:) \
%define extname %{-n:%{-n*}}%{!-n:%{error:No extension name given}} \
%define extdir $RPM_BUILD_ROOT/%{baseinstdir}/share/extensions \
%define solverbindir $SOLARVER/$INPATH/bin \
install -d -m 755 %{extdir}/%{extname} \
unzip -d %{extdir}/%{extname} %{solverbindir}/%{extname}.oxt


%install
rm -rf $RPM_BUILD_ROOT
source ./Linux*Env.Set.sh
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
mv ../unxlng*.pro/LibreOffice/installed/install/* $RPM_BUILD_ROOT/%{baseinstdir}
chmod -R +w $RPM_BUILD_ROOT/%{baseinstdir}
%if %{langpacks}
dmake ooolanguagepack
rm -rf ../unxlng*.pro/LibreOffice_languagepack/installed/install/log
for langpack in ../unxlng*.pro/LibreOffice_languagepack/installed/install/*; do
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
mv ../unxlng*.pro/LibreOffice_SDK/installed/install/*/sdk $RPM_BUILD_ROOT/%{sdkinstdir}
cd ../../

# install script providers
%install_bundled_extension -n script-provider-for-beanshell
%install_bundled_extension -n script-provider-for-javascript
%install_bundled_extension -n script-provider-for-python

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
ro      nohelp  western         si      nohelp  ctl     \
)

tar xzf %{SOURCE21}

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

cp -f %{SOURCE23} $RPM_BUILD_ROOT/%{_bindir}/unopkg
sed -i -e "s/LAUNCHER/unopkg/g" $RPM_BUILD_ROOT/%{_bindir}/unopkg
sed -i -e "s/BRAND/libreoffice/g" $RPM_BUILD_ROOT/%{_bindir}/unopkg
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/unopkg

cp -f %{SOURCE23} $RPM_BUILD_ROOT/%{_bindir}/libreoffice
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
%{basisinstdir}/share/fingerprint
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
%{basisinstdir}/share/xslt/odfflatxml
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
%{baseinstdir}/share/extensions/script-provider-for-beanshell

%files rhino
%defattr(-,root,root,-)
%{basisinstdir}/share/Scripts/javascript
%{baseinstdir}/share/extensions/script-provider-for-javascript

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
%{baseinstdir}/share/extensions/script-provider-for-python
%{basisinstdir}/share/registry/pyuno.xcd


%changelog
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

* Sun Oct 30 2010 Caolán McNamara <caolanm@redhat.com> 3.2.99.2-4
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
