%define name zoxide
%define version 0.9.4
%define release 3%{?dist}

Summary:  Fast cd command that learns your habits
Name:     %{name}
Version:  %{version}
Release:  %{release}
License:  MIT License
URL:      https://github.com/ajeetdsouza/zoxide
Source0:  https://github.com/ajeetdsouza/zoxide/archive/refs/tags/v%{version}.tar.gz

%define debug_package %{nil}

BuildRequires: curl
BuildRequires: gcc
BuildRequires: make
BuildRequires: gzip

%description
zoxide is a blazing fast alternative to cd, inspired by z and z.lua. It keeps
track of the directories you use most frequently, and uses a ranking algorithm
to navigate to the best match.

%prep
%setup -q

%build
# Install Rust using curl
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$PATH:$HOME/.cargo/bin"
cargo build --release
strip --strip-all target/release/%{name}

%install
# Install manpages
mkdir -p %{buildroot}%{_mandir}/man1/
install -Dpm 0644 man/man1/%{name}*.1 -t %{buildroot}%{_mandir}/man1/
# Install shell completions
install -Dpm 0644 contrib/completions/_%{name} -t %{buildroot}%{_datadir}/zsh/site-functions/
install -Dpm 0644 contrib/completions/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 0644 contrib/completions/%{name}.fish -t %{buildroot}/%{_datadir}/fish/vendor_completions.d/

# Copy the binary to /bin in the buildroot
mkdir -p %{buildroot}%{_bindir}
install -m 755 target/release/%{name} %{buildroot}%{_bindir}

# Copy the man page to /usr/share/man/man1 in the buildroot
gzip man/man1/*.1
install -m 644 man/man1/*.1.gz %{buildroot}%{_mandir}/man1/

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man1/*.1.gz

%changelog
* Mon May 6 2024 Danie de Jager - 0.9.4-3
- Rebuild with rustc 1.77.2
* Wed Feb 21 2024 Danie de Jager - 0.9.4-2
- Cleanup SPEC file
* Wed Feb 21 2024 Danie de Jager - 0.9.4-1
- Initial RPM build
