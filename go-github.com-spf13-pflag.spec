#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : go-github.com-spf13-pflag
Version  : v1.0.3
Release  : 1
URL      : https://proxy.golang.org/github.com/spf13/pflag/@v/list
Source0  : https://proxy.golang.org/github.com/spf13/pflag/@v/list
Source1  : https://proxy.golang.org/github.com/spf13/pflag/@v/v1.0.3.info
Source2  : https://proxy.golang.org/github.com/spf13/pflag/@v/v1.0.3.mod
Source3  : https://proxy.golang.org/github.com/spf13/pflag/@v/v1.0.3.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: go-github.com-spf13-pflag-data = %{version}-%{release}
BuildRequires : buildreq-golang

%description
[![Build Status](https://travis-ci.org/spf13/pflag.svg?branch=master)](https://travis-ci.org/spf13/pflag)
[![Go Report Card](https://goreportcard.com/badge/github.com/spf13/pflag)](https://goreportcard.com/report/github.com/spf13/pflag)
[![GoDoc](https://godoc.org/github.com/spf13/pflag?status.svg)](https://godoc.org/github.com/spf13/pflag)

%package data
Summary: data components for the go-github.com-spf13-pflag package.
Group: Data

%description data
data components for the go-github.com-spf13-pflag package.


%prep

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}/usr/share/goproxy/github.com/spf13/pflag/@v
# Create list file using packaged versions
echo v1.0.3 >> %{buildroot}/usr/share/goproxy/github.com/spf13/pflag/@v/list
install -m 0644 %{SOURCE1} %{buildroot}/usr/share/goproxy/github.com/spf13/pflag/@v/v1.0.3.info
install -m 0644 %{SOURCE2} %{buildroot}/usr/share/goproxy/github.com/spf13/pflag/@v/v1.0.3.mod
install -m 0644 %{SOURCE3} %{buildroot}/usr/share/goproxy/github.com/spf13/pflag/@v/v1.0.3.zip


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/goproxy/github.com/spf13/pflag/@v/list
/usr/share/goproxy/github.com/spf13/pflag/@v/v1.0.3.info
/usr/share/goproxy/github.com/spf13/pflag/@v/v1.0.3.mod
/usr/share/goproxy/github.com/spf13/pflag/@v/v1.0.3.zip
