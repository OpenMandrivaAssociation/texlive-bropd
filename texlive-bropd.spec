Name:		texlive-bropd
Version:	35383
Release:	1
Summary:	Simplified brackets and differentials in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bropd
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bropd.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bropd.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bropd.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
