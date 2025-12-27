Name: calculator
Version: 1.0
Release: 1
Summary: Simple calculator with GUI
License: MIT
Source0: calculator.tar.gz
BuildArch: noarch

%description
A Python calculator with Tkinter GUI.

%prep
%setup -q

%build
# No build for Python

%install
mkdir -p %{buildroot}/opt/calculator
cp calculator.py %{buildroot}/opt/calculator/
cp test_calculator.py %{buildroot}/opt/calculator/

%files
/opt/calculator/calculator.py
/opt/calculator/test_calculator.py
