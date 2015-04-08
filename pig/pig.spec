Name:		pig
Version:	0.14.0
Release:	1%{?dist}
Summary:	A platform for analyzing large data sets.

Group:		Applications/Databases
License:	Apache 2.0
URL:		pig.apache.org
Source0:	pig-0.14.0.tar.gz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	java-1.7.0-openjdk

BuildArch:	noarch
Exclusiveos:	linux

%description
RPM installer for precompiled Pig binaries.

%prep
%setup -q


%build
echo "Nothing to build..."


%install
rm -rf %{buildroot}
mkdir %{buildroot}

mkdir -p %{buildroot}/opt/pig
mv * %{buildroot}/opt/pig

mkdir -p %{buildroot}/usr/local/bin
ln -s /opt/pig/bin/pig %{buildroot}/usr/local/bin

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/opt/pig
/usr/local/bin/pig

%changelog

