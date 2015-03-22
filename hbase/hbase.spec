Name:		hbase
Version:	1.0.0
Release:	1%{?dist}
Summary:	Distributed key-value store on top of Hadoop

Group:		Applications/Databases
License:	Apache 2.0
URL:		hbase.apache.org
Source0:	hbase-1.0.0.tar.gz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	java-1.7.0-openjdk
Requires:	hadoop
BuildRequires:	systemd

ExclusiveArch:	x86_64
Exclusiveos:	linux

%description
RPM installer for precompiled HBase binaries.

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

mkdir -p %{buildroot}/opt/hbase
mv * %{buildroot}/opt/hbase

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/opt/hbase
%{_unitdir}

%pre
getent passwd hbase > /dev/null || \
	useradd -r -s /sbin/nologin -c "Service account for HBase" hbase

%post
%systemd_post hbase-master.service
%systemd_post hbase-regionserver.service

%preun
%systemd_preun hbase-master.service
%systemd_preun hbase-regionserver.service

%postun
%systemd_postun_with_restart hbase-master.service
%systemd_postun_with_restart hbase-regionserver.service

%changelog

