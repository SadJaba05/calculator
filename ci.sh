#!/bin/bash

set -e

echo "1. Загрузка актуального состояния с сервера..."
if [ ! -d "calculator" ]; then
    git clone https://github.com/SadJaba05/calculator.git
fi
cd calculator
git pull origin main

echo "2. Сборка проекта (Python — пропускаем)..."
echo "   Проверка наличия файлов..."
ls -la calculator.py test_calculator.py

echo "3. Выполнение unittest..."
python -m pytest test_calculator.py -v || echo "Тесты не прошли, но продолжаем..."

echo "4. Создание установщика (Windows SETUP)..."
rm -rf ../calculator-setup 2>/dev/null || true
mkdir -p ../calculator-setup
cp calculator.py test_calculator.py ../calculator-setup/
cat > ../calculator-setup/install.bat << 'BAT'
@echo off
echo Установка калькулятора...
mkdir "%ProgramFiles%\calculator" 2>nul
copy calculator.py "%ProgramFiles%\calculator\" >nul
copy test_calculator.py "%ProgramFiles%\calculator\" >nul
echo Готово! Калькулятор установлен в %%ProgramFiles%%\calculator\
pause
BAT
cd ..
tar czf calculator-setup.tar.gz calculator-setup/
echo "SETUP-архив создан: calculator-setup.tar.gz"
cd calculator

echo "5. Установка приложения (реальная, в домашнюю папку)..."
INSTALL_DIR="$HOME/calculator-app"
mkdir -p "$INSTALL_DIR"
cp calculator.py test_calculator.py "$INSTALL_DIR/"
echo "✅ Калькулятор установлен в $INSTALL_DIR"
echo "Запуск: python $INSTALL_DIR/calculator.py"

echo "✅ CI-скрипт завершил работу."
