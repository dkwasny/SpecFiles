Name:		solr
Version:	5.0.0
Release:	1%{?dist}
Summary:	Solr is the popular, blazing fast open source enterprise search platform from the Apache Lucene project.

Group:		Applications/Databases
License:	Apache 2.0
URL:		http://lucene.apache.org/solr/
Source0:	solr-5.0.0.tar.gz

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
mkdir %{buildroot}

mkdir -p %{buildroot}/%{_unitdir}
mv unit-files/* %{buildroot}/%{_unitdir}
rmdir unit-files

mkdir -p %{buildroot}/opt/solr
mv * %{buildroot}/opt/solr

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_unitdir}
# Solr likes to write to itself by default
# so I have to chown to the solr user.
%attr(-,solr,solr) /opt/solr

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

