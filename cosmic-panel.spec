%undefine _debugsource_packages

Name:           cosmic-panel
Version:        1.0.0
Release:        0.alpha4.0
Summary:        A panel for COSMIC DE
Group:          Desktop/COSMIC
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-panel
Source0:        https://github.com/pop-os/cosmic-panel/archive/epoch-%{version}-alpha.4/%{name}-epoch-%{version}-alpha.4.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%prep
%autosetup -n %{name}-epoch-%{version}-alpha.4 -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/cosmic
