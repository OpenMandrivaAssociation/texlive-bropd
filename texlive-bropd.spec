# revision 28222
# category Package
# catalog-ctan /macros/latex/contrib/bropd
# catalog-date 2012-11-09 11:55:25 +0100
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-bropd
Version:	1.1
Release:	8
Summary:	Simplified brackets and differentials in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bropd
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bropd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bropd.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bropd.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package simplifies the process of writing differential
operators and brackets in LaTeX. The commands facilitate the
easy manipulation of equations involving brackets and allow
partial differentials to be expressed in an alternate form.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bropd/bropd.sty
%doc %{_texmfdistdir}/doc/latex/bropd/README
%doc %{_texmfdistdir}/doc/latex/bropd/bropd.pdf
#- source
%doc %{_texmfdistdir}/source/latex/bropd/bropd.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
