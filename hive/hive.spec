Name:		hive
Version:	1.2.0
Release:	1%{?dist}
Summary:	A SQL-like interface that sits on top of Hadoop

Group:		Applications/Databases
License:	Apache 2.0
URL:		http://hive.apache.org/
Source0:	hive-1.2.0.tar.gz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	java-1.7.0-openjdk
Requires:	hadoop
BuildRequires:	systemd

BuildArch:	noarch
Exclusiveos:	linux

%description
RPM installer for precompiled Hive binaries.

%prep
%setup -q


%build
echo "Nothing to build..."


%install
rm -rf %{buildroot}
mkdir %{buildroot}

mkdir -p %{buildroot}/%{_unitdir}
mv unit-files/* %{buildroot}/%{_unitdir}
rmdir unit-files

mkdir -p %{buildroot}/opt/hive
mv * %{buildroot}/opt/hive

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/opt/hive
%{_unitdir}

%pre
getent passwd hive > /dev/null || \
	useradd -r -s /sbin/nologin -c "Service account for Hive" hive

%post
%systemd_post hive-hcatalog.service
%systemd_post hive-server.service
%systemd_post hive-webhcat.service

%preun
%systemd_preun hive-hcatalog.service
%systemd_preun hive-server.service
%systemd_preun hive-webhcat.service

%postun
%systemd_postun_with_restart hive-hcatalog.service
%systemd_postun_with_restart hive-server.service
%systemd_postun_with_restart hive-webhcat.service

%changelog

