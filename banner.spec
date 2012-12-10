%define name banner
%define version 1.3.2
%define release %mkrel 5

Summary: Print text as banner on the console
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://cedar-solutions.com/ftp/software/%{name}-%{version}.tar.bz2
License: GPL
Group: Text tools
Url: http://www.cedar-solutions.com/software.html
BuildRoot: %{_tmppath}/%{name}-buildroot
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





%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-5mdv2011.0
+ Revision: 616708
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 1.3.2-4mdv2010.0
+ Revision: 424010
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.3.2-3mdv2009.0
+ Revision: 243161
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.3.2-1mdv2008.1
+ Revision: 135828
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Feb 27 2007 Olivier Thauvin <nanardon@mandriva.org> 1.3.2-1mdv2007.0
+ Revision: 126262
- 1.3.2

* Sat Aug 05 2006 Olivier Thauvin <nanardon@mandriva.org> 1.3.1-3mdv2007.0
+ Revision: 52861
- rebuild
- Import banner

* Wed Oct 05 2005 Olivier Thauvin <nanardon@mandriva.org> 1.3.1-2mdk
- rebuild

* Thu Jul 08 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.3.1-1mdk
- 1.3.1

