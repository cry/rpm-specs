Name:           vim 
Version:        8.1.0303
Release:        1%{?dist}
Summary:        Vi IMproved

License:        Charityware
URL:            https://github.com/vim/vim
Source0:        https://github.com/vim/vim/archive/v8.1.0303.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby ruby-devel lua lua-devel luajit luajit-devel ctags git python python-devel python36 python36-devel tcl-devel perl perl-devel perl-ExtUtils-ParseXS perl-ExtUtils-XSpp perl-ExtUtils-CBuilder perl-ExtUtils-Embed ncurses-devel

# TODO: Figure out what vim actually requires
#Requires:       

%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-enhanced package contains a version of VIM with extra, recently
introduced features like Python and Perl interpreters.

%prep
%setup -q


%build
%define _prefix /usr/local
%configure --with-features=huge --enable-multibyte --enable-rubyinterp=dynamic --enable-pythoninterp=dynamic --enable-python3interp=dynamic --enable-perlinterp=dynamic --enable-luainterp=dynamic --enable-cscope --with-python3-config-dir=/usr/lib64/python3.6/config-3.6m-x86_64-linux-gnu --with-python3-command=python36
--with-python-config-dir=/usr/lib64/python2.7/config --with-compiledby=hello@carey.li
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT VIMRUNTIMEDIR=/usr/local/share/vim/vim81


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/usr


%changelog
