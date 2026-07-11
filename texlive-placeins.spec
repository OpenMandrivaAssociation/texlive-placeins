%global tl_name placeins
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Control float placement
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/placeins
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/placeins.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/placeins.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines a \FloatBarrier command, beyond which floats may not pass;
useful, for example, to ensure all floats for a section appear before
the next \section command.

