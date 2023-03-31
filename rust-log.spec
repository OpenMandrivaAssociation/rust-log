# make check seems to be broken because of missing files in the upstream crate:
# error: couldn't read tests/macros.rs: No such file or directory (os error 2)
# error: aborting due to previous error
# error: couldn't read tests/filters.rs: No such file or directory (os error 2)
# error: aborting due to previous error
# error: could not compile `log`
%bcond_with check
%global debug_package %{nil}

%global crate log

Name:           rust-%{crate}
Version:        0.4.14
Release:        2
Summary:        Lightweight logging facade for Rust

# Upstream license specification: MIT OR Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/log
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(cfg-if/default) >= 1.0.0 with crate(cfg-if/default) < 2.0.0)
%if %{with check}
BuildRequires:  (crate(serde/default) >= 1.0.0 with crate(serde/default) < 2.0.0)
BuildRequires:  (crate(serde/derive) >= 1.0.0 with crate(serde/derive) < 2.0.0)
BuildRequires:  (crate(serde_test/default) >= 1.0.0 with crate(serde_test/default) < 2.0.0)
BuildRequires:  (crate(sval/default) >= 1.0.0~alpha.5 with crate(sval/default) < 2.0.0)
BuildRequires:  (crate(sval/derive) >= 1.0.0~alpha.5 with crate(sval/derive) < 2.0.0)
BuildRequires:  (crate(value-bag/default) >= 1.0.0~alpha.6 with crate(value-bag/default) < 2.0.0)
BuildRequires:  (crate(value-bag/test) >= 1.0.0~alpha.6 with crate(value-bag/test) < 2.0.0)
%endif
%endif

%global _description %{expand:
Lightweight logging facade for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log) = 0.4.14
Requires:       cargo
Requires:       (crate(cfg-if/default) >= 1.0.0 with crate(cfg-if/default) < 2.0.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/default) = 0.4.14
Requires:       cargo
Requires:       crate(log) = 0.4.14

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+kv_unstable-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/kv_unstable) = 0.4.14
Requires:       cargo
Requires:       (crate(value-bag) >= 1.0.0~alpha.6 with crate(value-bag) < 2.0.0)
Requires:       crate(log) = 0.4.14

%description -n %{name}+kv_unstable-devel %{_description}

This package contains library source intended for building other packages
which use "kv_unstable" feature of "%{crate}" crate.

%files       -n %{name}+kv_unstable-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+kv_unstable_serde-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/kv_unstable_serde) = 0.4.14
Requires:       cargo
Requires:       (crate(serde) >= 1.0.0 with crate(serde) < 2.0.0)
Requires:       (crate(value-bag/serde) >= 1.0.0~alpha.6 with crate(value-bag/serde) < 2.0.0)
Requires:       crate(log) = 0.4.14
Requires:       crate(log/kv_unstable_std) = 0.4.14

%description -n %{name}+kv_unstable_serde-devel %{_description}

This package contains library source intended for building other packages
which use "kv_unstable_serde" feature of "%{crate}" crate.

%files       -n %{name}+kv_unstable_serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+kv_unstable_std-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/kv_unstable_std) = 0.4.14
Requires:       cargo
Requires:       (crate(value-bag/error) >= 1.0.0~alpha.6 with crate(value-bag/error) < 2.0.0)
Requires:       crate(log) = 0.4.14
Requires:       crate(log/kv_unstable) = 0.4.14
Requires:       crate(log/std) = 0.4.14

%description -n %{name}+kv_unstable_std-devel %{_description}

This package contains library source intended for building other packages
which use "kv_unstable_std" feature of "%{crate}" crate.

%files       -n %{name}+kv_unstable_std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+kv_unstable_sval-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/kv_unstable_sval) = 0.4.14
Requires:       cargo
Requires:       (crate(sval) >= 1.0.0~alpha.5 with crate(sval) < 2.0.0)
Requires:       (crate(value-bag/sval) >= 1.0.0~alpha.6 with crate(value-bag/sval) < 2.0.0)
Requires:       crate(log) = 0.4.14
Requires:       crate(log/kv_unstable) = 0.4.14

%description -n %{name}+kv_unstable_sval-devel %{_description}

This package contains library source intended for building other packages
which use "kv_unstable_sval" feature of "%{crate}" crate.

%files       -n %{name}+kv_unstable_sval-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+max_level_debug-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/max_level_debug) = 0.4.14
Requires:       cargo
Requires:       crate(log) = 0.4.14

%description -n %{name}+max_level_debug-devel %{_description}

This package contains library source intended for building other packages
which use "max_level_debug" feature of "%{crate}" crate.

%files       -n %{name}+max_level_debug-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+max_level_error-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/max_level_error) = 0.4.14
Requires:       cargo
Requires:       crate(log) = 0.4.14

%description -n %{name}+max_level_error-devel %{_description}

This package contains library source intended for building other packages
which use "max_level_error" feature of "%{crate}" crate.

%files       -n %{name}+max_level_error-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+max_level_info-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/max_level_info) = 0.4.14
Requires:       cargo
Requires:       crate(log) = 0.4.14

%description -n %{name}+max_level_info-devel %{_description}

This package contains library source intended for building other packages
which use "max_level_info" feature of "%{crate}" crate.

%files       -n %{name}+max_level_info-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+max_level_off-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/max_level_off) = 0.4.14
Requires:       cargo
Requires:       crate(log) = 0.4.14

%description -n %{name}+max_level_off-devel %{_description}

This package contains library source intended for building other packages
which use "max_level_off" feature of "%{crate}" crate.

%files       -n %{name}+max_level_off-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+max_level_trace-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/max_level_trace) = 0.4.14
Requires:       cargo
Requires:       crate(log) = 0.4.14

%description -n %{name}+max_level_trace-devel %{_description}

This package contains library source intended for building other packages
which use "max_level_trace" feature of "%{crate}" crate.

%files       -n %{name}+max_level_trace-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+max_level_warn-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/max_level_warn) = 0.4.14
Requires:       cargo
Requires:       crate(log) = 0.4.14

%description -n %{name}+max_level_warn-devel %{_description}

This package contains library source intended for building other packages
which use "max_level_warn" feature of "%{crate}" crate.

%files       -n %{name}+max_level_warn-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+release_max_level_debug-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/release_max_level_debug) = 0.4.14
Requires:       cargo
Requires:       crate(log) = 0.4.14

%description -n %{name}+release_max_level_debug-devel %{_description}

This package contains library source intended for building other packages
which use "release_max_level_debug" feature of "%{crate}" crate.

%files       -n %{name}+release_max_level_debug-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+release_max_level_error-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/release_max_level_error) = 0.4.14
Requires:       cargo
Requires:       crate(log) = 0.4.14

%description -n %{name}+release_max_level_error-devel %{_description}

This package contains library source intended for building other packages
which use "release_max_level_error" feature of "%{crate}" crate.

%files       -n %{name}+release_max_level_error-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+release_max_level_info-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/release_max_level_info) = 0.4.14
Requires:       cargo
Requires:       crate(log) = 0.4.14

%description -n %{name}+release_max_level_info-devel %{_description}

This package contains library source intended for building other packages
which use "release_max_level_info" feature of "%{crate}" crate.

%files       -n %{name}+release_max_level_info-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+release_max_level_off-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/release_max_level_off) = 0.4.14
Requires:       cargo
Requires:       crate(log) = 0.4.14

%description -n %{name}+release_max_level_off-devel %{_description}

This package contains library source intended for building other packages
which use "release_max_level_off" feature of "%{crate}" crate.

%files       -n %{name}+release_max_level_off-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+release_max_level_trace-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/release_max_level_trace) = 0.4.14
Requires:       cargo
Requires:       crate(log) = 0.4.14

%description -n %{name}+release_max_level_trace-devel %{_description}

This package contains library source intended for building other packages
which use "release_max_level_trace" feature of "%{crate}" crate.

%files       -n %{name}+release_max_level_trace-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+release_max_level_warn-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/release_max_level_warn) = 0.4.14
Requires:       cargo
Requires:       crate(log) = 0.4.14

%description -n %{name}+release_max_level_warn-devel %{_description}

This package contains library source intended for building other packages
which use "release_max_level_warn" feature of "%{crate}" crate.

%files       -n %{name}+release_max_level_warn-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/serde) = 0.4.14
Requires:       cargo
Requires:       (crate(serde) >= 1.0.0 with crate(serde) < 2.0.0)
Requires:       crate(log) = 0.4.14

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/std) = 0.4.14
Requires:       cargo
Requires:       crate(log) = 0.4.14

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sval-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/sval) = 0.4.14
Requires:       cargo
Requires:       (crate(sval) >= 1.0.0~alpha.5 with crate(sval) < 2.0.0)
Requires:       crate(log) = 0.4.14

%description -n %{name}+sval-devel %{_description}

This package contains library source intended for building other packages
which use "sval" feature of "%{crate}" crate.

%files       -n %{name}+sval-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+value-bag-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(log/value-bag) = 0.4.14
Requires:       cargo
Requires:       (crate(value-bag) >= 1.0.0~alpha.6 with crate(value-bag) < 2.0.0)
Requires:       crate(log) = 0.4.14

%description -n %{name}+value-bag-devel %{_description}

This package contains library source intended for building other packages
which use "value-bag" feature of "%{crate}" crate.

%files       -n %{name}+value-bag-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
