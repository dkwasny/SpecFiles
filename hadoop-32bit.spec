Name:		hadoop
Version:	2.5.0
Release:	1%{?dist}
Summary:	Distributed storage and processing framework

Group:		Applications/Databases
License:	Apache 2.0
URL:		hadoop.apache.org
Source0:	hadoop-2.5.0.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	java-1.7.0-openjdk

ExclusiveArch:	i386
Exclusiveos:	linux

%description
Hadoop compiled for 32-bit Linux.

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

%changelog

