Name:		flume
Version:	1.6.0
Release:	1%{?dist}
Summary:	A distributed, reliable, and available system for efficiently collecting, aggregating and moving large amounts of log data from many different sources to a centralized data store.

Group:		Applications/Databases
License:	Apache 2.0
URL:		flume.apache.org
Source0:	flume-1.6.0.tar.gz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	java-1.7.0-openjdk

BuildArch:	noarch
Exclusiveos:	linux

%description
RPM installer for precompiled Flume binaries.

%prep
%setup -q


%build
echo "Nothing to build..."


%install
rm -rf %{buildroot}
mkdir %{buildroot}

mkdir -p %{buildroot}/opt/flume
mv * %{buildroot}/opt/flume

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/opt/flume

%changelog

