Summary:	XGraph with animation
Summary(pl):	XGraph z obs³ug± animacji
Name:		xgraph
Version:	11.4
Release:	1
License:	BSD
Group:		Applications/Math
URL:		http://jean-luc.ncsa.uiuc.edu/Codes/xgraph/
Source0:	http://jean-luc.ncsa.uiuc.edu/Codes/xgraph/xgraph_bin/%{name}_anim.tar.gz
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-header.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man

%description
XGraph with animation is a modification of the popular XGraph plotting
program written by David Harrison at UC Berkeley. It does animation of
data sets, supports zooming regions with a mouse and taking numerical
derivatives.

%description -l pl
"XGraph z animacj±" jest modyfikacj± popularnego programu do robienia
wykresów XGraph, napisanego przez Davida Harrisona z Uniwersytetu w
Berkeley. Mo¿na w nim robiæ animacje zestawów danych, powiêkszaæ
kawa³ki wykresu myszk± i numerycznie ró¿niczkowaæ dane na wykresie.

%prep
%setup -q -n xgraph
%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_examplesdir}/xgraph
install xgraph $RPM_BUILD_ROOT%{_bindir}/xgraph
install xgraph.man $RPM_BUILD_ROOT%{_mandir}/man1/xgraph.1
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/xgraph/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/*
%{_mandir}/man1/*
%dir %{_examplesdir}/xgraph
%{_examplesdir}/xgraph/*
%doc README.NEWFEATURES
