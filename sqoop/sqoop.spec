Name:		sqoop
Version:	1.4.6
Release:	1%{?dist}
Summary:	A tool designed for efficiently transferring bulk data between Apache Hadoop 1.0 and structured datastores such as relational databases.

Group:		Applications/Databases
License:	Apache 2.0
URL:		http://sqoop.apache.org/
Source0:	sqoop-1.4.6.tar.gz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	java-1.7.0-openjdk

BuildArch:	noarch
Exclusiveos:	linux

%description
RPM installer for precompiled Sqoop (Hadoop 2.0) binaries.

%prep
%setup -q


%build
echo "Nothing to build..."


%install
rm -rf %{buildroot}
mkdir %{buildroot}

mkdir -p %{buildroot}/opt/sqoop
mv * %{buildroot}/opt/sqoop

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/opt/sqoop

%changelog

