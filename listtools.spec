%define lib_major                       0
%define lib_name                        %{mklibname p2p %{lib_major}}
%define lib_name_devel                  %{mklibname p2p -d}
%define lib_name_static_devel           %{mklibname p2p -d -s}

Name:           listtools
Version:        1.0
Release:        %mkrel 16
Epoch:          0
Summary:        P2P List Library
URL:            http://peerguardian.sourceforge.net/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-unix.patch
License:        BSD
Group:          System/Libraries
BuildRequires:  doxygen
BuildRequires:  boost-devel
BuildRequires:  mysql-devel
BuildRequires:  tetex
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
P2P List Library.

%package -n %{lib_name}
Summary:        Main library for the libp2p library
Group:          System/Libraries

%description -n %{lib_name}
This package contains the libraries needed to run programs dynamically
linked with the libp2p library.

%package -n %{lib_name_devel}
Group:          Development/C++
Summary:        Shared libraries and header files for the libp2p library
Provides:       p2p-devel = %{epoch}:%{version}-%{release}
Obsoletes:	%{mklibname p2p 0 -d}
Requires:       %{lib_name} = %{epoch}:%{version}-%{release}

%description -n %{lib_name_devel}
The %{name} package contains the shared libraries and header files
needed for developing libp2p applications.

%package -n %{lib_name_static_devel}
Group:          Development/C++
Summary:        Static libraries for the libp2p library
Provides:       p2p-static-devel = %{epoch}:%{version}-%{release}
Obsoletes:	%{mklibname p2p 0 -s -d}
Requires:       %{lib_name_devel} = %{epoch}:%{version}-%{release}

%description -n %{lib_name_static_devel}
The %{name} package contains the static libraries needed for developing
libp2p applications.

%prep
%setup -q -n %{name}
%patch0 -p1
%{_bindir}/autoreconf -f --verbose -i

%build
%{configure2_5x}
%{make}
%{make} doxygen-doc

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%check
%{make} check

%clean
%{__rm} -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/dumpp2p
%attr(0755,root,root) %{_bindir}/filterp2p
%attr(0755,root,root) %{_bindir}/genallow
%attr(0755,root,root) %{_bindir}/mergep2p

%files -n %{lib_name}
%defattr(0644,root,root,0755)
%doc p2b.txt
%attr(0755,root,root) %{_libdir}/libp2p.so.*

%files -n %{lib_name_devel}
%defattr(0644,root,root,0755)
%doc Docs/html
%dir %{_includedir}/p2p
%{_includedir}/p2p/*.hpp
%attr(0755,root,root) %{_libdir}/libp2p.so
%attr(0755,root,root) %{_libdir}/libp2p.la
%{_libdir}/pkgconfig/libp2p.pc

%files -n %{lib_name_static_devel}
%defattr(0644,root,root,0755)
%{_libdir}/libp2p.a
