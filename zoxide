%define name zoxide
%define version 0.9.4
%define release 1%{?dist}

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
strip --strip-all %{buildroot}%{_bindir}/*
# Install manpages
mkdir -p %{buildroot}%{_mandir}/man1/

%install
install -Dpm 0644 man/man1/%{name}*.1 -t %{buildroot}%{_mandir}/man1/
# Install shell completions
install -Dpm 0644 contrib/completions/_%{name} -t %{buildroot}%{_datadir}/zsh/site-functions/
install -Dpm 0644 contrib/completions/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 0644 contrib/completions/%{name}.fish -t %{buildroot}/%{_datadir}/fish/vendor_completions.d/

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}
%{_mandir}/man1/*.1*
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions

# Copy the binary to /bin in the buildroot
install -m 755 target/release/zoxide %{buildroot}/bin/

# Copy Bash completion
install -m 755 gen/completions/zoxide.bash %{buildroot}/etc/bash_completion.d/

# Copy the man page to /usr/share/man/man1 in the buildroot
gzip gen/zoxide.1
install -m 644 gen/zoxide.1.gz %{buildroot}/usr/share/man/man1/

%files
# List all the files to be included in the package
/bin/zoxide
/etc/bash_completion.d/zoxide.bash
/usr/share/man/man1/zoxide.1.gz

%changelog
* Wed Feb 21 2024 Danie de Jager - 0.9.4
- Initial RPM build
