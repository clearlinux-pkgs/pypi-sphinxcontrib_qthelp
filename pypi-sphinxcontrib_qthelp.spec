#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-sphinxcontrib_qthelp
Version  : 1.0.6
Release  : 39
URL      : https://files.pythonhosted.org/packages/4f/a2/53129fc967ac8402d5e4e83e23c959c3f7a07362ec154bdb2e197d8cc270/sphinxcontrib_qthelp-1.0.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/4f/a2/53129fc967ac8402d5e4e83e23c959c3f7a07362ec154bdb2e197d8cc270/sphinxcontrib_qthelp-1.0.6.tar.gz
Summary  : sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp documents
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-sphinxcontrib_qthelp-license = %{version}-%{release}
Requires: pypi-sphinxcontrib_qthelp-python = %{version}-%{release}
Requires: pypi-sphinxcontrib_qthelp-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
====================
sphinxcontrib-qthelp
====================
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
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-sphinxcontrib_qthelp package.


%prep
%setup -q -n sphinxcontrib_qthelp-1.0.6
cd %{_builddir}/sphinxcontrib_qthelp-1.0.6
pushd ..
cp -a sphinxcontrib_qthelp-1.0.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692059795
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_qthelp
cp %{_builddir}/sphinxcontrib_qthelp-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_qthelp/fc88bdd02ddfd29b245693fb34c3a9e6feee3dab || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
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
