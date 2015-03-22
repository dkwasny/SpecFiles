Name:		zookeeper
Version:	3.4.6
Release:	1%{?dist}
Summary:	ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services.

Group:		Applications/Databases
License:	Apache 2.0
URL:		http://zookeeper.apache.org/
Source0:	zookeeper-3.4.6.tar.gz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	java-1.7.0-openjdk
BuildRequires:	systemd

BuildArch:	noarch

%description
RPM installer for precompiled zookeeper binaries.

%prep
%setup -q


%build
echo "Nothing to build..."


%install
rm -rf %{buildroot}
mkdir %{buildroot}

# Remove these directories due to a broken python file
rm -r contrib
rm -r src

mkdir -p %{buildroot}/%{_unitdir}
mv unit-files/* %{buildroot}/%{_unitdir}
rmdir unit-files

mkdir -p %{buildroot}/opt/zookeeper
mv * %{buildroot}/opt/zookeeper

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/opt/zookeeper
%{_unitdir}

%pre
getent passwd zookeeper > /dev/null || \
	useradd -r -s /sbin/nologin -c "Service account for Zookeeper" zookeeper

%post
%systemd_post zookeeper.service

%preun
%systemd_preun zookeeper.service

%postun
%systemd_postun_with_restart zookeeper.service

%changelog

