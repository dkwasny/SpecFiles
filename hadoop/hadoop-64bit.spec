Name:		hadoop
Version:	2.5.1
Release:	1%{?dist}
Summary:	Distributed storage and processing framework

Group:		Applications/Databases
License:	Apache 2.0
URL:		hadoop.apache.org
Source0:	hadoop-2.5.1.tar.gz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	java-1.7.0-openjdk
BuildRequires:	systemd

ExclusiveArch:	x86_64
Exclusiveos:	linux

%description
RPM installer for precompiled hadoop binaries.

%prep
%setup -q


%build
echo "Nothing to build..."


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_unitdir}
mv ./unit-files/* %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/usr/local
mv ./{bin,include,lib,libexec,sbin,share,etc} %{buildroot}/usr/local

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/usr/local/bin
/usr/local/include
/usr/local/lib
/usr/local/libexec
/usr/local/sbin
/usr/local/share
%{_unitdir}
%config /usr/local/etc

%pre
getent passwd hdfs > /dev/null || \
	useradd -r -s /sbin/nologin -c "Service account for Hadoop" hdfs
getent passwd yarn > /dev/null || \
	useradd -r -s /sbin/nologin -c "Service account for YARN" yarn

%post
%systemd_post hdfs-namenode.service
%systemd_post hdfs-datanode.service
%systemd_post yarn-resourcemanager.service
%systemd_post yarn-nodemanager.service
%systemd_post yarn-mrhistoryserver.service

%preun
%systemd_preun hdfs-namenode.service
%systemd_preun hdfs-datanode.service
%systemd_preun yarn-resourcemanager.service
%systemd_preun yarn-nodemanager.service
%systemd_preun yarn-mrhistoryserver.service

%postun
%systemd_postun_with_restart hdfs-namenode.service
%systemd_postun_with_restart hdfs-datanode.service
%systemd_postun_with_restart yarn-resourcemanager.service
%systemd_postun_with_restart yarn-nodemanager.service
%systemd_postun_with_restart yarn-mrhistoryserver.service

%changelog

