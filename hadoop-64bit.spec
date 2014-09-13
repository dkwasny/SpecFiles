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
mkdir -p %{buildroot}/usr/local
cp -r . %{buildroot}/usr/local

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/usr/local/*

%pre
getent passwd hdfs > /dev/null || \
	useradd -r -s /sbin/nologin -c "Service account for Hadoop" hdfs
getent passwd yarn > /dev/null || \
	useradd -r -s /sbin/nologin -c "Service account for YARN" yarn

%changelog

