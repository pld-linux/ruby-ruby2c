Summary:	Translator from Ruby to C
Summary(pl.UTF-8):	Translator z języka Ruby na C
Name:		ruby-ruby2c
Version:	1.0.0.5
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/10428/RubyToC-%{version}.gem
# Source0-md5:	9667e19caa4e2d5f5c68a7706923f15f
URL:		http://ruby2c.rubyforge.org
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb >= 3.3.1
Requires:	ruby-parsetree
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ruby2c is a subset of the metaruby project, which aims at rewriting
ruby's internals in Ruby. ruby2c is the translation module and can
automatically translate a method into equivalent C code for a subset
of Ruby. Very BETA, but making rapid progress.

%description -l pl.UTF-8
ruby2c to podzbiór pojektu metaruby, którego celem jest przepisanie
wnętrzności interpretera ruby w języku Ruby. ruby2c to moduł
tłumaczenia, potrafiący automatycznie tłumaczyć metodę na
odpowiadający jej kod w C dla pozbioru języka Ruby. Zdecydowanie BETA,
ale postępy są szybkie.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%attr(755,root,root) %{_bindir}/ruby_to_c_show
%attr(755,root,root) %{_bindir}/ruby_to_c_validate
%{ruby_rubylibdir}/rewriter.rb
%{ruby_rubylibdir}/ruby_to_ansi_c.rb
%{ruby_rubylibdir}/ruby_to_ruby_c.rb
%{ruby_rubylibdir}/support.rb
%{ruby_rubylibdir}/type_checker.rb
%{ruby_rubylibdir}/typed_sexp_processor.rb
#%{ruby_ridir}/*
