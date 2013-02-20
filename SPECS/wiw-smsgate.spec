%global github_user thesharp
%global github_repo wiw-smsgate
%global github_tag 0.1

Name:           python-%{github-repo}
Version:        %{github-tag}
Release:        1.vortex%{?dist}
Summary:        In-house Python utility to send text messages
Vendor:         Vortex RPM

Group:          Applications/Internet
License:        MIT
URL:            http://github.com/%{github-user}/%{github-repo}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel, python-pip, curl

%description
This is our in-house utility to send text messages (SMS) from Nagios using our
own XML-RPC gateway. This project is here just because I was too lazy to setup
an internal git repository. Obviously, this utility is only usable for us,
sorry for that.

%prep
curl -O https://github.com/%{github_user}/%{github_repo}/archive/%{github_tag}.tar.gz
%setup -q -n %{github_tag}.tar.gz

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc PKG-INFO LICENSE README.md
%attr(755,root,root) %{_bindir}/wiw-smsgate
%config(noreplace) %{_sysconfdir}/wiw-smsgate.conf

%changelog
* Wed Feb 20 2013 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.1-1.vortex
- Initial packaging.

