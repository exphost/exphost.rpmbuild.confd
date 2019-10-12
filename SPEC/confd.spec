Name:           confd
Version:        0.16.0

%define build_timestamp %(date +"%Y%m%d")
Release:        %{build_timestamp}
Summary:        Confd
%undefine _disable_source_fetch

License:        MIT License
URL:            https://github.com/kelseyhightower/confd
Source0:        https://github.com/kelseyhightower/confd/releases/download/v%{?version}/confd-%{?version}-linux-amd64

%description
Confd

%prep

%install
install -d %{?buildroot}/usr/bin
cp confd-%{version}-linux-amd64 %{?buildroot}/usr/bin/confd


%clean
rm -rf %{buildroot}

%files
%attr(0755, root, root) /usr/bin/confd
