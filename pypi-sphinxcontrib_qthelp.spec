#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : pypi-sphinxcontrib_qthelp
Version  : 1.0.3
Release  : 34
URL      : https://files.pythonhosted.org/packages/b1/8e/c4846e59f38a5f2b4a0e3b27af38f2fcf904d4bfd82095bf92de0b114ebd/sphinxcontrib-qthelp-1.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/b1/8e/c4846e59f38a5f2b4a0e3b27af38f2fcf904d4bfd82095bf92de0b114ebd/sphinxcontrib-qthelp-1.0.3.tar.gz
Source1  : https://files.pythonhosted.org/packages/b1/8e/c4846e59f38a5f2b4a0e3b27af38f2fcf904d4bfd82095bf92de0b114ebd/sphinxcontrib-qthelp-1.0.3.tar.gz.asc
Summary  : sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp document.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-sphinxcontrib_qthelp-license = %{version}-%{release}
Requires: pypi-sphinxcontrib_qthelp-python = %{version}-%{release}
Requires: pypi-sphinxcontrib_qthelp-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp document.

%package license
Summary: license components for the pypi-sphinxcontrib_qthelp package.
Group: Default

%description license
license components for the pypi-sphinxcontrib_qthelp package.


%package python
Summary: python components for the pypi-sphinxcontrib_qthelp package.
Group: Default
Requires: pypi-sphinxcontrib_qthelp-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinxcontrib_qthelp package.


%package python3
Summary: python3 components for the pypi-sphinxcontrib_qthelp package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_qthelp)

%description python3
python3 components for the pypi-sphinxcontrib_qthelp package.


%prep
%setup -q -n sphinxcontrib-qthelp-1.0.3
cd %{_builddir}/sphinxcontrib-qthelp-1.0.3
pushd ..
cp -a sphinxcontrib-qthelp-1.0.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656370802
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_qthelp
cp %{_builddir}/sphinxcontrib-qthelp-1.0.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_qthelp/fc88bdd02ddfd29b245693fb34c3a9e6feee3dab
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinxcontrib_qthelp/fc88bdd02ddfd29b245693fb34c3a9e6feee3dab

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
