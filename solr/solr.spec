Name:		solr
Version:	4.10.0
Release:	1%{?dist}
Summary:	Solr is the popular, blazing fast open source enterprise search platform from the Apache Lucene project.

Group:		Applications/Databases
License:	Apache 2.0
URL:		http://lucene.apache.org/solr/
Source0:	solr-4.10.0.tar.gz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	java-1.7.0-openjdk
BuildRequires:	systemd

BuildArch:	noarch

%description
RPM installer for precompiled solr binaries.

%prep
%setup -q


%build
echo "Nothing to build..."


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_unitdir}
mv ./unit-files/* %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/usr/local
mv ./{bin,etc} %{buildroot}/usr/local
mkdir -p %{buildroot}/var/local/
mv ./vardir %{buildroot}/var/local/solr

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/usr/local/bin
%{_unitdir}
%config /usr/local/etc
%attr(-,solr,solr) /var/local/solr

%pre
getent passwd solr > /dev/null || \
	useradd -r -s /sbin/nologin -c "Service account for Solr" solr

%post
%systemd_post solr.service

%preun
%systemd_preun solr.service

%postun
%systemd_postun_with_restart solr.service

%changelog

