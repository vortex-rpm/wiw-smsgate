%global github_user thesharp
%global github_repo wiw-smsgate
%global github_tag 0.2

%global __pip pip

Name:           python-%{github_repo}
Version:        %{github_tag}
Release:        1.vortex%{?dist}
Summary:        In-house Python utility to send text messages
Vendor:         Vortex RPM

Group:          Applications/Internet
License:        MIT
URL:            http://github.com/%{github_user}/%{github_repo}
Source:         dummy
NoSource:       0
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel, python-pip, python-nose, python-virtualenv

%description
This is our in-house utility to send text messages (SMS) from Nagios using our
own XML-RPC gateway. This project is here just because I was too lazy to setup
an internal git repository. Obviously, this utility is only usable for us,
sorry for that.

%prep
tar xf %{github_repo}-%{github_tag}
cd %{github_repo}-%{github_tag}

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%check
virtualenv env
source env/bin/activate
%{__pip} install .
nosetests
deactivate
rm -rf env

%files
%defattr(-,root,root,-)
%doc PKG-INFO LICENSE README.md
%attr(755,root,root) %{_bindir}/wiw-smsgate
%config(noreplace) %{_sysconfdir}/wiw-smsgate.conf

%changelog
* Wed Feb 20 2013 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.2-1.vortex
- Improved testsuite.

* Wed Feb 20 2013 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.1-1.vortex
- Initial packaging.

