# UAS SPK MODEL
# Arif Cahya Dito
# 201011401744
# 07TPLP013

## Virtualenv

install, create, activate virtual environment using virtualenv

https://medium.com/analytics-vidhya/virtual-environment-6ad5d9b6af59

## Install depedencies

run `pip install -r requirements.txt`

## create postgresql database

create database in your locals

modify settings.py

## create table

run:

    python main.py create_table

## create data

run this query in your db client

INSERT INTO `hitung_smartphone` (`id`, `brand`, `ram_gb`, `storage_gb`, `processor`, `battery`, `harga`) VALUES  (1, 'Samsung Galaxy A01', '2', '16', 'Qualcomm Snapdragon 439', '3000', '1499000'), (2, 'Samsung Galaxy M01', '3', '32', 'Qualcomm Snapdragon 439', '4000', '1999000'), (3, 'Xiaomi Redmi 9C', '3', '64', 'Mediatek Helio G35', '5000', '1899000'), (4, 'Xiaomi Redmi 9', '3', '32', 'Mediatek Helio G80', '5020', '1799000'), (5, 'Realme C11', '2', '32', 'Mediatek Helio G35', '5000', '1499000'), (6, 'Realme C21', '3', '32', 'Mediatek Helio G35', '5000', '1699000'),(7, 'Oppo A15', '3', '32', 'Mediatek Helio P35', '4230', '1699000'), (8, 'Oppo A53', '4', '64', 'Qualcomm Snapdragon 460', '5000', '2299000'), (9, 'Vivo Y12s', '3', '32', 'Mediatek Helio P35', '5000', '1699000'), (10, 'Vivo Y20', '4', '64', 'Qualcomm Snapdragon 460', '5000', '2099000');

## run SAW

     python main.py saw

## run WP

    python main.py wp

lalu implementasikan di data kalian masing-masing

## Output SAW dan WP
![image](https://github.com/MyDito/UAS_SPK_MODEL/assets/112084539/3924a413-62d7-46c9-8bba-1f212a82f932)

