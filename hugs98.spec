%define hugs_ver Mar2005-patched

Name:		hugs98
Version:	2005.03
Release:	4%{?dist}
Summary:	Haskell Interpreter

Group:		Development/Languages
License:	BSD
URL:		http://www.haskell.org/hugs
Source0:	http://cvs.haskell.org/Hugs/downloads/Mar2005/%{name}-%{hugs_ver}.tar.gz
Patch0:		openal-1.0_1.2.patch
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
BuildRequires:	openal-devel

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
%patch0 -p1


%build
%configure --with-pthreads
touch src/stamp-h.in
make %{_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install_all_but_docs
make -C docs DESTDIR=$RPM_BUILD_ROOT install_man

find $RPM_BUILD_ROOT -name '*.so' -exec chmod 0755 '{}' ';'

mv $RPM_BUILD_ROOT%{_libdir}/hugs/demos installed-demos
rm installed-demos/Makefile.in


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


%changelog
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
