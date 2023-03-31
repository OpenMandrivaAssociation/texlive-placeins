Name:		texlive-placeins
Version:	19848
Release:	2
Summary:	Control float placement
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/placeins
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/placeins.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/placeins.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines a \FloatBarrier command, beyond which floats may not
pass; useful, for example, to ensure all floats for a section
appear before the next \section command.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/placeins/placeins.sty
%doc %{_texmfdistdir}/doc/latex/placeins/placeins-doc.pdf
%doc %{_texmfdistdir}/doc/latex/placeins/placeins-doc.tex
%doc %{_texmfdistdir}/doc/latex/placeins/placeins.txt

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
