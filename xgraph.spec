Summary:	XGraph with animation
Summary(pl):	XGraph z obs³ug± animacji
Name:		xgraph
Version:	12.1
Release:	2
License:	BSD
Group:		Applications/Math
URL:		http://www.isi.edu/nsnam/xgraph/
Source0:	http://www.isi.edu/nsnam/dist/%{name}-%{version}.tar.gz
# Source0-md5:	c4cbfb3291a607dd274e7fb161b9056a
Patch0:		%{name}-manlocation.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%setup -q
%patch0
mv %{name}.man %{name}.1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/xgraph

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/xgraph

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_examplesdir}/xgraph
