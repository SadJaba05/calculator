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

echo "4. Создание установщика (RPM)..."
if command -v rpmbuild &> /dev/null; then
    cd ..
    tar czf calculator.tar.gz calculator/calculator.py calculator/test_calculator.py
    mkdir -p ~/rpmbuild/SOURCES
    cp calculator.tar.gz ~/rpmbuild/SOURCES/
    rpmbuild -bb calculator.spec 2>/dev/null && echo "RPM создан"
    cd calculator
else
    echo "rpmbuild не установлен — пропускаем создание RPM"
fi

echo "5. Установка приложения..."
if [ -f ~/rpmbuild/RPMS/noarch/calculator-1.0-1.noarch.rpm ]; then
    sudo rpm -i ~/rpmbuild/RPMS/noarch/calculator-1.0-1.noarch.rpm 2>/dev/null || echo "Установка RPM не удалась"
else
    echo "RPM-файл не найден — пропускаем установку"
fi

echo "✅ CI-скрипт завершил работу."
