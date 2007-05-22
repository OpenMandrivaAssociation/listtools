%define lib_major                       0
%define lib_name_orig                   %mklibname p2p
%define lib_name_orig_devel             %mklibname p2p -d
%define lib_name_orig_static_devel      %mklibname p2p -d -s
%define lib_name                        %mklibname p2p %{lib_major}
%define lib_name_devel                  %mklibname p2p %{lib_major} -d
%define lib_name_static_devel           %mklibname p2p %{lib_major} -d -s

Name:           listtools
Version:        1.0
Release:        %mkrel 1
Epoch:          0
Summary:        C P2P List Library
URL:            http://peerguardian.sourceforge.net/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-unix.patch
License:        BSD-style
Group:          System/Libraries
BuildRequires:  doxygen
BuildRequires:  libboost-devel
BuildRequires:  libmysql-devel
Buildroot:      %{_tmppath}/%{name}-%{epoch}:%{version}-%{release}-root

%description
C P2P List Library.

%package -n %{lib_name}
Summary:        Main library for the libp2p library
Group:          System/Libraries

%description -n %{lib_name}
This package contains the libraries needed to run programs dynamically
linked with the libp2p library.

%package -n %{lib_name_devel}
Group:          Development/C++
Summary:        Shared libraries and header files for the libp2p library
Provides:       %{name}-devel = %{epoch}:%{version}-%{release}
Provides:       %{lib_name_orig_devel} = %{epoch}:%{version}-%{release}
Requires:       %{lib_name} = %{epoch}:%{version}-%{release}

%description -n %{lib_name_devel}
The %{name} package contains the shared libraries and header files
needed for developing libp2p applications.

%package -n %{lib_name_static_devel}
Group:          Development/C++
Summary:        Static libraries for the libp2p library
Provides:       %{lib_name_orig_static_devel} = %{epoch}:%{version}-%{release}
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

%install
%{__rm} -rf %{buildroot}
%{makeinstall}

%check
%{make} check

%clean
%{__rm} -rf %{buildroot}

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

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
%dir %{_includedir}/p2p
%{_includedir}/p2p/*.hpp
%attr(0755,root,root) %{_libdir}/libp2p.so
%attr(0755,root,root) %{_libdir}/libp2p.la
%{_libdir}/pkgconfig/libp2p.pc

%files -n %{lib_name_static_devel}
%defattr(0644,root,root,0755)
%{_libdir}/libp2p.a
