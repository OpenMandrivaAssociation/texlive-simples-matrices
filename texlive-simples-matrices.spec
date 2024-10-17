Name:		texlive-simples-matrices
Version:	63802
Release:	2
Summary:	Define matrices by given list of values
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/simples-matrices
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simples-matrices.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simples-matrices.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simples-matrices.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Macros to define and write matrices whose coefficients are
given row by row in a list of values separated by commas.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/simples-matrices
%{_texmfdistdir}/tex/latex/simples-matrices
%doc %{_texmfdistdir}/doc/latex/simples-matrices

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
