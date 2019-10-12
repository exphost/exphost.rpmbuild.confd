Name:           helloworld
Version:        1.0
Release:        1%{?dist}
Summary:        A hello world program

License:        GPLv3+
URL:            https://example.com
Source0:        helloworld-1.0.tar.gz

Requires(post): info
Requires(preun): info

%description
A helloworld program

%prep
%setup

%install
make PREFIX=/usr DESTDIR=%{?buildroot} install


%clean
rm -rf %{buildroot}

%files
%{_bindir}/helloworld.sh
