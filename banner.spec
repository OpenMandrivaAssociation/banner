%define name banner
%define version 1.3.2
%define release %mkrel 1

Summary: Print text as banner on the console
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://cedar-solutions.com/ftp/software/%{name}-%{version}.tar.bz2
License: GPL
Group: Text tools
Url: http://www.cedar-solutions.com/software.html
BuildRequires: automake

%description
Banner fills an apparent hole in Linux - that is, that is does not provide 
a "banner" program itself, while nearly all UNIX systems seem to do so.
Banner prints a "banner" on the screen that corresponds to the first 10 
characters of a string entered on the command line, in a way similar to
what you might see when using Solaris or AIX. There are fancier things out 
there, but this is nice and simple. 

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL README
%_bindir/banner



