%if 0%{?fedora} > 12
%global with_python3 1
%{!?python3_sitearch: %define python_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%else
%{!?python_sitearch: %define python_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%endif

%global alphatag b1
Name: pyusb
Version: 1.0.0
Release: 0.11.%{alphatag}%{?dist}
Summary: Python bindings for libusb
Group: Development/Languages
License: BSD
URL: http://pyusb.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}%{alphatag}.zip
BuildRequires: python2-devel
%if 0%{?with_python3}
BuildRequires:  python3-devel
%endif # if with_python3
BuildRequires: libusb-devel
BuildArch: noarch

%description
PyUSB provides easy USB access to python. The module contains classes and
methods to support most USB operations.

%if 0%{?with_python3}
%package -n python3-pyusb
Summary:        Python 3 bindings for libusb
Group:          Development/Languages

%description -n python3-pyusb
PyUSB provides easy USB access to python. The module contains classes and
methods to support most USB operations.
%endif # with_python3

%prep
%setup -q -n %{name}-%{version}%{alphatag}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build
sed -i -e 's/\r//g' README.rst

%if 0%{?with_python3}
pushd %{py3dir}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd
%endif # with_python3


%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%endif

%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc README.rst LICENSE
%{python_sitelib}/*

%if 0%{?with_python3}
%files -n python3-pyusb
%doc README.rst LICENSE
%{python3_sitelib}/*
%endif # with_python3

%changelog
* Thu Sep 25 2014 Petr Vobornik <pvoborni@redhat.com> - 1.0.0-0.11.b1
- Fixed Source0 in spec file.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.10.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.0-0.9.b1
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Nov 11 2013 Jon Ciesla <limburgher@gmail.com> - 1.0.0-0.8.b1
- Latest upstream.
- Add python3 support, spec cleanup, BZ 1022851.
- Fixed changelog.

* Fri Sep 13 2013 Jon Ciesla <limburgher@gmail.com> - 1.0.0-0.7.a3
- Latest upstream.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.6.a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.5.a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.4.a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 23 2012 Tim Waugh <twaugh@redhat.com> - 1.0.0-0.3.a2
- 1.0.0-a2.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.2.a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 30 2011 Tim Waugh <twaugh@redhat.com> - 1.0.0-0.1.a1
- 1.0.0-a1 (bug #586950).

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.4.1-3
- Rebuild for Python 2.6

* Mon Jun 16 2008 Jeremy Katz <katzj@redhat.com> - 0.4.1-2
- Fix end-of-line in README

* Mon Jun 16 2008 Jeremy Katz <katzj@redhat.com> - 0.4.1-1
- Initial packaging

