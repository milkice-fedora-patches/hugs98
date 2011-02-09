%define hugs_ver plus-Sep2006

Name:		hugs98
Version:	2006.09
Release:	10%{?dist}
Summary:	Haskell Interpreter

Group:		Development/Languages
License:	BSD
URL:		http://www.haskell.org/hugs
Source0:	http://cvs.haskell.org/Hugs/downloads/2006-09/%{name}-%{hugs_ver}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	docbook-utils
BuildRequires:	freeglut-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
BuildRequires:	libICE-devel
BuildRequires:	libSM-devel
BuildRequires:	libX11-devel
BuildRequires:	libXi-devel
BuildRequires:	libXmu-devel
BuildRequires:	libXt-devel
BuildRequires:	readline-devel
BuildRequires:	xorg-x11-proto-devel
BuildRequires:	openal-soft-devel
BuildRequires:	freealut-devel
BuildRequires:	prelink

%description
Hugs 98 is a functional programming system based on Haskell 98, the de
facto standard for non-strict functional programming languages. Hugs
98 provides an almost complete implementation of Haskell 98.


%package openal
Summary:	OpenAL package for Hugs98
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description openal
OpenAL package for Hugs98.


%package alut
Summary:	ALUT package for Hugs98
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-openal = %{version}-%{release}

%description alut
ALUT package for Hugs98.


%package x11
Summary:	X11 package for Hugs98
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description x11
X11 package for Hugs98.


%package opengl
Summary:	OpenGL package for Hugs98
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description opengl
OpenGL package for Hugs98.


%package glut
Summary:	GLUT package for Hugs98
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-opengl = %{version}-%{release}

%description glut
GLUT package for Hugs98.


%package hgl
Summary:	Haskell Graphics Library for Hugs98
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-x11 = %{version}-%{release}

%description hgl
Haskell Graphics Library for Hugs98.


%package demos
Summary:	Demo files for Hugs98
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-glut = %{version}-%{release}
Requires:	%{name}-hgl = %{version}-%{release}

%description demos
Demo files for Hugs98.


%prep
%setup -q -n %{name}-%{hugs_ver}
# this is to avoid network lookup of the DTD
sed -i 's|\"http://www.oasis-open.org.*\"||' docs/users_guide/users_guide.xml


%build
%configure --with-pthreads --enable-char-encoding=locale
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install_all_but_docs
make -C docs DESTDIR=$RPM_BUILD_ROOT install_man

execstack -s $RPM_BUILD_ROOT%{_bindir}/{hugs,runhugs,ffihugs}

find $RPM_BUILD_ROOT -name '*.so' -exec chmod 0755 '{}' ';'

mv $RPM_BUILD_ROOT%{_libdir}/hugs/demos installed-demos
rm installed-demos/Makefile.in

mv $RPM_BUILD_ROOT%{_datadir}/hsc2hs-*/* $RPM_BUILD_ROOT%{_libdir}/hugs/programs/hsc2hs

sed -i "s|^bindir.*|bindir=\"%{_bindir}\"|
        s|^libdir.*|libdir=\"%{_libdir}/hugs/programs/hsc2hs|
        s|^datadir.*|datadir=\"%{_libdir}/hugs/programs/hsc2hs\"|" \
    $RPM_BUILD_ROOT%{_libdir}/hugs/programs/hsc2hs/Paths_hsc2hs.hs



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc License
%doc Readme
%doc Credits
%doc docs/ffi-notes.txt
%doc docs/server.html
%doc docs/libraries-notes.txt
%doc docs/users_guide/users_guide
%{_bindir}/*
%{_libdir}/hugs
%exclude %{_libdir}/hugs/packages/OpenAL
%exclude %{_libdir}/hugs/packages/ALUT
%exclude %{_libdir}/hugs/packages/X11
%exclude %{_libdir}/hugs/packages/OpenGL
%exclude %{_libdir}/hugs/packages/GLUT
%exclude %{_libdir}/hugs/packages/HGL
%{_mandir}/man*/*


%files demos
%defattr(-,root,root,-)
%doc installed-demos/*


%files openal
%defattr(-,root,root,-)
%{_libdir}/hugs/packages/OpenAL


%files alut
%defattr(-,root,root,-)
%{_libdir}/hugs/packages/ALUT


%files x11
%defattr(-,root,root,-)
%{_libdir}/hugs/packages/X11


%files opengl
%defattr(-,root,root,-)
%{_libdir}/hugs/packages/OpenGL


%files glut
%defattr(-,root,root,-)
%{_libdir}/hugs/packages/GLUT


%files hgl
%defattr(-,root,root,-)
%{_libdir}/hugs/packages/HGL


%post
update-alternatives --install %{_bindir}/runhaskell runhaskell \
  %{_bindir}/runhugs 100
update-alternatives --install %{_bindir}/hsc2hs hsc2hs \
  %{_bindir}/hsc2hs-hugs 100
update-alternatives --install %{_bindir}/cpphs cpphs \
  %{_bindir}/cpphs-hugs 100


%preun
if [ "$1" = 0 ]; then
  update-alternatives --remove runhaskell %{_bindir}/runhugs
  update-alternatives --remove hsc2hs     %{_bindir}/hsc2hs-hugs
  update-alternatives --remove cpphs      %{_bindir}/cpphs-hugs
fi


%changelog
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2006.09-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 19 2010 Jens Petersen <petersen@redhat.com> - 2006.09-9
- rebuild

* Sun Aug 16 2009 Gerard Milmeister <gemi@bluewin.ch> - 2006.09-8
- rebuild against openal-soft

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2006.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul  3 2009 Gerard Milmeister <gemi@bluewin.ch> - 2006.09-6
- added alternatives setup for runhaskell and friends

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2006.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2006.09-4
- Autorebuild for GCC 4.3

* Sun Feb 11 2007 Gerard Milmeister <gemi@bluewin.ch> - 2006.09-2
- rebuild to use ncurses

* Mon Oct 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 2006.09-1
- new version Sep2006

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 2006.05-6
- Rebuild for FE6

* Fri Jun 23 2006 Gerard Milmeister <gemi@bluewin.ch> - 2006.05-5
- switch char encoding from utf-8 to locale

* Wed Jun 21 2006 Gerard Milmeister <gemi@bluewin.ch> - 2006.05-4
- added execstack for the hugs binary

* Tue Jun 20 2006 Gerard Milmeister <gemi@bluewin.ch> - 2006.05-1
- new version 2006.05 with libraries

* Mon Apr 24 2006 Gerard Milmeister <gemi@bluewin.ch> - 2005.03-3
- added patch provided by Jens Petersen to build OpenAL package

* Tue Apr 18 2006 Gerard Milmeister <gemi@bluewin.ch> - 2005.03-1
- changed version numbering scheme
- split off demos package
- split of some packages
- do not build openal support (compile errors)
- enable pthreads

* Wed Mar 30 2005 Gerard Milmeister <gemi@bluewin.ch> - 200503-1
- New Version Mar2005

* Sun Feb 13 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:200311-1
- Changed version scheme

* Mon Jan  5 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.0-0.fdr.1.200311
- New Version Nov2003

* Mon Oct 20 2003 Gerard Milmeister <gemi@bluewin.ch> - Nov2002-0.fdr.1
- First Fedora release
