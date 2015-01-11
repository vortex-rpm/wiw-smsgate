%global github_user thesharp
%global github_repo wiw-smsgate
%global github_tag 1.1

%global __pip pip

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%if 0{?rhel} == 6
%global _py_ver 2.6
%else
%global _py_ver 2.7
%endif

Name:           python-%{github_repo}
Version:        %{github_tag}
Release:        2.vortex%{?dist}
Summary:        In-house Python utility to send text messages
Vendor:         Vortex RPM

Group:          Applications/Internet
License:        MIT
URL:            http://github.com/%{github_user}/%{github_repo}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel

%description
This is our in-house utility to send text messages (SMS) from Nagios using our
own XML-RPC gateway. This project is here just because I was too lazy to setup
an internal git repository. Obviously, this utility is only usable for us,
sorry for that.

%prep
curl -L -o %{github_repo}-%{github_tag}.tar.gz https://github.com/%{github_user}/%{github_repo}/archive/%{github_tag}.tar.gz
tar xf %{github_repo}-%{github_tag}.tar.gz
cd %{github_repo}-%{github_tag}

%install
cd %{github_repo}-%{github_tag}
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root %{buildroot}
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}%{_libdir}/python%{_py_ver}/site-packages
mv %{buildroot}/usr/etc/wiw-smsgate.conf %{buildroot}/etc/wiw-smsgate.conf
mv %{buildroot}/usr/lib/python%{_py_ver}/site-packages/smsgate.py %{buildroot}%{_libdir}/python%{_py_ver}/site-packages/
rm -rf %{buildroot}/usr/lib

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{github_repo}-%{github_tag}/LICENSE %{github_repo}-%{github_tag}/README.md
%attr(755,root,root) %{_bindir}/wiw-smsgate
%attr(644,root,root) %{_libdir}/python%{_py_ver}/site-packages/smsgate.py
%config(noreplace) %{_sysconfdir}/wiw-smsgate.conf

%changelog
* Mon Jan 12 2014 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 1.1-3.vortex
- Let's try this ugly hack to build for both EL6 and EL7.

* Fri Jun 28 2013 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 1.1-2.vortex
- Blah.

* Fri Jun 28 2013 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 1.1-1.vortex
- Update to 1.1.

* Wed Feb 20 2013 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.3-1.vortex
- Well, it should be like that from the start.

* Wed Feb 20 2013 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.2-1.vortex
- Improved testsuite.

* Wed Feb 20 2013 Ilya A. Otyutskiy <sharp@thesharp.ru> - 0.1-1.vortex
- Initial packaging.

