%global tl_name simples-matrices
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	Define matrices by given list of values
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/simples-matrices
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simples-matrices.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simples-matrices.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simples-matrices.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Macros to define and write matrices whose coefficients are given row by
row in a list of values separated by commas.

