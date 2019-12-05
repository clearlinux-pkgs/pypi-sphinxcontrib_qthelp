#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : sphinxcontrib-qthelp
Version  : 1.0.2
Release  : 6
URL      : https://files.pythonhosted.org/packages/0c/f0/690cd10603e3ea8d184b2fffde1d965dd337b87a1d5f7625d0f6791094f4/sphinxcontrib-qthelp-1.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/0c/f0/690cd10603e3ea8d184b2fffde1d965dd337b87a1d5f7625d0f6791094f4/sphinxcontrib-qthelp-1.0.2.tar.gz
Source99 : https://files.pythonhosted.org/packages/0c/f0/690cd10603e3ea8d184b2fffde1d965dd337b87a1d5f7625d0f6791094f4/sphinxcontrib-qthelp-1.0.2.tar.gz.asc
Summary  : No summary provided
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-qthelp-license = %{version}-%{release}
Requires: sphinxcontrib-qthelp-python = %{version}-%{release}
Requires: sphinxcontrib-qthelp-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
====================
sphinxcontrib-qthelp
====================
sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp document.

%package license
Summary: license components for the sphinxcontrib-qthelp package.
Group: Default

%description license
license components for the sphinxcontrib-qthelp package.


%package python
Summary: python components for the sphinxcontrib-qthelp package.
Group: Default
Requires: sphinxcontrib-qthelp-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-qthelp package.


%package python3
Summary: python3 components for the sphinxcontrib-qthelp package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sphinxcontrib-qthelp package.


%prep
%setup -q -n sphinxcontrib-qthelp-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554254528
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-qthelp
cp LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-qthelp/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-qthelp/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
