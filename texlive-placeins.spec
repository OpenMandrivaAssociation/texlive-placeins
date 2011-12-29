# revision 19848
# category Package
# catalog-ctan /macros/latex/contrib/placeins
# catalog-date 2010-09-22 15:00:44 +0200
# catalog-license pd
# catalog-version 2.2
Name:		texlive-placeins
Version:	2.2
Release:	1
Summary:	Control float placement
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/placeins
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/placeins.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/placeins.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
